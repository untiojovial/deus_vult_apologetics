#!/usr/bin/env python3
"""Constructor de dossieres nuevos.

Convierte un borrador en Markdown estructurado (ver _proyecto/plantilla/FORMATO_BORRADOR.md) en un
HTML autocontenido con el MISMO lenguaje visual que los dossieres existentes de la familia
"Indice lateral + portada + secciones" (Cinzel / EB Garamond / Source Sans 3).

La hoja de estilo base se toma LITERALMENTE de un dossier existente (paracleto-dossier.html, leido del
commit base). Las paletas "pergamino" y "marino" aplican los colores de crucifixion-dossier.html y
jn11-dossier.html. Los componentes nuevos (evidencia, cadena de debate, etc.) son aditivos.

Uso:
  python _proyecto/scripts/build_dossier.py <borrador.md> [-o salida.html] [--check]
"""
import html, json, os, re, subprocess, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
BASE_COMMIT = "75cafb8"
BASE_DOSSIER = "static/refutaciones/paracleto-dossier.html"

# paracleto (esmeralda) -> pergamino (crucifixion-dossier) / marino (jn11-dossier)
PALETAS = {
    "esmeralda": {},
    "pergamino": {
        "#0f1a10": "#1a1207", "#f4f0e4": "#f5eedd", "#e6dfca": "#e8dcc4", "#080f08": "#1a0a00",
        "#1a3a1a": "#3d1a00", "#7a8b14": "#8b6914", "#b0c228": "#c49a28", "#6a9a6a": "#c4a96a",
        "#a8c8a0": "#d8c080", "#3a4a2a": "#5a4a2a", "#060e06": "#110800", "#0d180d": "#1f1000",
        "rgba(110,155,80,": "rgba(196,169,106,", "rgba(180,210,160,0.72)": "rgba(220,200,155,0.72)",
        "#030a03": "#0a0400", "#e8f4e0": "#f0e4c0", "rgba(232,244,224,0.88)": "rgba(240,228,192,0.88)",
        "#1a2a0a": "#2a1a00", "#c8e0a0": "#e8c88a", "#b8d890": "#d8b870", "#e8f8d0": "#f8ead8",
        "#edf0e0": "#f0e8d8", "#1a3a10": "#1a2a10", "#3a3a10": "#3a2a00", "#0f1a08": "#2a1000",
        "#f0f4e0": "#f5ead0",
    },
    "marino": {
        "#0f1a10": "#1a1207", "#f4f0e4": "#f6efdf", "#e6dfca": "#ece2cb", "#080f08": "#0f1a2e",
        "#1a3a1a": "#1a2d4a", "#7a8b14": "#8b7414", "#b0c228": "#c4a228", "#6a9a6a": "#7a9ab4",
        "#a8c8a0": "#b8cfe0", "#3a4a2a": "#3a4a5a", "#060e06": "#0a1220", "#0d180d": "#141f33",
        "rgba(110,155,80,": "rgba(122,154,180,", "rgba(180,210,160,0.72)": "rgba(184,207,224,0.7)",
        "#030a03": "#080e1c", "#e8f4e0": "#e8f0f8", "rgba(232,244,224,0.88)": "rgba(232,240,248,0.85)",
        "#1a2a0a": "#1a2a3a", "#c8e0a0": "#a8cce0", "#b8d890": "#a8cce0", "#e8f8d0": "#e8f0f8",
        "#edf0e0": "#e8eef5", "#1a3a10": "#1a3a5a", "#3a3a10": "#3a4a1a", "#0f1a08": "#0f1a2e",
        "#f0f4e0": "#eef3f8",
    },
}

