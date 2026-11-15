#!/usr/bin/env python3
"""FASE 2 — Seleccion editorial de los 50 dossieres (decision del director, 2026-11-14).

Genera: DOSSIER_REGISTRY.json, RESEARCH_TASKS.json, SELECCION_TEMATICA.md, actualiza TOPIC_CANDIDATES.json
(candidatos del director + decision sobre cada candidato) y crea dossieres/Dxx-slug/expediente.json.
Reejecutable: no pisa el campo 'estado' de un dossier que ya haya avanzado.

Las 'fuentes_preliminares' son PISTAS del director (clase F hasta que el investigador las abra y verifique).
"""
import json, os

PROY = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

PERFILES = {
    "R01": "Crítica textual, manuscritos y transmisión de la Biblia",
    "R02": "Teología filosófica cristiano-musulmana (Trinidad, cristología, kalām)",
    "R03": "Estudios coránicos: manuscritos, lecturas, tafsīr y hadiz",
    "R04": "Controversia católico-protestante: exégesis, sacramentos, patrística latina",
    "R05": "Eclesiología histórica: primado romano, concilios y Oriente cristiano",
    "R06": "Movimientos restauracionistas y unitarios (SUD, Testigos de Jehová, unitarismo bíblico)",
    "R07": "Filosofía de la religión y metafísica tomista",
    "R08": "Biblia hebrea, judaísmo y orígenes cristianos (resurrección, mesianismo)",
    "R09": "Historia de la Iglesia, historiografía y controversias contemporáneas",
    "R10": "Patrística, Antigüedad tardía y frontera académica",
}

ISL, PRO, ORT, RES, FIL, HIS = "Islam", "Protestantismo", "Ortodoxia oriental", "Restauracionismo y unitarismo", "Ateísmo y naturalismo", "Crítica histórica y judaísmo"

