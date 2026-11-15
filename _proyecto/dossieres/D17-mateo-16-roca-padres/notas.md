# Notas del investigador — D17 (piloto)

Investigador R04. Entregables: `fuentes.json` (34 fuentes), `partes/p01.md` a `partes/p05.md`. Estados: 5 VERIFICADAS, 11 PARCIALES (en el borrador figuran como «Pendiente de verificación»), 18 NO_VERIFICADAS.

## 1. Lo que no he podido verificar

**Textos primarios no leídos en fuente abierta**
- Agustín, *Retractationes* I.21: solo latín de una fuente secundaria (blog que cita PL 32,618). augustinus.it devolvió HTTP 999 (bloqueo). Antes de publicar, leer PL 32 o CSEL 36.
- Agustín, *Tract. Ioh.* 124.5; *Sermo* 229P; Ambrosio, *De fide* IV.5.53 y *Exp. Luc.* VI.98; Afraates, *Dem.* I: solo vía la encuesta de Webster.
- Cipriano, *De unit.* 4: latín de PL 4 vía earlychurchtexts; la variante «super unum» no resuelta (edición crítica de Hartel).
- Tertuliano, *De pud.* 21: solo traducción inglesa en resumen (bkv); el latín no se vio.
- Crisóstomo, Orígenes y León se leyeron en traducción inglesa (NPNF / ANF). Los originales griego y latino no se consultaron.

**Textos bíblicos**
- Interlineales de Biblehub: base textual no identificada. Contrastar Mt 16:18, Jn 1:42, Lc 22:32 y Ef 2:20 con NA28 o SBLGNT.
- Is 22:22 leído en tabla hebrea. No leídos: Is 22:15-21 (sustitución de Sebna por Eliaquim), Is 22:25 (la clavija que cede) y la Septuaginta.
- No leídos en esta sesión: Mt 16:19 (griego), Mt 18:18, Mt 28:20, Jn 21:15-17, 1 Cor 3:11 (citado vía Nichol), 1 Pe 2:4-10, y la Peshita (dato circulante, no comprobado).

**Launoy**
- No he localizado la obra de Launoy. Las cifras (17/44/16/8 y corregidas 16/17/4/6) vienen de la crítica anónima de 1955 (leída en texto). Antes de usarlas, localizar a Launoy o una exposición fiable del recuento.

**Académicos y comentarios citados solo por terceros**
- Carson (EBC 8, p. 368): cita atribuida solo en sitios católicos. No usar la frase sin comprobarla.
- Cullmann (TDNT 6): la frase «Protestant attempts to evade it...» atribuida en sitios católicos no está comprobada. No citarla.
- Davies-Allison (ICC II): Festa da años distintos (2004 y 2014); el ICC II es de 1991. Confirmar año y página.
- Caragounis (1990), Hagner (1995), Osborne (2010), Nolland (2005), Lenski, Quarles (2017, título no verificado), Jobes (año 2011 según Festa; confirmar).
- Osborne: el dato «la mayoría hoy reconoce a Pedro» solo llega por Festa. Es el dato más usado del dossier para la mayoría; comprobar en el original antes de publicar.
- Festa (2023): leído en texto (pdftotext). Los caracteres griegos no se extrajeron del PDF.

**Rivales**
- MacKenzie (equip.org): bloqueado por Cloudflare para lectura directa. No he forzado el acceso. Lectura solo por resumen (WebFetch). Hay que leer el texto completo para la revisión adversarial.
- Allison (Crossway): solo resumen.
- El título de la reseña de MacKenzie coincide con el de la obra revisada, «Jesus, Peter and the Keys». Atribuir la obra revisada (JPK) a su autor exacto solo después de verificarlo. No lo he hecho.
- Ortlund: no he encontrado escrito suyo sobre Mt 16:18; solo un episodio de podcast (Truth Unites, dic. 2024) que no pude leer. Su argumento no está representado con fiabilidad. Pendiente antes de la revisión adversarial.

**Fechas**
- Las fechas marcadas como «dato general» en la tabla (Tertuliano, Orígenes, Cipriano, Crisóstomo, Agustín, Ambrosio) no se han comprobado en fuente abierta.

## 2. Diferencias con el expediente

