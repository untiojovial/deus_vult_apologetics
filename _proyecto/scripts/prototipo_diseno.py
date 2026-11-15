#!/usr/bin/env python3
"""Genera el prototipo ESTATICO del rediseño (portada + catalogo de un apartado) con datos reales del sitio.
Salida: _proyecto/diseno/inicio.html y _proyecto/diseno/apartado.html (usan sitio.css).
Es una maqueta para validar la direccion visual; el diseño definitivo se porta a plantillas Hugo."""
import html, json, os, re, unicodedata

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
PROY = os.path.join(ROOT, "_proyecto")
OUT = os.path.join(PROY, "diseno")
E = html.escape

PRIM = ["filosofia", "historia", "biblia", "exegesis", "refutaciones", "doctrina", "respondiendo-al-islam", "santos"]
SEC = ["idiomas", "colaboradores", "calendario"]
BUCKET = [("islam", "Islam"), ("protest", "Protestantismo"), ("ortodox", "Ortodoxia oriental"), ("testigo", "Restauracionismo y unitarismo"),
          ("mormon", "Restauracionismo y unitarismo"), ("unitar", "Restauracionismo y unitarismo"), ("antitrinit", "Restauracionismo y unitarismo"),
          ("arrian", "Restauracionismo y unitarismo"), ("ate", "Ateísmo y naturalismo"), ("secul", "Crítica histórica y judaísmo"),
          ("juda", "Crítica histórica y judaísmo"), ("crític", "Crítica histórica y judaísmo"), ("escépt", "Crítica histórica y judaísmo")]
CONTRO = [("Islam", "Corán, hadices, taḥrīf, tawḥīd y la figura de Mahoma ante las fuentes."),
          ("Protestantismo", "Escritura y Tradición, papado, sacramentos, María y justificación."),
          ("Ortodoxia oriental", "Primado romano, concilios, filioque y la distinción esencia-energías."),
          ("Restauracionismo y unitarismo", "Mormonismo, Testigos de Jehová y las lecturas unitarias de la Escritura."),
          ("Ateísmo y naturalismo", "Existencia de Dios, problema del mal, milagros y filosofía de la mente."),
          ("Crítica histórica y judaísmo", "Historicidad de Jesús, resurrección, transmisión del texto y profecía mesiánica.")]
RUTAS = [("La divinidad de Cristo, texto a texto", "De los testimonios más antiguos a la definición de Nicea.",
          ["Jesus, Hijo de Dios", "Credo Divino Prepaulino", "La Divinidad de Cristo en Q", "Juan 20:28", "El Padre y Yo Somos Uno", "Concilio de Nicea (Dossier)"]),
         ("Diálogo con el islam: por dónde empezar", "Las seis cuestiones que aparecen en casi todo debate.",
          ["Muhammad ibn Abdallah", "Canon Biblia vs Quran", "Crucifixion de Cristo", "Fue Jesus Musulman", "El Paraclito", "Tawhid y Omnipotencia"]),
         ("Católicos y protestantes", "Autoridad, salvación y sacramentos, con sus fuentes.",
          ["Contra la Sola Scriptura", "La Salvación Católica", "La Transubstanciacion", "De Purgatorio", "La Inmaculada Concepcion", "El Concilio de Trento"])]


def nrm(s):
    return "".join(c for c in unicodedata.normalize("NFD", s.lower()) if unicodedata.category(c) != "Mn")


def front(path):
    s = open(os.path.join(ROOT, path), encoding="utf-8").read()
    m = re.match(r"^---\n(.*?)\n---", s, re.S)
    d = {}
    for ln in (m.group(1) if m else "").split("\n"):
        mm = re.match(r'^(\w+):\s*"?(.*?)"?\s*$', ln)
        if mm:
            d[mm.group(1)] = mm.group(2)
    return d


