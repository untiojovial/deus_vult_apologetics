# Notas del investigador R08 — D41 (piloto)

Fecha: 2026-11-14. Archivos: `fuentes.json` (45 entradas: 8 primarias verificadas, 9 VERIFICADA en total, 32 PARCIAL, 4 NO_VERIFICADA), `partes/p01.md` a `partes/p06.md`.

## 1. Qué no se pudo verificar

- **Libros leídos solo en reseñas o citas de segunda mano.** Allison (2021 y 2005), Ehrman (2014), Lüdemann (1994; se leyó su página-resumen), Wright (2003), Loke (2020), Licona (2010), Habermas y Licona (2004), Crossan. Las citas de Allison de 2005 (pp. 324-5, 340, 342, 347) vienen transcritas por William Lane Craig, que es apologeta. Antes de usarlas como literales en el dossier final hay que cotejarlas con el libro.
- **Loke (2020).** El PDF de acceso abierto (OAPEN) dio errores de conexión en todos los intentos. Su tratamiento de la alucinación no se ha leído. Es la fuente académica más relevante que falta, porque el expediente la cita como acceso abierto.
- **Rees (1971).** El artículo de PMC devolvió reCAPTCHA. Las cifras (227 viudas y 66 viudos; 80,7 %; 36,1 %) proceden de un resumen de agregador y de un buscador. Conviene cotejarlas con el BMJ.
- **Grimby (1993).** No se pudo leer PubMed (exigía cookies). Las cifras (14 hombres y 36 mujeres; la mitad con sensación de presencia; un tercio con visión u oído) son aproximadas, según el resumen recuperado por buscador.
- **Smith (2019).** Solo resumen. El argumento de la alucinación colectiva es la objeción naturalista más seria del dossier; hay que leer el artículo completo antes de la revisión adversarial.
- **Lake (1907).** No se localizó la hipótesis de la «tumba equivocada» en las páginas leídas (55-61, 134, 145, 202). La atribución a Lake aparece en fuentes secundarias divergentes (una atribuye la explicación a las lágrimas). Hay que leer las páginas 61-79 y el capítulo sobre Juan.
- **Paulogia.** El expediente lo cita como adversario principal. La búsqueda no devolvió ninguna fuente sobre él, así que no aparece en el dossier con argumentos suyos. El director debe indicar qué publicaciones suyas se han de analizar, o retirar el nombre.
- **Crossan y Habermas-Licona.** Solo citados por terceros; figuran en `fuentes.json` como NO_VERIFICADA y no sostienen ninguna premisa.
- **4Q521.** La traducción procede de Wikipedia; la edición de Puech (RQ 15, 1992) no se consultó. El sujeto de la vivificación es el punto decisivo del silogismo VI y de la cadena III, y hay que cotejarlo.
- **Textos griegos.** Los de Mt, Mc, Lc y 1 Co provienen de interlineales de Biblehub, que no indican edición. Deben cotejarse con NA28. La forma de Mc 16,8 y el final de Marcos son textualmente sensibles.
- **Justino, Orígenes e Ignacio.** Se leyeron en traducción inglesa (ANF). No se ha cotejado el griego. Por eso `original` aparece sin transcribir en E-D41-01, E-D41-02 y E-D41-04.
- **Knox.** La traducción Knox de Mt 28 y Lc 24 tiene copyright; no se ha reproducido en el dossier. Las citas proceden de la Vulgata (dominio público) y del griego.

## 2. Discrepancias con el expediente

