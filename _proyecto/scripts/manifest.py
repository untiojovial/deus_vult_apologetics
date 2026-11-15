#!/usr/bin/env python3
"""Manifiesto y verificacion de integridad del contenido protegido.

Uso:
  python _proyecto/scripts/manifest.py build    # genera manifiesto desde el commit base (solo la 1a vez)
  python _proyecto/scripts/manifest.py verify   # comprueba que nada protegido ha cambiado
  python _proyecto/scripts/manifest.py extract <dir>  # vuelca texto plano de cada dossier a <dir>

El manifiesto se calcula sobre los BLOBS del commit base (BASE_COMMIT), no sobre el
arbol de trabajo, de modo que es reproducible e independiente de finales de linea.
"""
import hashlib, json, os, re, subprocess, sys, html

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
PROY = os.path.join(ROOT, "_proyecto")
BASE_COMMIT = "75cafb8"  # ultimo commit del propietario antes del proyecto

STRICT_PREFIXES = ("static/refutaciones/",)          # dossieres HTML: intocables
STRICT_CONTENT = re.compile(r"^content/.+/(?!_index\.md$)[^/]+\.md$")  # envoltorios y articulos
ADDITIVE = re.compile(r"^(content/(.+/)?_index\.md|content/search\.md|hugo\.toml|assets/.+|layouts/.+|archetypes/.+)$")


def git(*args, binary=False):
    out = subprocess.run(["git", "-C", ROOT, *args], capture_output=True, check=True).stdout
    return out if binary else out.decode("utf-8", "replace")


def blobs(commit, paths):
    """Devuelve {path: bytes} leyendo todos los blobs con un unico proceso git cat-file --batch."""
    inp = "".join(f"{commit}:{p}\n" for p in paths).encode("utf-8")
    out = subprocess.run(["git", "-C", ROOT, "cat-file", "--batch"], input=inp, capture_output=True, check=True).stdout
    res, i = {}, 0
    for p in paths:
        nl = out.index(b"\n", i)
        header = out[i:nl].split()
        if header[-1] == b"missing":
            res[p] = None
            i = nl + 1
            continue
        size = int(header[2])
        res[p] = out[nl + 1: nl + 1 + size]
        i = nl + 1 + size + 1
    return res


def tree(commit):
    """{path: blob_sha1} de un commit."""
    res = {}
    for line in git("ls-tree", "-r", commit).splitlines():
        meta, path = line.split("\t", 1)
        res[path] = meta.split()[2]
    return res


def classify(path):
    if path.startswith(STRICT_PREFIXES) or STRICT_CONTENT.match(path):
        return "ESTRICTO"
    if ADDITIVE.match(path):
        return "ADITIVO"
    return None


def plain_text(raw):
    s = raw.decode("utf-8", "replace")
    s = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", s, flags=re.S | re.I)
    s = re.sub(r"<br\s*/?>|</(p|div|li|h[1-6]|tr|section|blockquote)>", "\n", s, flags=re.I)
    s = re.sub(r"<[^>]+>", " ", s)
    s = html.unescape(s)
    s = re.sub(r"[ \t\r\f\v]+", " ", s)
    s = re.sub(r"\n\s*\n+", "\n", s)
    return s.strip()


def base_files():
    return [p for p in git("ls-tree", "-r", "--name-only", BASE_COMMIT).splitlines() if classify(p)]


