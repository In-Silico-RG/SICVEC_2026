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
}, {
    # Wilson Castro: title, abstract and bio verbatim from his acceptance email (insilico@, 2026-09-21). Colon in the title
    # added by us; his text has none. Affiliation in his own words. Photo: inline image in his email (10_Ponentes/Foto Castro.png).
    "name": "Dr. Wilson Manuel Castro Silupu",
    "role": "Conferencista magistral",
    "affiliation": "Profesor Principal y Docente Investigador, Universidad Nacional de Frontera (UNF), Perú. Investigador "
                   "Distinguido reconocido por el CONCYTEC y miembro senior del IEEE",
    "photo": "speaker_castro.jpg",
    "talk": "Medicinal plant discrimination: A study of deep learning techniques and a novel approach for data augmentation",
    "format": "Virtual",
    "bio": [
        "El Dr. Wilson Manuel Castro Silupu es Profesor Principal y Docente Investigador en la Universidad Nacional de "
        "Frontera, Investigador Distinguido reconocido por el CONCYTEC y miembro senior del IEEE, distinción que consolida su "
        "posicionamiento en comunidades científicas internacionales. Obtuvo el grado de Doctor en Ciencia, Tecnología y "
        "Gestión Alimentaria y la Maestría en Ciencia e Ingeniería de los Alimentos en la Universidad Politécnica de "
        "Valencia. Asimismo, en su proceso de continuo perfeccionamiento ha realizado estancias de investigación en "
        "instituciones internacionales de Europa y América Latina, fortaleciendo colaboraciones científicas y promoviendo "
        "la difusión de avances científicos en revistas indexadas de alto impacto.",
        "Su producción científica se enfoca en la intersección entre Food Science, Agroindustrial Systems y Emerging "
        "Technologies, con especial énfasis en Precision Agriculture, Hyperspectral Imaging, Machine Learning, Remote "
        "Sensing, Spectroscopy y Data-Driven Modeling aplicados a la calidad, autenticidad e inocuidad de alimentos. Su "
        "trabajo contribuye al desarrollo de metodologías no destructivas, sistemas inteligentes de monitoreo y "
        "herramientas analíticas para la optimización de cadenas agroalimentarias sostenibles, totalizando más de setenta "
        "artículos científicos en Scopus y Web of Science. Participa activamente en proyectos financiados mediante fondos "
        "competitivos (FINCyT, PROCIENCIA, PNIA), consolidando redes de investigación y transferencia tecnológica, y la "
        "generación de conocimiento de alto impacto, promoviendo la interdisciplinariedad, la colaboración internacional "
        "y la publicación en revistas indexadas de alto impacto.",
    ],
    "abstract": [
        "Medicinal plants in remote mountain ecosystems are threatened, requiring accurate identification for conservation "
        "and sustainable management. However, traditional methods require specialized expertise, and ground surveys in "
        "Peru's Paramos and cloud forests are logistically challenging. This study develops and validates a methodology "
        "for discriminating six medicinal plant species using RGB images acquired from UAV and deep learning. Individual "
        "plants from six species of medicinal plants were identified and georeferenced; from these, aerial RGB images "
        "were acquired at 3 to 5 m altitude. The rectangular ROIs of each image were extracted using the Segment Anything "
        "model (SAM), which constituted our image database. Then the image database was augmented through two methods "
        "(a) Geometric transformation and (b) a proposal called “Cartesian subsampling”. Finally, five CNN "
        "architectures for classifying tasks were trained, validated, and their results statistically compared.",
        "Geometric transformation yielded higher overall accuracy, with MobileNetV2 achieving 97.86% and ResNet-50 "
        "97.66%, while models trained from scratch performed lower (AlexNet-Deep: 90.14%, PhytoNet: 81.11%). Cartesian "
        "subsampling showed advantages when geometric invariance was critical for transfer-learning models. Confusion "
        "persisted between species of Myrcianthes that were morphologically similar, with F1 scores ranging from 0.76 to "
        "0.97. Classification precisions from 81% to 97% were achieved, with geometric transformation outperforming "
        "Cartesian methods in all models. ResNet-50 offers the best balance of accuracy, computational efficiency, and "
        "training stability for practical conservation applications in remote mountain ecosystems.",
    ],
}, {
    # Marianny Combariza: accepted 2026-09-21 (insilico@), one line, no material yet. Affiliation as written in our
    # invitation letter (AC). Title, bio, abstract and photo: pending; the page shows "por confirmar".
    "name": "Dra. Marianny Y. Combariza",
    "role": "Conferencista magistral",
    "affiliation": "Investigadora, Centro de Estudios e Investigaciones Ambientales (CEIAM), Universidad Industrial de "
                   "Santander (UIS), Bucaramanga, Colombia",
    "photo": None,
    "talk": None,
    "format": "Virtual",
    "bio": [],
    "abstract": [],
}]

# Footer. Source: proposal section 8.2 and CLAUDE.md/FICHA (roles). No personal emails or phones on the public page.
COORDINADORES = [
    ("Aldo F. Combariza", "Coordinación General"),
    ("María Ximena Díaz", "Coordinación Académica"),
    ("Sebastián Vargas", "Coordinación Logística"),
    ("Selena Arias Avila", "Coordinación Administrativa"),
]
DEPARTAMENTOS = [
    "Departamento de Biología y Química",
    "Departamento de Ingeniería Agroindustrial",
    "Departamento de Ingeniería Agrícola",
    "Departamento de Física",
]

EMAIL_COORDINACION = "insilico@unisucre.edu.co"   # AC, 2026-09-19: the coordinators' contact email