# (id, slug, titulo, apartado, paleta, area, adversario, tesis, preguntas, originalidad, fuentes, candidatos, resp, rev_doc, rev_adv, extension, piloto)
D = [
 ("D01", "palimpsesto-sana-cierre-coran", "El Palimpsesto de Saná y el Cierre del Texto Coránico: | Lo que el Manuscrito Demuestra y lo que No",
  "respondiendo-al-islam", "esmeralda", ISL, "Apologética musulmana de la preservación perfecta (Islamic Awareness, Yaqeen) y, en el otro extremo, el revisionismo radical",
  "El texto inferior de Ṣanʿāʾ 1 documenta materialmente una tradición textual coránica distinta de la ʿuthmānica; ello refuta la tesis popular de la preservación «letra por letra» sin autorizar la tesis contraria de un Corán inventado tardíamente. La comparación honesta con la transmisión del NT deja de favorecer al Corán.",
  ["¿Qué variantes contiene exactamente el texto inferior y de qué tipo son?", "¿Es un códice de Compañero (Sadeghi-Goudarzi) o un ejercicio escolar (Hilali)?", "¿Cuándo se cerró el rasm: c. 650 (Sinai, van Putten) o bajo ʿAbd al-Malik (Shoemaker)?", "¿Qué puede y qué no puede concluir un apologista cristiano?"],
  "«Canon Biblia vs Quran» menciona Saná de pasada dentro de una comparación de cánones; aquí el manuscrito y el debate académico sobre el cierre del rasm son el objeto único.",
  ["Sadeghi & Goudarzi, «Ṣanʿāʾ 1 and the Origins of the Qurʾān», Der Islam 87 (2012)", "Sadeghi & Bergmann, Arabica 57 (2010)", "Hilali, The Sanaa Palimpsest (OUP 2017)", "Sinai, «When did the consonantal skeleton of the Quran reach closure?», BSOAS 77 (2014)", "Shoemaker, Creating the Qur'an (UC Press 2022, acceso abierto)", "van Putten, «The Grace of God…», BSOAS 82 (2019)", "Bujārī 4987"],
  ["C-R03-01", "C-R03-09", "C-R03-04", "C-R10-03"], "R03", "R01", "R02", "9.000-11.000", True),
 ("D02", "qiraat-ahruf-variantes", "Qirāʾāt y Aḥruf: | ¿Lecturas Reveladas o Variantes Textuales?",
  "respondiendo-al-islam", "esmeralda", ISL, "Islamic Awareness («Qirāʾāt»), Yaqeen Institute (Khatib y Khan)",
  "Las diez lecturas canónicas son el resultado de un proceso histórico de selección (Ibn Mujāhid, s. X) sobre un rasm ambiguo; la doctrina de los siete aḥruf no explica las lecturas existentes y la tesis «un solo Corán sin variantes» es insostenible en sus propios términos.",
  ["¿Qué son los siete aḥruf según los hadices y qué relación tienen con las qirāʾāt?", "¿Qué diferencias de sentido hay entre Ḥafṣ y Warsh?", "¿Qué muestra la «segunda canonización» (Nasser)?", "¿Cómo responde la mejor apologética (Yaqeen) y dónde falla?"],
  "«Divergencias entre Coranes» (686 palabras) analiza un único caso (Hud 11:81). Este dossier es el tratamiento sistemático de la doctrina y de su historia.",
  ["Bujārī 4992, 4991; Muslim 818-821", "Ibn Mujāhid, Kitāb al-Sabʿa", "Nasser, The Transmission of the Variant Readings of the Qurʾān (Brill 2013); The Second Canonization of the Qurʾān (2020)", "van Putten, Quranic Arabic (Brill 2022, acceso abierto)", "Dutton, Journal of Qur'anic Studies", "Khatib & Khan (Yaqeen), «The Origins of the Variant Readings of the Qur'an»"],
  ["C-R03-08", "C-R03-07"], "R03", "R10", "R02", "8.000-10.000", False),
 ("D03", "ijaz-desafio-coranico", "El Desafío del Corán: | La Inimitabilidad (Iʿjāz) como Argumento",
  "respondiendo-al-islam", "esmeralda", ISL, "Hamza Tzortzis, Sapience Institute, Yaqeen; tradición clásica (al-Bāqillānī, al-Jurjānī)",
  "El argumento de la inimitabilidad no es verificable por un criterio público: o es circular (el juez del desafío es el propio creyente), o depende de un juicio estético sin procedimiento, o se refugia en la ṣarfa. No puede funcionar como prueba para un no musulmán.",
  ["¿Qué exige exactamente el taḥaddī (Q 2:23; 10:38; 11:13; 17:88; 52:34)?", "¿Qué criterios de éxito propusieron los teólogos clásicos y por qué discreparon?", "¿Es válido el argumento abductivo de Tzortzis?", "¿Qué intentos históricos existieron y cómo se descartaron?"],
  "«Surah 4:82 - Falacia» trata el argumento de la ausencia de contradicción, no el del desafío literario.",
  ["Q 2:23-24; 10:38; 11:13; 17:88; 52:33-34", "al-Bāqillānī, Iʿjāz al-Qurʾān", "ʿAbd al-Qāhir al-Jurjānī, Dalāʾil al-iʿjāz", "al-Naẓẓām y la ṣarfa", "Tzortzis, The Divine Reality", "Stewart, «Sajʿ in the Qurʾān», Journal of Arabic Literature 21 (1990)", "Encyclopaedia of the Qurʾān, s.v. «Inimitability»"],
  ["C-R03-06"], "R02", "R03", "R07", "7.000-9.000", False),
 ("D04", "embriologia-coranica-galeno", "La «Embriología Coránica»: | Q 23:12-14 ante Galeno, la Lexicografía y la Ciencia",
  "respondiendo-al-islam", "esmeralda", ISL, "Bucaillismo; Keith Moore; Hamza Tzortzis (versión 2011-2013); IslamQA",
  "La descripción coránica del desarrollo embrionario coincide con el saber médico tardoantiguo (Hipócrates, Galeno, tradición talmúdica) y contiene afirmaciones que solo son «científicas» mediante relectura léxica posterior; no constituye un milagro científico.",
  ["¿Qué significan nuṭfa, ʿalaqa, muḍgha en los léxicos clásicos?", "¿Qué decían Galeno y los médicos siríacos antes del s. VII?", "¿Qué pasa con «huesos, luego carne» y con Q 86:6-7?", "¿Por qué varios apologistas musulmanes han abandonado el argumento?"],
  "«Hadices Médicos» trata la Sunnah y «El Testigo Involuntario» la cosmología de Q 18:86. La embriología coránica no tiene dossier.",
  ["Q 22:5; 23:12-14; 40:67; 75:37-39; 86:5-7", "Galeno, De semine; De foetuum formatione", "Bujārī 3208; Muslim 2643-2645", "Lane, Arabic-English Lexicon", "Needham, A History of Embryology", "Musallam, Sex and Society in Islam", "Tzortzis, «Embryology in the Qur'an» y su retractación"],
  ["C-R03-05"], "R03", "R07", "R02", "7.000-9.000", False),
 ("D05", "mahoma-biblia-hebrea", "¿Mahoma en la Biblia Hebrea?: | Deuteronomio 18, Cantar 5:16, Hageo 2:7 e Isaías 21",
  "respondiendo-al-islam", "esmeralda", ISL, "Zakir Naik, Ahmed Deedat, Blogging Theology, IslamOnline; tradición de ʿAlī al-Ṭabarī e Ibn Rabban",
  "Ninguno de los cuatro textos admite la lectura islámica sin violar la gramática hebrea y el contexto: maḥămaddîm es un nombre común plural, ḥemdat un colectivo, «de entre tus hermanos» designa a israelitas y el oráculo de Arabia de Is 21 anuncia una derrota.",
  ["¿Qué es morfológicamente maḥămaddîm y por qué no es un nombre propio?", "¿A quién se refiere «tus hermanos» en Deuteronomio (cf. 17:15)?", "¿Cumple Mahoma los criterios de Dt 18:20-22?", "¿Qué método («correspondencias») usa la apologética islámica y por qué es infalsable?"],
  "«Isaías 42» y «Parán, Madián y Sela» cubren Is 42 y Dt 33:2/Hab 3. Estos cuatro textos y el método onomástico no están tratados.",
  ["Dt 17:15; 18:15-22; 34:10; Hch 3:22-26; 7:37", "Cant 5:10-16; Hag 2:6-9; Is 21:13-17", "HALOT y BDB s.v. ḥmd", "ʿAlī ibn Rabban al-Ṭabarī, Kitāb al-dīn wa-l-dawla", "Q 7:157; 61:6", "Lazarus-Yafeh, Intertwined Worlds (1992)", "Adang, Muslim Writers on Judaism and the Hebrew Bible (1996)"],
  ["C-R03-02", "C-R03-03", "C-R03-10", "C-R03-11"], "R03", "R08", "R02", "8.000-10.000", False),
 ("D06", "versos-satanicos-gharaniq", "Los Versos Satánicos: | El Episodio de las Gharānīq en las Fuentes Islámicas Tempranas",
  "respondiendo-al-islam", "esmeralda", ISL, "Apologética musulmana moderna que niega el episodio (Yaqeen, IslamQA, al-Albānī)",
  "El episodio está atestiguado por numerosas cadenas independientes en los dos primeros siglos del islam y fue aceptado por la primera comunidad; su rechazo es posterior y de motivación dogmática. Plantea un dilema real al criterio profético de Dt 18:20 y a la doctrina de la ʿiṣma.",
  ["¿Qué relatos transmiten al-Ṭabarī, Ibn Saʿd, al-Wāqidī y cuántas cadenas hay?", "¿Cómo se relacionan Q 53:19-23, 22:52 y 17:73-75 con el episodio?", "¿Por qué lo aceptaron Ibn Taymiyya y los primeros exegetas y por qué se rechazó después?", "¿Es aplicable el criterio de dificultad (embarazo)?"],
  "Ningún dossier existente trata el episodio (0 menciones en el mapa temático).",
  ["al-Ṭabarī, Taʾrīkh I, 1192-1196 (trad. Watt-McDonald, vol. 6)", "al-Ṭabarī, Jāmiʿ al-bayān ad Q 22:52", "Ibn Saʿd, Ṭabaqāt I", "Q 53:19-23; 22:52-53; 17:73-75", "Shahab Ahmed, Before Orthodoxy: The Satanic Verses in Early Islam (Harvard 2017)", "Burton, «Those Are the High-Flying Cranes», JSS 15 (1970)", "Ibn Taymiyya, Majmūʿ al-fatāwā X"],
  ["DIR-01"], "R10", "R03", "R02", "8.000-10.000", False),
 ("D07", "tahrif-historia-acusacion", "Historia de una Acusación: | El Taḥrīf de las Escrituras del Corán a Ibn Ḥazm",
  "respondiendo-al-islam", "esmeralda", ISL, "Islamic Discourse («The Earliest Muslims Believed in…»), Islamic Awareness, Blogging Theology",
  "El Corán y la exégesis temprana acusan a judíos y cristianos de tergiversar el sentido (taḥrīf maʿnawī) y de ocultar, no de haber alterado materialmente los libros; la tesis de la corrupción textual (lafẓī) se sistematiza con Ibn Ḥazm (s. XI) por necesidad polémica.",
  ["¿Qué dicen Q 2:75; 4:46; 5:13; 5:41 en su contexto?", "¿Qué sostienen al-Ṭabarī, al-Rāzī e Ibn ʿAbbās (en Bujārī)?", "¿Contiene el diálogo de Timoteo I con al-Mahdī la acusación, y en qué forma?", "¿Qué responden los autores musulmanes que defienden la antigüedad del taḥrīf lafẓī?"],
  "«Jeremías 8:8» y «Josías» refutan el uso de dos textos bíblicos; ninguno estudia la historia interna de la doctrina islámica.",
  ["Q 2:75-79; 3:78; 4:46; 5:13, 41; 5:43-48", "Bujārī, Kitāb al-Tawḥīd, cap. 55 (comentario atribuido a Ibn ʿAbbās)", "al-Ṭabarī y Fakhr al-Dīn al-Rāzī ad loc.", "Ibn Ḥazm, al-Fiṣal fī l-milal", "Timoteo I, Apología ante al-Mahdī (ed. Mingana 1928)", "Saeed, «The Charge of Distortion», The Muslim World 92 (2002)", "Reynolds, JAOS 130 (2010)", "Whittingham, A History of Muslim Views of the Bible (2021)"],
  ["C-R01-02", "C-R01-03", "C-R01-10"], "R01", "R10", "R03", "8.000-10.000", False),
 ("D08", "biblia-siglo-vii-texto-original", "La Biblia que Mahoma Conoció: | El «Texto Original», Epp, Ehrman y la Premisa del Corán",
  "respondiendo-al-islam", "esmeralda", ISL, "Islamic Awareness (apéndices sobre crítica textual), Calling Christians (Ijaz Ahmad), uso musulmán de Epp y Ehrman",
  "El Corán remite a la Torá y al Evangelio «que tienen ante sí» (s. VII); los grandes códices del s. IV-V y las versiones prueban que ese texto es sustancialmente el nuestro. La «multivalencia del texto original» de Epp y la «corrupción ortodoxa» de Ehrman no sostienen la conclusión que la apologética musulmana les atribuye.",
  ["¿Qué afirma realmente Epp (1999) y qué no?", "¿Qué casos de Ehrman afectan a una doctrina y cómo responde Wallace?", "¿Qué testigos del NT anteriores al 610 existen y qué cubren?", "¿Puede el argumento musulmán evitar el dilema de Q 5:47 y 10:94?"],
  "«Canon Biblia vs Quran» compara procesos de canonización; «Patrística NT» trata las citas de los Padres. Aquí se analiza el uso musulmán de la crítica textual académica y la continuidad s. IV-VII.",
  ["Epp, «The Multivalence of the Term 'Original Text'», HTR 92 (1999)", "Ehrman, The Orthodox Corruption of Scripture (1993/2011)", "Wallace (ed.), Revisiting the Corruption of the New Testament (2011)", "Códices Sinaítico, Vaticano, Alejandrino; Peshitta; Vulgata", "Q 5:43-48, 68; 7:157; 10:94", "Holmes, «From 'Original Text' to 'Initial Text'» (2013)"],
  ["C-R01-01", "C-R01-05", "C-R01-07", "C-R01-04", "C-R01-06"], "R01", "R08", "R03", "9.000-11.000", False),
 ("D09", "aqanim-trinidad-arabe", "Aqānīm: | Los Teólogos Árabes Cristianos ante la Acusación de Triteísmo",
  "respondiendo-al-islam", "esmeralda", ISL, "Mohammed Hijab, Ibn Taymiyya (al-Jawāb al-ṣaḥīḥ), objeción numérica del tawḥīd",
  "La acusación de triteísmo fue respondida en árabe y en categorías del kalām ya en el s. IX: Abū Qurra, Abū Rāʾiṭa y ʿAmmār al-Baṣrī mostraron que uqnūm no es «un dios» y que la unidad divina no es la unidad numérica de un individuo creado.",
  ["¿Qué significan uqnūm/aqānīm, jawhar, ṣifa en estos autores?", "¿Cómo argumentan a partir de los atributos divinos (vida, palabra)?", "¿Qué replicaron los mutakallimūn (al-Warrāq, ʿAbd al-Jabbār)?", "¿Qué queda vigente hoy de esa defensa?"],
  "«Tawhid y Omnipotencia» y «El Espejo Vacío» argumentan filosóficamente contra el tawḥīd; ninguno recupera la apologética árabe cristiana ni su terminología.",
  ["Teodoro Abū Qurra, Mayāmir", "Abū Rāʾiṭa al-Takrītī (ed. Keating, Brill 2006)", "ʿAmmār al-Baṣrī, Kitāb al-Burhān", "Abū ʿĪsā al-Warrāq, Radd ʿalā l-thalāth firaq (ed. Thomas)", "Griffith, The Church in the Shadow of the Mosque (2008)", "Husseini, Early Christian-Muslim Debate on the Unity of God (Brill 2014)", "Q 4:171; 5:73, 116"],
  ["C-R02-01", "C-R02-10"], "R02", "R10", "R03", "8.000-10.000", False),
 ("D10", "muere-dios-en-la-cruz", "¿Muere Dios en la Cruz?: | Impasibilidad Divina y Comunicación de Idiomas",
  "doctrina", "marino", ISL, "Khalil Andani, Mohammed Hijab, Shabir Ally: «si Jesús es Dios y murió, Dios murió»",
  "La objeción confunde naturaleza y persona. La cristología de Éfeso, Calcedonia y Constantinopla II afirma que el Verbo impasible padeció verdaderamente según la carne asumida; la predicación es real (communicatio idiomatum) sin atribuir mutación ni muerte a la naturaleza divina.",
  ["¿Qué significa «uno de la Trinidad padeció en la carne»?", "¿Es coherente predicar de un mismo sujeto propiedades contradictorias «según» naturalezas distintas (reduplicación)?", "¿Quién sostenía el universo durante el triduo?", "¿Qué responde el adversario a la estrategia reduplicativa?"],
  "«Éfeso y Calcedonia» narra los concilios y «Cristo Impecabilidad» trata el pecado. La objeción filosófico-islámica a la muerte de Dios no tiene tratamiento propio.",
  ["Cirilo, Tercera carta a Nestorio, anatematismo 12", "León Magno, Tomus ad Flavianum", "Constantinopla II (553), canon 10", "Tomás de Aquino, ST III q.16 a.4-5; q.46 a.12; q.50 a.2-3", "Weinandy, Does God Suffer? (2000)", "Gavrilyuk, The Suffering of the Impassible God (2004)", "Pawl, In Defense of Conciliar Christology (2016)"],
  ["C-R02-03"], "R02", "R05", "R03", "7.000-9.000", False),
 ("D11", "satisfaccion-vicaria-objecion", "¿Es Injusto que Uno Muera por Otros?: | La Satisfacción de Cristo ante la Objeción Islámica y Sociniana",
  "doctrina", "marino", ISL, "Shabir Ally, Zakir Naik (Q 6:164); Fausto Socino; críticos modernos de la sustitución penal",
  "La doctrina católica no enseña que el Padre castigue a un inocente en lugar de los culpables: enseña la satisfacción vicaria por amor y obediencia (Anselmo, Tomás, Trento). La objeción de injusticia alcanza a una teoría penal que el catolicismo no profesa.",
  ["¿Qué distingue satisfacción vicaria de sustitución penal?", "¿Puede un inocente satisfacer por otro sin injusticia (ST III q.48)?", "¿Admite el propio islam formas de rescate e intercesión?", "¿Qué responde la objeción sociniana y cómo se contesta?"],
  "«¿Nadie Cargará el Pecado de Otro?» es una crítica interna al Corán; aquí se expone y defiende positivamente la soteriología católica frente a la objeción.",
  ["Anselmo, Cur Deus homo", "Tomás de Aquino, ST III q.46-49", "Concilio de Trento, ses. VI, cap. 7", "CIC 599-618", "Socino, De Jesu Christo Servatore (1594)", "Stump, Atonement (OUP 2018)", "Q 6:164; 17:15; 35:18; 53:38"],
  ["DIR-02"], "R04", "R02", "R03", "7.000-9.000", False),
 ("D12", "naskh-abrogacion-versiculos-perdidos", "Naskh: | Abrogación, Aleyas Olvidadas y la Lapidación Ausente del Corán",
  "respondiendo-al-islam", "esmeralda", ISL, "Defensas contemporáneas del naskh (IslamQA, Yaqeen) y negacionistas modernos de la abrogación",
  "La doctrina clásica de la abrogación reconoce tres clases, incluida la de aleyas cuyo texto desapareció pero cuya norma sigue vigente (lapidación) y la de texto y norma retirados (lactancia). Las fuentes canónicas describen así un Corán del que se perdió material revelado.",
  ["¿Qué dicen Q 2:106 y 16:101 y cómo los leyó la exégesis clásica?", "¿Qué afirman los hadices sobre la aleya de la lapidación y las diez lactancias?", "¿Cómo armonizan los ulemas esto con Q 15:9?", "¿Qué coste tiene la salida modernista de negar el naskh?"],
  "«Dilema Mesiánico» usa «abrogación» para la relación Jesús-Torá. La doctrina islámica del naskh y los versículos perdidos no están tratados.",
  ["Q 2:106; 13:39; 15:9; 16:101; 87:6-7", "Bujārī 6829-6830; Muslim 1691 (lapidación)", "Muslim 1452 (diez lactancias); Ibn Mājah 1944", "Muslim 1050 (sura comparable a Barāʾa)", "al-Suyūṭī, al-Itqān, nawʿ 47", "Burton, The Sources of Islamic Law (1990)", "Fatoohi, Abrogation in the Qur'an and Islamic Law (2013)"],
  ["DIR-03"], "R03", "R01", "R02", "7.000-9.000", False),
 ("D13", "juan-damasceno-ismaelitas", "Juan Damasceno y la «Herejía de los Ismaelitas»: | La Primera Refutación Cristiana del Islam",
  "historia", "pergamino", ISL, "Lecturas revisionistas que niegan la autenticidad del cap. 100 y apologética musulmana que lo desautoriza",
  "El capítulo 100 del De haeresibus es auténtico, se escribió desde dentro del califato omeya y contiene ya los argumentos centrales del debate (testigos de la revelación, Verbo y Espíritu de Dios, la acusación recíproca de asociadores y mutiladores).",
  ["¿Qué prueba la tradición manuscrita sobre la autenticidad?", "¿Qué sabía Juan del Corán (suras que cita)?", "¿Cuál es su argumento del «Verbo y Espíritu»?", "¿Qué aporta como fuente externa sobre el islam primitivo?"],
  "Juan Damasceno solo aparece citado de pasada en seis dossieres; no hay estudio de su obra antiislámica.",
  ["Juan Damasceno, De haeresibus 100 (PG 94, 764-773; ed. Kotter IV)", "Disputatio Saraceni et Christiani", "Sahas, John of Damascus on Islam (Brill 1972)", "Schadler, John of Damascus and Islam (Brill 2018)", "Le Coz, Jean Damascène: Écrits sur l'Islam (SC 383)", "Hoyland, Seeing Islam as Others Saw It (1997)"],
  ["DIR-04"], "R10", "R05", "R03", "7.000-9.000", False),
 ("D14", "coran-literatura-siriaca", "El Corán y la Literatura Siríaca: | Alejandro, los Durmientes de Éfeso y José",
  "respondiendo-al-islam", "esmeralda", ISL, "Islamic Awareness (Dhū l-Qarnayn = Ciro), apologética que niega dependencias literarias",
  "Tres relatos de la sura 18 y la sura 12 reproducen rasgos específicos de textos siríacos de los siglos VI-VII (la Neṣḥānā de Alejandro, la homilía de Jacobo de Sarug, la tradición homilética sobre José); la mejor explicación es que el Corán participa de la cultura religiosa de la Antigüedad tardía.",
  ["¿Qué paralelos exactos hay entre Q 18:83-102 y la Leyenda siríaca de Alejandro?", "¿Cuál es la datación de la Neṣḥānā (Tesei vs. críticos)?", "¿Qué dirección tiene la dependencia?", "¿Funciona la identificación con Ciro?"],
  "«El Corán y los Evangelios Apócrifos» trata los relatos de María y la infancia; «El Testigo Involuntario» la puesta del sol de Q 18:86. Las fuentes siríacas no están tratadas.",
  ["Neṣḥānā d-Aleksandrōs (ed. Budge 1889)", "van Bladel, «The Alexander Legend in the Qurʾān 18:83-102» (2008)", "Tesei, The Syriac Legend of Alexander's Gate (OUP 2023)", "Jacobo de Sarug, Homilía sobre los Durmientes", "Griffith, «Christian Lore and the Arabic Qurʾān» (2008)", "Witztum, The Syriac Milieu of the Quran (tesis, Princeton 2011)", "Reynolds, The Qurʾān and Its Biblical Subtext (2010)"],
  ["C-R10-04", "DIR-05"], "R10", "R03", "R02", "8.000-10.000", False),
 ("D15", "problema-logico-trinidad", "El Problema Lógico de la Trinidad: | Identidad, Conteo y Relaciones Subsistentes",
  "filosofia", "marino", ISL, "Jake Brancatella («The Muslim Metaphysician»), Dale Tuggy, Islamic Discourse («The Logic of…»)",
  "El argumento de inconsistencia depende de leer «es» como identidad absoluta en «el Padre es Dios». La doctrina de Letrán IV y la teoría tomista de las relaciones subsistentes ofrecen un modelo formalmente consistente; el adversario debe probar que ese modelo es incoherente, no solo que es misterioso.",
  ["¿Cómo se formaliza exactamente la tríada inconsistente?", "¿Qué premisa niega cada solución (identidad relativa, constitución, relaciones)?", "¿Responde el tomismo sin caer en modalismo ni en triteísmo?", "¿Cuáles son las mejores réplicas de Tuggy y Brancatella?"],
  "«Manual Tomista», «Exactamente Tres» y «Tríada Trascendental» exponen la doctrina o argumentan a su favor; ninguno formaliza y responde el argumento de inconsistencia lógica contemporáneo.",
  ["Concilio IV de Letrán (1215), Firmiter y Damnamus", "Tomás de Aquino, ST I q.28-30, q.39 a.1-2", "Tuggy, «Trinity», Stanford Encyclopedia of Philosophy", "Brower & Rea, «Material Constitution and the Trinity», Faith and Philosophy 22 (2005)", "van Inwagen, «And Yet They Are Not Three Gods But One God» (1988)", "Branson, The Logical Problem of the Trinity (tesis, Notre Dame 2014)"],
  ["C-R02-04", "C-R02-06", "C-R02-11", "C-R06-08"], "R02", "R07", "R06", "9.000-11.000", False),
 ("D16", "unico-dios-verdadero-unitarismo", "«El Único Dios Verdadero»: | Juan 17:3, 1 Corintios 8:6 y el Shemá ante el Unitarismo",
  "exegesis", "marino", RES, "Anthony Buzzard, Dale Tuggy, Sean Finnegan; uso musulmán de la exégesis unitaria",
  "Jn 17:3 y 1 Cor 8:6 no excluyen al Hijo de la identidad divina: el primero distingue personas dentro de un evangelio que abre y cierra con la divinidad del Verbo; el segundo reparte entre el Padre y Jesús las dos palabras del Shemá (θεός, κύριος).",
  ["¿Qué alcance tiene μόνος en Jn 17:3 (cf. Jud 4; Jn 5:44)?", "¿Reformula Pablo el Shemá en 1 Cor 8:6?", "¿Qué responden los unitarios a Bauckham y Wright?", "¿Cómo leyeron el texto Agustín y Tomás?"],
  "Ningún dossier exegético trata Jn 17:3 ni el Shemá; «El Cristo de Pablo» menciona 1 Cor 8:6 sin responder la exégesis unitaria.",
  ["Jn 17:1-5; 1:1, 18; 5:44; 20:28; 1 Jn 5:20", "Dt 6:4 (MT y LXX); Mc 12:29; 1 Cor 8:4-6", "Buzzard & Hunting, The Doctrine of the Trinity (1998)", "Bauckham, Jesus and the God of Israel (2008)", "Agustín, De Trinitate VI.9; In Ioh. tract. 105", "Tomás de Aquino, ST I q.31 a.4; Super Ioannem c.17"],
  ["C-R02-08", "C-R06-07", "C-R02-09"], "R06", "R08", "R02", "7.000-9.000", False),
 ("D17", "mateo-16-roca-padres", "«Sobre Esta Piedra»: | Mateo 16:18 en la Exégesis y en los Padres",
  "exegesis", "marino", PRO, "James White, William Webster (The Matthew 16 Controversy), Gavin Ortlund",
  "La exégesis gramatical identifica la roca con Pedro (como reconocen hoy numerosos exegetas protestantes), y la pluralidad de aplicaciones patrísticas (Pedro, su fe, Cristo) no es una negación de la primera: los mismos Padres que predican la «confesión» afirman el oficio petrino.",
  ["¿Sostiene el arameo Kēphā y el juego Πέτρος/πέτρα la identificación?", "¿Qué prueba y qué no prueba el recuento de Launoy?", "¿Cómo se relacionan Is 22:22 y las llaves?", "¿Se sigue de la exégesis un oficio transmisible?"],
  "El primado solo aparece dentro de los dossieres conciliares. No existe un estudio de Mt 16:18.",
  ["Mt 16:13-19; Is 22:15-25; Jn 1:42; 21:15-17; Lc 22:31-32", "Orígenes, Comm. in Matt. XII.10-14", "Agustín, Retractationes I.21; Sermo 76", "Crisóstomo, Hom. in Matt. 54", "León Magno, Sermones 3-4", "Cullmann, Peter: Disciple, Apostle, Martyr", "Davies & Allison, Matthew (ICC) II", "Webster, The Matthew 16 Controversy (1996)"],
  ["C-R04-06"], "R04", "R05", "R09", "9.000-11.000", True),
 ("D18", "cipriano-catedra-pedro", "Cipriano y la Cátedra de Pedro: | De unitate 4, Esteban I y la Controversia Bautismal",
  "historia", "pergamino", PRO, "Ligonier («The Rise of the Papacy»), Geoffrey Dunn, William Webster",
  "Las dos recensiones de De unitate 4 son de Cipriano; su doctrina reconoce en la sede de Pedro el origen de la unidad episcopal («ecclesia principalis»). Su resistencia a Esteban muestra una teoría del primado aún no desarrollada, no su inexistencia; y fue la posición de Roma la que la Iglesia recibió.",
  ["¿Qué dice cada recensión y cuál es su relación (Bévenot)?", "¿Qué significa «ecclesia principalis unde unitas sacerdotalis exorta est» (Ep. 59.14)?", "¿Qué prueba el conflicto con Esteban y la carta de Firmiliano?", "¿Cómo debe usar el apologista católico a Cipriano sin exagerar?"],
  "Cipriano aparece citado en varios dossieres pero no hay estudio de su eclesiología ni de la cuestión textual.",
  ["Cipriano, De catholicae ecclesiae unitate 4-5 (CCSL 3; Bévenot, ACW 25)", "Cipriano, Epp. 55, 59, 67-75", "Sententiae episcoporum LXXXVII", "Eusebio, HE VII.2-9", "Bévenot, St. Cyprian's De Unitate chap. 4 in the Light of the Manuscripts (1937)", "Dunn, Cyprian and the Bishops of Rome (2007)"],
  ["C-R04-01", "C-R04-07"], "R04", "R10", "R05", "8.000-10.000", False),
 ("D19", "obispo-monarquico-roma", "¿Hubo un Obispo en Roma antes del 150?: | Clemente, Ignacio, Hermas e Ireneo ante la Tesis de Lampe",
  "historia", "pergamino", PRO, "Peter Lampe, Allen Brent, Eamon Duffy (como concesión católica), uso protestante y ortodoxo de esta tesis",
  "Que la Iglesia romana tuviera gobierno colegial en el s. I no refuta la sucesión apostólica: 1 Clemente afirma un orden instituido por los apóstoles con sucesión; la lista de Ireneo y Hegesipo es anterior a la controversia; y el desarrollo del monoepiscopado es explicitación de un ministerio de presidencia ya presente.",
  ["¿Qué prueba exactamente Lampe y qué infiere de más?", "¿Qué enseña 1 Clem 42-44 sobre la sucesión?", "¿Es fiable la lista de Ireneo (AH III.3.3)?", "¿Afecta la datación tardía de Ignacio al argumento?"],
  "Es la objeción académica más fuerte contra el papado y no aparece en ningún dossier (sucesión apostólica: 3 menciones marginales).",
  ["1 Clemente 40-44; 63", "Ignacio, Ad Romanos, prólogo", "Hermas, Visión 2.4.3", "Ireneo, Adv. haer. III.3.1-3", "Hegesipo ap. Eusebio, HE IV.22", "Lampe, From Paul to Valentinus (2003)", "Sullivan, From Apostles to Bishops (2001)", "Stewart, The Original Bishops (2014)"],
  ["DIR-06", "C-R10-06"], "R05", "R10", "R04", "9.000-11.000", False),
 ("D20", "hebreos-sacrificio-misa", "«Una Vez para Siempre»: | Hebreos 9-10 y el Sacrificio de la Misa",
  "doctrina", "marino", PRO, "James White, TurretinFan («Offered Often or Once?»), Heidelblog",
  "Hebreos excluye la repetición del sacrificio cruento, no su presencia sacramental. Trento enseña un único sacrificio y una única víctima con distinto modo de ofrecerse; la liturgia celestial del propio Hebreos (7:25; 8:1-3; 9:24) y Mal 1:11 exigen una ofrenda perenne.",
  ["¿Qué niega exactamente ἐφάπαξ?", "¿Qué significa que Cristo «tiene algo que ofrecer» en el santuario celestial (8:3)?", "¿Qué entendían por «sacrificio» Didaché 14, Justino e Ireneo?", "¿Responde la distinción repetición/re-presentación al argumento del aoristo?"],
  "«La Transubstanciación» trata la presencia real. El carácter sacrificial de la Misa no tiene dossier.",
  ["Heb 7:23-27; 8:1-6; 9:11-28; 10:1-18; 13:10", "Mal 1:11; 1 Cor 10:14-21; 11:23-26", "Didaché 14; Justino, Dial. 41 y 117; Ireneo, AH IV.17-18", "Crisóstomo, Hom. in Heb. 17", "Concilio de Trento, ses. XXII, cap. 1-2 y cánones", "CIC 1362-1372"],
  ["C-R04-02"], "R04", "R01", "R09", "7.000-9.000", False),
 ("D21", "deuterocanonicos-canon-antiguo-testamento", "Los Deuterocanónicos: | ¿Añadió Trento Libros a la Biblia?",
  "biblia", "pergamino", PRO, "Ligonier, Michael Kruger, Roger Beckwith; Dan McClellan como voz crítica",
  "No existió un canon hebreo cerrado y universal antes de Cristo que la Iglesia hubiera debido recibir; las listas latinas de 393-419, Florencia y Trento ratifican el uso litúrgico predominante. Las dudas de Jerónimo y Atanasio son reales y deben explicarse, no ocultarse.",
  ["¿Qué prueban Josefo, el prólogo del Sirácida y Qumrán sobre un canon cerrado?", "¿Qué estatus dan Atanasio y Jerónimo a estos libros?", "¿Qué decidieron Hipona, Cartago y Florencia?", "¿Es el «sínodo de Jamnia» un argumento válido para alguien?"],
  "«Contra la Sola Scriptura» toca el canon como argumento contra el principio. La cuestión histórica de los deuterocanónicos no tiene dossier.",
  ["Josefo, Contra Apionem I.37-43", "Atanasio, Carta festal 39", "Jerónimo, Prologus galeatus; prólogos a Tobías y Judit", "Agustín, De doctrina christiana II.8", "Breviarium Hipponense; Cartago 397 y 419", "Florencia, Cantate Domino (1442); Trento, ses. IV", "Gallagher & Meade, The Biblical Canon Lists from Early Christianity (2017)", "Beckwith, The Old Testament Canon of the New Testament Church (1985)"],
  ["C-R04-03", "C-R09-09", "C-R04-12"], "R01", "R08", "R04", "9.000-11.000", False),
 ("D22", "atar-desatar-penitencia", "«A Quienes Perdonéis los Pecados»: | Juan 20:23 y la Penitencia en la Iglesia Antigua",
  "doctrina", "marino", PRO, "Calvino (Inst. III.4), exégesis evangélica del perfecto pasivo (Mantey), GotQuestions",
  "Jn 20:21-23 confiere un poder judicial de perdonar y retener que supone conocimiento de los pecados; la Iglesia de los siglos II-III lo ejerció mediante la exomologesis ante el obispo. La forma privada es desarrollo disciplinar de una potestad idéntica.",
  ["¿Qué implica el perfecto ἀφέωνται / κεκράτηνται?", "¿A quién se dirige el mandato: a los apóstoles o a todo creyente?", "¿Qué muestran Tertuliano, Cipriano y Orígenes sobre la práctica?", "¿Cuándo y cómo aparece la confesión privada reiterable?"],
  "Ningún dossier trata la confesión sacramental (las 11 menciones del mapa son incidentales).",
  ["Jn 20:19-23; Mt 16:19; 18:15-18; 2 Cor 2:5-11; Stg 5:14-16", "Didaché 4.14; 14.1", "Tertuliano, De paenitentia 7-10; De pudicitia", "Cipriano, De lapsis 28-29", "Orígenes, Hom. in Lev. 2.4", "Concilio de Trento, ses. XIV", "Poschmann, Penance and the Anointing of the Sick (1964)"],
  ["C-R04-04"], "R04", "R09", "R05", "7.000-9.000", False),
 ("D23", "desarrollo-doctrinal-newman", "¿Desarrollo o Corrupción?: | Newman, Vicente de Lerins y el Argumento de las «Acreciones»",
  "doctrina", "marino", PRO, "Gavin Ortlund (What It Means to Be Protestant, 2024), Brandon Kenny, Triablogue",
  "La acusación de «acreciones» presupone un criterio que el protestantismo no puede aplicar a sus propias doctrinas (canon, sola fide, Trinidad nicena). La teoría del desarrollo no es una licencia: ofrece criterios y es coherente con el propio Vicente de Lerins (Commonitorium 23).",
  ["¿Qué exige realmente el canon vicentino y qué dice el capítulo 23?", "¿Son operativas las siete notas de Newman o infalsables?", "¿Cuál es el caso más difícil (Asunción, infalibilidad)?", "¿Supera el protestantismo su propio test?"],
  "Los dossieres marianos defienden dogmas concretos. El principio del desarrollo doctrinal, que los sostiene a todos, no está tratado.",
  ["Vicente de Lerins, Commonitorium 2 y 23", "Newman, An Essay on the Development of Christian Doctrine (1878)", "Dei Verbum 8-10", "Vaticano I, Dei Filius cap. 4", "Ortlund, What It Means to Be Protestant (2024)", "Guarino, Vincent of Lérins and the Development of Christian Doctrine (2013)"],
  ["C-R04-05", "C-R04-08"], "R09", "R04", "R05", "8.000-10.000", False),
 ("D24", "hermanos-de-jesus-virginidad-perpetua", "Los «Hermanos» de Jesús: | La Virginidad Perpetua de María ante la Exégesis",
  "doctrina", "marino", PRO, "Eric Svendsen (Who Is My Mother?), John P. Meier (posición helvidiana académica), James White",
  "El NT no nombra nunca a hijos de María; dos de los «hermanos» son hijos de otra María (Mc 15:40); Jn 19:26-27 es difícilmente explicable si existían. La lectura helvidiana es posible léxicamente pero no exigida, y la tradición de los siglos II-IV la desconoce hasta Helvidio.",
  ["¿Qué alcance tiene ἀδελφός en griego judío y por qué no se usa ἀνεψιός?", "¿Qué implica ἕως οὗ en Mt 1:25?", "¿Quiénes son Santiago y José de Mc 15:40?", "¿Cuál es la respuesta al argumento de Meier?"],
  "«María, Madre de Dios» menciona la cuestión una vez. No tiene tratamiento propio.",
  ["Mt 1:18-25; 12:46-50; 13:55-56; 27:56; Mc 6:3; 15:40; Jn 19:25-27; Gal 1:19", "Protoevangelio de Santiago 9; 17-19", "Hegesipo ap. Eusebio, HE III.11; IV.22", "Jerónimo, Adversus Helvidium", "Epifanio, Panarion 78", "Meier, A Marginal Jew I (1991), cap. 10", "Bauckham, Jude and the Relatives of Jesus (1990)"],
  ["DIR-07"], "R09", "R08", "R04", "8.000-10.000", False),
 ("D25", "primado-jurisdiccion-primer-milenio", "¿Primado de Honor o de Jurisdicción?: | El Primer Milenio ante el Vaticano I",
  "historia", "pergamino", ORT, "Ubi Petrus, Craig Truglia (Orthodox Christian Theology), Edward Siecienski, Documento de Chieti leído en clave ortodoxa",
  "Las fuentes del primer milenio muestran a Roma ejerciendo y a Oriente reconociendo, en momentos decisivos, una autoridad que excede la precedencia honorífica (apelaciones de Sárdica, Fórmula de Hormisdas, carta de Agatón). Hay continuidad sustancial con Pastor Aeternus, y también un desarrollo real que debe admitirse.",
  ["¿Qué significa «primado de honor» en las fuentes (πρεσβεῖα τῆς τιμῆς)?", "¿Qué firmaron los obispos orientales con la Fórmula de Hormisdas?", "¿Cómo recibió Constantinopla III la carta de Agatón?", "¿Cuáles son los mejores contraejemplos ortodoxos?"],
  "«Concilio de Florencia» y «Vaticano II» tocan el primado en su momento histórico. El dossier del primer milenio no existe.",
  ["Concilio de Sárdica, cánones 3-5", "Fórmula de Hormisdas (519), Collectio Avellana", "Agatón, carta a Constantino IV (Mansi XI)", "Máximo el Confesor, Opuscula 11-12", "Pastor Aeternus, cap. 2-3", "Documentos de Rávena (2007), Chieti (2016) y Alejandría (2023)", "Siecienski, The Papacy and the Orthodox (2017)", "Schatz, Papal Primacy (1996)"],
  ["C-R05-01", "C-R05-08", "C-R05-07"], "R05", "R09", "R04", "10.000-12.000", False),
 ("D26", "honorio-vigilio-liberio-infalibilidad", "Honorio, Vigilio y Liberio: | Tres Papas ante la Infalibilidad",
  "historia", "pergamino", ORT, "Craig Truglia, Ubi Petrus; Döllinger; uso protestante (James White)",
  "Ninguno de los tres casos cumple las condiciones de una definición ex cathedra fijadas por Pastor Aeternus: Honorio escribió cartas privadas de gobierno que fueron condenadas por negligencia; Vigilio vaciló bajo coacción en una cuestión de personas; Liberio cedió en el destierro. Los casos prueban que un papa puede fallar gravemente, no que la definición sea falsa.",
  ["¿Qué dijo exactamente Honorio a Sergio y por qué lo anatematizó el VI concilio?", "¿Cómo matizó León II la condena?", "¿Fue el Constitutum de Vigilio un acto magisterial definitivo?", "¿Es el criterio ex cathedra una inmunización ad hoc?"],
  "«Concilios de Constantinopla» dedica una sección a Honorio. Aquí se estudian los tres casos con sus fuentes y la objeción de infalsabilidad.",
  ["Honorio, cartas a Sergio (Mansi XI, 537-544 y 579)", "Constantinopla III, sesiones XIII y XVIII", "León II, cartas a Constantino IV y a los obispos hispanos", "Vigilio, Constitutum I y II", "Atanasio, Historia Arianorum 41; Hilario, Fragmenta historica", "Pastor Aeternus, cap. 4; relatio de Gasser", "Chapman, The Condemnation of Pope Honorius (1907)", "Price, The Acts of the Council of Constantinople of 553 (2009)"],
  ["C-R05-02", "C-R04-11"], "R05", "R10", "R09", "10.000-12.000", True),
 ("D27", "canon-28-calcedonia", "El Canon 28 de Calcedonia: | Roma, Constantinopla y el Fundamento del Primado",
  "historia", "pergamino", ORT, "Craig Truglia («Did Rome Accept Constantinople I Before Chalcedon?»), eclesiología ortodoxa del «principio de acomodación»",
  "El canon 28 funda el rango en la capitalidad política; León lo rechazó por contradecir Nicea y los propios padres conciliares pidieron su confirmación, reconociendo que dependía de ella. El episodio documenta dos teorías del primado y muestra cuál se sometió al juicio de la otra.",
  ["¿Qué dice el canon y en qué sesión se aprobó?", "¿Qué pide la carta sinodal a León (Ep. 98)?", "¿Qué responden León (Epp. 104-106) y Anatolio (Ep. 132)?", "¿Aceptó Roma más tarde el rango de Constantinopla, y qué prueba eso?"],
  "«Éfeso y Calcedonia» trata la cristología del concilio; el canon 28 y su recepción no están estudiados.",
  ["Constantinopla I, canon 3; Calcedonia, canon 28 y sesión XVI", "León Magno, Epp. 98, 104, 105, 106, 132", "Nicea I, canon 6", "Price & Gaddis, The Acts of the Council of Chalcedon (2005)", "L'Huillier, The Church of the Ancient Councils (1996)", "Letrán IV, canon 5"],
  ["C-R05-03"], "R05", "R09", "R10", "7.000-9.000", False),
 ("D28", "esencia-energias-simplicidad", "Esencia y Energías: | La Objeción Palamita a la Simplicidad Divina Tomista",
  "filosofia", "marino", ORT, "Jay Dyer, David Bradshaw (Aristotle East and West), polémica neopalamita",
  "La simplicidad divina tomista no hace de la gracia algo creado en sentido que impida la deificación ni de la visión beatífica una comprensión de la esencia. La distinción real esencia-energías, tomada como distinción en Dios, introduce composición; leída como distinción formal o de razón con fundamento, es compatible con Tomás.",
  ["¿Qué tipo de distinción afirma Palamas y qué definió el Tomo de 1351?", "¿Qué niega Tomás cuando niega composición en Dios?", "¿Es la gracia creada un obstáculo para la participación real en Dios?", "¿Es convincente la tesis de Bradshaw sobre energeia?"],
  "La web desarrolla la simplicidad divina contra el islam y el teísmo neoclásico. La objeción ortodoxa no aparece (0 menciones de Palamas).",
  ["Gregorio Palamas, Tríadas III; Capita 150", "Tomo sinodal de 1351", "Tomás de Aquino, ST I q.3; q.12; q.13; I-II q.110", "Benedicto XII, Benedictus Deus (1336)", "Bradshaw, Aristotle East and West (2004)", "Williams, The Ground of Union (1999)", "Jugie, «Palamas» y «Palamite (controverse)», DTC"],
  ["C-R05-05"], "R07", "R05", "R02", "9.000-11.000", False),
 ("D29", "pseudo-isidoro-donacion-constantino", "Las Falsas Decretales: | ¿Se Construyó el Papado sobre Falsificaciones?",
  "historia", "pergamino", ORT, "Döllinger («Janus»), polémica ortodoxa y protestante, Ubi Petrus",
  "Las Decretales pseudoisidorianas (c. 850) se forjaron en la Galia para proteger a los obispos frente a metropolitanos y poder civil, no en Roma ni para crear el primado; las prerrogativas que el papado reivindicaba están documentadas siglos antes en textos auténticos. Fueron católicos quienes probaron la falsedad.",
  ["¿Dónde, cuándo y para qué se fabricaron?", "¿Qué uso hicieron de ellas Nicolás I y los canonistas?", "¿Qué pretensiones papales auténticas son anteriores al 850?", "¿Qué papel tuvo la Donación de Constantino?"],
  "Ningún dossier trata la objeción de las falsificaciones.",
  ["Decretales Pseudo-Isidorianae (ed. Hinschius 1863)", "Constitutum Constantini (ed. Fuhrmann, MGH)", "Lorenzo Valla, De falso credita… donatione (1440)", "Fuhrmann, Einfluss und Verbreitung der pseudoisidorischen Fälschungen (1972-74)", "Knibbs, «Ebo of Reims, Pseudo-Isidore…», Speculum 92 (2017)", "León Magno, Gelasio I (Duo sunt), Siricio: decretales auténticas"],
  ["C-R05-12"], "R05", "R09", "R04", "7.000-9.000", False),
 ("D30", "libro-de-abraham-papiros", "El Libro de Abraham y los Papiros de José Smith: | Un Test Empírico de una Traducción Profética",
  "refutaciones", "pergamino", RES, "FAIR Latter-day Saints, John Gee, Kerry Muhlestein; ensayo oficial «Translation and Historicity of the Book of Abraham»",
  "Los papiros recuperados en 1967 son textos funerarios de época ptolemaica (Libro de las Respiraciones) y los facsímiles se interpretan en contra de la egiptología. Las hipótesis de rescate (rollo perdido, papiro como «catalizador») sacrifican la pretensión original de traducción.",
  ["¿Qué son los papiros I, X y XI y qué dicen?", "¿Qué muestran los Kirtland Egyptian Papers sobre el método?", "¿Son correctas las explicaciones de los facsímiles?", "¿Qué fuerza tienen las teorías del rollo perdido y del catalizador?"],
  "No existe ningún dossier sobre mormonismo.",
  ["Joseph Smith Papyri I, X, XI (Church History Library)", "Perla de Gran Precio: Libro de Abraham y Facsímiles 1-3", "Kirtland Egyptian Papers (Joseph Smith Papers)", "Gospel Topics Essay (2014)", "Ritner, The Joseph Smith Egyptian Papyri: A Complete Edition (2011)", "Baer, Dialogue 3 (1968)", "Gee, An Introduction to the Book of Abraham (2017)"],
  ["C-R06-02"], "R06", "R01", "R09", "8.000-10.000", False),
 ("D31", "607-1914-cronologia-testigos", "607 a.C. y 1914: | La Cronología de los Testigos de Jehová ante las Fuentes Babilónicas",
  "refutaciones", "pergamino", RES, "Watch Tower (La Atalaya, 1 de octubre y 1 de noviembre de 2011), Rolf Furuli",
  "Jerusalén cayó en 587/586 a.C.: lo establecen de forma independiente las crónicas babilónicas, miles de tablillas comerciales fechadas, los diarios astronómicos y el Canon de Ptolomeo. Sin 607 no hay 1914, y con ello cae el fundamento de la autoridad del Cuerpo Gobernante.",
  ["¿Qué líneas de evidencia independientes fijan los reinados neobabilónicos?", "¿Qué dice VAT 4956 y cómo lo reinterpreta Furuli?", "¿Exigen Jer 25 y 29 setenta años de desolación desde la caída?", "¿Qué depende doctrinalmente de 1914?"],
  "No existe ningún dossier sobre los Testigos de Jehová.",
  ["BM 21946 (Crónica de Nabucodonosor)", "VAT 4956 (diario astronómico, año 37)", "Estela de Adad-guppi (Harrán)", "Canon de Ptolomeo; lista real de Uruk", "Jer 25:8-12; 29:10; 2 Cr 36:20-23; Dn 9:2; Zac 1:12; 7:5", "La Atalaya, «¿Cuándo fue destruida la antigua Jerusalén?» (2011)", "Jonsson, The Gentile Times Reconsidered (4ª ed. 2004)", "Parker & Dubberstein, Babylonian Chronology (1956)"],
  ["C-R06-03"], "R06", "R08", "R01", "9.000-11.000", True),
 ("D32", "jehova-nuevo-testamento-nombre-divino", "«Jehová» en el Nuevo Testamento: | El Nombre Divino, los Manuscritos y la Traducción del Nuevo Mundo",
  "biblia", "pergamino", RES, "Watch Tower (TNM, Apéndices A5 y C), tesis de George Howard",
  "Ninguno de los más de 5.000 manuscritos griegos del NT contiene el Tetragrámaton; las 237 inserciones de la TNM son conjetura. Además, el NT aplica a Jesús textos del AT sobre YHWH (Rom 10:13; Flp 2:10-11; Heb 1:10), y la restitución selectiva oculta esa identificación.",
  ["¿Qué muestran P. Fouad 266, 8ḤevXIIgr y 4Q120 sobre la LXX precristiana?", "¿Qué afirmó Howard (1977) y cómo fue respondido?", "¿Qué criterio usa la TNM para decidir dónde insertar el Nombre?", "¿Qué implica el uso de los nomina sacra?"],
  "«Juan 11» (Jn 1:1) trata un versículo de la TNM. La cuestión del Nombre divino en el NT no está tratada.",
  ["TNM (2013), Apéndices A5 y C", "P. Fouad 266; 8ḤevXIIgr; 4Q120; P.Oxy. 3522", "Howard, «The Tetragram and the New Testament», JBL 96 (1977)", "Pietersma, «Kyrios or Tetragram» (1984)", "Rom 10:9-13 / Jl 3:5; Flp 2:9-11 / Is 45:23; Heb 1:10-12 / Sal 102", "Hurtado, The Earliest Christian Artifacts (2006)", "Orígenes, In Ps. 2; Jerónimo, Prologus galeatus"],
  ["DIR-08", "C-R06-12"], "R01", "R06", "R08", "8.000-10.000", False),
 ("D33", "gran-apostasia-restauracionismo", "La «Gran Apostasía»: | El Presupuesto Común del Restauracionismo ante la Historia",
  "historia", "pergamino", RES, "FAIR («Apostasy»), James Talmage; Watch Tower; Ellen White (El conflicto de los siglos)",
  "Mormones, Testigos y adventistas dependen de la tesis de que la Iglesia visible desapareció o se corrompió totalmente poco después de los apóstoles. Esa tesis contradice las promesas de Cristo, carece de fecha y de testigos, y choca con la continuidad documentada de doctrina, ministerio y culto entre 95 y 200.",
  ["¿Cuándo sitúa cada grupo la apostasía y con qué prueba?", "¿Qué predicen realmente 2 Tes 2:3 y Hch 20:29?", "¿Qué continuidad muestran Clemente, Ignacio, Policarpo, Justino e Ireneo?", "¿Por qué la tesis es infalsable y qué coste tiene?"],
  "Ningún dossier trata el presupuesto restauracionista. «El Mito del Sincretismo Pagano» responde acusaciones concretas, no la tesis de la apostasía total.",
  ["Mt 16:18; 28:20; Jn 16:13; 1 Tim 3:15; 2 Tes 2:1-12; Hch 20:28-30", "Doctrina y Convenios 1:30; José Smith-Historia 1:18-19", "Talmage, The Great Apostasy (1909)", "1 Clemente; Ignacio; Policarpo; Ireneo, AH III.3-4", "Tertuliano, De praescriptione 20-32", "Reynolds (ed.), Early Christians in Disarray (BYU 2005)"],
  ["DIR-09", "C-R06-04"], "R06", "R09", "R10", "8.000-10.000", False),
 ("D34", "theosis-exaltacion-mormona", "¿Enseñaron los Padres que Seremos Dioses?: | Theosis Patrística y Exaltación Mormona",
  "doctrina", "marino", RES, "FAIR, Gospel Topics Essay «Becoming Like God», Jordan Vajda, Keith Norman",
  "La deificación patrística es participación por gracia de la criatura en la vida del único Dios increado; presupone la creación ex nihilo y la distinción infinita Creador-criatura. La exaltación mormona presupone que Dios y el hombre son de la misma especie. La coincidencia es de vocabulario.",
  ["¿Qué enseñan el sermón de King Follett y D&C 132?", "¿Qué afirman Ireneo y Atanasio en su contexto?", "¿Qué límites pone la tradición (2 Pe 1:4; Letrán IV)?", "¿Es justa la cita mormona de los Padres?"],
  "No existe dossier sobre mormonismo; la theosis solo aparece de pasada.",
  ["José Smith, King Follett Discourse (1844)", "Doctrina y Convenios 130:22; 132:19-20", "Gospel Topics Essay, «Becoming Like God»", "Ireneo, AH IV.38; V, praef.", "Atanasio, De incarnatione 54; Contra Arianos I.39", "Sal 82:6; Jn 10:34-36; 2 Pe 1:4", "Letrán IV, cap. 2", "Russell, The Doctrine of Deification in the Greek Patristic Tradition (2004)"],
  ["C-R06-06"], "R06", "R10", "R05", "7.000-9.000", False),
 ("D35", "ocultamiento-divino", "El Ocultamiento Divino: | ¿Por Qué No Es Evidente la Existencia de Dios?",
  "filosofia", "marino", FIL, "J. L. Schellenberg; Internet Encyclopedia of Philosophy y SEP como estado de la cuestión",
  "La premisa de que un Dios perfectamente amoroso garantizaría a toda persona no resistente una creencia explícita en cada momento es falsa: confunde la relación personal con Dios con la creencia proposicional y supone una concepción del amor divino ajena al teísmo clásico.",
  ["¿Cuál es la formulación más fuerte del argumento (2015)?", "¿Existe la incredulidad no resistente y qué dice de ella el Magisterio (LG 16)?", "¿Qué bienes exigen distancia epistémica?", "¿Qué responde Schellenberg a cada estrategia?"],
  "El mapa temático no registra ningún tratamiento del ocultamiento divino ni del problema del mal.",
  ["Schellenberg, Divine Hiddenness and Human Reason (1993); The Hiddenness Argument (2015)", "Howard-Snyder & Green, «Hiddenness of God», SEP", "Rea, The Hiddenness of God (2018)", "Pascal, Pensées (Deus absconditus); Is 45:15", "Tomás de Aquino, ST I q.2 a.1; II-II q.2 a.3-7; q.10 a.1", "Vaticano I, Dei Filius cap. 2; Lumen gentium 16; Gaudium et spes 19-21"],
  ["C-R07-03"], "R07", "R02", "R09", "8.000-10.000", True),
 ("D36", "problema-evidencial-mal", "El Mal como Evidencia: | Rowe, Draper y el Sufrimiento Animal ante el Teísmo Clásico",
  "filosofia", "marino", FIL, "William Rowe, Paul Draper, Jeffery Jay Lowder (Secular Web)",
  "El argumento evidencial compara el teísmo con una «hipótesis de indiferencia» atribuyendo a Dios las obligaciones de un agente moral dentro del mundo. El teísmo clásico (Dios como causa del ser, el mal como privación) cambia las probabilidades relevantes; el sufrimiento animal sigue siendo la dificultad más seria.",
  ["¿Cómo se formaliza el argumento bayesiano de Draper?", "¿Qué fuerza tiene el teísmo escéptico y qué coste?", "¿Es Dios un agente moral obligado (Davies)?", "¿Qué puede decirse honestamente del dolor animal prehumano?"],
  "El problema del mal no tiene ninguna cobertura en la web (0 menciones).",
  ["Rowe, «The Problem of Evil and Some Varieties of Atheism», APQ 16 (1979)", "Draper, «Pain and Pleasure», Noûs 23 (1989)", "Tomás de Aquino, ST I q.2 a.3 ad 1; q.19 a.9; q.22; q.48-49; SCG III.71", "Agustín, Enchiridion 11", "Davies, The Reality of God and the Problem of Evil (2006)", "Murray, Nature Red in Tooth and Claw (2008)", "Stump, Wandering in Darkness (2010)"],
  ["C-R07-02"], "R07", "R02", "R06", "9.000-11.000", False),
 ("D37", "inercia-existencial-conservacion", "La Inercia Existencial: | ¿Necesitan las Cosas a Dios para Seguir Existiendo?",
  "filosofia", "marino", FIL, "Joseph Schmid y Daniel Linford (Existential Inertia and Classical Theistic Proofs, 2023), Graham Oppy",
  "La tesis de la inercia existencial no neutraliza las pruebas tomistas: o es un hecho bruto, o se funda en la naturaleza de las cosas, y en este caso presupone que la esencia explica su propio acto de ser, lo que la distinción real entre essentia y esse excluye en todo ente contingente.",
  ["¿Qué versiones de la inercia existencial distingue Schmid?", "¿Depende la prueba de la conservación de la distinción real?", "¿Es la persistencia un «no-cambio» que no requiere causa?", "¿Cuál es la réplica de Schmid a Feser?"],
  "Los dossieres tomistas tratan la Trinidad, la eternidad y el colapso modal. La conservación en el ser frente a Schmid no está tratada.",
  ["Tomás de Aquino, ST I q.104 a.1-2; De potentia q.5 a.1; De ente et essentia c.4", "Schmid & Linford, Existential Inertia and Classical Theistic Proofs (Springer 2023)", "Schmid, «Existential Inertia and the Aristotelian Proof», IJPR 89 (2021)", "Feser, Five Proofs of the Existence of God (2017); ACPQ 85 (2011)", "Fabro, Participation et causalité (1961)"],
  ["C-R07-01"], "R07", "R02", "R06", "8.000-10.000", False),
 ("D38", "razon-suficiente-hechos-brutos", "¿Puede Haber Hechos Brutos?: | El Principio de Razón Suficiente y el Argumento de la Contingencia",
  "filosofia", "marino", FIL, "Graham Oppy (Arguing about Gods), Felipe Leon, Peter van Inwagen (objeción del colapso modal al PRS)",
  "El naturalista que acepta un hecho contingente inexplicado paga un precio epistémico que socava la práctica explicativa de la ciencia. Una versión restringida del principio basta para el argumento de la contingencia y no implica necesitarismo.",
  ["¿Qué versión del PRS necesita el argumento?", "¿Cómo se evita el colapso modal de van Inwagen?", "¿Es legítimo el criterio de «argumento exitoso» de Oppy?", "¿Por qué el ser necesario no puede ser el universo?"],
  "«Tomismo, Eternidad y Colapso Modal» trata el colapso modal de la libertad divina. El PRS y los hechos brutos no están tratados; no hay dossier sobre argumentos cosmológicos.",
  ["Leibniz, Monadología 31-39; Principios de la naturaleza y de la gracia 7-8", "Tomás de Aquino, ST I q.2 a.3 (tertia via); De ente c.4", "Pruss, The Principle of Sufficient Reason (2006)", "Pruss & Rasmussen, Necessary Existence (2018)", "van Inwagen, An Essay on Free Will (1983), 202-204", "Oppy, Arguing about Gods (2006)", "Della Rocca, «PSR», Philosophers' Imprint 10 (2010)"],
  ["C-R07-11", "C-R07-10", "C-R07-12", "C-R07-04"], "R07", "R06", "R02", "9.000-11.000", False),
 ("D39", "intelecto-inmaterial-neurociencia", "Mente, Cerebro y Alma: | La Inmaterialidad del Intelecto ante la Neurociencia",
  "filosofia", "marino", FIL, "Materialismo eliminativo y fisicalismo (Churchland, Kim); lectura popular de Libet",
  "La dependencia del pensamiento respecto del cerebro es exactamente lo que el hilemorfismo predice; no refuta que el acto intelectual, por su determinación semántica y su universalidad, no pueda ser una operación de un órgano material (argumento de Ross).",
  ["¿En qué difiere el hilemorfismo del dualismo cartesiano?", "¿Qué prueba y qué no prueba la correlación neuronal?", "¿Es sólido el argumento de la indeterminación de lo físico?", "¿Cómo responde el tomismo al problema de la interacción y al cierre causal?"],
  "Las 16 menciones de «alma» en la web son incidentales. No hay dossier de antropología filosófica.",
  ["Aristóteles, De anima III.4-5", "Tomás de Aquino, ST I q.75 a.2, a.6; q.76 a.1; q.84 a.6-7; Q. D. De anima", "Ross, «Immaterial Aspects of Thought», Journal of Philosophy 89 (1992)", "Feser, «Kripke, Ross, and the Immaterial Aspects of Thought», ACPQ 87 (2013)", "Concilio de Vienne (1312); Letrán V (1513)", "Madden, Mind, Matter, and Nature (2013)"],
  ["C-R07-08"], "R02", "R07", "R06", "8.000-10.000", False),
 ("D40", "hume-bayes-milagros", "Hume, Bayes y los Milagros: | ¿Puede un Testimonio Hacer Creíble una Resurrección?",
  "filosofia", "marino", FIL, "David Hume; Bart Ehrman («el historiador no puede afirmar milagros»); Richard Carrier",
  "El argumento de Hume, formalizado, es inválido (Earman): la probabilidad previa baja de un milagro puede ser superada por testimonios independientes. La cuestión se decide por la evidencia concreta y por la plausibilidad previa del teísmo, no por un veto metodológico.",
  ["¿Cuál es la estructura bayesiana del argumento de Hume?", "¿Qué exige la independencia de testigos?", "¿Viola un milagro las leyes de la naturaleza según Tomás?", "¿Cómo se responde a los paralelos (Apolonio, Vespasiano)?"],
  "«Método Histórico» trata los límites del método histórico-crítico. El argumento de Hume y su formalización no están desarrollados.",
  ["Hume, An Enquiry concerning Human Understanding, sec. X", "Earman, Hume's Abject Failure (2000)", "McGrew & McGrew, «The Argument from Miracles» (Blackwell Companion to Natural Theology, 2009)", "Tomás de Aquino, ST I q.105 a.6-8; SCG III.98-102", "Vaticano I, Dei Filius cap. 3", "Swinburne, The Resurrection of God Incarnate (2003)"],
  ["C-R09-01", "C-R09-04", "C-R09-05"], "R09", "R07", "R08", "8.000-10.000", False),
 ("D41", "resurreccion-hipotesis-rivales", "La Resurrección ante sus Rivales: | Alucinación, Visiones de Duelo y Leyenda",
  "historia", "pergamino", HIS, "Bart Ehrman, Gerd Lüdemann, Dale Allison (como crítico moderado), Paulogia",
  "Ninguna hipótesis naturalista explica conjuntamente la convicción de los discípulos, las apariciones a grupos y a adversarios (Santiago, Pablo), la tumba vacía y la forma «resurrección corporal» del anuncio. La resurrección es la mejor explicación; el argumento es abductivo y su fuerza depende de la plausibilidad previa del teísmo.",
  ["¿Qué explican y qué no explican las visiones de duelo?", "¿Existen alucinaciones colectivas documentadas?", "¿Qué valor tienen la tumba vacía y el testimonio de las mujeres?", "¿Cuál es la objeción más fuerte de Allison?"],
  "La resurrección aparece en 16 dossieres como premisa, pero no tiene investigación propia.",
  ["1 Cor 15:3-8; Mc 16:1-8; Mt 28; Lc 24; Jn 20-21", "Lüdemann, The Resurrection of Jesus (1994)", "Ehrman, How Jesus Became God (2014)", "Allison, The Resurrection of Jesus (2021)", "Wright, The Resurrection of the Son of God (2003)", "Loke, Investigating the Resurrection of Jesus Christ (Routledge 2020, acceso abierto)", "Rees, «The Hallucinations of Widowhood», BMJ (1971)"],
  ["C-R08-01", "C-R09-03", "C-R08-08", "C-R09-02"], "R08", "R09", "R07", "10.000-12.000", True),
 ("D42", "credo-1-corintios-15", "El Credo de 1 Corintios 15:3-8: | La Fuente Más Antigua del Cristianismo",
  "biblia", "pergamino", HIS, "Robert Price (tesis de la interpolación), miticismo, apologética musulmana que separa a Pablo de Jerusalén",
  "1 Cor 15:3-7 transmite una fórmula recibida por Pablo en los primeros años tras la crucifixión, de origen jerosolimitano; no es una interpolación, y su contenido (muerte, sepultura, resurrección al tercer día, apariciones) es el mismo que proclamaban Pedro y Santiago.",
  ["¿Qué indicios lingüísticos prueban el carácter tradicional?", "¿Dónde y cuándo la recibió Pablo (Gal 1:18)?", "¿Hasta dónde llega la fórmula primitiva?", "¿Es sostenible la tesis de la interpolación?"],
  "«Defensa del Apóstol Pablo» usa los credos como argumento. El análisis filológico e histórico de la fórmula no está hecho.",
  ["1 Cor 15:1-11; 11:23; Gal 1:11-2:10", "Conzelmann, 1 Corinthians (Hermeneia)", "Kloppenborg, CBQ 40 (1978)", "Price, «Apocryphal Apparitions», JHC 2 (1995)", "Hengel, «Das Begräbnis Jesu bei Paulus» (2001)", "Dunn, Jesus Remembered (2003), 854-857", "Bauckham, Jesus and the Eyewitnesses (2017)"],
  ["C-R08-09"], "R08", "R01", "R09", "7.000-9.000", False),
 ("D43", "miticismo-existio-jesus", "¿Existió Jesús?: | El Miticismo de Carrier ante las Fuentes",
  "historia", "pergamino", HIS, "Richard Carrier (On the Historicity of Jesus), Robert Price, Earl Doherty",
  "La hipótesis de un Cristo puramente celeste exige leer contra su sentido natural Gal 1:19; 4:4; Rom 1:3 y 1 Tes 2:14-15, descartar a Josefo y a Tácito y aplicar el teorema de Bayes con probabilidades previas arbitrarias. La existencia histórica de Jesús es la conclusión de prácticamente toda la investigación, creyente o no.",
  ["¿Cuál es el argumento bayesiano de Carrier y dónde se introducen los supuestos?", "¿Qué significa «hermano del Señor» y «nacido de mujer»?", "¿Qué valor tiene la clase de referencia Rank-Raglan?", "¿Qué queda de la Ascensión de Isaías como paralelo?"],
  "El miticismo solo se menciona una vez en toda la web.",
  ["Gal 1:19; 4:4; Rom 1:3; 1 Cor 9:5; 11:23-26; 1 Tes 2:14-16", "Tácito, Annales XV.44; Josefo, AJ XX.200", "Carrier, On the Historicity of Jesus (2014)", "Ehrman, Did Jesus Exist? (2012)", "Gullotta, «On Richard Carrier's Doubts», JSHJ 15 (2017)", "Casey, Jesus: Evidence and Argument or Mythicist Myths? (2014)"],
  ["C-R08-02"], "R09", "R10", "R07", "8.000-10.000", False),
 ("D44", "genealogias-jeconias", "Las Dos Genealogías y la Maldición de Jeconías: | ¿Puede Jesús Ser Hijo de David?",
  "biblia", "pergamino", HIS, "Tovia Singer (Outreach Judaism), Jews for Judaism; apologética musulmana de las contradicciones",
  "Las genealogías responden a propósitos distintos y son armonizables por vías conocidas desde Julio Africano; la filiación legal bastaba para la descendencia davídica; y la propia Escritura hebrea revoca el oráculo contra Jeconías (Hag 2:23). Ninguna armonización es demostrable: se muestra su posibilidad real.",
  ["¿Qué soluciones existen (levirato, línea legal y natural, línea de María) y cuál es más probable?", "¿Transmitía derechos la paternidad legal?", "¿Qué alcance tiene Jer 22:30 a la luz de Hag 2:23 y de la tradición rabínica?", "¿Qué objeta Singer a cada salida?"],
  "«100 Profecías» menciona las genealogías de pasada. No hay tratamiento de la objeción.",
  ["Mt 1:1-17; Lc 3:23-38; 1 Cr 3:10-19", "Jer 22:24-30; Hag 2:20-23", "Julio Africano, Carta a Arístides, ap. Eusebio, HE I.7", "Pesiqta de-Rav Kahana 24; Levítico Rabbah 19.6", "Brown, The Birth of the Messiah (1993)", "Johnson, The Purpose of the Biblical Genealogies (1988)"],
  ["C-R08-03"], "R08", "R01", "R06", "7.000-9.000", False),
 ("D45", "salmo-22-zacarias-12-traspasado", "El Mesías Traspasado: | Salmo 22:17 y Zacarías 12:10 ante la Contramisión Judía",
  "exegesis", "pergamino", HIS, "Tovia Singer, Rabbi Yisroel Blumenthal, Uri Yosef",
  "La lectura «como león» del texto masorético es gramaticalmente defectiva; la lectura verbal está atestiguada antes del cristianismo (LXX) y en el manuscrito de Naḥal Ḥever. En Zac 12:10, el texto hebreo más difícil («me mirarán a mí, a quien traspasaron») es el original. Ninguna de las dos lecturas es una invención cristiana.",
  ["¿Qué se lee exactamente en 5/6ḤevPs y con qué seguridad?", "¿Qué significa כארו y de qué raíz deriva?", "¿Cómo explica la contramisión la LXX?", "¿Qué dice la tradición rabínica de Zac 12:10 (Sukkah 52a)?"],
  "«100 Profecías» y «Dilema Mesiánico» citan el Sal 22 sin discutir el problema textual.",
  ["Sal 22:17 (TM, LXX 21:17, Áquila, Símaco, Peshitta)", "5/6ḤevPs (Naḥal Ḥever), DJD XXXVIII", "Zac 12:10 (TM, LXX); Jn 19:37; Ap 1:7", "b. Sukkah 52a; Midrash Tehillim 22", "Strawn, «Psalm 22:17b: More Guessing», JBL 119 (2000)", "Vall, «Psalm 22:17b: 'The Old Guess'», JBL 116 (1997)"],
  ["C-R08-05", "C-R08-07"], "R08", "R03", "R06", "8.000-10.000", False),
 ("D46", "isaias-7-14-almah", "Isaías 7:14: | ʿAlmâ, Parthenos y la Señal del Emmanuel",
  "exegesis", "pergamino", HIS, "Tovia Singer, Jews for Judaism; Bart Ehrman; apologética musulmana",
  "ʿAlmâ designa a una joven en edad núbil de la que se presume la virginidad; la traducción παρθένος es judía y precristiana; y el oráculo desborda su cumplimiento inmediato hacia el niño de Is 9 y 11. Mateo lee tipológicamente, no inventa.",
  ["¿Qué significan ʿalmâ y bətûlâ en todos sus usos bíblicos?", "¿Por qué tradujo así la LXX?", "¿Quién es el niño en el horizonte inmediato del capítulo?", "¿Es legítima la doble referencia?"],
  "Is 7:14 solo se menciona en cuatro dossieres; no tiene estudio propio.",
  ["Is 7:1-17; 8:1-10; 9:1-6; 11:1-9 (TM, 1QIsaª, LXX)", "Gn 24:43; Ex 2:8; Sal 68:26; Pr 30:19; Cant 1:3; 6:8", "Mt 1:18-25", "Justino, Dial. 43; 66-67; 84", "Ireneo, AH III.21", "Wildberger, Isaiah 1-12", "Rashi ad loc."],
  ["C-R08-06"], "R08", "R01", "R06", "7.000-9.000", False),
 ("D47", "p52-datacion-papiros", "P52 y los Límites de la Paleografía: | Qué Puede Probar la Datación de los Papiros",
  "biblia", "pergamino", HIS, "Brent Nongbri (crítica académica); MuslimProphets y otros sitios que usan la datación tardía",
  "La datación de P52 «hacia 125» fue siempre una estimación paleográfica con un margen amplio; el apologista no debe usarla como prueba puntual. Aun con la horquilla ampliada, el conjunto de papiros y la atestación patrística sitúan el cuarto evangelio en circulación dentro del siglo II temprano.",
  ["¿Cómo se fecha un papiro literario sin fecha y con qué margen?", "¿Qué argumentó Nongbri en 2005 y 2020?", "¿Qué otros testigos tempranos de Juan existen?", "¿Qué uso apologético es legítimo?"],
  "«Patrística NT» y «Autoría de los Evangelios» citan papiros, con algún error de datación señalado en la auditoría. El método paleográfico no está tratado.",
  ["P.Ryl. III 457 (John Rylands Library, imagen digital)", "Roberts, An Unpublished Fragment of the Fourth Gospel (1935)", "Nongbri, «The Use and Abuse of P52», HTR 98 (2005); NTS 66 (2020)", "Orsini & Clarysse, ETL 88 (2012)", "Nongbri, God's Library (2018)", "P.Egerton 2; P66; P75; P90"],
  ["C-R10-01", "C-R01-09"], "R01", "R10", "R08", "7.000-9.000", False),
 ("D48", "nombres-testigos-oculares", "Los Nombres de los Evangelios: | Onomástica, Estadística y Testigos Oculares",
  "historia", "pergamino", HIS, "Kamil Gregor y Brian Blais (crítica estadística a Bauckham), escepticismo académico",
  "La distribución de nombres personales de los evangelios concuerda con la de la Palestina judía del s. I según el corpus de Ilan. La crítica estadística de 2023 obliga a formular el argumento con más cautela, pero no elimina la convergencia: es un indicio de arraigo local, no una prueba de testimonio ocular.",
  ["¿Qué sostiene Bauckham y sobre qué datos?", "¿Qué objeción estadística plantean Gregor y Blais?", "¿Qué responden Van de Weghe y otros?", "¿Qué conclusión es defendible?"],
  "«Autoría de los Evangelios» defiende la autoría tradicional sin tratar el argumento onomástico ni su debate reciente.",
  ["Bauckham, Jesus and the Eyewitnesses (2ª ed. 2017), cap. 3-4", "Ilan, Lexicon of Jewish Names in Late Antiquity I (2002)", "Gregor & Blais, «Is Name Popularity a Good Test of Historicity?», JSHJ 21 (2023)", "Van de Weghe, réplica (2023-2024)", "arXiv:2403.14883"],
  ["C-R10-02"], "R10", "R01", "R08", "7.000-9.000", False),
 ("D49", "testimonium-flavianum", "El Testimonium Flavianum: | Josefo, Jesús y el Debate sobre la Autenticidad",
  "historia", "pergamino", HIS, "Ken Olson (tesis de la falsificación eusebiana), Richard Carrier, miticismo",
  "AJ XVIII.63-64 conserva un núcleo de Josefo; las frases confesionales admiten o una interpolación parcial o una lectura no cristiana del original, como muestran las versiones de Agapio y Miguel el Sirio y el estudio de Schmidt (2025). El pasaje de AJ XX.200 es independiente y no discutido seriamente.",
  ["¿Qué dice la tradición manuscrita griega, latina, árabe y siríaca?", "¿Es eusebiano el vocabulario (Olson)?", "¿Qué aporta la tesis de Schmidt?", "¿Qué puede afirmarse con seguridad?"],
  "«Crucifixión de Cristo» usa a Josefo como testigo. El debate sobre la autenticidad no está desarrollado.",
  ["Josefo, AJ XVIII.63-64; XX.200", "Orígenes, Contra Celsum I.47; Comm. in Matt. X.17", "Eusebio, HE I.11; Demonstratio III.5", "Agapio de Manbij, Kitāb al-ʿUnwān (Pines 1971)", "Whealey, Josephus on Jesus (2003)", "Olson, CBQ 61 (1999)", "Schmidt, Josephus and Jesus: New Evidence for the One Called Christ (OUP 2025, acceso abierto)"],
  ["DIR-10"], "R10", "R09", "R08", "8.000-10.000", False),
 ("D50", "iglesia-esclavitud", "La Iglesia y la Esclavitud: | Escritura, Magisterio e Historia ante la Acusación",
  "historia", "pergamino", FIL, "Crítica atea (Sam Harris, Dan Barker), John Noonan (tesis del cambio doctrinal), apologética musulmana comparada",
  "La Escritura regula y limita una institución universal sin instituirla, y contiene los principios que la hicieron insostenible. El Magisterio condenó la esclavización de pueblos desde 1435; también hubo concesiones y tolerancias (1452, 1866) que deben reconocerse y distinguirse de una enseñanza doctrinal.",
  ["¿Qué distinguían los teólogos entre servidumbre «justa» y esclavitud racial?", "¿Qué dicen Sicut dudum, Sublimis Deus e In supremo?", "¿Cómo se explican Dum diversas y la instrucción de 1866?", "¿Hubo cambio de doctrina (Noonan) o desarrollo?"],
  "La esclavitud no aparece en ningún dossier (0 menciones).",
  ["Ex 21; Lv 25:39-46; Dt 23:16-17; Flm; 1 Cor 7:21-23; Gal 3:28; 1 Tim 1:10", "Gregorio de Nisa, Hom. in Eccl. 4", "Eugenio IV, Sicut dudum (1435); Nicolás V, Dum diversas (1452)", "Pablo III, Sublimis Deus (1537); Gregorio XVI, In supremo (1839)", "Santo Oficio, Instrucción de 20 de junio de 1866", "Gaudium et spes 27; Veritatis splendor 80", "Noonan, A Church That Can and Cannot Change (2005)", "Panzer, The Popes and Slavery (1996)"],
  ["DIR-11"], "R09", "R05", "R07", "9.000-11.000", False),
]