- La tesis del expediente afirma que «los mismos Padres que predican la confesión afirman el oficio petrino». Solo se cumple en Crisóstomo y León. Agustín (Retr. I.21) no toma partido; Orígenes condiciona las llaves a la vida moral y no menciona a Roma. El dossier reformula la tesis en `p01.md` y lo explica en el resumen. El director debe decidir si acepta la reformulación.
- El expediente llama «rival» al artículo de MacKenzie, que es una reseña, y ambos rivales son de 1998 y 2015. Festa (2023), no listado en el expediente, es el estudio académico más completo y se trata como rival académico.
- El expediente pide ≥8 fuentes primarias verificadas y ≥6 estudios académicos. Hay 3 primarias patrísticas verificadas (Orígenes, Crisóstomo, León) más textos bíblicos parciales, y 2 estudios académicos verificados (Festa y la crítica de 1955). No se cumple el mínimo orientativo; el déficit es real y no se ha disimulado.
- Extensión: el borrador tiene unas 12.900 palabras según `build_dossier.py --check` (incluye marcado, tablas y bloques). El expediente prevé 9.000-11.000; el contenido real está en ese rango, y no se ha inflado.

## 3. Objeciones que no he logrado responder bien

1. **Is 22:25 (la clavija cede).** Si la transmisión de llaves por el paralelo de Isaías se usa como argumento, la objeción de que el oficio puede fallar es fuerte. Mi respuesta (la indefectibilidad se apoya en Mt 16:18b, no en Is 22) es una premisa, no una demostración, y no he leído Is 22 completo.
2. **Tertuliano (De pud. 21).** Liga las llaves a Pedro personalmente. Mi respuesta (es polémica montanista) explica el contexto, pero no responde a la lectura en sí. Necesita el latín.
3. **Función fundacional única (Nolland, citado en Festa).** La distinción entre función fundacional y función de sostén es una premisa mía, sin apoyo verificado en el texto de Nolland.
4. **Objeción de Quarles (Mt 16:23).** Si Pedro podía errar tras Mt 16:18, el fundamento no es indefectible en su persona. El dossier distingue indefectibilidad y impecabilidad sin desarrollarlo; es un punto que el lector protestante va a presionar.
5. **Caragounis.** La crítica al argumento aramaico tiene un libro entero que no he leído. Si su argumento es más fuerte que lo que resume Festa, el silogismo II debe reescribirse.
6. **Ortlund.** Sin su argumento escrito, no puedo responder a su versión.

## 4. Pruebas visuales (no descargadas)

- Candidato: Pietro Perugino, *Consegna delle chiavi* (1481-1482), Capilla Sixtina. Archivo indicado en la búsqueda: «Christ Handing the Keys to St. Peter by Pietro Perugino.jpg» en Wikimedia Commons (URL canónica supuesta: https://commons.wikimedia.org/wiki/File:Christ_Handing_the_Keys_to_St._Peter_by_Pietro_Perugino.jpg, no abierta). Los espejos la describen como dominio público; la licencia no se ha comprobado en la página de Commons. Verificar antes de usar.
- Sobre Mt 16:18 no he buscado otras imágenes (manuscritos con la lectura, inscripciones de Roma, códices de Orígenes). No hay imagen en el borrador.

## 5. Pendiente antes de la revisión documental (R05)

1. Abrir Retr. I.21 en PL 32 o CSEL 36 y comprobar el latín.
2. Confirmar NA28 en Mt 16:18-19, Jn 1:42, Lc 22:32, Ef 2:20 y Is 22:15-25.
3. Localizar a Launoy o una exposición fiable de su recuento; confirmar el mapeo de la crítica de 1955.
4. Comprobar Osborne (p. 627-628) y Nolland (p. 670) en original: son la base del dato de mayoría.
5. Comprobar la cita de Carson (EBC 8, p. 368) y eliminar la cita de Cullmann si no se encuentra.
6. Confirmar la edición y el año de Davies-Allison, Jobes y Lenski.
7. Leer MacKenzie y Allison completos (con permiso o por otra vía legítima).

## 6. Sugerencias de búsqueda adicional (no hechas)

- Biblioteca Digital de Orígenes (GCS, Klostermann) para el griego de Comm. Matt. XII.10-14.
- Edición crítica de Cipriano (Hartel) para «super illum unum» frente a «super unum».
- Texto completo de la encuesta de Webster (252.883 caracteres; leí unos 100.000).
