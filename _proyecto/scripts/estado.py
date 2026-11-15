#!/usr/bin/env python3
"""Cambia el estado de uno o varios dossieres en DOSSIER_REGISTRY.json.
  python _proyecto/scripts/estado.py BORRADOR D01 D17 [--nota "texto"]
"""
import json, os, sys
P = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "DOSSIER_REGISTRY.json")
ORDEN = ["APROBADO", "INVESTIGANDO", "FUENTES_VERIFICADAS", "BORRADOR", "REVISION_ADVERSARIAL", "CORRECCIONES",
         "APROBACION_EDITORIAL", "INTEGRADO", "VERIFICADO"]
args = sys.argv[1:]
nota = None
if "--nota" in args:
    i = args.index("--nota"); nota = args[i + 1]; del args[i:i + 2]
if not args or args[0] not in ORDEN:
    sys.exit(__doc__ + "\nEstados: " + ", ".join(ORDEN))
reg = json.load(open(P, encoding="utf-8"))
for d in reg["dossieres"]:
    if d["id"] in args[1:]:
        d["estado"] = args[0]
        if nota:
            d.setdefault("notas_director", []).append(nota)
        print(d["id"], "->", args[0])
json.dump(reg, open(P, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
