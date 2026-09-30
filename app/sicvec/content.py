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

# Programme from the organizers' sheet (08_Cronograma/Programacion SICVEC - Copia de Hoja 1 (1).pdf, AC 2026-09-30).
# Talk titles of the keynotes as sent by the speakers; empty talk slots are filled after peer review.
PROGRAMA = [
    ('Lunes 19 de octubre', [
        ('07:45–08:15', 'Inscripción y registro de participantes'),
        ('08:15–08:30', 'Acto de apertura e instalación del SICVEC 2026'),
        ('08:30–09:30', 'Conferencia magistral 1 · Dra. Beatriz Escobar Morales, Centro de Investigación Científica de Yucatán (CICY), Mérida, México · «Transformación sostenible del sargazo holopelágico en materiales funcionales avanzados»'),
        ('09:30–09:55', 'Ponencia 1 (por asignar)'),
        ('09:55–10:20', 'Ponencia 2 (por asignar)'),
        ('10:20–10:40', 'Receso (café)'),
        ('10:40–11:05', 'Ponencia 3 (por asignar)'),
        ('11:05–11:30', 'Ponencia 4 (por asignar)'),
        ('11:30–11:55', 'Ponencia 5 · Gobernación de Sucre, Sincelejo, Colombia'),
        ('11:55–12:20', 'Ponencia 6 (por asignar)'),
        ('12:20–14:00', 'Almuerzo libre'),
        ('14:00–15:00', 'Conferencia magistral 2 · Dr. Wilson Manuel Castro Silupu, Universidad Nacional de Frontera, Perú · «Medicinal plant discrimination: A study of deep learning techniques and a novel approach for data augmentation»'),
        ('15:00–15:25', 'Ponencia 7 · Dr. Pedro Meza Catellar, Universidad de San Buenaventura, Cartagena de Indias, Colombia'),
        ('15:25–15:50', 'Ponencia 8 (por asignar)'),
        ('15:50–16:10', 'Receso (café)'),
        ('16:10–17:30', 'Sesión de pósteres + networking'),
    ]),
    ('Martes 20 de octubre', [
        ('08:00–08:30', 'Inscripción y registro de participantes'),
        ('08:30–09:00', 'Ponencia 9 · Esp. Carlos Meza Bertel, Parque Comercial Guacarí, Sincelejo, Colombia'),
        ('09:00–10:00', 'Conferencia magistral 3 · Prof. Enrico Valli, Università di Bologna, Bolonia, Italia · «Valorization of by-products from olive oil production as a source of bioactive compounds»'),
        ('10:00–10:25', 'Ponencia 10 · Dra. Laura Hil Pastor, Universidad de Sucre, Sincelejo, Colombia'),
        ('10:25–10:50', 'Receso (café)'),
        ('10:50–11:15', 'Ponencia 11 · Est. Mg. Guillermo Alejandro Corrales, Universidad Santo Tomás, Bogotá, Colombia · «Efecto de la producción de metano durante la codigestión anaeróbica de estiércol de bovino, residuos de maíz y lenteja de agua (Lemna sp.)»'),
        ('11:15–11:20', 'Espacio publicitario'),
        ('11:20–12:20', 'Conferencia magistral 4 · Dra. Monique Renon Eller, Universidade Federal de Viçosa, Viçosa, Brasil'),
        ('12:20–14:00', 'Almuerzo libre'),
        ('14:00–14:25', 'Ponencia 12 (por asignar)'),
        ('14:25–14:50', 'Ponencia 13 (por asignar)'),
        ('14:50–15:15', 'Ponencia 14 (por asignar)'),
        ('15:15–15:35', 'Receso (café)'),
        ('15:35–16:35', 'Conferencia magistral 5 · Dra. Marianny Y. Combariza, Universidad Industrial de Santander, Bucaramanga, Colombia'),
        ('16:35–17:00', 'Acto de clausura: reconocimiento a los mejores pósteres y cierre del evento'),
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

# Order on the speakers page: Valli first (AC, 2026-09-30).
SPEAKERS = [{
    # Enrico Valli: accepted by email, 2026-09-29 (aldo.combariza@). Affiliation, title and bio verbatim from that email
    # (bio in English, his words). Photo: attachment of that email (10_Ponentes/Foto Valli.jpg). Abstract pending.
    "name": "Prof. Enrico Valli",
    "role": "Conferencista magistral",
    "affiliation": "Department of Agricultural and Food Sciences and Interdepartmental Centre for Industrial Agrofood "
                   "Research, Alma Mater Studiorum – Università di Bologna, Italia",
    "photo": "speaker_valli.jpg",
    "talk": "Valorization of by-products from olive oil production as a source of bioactive compounds",
    "format": "Virtual",
    # Slot confirmed: Tuesday 20 Oct 09:00-10:00 COT (his emails of 29-30 Sept; AC chose 09:00, 2026-09-30).
    "when": {"es": "Martes 20 de octubre, 9:00–10:00 (hora de Colombia, UTC−5)",
             "en": "Tuesday 20 October, 9:00–10:00 (Colombia time, UTC−5)",
             "pt": "Terça-feira, 20 de outubro, 9:00–10:00 (horário da Colômbia, UTC−5)"},
    "bio": [
        "Associate professor in the Department of Agricultural and Food Sciences at the University of Bologna since 2022, "
        "performing research in the field of instrumental and sensory analysis of foods and sustainable food technologies. "
        "Main interests lie in the analytical methods for assessing the quality and authenticity of olive oil and the "
        "technological valorization of agri-food by-products. He has been involved - and is currently part - of research "
        "teams in several national and EU research projects. He is the delegate for orientation for the DISTAL bachelor's "
        "and master's degree courses held in Cesena.",
    ],
    "abstract": [],
}, {
    # Talk title and abstract: verbatim from her files (10_Ponentes). Bio: her own sentences, abridged (paragraphs 1-2 verbatim,
    # paragraph 3 = two sentences from the rest of her bio).
    "name": "Dra. Beatriz Escobar Morales",
    "role": "Conferencista magistral",
    "affiliation": "Investigadora por México–SECIHTI, Unidad de Energía Renovable, Centro de Investigación Científica de "
                   "Yucatán (CICY), Mérida, México",
    "photo": "speaker_escobar.jpg",
    "talk": "Transformación sostenible del sargazo holopelágico en materiales funcionales avanzados",
    "format": "Virtual",
    # Slot: organizers' programme sheet, AC 2026-09-30.
    "when": {"es": "Lunes 19 de octubre, 8:30–9:30 (hora de Colombia, UTC−5)",
             "en": "Monday 19 October, 8:30–9:30 (Colombia time, UTC−5)",
             "pt": "Segunda-feira, 19 de outubro, 8:30–9:30 (horário da Colômbia, UTC−5)"},
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
    # Slot: organizers' programme sheet, AC 2026-09-30.
    "when": {"es": "Lunes 19 de octubre, 14:00–15:00 (hora de Colombia, UTC−5)",
             "en": "Monday 19 October, 14:00–15:00 (Colombia time, UTC−5)",
             "pt": "Segunda-feira, 19 de outubro, 14:00–15:00 (horário da Colômbia, UTC−5)"},
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
    "affiliation": "Profesora de Química e Investigadora Sénior; directora del Centro de Estudios e Investigaciones "
                   "Ambientales (CEIAM), Escuela de Química, Universidad Industrial de Santander (UIS), Bucaramanga, "
                   "Colombia",
    "photo": "speaker_combariza.jpg",  # 10_Ponentes/Foto_Combariza_2.png (AC, 2026-09-30); 242x242, shown at 160 px
    "talk": None,
    "format": "Virtual",
    # Slot: organizers' programme sheet, AC 2026-09-30.
    "when": {"es": "Martes 20 de octubre, 15:35–16:35 (hora de Colombia, UTC−5)",
             "en": "Tuesday 20 October, 15:35–16:35 (Colombia time, UTC−5)",
             "pt": "Terça-feira, 20 de outubro, 15:35–16:35 (horário da Colômbia, UTC−5)"},
    # Bio written by us from her CV (10_Ponentes/cvCombariza.pdf, 2025, given by AC 2026-09-30) plus public sources;
    # sources in 10_Ponentes/FICHA_MCombariza.md. Not yet seen by her.
    "bio": [
        "Profesora de Química e Investigadora Sénior (Ministerio de Ciencia, Tecnología e Innovación) de la Escuela de "
        "Química de la Universidad Industrial de Santander (UIS), y directora del Centro de Estudios e Investigaciones "
        "Ambientales (CEIAM) desde 2007. Química (1994) y magíster en Química Analítica (1996) de la UIS; magíster (2003) "
        "y doctora en Química (2004) de la University of Massachusetts Amherst.",
        "Su trabajo integra la química analítica avanzada, la ciencia de materiales y los principios de la bioeconomía "
        "circular para entender, mitigar y transformar problemas ambientales, con un compromiso explícito: aumentar la "
        "circularidad de los materiales en los sectores agroindustrial y tecnológico de Colombia. Aplica la "
        "nanotecnología a la biomasa: aísla, caracteriza y modifica la celulosa, la lignina y la hemicelulosa de "
        "residuos lignocelulósicos del cacao, el fique y la palma de aceite para crear materiales funcionales, como "
        "aditivos que rompen o estabilizan emulsiones, nanocompuestos que remueven contaminantes recalcitrantes del "
        "agua y materiales que capturan y liberan nutrientes de aguas residuales. Lidera además la valorización "
        "biotecnológica de residuos agroindustriales ricos en azúcares (cacao, café, glicerol del biodiésel) para "
        "producir biopolímeros como polihidroxialcanoatos (PHA) y celulosa bacteriana, con el fin de reducir la "
        "dependencia de los polímeros sintéticos. Su obra toca así cinco de los seis ejes de SICVEC 2026: economía "
        "circular, química verde, biotecnología, tecnologías para el agua y cadenas agroindustriales.",
        "Ha dirigido 23 tesis de doctorado y maestría defendidas, sobre nanocelulosa de fique, materiales a partir de "
        "biomasa residual de palma, producción de PHB con glicerol residual del biodiésel y celulosa bacteriana a partir "
        "de efluentes de la fermentación del café, entre otros temas. Ha obtenido más de 3 millones de dólares en "
        "financiación del Sistema General de Regalías, del Ministerio de Ciencia, Tecnología e Innovación y de agencias "
        "internacionales para explorar nuevos usos de los materiales lignocelulósicos residuales de Colombia. Es "
        "coinventora de patentes sobre nanocelulosa para inhibir y romper emulsiones, celulosa bacteriana modificada y "
        "materiales para remover contaminantes del agua, y figuró en el ranking de mujeres con más patentes concedidas "
        "en Colombia en 2022 (Superintendencia de Industria y Comercio).",
        "Ha publicado más de 85 artículos en revistas como Green Chemistry, Analytical Chemistry, ACS Applied Materials "
        "& Interfaces, Chemical Communications, Carbohydrate Polymers, Cellulose, Energy & Fuels y Fuel, con más de 2.400 "
        "citas (índice h 30). Ha sido conferencista plenaria en las ACS Science Talks (2024), el Programa de Plásticos "
        "Circulares en las Américas (2023) y la Conferencia Internacional de Palma de Aceite (2022). Es miembro del "
        "Editorial Advisory Board de Energy & Fuels (American Chemical Society) y recibió el Premio Eloy Valenzuela "
        "2025-2026 de la UIS en la modalidad Trayectoria Investigativa, el máximo reconocimiento de esa universidad a la "
        "investigación.",
    ],
    "abstract": [],
}, {
    # Monique Renon Eller: speaker per AC, 2026-09-29 (also on AC's poster of 2026-09-28). Name and university only;
    # format, title, bio, abstract and photo pending.
    "name": "Dra. Monique Renon Eller",
    "role": "Conferencista magistral",
    "affiliation": "Profesora asociada, Departamento de Tecnología de Alimentos, Universidade Federal de Viçosa (UFV), "
                   "Brasil",
    "photo": "speaker_renon.jpg",  # 10_Ponentes/Foto_Monique_Renon.png (AC, 2026-09-30), cropped square without UFV logo
    "talk": None,
    "format": None,
    # Slot: organizers' programme sheet, AC 2026-09-30.
    "when": {"es": "Martes 20 de octubre, 11:20–12:20 (hora de Colombia, UTC−5)",
             "en": "Tuesday 20 October, 11:20–12:20 (Colombia time, UTC−5)",
             "pt": "Terça-feira, 20 de outubro, 11:20–12:20 (horário da Colômbia, UTC−5)"},
    # Bio written by us from her UFV faculty profile and her Lattes CV as mirrored by Escavador (10_Ponentes/Monique Renon
    # Eller _ Escavador.pdf, data of 2024-07-28), AC 2026-09-30; sources in 10_Ponentes/FICHA_RenonEller.md. Not yet seen by her.
    "bio": [
        "Profesora asociada del Departamento de Tecnología de Alimentos de la Universidade Federal de Viçosa (UFV), "
        "Brasil, donde enseña desde 2013, y orientadora en su Programa de Posgrado en Ciencia y Tecnología de Alimentos. "
        "Bioquímica (2008), magíster (2010) y doctora (2013) en Microbiología Agrícola por la UFV. Es investigadora DT-2 "
        "del Consejo Nacional de Desarrollo Científico y Tecnológico (CNPq) en Biotecnología y Microbiología Industrial.",
        "Estudia los bioprocesos desde la perspectiva de la bioeconomía circular y la sostenibilidad: usa levaduras, "
        "bacterias, hongos y sus enzimas para convertir subproductos agroindustriales en productos de valor. Integra la "
        "red Soja+ (Fapemig), que impulsa la economía circular en la cadena de procesamiento de la soja en Minas Gerais "
        "transformando la cáscara y la melaza, subproductos abundantes y hoy poco aprovechados, en bioetanol y otros "
        "productos de interés comercial, y la red INCT Leveduras (CNPq), dedicada a conocer, conservar y usar de forma "
        "sostenible las levaduras de la biodiversidad brasileña. Con su grupo ha producido bioetanol a partir de yuca "
        "industrial, hongos comestibles enriquecidos con selenio cultivados sobre subproductos agroindustriales y vinagre "
        "a partir del agua de fermentación del café, y estudia la producción de biosurfactantes por levaduras a partir de "
        "subproductos industriales. Desarrolla además sistemas colorimétricos para detectar microorganismos y "
        "contaminantes en los alimentos. Su trabajo dialoga así con los ejes de Biotecnología Sostenible, Economía "
        "Circular y Sostenibilidad en Cadenas de Suministro de SICVEC 2026.",
        "Lidera el grupo de investigación «Productos y Procesos Biotecnológicos en la Industria de Alimentos», coordina "
        "el Laboratorio de Procesos Bioquímicos y Fermentativos y el Laboratorio de Fermentación de la UFV, y creó el "
        "Centro de Referencia en Bioprocesos de la UFV, un programa para impulsar el desarrollo tecnológico y la "
        "innovación en Minas Gerais. Trabaja en alianza con empresas del sector agropecuario y de la industria de "
        "alimentos. Ha dirigido 5 tesis de doctorado y 9 de maestría, ha codirigido 13 de doctorado y 11 de maestría, y "
        "ha orientado 85 trabajos de iniciación científica y de grado. Es autora de una treintena de artículos en revistas "
        "como Food & Function, Waste and Biomass Valorization, Archives of Virology, Coffee Science e Industrial "
        "Biotechnology. Obtuvo el primer lugar del Programa Avança Café (Embrapa Café y parques tecnológicos de Viçosa y "
        "Lavras, 2023) y del Desafío de Investigación, Innovación y Negocios del Parque Tecnológico de Viçosa (2018), y "
        "el premio al mejor trabajo oral en biotecnología del XXII Simposio Nacional de Bioprocesos de Brasil (2019).",
    ],
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

# ---------- English and Portuguese (AC, 2026-09-28: official languages es/en/pt) ----------
# Translations of the Spanish texts above. Speakers' bios and abstracts are not translated (their own words).
_EN = {
    "OBJETIVO_GENERAL": ("To create a space for dialogue and knowledge production on green science and circular economy "
                         "that strengthens the capacities of researchers, students and professionals in Latin America."),
    "OBJETIVOS": [
        "Disseminate cutting-edge research on sustainable processes, green biotechnology and circular economy.",
        "Foster networking among academics, entrepreneurs and green innovators from Colombia and Latin America.",
        "Identify opportunities for inter-institutional collaboration on applied research projects.",
        "Build capacity in undergraduate and graduate students in sustainability and green innovation.",
        "Document the state of the art of green science in the region to inform future public policy.",
    ],
    "EJES_TOPICOS": [
        "Transition from linear to circular models, design for circularity, waste valorisation, cascade economy, "
        "industrial symbiosis, life-cycle assessment.",
        "Green synthesis, sustainable solvents and reagents, biocatalysis and catalysis, clean processes, molecular design "
        "to minimise waste, sustainable pharmaceutical chemistry, efficient transformations, toxicity reduction, advanced "
        "synthesis technologies (continuous flow, microwave, ultrasound), biomass valorisation.",
        "Bioproducts, microbial fermentation, green enzymes, biorefineries, bioplastics, bioethanol, biofertilisers, "
        "industrial enzymes from biological sources.",
        "Clean energy, water treatment, environmental remediation, CO₂ capture technologies, artificial photosynthesis, "
        "solar and wind energy in the food industry.",
        "Green certifications, carbon footprint, cleaner production, innovation in agro-industry, sustainable agriculture, "
        "traceability, short supply chains.",
        "SDGs 2030, regulatory frameworks for circular economy, green incentives, corporate social responsibility, "
        "environmental education, green local governments.",
    ],
    "ODS": [
        ("12", "Responsible consumption and production", "Circular economy, waste valorisation, cleaner processes."),
        ("13", "Climate action", "Green technologies, carbon emission reduction, environmental sustainability."),
        ("15", "Life on land", "Biodiversity, sustainable agro-industrial processes, green transition."),
        ("17", "Partnerships for the goals", "Academic collaboration, technology transfer, inter-institutional networks."),
    ],
    "PROGRAMA": [
        ('Monday 19 October', [
            ('07:45–08:15', 'Registration and check-in'),
            ('08:15–08:30', 'Opening ceremony of SICVEC 2026'),
            ('08:30–09:30', 'Keynote lecture 1 · Dra. Beatriz Escobar Morales, Centro de Investigación Científica de Yucatán (CICY), Mérida, Mexico · «Transformación sostenible del sargazo holopelágico en materiales funcionales avanzados»'),
            ('09:30–09:55', 'Talk 1 (to be assigned)'),
            ('09:55–10:20', 'Talk 2 (to be assigned)'),
            ('10:20–10:40', 'Coffee break'),
            ('10:40–11:05', 'Talk 3 (to be assigned)'),
            ('11:05–11:30', 'Talk 4 (to be assigned)'),
            ('11:30–11:55', 'Talk 5 · Gobernación de Sucre, Sincelejo, Colombia'),
            ('11:55–12:20', 'Talk 6 (to be assigned)'),
            ('12:20–14:00', 'Lunch (on your own)'),
            ('14:00–15:00', 'Keynote lecture 2 · Dr. Wilson Manuel Castro Silupu, Universidad Nacional de Frontera, Peru · «Medicinal plant discrimination: A study of deep learning techniques and a novel approach for data augmentation»'),
            ('15:00–15:25', 'Talk 7 · Dr. Pedro Meza Catellar, Universidad de San Buenaventura, Cartagena de Indias, Colombia'),
            ('15:25–15:50', 'Talk 8 (to be assigned)'),
            ('15:50–16:10', 'Coffee break'),
            ('16:10–17:30', 'Poster session + networking'),
        ]),
        ('Tuesday 20 October', [
            ('08:00–08:30', 'Registration and check-in'),
            ('08:30–09:00', 'Talk 9 · Esp. Carlos Meza Bertel, Parque Comercial Guacarí, Sincelejo, Colombia'),
            ('09:00–10:00', 'Keynote lecture 3 · Prof. Enrico Valli, Università di Bologna, Bologna, Italy · «Valorization of by-products from olive oil production as a source of bioactive compounds»'),
            ('10:00–10:25', 'Talk 10 · Dra. Laura Hil Pastor, Universidad de Sucre, Sincelejo, Colombia'),
            ('10:25–10:50', 'Coffee break'),
            ('10:50–11:15', 'Talk 11 · Est. Mg. Guillermo Alejandro Corrales, Universidad Santo Tomás, Bogotá, Colombia · «Efecto de la producción de metano durante la codigestión anaeróbica de estiércol de bovino, residuos de maíz y lenteja de agua (Lemna sp.)»'),
            ('11:15–11:20', 'Sponsor slot'),
            ('11:20–12:20', 'Keynote lecture 4 · Dra. Monique Renon Eller, Universidade Federal de Viçosa, Viçosa, Brazil'),
            ('12:20–14:00', 'Lunch (on your own)'),
            ('14:00–14:25', 'Talk 12 (to be assigned)'),
            ('14:25–14:50', 'Talk 13 (to be assigned)'),
            ('14:50–15:15', 'Talk 14 (to be assigned)'),
            ('15:15–15:35', 'Coffee break'),
            ('15:35–16:35', 'Keynote lecture 5 · Dra. Marianny Y. Combariza, Universidad Industrial de Santander, Bucaramanga, Colombia'),
            ('16:35–17:00', 'Closing ceremony: best poster awards and close of the symposium'),
        ]),
    ],
    "PUBLICO": [
        "Researchers in chemistry, physics, mathematics, biology, environmental sciences and all branches of engineering.",
        "Undergraduate and graduate students in basic sciences and engineering.",
        "Science and engineering lecturers interested in sustainability and circular economy.",
        "Professionals from the food, chemical, energy, agricultural, materials and environmental-services industries.",
        "Entrepreneurs with green innovation initiatives, environmental managers and consultants.",
        "Public-sector decision makers and civil-society organisations.",
    ],
    "ROLE": "Keynote speaker",
    "COORDINADORES": [("Aldo F. Combariza", "General Coordination"), ("María Ximena Díaz", "Academic Coordination"),
                      ("Sebastián Vargas", "Logistics Coordination"), ("Selena Arias Avila", "Administrative Coordination")],
    "DEPARTAMENTOS": ["Department of Biology and Chemistry", "Department of Agro-industrial Engineering",
                      "Department of Agricultural Engineering", "Department of Physics"],
}
_PT = {
    "OBJETIVO_GENERAL": ("Criar um espaço de diálogo e produção de conhecimento sobre ciência verde e economia circular que "
                         "fortaleça as capacidades de pesquisadores, estudantes e profissionais na América Latina."),
    "OBJETIVOS": [
        "Divulgar pesquisas de ponta em processos sustentáveis, biotecnologia verde e economia circular.",
        "Promover o networking entre acadêmicos, empresários e inovadores verdes da Colômbia e da América Latina.",
        "Identificar oportunidades de colaboração interinstitucional em projetos de pesquisa aplicada.",
        "Fomentar a formação de estudantes de graduação e pós-graduação em sustentabilidade e inovação verde.",
        "Documentar o estado da arte da ciência verde na região para futuros impactos em políticas públicas.",
    ],
    "EJES_TOPICOS": [
        "Transição de modelos lineares para circulares, design para a circularidade, valorização de resíduos, economia "
        "em cascata, simbiose industrial, avaliação do ciclo de vida.",
        "Síntese verde, solventes e reagentes sustentáveis, biocatálise e catálise, processos limpos, design molecular "
        "para minimizar resíduos, química farmacêutica sustentável, transformações eficientes, redução da toxicidade, "
        "tecnologias de síntese avançadas (fluxo contínuo, micro-ondas, ultrassom), valorização da biomassa.",
        "Bioprodutos, fermentação microbiana, enzimas verdes, biorrefinarias, bioplásticos, bioetanol, biofertilizantes, "
        "enzimas industriais de fonte biológica.",
        "Energias limpas, tratamento de águas, remediação ambiental, tecnologias de captura de CO₂, fotossíntese "
        "artificial, energia solar e eólica na indústria de alimentos.",
        "Certificações verdes, pegada de carbono, produção mais limpa, inovação na agroindústria, agricultura "
        "sustentável, rastreabilidade, cadeias curtas.",
        "ODS 2030, marcos regulatórios para a economia circular, incentivos verdes, responsabilidade social empresarial, "
        "educação ambiental, governos locais verdes.",
    ],
    "ODS": [
        ("12", "Consumo e produção responsáveis", "Economia circular, valorização de resíduos, processos mais limpos."),
        ("13", "Ação contra a mudança global do clima", "Tecnologias verdes, redução de emissões de carbono, sustentabilidade ambiental."),
        ("15", "Vida terrestre", "Biodiversidade, processos agroindustriais sustentáveis, transição verde."),
        ("17", "Parcerias e meios de implementação", "Colaboração acadêmica, transferência de tecnologia, redes interinstitucionais."),
    ],
    "PROGRAMA": [
        ('Segunda-feira, 19 de outubro', [
            ('07:45–08:15', 'Inscrição e credenciamento dos participantes'),
            ('08:15–08:30', 'Cerimônia de abertura do SICVEC 2026'),
            ('08:30–09:30', 'Conferência magistral 1 · Dra. Beatriz Escobar Morales, Centro de Investigación Científica de Yucatán (CICY), Mérida, México · «Transformación sostenible del sargazo holopelágico en materiales funcionales avanzados»'),
            ('09:30–09:55', 'Apresentação 1 (a definir)'),
            ('09:55–10:20', 'Apresentação 2 (a definir)'),
            ('10:20–10:40', 'Intervalo (café)'),
            ('10:40–11:05', 'Apresentação 3 (a definir)'),
            ('11:05–11:30', 'Apresentação 4 (a definir)'),
            ('11:30–11:55', 'Apresentação 5 · Gobernación de Sucre, Sincelejo, Colombia'),
            ('11:55–12:20', 'Apresentação 6 (a definir)'),
            ('12:20–14:00', 'Almoço livre'),
            ('14:00–15:00', 'Conferência magistral 2 · Dr. Wilson Manuel Castro Silupu, Universidad Nacional de Frontera, Peru · «Medicinal plant discrimination: A study of deep learning techniques and a novel approach for data augmentation»'),
            ('15:00–15:25', 'Apresentação 7 · Dr. Pedro Meza Catellar, Universidad de San Buenaventura, Cartagena de Indias, Colombia'),
            ('15:25–15:50', 'Apresentação 8 (a definir)'),
            ('15:50–16:10', 'Intervalo (café)'),
            ('16:10–17:30', 'Sessão de pôsteres + networking'),
        ]),
        ('Terça-feira, 20 de outubro', [
            ('08:00–08:30', 'Inscrição e credenciamento dos participantes'),
            ('08:30–09:00', 'Apresentação 9 · Esp. Carlos Meza Bertel, Parque Comercial Guacarí, Sincelejo, Colombia'),
            ('09:00–10:00', 'Conferência magistral 3 · Prof. Enrico Valli, Università di Bologna, Bolonha, Itália · «Valorization of by-products from olive oil production as a source of bioactive compounds»'),
            ('10:00–10:25', 'Apresentação 10 · Dra. Laura Hil Pastor, Universidad de Sucre, Sincelejo, Colombia'),
            ('10:25–10:50', 'Intervalo (café)'),
            ('10:50–11:15', 'Apresentação 11 · Est. Mg. Guillermo Alejandro Corrales, Universidad Santo Tomás, Bogotá, Colombia · «Efecto de la producción de metano durante la codigestión anaeróbica de estiércol de bovino, residuos de maíz y lenteja de agua (Lemna sp.)»'),
            ('11:15–11:20', 'Espaço publicitário'),
            ('11:20–12:20', 'Conferência magistral 4 · Dra. Monique Renon Eller, Universidade Federal de Viçosa, Viçosa, Brasil'),
            ('12:20–14:00', 'Almoço livre'),
            ('14:00–14:25', 'Apresentação 12 (a definir)'),
            ('14:25–14:50', 'Apresentação 13 (a definir)'),
            ('14:50–15:15', 'Apresentação 14 (a definir)'),
            ('15:15–15:35', 'Intervalo (café)'),
            ('15:35–16:35', 'Conferência magistral 5 · Dra. Marianny Y. Combariza, Universidad Industrial de Santander, Bucaramanga, Colombia'),
            ('16:35–17:00', 'Cerimônia de encerramento: reconhecimento aos melhores pôsteres e encerramento do evento'),
        ]),
    ],
    "PUBLICO": [
        "Pesquisadores em química, física, matemática, biologia, ciências ambientais e todas as engenharias.",
        "Estudantes de graduação e pós-graduação em ciências básicas e engenharias.",
        "Docentes de ciências e engenharia interessados em sustentabilidade e economia circular.",
        "Profissionais das indústrias de alimentos, química, energia, agrícola, de materiais e de serviços ambientais.",
        "Empreendedores com iniciativas de inovação verde, gestores ambientais e consultores.",
        "Tomadores de decisão do setor público e organizações da sociedade civil.",
    ],
    "ROLE": "Palestrante magistral",
    "COORDINADORES": [("Aldo F. Combariza", "Coordenação Geral"), ("María Ximena Díaz", "Coordenação Acadêmica"),
                      ("Sebastián Vargas", "Coordenação de Logística"), ("Selena Arias Avila", "Coordenação Administrativa")],
    "DEPARTAMENTOS": ["Departamento de Biologia e Química", "Departamento de Engenharia Agroindustrial",
                      "Departamento de Engenharia Agrícola", "Departamento de Física"],
}


def for_lang(lang):
    """Content for one interface language; anything not translated falls back to Spanish."""
    from types import SimpleNamespace
    names = ("OBJETIVO_GENERAL", "OBJETIVOS", "EJES_TOPICOS", "ODS", "PROGRAMA", "PUBLICO", "COORDINADORES",
             "DEPARTAMENTOS", "SPEAKERS", "EMAIL_COORDINACION")
    base = {n: globals()[n] for n in names}
    tr = {"en": _EN, "pt": _PT}.get(lang)
    if tr:
        base.update({k: v for k, v in tr.items() if k != "ROLE"})
        base["SPEAKERS"] = [dict(s, role=tr["ROLE"]) for s in SPEAKERS]
    return SimpleNamespace(**base)
