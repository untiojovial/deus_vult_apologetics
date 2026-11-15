# Estándar editorial y control de calidad

## 1. Qué es un dossier aceptable

Un expediente argumentativo y documental que permite preparar un debate real sin buscar fuera lo esencial.
No es una entrada de blog, ni una lista de versículos, ni un resumen de Wikipedia.

### Estructura intelectual (adáptese; no es una plantilla mecánica)
A. Resumen ejecutivo · B. Formulación precisa del problema (y del artículo rival, si lo hay) · C. Definiciones técnicas ·
D. Contexto histórico y doctrinal (cronología) · E. Fuentes primarias (ficha completa) · F. Análisis filológico ·
G. Evidencia documental · H. Estado de la cuestión académica (consenso / mayoría / minoría / abierto / confesional / refutado) ·
I. Argumentación principal · J. 5-10 silogismos **desarrollados** · K. Mejor formulación de la posición contraria ·
L. Refutación · M. Cadenas de contraobjeciones (≥ 2 niveles en lo difícil) · N. Tablas comparativas ·
O. Conclusión graduada (`:::certeza`) · P. Herramientas para el debate · Q. Bibliografía clasificada.

### Extensión
5.000-8.000 palabras (avanzado); 8.000-15.000 (complejo). Nunca relleno: si el tema da para 5.500, son 5.500.

## 2. Reglas de honestidad (causa de rechazo inmediato)

1. **Nada inventado**: citas, páginas, DOI, manuscritos, traducciones publicadas, consensos, artículos, tuits, objeciones atribuidas a personas reales.
2. Toda cita literal procede de una fuente **abierta y leída** por el investigador, o se marca `Pendiente de verificación` y no sostiene ningún argumento.
3. «Consenso académico» solo si se ha verificado; si no: «posición mayoritaria según X e Y».
4. No se atribuye a un autor lo que no sostiene. Un autor individual no es «el islam» ni «los protestantes».
5. Las objeciones hipotéticas se rotulan como hipotéticas.
6. No se oculta una dificultad real: se reconoce y se da la mejor respuesta disponible; si no la hay, se dice.
7. Citas de artículos rivales: breves (≤ 40 palabras), literales, con enlace. Nunca reproducir artículos enteros.
8. Imágenes: solo dominio público o licencia abierta, descargadas de la institución titular, con crédito. Ninguna imagen generada que simule un documento.
9. Se critican ideas y argumentos, no personas ni comunidades.
10. Frente al islam: núcleo niceno, sin disputas intracristianas. Frente a protestantes/ortodoxos: posición específicamente católica.
11. No se presupone la verdad del catolicismo para probar una tesis católica a quien no la comparte. Distinguir argumento interno / externo / comparativo.
12. Distinguir validez de solidez; probabilidad de demostración. Nada de falsos dilemas: examinar las salidas.

## 3. Clases de fuente (`fuentes.json` de cada dossier → `SOURCE_REGISTRY.json`)

A primaria · B estudio académico · C documento doctrinal oficial · D obra/artículo apologético · E divulgación · F pista no verificada (nunca como prueba).
Campos: id, dossier, afirmación respaldada, autor, título, fecha, página/sección, URL, DOI, cita verificada, idioma, licencia, fecha de consulta, estado, limitaciones.

## 4. Flujo y revisiones

1. **Investigación** (responsable): `fuentes.json` + `notas.md` → estado FUENTES_VERIFICADAS.
2. **Borrador** (responsable): `borrador.md` conforme a `plantilla/FORMATO_BORRADOR.md` → BORRADOR.
3. **Revisión documental** (otro investigador): reabre las fuentes críticas y comprueba citas, fechas, páginas, traducciones, contexto, licencias y fidelidad al artículo rival → `revision_documental.md` con lista de hallazgos (gravedad alta/media/baja).
4. **Revisión adversarial** (un tercero): adopta la posición del adversario más competente (consultando sus publicaciones reales) e intenta desmontar el dossier: premisas débiles, falacias, objeciones omitidas, respuestas superficiales, conclusiones excesivas → `revision_adversarial.md`.
5. **Correcciones** (responsable): `correcciones.md` respondiendo punto por punto; borrador actualizado.
6. **Revisión final del director**: lectura completa, comprobación por muestreo de citas, decisión → APROBACION_EDITORIAL o vuelta a investigación.
7. **Integración** (director): HTML en `static/refutaciones/`, envoltorio en `content/<apartado>/`, índices → INTEGRADO; verificación técnica y `manifest.py verify` → VERIFICADO.

## 5. Lista de aceptación (todas obligatorias)

- [ ] Tema nuevo, sin duplicar dossier existente ni otro de los 50 (comprobado contra `EXISTING_TOPIC_MAP.json`).
- [ ] Tesis diferenciada y enunciada en el resumen.
- [ ] Extensión y profundidad suficientes; sin relleno.
- [ ] Fuentes primarias pertinentes con ficha completa; bibliografía especializada real.
- [ ] Todas las citas críticas verificadas (o marcadas y sin peso probatorio).
- [ ] ≥ 5 silogismos con justificación de premisas, objeciones y evaluación de fuerza (salvo tema que no lo admita, justificado).
- [ ] Mejor versión de la posición contraria; artículos rivales representados fielmente y enlazados.
- [ ] Cadenas de contraobjeción en los puntos difíciles.
- [ ] Conclusión graduada (demostrado / probable / defendible / abierto / no afirmable).
- [ ] Herramientas de debate y bibliografía clasificada.
- [ ] Revisión documental y adversarial superadas; correcciones aplicadas.
- [ ] `build_dossier.py --check` sin avisos injustificados.
- [ ] Derechos de autor respetados.
- [ ] Integrado con el diseño existente; rutas e índices correctos; `manifest.py verify` OK.