# Componentes ADITIVOS: solo usan variables y patrones de la hoja base.
ADITIVO_CSS = """
/* ═══ COMPONENTES ADITIVOS (dossieres nuevos) — mismo lenguaje visual ═══ */
h4{font-family:'Cinzel',serif;font-size:9.5px;letter-spacing:2.5px;text-transform:uppercase;color:var(--emerald);margin:20px 0 8px}
section ul,section ol{margin:0 0 14px 26px;line-height:1.72;font-size:1.01rem}
section li{margin-bottom:6px}
section li>p{margin-bottom:6px}
section a{color:var(--emerald);text-decoration:underline;text-decoration-color:var(--rule);text-underline-offset:2px;word-break:break-word}
.verdict a{color:var(--gold-lt)}
.tbl-wrap{overflow-x:auto;margin:18px 0}
.tbl-wrap table{margin:0}
.obj-q[data-lbl]::before{content:'✦ ' attr(data-lbl) ': '}
.obj-r[data-lbl]::before{content:'→ ' attr(data-lbl) ': '}
.obj-q p,.obj-r p{font-size:.97rem;margin-bottom:8px}
.obj-q p:first-child,.obj-r p:first-child{display:inline}
.syl-form{font-family:'Source Sans 3',sans-serif;font-size:.74rem;letter-spacing:.4px;color:var(--margin);margin-bottom:10px}
.syl-notes{background:var(--parchment);border:1.5px solid var(--gold);border-top:none;margin:-22px 0 22px;padding:16px 26px 18px}
.syl-notes p,.syl-notes li{font-size:.95rem}
.syl-notes h4:first-child{margin-top:0}
.chain{margin:22px 0;border-left:3px solid var(--rule-lt);padding-left:0}
.chain-title{font-family:'Cinzel',serif;font-size:9px;letter-spacing:3px;text-transform:uppercase;color:var(--gold);margin:0 0 10px 18px}
.chain-step{padding:12px 18px;margin-bottom:2px;line-height:1.72;font-size:.97rem}
.chain-step p{font-size:.97rem;margin-bottom:8px}
.chain-step.pro{background:var(--aged);border-left:4px solid var(--gold);margin-left:-3px}
.chain-step.con{background:#edf0e0;border-left:4px solid var(--emerald);margin-left:-3px;font-style:italic;color:var(--emerald)}
.chain-step.con strong{color:var(--emerald)}
.chain-lbl{font-family:'Cinzel',serif;font-size:8px;letter-spacing:2.5px;text-transform:uppercase;font-style:normal;display:block;margin-bottom:5px;color:var(--gold)}
.chain-step.con .chain-lbl{color:var(--emerald)}
.evid{border-left:4px solid var(--gold)}
.evid.rival{border-left-color:var(--crimson)}
.evid-meta{display:grid;grid-template-columns:max-content 1fr;gap:3px 14px;font-family:'Source Sans 3',sans-serif;font-size:.8rem;line-height:1.5;color:var(--margin);margin-bottom:12px}
.evid-meta dt{font-weight:600;color:var(--emerald);text-transform:uppercase;letter-spacing:.6px;font-size:.68rem;padding-top:2px}
.evid-meta dd{word-break:break-word}
.evid-orig{font-size:1.04rem;line-height:1.8;margin:10px 0 6px;padding:10px 14px;background:var(--parchment);border:1px solid var(--rule-lt)}
.evid-orig[dir=rtl]{font-size:1.2rem;line-height:2}
.evid-translit{font-style:italic;font-size:.92rem;color:var(--margin);margin-bottom:6px}
.evid-trad{font-style:italic;margin-bottom:10px}
.evid figure,.figura{margin:14px 0;text-align:center}
.evid figure img,.figura img{max-width:100%;height:auto;border:1px solid var(--rule-lt);background:#fff}
figcaption{font-family:'Source Sans 3',sans-serif;font-size:.76rem;color:var(--margin);line-height:1.5;margin-top:6px;text-align:left}
.estado{display:inline-block;font-family:'Cinzel',serif;font-size:7.5px;letter-spacing:2px;text-transform:uppercase;padding:3px 8px;margin-left:8px;vertical-align:middle;background:#1a6a1a;color:#e8f8e8}
.estado.pend{background:var(--crimson);color:#f8e8e8}
.certeza{width:100%;border-collapse:collapse;margin:18px 0;font-size:.95rem}
.certeza td{padding:10px 14px;vertical-align:top;line-height:1.6;border-bottom:1px solid var(--rule-lt);background:var(--parchment)}
.certeza td:first-child{width:170px;font-family:'Cinzel',serif;font-size:8.5px;letter-spacing:2px;text-transform:uppercase;color:var(--aged);background:var(--emerald);font-weight:600}
.certeza tr.c2 td:first-child{opacity:.9}.certeza tr.c3 td:first-child{opacity:.8}.certeza tr.c4 td:first-child{background:var(--margin)}.certeza tr.c5 td:first-child{background:var(--crimson)}
.colofon{padding:22px 58px 30px;font-family:'Source Sans 3',sans-serif;font-size:.74rem;color:var(--margin);line-height:1.6;border-top:6px double var(--gold);background:var(--aged)}
.sir{direction:rtl;font-size:1.12rem;display:inline-block;line-height:1.7;color:var(--crimson)}
.tr{font-style:italic;color:var(--margin);font-size:.95em}
@media(max-width:680px){.syl-notes{padding:14px 16px}.evid-meta{grid-template-columns:1fr}.evid-meta dt{padding-top:6px}.certeza td:first-child{width:104px}.colofon{padding:18px 20px 24px}}
@media print{#toc-btn,#toc-panel,#toc-overlay{display:none}body{background:#fff}#main{box-shadow:none;max-width:100%}}
"""