- **«Rees & Lutkins» (BMJ 1971).** El artículo de 1971 es de autor único (W. Dewi Rees). «Lutkins» corresponde a un artículo de 1967 («Mortality of bereavement»), citado con la grafía «Luteins» en una fuente. Se ha citado solo el de 1971.
- **Título de Allison (2021).** El subtítulo exacto es «Apologetics, Polemics, History» (T&T Clark). El expediente no lo indica.
- **Ehrman, 2015 y 2019.** Los artículos del expediente están tras muro de pago parcial. Solo se leyó la parte pública. La explicación completa de Ehrman sobre visiones y sobre las mujeres no está verificada.
- **Debate Horn–O'Connor (2026).** La página no tiene transcripción. Las frases de O'Connor no se atribuyen a nadie en el dossier.
- **Catalaxia.** El expediente no lo incluye. Se añadió como crítico hispanohablante (autor no identificado, 2023). Puede retirarse.
- **Extensión.** El expediente prevé 10.000-12.000 palabras. El borrador tiene unas 15.000 contando las citas en griego y latín. Conviene recortar en la revisión, sobre todo la sección de herramientas y la de la refutación de Allison, si el director prefiere la extensión prevista.

## 3. Estado de las fuentes y avisos del validador

Ejecuté `build_dossier.py --check` sobre una copia concatenada en el scratchpad (sin escribir en el repositorio). El resultado: 7 silogismos, 3 cadenas, 3 objeciones, 14 evidencias, 6 rivales. Los avisos son de dos tipos:

- «fuente no verificada» para E-D41-09 a E-D41-14 y «rival no verificada» para R-D41-01 a R-D41-06. Corresponden a fuentes con estado PARCIAL en `fuentes.json` (textos griegos de interlineal sin edición y artículos de acceso parcial). Están justificados en ese archivo.
- No hay avisos de estructura.

## 4. Objeciones que no he logrado responder bien

- **Allison, parte (a): cosmovisión.** La concesión es real. El dossier responde que el argumento sigue siendo comparativo, pero una comparación entre premisas distintas no garantiza que la conclusión sea compartida. Este punto sigue abierto.
- **Smith y la alucinación colectiva.** La respuesta del dossier (la literatura clínica no documenta visiones de imágenes compartidas, y los relatos describen contacto y comida) es débil si Smith tiene evidencia clínica que no he leído.
- **4Q521.** Si el texto permite leer al ungido como vivificador de muertos en un sentido que incluya a un ejecutado, la cadena III se debilita mucho. No he podido resolverlo.
- **El salto de la visión a la proclamación.** Ni el dossier ni las fuentes leídas explican con precisión cómo una visión de Pedro se convirtió en proclamación pública en Jerusalén. Es la objeción central de Ehrman (R-D41-01), y no la he visto resuelta en las fuentes leídas.
- **Testimonio femenino.** El argumento del criterio de vergüenza depende de una afirmación sobre el valor legal del testimonio de mujeres en el judaísmo, que no he verificado. Está marcado como tal en la sección L.

## 5. Sugerencias de pruebas visuales

- **Fra Angelico, *Noli me tangere*** (celda 1, convento de San Marco). Ficha de Wikimedia Commons leída: Public Domain Mark 1.0, Museo Nazionale di San Marco. Ilustra Jn 20,17; no es evidencia histórica. Verificar la licencia en la página oficial de Commons antes de usarla.
- **Ivanov, *La aparición de Cristo ante el pueblo*** (Galería Tretiakov, 1837-1857). Aparece en fuentes secundarias. No he localizado una ficha de Commons con licencia verificada; la fotografía de sala puede tener derechos propios. No recomiendo usarla sin verificación.
- **Un manuscrito del final de Marcos** (Códice Sinaítico o Vaticano, 16,8). Sería útil para mostrar visualmente el final corto, pero no he buscado la imagen ni su licencia.
- **4Q521 (fragmento 2).** Las imágenes de los rollos del Museo de Israel suelen tener restricciones; no he comprobado ninguna.

No se ha descargado ninguna imagen.

## 6. Sobre el encargo

- No he ejecutado git, ni instalado nada, ni modificado nada fuera de esta carpeta.
- El validador se ejecutó sobre una copia en el scratchpad para no crear `borrador.md` en la carpeta del dossier. El director puede generar el borrador con `build_dossier.py <carpeta>` cuando lo considere.
- Quedan fuera del dossier, como se pidió: el análisis detallado del credo de 1 Co 15,3-8 (D42) y el argumento de Hume (D40). Solo se mencionan.
