# FASE 1 — Exploración de apologética rival y descubrimiento de temas

Eres uno de los diez investigadores de un proyecto editorial: ampliar una web de apologética **católica**
en español ("Defendiendo la Fe") con 50 dossieres nuevos de investigación de alto nivel. Reportas al
director editorial. En esta fase **no redactas dossieres**: exploras, lees y propones.

Tu número de investigador (Rxx) y tu ÁREA están en la tabla del final. Trabaja solo tu área.

## Objetivo
Descubrir, leyendo directamente lo que publican los adversarios intelectuales del catolicismo / del
cristianismo histórico, **las controversias con más potencial** para un dossier extenso (5.000-12.000
palabras) y original. Interesan sobre todo:
- artículos, series y argumentos **sofisticados**, con fuentes primarias y bibliografía académica, que
  conozcan ya las respuestas cristianas habituales;
- objeciones que los apologistas cristianos **no han respondido bien** o cuya mejor contrarréplica rival
  sigue circulando sin respuesta;
- controversias académicas recientes, fuentes poco usadas, documentos originales;
- NO los tópicos que cualquier apologista conoce, salvo que haya un ángulo realmente nuevo.

## Método obligatorio
1. Usa las herramientas web reales (WebSearch y WebFetch; si no las tienes cargadas, búscalas con ToolSearch
   usando la consulta `select:WebSearch,WebFetch`). No trabajes solo de memoria.
2. Para cada sitio/autor relevante: abre la página, localiza sus mejores publicaciones, **lee los artículos
   completos** (no el resumen del buscador) y extrae tesis, premisas, fuentes que usa.
3. Sigue el hilo de la controversia: respuesta cristiana existente → contrarréplica rival → estado actual.
4. Antes de proponer un tema, compara con la lista de dossieres ya publicados:
   `C:\Users\eperez71\Videos\deus_vult_apologetics\_proyecto\audit\existing_titles.md`. No propongas lo ya cubierto;
   si es adyacente, explica por qué es una cuestión genuinamente distinta.
5. Excluye TikTok por completo.

## Honestidad documental (crítico)
- **No inventes nada**: ni URL, ni títulos de artículos, ni autores, ni citas, ni DOI, ni publicaciones de X.
- Cada URL que registres lleva `"verificado": true` SOLO si la abriste con éxito en esta sesión y contiene lo que
  dices. Si la conoces de memoria o salió en un buscador pero no pudiste abrirla: `"verificado": false`.
- Las citas textuales deben ser breves (menos de 25 palabras), literales y copiadas de la página abierta.
- Si un sitio bloquea el acceso, anótalo en `limitaciones`; no rellenes con suposiciones.
- No atribuyas a un autor conclusiones que no sostiene. Distingue posición oficial de una confesión y opinión
  de un autor individual.