ROMAN = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
         (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]


def roman(n):
    out = ""
    for v, s in ROMAN:
        while n >= v:
            out += s
            n -= v
    return out


def base_parts():
    raw = subprocess.run(["git", "-C", ROOT, "show", f"{BASE_COMMIT}:{BASE_DOSSIER}"], capture_output=True, check=True).stdout
    s = raw.decode("utf-8")
    css = re.search(r"<style[^>]*>(.*?)</style>", s, re.S).group(1)
    js = re.search(r"<script[^>]*>(.*?)</script>", s, re.S).group(1)
    return css, js


# ───────────────────────── inline ─────────────────────────
LANGS = {"gr": "gr", "he": "he", "ar": "ar", "la": "la", "sir": "sir", "tr": "tr"}


def inline(t):
    t = html.escape(t, quote=False)
    # enlaces [texto](url)
    def link(m):
        url = m.group(2).replace('"', "%22")
        return f'<a href="{url}" target="_blank" rel="noopener">{m.group(1)}</a>'
    t = re.sub(r"\[([^\]]+)\]\((https?://[^\s)]+)\)", link, t)
    t = re.sub(r"\[([^\]]+)\]\((#[\w-]+)\)", r'<a href="\2">\1</a>', t)
    # spans de lengua {gr|texto}
    def lang(m):
        cls = LANGS.get(m.group(1))
        return f'<span class="{cls}">{m.group(2)}</span>' if cls else m.group(0)
    t = re.sub(r"\{(\w+)\|([^{}]+)\}", lang, t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", t)
    t = t.replace(" -- ", " — ")
    return t


# ───────────────────────── bloques markdown ─────────────────────────
def md_blocks(text, stats):
    """Markdown basico -> HTML (parrafos, h3/h4, listas, citas, tablas, imagenes)."""
    out = []
    lines = text.strip("\n").split("\n")
    i = 0
    while i < len(lines):
        ln = lines[i]
        if not ln.strip():
            i += 1
            continue
        if ln.startswith("#### "):
            out.append(f"<h4>{inline(ln[5:].strip())}</h4>"); i += 1; continue
        if ln.startswith("### "):
            out.append(f"<h3>{inline(ln[4:].strip())}</h3>"); i += 1; continue
        m = re.match(r'!\[([^\]]*)\]\(([^\s)]+)(?:\s+"([^"]*)")?\)\s*$', ln)
        if m:
            cap = f"<figcaption>{inline(m.group(3))}</figcaption>" if m.group(3) else ""
            out.append(f'<figure class="figura"><img src="{html.escape(m.group(2))}" alt="{html.escape(m.group(1))}" loading="lazy">{cap}</figure>')
            stats["imagenes"] += 1
            i += 1; continue
        if ln.startswith(">"):
            buf = []
            while i < len(lines) and lines[i].startswith(">"):
                buf.append(lines[i][1:].strip()); i += 1
            src = ""
            if buf and re.match(r"^(—|--)\s*", buf[-1]):
                src = f'<span class="src">{inline(re.sub(r"^(—|--)\s*", "", buf.pop()))}</span>'
            body = "<br>".join(inline(b) for b in buf if b)
            out.append(f"<blockquote>{body}{src}</blockquote>")
            continue
        if ln.lstrip().startswith("|") and i + 1 < len(lines) and re.match(r"^\s*\|?\s*:?-{2,}", lines[i + 1]):
            def cells(l):
                return [c.strip() for c in l.strip().strip("|").split("|")]
            head = cells(ln); i += 2
            rows = []
            while i < len(lines) and lines[i].lstrip().startswith("|"):
                rows.append(cells(lines[i])); i += 1
            h = "".join(f"<th>{inline(c)}</th>" for c in head)
            b = "".join("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>" for r in rows)
            out.append(f'<div class="tbl-wrap"><table><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table></div>')
            stats["tablas"] += 1
            continue
        m = re.match(r"^(\s*)([-*]|\d+[.)])\s+", ln)
        if m:
            ordered = m.group(2)[0].isdigit()
            items = []
            while i < len(lines):
                mm = re.match(r"^(\s*)([-*]|\d+[.)])\s+(.*)$", lines[i])
                if mm:
                    items.append(mm.group(3)); i += 1
                elif lines[i].strip() and lines[i].startswith(("  ", "\t")) and items:
                    items[-1] += " " + lines[i].strip(); i += 1
                else:
                    break
            tag = "ol" if ordered else "ul"
            out.append(f"<{tag}>" + "".join(f"<li>{inline(x)}</li>" for x in items) + f"</{tag}>")
            continue
        buf = []
        while i < len(lines) and lines[i].strip() and not re.match(r"^(#{3,4} |>|\s*([-*]|\d+[.)])\s+|!\[)", lines[i]) \
                and not (lines[i].lstrip().startswith("|") and i + 1 < len(lines) and re.match(r"^\s*\|?\s*:?-{2,}", lines[i + 1])):
            buf.append(lines[i].strip()); i += 1
        if buf:
            out.append(f"<p>{inline(' '.join(buf))}</p>")
        else:  # linea no reconocida: evitar bucle infinito
            out.append(f"<p>{inline(ln.strip())}</p>"); i += 1
    return "\n".join(out)


def keyed(body, keys):
    """Separa 'CLAVE: valor' multilinea. Devuelve lista [(clave, valor)] y el resto tras '---'."""
    head, _, rest = body.partition("\n---\n")
    if body.strip().startswith("---\n"):
        head, rest = "", body.strip()[4:]
    pairs, cur = [], None
    pat = re.compile(r"^(" + "|".join(keys) + r"):\s*(.*)$")
    for ln in head.split("\n"):
        m = pat.match(ln)
        if m:
            cur = [m.group(1), m.group(2)]
            pairs.append(cur)
        elif cur is not None:
            cur[1] += "\n" + ln
    return [(k, v.strip()) for k, v in pairs], rest.strip()


def para_or_inline(v, stats):
    """Valor corto -> inline; con saltos de parrafo o listas -> bloques."""
    if "\n\n" in v or re.search(r"^\s*([-*]|\d+[.)])\s+", v, re.M) or v.startswith(">"):
        return md_blocks(v, stats)
    return inline(" ".join(x.strip() for x in v.split("\n")))


PREM_LBL = {"PM": "Premisa mayor", "Pm": "Premisa menor", "PA": "Premisa auxiliar"}
CHAIN = {"A": ("pro", "Argumento"), "O": ("con", "Objeción"), "R": ("pro", "Respuesta"),
         "CO": ("con", "Contraobjeción"), "CR": ("pro", "Contrarréplica"),
         "CO2": ("con", "Segunda contraobjeción"), "CR2": ("pro", "Segunda contrarréplica"),
         "E": ("pro", "Evaluación")}
META_ORDER = [("tipo", "Tipo"), ("autor", "Autor"), ("documento", "Documento"), ("obra", "Obra"), ("titulo", "Título"),
              ("sitio", "Sitio"), ("fecha", "Fecha"), ("ubicacion", "Localización"), ("edicion", "Edición"),
              ("lengua", "Lengua"), ("conservacion", "Conservación"), ("url", "Enlace"), ("licencia", "Licencia"),
              ("consulta", "Consultado"), ("clase", "Clase de fuente")]
CERT = [("demostrado", "Demostrado", "c1"), ("probable", "Altamente probable", "c2"),
        ("defendible", "Razonablemente defendible", "c3"), ("abierto", "Debate abierto", "c4"),
        ("no-afirmable", "No puede afirmarse", "c5")]


def directive(kind, arg, body, stats, warn):
    kind = kind.lower()
    if kind == "silogismo":
        pairs, rest = keyed(body, ["PM", "Pm", "PA", r"P\d+", "C", "forma", "fuerza"])
        stats["silogismos"] += 1
        h = [f'<div class="syllogism"><div class="syllogism-title">{inline(arg or "Silogismo")}</div>']
        d = dict(pairs)
        if "forma" in d:
            h.append(f'<div class="syl-form">Forma lógica: {inline(d["forma"])}</div>')
        if not any(k == "C" for k, _ in pairs):
            warn.append(f"silogismo sin conclusión: {arg}")
        for k, v in pairs:
            if k in ("forma", "fuerza"):
                continue
            if k == "C":
                h.append(f'<p class="conclusion">∴ Conclusión: {inline(" ".join(v.split()))}</p>')
            else:
                lbl = PREM_LBL.get(k) or f"Premisa {k[1:]}"
                h.append(f'<p><strong>{lbl}:</strong> {inline(" ".join(v.split()))}</p>')
        h.append("</div>")
        notes = ""
        if rest:
            notes += md_blocks(rest, stats)
        if "fuerza" in d:
            notes += f'<h4>Evaluación de su fuerza</h4><p>{inline(" ".join(d["fuerza"].split()))}</p>'
        if notes:
            h.append(f'<div class="syl-notes">{notes}</div>')
        else:
            warn.append(f"silogismo sin justificación de premisas: {arg}")
        return "\n".join(h)
    if kind == "objecion":
        pairs, _ = keyed(body, ["Q", "R"])
        stats["objeciones"] += 1
        d = dict(pairs)
        ql, _, rl = (arg or "Objeción|Respuesta").partition("|")
        return (f'<div class="obj"><div class="obj-q" data-lbl="{html.escape(ql.strip() or "Objeción")}">{para_or_inline(d.get("Q", ""), stats)}</div>'
                f'<div class="obj-r" data-lbl="{html.escape(rl.strip() or "Respuesta")}">{para_or_inline(d.get("R", ""), stats)}</div></div>')
    if kind == "cadena":
        pairs, _ = keyed(body, list(CHAIN.keys()))
        stats["cadenas"] += 1
        h = ['<div class="chain">']
        if arg:
            h.append(f'<div class="chain-title">{inline(arg)}</div>')
        for k, v in pairs:
            cls, lbl = CHAIN[k]
            h.append(f'<div class="chain-step {cls}"><span class="chain-lbl">{lbl}</span>{para_or_inline(v, stats)}</div>')
        h.append("</div>")
        return "\n".join(h)
    if kind in ("evidencia", "fuente", "rival"):
        keys = [k for k, _ in META_ORDER] + ["id", "estado", "imagen", "pie", "original", "dir", "transliteracion", "traduccion", "cita"]
        pairs, rest = keyed(body, keys)
        d = dict(pairs)
        stats["rivales" if kind == "rival" else "evidencias"] += 1
        ident = d.get("id", "")
        name = {"evidencia": "Evidencia", "fuente": "Fuente primaria", "rival": "Publicación analizada"}[kind]
        if kind != "fuente" and not d.get("url"):
            warn.append(f"{kind} sin url: {ident or arg}")
        est = ""
        if d.get("estado"):
            pend = not d["estado"].lower().startswith("verific")
            est = f'<span class="estado{" pend" if pend else ""}">{html.escape(d["estado"])}</span>'
            if pend:
                warn.append(f"{kind} no verificada: {ident or arg}")
        lbl = " · ".join(x for x in [f"{name} {ident}".strip(), arg] if x)
        h = [f'<div class="card evid{" rival" if kind == "rival" else ""}"{f" id={chr(34)}{html.escape(ident)}{chr(34)}" if ident else ""}><div class="card-lbl">{inline(lbl)}{est}</div>']
        meta = "".join(f"<dt>{lab}</dt><dd>{inline(d[k]) if k != 'url' else inline('[' + d[k] + '](' + d[k] + ')')}</dd>" for k, lab in META_ORDER if d.get(k))
        if meta:
            h.append(f'<dl class="evid-meta">{meta}</dl>')
        if d.get("imagen"):
            cap = f"<figcaption>{inline(d['pie'])}</figcaption>" if d.get("pie") else ""
            h.append(f'<figure><img src="{html.escape(d["imagen"])}" alt="{html.escape(arg or ident)}" loading="lazy">{cap}</figure>')
            stats["imagenes"] += 1
        if d.get("original"):
            rtl = ' dir="rtl"' if d.get("dir", "").lower() == "rtl" else ""
            h.append(f'<div class="evid-orig"{rtl}>{inline(d["original"])}</div>')
        if d.get("transliteracion"):
            h.append(f'<div class="evid-translit">{inline(d["transliteracion"])}</div>')
        if d.get("traduccion"):
            h.append(f'<p class="evid-trad">{inline(d["traduccion"])}</p>')
        if d.get("cita"):
            h.append(f"<blockquote>{inline(d['cita'])}</blockquote>")
        if rest:
            h.append(md_blocks(rest, stats))
        h.append("</div>")
        return "\n".join(h)
    if kind == "certeza":
        pairs, _ = keyed(body, [k for k, _, _ in CERT])
        d = dict(pairs)
        rows = "".join(f'<tr class="{c}"><td>{lab}</td><td>{para_or_inline(d[k], stats)}</td></tr>' for k, lab, c in CERT if d.get(k))
        return f'<table class="certeza"><tbody>{rows}</tbody></table>'
    if kind == "veredicto":
        return f'<div class="verdict"><div class="verdict-lbl">{inline(arg or "Veredicto")}</div>{md_blocks(body, stats)}</div>'
    if kind == "hl":
        return f'<div class="hl">{md_blocks(body, stats)}</div>'
    if kind == "nota":
        return f'<div class="footnote">{md_blocks(body, stats)}</div>'
    if kind in ("card", "def", "ficha"):
        lbl = f'<div class="card-lbl">{inline(arg)}</div>' if arg else ""
        return f'<div class="card">{lbl}{md_blocks(body, stats)}</div>'
    warn.append(f"directiva desconocida: {kind}")
    return md_blocks(body, stats)


def render_section_body(text, stats, warn):
    out, buf = [], []
    lines = text.split("\n")
    i = 0
    while i < len(lines):
        m = re.match(r"^:::\s*(\w+)\s*(.*)$", lines[i])
        if m:
            if buf:
                out.append(md_blocks("\n".join(buf), stats)); buf = []
            j = i + 1
            body = []
            while j < len(lines) and lines[j].strip() != ":::":
                body.append(lines[j]); j += 1
            if j >= len(lines):
                warn.append(f"directiva sin cerrar: {m.group(1)} {m.group(2)[:40]}")
            out.append(directive(m.group(1), m.group(2).strip(), "\n".join(body), stats, warn))
            i = j + 1
        else:
            buf.append(lines[i]); i += 1
    if buf:
        out.append(md_blocks("\n".join(buf), stats))
    return "\n".join(x for x in out if x)


def parse_front(src):
    m = re.match(r"^---\n(.*?)\n---\n", src, re.S)
    if not m:
        sys.exit("El borrador debe empezar con un bloque de metadatos entre lineas '---'.")
    meta = {}
    for ln in m.group(1).split("\n"):
        mm = re.match(r"^([\w-]+):\s*(.*)$", ln)
        if mm:
            v = mm.group(2).strip()
            if v.startswith("[") and v.endswith("]"):
                v = [x.strip().strip('"\'') for x in v[1:-1].split(",") if x.strip()]
            else:
                v = v.strip('"')
            meta[mm.group(1)] = v
    return meta, src[m.end():]


def slugify(t):
    t = t.lower()
    for a, b in zip("áéíóúüñ", "aeiouun"):
        t = t.replace(a, b)
    return re.sub(r"[^a-z0-9]+", "-", t).strip("-")[:40]


def normalizar(txt):
    """Repara errores de formato frecuentes de los borradores sin tocar el contenido:
    - bloque ':::tipo' sin cerrar antes de otro bloque, de una seccion '## ' o de '@grupo' -> inserta ':::';
    - cabecera '---' repetida en partes posteriores a la primera -> se elimina."""
    lines = txt.split("\n")
    out, abierto, cerrados = [], False, 0
    i = 0
    # la cabecera inicial (--- ... ---) se copia tal cual
    if lines and lines[0].strip() == "---":
        j = 1
        while j < len(lines) and lines[j].strip() != "---":
            j += 1
        out = lines[: j + 1]
        i = j + 1
    while i < len(lines):
        ln = lines[i]
        abre = re.match(r"^:::\s*\w+", ln)
        if abierto and (abre or re.match(r"^(## |@grupo\s)", ln)):
            while out and not out[-1].strip():
                out.pop()
            out += [":::", ""]
            abierto = False
            cerrados += 1
        if abre:
            abierto = True
        elif ln.strip() == ":::":
            abierto = False
        out.append(ln)
        i += 1
    if abierto:
        out.append(":::")
        cerrados += 1
    if cerrados:
        print(f"[normalizar] {cerrados} bloque(s) sin cerrar reparado(s)", file=sys.stderr)
    return "\n".join(out)


def build(path, out=None, check=False):
    if os.path.isdir(path):  # carpeta de dossier: concatena partes/p*.md en borrador.md
        import glob
        partes = sorted(glob.glob(os.path.join(path, "partes", "p*.md")))
        if not partes:
            sys.exit("No hay partes/p*.md en " + path)
        txt = "\n\n".join(open(x, encoding="utf-8-sig").read().replace("\r\n", "\n").strip("\n") for x in partes) + "\n"
        txt = normalizar(txt)
        path = os.path.join(path, "borrador.md")
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write(txt)
    src = open(path, encoding="utf-8-sig").read().replace("\r\n", "\n")
    meta, body = parse_front(src)
    stats = dict(silogismos=0, objeciones=0, cadenas=0, evidencias=0, rivales=0, tablas=0, imagenes=0, secciones=0)
    warn = []
    for req in ("id", "slug", "titulo", "apartado", "paleta", "resumen"):
        if not meta.get(req):
            warn.append(f"falta metadato obligatorio: {req}")
    # secciones
    sections, group, cur = [], None, None
    pre = []
    for ln in body.split("\n"):
        g = re.match(r"^@grupo\s+(.+)$", ln)
        h = re.match(r"^##\s+(.+?)(?:\s*\{#([\w-]+)\})?\s*$", ln)
        if g:
            group = g.group(1).strip(); continue
        if h:
            cur = {"title": h.group(1).strip(), "id": h.group(2) or slugify(h.group(1)), "group": group, "lines": []}
            group = None
            sections.append(cur); continue
        (cur["lines"] if cur else pre).append(ln)
    if any(x.strip() for x in pre):
        warn.append("hay texto antes de la primera seccion '## ' (se ignora)")
    ids = [s["id"] for s in sections]
    if len(set(ids)) != len(ids):
        warn.append("ids de seccion duplicados")
    toc, secs_html = [], []
    for n, s in enumerate(sections, 1):
        stats["secciones"] += 1
        if s["group"]:
            toc.append(f'  <div class="toc-group">{html.escape(s["group"])}</div>')
        plain_title = re.sub(r"[*{}]|\w+\|", "", s["title"])
        toc.append(f'  <a href="#{s["id"]}">{roman(n)}. {html.escape(plain_title)}</a>')
        secs_html.append(f'<!-- {roman(n)} -->\n<section id="{s["id"]}">\n  <div class="sec-label">Sección {roman(n)}</div>\n  <h2>{inline(s["title"])}</h2>\n'
                         + render_section_body("\n".join(s["lines"]), stats, warn) + "\n</section>")
    css, js = base_parts()
    pal = meta.get("paleta", "esmeralda")
    if pal not in PALETAS:
        warn.append(f"paleta desconocida '{pal}', se usa esmeralda"); pal = "esmeralda"
    for a, b in PALETAS[pal].items():
        css = css.replace(a, b)
    aditivo = ADITIVO_CSS
    for a, b in PALETAS[pal].items():
        aditivo = aditivo.replace(a, b)
    title = meta.get("titulo", "")
    cover_title = "<br>".join(inline(x.strip()) for x in title.split("|"))
    plain = re.sub(r"\s*\|\s*", " ", title)
    verse = ""
    if meta.get("epigrafe"):
        orig = f'<span class="gr-lg"{" dir=" + chr(34) + "rtl" + chr(34) if meta.get("epigrafe_dir") == "rtl" else ""}>{inline(meta["epigrafe_original"])}</span>' if meta.get("epigrafe_original") else ""
        ref = f'<br><span style="font-size:.78rem;color:var(--rule);">{inline(meta["epigrafe_ref"])}</span>' if meta.get("epigrafe_ref") else ""
        verse = f'<div class="cover-verse">{orig}<em>{inline(meta["epigrafe"])}</em>{ref}</div>'
    words = len(re.sub(r"<[^>]+>", " ", "\n".join(secs_html)).split())
    stats["palabras"] = words
    # control editorial minimo (QUALITY_CONTROL.md §5); no aplica al ejemplo de plantilla (D00)
    if meta.get("id") != "D00":
        todo = "\n".join(secs_html)
        if words < 5000:
            warn.append(f"extension insuficiente: {words} palabras (minimo orientativo 5.000)")
        if stats["silogismos"] < 5:
            warn.append(f"solo {stats['silogismos']} silogismos (minimo 5, salvo justificacion)")
        if 'class="certeza"' not in todo:
            warn.append("falta la escala de certeza (:::certeza) en la conclusion")
        if 'class="verdict"' not in todo:
            warn.append("falta el veredicto final (:::veredicto)")
        if stats["cadenas"] < 2:
            warn.append(f"solo {stats['cadenas']} cadenas de debate (minimo 2)")
        if stats["evidencias"] < 4:
            warn.append(f"solo {stats['evidencias']} fichas de evidencia/fuente primaria (minimo orientativo 4)")
        if not re.search(r"bibliograf", todo, re.I):
            warn.append("falta la seccion de bibliografia")
        if not re.search(r"herramientas para el debate", todo, re.I):
            warn.append("falta la seccion «Herramientas para el debate»")
    colofon = (f'<div class="colofon">Defendiendo la Fe · Dossier {html.escape(meta.get("id", ""))} · '
               f'{html.escape(meta.get("fecha", ""))}. Las fuentes se citan con su localización para que el lector pueda comprobarlas. '
               f'Las citas de publicaciones ajenas son breves y se reproducen con fines de crítica y estudio.</div>')
    doc = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="description" content="{html.escape(meta.get('resumen', ''), quote=True)}">
<title>Dossier Apologético · {html.escape(plain)}</title>
<style>{css}{aditivo}</style>
</head>
<body>

<button id="toc-btn" aria-controls="toc-panel" aria-expanded="false" aria-label="Abrir índice">
  <span class="hbars" aria-hidden="true"><span></span><span></span><span></span></span>
  Índice
</button>
<div id="toc-overlay" aria-hidden="true"></div>
<nav id="toc-panel" aria-label="Índice">
  <div class="toc-spacer"></div>
  <div class="toc-title">Contenido</div>
{chr(10).join(toc)}
</nav>

<div id="main">

<!-- COVER -->
<div class="cover">
  <div class="cover-eyebrow">{inline(meta.get('eyebrow', 'Dossier Apologético'))}</div>
  <h1 class="cover-title">{cover_title}</h1>
  <p class="cover-sub">{inline(meta.get('subtitulo', ''))}</p>
  {verse}
</div>

{chr(10).join(secs_html)}

{colofon}
</div>

<script>{js}</script>
</body>
</html>
"""
    if not check:
        out = out or os.path.join(os.path.dirname(path), "build", meta.get("slug", "dossier") + ".html")
        os.makedirs(os.path.dirname(out), exist_ok=True)
        with open(out, "w", encoding="utf-8", newline="\n") as f:
            f.write(doc)
    report = {"salida": out, "meta": {k: meta.get(k) for k in ("id", "slug", "titulo", "apartado", "paleta")}, "stats": stats, "avisos": warn}
    print(json.dumps(report, ensure_ascii=False, indent=1))
    return report


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    if not args:
        sys.exit(__doc__)
    o = sys.argv[sys.argv.index("-o") + 1] if "-o" in sys.argv else None
    if o:
        args = [a for a in args if a != o]
    build(args[0], o, "--check" in sys.argv)
