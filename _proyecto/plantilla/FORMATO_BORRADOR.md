# Formato de borrador de dossier (`borrador.md`)

El investigador escribe **solo** `borrador.md` (Markdown estructurado). El director lo convierte en HTML con
`python _proyecto/scripts/build_dossier.py <borrador.md>`, que aplica el diseño de los dossieres existentes.
**No escribas HTML ni CSS.** Ejemplo completo y funcional: `_proyecto/plantilla/ejemplo.md`.

## 1. Cabecera (obligatoria)

```
---
id: D07
slug: honorio-sexto-concilio          (minúsculas, guiones; será el nombre del archivo)
titulo: Primera línea del título: | Segunda línea     (la barra | parte el título en la portada)
subtitulo: Frase que describe el alcance del dossier
eyebrow: Dossier Apologético · Área · Subárea
epigrafe_original: texto en lengua original (opcional)
epigrafe: «traducción del epígrafe» (opcional)
epigrafe_ref: referencia del epígrafe (opcional)
apartado: historia         (filosofia | historia | biblia | exegesis | refutaciones | doctrina | respondiendo-al-islam | santos)
paleta: marino             (esmeralda = islam · pergamino = historia/Biblia/patrística · marino = doctrina/filosofía/exégesis)
fecha: 2026-11-14
tags: [papado, honorio, monotelismo]
resumen: Una o dos frases para buscadores e índices (máx. 220 caracteres).
---
```

## 2. Secciones

- Cada sección empieza con `## Título de la sección {#id-corto}`. La numeración romana y el índice lateral se generan solos.
- Antes de una sección puedes abrir un grupo del índice con una línea `@grupo Nombre del grupo`.
- Subtítulos dentro de sección: `### Subtítulo` y `#### Rótulo menor`.
- No uses `#` ni `##` para otra cosa. No dejes texto antes de la primera sección.

## 3. Texto

- Párrafos separados por línea en blanco. `**negrita**`, `*cursiva*`, `[texto](https://url)`.
- Lenguas originales: `{gr|λόγος}` griego · `{he|דָּבָר}` hebreo · `{ar|كلمة}` árabe · `{sir|ܡܠܬܐ}` siríaco · `{la|Verbum}` latín · `{tr|logos}` transliteración.
- Listas con `- ` o `1. `. Tablas con barras `|` y línea separadora `|---|---|`.
- Cita en bloque: líneas que empiezan con `> `; la última línea `> — Autor, *Obra* loc. (edición, página)` se muestra como referencia.
- Imagen (solo dominio público / licencia abierta, archivo real descargado en la carpeta del dossier): `![texto alternativo](ruta/imagen.jpg "Pie con autor, institución, signatura, licencia y URL")`.

## 4. Bloques especiales

Todos se abren con `:::tipo Título` y se cierran con una línea `:::`. No se anidan.

### Silogismo
```
:::silogismo Silogismo III — Del silencio de las actas
forma: Modus tollens            (opcional: modus ponens, reducción al absurdo, dilema, abductivo, modal S5…)
PM: Premisa mayor.              (usa PM/Pm para dos premisas; P1, P2, P3… para más; PA para auxiliar)
Pm: Premisa menor.
C: Conclusión.
fuerza: Evaluación honesta: demostrativo / probable / abductivo, y de qué premisa depende.
---
#### Justificación de la premisa mayor
…
#### Justificación de la premisa menor
…
#### Por qué se sigue la conclusión
…
#### Objeciones y respuestas
…
:::
```
Todo silogismo **debe** llevar tras `---` la justificación independiente de cada premisa. Sin eso el constructor avisa y no se acepta.

### Objeción y respuesta
```
:::objecion Objeción ortodoxa|Respuesta católica
Q: Formulación fiel y fuerte de la objeción.
R: Respuesta. Puede tener varios párrafos separados por línea en blanco.
:::
```

### Cadena de debate (varios niveles)
```
:::cadena Cadena de debate — título
A: Argumento católico.
O: Objeción rival.
R: Respuesta.
CO: Contraobjeción del adversario más competente.
CR: Contrarréplica.
CO2: …            (opcional)
CR2: …            (opcional)
E: Evaluación final: qué queda en pie.   (opcional)
:::
```

### Evidencia documental / fuente primaria
```
:::evidencia Título breve de la evidencia
id: E-D07-03
tipo: Acta conciliar | Manuscrito | Papiro | Inscripción | Carta | Documento oficial | Edición crítica…
autor: …
documento: …           (u `obra:`)
fecha: …
ubicacion: libro, capítulo, folio, columna o página exacta
edicion: edición crítica o traducción usada, con página
lengua: …
conservacion: institución y signatura (si es un objeto físico)
url: https://…        (enlace verificable; obligatorio)
licencia: Dominio público | CC BY-SA 4.0 | Solo enlace (no se reproduce) …
consulta: 2026-11-14
clase: A               (A primaria · B estudio académico · C documento doctrinal oficial · D apologética · E divulgación)
estado: Verificada     («Verificada» SOLO si abriste la fuente y comprobaste el texto; si no, «Pendiente de verificación»)
original: texto en la lengua original
dir: rtl               (solo para hebreo/árabe/siríaco)
transliteracion: …
traduccion: «…»
imagen: ruta/archivo.jpg     (opcional, solo si es legítimo reproducirla)
pie: pie de la imagen con crédito y licencia
---
**Qué demuestra:** … **Qué no demuestra:** … Contexto y relevancia para el argumento.
:::
```
`:::fuente` es igual, para textos primarios citados por extenso.

### Publicación rival analizada
```
:::rival «Título exacto del artículo»
id: R-D07-01
autor: …
sitio: …
fecha: …
url: https://…
estado: Verificada
cita: «Extracto literal breve (máx. 40 palabras).»
---
**Tesis central.** …
**Reconstrucción lógica.** (1) … (2) … (3) Por tanto, …
**Qué tendría que demostrar para que funcione.** …
**Qué hay de sólido en el argumento.** …
:::
```

### Otros
- `:::hl` … `:::` — recuadro destacado (tesis, definición clave).
- `:::card Rótulo` … `:::` — ficha (definiciones técnicas, cronologías, listas de datos).
- `:::certeza` con líneas `demostrado:`, `probable:`, `defendible:`, `abierto:`, `no-afirmable:` — escala de la conclusión (obligatoria en la conclusión).
- `:::veredicto Conclusión apologética` … `:::` — recuadro final.
- `:::nota` … `:::` — nota bibliográfica al pie de sección.

## 5. Comprobación

`python _proyecto/scripts/build_dossier.py borrador.md --check` devuelve estadísticas (palabras, silogismos, evidencias…) y avisos.
Un borrador con avisos no se acepta salvo los de «Pendiente de verificación» que estén justificados en `fuentes.json`.
