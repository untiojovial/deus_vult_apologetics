#!/usr/bin/env python3
"""Lee el TEXTO LITERAL de una página o PDF público y lo guarda como copia de trabajo para verificar citas.
(Autorizado por el propietario el 2026-11-15: lectura con curl de fuentes públicas, sin instalar nada.)

  python _proyecto/scripts/leer_fuente.py <URL> <carpeta_del_dossier> [--buscar "texto"] [--max 6000]

- Descarga con curl (agente genérico, sin datos personales), convierte HTML a texto plano (o PDF con pdftotext
  si está disponible) y guarda `fuentes_raw/<nombre>.txt` con la URL y la fecha en la cabecera.
- Con --buscar muestra los pasajes que contienen ese texto (sin distinguir mayúsculas ni acentos), con contexto.
- Sin --buscar muestra el principio del texto (hasta --max caracteres).
No sigue enlaces, no envía formularios, no usa credenciales. Si el sitio bloquea (403, captcha), no insistas.
"""
import datetime, hashlib, html, os, re, subprocess, sys, unicodedata


def nrm(s):
    return "".join(c for c in unicodedata.normalize("NFD", s.lower()) if unicodedata.category(c) != "Mn")


def main():
    a = sys.argv[1:]
    if len(a) < 2:
        sys.exit(__doc__)
    url, carpeta = a[0], a[1]
    buscar = a[a.index("--buscar") + 1] if "--buscar" in a else None
    mx = int(a[a.index("--max") + 1]) if "--max" in a else 6000
    if not re.match(r"^https?://", url):
        sys.exit("Solo URL http(s).")
    raw_dir = os.path.join(carpeta, "fuentes_raw")
    os.makedirs(raw_dir, exist_ok=True)
    base = re.sub(r"[^a-zA-Z0-9]+", "-", re.sub(r"^https?://(www\.)?", "", url))[:70].strip("-") + "-" + hashlib.md5(url.encode()).hexdigest()[:6]
    tmp = os.path.join(raw_dir, base + ".bin")
    r = subprocess.run(["curl", "-sL", "--max-time", "60", "--max-filesize", "40000000", "-A", "Mozilla/5.0 (compatible; lector-de-fuentes)",
                        "-w", "%{http_code} %{content_type}", "-o", tmp, url], capture_output=True, text=True)
    info = r.stdout.strip()
    code = info.split(" ")[0] if info else "?"
    if code != "200" or not os.path.exists(tmp):
        if os.path.exists(tmp):
            os.remove(tmp)
        sys.exit(f"No se pudo leer ({info or r.stderr.strip()}). Marca la fuente como no verificada.")
    data = open(tmp, "rb").read()
    if data[:5] == b"%PDF-":
        pdf = os.path.join(raw_dir, base + ".pdf")
        os.replace(tmp, pdf)
        try:
            txt = subprocess.run(["pdftotext", "-layout", "-enc", "UTF-8", pdf, "-"], capture_output=True).stdout.decode("utf-8", "replace")
        except FileNotFoundError:
            sys.exit("PDF guardado en " + pdf + " pero pdftotext no está disponible.")
        os.remove(pdf)
    else:
        m = re.search(rb"charset=[\"']?([\w-]+)", data[:3000])
        enc = m.group(1).decode() if m else "utf-8"
        try:
            s = data.decode(enc, "replace")
        except LookupError:
            s = data.decode("utf-8", "replace")
        os.remove(tmp)
        s = re.sub(r"<(script|style|noscript)[^>]*>.*?</\1>", " ", s, flags=re.S | re.I)
        s = re.sub(r"<br\s*/?>|</(p|div|li|h[1-6]|tr|td|blockquote)>", "\n", s, flags=re.I)
        txt = html.unescape(re.sub(r"<[^>]+>", " ", s))
    txt = re.sub(r"[ \t\r\f\v]+", " ", txt)
    txt = re.sub(r"\n\s*\n+", "\n", txt).strip()
    out = os.path.join(raw_dir, base + ".txt")
    with open(out, "w", encoding="utf-8", newline="\n") as f:
        f.write(f"# URL: {url}\n# Consultado: {datetime.date.today().isoformat()}\n# Caracteres: {len(txt)}\n\n{txt}\n")
    print(f"[guardado] {out} ({len(txt)} caracteres)")
    if len(txt) < 400:
        print("[aviso] Texto muy corto: puede ser una página que requiere JavaScript o un bloqueo.")
    if buscar:
        n, q, hits = nrm(txt), nrm(buscar), 0
        i = n.find(q)
        while i != -1 and hits < 6:
            print(f"\n--- coincidencia {hits + 1} (posición {i}) ---\n" + txt[max(0, i - 500): i + len(buscar) + 900])
            hits += 1
            i = n.find(q, i + len(q))
        if not hits:
            print(f"\n[sin coincidencias para «{buscar}»]")
    else:
        print("\n" + txt[:mx])


if __name__ == "__main__":
    main()