# Candidatos propios del director (origen DIR). Los 11 primeros se seleccionan; el resto se registran y descartan.
DIR = [
 ("DIR-01", "Los versos satánicos (gharānīq) en las fuentes islámicas tempranas", ISL, "Laguna total en la web; fuentes primarias abundantes; monografía de Shahab Ahmed (2017)."),
 ("DIR-02", "Satisfacción vicaria frente a la objeción islámica y sociniana de injusticia", ISL, "La web critica el Corán pero no expone la soteriología católica frente a la objeción más repetida."),
 ("DIR-03", "Naskh: abrogación y versículos perdidos (lapidación, lactancia)", ISL, "Laguna; fuentes canónicas explícitas."),
 ("DIR-04", "Juan Damasceno, De haeresibus 100: primera refutación cristiana del islam", ISL, "Fuente primaria de primer orden nunca estudiada en la web."),
 ("DIR-05", "Dhū l-Qarnayn y la Leyenda siríaca de Alejandro", ISL, "Se fusiona con C-R10-04 en D14."),
 ("DIR-06", "El episcopado monárquico en Roma y la tesis de Lampe", PRO, "Objeción académica más fuerte al papado; ausente en la web y en los informes."),
 ("DIR-07", "Los «hermanos de Jesús» y la virginidad perpetua", PRO, "Dogma mariano sin dossier; debate exegético serio (Meier, Bauckham)."),
 ("DIR-08", "El nombre «Jehová» en el NT de la Traducción del Nuevo Mundo", RES, "Tema documental (papiros de la LXX) más sólido que Jn 1:1, ya cubierto."),
 ("DIR-09", "La «Gran Apostasía» como presupuesto restauracionista", RES, "Ataca la raíz común de SUD, TJ y adventistas."),
 ("DIR-10", "El Testimonium Flavianum tras Schmidt (2025)", HIS, "Novedad académica reciente en acceso abierto."),
 ("DIR-11", "La Iglesia y la esclavitud", FIL, "Objeción atea muy extendida; laguna total; exige reconocer dificultades reales."),
 ("DIR-12", "El caso Galileo", FIL, "DESCARTADO: bien cubierto en la apologética en español; menor originalidad relativa."),
 ("DIR-13", "La Sábana Santa de Turín", HIS, "DESCARTADO: el estado de la evidencia no permite conclusiones firmes; alto riesgo de sobreafirmar."),
 ("DIR-14", "Los milagros de Mahoma: Corán frente a sīra", ISL, "DESCARTADO: solapamiento con «Muhammad ibn Abdallah» y con D06."),
 ("DIR-15", "El «dilema islámico» (Q 5:47, 5:68, 10:94)", ISL, "DESCARTADO como dossier propio: ya desarrollado en «Josías» y «Jeremías 8:8»; su estado actual se integra en D07 y D08."),
 ("DIR-16", "El argumento kalām y el pasado infinito", FIL, "DESCARTADO: Tomás niega que el comienzo temporal sea demostrable; se prioriza el argumento de la contingencia (D38)."),
 ("DIR-17", "El filioque en los Padres griegos (Blachernae, Lyon II)", ORT, "DESCARTADO: «Concilio de Florencia» ya desarrolla el filioque; riesgo de duplicidad."),
 ("DIR-18", "Las indulgencias y el tesoro de méritos", PRO, "DESCARTADO en esta tanda: «De Purgatorio» y «Trento» cubren parte; queda como reserva."),
 ("DIR-19", "Daniel 9 y las setenta semanas ante la contramisión judía", HIS, "DESCARTADO: «Daniel y el Quinto Reino» ya desarrolla Dn 9."),
 ("DIR-20", "El censo de Quirinio (Lc 2:1-2)", HIS, "RESERVA: buen tema, sin sitio en los 50."),
]

