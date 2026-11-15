# PLAN MAESTRO — Biblioteca de Apologética Católica "Defendiendo la Fe"

> **Toda sesión nueva empieza leyendo, en este orden:** `HANDOFF.md` → `PROJECT_PROGRESS.md` → `BLOCKERS.md` → este plan.
> El encargo original íntegro del propietario está resumido en la sección 9; sus reglas inviolables, en la 2.

## 1. Arquitectura real del repositorio (auditada el 2026-11-14)

| Elemento | Realidad |
|---|---|
| Generador | **Hugo** (extended 0.147.8 en CI) + tema **PaperMod** (submódulo git en `themes/PaperMod`) |
| Despliegue | GitHub Actions → Cloudflare Pages **en cada push a `main`**. ⇒ **Nunca hacer push a `main`** sin permiso expreso. |
| Rama de trabajo | `proyecto/biblioteca-apologetica` (base: commit `75cafb8`) |
| Apartados (menú) | Filosofia, Historia, Biblia, Exegesis, Refutaciones, Doctrina, Respondiendo al Islam, Santos, Idiomas, Colaboradores, Calendario, Busqueda |
| Dossier = | 1 archivo HTML **autocontenido** en `static/refutaciones/<slug>.html` (CSS y JS inline, fuentes de Google) **+** 1 envoltorio `content/<apartado>/<slug>-dossier.md` que lo incrusta con el shortcode `dossier_iframe` |
| Dossieres existentes | 102 dossieres + 12 lecciones de idiomas = 114 HTML (~770.000 palabras). 112 hojas de estilo distintas: **no hay plantilla única**; hay "familias" visuales |
| Familia visual dominante | Cinzel + EB Garamond + Source Sans 3 (26 dossieres; p. ej. `paracleto-dossier.html`): botón "Índice" + panel lateral, `.cover`, `section` + `.sec-label`, `.card`, `.syllogism`, `.obj`, `.verdict`, `.hl`, tablas, `.footnote` |
| Estilo del sitio | `assets/css/extended/faith-theme.css` (solo afecta a las páginas Hugo; **no** entra en los iframes de los dossieres) |
| Búsqueda | PaperMod + Fuse.js sobre `index.json` (`layouts/index.json`). Solo indexa el resumen del envoltorio, **no** el texto del dossier |
| Índices de apartado | Listas manuales en cada `content/<apartado>/_index.md` + listado automático de `layouts/_default/list.html` |

## 2. Reglas inviolables (del propietario)

1. No renombrar apartados, subapartados ni dossieres. No eliminar, reescribir, resumir ni alterar dossieres antiguos (texto, citas, imágenes, conclusiones, **diseño interno**). No romper rutas ni funcionalidades.
2. Errores hallados en dossieres antiguos → solo a `RECOMENDACIONES_DOSSIERES_ANTIGUOS.md`. No se corrigen sin permiso.
3. Los 50 dossieres nuevos usan el **mismo lenguaje visual** que los antiguos (familia dominante, ver §5). Componentes nuevos solo aditivos.
4. Nada inventado: ni citas, ni páginas, ni DOI, ni manuscritos, ni consensos, ni artículos rivales, ni publicaciones de X. Lo no verificado se marca como tal y no se usa como prueba.
5. Sin imágenes fabricadas de documentos. Solo dominio público / licencias abiertas / cita breve con enlace.
6. Sin despliegues a producción, sin secretos en el repo, sin TikTok.
7. Compromiso doctrinal católico **sin** rebajar el rigor: reconocer dificultades reales, no deformar al rival, criticar ideas y no personas. Frente al islam, defender el núcleo niceno sin disputas intracristianas.

## 3. Sistema de protección

- `scripts/manifest.py build` → `EXISTING_CONTENT_MANIFEST.json` (263 archivos, sha256, palabras, títulos, rutas) y `PROTECTED_FILES.json` (241 **ESTRICTO**, 22 **ADITIVO**), calculados sobre los blobs del commit base.
- `scripts/manifest.py verify` → falla si cualquier archivo ESTRICTO difiere del commit base (árbol de trabajo y HEAD). **Ejecutar antes de cada commit y al final de cada lote.**
- ESTRICTO = `static/refutaciones/*.html` + todo `content/**/*.md` que no sea `_index.md`. ADITIVO = `_index.md`, `hugo.toml`, `layouts/`, `assets/`, `archetypes/` (pueden evolucionar para el rediseño, sin renombrar ni romper rutas).
- Los investigadores (subagentes) solo escriben en `_proyecto/investigadores/Rxx/` y `_proyecto/dossieres/Dxx/`. La integración en `static/` y `content/` la hace únicamente el director.

## 4. Estructura persistente (`_proyecto/`)

