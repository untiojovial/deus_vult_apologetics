# HANDOFF — estado exacto y siguiente acción

> Actualizado: 2026-11-14 (sesión 1). Leer después: `PROJECT_PROGRESS.md`, `BLOCKERS.md`, `PROJECT_MASTER_PLAN.md`.

## Dónde estamos
- Fases 0, 1, 2 y 4 **terminadas**. Fase 3 (pilotos): **seis borradores entregados**, estado BORRADOR; revisiones pendientes/en curso.
- Rediseño «Scriptorium» implementado en plantillas Hugo y probado en local (ver `PROJECT_PROGRESS.md`, Fase 4). **Sin desplegar**:
  está en el árbol de trabajo de la rama `proyecto/biblioteca-apologetica`, sin commit.
- Pilotos: D01, D17, D26, D31, D35, D41 en `dossieres/Dxx-slug/` (`partes/`, `borrador.md`, `build/<slug>.html`, `fuentes.json`, `notas.md`).
  Todos compilan. Problema común: pocas fuentes verificadas literalmente (BLOCKERS B8).
- Nada nuevo integrado todavía en `static/` ni `content/` (salvo `content/indice.md`, página del índice general).
- `python _proyecto/scripts/manifest.py verify` → OK (241 archivos protegidos intactos).

## Siguiente acción (en orden)
1. Mirar si existen `revision_adversarial.md` / `revision_documental.md` en las carpetas de los pilotos (se lanzaron revisiones
   adversariales al final de la sesión 1; pueden haberse cortado). Relanzar las que falten con `investigadores/PROMPT_REVISION.md`
   y los revisores de `DOSSIER_REGISTRY.json`.
2. Resolver B8 con el propietario (cómo verificar citas literalmente). Según su respuesta, lanzar la **fase de refuerzo documental**
   de cada piloto (el autor reabre las fuentes primarias y sustituye lo PARCIAL / NO_VERIFICADA por texto verificado o lo retira).
3. Correcciones del autor (`correcciones.md`) respondiendo a las dos revisiones; el director lee el borrador entero, recorta a la
   extensión prevista y decide APROBACION_EDITORIAL (`scripts/estado.py`).
4. `python _proyecto/scripts/integrar.py Dxx …` → `python _proyecto/scripts/datos_sitio.py` no hace falta para los nuevos (llevan
   metadatos propios) → compilar con Hugo → `manifest.py verify`.
5. Ajustar `PROMPT_DOSSIER.md` con las lecciones de los pilotos (límite de extensión, depurar rivales, mínimo de verificadas) y
   lanzar los 44 restantes en tandas de ≤ 6 (ver `DOSSIER_REGISTRY.json`, estado APROBADO).
6. Fases 8-9: auditoría global y entrega.

## Comandos útiles
- Hugo: `"%LOCALAPPDATA%/Microsoft/WinGet/Packages/Hugo.Hugo.Extended_Microsoft.Winget.Source_8wekyb3d8bbwe/hugo.exe" server --buildFuture`
  (o la configuración `hugo` de `.claude/launch.json`).
- Construir un dossier: `python _proyecto/scripts/build_dossier.py _proyecto/dossieres/Dxx-slug`
- Estado de los 50: `python _proyecto/scripts/integrar.py --lista`

## Cómo reanudar
El propietario escribe «continúa el proyecto». La sesión nueva lee este archivo y sigue desde «Siguiente acción».

## Decisiones ya tomadas (no reabrir)
- Los dossieres nuevos usan la familia visual «Índice lateral + portada» (CSS literal de `paracleto-dossier.html`), con paletas
  esmeralda (islam), pergamino (historia/Biblia/patrística) y marino (doctrina/filosofía/exégesis).
- Los investigadores escriben Markdown estructurado; solo el director genera HTML e integra.
- No se corrige contenido antiguo: solo `RECOMENDACIONES_DOSSIERES_ANTIGUOS.md`.
- No se hace push a `main`.

## Pendiente de decisión del propietario
- Permiso para instalar Hugo (`winget install Hugo.Hugo.Extended`).
- Permiso para commits locales en la rama del proyecto.
- Si quiere que se aplique alguna de las correcciones de `RECOMENDACIONES_DOSSIERES_ANTIGUOS.md`.