MOTIVOS = {  # decisiones explicitas sobre candidatos de investigadores no seleccionados
 "C-R02-02": "Riesgo alto de duplicidad con «Tawhid y Omnipotencia» y «El Espejo Vacío».",
 "C-R02-05": "Tema menor; cabe como objeción dentro de D09.",
 "C-R02-07": "Demasiado especializado y con pocas fuentes accesibles.",
 "C-R02-12": "Riesgo alto de duplicidad con los dossieres tomistas existentes.",
 "C-R04-09": "Reserva (indulgencias): cobertura parcial en «De Purgatorio» y «Trento».",
 "C-R04-10": "Riesgo alto de duplicidad con «La Salvación Católica» y «Trento».",
 "C-R05-04": "Riesgo de duplicidad con «Concilio de Florencia» (filioque).",
 "C-R05-06": "Reserva (órdenes anglicanas): interlocutor minoritario en el ámbito hispano.",
 "C-R05-09": "Riesgo alto de duplicidad con «La Inmaculada Concepción» y «De Assumptione».",
 "C-R05-10": "Riesgo alto de duplicidad con «De Purgatorio».",
 "C-R05-11": "Interlocutor luterano confesional; menor relevancia relativa.",
 "C-R06-01": "Riesgo alto de duplicidad: el dossier «Juan 11» trata en realidad Jn 1:1 y la lectura «un dios».",
 "C-R06-05": "Reserva (ADN y Libro de Mormón): se prioriza D30 como test empírico del mormonismo.",
 "C-R06-09": "Riesgo alto de duplicidad con «Mateo 28:19 - Autenticidad».",
 "C-R06-10": "Interlocutor adventista; relevancia menor. Se integra en D33.",
 "C-R06-11": "Fuentes insuficientes.",
 "C-R07-05": "Kalām: se prioriza el argumento de la contingencia (D38), más coherente con la orientación tomista.",
 "C-R07-06": "Ídem.",
 "C-R07-07": "Reserva (argumento evolutivo contra el naturalismo).",
 "C-R07-09": "Riesgo de duplicidad con los dossieres sobre simplicidad divina.",
 "C-R08-04": "Reserva (censo de Quirinio).",
 "C-R08-10": "Riesgo alto de duplicidad con «Marcos 13:32» y «El Apocalipsis Católico».",
 "C-R08-11": "Riesgo de duplicidad con «Daniel y el Quinto Reino».",
 "C-R08-12": "Tema menor; cabe en D45.",
 "C-R09-07": "Riesgo medio-alto de duplicidad; tema muy técnico de cronología.",
 "C-R09-06": "Cercano a «El Señor del Sábado - Marcos 2:28».",
 "C-R09-08": "Riesgo alto de duplicidad con «Autoría de los Evangelios».",
 "C-R09-10": "Cubierto por «100 Contradicciones Bíblicas Resueltas».",
 "C-R09-11": "Riesgo medio-alto de duplicidad con «Autoría de los Evangelios».",
 "C-R09-12": "Evidencia de difícil verificación; riesgo de sobreafirmar.",
 "C-R09-13": "Riesgo alto de duplicidad con los dossieres de divinidad de Cristo.",
 "C-R10-05": "Riesgo alto de duplicidad con «Credo Divino Prepaulino» y «Dos Poderes en el Cielo».",
 "C-R01-08": "No se halló uso rival real del versículo; no responde a una controversia viva.",
}


