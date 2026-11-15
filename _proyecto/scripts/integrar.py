#!/usr/bin/env python3
"""Integra en el sitio un dossier nuevo ya aprobado por el director.

  python _proyecto/scripts/integrar.py D17 [D26 ...]      # integra
  python _proyecto/scripts/integrar.py --lista            # estado de los 50

Por cada dossier:
  1. reconstruye el HTML desde dossieres/Dxx-slug/ (partes o borrador.md) con build_dossier.py;
  2. copia el HTML a static/refutaciones/<slug>.html (se niega a pisar un archivo protegido);
  3. crea content/<apartado>/<slug>-dossier.md con el mismo formato de envoltorio que los dossieres antiguos;
  4. añade su enlace al final de content/<apartado>/_index.md (archivo ADITIVO; idempotente);
  5. marca el dossier como INTEGRADO en DOSSIER_REGISTRY.json.
Solo integra dossieres en estado APROBACION_EDITORIAL (o con --forzar para pruebas técnicas).
"""
import json, os, shutil, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
PROY = os.path.join(ROOT, "_proyecto")
sys.path.insert(0, HERE)
import build_dossier  # noqa: E402

ORDEN = ["CANDIDATO", "APROBADO", "INVESTIGANDO", "FUENTES_VERIFICADAS", "BORRADOR", "REVISION_ADVERSARIAL",
         "CORRECCIONES", "APROBACION_EDITORIAL", "INTEGRADO", "VERIFICADO"]


def load(name):
    return json.load(open(os.path.join(PROY, name), encoding="utf-8"))


def integrar(did, reg, prot, forzar):
    d = next((x for x in reg["dossieres"] if x["id"] == did), None)
    if not d:
        sys.exit(f"{did}: no existe en DOSSIER_REGISTRY.json")
    if d["estado"] not in ("APROBACION_EDITORIAL", "INTEGRADO", "VERIFICADO") and not forzar:
        sys.exit(f"{did}: estado {d['estado']}; solo se integran dossieres con APROBACION_EDITORIAL")
    folder = os.path.join(PROY, d["carpeta"].replace("/", os.sep))
    src = folder if os.path.isdir(os.path.join(folder, "partes")) else os.path.join(folder, "borrador.md")
    rep = build_dossier.build(src)
    serios = [a for a in rep["avisos"] if "no verificada" not in a]
    if serios and not forzar:
        sys.exit(f"{did}: avisos del constructor sin resolver: {serios}")
    slug, apartado = d["slug"], d["apartado"]
    html_rel = f"static/refutaciones/{slug}.html"
    md_rel = f"content/{apartado}/{slug}-dossier.md"
    for rel in (html_rel, md_rel):
        if rel in prot["ESTRICTO"]:
            sys.exit(f"{did}: {rel} es un archivo PROTEGIDO; cambia el slug")
    shutil.copyfile(rep["salida"], os.path.join(ROOT, html_rel.replace("/", os.sep)))
    meta = build_dossier.parse_front(open(os.path.join(folder, "borrador.md"), encoding="utf-8-sig").read().replace("\r\n", "\n"))[0]
    titulo = d["titulo"].replace(" | ", " ").replace('"', "'")
    tags = meta.get("tags") or []
    if isinstance(tags, str):
        tags = [tags]
    tags = [t for t in tags if t] + ["dossier"]
    resumen = (meta.get("resumen") or d["tesis"]).replace('"', "'")
    front = [
        "---",
        f'title: "{titulo} (Dossier)"',
        f"date: {meta.get('fecha', '2026-11-14')}T12:00:00-05:00",
        "draft: false",
        f'slug: "{slug}-dossier"',
        f'url: "/{apartado}/{slug}-dossier/"',
        "aliases:",
        f'  - "/{apartado}/{slug}-dossier"',
        f'categories: ["{apartado}"]',
        "tags: [" + ", ".join(f'"{t}"' for t in tags) + "]",
        f'summary: "{resumen}"',
        "showToc: false",
        f'dossier_id: "{did}"',
        f'area: "{d["area"]}"',
        f"palabras: {rep['stats']['palabras']}",
        "coleccion: \"biblioteca-2026\"",
        "---",
        "",
        f"> Dossier completo en HTML: [Abrir version integral](/refutaciones/{slug}.html)",
        "",
        "## Dossier integral embebido",
        "",
        f'{{{{< dossier_iframe src="/refutaciones/{slug}.html" title="{titulo}" >}}}}',
        "",
    ]
    with open(os.path.join(ROOT, md_rel.replace("/", os.sep)), "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(front))
    idx = os.path.join(ROOT, "content", apartado, "_index.md")
    line = f"- [{titulo} (Dossier)](/{apartado}/{slug}-dossier/)"
    txt = open(idx, encoding="utf-8").read()
    if f"/{apartado}/{slug}-dossier/" not in txt:
        with open(idx, "a", encoding="utf-8", newline="\n") as f:
            f.write(("" if txt.endswith("\n") else "\n") + line + "\n")
    d["estado"] = "INTEGRADO"
    d["html"] = html_rel
    d["envoltorio"] = md_rel
    d["palabras"] = rep["stats"]["palabras"]
    d["estadisticas"] = rep["stats"]
    print(f"{did} integrado: {html_rel} · {md_rel} · {rep['stats']['palabras']} palabras")


def main():
    reg = load("DOSSIER_REGISTRY.json")
    if "--lista" in sys.argv:
        from collections import Counter
        for x in reg["dossieres"]:
            print(x["id"], x["estado"].ljust(22), x["responsable"], x["slug"])
        print(dict(Counter(x["estado"] for x in reg["dossieres"])))
        return
    prot = load("PROTECTED_FILES.json")
    forzar = "--forzar" in sys.argv
    ids = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not ids:
        sys.exit(__doc__)
    for did in ids:
        integrar(did, reg, prot, forzar)
    json.dump(reg, open(os.path.join(PROY, "DOSSIER_REGISTRY.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("Ahora ejecuta: python _proyecto/scripts/manifest.py verify")


if __name__ == "__main__":
    main()