def datos():
    man = json.load(open(os.path.join(PROY, "EXISTING_CONTENT_MANIFEST.json"), encoding="utf-8"))["archivos"]
    tmap = {x["url"]: x for x in json.load(open(os.path.join(PROY, "EXISTING_TOPIC_MAP.json"), encoding="utf-8"))["dossieres"]}
    words = {e["path"]: e.get("palabras", 0) for e in man if e["path"].endswith(".html")}
    secs = {}
    for e in man:
        p = e["path"]
        if not p.startswith("content/") or not p.endswith(".md") or p.count("/") != 2:
            continue
        sec = p.split("/")[1]
        s = secs.setdefault(sec, {"slug": sec, "items": []})
        f = front(p)
        if p.endswith("_index.md"):
            s["titulo"], s["desc"] = f.get("title", sec), f.get("description", "")
            continue
        w = words.get("static" + e["dossier_html"], 0) if e.get("dossier_html") else 0
        inter = nrm(str(tmap.get(e.get("url"), {}).get("interlocutor", "")))
        area = next((b for k, b in BUCKET if nrm(k) in inter), "")
        s["items"].append({"titulo": f.get("title", ""), "url": e.get("url") or f.get("url", "#"), "resumen": f.get("summary", ""),
                           "palabras": w, "area": area, "dossier": bool(e.get("dossier_html"))})
    nuevos = json.load(open(os.path.join(PROY, "DOSSIER_REGISTRY.json"), encoding="utf-8"))["dossieres"]
    return secs, nuevos


MENU = {"filosofia": "Filosofia", "historia": "Historia", "biblia": "Biblia", "exegesis": "Exegesis", "refutaciones": "Refutaciones",
        "doctrina": "Doctrina", "respondiendo-al-islam": "Respondiendo al Islam", "santos": "Santos", "idiomas": "Idiomas",
        "colaboradores": "Colaboradores", "calendario": "Calendario"}  # nombres EXACTOS del menu de hugo.toml


def cabecera(secs, actual=None, base=""):
    li = "".join(f'<li><a href="{base}apartado.html"{" aria-current=" + chr(34) + "page" + chr(34) if s == actual else ""}>{E(MENU[s])}</a></li>' for s in PRIM if s in secs)
    util = "".join(f'<a href="#">{E(MENU[s])}</a>' for s in SEC if s in secs) + '<a href="#">Busqueda</a>'
    return f"""<a class="salto" href="#contenido">Saltar al contenido</a>
<header class="cabecera"><div class="caja">
  <div class="cab-sup">
    <a class="marca" href="inicio.html" aria-label="Defendiendo la Fe, inicio">
      <svg class="sello" viewBox="0 0 40 40" aria-hidden="true"><circle cx="20" cy="20" r="18.5" fill="none" stroke="currentColor" stroke-width="1"/><path d="M20 8v24M12 16h16" stroke="currentColor" stroke-width="1.6" fill="none"/></svg>
      <span><span class="marca-nombre">Defendiendo la Fe</span><span class="marca-lema vers">Biblioteca de apologética católica</span></span>
    </a>
    <nav class="cab-util" aria-label="Utilidades">{util}</nav>
    <button class="menu-btn" aria-expanded="false" aria-controls="nav-prim">Menú</button>
  </div>
  <nav class="nav-prim" id="nav-prim" aria-label="Apartados"><ul>{li}</ul></nav>
</div></header>"""


def pie(secs):
    ap = "".join(f'<li><a href="#">{E(MENU[s])}</a></li>' for s in PRIM if s in secs)
    ot = "".join(f'<li><a href="#">{E(MENU[s])}</a></li>' for s in SEC if s in secs)
    return f"""<footer class="pie"><div class="caja">
  <div class="pie-grid">
    <div><h4 class="vers">Defendiendo la Fe</h4><p>Dossieres de investigación apologética con fuentes primarias, análisis filológico y argumentación formal. Cada cita lleva su localización para que el lector pueda comprobarla.</p></div>
    <div><h4 class="vers">Apartados</h4><ul>{ap}</ul></div>
    <div><h4 class="vers">Recursos</h4><ul>{ot}<li><a href="#">Busqueda</a></li></ul></div>
    <div><h4 class="vers">Biblioteca</h4><ul><li><a href="#">Índice general</a></li><li><a href="#">Rutas de estudio</a></li><li><a href="#">Fuentes rivales analizadas</a></li><li><a href="#">Método editorial</a></li></ul></div>
  </div>
  <div class="pie-fin"><span class="vers">Fides quaerens intellectum</span><span class="vers">Defendiendo la Fe · 2026</span></div>
</div></footer>
<script>
(function(){{var b=document.querySelector('.menu-btn'),n=document.getElementById('nav-prim');if(b)b.addEventListener('click',function(){{var o=n.classList.toggle('abierto');b.setAttribute('aria-expanded',o)}});}})();
</script>"""


