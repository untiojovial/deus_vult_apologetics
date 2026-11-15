#!/usr/bin/env python3
"""Genera data/dossieres.json: metadatos de los dossieres EXISTENTES para las plantillas del rediseño.

Los envoltorios .md antiguos estan protegidos y no pueden recibir metadatos nuevos; por eso el area de
controversia, la extension y los encabezados internos se aportan desde este archivo de datos, calculado a
partir de EXISTING_CONTENT_MANIFEST.json, EXISTING_TOPIC_MAP.json y del propio HTML (solo lectura).

  python _proyecto/scripts/datos_sitio.py
"""
import html, json, os, re, subprocess, unicodedata

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
PROY = os.path.join(ROOT, "_proyecto")

BUCKET = [("islam", "Islam"), ("protest", "Protestantismo"), ("ortodox", "Ortodoxia oriental"),
          ("testigo", "Restauracionismo y unitarismo"), ("mormon", "Restauracionismo y unitarismo"),
          ("unitar", "Restauracionismo y unitarismo"), ("antitrinit", "Restauracionismo y unitarismo"),
          ("arrian", "Restauracionismo y unitarismo"), ("ate", "Ateísmo y naturalismo"),
          ("secul", "Crítica histórica y judaísmo"), ("juda", "Crítica histórica y judaísmo"),
          ("critic", "Crítica histórica y judaísmo"), ("escept", "Crítica histórica y judaísmo")]


def nrm(s):
    return "".join(c for c in unicodedata.normalize("NFD", s.lower()) if unicodedata.category(c) != "Mn")


def encabezados(path):
    """h2 del HTML del dossier (texto plano), para el indice de busqueda."""
    raw = subprocess.run(["git", "-C", ROOT, "show", f"HEAD:{path}"], capture_output=True).stdout.decode("utf-8", "replace")
    hs = []
    for m in re.finditer(r"<h2[^>]*>(.*?)</h2>", raw, re.S | re.I):
        t = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", m.group(1)))).strip()
        if 3 < len(t) < 140 and t not in hs:
            hs.append(t)
    return hs[:40]


def main():
    man = json.load(open(os.path.join(PROY, "EXISTING_CONTENT_MANIFEST.json"), encoding="utf-8"))["archivos"]
    tmap = {x["url"]: x for x in json.load(open(os.path.join(PROY, "EXISTING_TOPIC_MAP.json"), encoding="utf-8"))["dossieres"]}
    words = {e["path"]: e.get("palabras", 0) for e in man if e["path"].endswith(".html")}
    out = {}
    for e in man:
        if not e.get("dossier_html"):
            continue
        hp = "static" + e["dossier_html"]
        url = e["url"] if e["url"].endswith("/") else e["url"] + "/"
        t = tmap.get(e["url"], {})
        inter = nrm(str(t.get("interlocutor", "")))
        area = next((b for k, b in BUCKET if k in inter), "")
        w = words.get(hp, 0)
        if e["path"].startswith("content/idiomas/"):
            area, w = "", 0
        out[url] = {"area": area, "palabras": w if w > 300 else 0, "encabezados": encabezados(hp) if w > 300 else []}
    os.makedirs(os.path.join(ROOT, "data"), exist_ok=True)
    with open(os.path.join(ROOT, "data", "dossieres.json"), "w", encoding="utf-8", newline="\n") as f:
        json.dump(out, f, ensure_ascii=False, indent=1, sort_keys=True)
    from collections import Counter
    print(len(out), "dossieres;", dict(Counter(v["area"] or "(sin área)" for v in out.values())))


if __name__ == "__main__":
    main()
