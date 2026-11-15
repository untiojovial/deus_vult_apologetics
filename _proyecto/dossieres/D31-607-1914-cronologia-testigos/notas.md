# Notas del investigador R06 — D31 (piloto)

Fecha: 2026-11-14. Carpeta: `dossieres\D31-607-1914-cronologia-testigos\`.
Entregables: `fuentes.json` (40 registros), `partes\p01.md` a `partes\p06.md`, este archivo.

## 1. Estado de verificación (resumen honesto)

- **Fuentes primarias con texto leído en esta sesión (estado VERIFICADA):** solo 2 Reyes 25:8 (traducción ESV en Biblehub). Es el único dato del dossier que he leído directamente en su fuente.
- **Primarias leídas solo por resumen o extracto de herramienta (PARCIAL):** ambos artículos de La Atalaya (2011), Reasoning From the Scriptures («Dates»), mensajes de Furuli (2006 y 2008), textos bíblicos de Jer 25/29, Jer 32:1, Jer 52:12, 2 Cr 36:20-21, la Crónica ABC 5 (vía Livius y COJS), el Canon (vía Wikipedia), la Crónica de Nabonido (fragmento de búsqueda), la estela de Adad-guppi (vía sitio crítico).
- **Primarias no leídas (NO_VERIFICADA):** VAT 4956 (ninguna edición ni imagen), BM 21946 (el registro del British Museum no se pudo abrir), BM 35382, la estela de Harán, Ezequiel 1:2, 33:21, 40:1; Zacarías 1:12, 7:5; Esdras 6:15; Daniel 4 y 9:2; textos hebreos en general.
- **Académicas:** ninguna leída directamente. Wiseman (1956), Grayson (1975), Sachs-Hunger (1988), Parker-Dubberstein (1956), Galil (1996), Lipschits (2005), Beaulieu (1989), Hunger (AfO 52, 2011), Furuli vols. 1-2 (2003, 2007/2008) y Neugebauer-Weidner (1915) constan solo como citas en fuentes secundarias o catálogos.
- **Requisito de ≥ 8 primarias verificadas: NO cumplido.** Solo hay una primaria VERIFICADA. Lo declaro así para que el revisor documental no lo dé por cumplido.
- **Requisito de ≥ 6 académicos: formalmente cumplido** (8 entradas clase B), pero ninguna está verificada.
- **Requisito de ≥ 25 fuentes: cumplido** (40 registros: 1 VERIFICADA, 25 PARCIAL y 14 NO_VERIFICADA, según el recuento de `fuentes.json`).

## 2. Extensión

El expediente pide 9.000–11.000 palabras y el prompt general 6.000–10.000. El conjunto de `partes\` tiene unas 17.000 tokens según `wc` (incluye el marcado, las tablas y los separadores), lo que equivale a unas 13.000–14.000 palabras de texto real. Esa cifra supera la del expediente, pero no la he medido con un contador de palabras del contenido: el director debe confirmarla con `build_dossier.py --check` antes de decidir si hay que recortar. Lo que sí considero sobredimensionado es el apartado de análisis filológico y las cadenas, que el revisor puede querer reducir.

## 3. Discrepancias encontradas en las fuentes

1. **Galil.** La fecha que recogió la búsqueda (2007) es incorrecta: la obra es de 1996 (Brill, vol. 9 de la serie de historia del Antiguo Oriente Próximo). Corregido en el registro y en la bibliografía, pero no he leído la obra.
2. **Adad-guppi y la estela de Harán.** Wikipedia («Harran Stela») y el sitio crítico describen objetos que pueden ser el mismo o distintos. Wikipedia no menciona a Adad-guppi, y su datación de composición (542–540) no coincide con la muerte de Adad-guppi en el año 9 de Nabonido (547/546). No lo he resuelto.
3. **Edad de Adad-guppi.** El sitio crítico dice 95 años hasta el fin del año 4 de Neriglisar y 104 hasta el año 9 de Nabonido. La búsqueda general dice 104 sin más detalle. El expediente no menciona la cifra de 95. No la he confirmado.
4. **Fin de la Crónica ABC 5.** Livius dice que el tramo conservado llega al año 11 de Nabucodonosor (594/593). COJS dice que la serie conservada llega a mediados del siglo III a.C., sin los años 594–557. Son afirmaciones incompatibles sobre el mismo objeto. Lo dejo señalado en la evidencia E-D31-04.
5. **Número de tablillas anómalas de Furuli.** En 2006 habla de unas cincuenta; en 2008, de unas noventa dentro de unas veinte mil datadas. El cambio es relevante y lo recojo en el silogismo VII.
6. **Furuli, Hunger y AfO.** La reproducción de la reseña de Hunger en un foro no contiene el texto de Hunger. No uso ningún juicio atribuido a Hunger.
7. **Lista de reyes de Uruk.** La cita de la Watch Tower (siete reyes entre Kandalanu y Nabonido, frente a cuatro del Canon) procede de un resumen. No he visto la lista.

## 4. Errores de partida del expediente que conviene corregir

- **El artículo de Reachout Trust (Piper, 2012) no es una publicación rival en el sentido de la plantilla.** Es una crítica de divulgación a la Watch Tower. En el dossier aparece como fuente de contraste (F-D31-11), no como bloque `:::rival`. El director debe decidir si lo sustituye por otra publicación.
- **El segundo «artículo rival» del expediente es el enlace a Should You Believe in the Trinity?** Es solo una referencia de estilo y no tiene contenido sobre cronología. No lo he usado.
- **La lista de fuentes preliminares del director incluye «Estela de Adad-guppi (Harrán)»**, con la descripción de estela de Harán. Ver punto 3.2.
- **El expediente dice «BM 21946 (Crónica de Nabucodonosor)».** Es correcto como identificación (ABC 5), pero el nombre habitual en la bibliografía es «Crónica de Nabucodonosor» o «Crónica de Jerusalén»; conviene unificar la denominación en el texto final. He usado «ABC 5 (BM 21946)».
- **El título del expediente** dice «607 a.C. y 1914: | La Cronología de los Testigos de Jehová ante las Fuentes Babilónicas». He usado «La cronología de los Testigos de Jehová ante las fuentes babilónicas» con minúscula en la segunda parte, por criterio de estilo. El director puede volver a la versión original.

## 5. Objeciones que no he logrado responder bien

- **El año 19 de 2 Reyes 25:8 frente al año 18 de Jeremías 32:1.** Mi respuesta (distinción de cómputo) es la explicación mayoritaria según fuentes secundarias, pero no he leído la literatura asiriológica que la documenta. Es el punto más débil de la refutación por lo que respecta al detalle de la fecha (586 frente a 587).
- **La Lista de Uruk y las omisiones del Canon.** Sostengo que las omisiones están antes de Nabopolasar, pero no he visto la lista. Si contiene reyes en el tramo 605–586, el argumento de la línea 2 debe revisarse.
- **Lectura de VAT 4956.** No he visto la edición de Sachs y Hunger ni una imagen de la tablilla. Mi valoración de la intercalación y de la lectura de Nisanu 9 frente a 8 procede de un sitio crítico de autor no identificado y de la Watch Tower. Es un punto en el que el dossier no debe presentarse como concluyente.
- **Zacarías 1:12 y 7:5 como argumento de los setenta años.** La respuesta de la Watch Tower («ayunos conmemorativos») es posible, y solo he presentado el argumento como «en construcción». No he comprobado el hebreo.
- **La dependencia doctrinal de 1914 respecto de 607.** He afirmado que el cálculo de 2.520 años depende de 607, lo que es aritméticamente seguro. Pero la afirmación del expediente de que «cae el fundamento de la autoridad del Cuerpo Gobernante» no la he verificado en fuente oficial, y no la he incluido como afirmación en el dossier (aparece como «no-afirmable» en la conclusión).
- **Jonsson como fuente.** Su juicio de que Furuli tiene una «agenda oculta» es ad hominem, y lo he excluido del argumento. Sus argumentos sobre la cronología sí se han usado, con la salvedad de que son de un crítico declarado.

## 6. Dudas de método

- He atribuido a la Watch Tower dos posiciones que deduje de su aritmética y no de un texto suyo: que el año 37 de VAT 4956 = 588 implica año 18 = 607 (esto lo dice el propio artículo) y que la crónica debería desplazarse veinte años para encajar con 607 (esto es una deducción mía). La deducción está marcada como tal en el texto de la argumentación principal (línea 1).
- Las contraobjeciones CO de las cadenas son reconstrucciones mías de lo que la posición contraria podría responder. Está indicado en el dossier.
- Las citas del texto bíblico en inglés están tomadas de Biblehub (ESV para 2 Reyes; BSB para el resto); donde no pude verificar la traducción exacta lo indico.

## 7. Sugerencias de pruebas visuales (no descargadas)

No he descargado nada. Son sugerencias para que el director decida:

- **BM 21946 (ABC 5).** Buscar en la colección en línea del British Museum y en Wikimedia Commons una fotografía con licencia abierta o de dominio público. Anotar número de museo, descripción y licencia exacta. El enlace de colección que probé (W_1896-0401-1) no se pudo abrir: no debe usarse sin confirmar.
- **VAT 4956.** Buscar en CDLI o en la Staatliche Museen zu Berlin (Vorderasiatisches Museum) una imagen o una ficha con licencia. La búsqueda general no devolvió ninguna entrada CDLI para VAT 4956.
- **Estela de Harán / Adad-guppi.** Buscar fotografía en Wikimedia Commons; verificar la institución donde se conserva (las fuentes no coinciden).
- **Tablilla de Nabonido (BM 35382).** Buscar en la colección del British Museum; el catálogo de Oxford que cité no tiene imagen propia.

## 8. Lo que queda por hacer antes de integrar el dossier

1. Verificar en edición primaria las tablillas (ABC 5, VAT 4956, BM 35382) o marcarlas como «Pendiente de verificación» en el texto final, que es lo que hacen ahora las fichas.
2. Cotejar las citas hebreas y las transliteraciones con BHS o Sefaria.
3. Confirmar la cifra de la estela de Adad-guppi y la traducción de Gadd (1958).
4. Leer la segunda parte de La Atalaya (2011) completa para comprobar el tratamiento del año 19 de 2 Reyes 25:8.
5. Confirmar la lectura de la Lista de Uruk y la literatura sobre las omisiones del Canon.
6. Verificar la formulación oficial actual de la dependencia doctrinal de 1914.
7. Sustituir o justificar el uso de Reachout (F-D31-11) como fuente de contraste.
8. Pasar `build_dossier.py --check` sobre la concatenación de `partes\` cuando el director lo ejecute.
