"""Public event-page content. Sources: 01_Propuesta (sections 3-7), 10_Ponentes/FICHA_Escobar.md and her bio/abstract files.
Nothing here is invented; items still undecided are marked PENDIENTE in the templates."""

OBJETIVO_GENERAL = ("Crear un espacio de diálogo y producción de conocimiento sobre ciencia verde y economía circular "
                    "que fortalezca capacidades de investigadores, estudiantes y profesionales en América Latina.")

OBJETIVOS = [
    "Difundir investigaciones de vanguardia en procesos sostenibles, biotecnología verde y economía circular.",
    "Facilitar networking entre académicos, empresarios e innovadores verdes de Colombia y la región de América Latina.",
    "Identificar oportunidades de colaboración interinstitucional para proyectos de investigación aplicada.",
    "Fomentar la formación de capacidades en estudiantes de pregrado y posgrado en sostenibilidad e innovación verde.",
    "Documentar el estado del arte en ciencia verde en la región para futuros impactos de política pública.",
]

# Same order and names as logic.AXES.
EJES_TOPICOS = [
    "Transición de modelos lineales a circulares, diseño para la circularidad, valorización de residuos, economía de "
    "cascada, simbiosis industrial, análisis de ciclo de vida.",
    "Síntesis verde, solventes y reactivos sostenibles, biocatálisis y catálisis, procesos limpios, diseño molecular para "
    "minimizar residuos, química farmacéutica sostenible, transformaciones eficientes, reducción de toxicidad, "
    "tecnologías de síntesis avanzadas (flujo continuo, microondas, ultrasonido), valorización de biomasa.",
    "Bioproductos, fermentación microbiana, enzimas verdes, biorrefinerías, bioplásticos, bioetanol, biofertilizantes, "
    "enzimas industriales de fuente biológica.",
    "Energías limpias, tratamiento de aguas, remediación ambiental, tecnologías de captura de CO₂, fotosíntesis "
    "artificial, energía solar y eólica en industria alimentaria.",
    "Certificaciones verdes, huella de carbono, producción más limpia, innovación en agroindustria, agricultura "
    "sostenible, trazabilidad, cadenas cortas.",
    "ODS 2030, marcos regulatorios para economía circular, incentivos verdes, responsabilidad social empresarial, "
    "educación ambiental, gobiernos locales verdes.",
]

ODS = [
    ("12", "Producción y consumo responsables", "Economía circular, valorización de residuos, procesos más limpios."),
    ("13", "Acción por el clima", "Tecnologías verdes, reducción de emisiones de carbono, sostenibilidad ambiental."),
    ("15", "Vida de ecosistemas terrestres", "Biodiversidad, procesos agroindustriales sostenibles, transición verde."),
    ("17", "Alianzas para lograr los objetivos", "Colaboración académica, transferencia de tecnología, redes entre instituciones."),
]

# Preliminary structure from the formal proposal (section 6.4). The final programme is not decided yet.
PROGRAMA = [
    ("Lunes 19 de octubre", [
        ("08:00–09:00", "Inauguración oficial + conferencia magistral"),
        ("09:00–10:30", "Ponencias · Eje 1: Economía Circular"),
        ("10:30–10:45", "Receso (café)"),
        ("10:45–12:15", "Ponencias · Eje 2: Química Verde y Procesos Sostenibles"),
        ("12:15–13:45", "Almuerzo"),
        ("13:45–15:15", "Ponencias · Eje 3: Biotecnología Sostenible"),
        ("15:15–15:30", "Receso (café)"),
        ("15:30–17:00", "Ponencias · Eje 4: Tecnologías Verdes y Energías Renovables"),
        ("17:00–18:00", "Pósteres + networking (Expo verde)"),
    ]),
    ("Martes 20 de octubre", [
        ("08:30–09:30", "Conferencia magistral 2"),
        ("09:30–11:00", "Ponencias · Eje 5: Sostenibilidad en Cadenas de Suministro"),
        ("11:00–11:15", "Receso (café)"),
        ("11:15–12:45", "Ponencias · Eje 6: Política Pública y Gobernanza Ambiental"),
        ("12:45–14:15", "Almuerzo"),
        ("14:15–15:45", "Ponencias (continuación) + sesión de preguntas"),
        ("15:45–16:45", "Mesa redonda: lecciones y desafíos"),
        ("16:45–17:15", "Clausura, reconocimientos y networking final"),
    ]),
]

PUBLICO = [
    "Investigadores en química, física, matemáticas, biología, ciencias ambientales y todas las ingenierías.",
    "Estudiantes de pregrado y posgrado en ciencias básicas e ingenierías.",
    "Docentes de ciencias e ingeniería interesados en sostenibilidad y economía circular.",
    "Profesionales de las industrias alimentaria, química, energética, agrícola, de materiales y de servicios ambientales.",
    "Emprendedores con iniciativas de innovación verde, gestores ambientales y consultores.",
    "Tomadores de decisión del sector público y organizaciones de la sociedad civil.",
]

