# Auditoría de diseño y plan de rediseño general

> Alcance: **todo lo que rodea a los dossieres** (inicio, cabecera, navegación, índices de apartado, buscador, página
> contenedora del dossier, pie). **Fuera de alcance, intocable:** el interior de los 114 HTML de `static/refutaciones/`.
> Los nombres de apartados, subapartados y dossieres no cambian. Las rutas no cambian.

## 1. Estado actual (auditado sobre el código; Hugo no instalado ⇒ sin compilación local, ver BLOCKERS B1)

| Elemento | Qué hay | Problema |
|---|---|---|
| Tema | PaperMod sin apenas adaptación + `assets/css/extended/faith-theme.css` (302 líneas) | Estética de blog personal, no de biblioteca |
| Inicio | `homeInfoParams`: bloque con enlaces-píldora a 12 apartados, 3 «destacados» y 4 calendarios; debajo, lista paginada de **todas** las páginas por fecha | No hay jerarquía ni puerta de entrada temática; 114 entradas en orden cronológico de 10 en 10 |
| Cabecera | 12 entradas de menú en una fila, cada una con una daga «†» y fondo píldora al pasar | Se desborda en pantallas medias; sin agrupación |
| Apartados | `_index.md` con lista manual de enlaces + listado automático de tarjetas idénticas (título, 32 palabras, fecha) | Doble listado; tarjetas sin metadatos útiles; sin filtro ni orden |
| Buscador | Fuse.js sobre `index.json` con el `.Plain` del envoltorio | Solo busca en el título y en una frase: el contenido real (el HTML del dossier) no está indexado |
| Página de dossier | Título + cita con enlace + iframe de 78vh | Doble barra de desplazamiento; sin contexto (apartado, extensión, temas, relacionados) |
| Decoración | Tres degradados radiales en `body`, cruces y cruces de Malta en `::before/::after` de cabecera, navegación, tarjetas, h1, h2 y bloque de inicio; marca de agua girada | Ruido visual repetitivo; exactamente la «estética genérica» que el propietario quiere evitar |
| Tipografía | Libre Baskerville + IBM Plex Sans | Correcta pero sin relación con la de los dossieres (EB Garamond / Cinzel / Source Sans 3) |
| Accesibilidad | Contraste suficiente; decoraciones en `content:` leídas por lectores de pantalla; sin «saltar al contenido» propio | Mejorable |
| Taxonomías | `categories` = apartado; `tags` libres e inconsistentes (`dossier`, `apologetica`…) | No sirven para filtrar por controversia o disciplina |

## 2. Dirección artística: «Scriptorium»

Una biblioteca de investigación, no un blog. Referentes: catálogos de bibliotecas digitales (e-codices, Biblioteca Apostólica
Vaticana Digital), enciclopedias académicas (Stanford Encyclopedia of Philosophy), revistas universitarias y la tradición
tipográfica del libro litúrgico (texto negro, **rúbrica** roja, versalitas).

- **Color**: papel `#f6f2e8`, tinta `#1b1814`, un único acento de **rúbrica** `#7a1f1f` (títulos de sección, enlaces activos,
  filetes); gris cálido para metadatos. Oro solo como filete de 1 px. Sin degradados, sin sombras, sin marcas de agua.
- **Tipografía**: EB Garamond (texto y títulos; es la de la familia dominante de dossieres, lo que une sitio y contenido) y
  Source Sans 3 para interfaz y metadatos en versalitas espaciadas. Una sola cruz, en el sello de la cabecera.
- **Composición**: retícula de catálogo. Filetes horizontales finos en lugar de tarjetas con borde y sombra. Mucho blanco.
  Numeración y signaturas («D17», «Historia · 24 dossieres») como elementos tipográficos.
- **Movimiento**: ninguno salvo transiciones de color de 120 ms. `prefers-reduced-motion` respetado.
- **Modo oscuro**: se conserva (PaperMod), con la misma paleta invertida.

## 3. Qué se construye

1. **Cabecera en dos niveles**: sello + título; fila primaria con los apartados de contenido; fila secundaria discreta
   (Idiomas, Colaboradores, Calendario, Búsqueda). Menú plegable en móvil. Mismos nombres y URLs.
2. **Inicio como portada de biblioteca**: lema; buscador grande; «Colecciones» (los apartados existentes, con su descripción y
   su número de dossieres, en lista tipográfica de dos columnas); «Nuevas investigaciones» (los dossieres de la colección 2026);
   «Explorar por controversia» (Islam, Protestantismo, Ortodoxia, Restauracionismo, Ateísmo, Judaísmo y crítica histórica);
   «Rutas de estudio» (itinerarios ordenados de 5-7 dossieres); calendario litúrgico en el pie de la portada.
3. **Índice de apartado como catálogo**: una fila por dossier (título, resumen, extensión, temas), orden alfabético o por
   fecha, **filtro instantáneo** por texto y por controversia. Sustituye a las tarjetas; la lista manual del `_index.md` se conserva.
4. **Índice general** (`/indice/`): todos los dossieres, alfabético, con salto por letra, y **directorio de fuentes rivales**
   refutadas (desde `ARTICLE_REFUTATION_REGISTRY.json`).
5. **Buscador**: `index.json` ampliado con apartado, temas, controversia y los **encabezados internos** de cada dossier
   (extraídos del HTML en compilación con `readFile`, sin modificar el HTML). No se indexa el texto completo (pesaría varios MB).
6. **Página contenedora del dossier**: migas, ficha (apartado, extensión, temas), botón «Leer a pantalla completa», iframe a
   altura de ventana sin doble desplazamiento, y «Dossieres relacionados». El interior del iframe no se toca.
7. **Pie**: mapa de apartados, nota editorial y metodológica, enlace al índice general.
8. **Metadatos aditivos**: los dossieres nuevos llevan `area`, `dossier_id`, `palabras`, `coleccion`. Para los antiguos, que no
   pueden modificarse, los mismos datos se aportan desde un archivo `data/dossieres.yaml` generado del mapa temático.

## 4. Qué NO se toca

- Ningún archivo de `static/refutaciones/`. Ningún envoltorio `.md` existente. Ningún título ni URL.
- El shortcode `dossier_iframe` conserva su marcado (`.dossier-embed`, `.dossier-link`); solo cambia el CSS exterior.
- `faith-theme.css` no entra en los iframes, así que su reescritura no puede alterar el interior de los dossieres. Aun así,
  tras el rediseño se ejecuta `manifest.py verify` y se comparan los HTML servidos byte a byte con el commit base.

## 5. Verificación prevista

Compilación con Hugo extended 0.147.8 (misma versión que CI); pruebas a 375, 768 y 1280 px; navegación por teclado;
contraste AA; comprobación de las 114 + 50 rutas y de todos los `aliases`; búsqueda; `manifest.py verify`.

## 6. Estado

- [x] Auditoría.
- [x] Prototipo estático de la portada y del catálogo (`_proyecto/diseno/`), para validar la dirección antes de portarla a Hugo.
- [x] Portado a plantillas Hugo (2026-11-14) y compilado con Hugo 0.147.8.
- [x] Pruebas a 375 / 768 / 1024 px, modo oscuro, menú móvil, filtros, búsqueda, rutas e integridad de los dossieres.
- [ ] Pendiente: prueba con lector de pantalla y en Safari/iOS; directorio de fuentes rivales en el índice general; página propia de rutas de estudio.