## Límites de escritura
Solo puedes crear/modificar archivos dentro de tu carpeta:
`C:\Users\eperez71\Videos\deus_vult_apologetics\_proyecto\investigadores\Rxx\`
No toques nada más del repositorio. No ejecutes git. No instales nada. No rellenes formularios ni crees cuentas.

## Entregables (dos archivos en tu carpeta)

### 1) `exploracion.json` (JSON válido, UTF-8)
```json
{
  "investigador": "Rxx",
  "area": "...",
  "fecha": "2026-11-14",
  "sitios": [
    {"nombre": "", "url": "", "verificado": true, "autor_o_entidad": "", "orientacion": "", "idioma": "",
     "areas_de_controversia": [""], "calidad_argumentativa": "baja|media|alta", "usa_bibliografia_academica": true,
     "publicaciones_destacadas": [{"titulo": "", "url": "", "verificado": true, "tesis": ""}],
     "lineas_de_refutacion": [""], "potencial_para_dossier": "bajo|medio|alto", "notas": ""}
  ],
  "articulos": [
    {"titulo": "", "autor": "", "sitio": "", "url": "", "verificado": true, "fecha_publicacion": "",
     "tesis_central": "", "tesis_secundarias": [""], "argumentos": [""], "fuentes_que_usa": [""],
     "puntos_fuertes": [""], "puntos_debiles": [""],
     "respuestas_cristianas_existentes": [{"autor": "", "url": "", "verificado": true, "resumen": ""}],
     "contrarreplicas_rivales": [{"autor": "", "url": "", "verificado": true, "resumen": ""}],
     "cita_breve_literal": ""}
  ],
  "candidatos": [
    {"titulo_provisional": "", "interlocutor": "", "apartado_web_sugerido": "filosofia|historia|biblia|exegesis|refutaciones|doctrina|respondiendo-al-islam|santos",
     "tesis_catolica_a_defender": "", "que_sostiene_el_rival": "", "estado_de_la_controversia": "",
     "articulos_rivales_que_lo_motivan": ["url"], "fuentes_primarias_clave": [""], "bibliografia_academica_clave": [""],
     "objeciones_mas_dificiles": [""], "por_que_tiene_interes_apologetico": "",
     "posibles_pruebas_documentales": ["manuscritos, papiros, inscripciones, documentos oficiales… con su ubicación si la conoces"],
     "riesgo_de_duplicacion": "ninguno|bajo|medio|alto — con qué dossier existente y por qué es distinto",
     "puntuacion": {"originalidad": 1, "relevancia": 1, "fuentes_primarias": 1, "bibliografia": 1, "complejidad": 1,
                    "potencial_argumentativo": 1, "pruebas_visuales": 1, "objeciones_relevantes": 1,
                    "interes_contemporaneo": 1, "potencial_extension": 1},
     "extension_estimada_palabras": 0}
  ],
  "limitaciones": [""]
}
```
Puntuaciones de 1 a 5. Entrega **entre 12 y 18 candidatos**, de 8 a 15 sitios y de 10 a 20 artículos leídos.
Prefiere pocos candidatos excelentes y bien documentados a muchos genéricos.

### 2) `exploracion.md`
Informe narrativo (800-1.500 palabras): panorama de tu área, quiénes son los adversarios más competentes, cuáles
son sus 5 mejores argumentos, qué controversias están "vivas", tus 5 candidatos preferidos y por qué, y qué no
pudiste verificar.

## Respuesta final al director
Máximo 25 líneas: rutas de los dos archivos, nº de sitios/artículos/candidatos, lista de títulos de candidatos
(una línea cada uno) y limitaciones encontradas.

---

## Áreas por investigador

| R | Área de exploración |
|---|---|
| R01 | **Islam — crítica textual e historicidad del NT.** Apologética musulmana contra la fiabilidad de la Biblia: variantes, canon, autoría, corrupción (taḥrīf), uso de Ehrman/Metzger/crítica histórica. Sitios tipo Islamic Awareness, Bismika Allahuma, Calling Christians (Ijaz Ahmad), Blogging Theology (Paul Williams), Many Prophets One Message, Answering-Christianity, MuslimProphets, etc. Busca también blogs poco conocidos pero eruditos. |
| R02 | **Islam — cristología, Trinidad y filosofía.** Críticas musulmanas a la divinidad de Jesús, la encarnación, la expiación y la Trinidad (lógicas y exegéticas): Yaqeen Institute, Sapience Institute, Jake Brancatella ("The Muslim Metaphysician"), Abdullah al-Andalusi, Hamza Tzortzis, Shabir Ally, Zakir Hussain, Mohammed Hijab, Bassam Zawadi, respuestas musulmanas a W. L. Craig, David Wood, Sam Shamoun, etc. Incluye el uso musulmán de unitarios (Dale Tuggy, Buzzard). |
| R03 | **Islam — defensa del Corán y de Mahoma.** Preservación coránica (manuscritos de Saná, Birmingham, qirāʾāt, Ibn Masʿūd), iʿjāz e inimitabilidad, "milagros científicos", profecías de Mahoma en la Biblia (Cantar 5:16, Dt 18:18, Dt 33:2, Is 21, Hag 2:7…), ética profética, y el Corán en la Antigüedad tardía según la academia. Incluye **fuentes en español, árabe y francés** si puedes leerlas con fiabilidad. |
| R04 | **Protestantismo reformado y evangélico contra Roma.** James White (aomin.org), Gavin Ortlund (Truth Unites), Triablogue, Beggars All, TurretinFan, William Webster, Ligonier, The Gospel Coalition, Desiring God, GotQuestions, Michael Kruger (canon), Reformation21. Temas: papado, justificación, María, canon, tradición, sacramentos, imágenes, purgatorio, desarrollo doctrinal. Busca sus mejores argumentos históricos (patrísticos). |
| R05 | **Ortodoxia oriental, luteranismo y anglicanismo contra Roma.** Craig Truglia (Orthodox Christian Theology), Ubi Petrus, Erick Ybarra (como interlocutor católico), Jay Dyer, P. Josiah Trenham, Edward Siecienski (filioque, papado), Laurent Cleenewerck; luteranos (Jordan Cooper, Just and Sinner) y anglicanos. Temas: Vaticano I vs primer milenio, filioque, casos de Honorio/Vigilio/Liberio, esencia-energías, pecado original, purgatorio, Inmaculada, infalibilidad, canon 28 de Calcedonia, Sárdica, falsas decretales. |
| R06 | **Mormonismo, Testigos de Jehová y otros restauracionistas/unitarios.** FAIR Latter-day Saints, Interpreter Foundation, Scripture Central, BYU Studies, churchofjesuschrist.org (Gospel Topics Essays); jw.org / wol.jw.org (Traducción del Nuevo Mundo, apéndices, "¿Debería creer usted en la Trinidad?"), Greg Stafford, Rolf Furuli; adventistas; pentecostales unicitarios; unitarios bíblicos (Dale Tuggy, Anthony Buzzard, Sean Finnegan / Restitutio); Iglesia ni Cristo. Usa documentos oficiales para fijar doctrinas. |
| R07 | **Ateísmo, agnosticismo y naturalismo — filosofía.** Graham Oppy, Joe Schmid (Majesty of Reason: inercia existencial, objeciones al teísmo clásico), J. H. Sobel, Paul Draper, J. L. Schellenberg (ocultamiento divino), problema del mal (evidencial, sufrimiento animal), Felipe Leon, Alex Malpass (Kalam), Secular Web (infidels.org), Internet Encyclopedia of Philosophy / SEP, objeciones a las cinco vías, a la simplicidad divina, al alma/hilemorfismo desde la neurociencia, argumento evolutivo contra la moral. |
| R08 | **Crítica histórica del cristianismo y contramisión judía.** Bart Ehrman (blog y libros), Richard Carrier (miticismo), Robert Price, Paulogia, Dale Allison (como voz crítica moderada), objeciones a la resurrección (alucinaciones, leyenda, tumba vacía), a los relatos de la infancia, al censo de Lucas; y contramisioneros judíos: Tovia Singer (Outreach Judaism), Jews for Judaism, Rabbi Yisroel Blumenthal (1000 Verses), Michael Skobac, Uri Yosef — Is 7:14, Sal 22:16, Dn 9, Zac 12:10, genealogías, Mesías ben David, ley eterna. |
| R09 | **X (Twitter) y debates contemporáneos.** Intenta buscar en X (x.com / twitter.com, también vía buscadores con `site:x.com`, Nitter o agregadores accesibles) hilos y debates especializados entre apologistas católicos, protestantes, ortodoxos, musulmanes y académicos (p. ej. cuentas de Trent Horn, Joe Heschmeyer, Jimmy Akin, Erick Ybarra, Gavin Ortlund, James White, Craig Truglia, Ijaz Ahmad, Paul Williams, Jake Brancatella, Dan McClellan, Bart Ehrman, Javad Hashmi, Marijn van Putten, Sean Anthony, Ilkka Lindstedt, hispanohablantes). Si X no es accesible sin sesión, **dilo claramente** y pivota a: canales/debates recientes (2023-2026) reseñados en blogs, Substack, Reddit r/AcademicBiblical, r/AcademicQuran, y rastrea cada afirmación hasta su fuente original. Busca controversias emergentes y enlaces a artículos largos. |
| R10 | **Frontera académica.** Revisa literatura reciente (2015-2026) en revistas y editoriales académicas para detectar líneas con potencial apologético poco explotado en español: Journal of Theological Studies, New Testament Studies, JSNT, JBL, Vigiliae Christianae, Journal of Early Christian Studies, Nova et Vetera, The Thomist, Journal of Qur'anic Studies, Journal of the International Qur'anic Studies Association, Religious Studies, Faith and Philosophy. Ejemplos de orientación (no lista cerrada): cristología temprana alta (Hurtado, Bauckham, Tilling, Fletcher-Louis), memoria y testimonio ocular, datación de papiros (Nongbri), Corán y cristianismo siríaco (Reynolds, Shoemaker, Sinai, Tesei), orígenes del islam, tomismo analítico reciente, Padres sobre primado romano (estudios históricos recientes), estudios sobre el canon. Busca artículos en acceso abierto que puedas leer de verdad. |