# Talk title and abstract: verbatim from her files (10_Ponentes). Bio: her own sentences, abridged (paragraphs 1-2 verbatim,
# paragraph 3 = two sentences from the rest of her bio).
SPEAKERS = [{
    "name": "Dra. Beatriz Escobar Morales",
    "role": "Conferencista magistral",
    "affiliation": "Investigadora por México–SECIHTI, Unidad de Energía Renovable, Centro de Investigación Científica de "
                   "Yucatán (CICY), Mérida, México",
    "photo": "speaker_escobar.jpg",
    "talk": "Transformación sostenible del sargazo holopelágico en materiales funcionales avanzados",
    "format": "Virtual",
    "bio": [
        "Investigadora por México–SECIHTI, adscrita a la Unidad de Energía Renovable del Centro de Investigación Científica "
        "de Yucatán (CICY). Es Doctora y Maestra en Energía por el Instituto de Energías Renovables de la Universidad "
        "Nacional Autónoma de México (UNAM) y Licenciada en Física por la Universidad Juárez Autónoma de Tabasco. Es "
        "miembro del Sistema Nacional de Investigadoras e Investigadores (SNII), Nivel II.",
        "Su línea de investigación se centra en el desarrollo de materiales funcionales para tecnologías energéticas, "
        "particularmente biocarbones, materiales de carbono y nanopartículas metálicas obtenidos a partir de biomasa. Sus "
        "investigaciones incorporan principios de química verde, valorización integral y economía circular para el "
        "desarrollo de electrocatalizadores y materiales destinados a celdas de combustible, producción de hidrógeno y "
        "sistemas de conversión y almacenamiento de energía. En los últimos años, ha impulsado particularmente el "
        "aprovechamiento sostenible del sargazo holopelágico como precursor de materiales funcionales de alto valor agregado.",
        "Actualmente es Presidenta de la Sociedad Mexicana del Hidrógeno para el periodo 2026–2028. En 2017 recibió el "
        "Premio Estatal de Ciencia, Tecnología e Innovación, en la categoría de Investigación Científica y Tecnológica.",
    ],
    "abstract": [
        "Las arribazones masivas de sargazo holopelágico en el Caribe Mexicano representan un desafío ambiental, social y "
        "económico debido a los grandes volúmenes de biomasa acumulada en las zonas costeras y a los impactos asociados con "
        "su descomposición y manejo. Sin embargo, su composición química y disponibilidad también ofrecen una oportunidad "
        "para replantear esta biomasa desde una perspectiva de economía circular, transitando de su consideración como "
        "residuo hacia su aprovechamiento como materia prima renovable para la obtención de productos y materiales de valor "
        "agregado.",
        "En esta conferencia se presentarán diferentes estrategias desarrolladas para la valorización integral del sargazo "
        "mediante principios de química verde, considerando rutas complementarias de transformación. Una de ellas comprende "
        "la conversión termoquímica de la biomasa en biocarbones porosos, seguida de procesos de activación y modificación "
        "superficial mediante heteroátomos, con el propósito de obtener materiales carbonosos funcionales con elevada área "
        "superficial y propiedades adecuadas para aplicaciones electroquímicas. Los resultados muestran que es posible "
        "obtener biocarbones derivados de sargazo con áreas superficiales superiores a 2000 m² g⁻¹, así como materiales "
        "dopados con nitrógeno o azufre, ampliando sus posibilidades de aplicación como electrocatalizadores y soportes "
        "catalíticos.",
        "De manera complementaria, los extractos de sargazo constituyen una plataforma para la síntesis verde de "
        "nanopartículas metálicas, aprovechando los compuestos bioactivos naturalmente presentes en la biomasa como agentes "
        "involucrados en los procesos de reducción y estabilización. Esta estrategia permite disminuir la dependencia de "
        "reactivos convencionales y ejemplifica cómo distintas fracciones de una misma biomasa pueden incorporarse en rutas "
        "de aprovechamiento complementarias. Los materiales obtenidos pueden posteriormente integrarse con biocarbones "
        "derivados del propio sargazo para desarrollar sistemas funcionales y electrocatalizadores.",
        "Estas rutas presentan un concepto de valorización integral, en el que el sargazo puede transformarse en biocarbones, "
        "materiales dopados, nanopartículas y sistemas híbridos con potencial en tecnologías energéticas y ambientales, "
        "incluyendo celdas de combustible, electroreducción de CO₂ y procesos catalíticos. Así, la convergencia entre "
        "química verde, ciencia de materiales y economía circular ofrece una estrategia para transformar una problemática "
        "costera en una oportunidad científica y tecnológica, promoviendo el desarrollo de procesos más sostenibles y "
        "nuevas cadenas de valor a partir de un recurso marino disponible regionalmente.",
    ],
}]