def build():
    entries = []
    files = base_files()
    data = blobs(BASE_COMMIT, files)
    for p in files:
        raw = data[p]
        e = {
            "path": p,
            "proteccion": classify(p),
            "sha256": hashlib.sha256(raw).hexdigest(),
            "bytes": len(raw),
        }
        if p.endswith(".html"):
            s = raw.decode("utf-8", "replace")
            m = re.search(r"<title>(.*?)</title>", s, re.S)
            e["titulo_html"] = html.unescape(m.group(1).strip()) if m else None
            e["palabras"] = len(plain_text(raw).split())
        elif p.endswith(".md"):
            s = raw.decode("utf-8", "replace")
            m = re.search(r'^title:\s*"?(.*?)"?\s*$', s, re.M)
            e["titulo"] = m.group(1) if m else None
            m = re.search(r'^url:\s*"?(.*?)"?\s*$', s, re.M)
            e["url"] = m.group(1) if m else None
            m = re.search(r'dossier_iframe src="([^"]+)"', s)
            e["dossier_html"] = m.group(1) if m else None
        entries.append(e)
    os.makedirs(PROY, exist_ok=True)
    manifest = {"base_commit": git("rev-parse", BASE_COMMIT).strip(), "total": len(entries), "archivos": entries}
    with open(os.path.join(PROY, "EXISTING_CONTENT_MANIFEST.json"), "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=1)
    prot = {
        "base_commit": manifest["base_commit"],
        "reglas": {
            "ESTRICTO": "No modificar ni un byte. Dossieres HTML, sus envoltorios .md y articulos existentes.",
            "ADITIVO": "Puede evolucionar para el rediseno general (indices, plantillas, CSS, config), sin renombrar apartados ni romper rutas.",
        },
        "ESTRICTO": {e["path"]: e["sha256"] for e in entries if e["proteccion"] == "ESTRICTO"},
        "ADITIVO": [e["path"] for e in entries if e["proteccion"] == "ADITIVO"],
    }
    with open(os.path.join(PROY, "PROTECTED_FILES.json"), "w", encoding="utf-8") as f:
        json.dump(prot, f, ensure_ascii=False, indent=1)
    print(f"manifiesto: {len(entries)} archivos; estrictos: {len(prot['ESTRICTO'])}; aditivos: {len(prot['ADITIVO'])}")


def verify():
    with open(os.path.join(PROY, "PROTECTED_FILES.json"), encoding="utf-8") as f:
        prot = json.load(f)
    bad = []
    # 1) el arbol de trabajo no difiere del commit base en ningun archivo estricto (git normaliza EOL)
    diff = git("diff", "--name-status", prot["base_commit"], "--", *sorted(prot["ESTRICTO"]))
    for line in diff.splitlines():
        bad.append("MODIFICADO/ELIMINADO (arbol de trabajo): " + line)
    # 2) los blobs en HEAD son identicos a los del commit base (mismo sha1 de blob => mismo contenido)
    base_t, head_t = tree(prot["base_commit"]), tree("HEAD")
    for p in prot["ESTRICTO"]:
        if p not in head_t:
            bad.append("AUSENTE EN HEAD: " + p)
        elif head_t[p] != base_t[p]:
            bad.append("CONTENIDO DISTINTO EN HEAD: " + p)
    # 3) comprobacion fuerte sha256 del contenido en HEAD
    data = blobs("HEAD", sorted(prot["ESTRICTO"]))
    for p, sha in prot["ESTRICTO"].items():
        if data.get(p) is not None and hashlib.sha256(data[p]).hexdigest() != sha:
            bad.append("SHA256 DISTINTO EN HEAD: " + p)
    if bad:
        print("FALLO DE INTEGRIDAD:")
        for b in bad:
            print("  -", b)
        sys.exit(1)
    print(f"OK: {len(prot['ESTRICTO'])} archivos protegidos intactos respecto a {prot['base_commit'][:7]}")


def extract(outdir):
    os.makedirs(outdir, exist_ok=True)
    n = 0
    files = [p for p in base_files() if p.startswith("static/refutaciones/") and p.endswith(".html")]
    data = blobs(BASE_COMMIT, files)
    for p in files:
        if True:
            raw = data[p]
            with open(os.path.join(outdir, os.path.basename(p)[:-5] + ".txt"), "w", encoding="utf-8") as f:
                f.write(plain_text(raw))
            n += 1
    print(f"{n} textos extraidos en {outdir}")


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "verify"
    if cmd == "build":
        build()
    elif cmd == "verify":
        verify()
    elif cmd == "extract":
        extract(sys.argv[2])
    else:
        sys.exit(__doc__)