| Archivo / carpeta | Contenido |
|---|---|
| `HANDOFF.md` | Estado exacto y siguiente acción. Se reescribe al final de cada sesión |
| `PROJECT_PROGRESS.md` | Bitácora cronológica por fase |
| `BLOCKERS.md` | Bloqueos y limitaciones del entorno |
| `QUALITY_CONTROL.md` | Estándar editorial y lista de aceptación por dossier |
| `DESIGN_AUDIT.md` | Auditoría de diseño y decisiones del rediseño |
| `RECOMENDACIONES_DOSSIERES_ANTIGUOS.md` | Errores/mejoras detectados en contenido protegido (no aplicados) |
| `EXISTING_CONTENT_MANIFEST.json`, `PROTECTED_FILES.json` | Protección |
| `EXISTING_TOPIC_MAP.json` | Mapa temático de los 102 dossieres (fusionado desde `audit/topic_map_parts/`) |
| `OPPOSING_APOLOGETICS_REGISTRY.json` | Directorio de webs/autores rivales |
| `ARTICLE_REFUTATION_REGISTRY.json` | Artículos rivales concretos analizados/refutados |
| `TOPIC_CANDIDATES.json` | 100-150 candidatos con matriz de evaluación |
| `DOSSIER_REGISTRY.json` | Los 50 aprobados: estado, responsable, revisor, tesis… |
| `RESEARCH_TASKS.json` | Tareas por investigador |
| `SOURCE_REGISTRY.json` | Registro central de fuentes (clases A-F, estado de verificación) |
| `investigadores/Rxx/` | Espacio aislado de cada investigador (informes de exploración, notas) |
| `dossieres/Dxx-slug/` | Expediente: `expediente.json`, `fuentes.json`, `borrador.md`, `revision_documental.md`, `revision_adversarial.md`, `correcciones.md` |
| `plantilla/` | Plantilla canónica de dossier nuevo + `scripts/build_dossier.py` |
| `scripts/` | `manifest.py`, constructores y verificadores |

Estados de dossier: CANDIDATO → APROBADO → INVESTIGANDO → FUENTES_VERIFICADAS → BORRADOR → REVISION_ADVERSARIAL → CORRECCIONES → APROBACION_EDITORIAL → INTEGRADO → VERIFICADO.

## 5. Plantilla de los dossieres nuevos

- Base: hoja de estilo de la familia dominante (Cinzel / EB Garamond / Source Sans 3), tomada **literalmente** de un dossier existente representativo; variación de paleta por área como ya hacen los antiguos.
- Los investigadores redactan en Markdown estructurado con bloques semánticos (`:::silogismo`, `:::objecion`, `:::evidencia`, `:::fuente`, `:::veredicto`…); `build_dossier.py` genera el HTML autocontenido. Así el diseño es uniforme y el texto es auditable y versionable.
- Componentes aditivos permitidos (mismo lenguaje visual): ficha de evidencia documental con metadatos, cadena de debate (argumento → objeción → respuesta → contraobjeción → contrarréplica), ficha "artículo rival analizado", escala de certeza en la conclusión.

## 6. Equipo

- Director/editor/auditor: Fable 5.2 (sesión principal).
- 10 investigadores: subagentes **Haiku 5.5, esfuerzo alto** (`model: haiku`, `effort: high`), reales e independientes, con acceso web. Perfiles en `RESEARCH_TASKS.json`.
- Revisión cruzada: (1) exactitud documental por un investigador distinto; (2) revisión adversarial por otro investigador que adopta la posición del mejor adversario; (3) revisión final del director.

## 7. Fases

| Fase | Contenido | Estado → ver `PROJECT_PROGRESS.md` |
|---|---|---|
| 0 | Auditoría, protección, mapa temático, infraestructura | |
| 1 | Exploración de apologética rival (islam, protestantismo, ortodoxia, mormonismo, TJ, ateísmo, judaísmo) + X | |
| 2 | 100-150 candidatos → matriz → 50 temas → asignación | |
| 3 | Pilotos (4-6 dossieres de áreas distintas) → ajuste del estándar | |
| 4 | Rediseño general del sitio (sin tocar el interior de los dossieres) | |
| 5-6 | Investigación paralela, redacción, revisiones | |
| 7 | Integración por lotes de ~5-8 con verificación | |
| 8 | Auditoría global | |
| 9 | Entrega | |

## 8. Presupuesto realista

50 dossieres × 5.000-12.000 palabras ≈ 300.000-500.000 palabras + investigación + 2 revisiones cada uno ⇒ **varias sesiones**. Ninguna sesión debe terminar sin actualizar `HANDOFF.md`. El trabajo no continúa solo entre sesiones: el propietario debe reanudar ("continúa el proyecto").

## 9. Resumen del encargo original (2026-11-14)

Rediseño estético general (biblioteca digital / enciclopedia académica; sin estética genérica de IA) + **exactamente 50 dossieres nuevos**, elegidos autónomamente por el director tras auditar los existentes e investigar la apologética rival real (prioridad: islam; también protestante, ortodoxa, mormona, TJ, atea, judía) y X. Cada dossier: resumen ejecutivo, formulación del problema, definiciones, contexto, fuentes primarias con ficha completa, filología, evidencia documental, estado de la cuestión, argumentación, 5-10 silogismos desarrollados (premisas justificadas, objeciones, evaluación de fuerza), mejor versión de la posición contraria, refutación, cadenas de contraobjeciones, comparación de evidencias, conclusión graduada (demostrado / probable / defendible / abierto), herramientas de debate, bibliografía clasificada. Refutación de artículos rivales concretos con estructura: argumento original → reconstrucción lógica → examen de sus fuentes → refutación → contraobjeción → contrarréplica → evaluación. Registro de fuentes con trazabilidad. Revisión adversarial obligatoria. Idioma: español académico, sin relleno.