def pagina(titulo, cuerpo):
    return f"""<!DOCTYPE html>
<html lang="es"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(titulo)}</title><link rel="stylesheet" href="sitio.css"></head>
<body>{cuerpo}</body></html>
"""


def fmt(n):
    return f"{n:,}".replace(",", ".")


def lectura(w):
    return f"{fmt(w)} palabras · {max(1, round(w / 220))} min" if w else ""


def inicio(secs, nuevos):
    todos = [i for s in secs.values() for i in s["items"] if i["dossier"] and s["slug"] != "idiomas"]
    total_w = sum(i["palabras"] for i in todos)
    cols = ""
    for n, s in enumerate([x for x in PRIM if x in secs], 1):
        c = sum(1 for i in secs[s]["items"] if i["dossier"])
        c2 = sum(1 for x in nuevos if x["apartado"] == s)
        cols += (f'<a class="col-item" href="apartado.html"><span class="col-num">{n:02d}</span><h3>{E(MENU[s])}</h3>'
                 f'<span class="col-cuenta">{c} dossieres{f" · {c2} en preparación" if c2 else ""}</span><p>{E(secs[s].get("desc", ""))}</p></a>')
    filas = ""
    for x in nuevos[:8]:
        filas += (f'<li class="fila"><span class="fila-sig">{x["id"]}</span><a href="#"><h3>{E(x["titulo"].replace(" | ", " "))}</h3>'
                  f'<p>{E(x["tesis"][:210].rsplit(" ", 1)[0])}…</p></a><span class="fila-meta">{E(x["area"])}<br>{E(MENU[x["apartado"]])}</span></li>')
    contro = ""
    for nombre, desc in CONTRO:
        n1 = sum(1 for i in todos if i["area"] == nombre)
        n2 = sum(1 for x in nuevos if x["area"] == nombre)
        contro += f'<a class="contro" href="#"><h3>{E(nombre)}</h3><p>{E(desc)}</p><span class="vers">{n1} dossieres · {n2} en preparación</span></a>'
    rutas = ""
    for t, d, pasos in RUTAS:
        lis = ""
        for p in pasos:
            it = next((i for i in todos if nrm(p) in nrm(i["titulo"])), None)
            if it:
                lis += f'<li><a href="{E(it["url"])}">{E(it["titulo"].replace(" (Dossier)", ""))}</a></li>'
        rutas += f'<div class="ruta"><h3>{E(t)}</h3><p>{E(d)}</p><ol>{lis}</ol></div>'
    cuerpo = cabecera(secs) + f"""
<main id="contenido"><div class="caja">
  <section class="portada">
    <div><span class="vers">Fuentes · Argumentos · Refutaciones</span>
      <h1>Razones para creer, <em>con las fuentes delante</em>.</h1></div>
    <div><p>Una biblioteca de dossieres de investigación apologética: textos originales, manuscritos, silogismos desarrollados y la mejor versión de cada objeción, respondida.</p>
      <form class="buscar" role="search" action="#"><input type="search" placeholder="Buscar un tema, un versículo, un autor…" aria-label="Buscar en la biblioteca"><button type="submit">Buscar</button></form>
      <ul class="cifras"><li><b>{len(todos)}</b><span class="vers">Dossieres</span></li><li><b>{len(nuevos)}</b><span class="vers">En preparación</span></li><li><b>{fmt(round(total_w, -3))}</b><span class="vers">Palabras</span></li></ul></div>
  </section>
  <section class="sec" aria-labelledby="h-col"><div class="sec-cab"><h2 id="h-col">Colecciones</h2><a class="mas" href="#">Índice general →</a></div>
    <div class="colecciones">{cols}</div></section>
  <section class="sec" aria-labelledby="h-nue"><div class="sec-cab"><h2 id="h-nue">Nuevas investigaciones</h2><a class="mas" href="#">Las cincuenta →</a></div>
    <p class="sec-intro">Cincuenta expedientes nuevos que responden a publicaciones concretas de la apologética musulmana, protestante, ortodoxa, restauracionista y atea, con revisión documental y adversarial.</p>
    <ol class="catalogo">{filas}</ol></section>
  <section class="sec" aria-labelledby="h-con"><div class="sec-cab"><h2 id="h-con">Explorar por controversia</h2></div>
    <div class="controversias">{contro}</div></section>
  <section class="sec" aria-labelledby="h-rut"><div class="sec-cab"><h2 id="h-rut">Rutas de estudio</h2><a class="mas" href="#">Todas las rutas →</a></div>
    <div class="rutas">{rutas}</div></section>
</div></main>""" + pie(secs)
    return pagina("Defendiendo la Fe — Biblioteca de apologética católica", cuerpo)