def load(p, default):
    try:
        return json.load(open(p, encoding="utf-8"))
    except Exception:
        return default


def main():
    tc_path = os.path.join(PROY, "TOPIC_CANDIDATES.json")
    tc = load(tc_path, {"candidatos": []})
    cands = [c for c in tc["candidatos"] if c.get("origen") != "DIR"]
    for cid, titulo, area, nota in DIR:
        cands.append({"id": cid, "origen": "DIR", "titulo_provisional": titulo, "interlocutor": area, "nota_director": nota, "estado": "CANDIDATO"})
    byid = {c["id"]: c for c in cands}
    usado = {}
    for d in D:
        for cid in d[11]:
            assert cid in byid, f"candidato inexistente {cid} en {d[0]}"
            usado.setdefault(cid, d[0])
    for c in cands:
        if c["id"] in usado:
            c["estado"] = "SELECCIONADO"
            c["dossier"] = usado[c["id"]]
            c["decision_editorial"] = f"Integrado en {usado[c['id']]}."
        else:
            c["estado"] = "DESCARTADO"
            c["decision_editorial"] = MOTIVOS.get(c["id"]) or c.get("nota_director") or "No seleccionado: puntuación relativa inferior o solapamiento con un tema seleccionado."
    json.dump({"total": len(cands), "seleccionados": len(usado), "candidatos": cands}, open(tc_path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

    reg_path = os.path.join(PROY, "DOSSIER_REGISTRY.json")
    prev = {x["id"]: x for x in load(reg_path, {"dossieres": []}).get("dossieres", [])}
    reg, tasks = [], {r: {"perfil": p, "responsable_de": [], "revision_documental_de": [], "revision_adversarial_de": []} for r, p in PERFILES.items()}
    for (did, slug, titulo, apartado, paleta, area, adversario, tesis, preguntas, originalidad, fuentes, cids, resp, rdoc, radv, ext, piloto) in D:
        assert len({resp, rdoc, radv}) == 3, did
        urls = []
        for cid in cids:
            for u in byid[cid].get("articulos_rivales_que_lo_motivan", []) or []:
                if u not in urls:
                    urls.append(u)
        e = {"id": did, "slug": slug, "titulo": titulo, "apartado": apartado, "paleta": paleta, "area": area,
             "adversario_principal": adversario, "tesis": tesis, "preguntas_de_investigacion": preguntas,
             "justificacion_de_originalidad": originalidad, "fuentes_preliminares_del_director": fuentes,
             "articulos_rivales_de_partida": urls, "candidatos_origen": cids,
             "responsable": resp, "revisor_documental": rdoc, "revisor_adversarial": radv,
             "extension_prevista_palabras": ext, "piloto": piloto,
             "estado": prev.get(did, {}).get("estado", "APROBADO"), "carpeta": f"dossieres/{did}-{slug}"}
        for k, v in prev.get(did, {}).items():  # conservar lo añadido despues (notas, html, estadisticas...)
            e.setdefault(k, v)
        reg.append(e)
        tasks[resp]["responsable_de"].append(did)
        tasks[rdoc]["revision_documental_de"].append(did)
        tasks[radv]["revision_adversarial_de"].append(did)
        folder = os.path.join(PROY, "dossieres", f"{did}-{slug}")
        os.makedirs(folder, exist_ok=True)
        exp = dict(e)
        exp["nota"] = ("Las fuentes preliminares son pistas del director (clase F): hay que abrirlas y verificarlas. "
                       "Los artículos rivales de partida proceden de la exploración de Fase 1 (ver ARTICLE_REFUTATION_REGISTRY.json).")
        json.dump(exp, open(os.path.join(folder, "expediente.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    assert len(reg) == 50 and len({x["slug"] for x in reg}) == 50
    json.dump({"total": len(reg), "fecha_seleccion": "2026-11-14", "dossieres": reg}, open(reg_path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    json.dump({"modelo": "haiku (Claude Haiku 5.5)", "esfuerzo": "high", "investigadores": tasks}, open(os.path.join(PROY, "RESEARCH_TASKS.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)

    # documento de seleccion
    L = ["# Selección temática — los 50 dossieres nuevos", "",
         "> Decisión editorial del director (Fable 5.2), 2026-11-14. Datos completos en `DOSSIER_REGISTRY.json`; candidatos y motivos de descarte en `TOPIC_CANDIDATES.json`.", "",
         f"**Candidatos evaluados:** {len(cands)} ({len(cands) - len(DIR)} de los diez investigadores tras leer 156 artículos de 102 sitios; {len(DIR)} del director a partir de las lagunas del mapa temático). "
         f"**Integrados en los 50:** {len(usado)}. **Descartados o en reserva:** {len(cands) - len(usado)}.", "",
         "## Criterios", "",
         "1. **No duplicar**: cada tema se contrastó con `EXISTING_TOPIC_MAP.json` (tesis, cuestiones y argumentos de los 102 dossieres leídos íntegramente). Se descartó todo candidato con riesgo alto.",
         "2. **Cubrir lagunas reales**: la web tenía 37 dossieres sobre el islam, pero ninguno sobre papado, resurrección, problema del mal, mormonismo o Testigos de Jehová.",
         "3. **Responder a publicaciones rivales reales** localizadas en la Fase 1, priorizando las más sofisticadas.",
         "4. **Disponibilidad de fuentes primarias verificables** y de bibliografía académica.",
         "5. **Fusionar** candidatos que comparten controversia en vez de multiplicar dossieres casi iguales.", "",
         "## Distribución", ""]
    from collections import Counter
    cnt = Counter(x["area"] for x in reg)
    L += ["| Área | Dossieres |", "|---|---|"] + [f"| {a} | {n} |" for a, n in cnt.most_common()] + [""]
    L += ["## Los 50 temas", ""]
    area = None
    for x in reg:
        if x["area"] != area:
            area = x["area"]
            L += [f"### {area}", ""]
        L += [f"**{x['id']} — {x['titulo'].replace(' | ', ' ')}**" + ("  *(piloto)*" if x["piloto"] else ""),
              f"- Apartado: `{x['apartado']}` · Responsable {x['responsable']} · Rev. documental {x['revisor_documental']} · Rev. adversarial {x['revisor_adversarial']} · {x['extension_prevista_palabras']} palabras",
              f"- Adversario: {x['adversario_principal']}",
              f"- Tesis: {x['tesis']}",
              f"- Por qué no es duplicidad: {x['justificacion_de_originalidad']}", ""]
    L += ["## Equipo", "", "| Investigador | Perfil | Responsable de | Revisa (documental) | Revisa (adversarial) |", "|---|---|---|---|---|"]
    for r, t in tasks.items():
        L.append(f"| {r} | {t['perfil']} | {', '.join(t['responsable_de'])} | {', '.join(t['revision_documental_de'])} | {', '.join(t['revision_adversarial_de'])} |")
    L += ["", "## Candidatos no seleccionados (con motivo)", ""]
    for c in cands:
        if c["estado"] == "DESCARTADO":
            L.append(f"- `{c['id']}` {c['titulo_provisional']} — {c['decision_editorial']}")
    open(os.path.join(PROY, "SELECCION_TEMATICA.md"), "w", encoding="utf-8").write("\n".join(L) + "\n")
    print(f"50 dossieres registrados; candidatos: {len(cands)} (seleccionados {len(usado)}).")
    for r, t in tasks.items():
        print(r, len(t["responsable_de"]), len(t["revision_documental_de"]), len(t["revision_adversarial_de"]))
    print(dict(cnt))


if __name__ == "__main__":
    main()
