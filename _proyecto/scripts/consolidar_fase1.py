#!/usr/bin/env python3
"""Fusiona los informes de exploracion (investigadores/Rxx/exploracion.json) en los registros centrales.

  python _proyecto/scripts/consolidar_fase1.py

Regenera: OPPOSING_APOLOGETICS_REGISTRY.json, ARTICLE_REFUTATION_REGISTRY.json y la parte
"investigadores" de TOPIC_CANDIDATES.json (conserva los candidatos añadidos por el director, origen "DIR").
"""
import glob, json, os, re

PROY = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


def load(p, default):
    try:
        return json.load(open(p, encoding="utf-8"))
    except Exception:
        return default


def host(u):
    m = re.match(r"https?://(?:www\.)?([^/]+)", u or "")
    return m.group(1).lower() if m else (u or "").lower()


sitios, articulos, cands, resumen = {}, {}, [], []
for p in sorted(glob.glob(os.path.join(PROY, "investigadores", "R*", "exploracion.json"))):
    d = load(p, None)
    r = os.path.basename(os.path.dirname(p))
    if not d:
        resumen.append(f"{r}: JSON invalido")
        continue
    for s in d.get("sitios", []):
        k = host(s.get("url"))
        if k in sitios:
            sitios[k]["investigadores"].append(r)
            sitios[k]["publicaciones_destacadas"] += s.get("publicaciones_destacadas", [])
        else:
            s = dict(s)
            s["investigadores"] = [r]
            sitios[k] = s
    for a in d.get("articulos", []):
        k = (a.get("url") or a.get("titulo") or "").strip().rstrip("/").lower()
        if k and k not in articulos:
            a = dict(a)
            a["investigador"] = r
            a["estado_refutacion"] = "REGISTRADO"
            a["dossier_asociado"] = None
            articulos[k] = a
    for i, c in enumerate(d.get("candidatos", []), 1):
        c = dict(c)
        sc = c.get("puntuacion") or {}
        c["id"] = f"C-{r}-{i:02d}"
        c["origen"] = r
        c["puntuacion_total"] = sum(v for v in sc.values() if isinstance(v, (int, float)))
        c.setdefault("estado", "CANDIDATO")
        cands.append(c)
    resumen.append(f"{r}: {len(d.get('sitios', []))} sitios, {len(d.get('articulos', []))} articulos, {len(d.get('candidatos', []))} candidatos")

json.dump({"total": len(sitios), "sitios": sorted(sitios.values(), key=lambda s: (s.get("orientacion") or "", s.get("nombre") or ""))},
          open(os.path.join(PROY, "OPPOSING_APOLOGETICS_REGISTRY.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
json.dump({"total": len(articulos), "articulos": list(articulos.values())},
          open(os.path.join(PROY, "ARTICLE_REFUTATION_REGISTRY.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)

prev = load(os.path.join(PROY, "TOPIC_CANDIDATES.json"), {"candidatos": []})
estado_prev = {c.get("id"): c for c in prev.get("candidatos", [])}
director = [c for c in prev.get("candidatos", []) if c.get("origen") == "DIR"]
for c in cands:  # conservar decisiones editoriales ya tomadas
    old = estado_prev.get(c["id"])
    if old:
        for k in ("estado", "decision_editorial", "dossier", "fusionado_en"):
            if k in old:
                c[k] = old[k]
allc = cands + director
json.dump({"total": len(allc), "candidatos": allc},
          open(os.path.join(PROY, "TOPIC_CANDIDATES.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)

print("\n".join(resumen))
print(f"TOTAL: {len(sitios)} sitios unicos, {len(articulos)} articulos, {len(allc)} candidatos ({len(director)} del director)")
ver = sum(1 for a in articulos.values() if a.get("verificado") is True)
print(f"articulos con URL verificada por el investigador: {ver}/{len(articulos)}")
