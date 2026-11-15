# R01 — Islam: crítica textual e historicidad del NT (Fase 1, exploración)

Fecha: 2026-11-14. Datos completos en `exploracion.json` de esta misma carpeta.

## Panorama

La apologética musulmana contra la fiabilidad de la Biblia se concentra en un puñado de sitios que reutilizan una misma bibliografía: Metzger, Aland, Ehrman (sobre todo *The Orthodox Corruption of Scripture* y *Misquoting Jesus*) y la antología de fuentes clásicas que recoge WikiIslam. El argumento central es el taḥrīf: la Biblia actual no sería la que Dios reveló, porque el texto se alteró o porque su sentido se tergiversó. Los sitios leídos reparten el argumento en tres pasos: hay muchas variantes, no hay un isnād que garantice la transmisión y los cánones varían.

Los adversarios más competentes son **Islamic Awareness**, que cita fuentes académicas reales y con fecha, y **Islamic Discourse**, que reúne testimonios cristianos árabes del siglo VIII-X sobre la acusación. **Calling Christians** y **Answering-Christianity** son polémicos y con poca bibliografía; **MuslimProphets** cuantifica la cobertura de los papiros con cifras de Wikipedia; **islam.wiki** (Ahmed Deedat) y **Paul Williams** (Hashiya) completan el panorama.

## Los cinco mejores argumentos rivales

1. **Variantes como prueba de corrupción.** La cifra de 400.000 variantes (Ehrman, Wallace) o 150.000-250.000 (Interpreter's Dictionary, citado por IA) se usa como prueba de alteración. Es el argumento más difundido y el más fácil de contestar mal.
2. **Ausencia de isnād.** IA afirma que la Biblia carece de una cadena de transmisión comparable a la del hadiz, y cita a Ibn al-Mubārak: sin isnād, cualquiera podría atribuir cualquier cosa. Christian replies (Katz, citado por IA) no se leyeron.
3. **Discontinuidad con el tiempo de Mahoma.** IA sostiene que la Biblia actual "no es demostrablemente la misma" que la de su época. Es un argumento temporal que se puede comprobar con códices de los siglos IV-VII.
4. **Canon tardío.** IA y Calling Christians señalan que el NT de 27 libros aparece como lista en 367 (Atanasio) y que los cánones varían. Este punto ya está cubierto en `canon-biblia-quran`.
5. **El taḥrīf clásico era interpretativo.** WikiIslam y Saeed (2002, por resumen) sostienen que casi todos los comentaristas clásicos (Ibn ʿAbbās, Ṭabarī, Rāzī, Ibn Kathīr) niegan la alteración textual. Este argumento es un arma contra los polemistas modernos, que lo ignoran.

## Controversias vivas

- **Ehrman frente a Wallace.** Wallace (ed., *Revisiting the Corruption of the New Testament*, 2011) responde a la tesis de la corrupción ortodoxa caso por caso; Fee (1995) criticó que Ehrman convierte posibilidades en probabilidades. El debate es real, pero ya está parcialmente cubierto en el repositorio.
- **El diálogo de Timoteo I con al-Mahdi (c. 781-782).** Hay una discrepancia de fuentes: el texto de Mingana (1928, día 2) no contiene la acusación de alteración, pero ChinaSource (Chagas, 2024) e Islamic Discourse la sitúan en el diálogo. El primer día no está en la versión abierta, así que la cuestión queda sin resolver.
- **El texto original.** IA usa la premisa de un texto original perdido. Epp (HTR 1999) sostiene que "texto original" es multivalente, algo que ningún apologeta cristiano de los leídos discute.
- **Las fuentes clásicas.** Hay desacuerdo sobre si Ibn Ḥazm (s. XI) fue el primer defensor del taḥrīf textual o un caso aislado. Las citas de WikiIslam necesitan verificación en el árabe original.

## Mis cinco candidatos preferidos

1. **Epp y la multivalencia del "texto original"** (`respondiendo-al-islam`). Distinción académica de un autor no cristiano que desarma la premisa del original perdido. Riesgo de duplicación bajo.
2. **Timoteo I y al-Mahdi: ¿dónde nace la acusación de taḥrīf?** (`historia`). Original y con fuentes primarias accesibles, pero depende de leer el primer día del diálogo.
3. **Los clásicos del tafsīr y el taḥrīf** (`respondiendo-al-islam`). Muestra que el taḥrīf textual no es la postura clásica dominante. Riesgo medio-bajo.
4. **Continuidad textual de los siglos IV-VII** (`biblia`). Verificable con códices y papiros; riesgo medio con `patristica-nt` y `canon-biblia-quran`.
5. **La "corrupción ortodoxa" de Ehrman y la respuesta de Wallace** (`biblia`). La tesis más fuerte de la acusación con su mejor autor. Riesgo alto: conviene fusionarla con R08 o reducirla a casos no tratados.

Otros candidatos documentados: isnād frente a transmisión bíblica (riesgo medio con `tawatur-psicologia-cognitiva-dossier`); anécdota de Dalrymple y los once versículos; 1 Tim 3:16 (riesgo bajo); fragmentariedad de los papiros (riesgo medio-alto con R10); y apologética cristiana árabe del taḥrīf (siglos VIII-X), hermana de la candidata de Timoteo I.

## Qué no pude verificar

- **Sitios no accesibles:** www.islamicawareness.org (redirige a dominio aparcado), bismikaallahuma.org (error SSL y HTTP 500) y manyprophetsonemessage.com (HTTP 500). Figuran con `verificado: false`.
- **Lectura por resumen:** las páginas se leyeron mediante WebFetch, que devuelve un resumen y no el texto íntegro. Por eso no hay citas literales en el JSON.
- **Fuentes solo de segunda mano:** Ehrman (1993), Saeed (2002), Schaffner (2016), Whittingham (2011), Hill & Kruger (2012), Nongbri (2018), Samir & Nasry (2018) y Frary (2003) no se abrieron. El PDF de Reynolds era binario, y el ensayo de Paul Williams solo se leyó en su título y notas.
- **Cumplimiento de mínimos:** 10 candidatos (la consigna pide 12-18) y 7 sitios rivales leídos (la consigna pide 8-15). La diferencia se explica porque gran parte del área ya está cubierta por dossieres publicados y porque tres sitios no fueron accesibles.
- **Respuestas cristianas:** todas las leídas son en inglés (Nix, Andrews, Stava, Thompson, Wallace, Fantin).
- **Uso islámico de 1 Tim 3:16:** no encontrado en los sitios leídos.
