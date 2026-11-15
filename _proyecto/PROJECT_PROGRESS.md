# Bitácora del proyecto

## Sesión 1 — 2026-11-14

### FASE 0 — Auditoría, protección, infraestructura ✅
- Repositorio auditado: Hugo + PaperMod; dossieres = HTML autocontenido en `static/refutaciones/` + envoltorio `.md` con iframe. 102 dossieres + 12 lecciones de idiomas (~770.000 palabras). 112 hojas de estilo distintas.
- Rama `proyecto/biblioteca-apologetica` creada desde `75cafb8`. `main` despliega a Cloudflare en cada push: **no tocar**.
- `scripts/manifest.py` → manifiesto (263 archivos), 241 en protección ESTRICTA; `verify` pasa.
- Mapa temático: 15 auditores Haiku leyeron íntegramente los 102 dossieres → `EXISTING_TOPIC_MAP.json` (tesis, cuestiones, argumentos, textos, autores, objeciones, temas adyacentes sin desarrollar, posibles errores).
- `RECOMENDACIONES_DOSSIERES_ANTIGUOS.md`: sospechas de error detectadas en contenido protegido (**no aplicadas**).
- Plantilla de dossier nuevo: `scripts/build_dossier.py` (CSS literal de `paracleto-dossier.html`; paletas esmeralda / pergamino / marino tomadas de dossieres existentes; componentes aditivos). Formato: `plantilla/FORMATO_BORRADOR.md`; ejemplo: `plantilla/ejemplo.md`. Probado en navegador (fuentes, paleta, sin desbordamiento).
- Estándar: `QUALITY_CONTROL.md`.

### Lagunas detectadas en la web (del mapa temático)
Sin dossier propio: papado/primado romano · resurrección · problema del mal y ocultamiento divino · argumentos cosmológicos · mormonismo (0) · Testigos de Jehová (0) · canon deuterocanónico · Is 7:14 · Dn 9 · Sal 22 · iʿjāz y «milagros científicos» · manuscritos coránicos (Saná, Birmingham, qirāʾāt; solo parcial) · «Mahoma en la Biblia» (Cant 5:16, Dt 18) · versos satánicos · esencia-energías · Honorio (solo de pasada) · órdenes anglicanas · miticismo · alma y neurociencia.

### FASE 1 — Exploración de apologética rival ✅
- 10 investigadores Haiku 5.5 (esfuerzo alto) con `investigadores/PROMPT_FASE1_exploracion.md`. Nueve se cortaron por el límite
  de uso; R01, R09 y R10 se reanudaron y entregaron. R02, R03, R06, R07, R08 entregaron JSON sin informe narrativo.
- Resultado: **102 sitios, 156 artículos leídos, 112 candidatos** (`scripts/consolidar_fase1.py`).
- Limitaciones documentadas por los investigadores: X inaccesible (HTTP 402); Reddit inaccesible; aomin.org, Ligonier, TGC,
  De Gruyter, SAGE, MUSE bloquean; WebFetch devuelve paráfrasis, no texto literal; R10 quedó por debajo del mínimo (6 candidatos).

### FASE 2 — Selección de los 50 temas ✅
- 132 candidatos (112 de investigadores + 20 del director) → 50 dossieres (`scripts/seleccion_fase2.py`).
- Distribución: Islam 15 · Crítica histórica y judaísmo 9 · Protestantismo 8 · Ateísmo y naturalismo 7 · Restauracionismo y
  unitarismo 6 · Ortodoxia oriental 5. Cinco dossieres por investigador como responsable; revisores documental y adversarial
  siempre distintos del autor.
- Documento: `SELECCION_TEMATICA.md` (tesis, adversario, justificación de no duplicidad y motivos de descarte).

### FASE 3 — Pilotos (borradores entregados; revisiones en curso)
- Prompts: `investigadores/PROMPT_DOSSIER.md` (investigación + redacción por partes) y `PROMPT_REVISION.md` (documental / adversarial).
- Los seis se cortaron una vez por el límite de uso y se reanudaron. Todos compilan con `build_dossier.py` sin avisos de estructura:

| Dossier | Autor | Palabras | Silog. | Cadenas | Evid. | Fuentes (verif./parcial/no verif.) | Primarias verificadas |
|---|---|---|---|---|---|---|---|
| D01 Saná | R03 | 13.125 | 6 | 2 | 5 | 3 / 12 / 14 | 2 |
| D17 Mateo 16:18 | R04 | 12.901 | 7 | 3 | 8 | 5 / 11 / 18 | 3 |
| D26 Honorio-Vigilio-Liberio | R05 | 14.985 | 7 | 4 | 10 | 7 / 11 / 14 | 4 |
| D31 607 a.C./1914 | R06 | 16.650 | 7 | 3 | 8 | 1 / 25 / 14 | 1 |
| D35 Ocultamiento divino | R07 | 14.435 | 6 | 3 | 12 | 12 / 12 / 12 | 10 |
| D41 Resurrección | R08 | 15.076 | 7 | 3 | 14 | 9 / 32 / 4 | 8 |

**Lecciones de los pilotos**
1. La estructura intelectual funciona: silogismos con justificación de premisas, cadenas de debate, conclusión graduada, y
   notas honestas sobre lo no verificado. Varios autores corrigieron la tesis del expediente cuando las fuentes no la sostenían
   (p. ej. D17: no todos los Padres que predican «la confesión» afirman el oficio petrino).
2. **El cuello de botella es la verificación documental.** Solo D35 y D41 alcanzan el mínimo de 8 primarias verificadas. Causas:
   WebFetch devuelve resúmenes; muchos repositorios bloquean (augustinus.it, De Gruyter, PMC, equip.org); los PDF grandes no se leen.
   Ningún dossier puede pasar a APROBACION_EDITORIAL con este nivel: necesitan una **fase de refuerzo documental**.
3. Los borradores salen más largos de lo previsto (13-16 mil palabras frente a 9-12 mil): habrá que recortar en la edición.
4. Errores de formato recurrentes (bloques `:::` sin cerrar): el constructor ya los repara (`normalizar`).
5. Algunos «artículos rivales de partida» de los expedientes no eran rivales (reseñas, apologética cristiana): hay que depurarlos.

### FASE 4 — Rediseño general ✅ (implementado y probado en local; sin desplegar)
- Hugo extended 0.147.8 instalado con permiso del propietario (misma versión que CI).
- Archivos: `layouts/partials/header.html`, `layouts/_default/list.html`, `layouts/_default/single.html`, `layouts/_default/indice.html`,
  `layouts/partials/{extend_head,extend_footer,fila_dossier}.html`, `layouts/index.json`, `assets/css/extended/faith-theme.css`,
  `content/indice.md`, `data/{dossieres.json,controversias.yaml,rutas.yaml}`, 4 líneas en `hugo.toml`.
- Qué cambia: cabecera en dos niveles, portada de biblioteca (colecciones, últimas incorporaciones / nuevas investigaciones,
  controversias, rutas de estudio, calendario), catálogo de apartado con filtro por texto y por controversia, índice general
  `/indice/`, página de dossier con ficha + relacionados + pantalla completa, pie con mapa, buscador que indexa los encabezados
  internos de cada dossier y admite `?q=` desde la portada.
- Verificado: compila (737 páginas, 46 de paginación, 439 alias); **ninguna ruta perdida** respecto al sitio original (solo se añade
  `/indice/`); 0 enlaces internos rotos; los 114 HTML de `refutaciones/` idénticos byte a byte; `manifest.py verify` OK; sin
  desbordamiento a 375, 768 y 1024 px; modo oscuro; menú móvil; filtros; búsqueda.
- No verificado: lectores de pantalla reales, Safari/iOS, rendimiento con Lighthouse.

### Incidencias
- Límite de 20 subagentes simultáneos; límite de uso de 5 h alcanzado una vez (9 agentes cortados).
- Hugo no está instalado en la máquina (ver `BLOCKERS.md`).
- Las capturas del navegador integrado fallan a menudo; se verifica con inspección DOM.