def apartado(secs, slug="respondiendo-al-islam"):
    s = secs[slug]
    items = sorted([i for i in s["items"] if i["dossier"]], key=lambda i: nrm(i["titulo"]))
    areas = sorted({i["area"] for i in items if i["area"]})
    chips = '<button class="chip" aria-pressed="true" data-area="">Todos</button>' + "".join(f'<button class="chip" aria-pressed="false" data-area="{E(a)}">{E(a)}</button>' for a in areas)
    filas = ""
    for n, i in enumerate(items, 1):
        filas += (f'<li class="fila" data-area="{E(i["area"])}" data-t="{E(nrm(i["titulo"] + " " + i["resumen"]))}"><span class="fila-sig">{n:02d}</span>'
                  f'<a href="{E(i["url"])}"><h3>{E(i["titulo"].replace(" (Dossier)", ""))}</h3><p>{E(i["resumen"])}</p></a>'
                  f'<span class="fila-meta">{lectura(i["palabras"])}<br>{E(i["area"])}</span></li>')
    cuerpo = cabecera(secs, slug) + f"""
<main id="contenido"><div class="caja">
  <header class="pag-cab"><nav class="migas" aria-label="Migas"><a href="inicio.html">Inicio</a> / {E(s["titulo"])}</nav>
    <h1>{E(s["titulo"])}</h1><p>{E(s.get("desc", ""))}</p></header>
  <div class="filtros"><input type="search" id="q" placeholder="Filtrar por título o tema…" aria-label="Filtrar dossieres">{chips}</div>
  <p class="cuenta-res" id="cuenta" aria-live="polite">{len(items)} dossieres</p>
  <ol class="catalogo" id="cat">{filas}</ol>
</div></main>""" + pie(secs) + """
<script>
(function(){var q=document.getElementById('q'),rows=[].slice.call(document.querySelectorAll('#cat .fila')),chips=[].slice.call(document.querySelectorAll('.chip')),area='';
function nrm(s){return s.toLowerCase().normalize('NFD').replace(/[\\u0300-\\u036f]/g,'')}
function go(){var t=nrm(q.value),n=0;rows.forEach(function(r){var ok=(!area||r.dataset.area===area)&&(!t||r.dataset.t.indexOf(t)>-1);r.hidden=!ok;if(ok)n++});document.getElementById('cuenta').textContent=n+(n===1?' dossier':' dossieres')}
q.addEventListener('input',go);chips.forEach(function(c){c.addEventListener('click',function(){area=c.dataset.area;chips.forEach(function(x){x.setAttribute('aria-pressed',x===c)});go()})});})();
</script>"""
    return pagina(s["titulo"] + " — Defendiendo la Fe", cuerpo)


if __name__ == "__main__":
    secs, nuevos = datos()
    os.makedirs(OUT, exist_ok=True)
    open(os.path.join(OUT, "inicio.html"), "w", encoding="utf-8", newline="\n").write(inicio(secs, nuevos))
    open(os.path.join(OUT, "apartado.html"), "w", encoding="utf-8", newline="\n").write(apartado(secs))
    print("prototipo generado en", OUT, "| apartados:", sorted(secs))
