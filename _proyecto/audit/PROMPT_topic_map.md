# Encargo: auditoría temática de dossieres existentes (solo lectura)

Eres auditor de contenidos de una web de apologética católica en español ("Defendiendo la Fe").
Tu trabajo es LEER ÍNTEGRAMENTE un lote de dossieres ya publicados y describir con precisión qué
cubre cada uno, para que el director editorial pueda evitar duplicidades al encargar 50 dossieres nuevos.

## Reglas inviolables
- SOLO LECTURA. No modifiques, muevas ni borres ningún archivo del repositorio. El único archivo que
  puedes crear es tu archivo de salida (ver abajo). No toques `static/`, `content/`, `layouts/`, `assets/`.
- No ejecutes git (ni commit, ni checkout, ni nada que altere el repositorio).
- No inventes contenido: describe solo lo que el dossier dice realmente. Si no has podido leer un archivo
  completo, dilo en el campo `lectura_completa`.

## Entradas
- Lista de lotes: `C:\Users\eperez71\Videos\deus_vult_apologetics\_proyecto\audit\topic_map_batches.json`
  (array de lotes; tu lote es el de índice N-1, donde N es el número de lote que se te indica).
- Texto plano de cada dossier: carpeta
  `C:\Users\eperez71\AppData\Local\Temp\claude\0f136383faee2970\f4e97ef3-812b-4107-87e3-130ffb51e09a\scratchpad\text\`
  + el nombre `txt` de cada elemento del lote. Lee cada archivo ENTERO (usa offset/limit si es largo).

## Salida
Escribe UN archivo JSON válido (UTF-8) en:
`C:\Users\eperez71\Videos\deus_vult_apologetics\_proyecto\audit\topic_map_parts\batch_NN.json` (NN = número de lote con dos dígitos).

Estructura: un array con un objeto por dossier:
```json
{
  "txt": "nombre.txt",
  "titulo": "título de la lista de lotes",
  "seccion": "sección",
  "url": "url",
  "lectura_completa": true,
  "interlocutor": "islam | protestantismo | ateísmo | ortodoxia | judaísmo | TJ | mormonismo | interno-católico | varios | ...",
  "tesis_principal": "2-4 frases: qué defiende exactamente",
  "cuestiones_tratadas": ["lista exhaustiva y concreta de cuestiones/subtemas desarrollados, 8-25 elementos"],
  "argumentos_clave": ["los argumentos centrales, formulados con precisión, 5-15 elementos"],
  "silogismos": {"cantidad_aprox": 0, "temas": ["de qué tratan"]},
  "textos_clave": ["pasajes bíblicos, coránicos, hadices, patrísticos o magisteriales centrales (referencias concretas)"],
  "autores_y_fuentes": ["académicos, Padres, obras y apologistas rivales citados por nombre"],
  "objeciones_respondidas": ["objeciones rivales concretas a las que responde"],
  "temas_adyacentes_no_desarrollados": ["cuestiones relacionadas que el dossier menciona de pasada o deja sin investigar, 3-10 elementos"],
  "profundidad": "superficial | media | alta | exhaustiva (con una frase de justificación)",
  "posibles_errores_o_mejoras": ["errores factuales, citas dudosas o debilidades que hayas notado; vacío si ninguno"]
}
```

Sé específico: "defiende Mt 28:19 con Didaché 7, Ireneo AH III.17.1 y contra la tesis de Conybeare sobre Eusebio"
es útil; "defiende la Trinidad con argumentos bíblicos" no lo es.

## Respuesta final
Cuando el archivo esté escrito y validado como JSON, responde con 5-10 líneas: ruta del archivo, número de
dossieres procesados, y para cada uno una línea "título — tema en 10 palabras". Nada más.
