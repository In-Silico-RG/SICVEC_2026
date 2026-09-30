"""Interface languages (AC, 2026-09-28: official languages Spanish, English and Portuguese).

Public pages, forms, validation messages and author emails are translated. Admin and reviewer pages stay in Spanish.
Stored values (axis names, modality/category keys) stay in Spanish; only their labels change.
"""
from markupsafe import Markup

LANGS = ("es", "en", "pt")
LANG_NAMES = {"es": "Español", "en": "English", "pt": "Português"}

# Labels for values stored in Spanish (same order as logic.AXES).
AXES = {
    "en": ["Circular Economy", "Green Chemistry and Sustainable Processes", "Sustainable Biotechnology",
           "Green Technologies and Renewable Energy", "Sustainability in Supply Chains",
           "Public Policy and Environmental Governance"],
    "pt": ["Economia Circular", "Química Verde e Processos Sustentáveis", "Biotecnologia Sustentável",
           "Tecnologias Verdes e Energias Renováveis", "Sustentabilidade em Cadeias de Suprimentos",
           "Políticas Públicas e Governança Ambiental"],
}
MODALITIES = {
    "en": {"oral": "Oral presentation (20 min)", "poster": "Scientific poster (90 × 120 cm)"},
    "pt": {"oral": "Apresentação oral (20 min)", "poster": "Pôster científico (90 × 120 cm)"},
}
CATEGORIES = {
    "en": {"pregrado": "Undergraduate student", "posgrado": "Graduate student", "profesional": "Professional",
           "virtual": "Online attendance"},
    "pt": {"pregrado": "Estudante de graduação", "posgrado": "Estudante de pós-graduação", "profesional": "Profissional",
           "virtual": "Participação on-line"},
}
DECISIONS = {
    "en": {"aceptado": "Accepted", "aceptado_con_cambios": "Accepted with changes", "rechazado": "Not accepted"},
    "pt": {"aceptado": "Aceito", "aceptado_con_cambios": "Aceito com alterações", "rechazado": "Não aceito"},
}

T = {
    # header and footer
    "nav_home": ("Inicio", "Home", "Início"),
    "nav_program": ("Programa", "Programme", "Programação"),
    "nav_speakers": ("Conferencistas", "Speakers", "Palestrantes"),
    "nav_submit": ("Enviar resumen", "Submit abstract", "Enviar resumo"),
    "nav_register": ("Inscripción", "Registration", "Inscrição"),
    "f_organizan": ("Organizan", "Organised by", "Organização"),
    "f_colaboran": ("Colaboran", "In collaboration with", "Colaboração"),
    "f_fisica": ("Departamento<br><strong>de Física</strong>", "Department<br><strong>of Physics</strong>",
                 "Departamento<br><strong>de Física</strong>"),
    "f_organiza": ("Organiza", "Organiser", "Organização"),
    "f_org_text": (
        "<strong>Grupo de Investigación IN SILICO</strong><br>Departamento de Biología y Química<br>Facultad de Educación "
        "y Ciencias<br>Universidad de Sucre (UNISUCRE)<br>Sincelejo, Sucre, Colombia",
        "<strong>IN SILICO Research Group</strong><br>Department of Biology and Chemistry<br>Faculty of Education and "
        "Sciences<br>Universidad de Sucre (UNISUCRE)<br>Sincelejo, Sucre, Colombia",
        "<strong>Grupo de Pesquisa IN SILICO</strong><br>Departamento de Biologia e Química<br>Faculdade de Educação e "
        "Ciências<br>Universidad de Sucre (UNISUCRE)<br>Sincelejo, Sucre, Colômbia"),
    "f_coorg": ("Co-organizadores", "Co-organisers", "Co-organizadores"),
    "f_coord": ("Coordinación", "Coordination", "Coordenação"),
    "f_event": ("Evento y contacto", "Event and contact", "Evento e contato"),
    "f_dates": ("19–20 de octubre de 2026", "19–20 October 2026", "19–20 de outubro de 2026"),
    "f_hybrid": ("Modalidad híbrida", "Hybrid format", "Formato híbrido"),
    "f_fin": ("I Simposio Internacional de Ciencia Verde y Economía Circular · Universidad de Sucre, Colombia",
              "1st International Symposium on Green Science and Circular Economy · Universidad de Sucre, Colombia",
              "I Simpósio Internacional de Ciência Verde e Economia Circular · Universidad de Sucre, Colômbia"),
    # home
    "idx_h1": ("Simposio Internacional de Ciencia Verde y Economía Circular",
               "International Symposium on Green Science and Circular Economy",
               "Simpósio Internacional de Ciência Verde e Economia Circular"),
    "idx_lead": ("19–20 de octubre de 2026 · Centro Comercial Guacarí, Sincelejo, Sucre, Colombia · modalidad híbrida.",
                 "19–20 October 2026 · Centro Comercial Guacarí, Sincelejo, Sucre, Colombia · hybrid format.",
                 "19–20 de outubro de 2026 · Centro Comercial Guacarí, Sincelejo, Sucre, Colômbia · formato híbrido."),
    "idx_langs": ("<strong>Idiomas oficiales:</strong> español, inglés y portugués.",
                  "<strong>Official languages:</strong> Spanish, English and Portuguese.",
                  "<strong>Idiomas oficiais:</strong> espanhol, inglês e português."),
    "btn_submit_abs": ("Enviar un resumen", "Submit an abstract", "Enviar um resumo"),
    "btn_register": ("Inscribirme", "Register", "Inscrever-me"),
    "btn_program": ("Ver programa", "See the programme", "Ver programação"),
    "h_dates": ("Fechas importantes", "Key dates", "Datas importantes"),
    "d_close": ("Cierre de resúmenes", "Abstract deadline", "Prazo para resumos"),
    "col_time": ("(hora Colombia)", "(Colombia time, UTC−5)", "(horário da Colômbia, UTC−5)"),
    "d_review": ("Evaluación de pares", "Peer review", "Avaliação por pares"),
    "d_until": ("hasta", "until", "até"),
    "d_pay": ("Límite de pago de inscripción presencial", "Payment deadline for in-person registration",
              "Prazo de pagamento da inscrição presencial"),
    "d_symp": ("Simposio", "Symposium", "Simpósio"),
    "d_symp_val": ("Lunes 19 y martes 20 de octubre de 2026", "Monday 19 and Tuesday 20 October 2026",
                   "Segunda-feira 19 e terça-feira 20 de outubro de 2026"),
    "h_about": ("Sobre el simposio", "About the symposium", "Sobre o simpósio"),
    "about_p": ("El Simposio Internacional de Ciencia Verde y Economía Circular (SICVEC 2026) es una iniciativa de la "
                "Universidad de Sucre (UNISUCRE) para generar espacios de diálogo, investigación e innovación en torno a "
                "los desafíos de sostenibilidad ambiental, los procesos circulares y las tecnologías verdes.",
                "The International Symposium on Green Science and Circular Economy (SICVEC 2026) is an initiative of "
                "Universidad de Sucre (UNISUCRE) to create spaces for dialogue, research and innovation around the "
                "challenges of environmental sustainability, circular processes and green technologies.",
                "O Simpósio Internacional de Ciência Verde e Economia Circular (SICVEC 2026) é uma iniciativa da "
                "Universidad de Sucre (UNISUCRE) para criar espaços de diálogo, pesquisa e inovação em torno dos desafios "
                "da sustentabilidade ambiental, dos processos circulares e das tecnologias verdes."),
    "h_obj": ("Objetivos específicos", "Specific objectives", "Objetivos específicos"),
    "h_axes": ("Ejes temáticos", "Thematic axes", "Eixos temáticos"),
    "axis_word": ("Eje", "Axis", "Eixo"),
    "h_ods": ("Objetivos de Desarrollo Sostenible", "Sustainable Development Goals",
              "Objetivos de Desenvolvimento Sustentável"),
    "ods_word": ("ODS", "SDG", "ODS"),
    "h_participate": ("Cómo participar", "How to take part", "Como participar"),
    "p_present_h": ("Presentar un trabajo", "Present your work", "Apresentar um trabalho"),
    "p_present": ("{oral} o {poster}. Resúmenes evaluados por pares (revisión ciega) hasta el {date}.",
                  "{oral} or {poster}. Abstracts are peer reviewed (blind review); deadline {date}.",
                  "{oral} ou {poster}. Resumos avaliados por pares (avaliação cega) até {date}."),
    "p_attend_h": ("Asistir en Sincelejo", "Attend in Sincelejo", "Participar em Sincelejo"),
    "p_attend_cat": ("Inscripción presencial por categoría:", "In-person registration by category:",
                     "Inscrição presencial por categoria:"),
    "fee_pre": ("Pregrado", "Undergraduate students", "Estudantes de graduação"),
    "fee_pos": ("Posgrado", "Graduate students", "Estudantes de pós-graduação"),
    "fee_pro": ("Profesional", "Professionals", "Profissionais"),
    "p_online_h": ("Asistir en línea", "Attend online", "Participar on-line"),
    "p_online": ("Participación en línea gratuita para participantes externos e internacionales. Plataforma de "
                 "transmisión: <span class=\"pend\">por anunciar</span>.",
                 "Online participation is free for external and international participants. Streaming platform: "
                 "<span class=\"pend\">to be announced</span>.",
                 "Participação on-line gratuita para participantes externos e internacionais. Plataforma de "
                 "transmissão: <span class=\"pend\">a ser anunciada</span>."),
    "btn_seat": ("Inscribirme en línea", "Register online", "Inscrever-me on-line"),
    "h_audience": ("Dirigido a", "Who should attend", "Público-alvo"),
    "h_venue": ("Lugar", "Venue", "Local"),
    "venue_addr": ("Calle 28 No. 25B-97, Barrio Bostón, Sincelejo, Sucre, Colombia.",
                   "Calle 28 No. 25B-97, Barrio Bostón, Sincelejo, Sucre, Colombia.",
                   "Calle 28 No. 25B-97, Barrio Bostón, Sincelejo, Sucre, Colômbia."),
    "btn_maps": ("Ver en Google Maps", "View on Google Maps", "Ver no Google Maps"),
    "venue_room": ("Sede: sala de conferencias del Centro Comercial Guacarí.",
                   "Room: conference hall of Centro Comercial Guacarí.",
                   "Sala: auditório do Centro Comercial Guacarí."),
    # programme
    "prog_title": ("Programa", "Programme", "Programação"),
    "prog_notice": ("<strong>Programa preliminar.</strong> Estructura propuesta por el comité organizador; el orden de "
                    "presentaciones y las franjas de conferencistas se publicarán tras la evaluación de resúmenes "
                    "(decisiones el 15 de octubre) y pueden cambiar. Horario de Colombia (UTC−5). Modalidad híbrida.",
                    "<strong>Preliminary programme.</strong> Structure proposed by the organising committee; the order of "
                    "talks and the speakers' slots will be published after abstract review (decisions on 15 October) and "
                    "may change. Colombia time (UTC−5). Hybrid format.",
                    "<strong>Programação preliminar.</strong> Estrutura proposta pela comissão organizadora; a ordem das "
                    "apresentações e os horários dos palestrantes serão publicados após a avaliação dos resumos (decisões "
                    "em 15 de outubro) e podem mudar. Horário da Colômbia (UTC−5). Formato híbrido."),
    # speakers
    "sp_title": ("Conferencistas", "Speakers", "Palestrantes"),
    "sp_talk": ("Conferencia:", "Talk:", "Palestra:"),
    "sp_title_tbc": ("Título de la conferencia: por confirmar.", "Talk title: to be confirmed.",
                     "Título da palestra: a confirmar."),
    "sp_when": ("Fecha y hora:", "Date and time:", "Data e horário:"),
    "sp_date_tbc": ("Fecha y hora de la conferencia: por confirmar (19 o 20 de octubre).",
                    "Date and time: to be confirmed (19 or 20 October).",
                    "Data e horário: a confirmar (19 ou 20 de outubro)."),
    "sp_bio": ("Semblanza", "Biography", "Biografia"),
    "sp_abstract": ("Resumen de la conferencia", "Abstract of the talk", "Resumo da palestra"),
    "sp_original": ("", "Biography and abstract in the speaker's original language.",
                    "Biografia e resumo no idioma original do palestrante."),
    "sp_more": ("Se anunciarán más conferencistas.", "More speakers will be announced.",
                "Mais palestrantes serão anunciados."),
    # abstract form
    "sub_h1": ("Envío de resúmenes", "Abstract submission", "Envio de resumos"),
    "sub_intro": ("Cierre: {date} (hora Colombia). El resumen se pega como texto y <b>no debe incluir nombres de "
                  "autores ni afiliaciones</b> (revisión ciega). Máximo de palabras: oral {oral}, póster {poster}. "
                  "Idiomas aceptados: español, inglés o portugués.",
                  "Deadline: {date} (Colombia time, UTC−5). Paste the abstract as text; it <b>must not include author "
                  "names or affiliations</b> (blind review). Word limit: oral {oral}, poster {poster}. Accepted "
                  "languages: Spanish, English or Portuguese.",
                  "Prazo: {date} (horário da Colômbia, UTC−5). Cole o resumo como texto; ele <b>não deve incluir nomes "
                  "de autores nem afiliações</b> (avaliação cega). Limite de palavras: oral {oral}, pôster {poster}. "
                  "Idiomas aceitos: espanhol, inglês ou português."),
    "l_email_contact": ("Correo de contacto", "Contact email", "E-mail de contato"),
    "l_title": ("Título del trabajo", "Title of the work", "Título do trabalho"),
    "l_lang": ("Idioma del resumen", "Language of the abstract", "Idioma do resumo"),
    "l_modality": ("Modalidad", "Format", "Modalidade"),
    "l_presentation": ("Presentación", "Presentation", "Apresentação"),
    "opt_presencial": ("Presencial", "In person", "Presencial"),
    "opt_virtual": ("Virtual", "Online", "On-line"),
    "l_axis": ("Eje temático principal", "Main thematic axis", "Eixo temático principal"),
    "l_abstract": ("Resumen (sin nombres de autores ni afiliaciones)", "Abstract (no author names or affiliations)",
                   "Resumo (sem nomes de autores nem afiliações)"),
    "l_keywords": ("Palabras clave", "Keywords", "Palavras-chave"),
    "l_keywords_help": ("(3 a 5, separadas por comas)", "(3 to 5, separated by commas)",
                        "(3 a 5, separadas por vírgulas)"),
    "h_presenter": ("Autor que presenta", "Presenting author", "Autor que apresenta"),
    "l_fullname": ("Nombre completo", "Full name", "Nome completo"),
    "l_institution": ("Institución", "Institution", "Instituição"),
    "l_program": ("Programa académico o profesión", "Academic programme or profession", "Curso ou profissão"),
    "l_country_from": ("País de procedencia", "Country", "País de origem"),
    "l_others": ("Otros autores", "Other authors", "Outros autores"),
    "l_others_help": ("(opcional, uno por línea: nombre, institución; máximo 4 más)",
                      "(optional, one per line: name, institution; up to 4 more)",
                      "(opcional, um por linha: nome, instituição; no máximo mais 4)"),
    "l_originality": ("El trabajo es original y no está en evaluación en otro evento.",
                      "The work is original and is not under review for another event.",
                      "O trabalho é original e não está em avaliação em outro evento."),
    "btn_send_abs": ("Enviar resumen", "Submit abstract", "Enviar resumo"),
    "subok_h1": ("Resumen recibido", "Abstract received", "Resumo recebido"),
    "subok_text": ("Su referencia es <b>{ref}</b>. Le enviamos una confirmación por correo.",
                   "Your reference is <b>{ref}</b>. We have sent you a confirmation email.",
                   "Sua referência é <b>{ref}</b>. Enviamos uma confirmação por e-mail."),
    "subok_flags": ("El comité revisará manualmente su envío porque:",
                    "The committee will check your submission manually because:",
                    "A comissão revisará seu envio manualmente porque:"),
    "subok_blind": ("Recuerde que el resumen no debe identificar a los autores.",
                    "Remember that the abstract must not identify the authors.",
                    "Lembre-se de que o resumo não deve identificar os autores."),
    "closed_h1": ("Plazo cerrado", "Deadline passed", "Prazo encerrado"),
    "closed_submit": ("El envío de resúmenes cerró el {date} (hora Colombia).",
                      "Abstract submission closed on {date} (Colombia time).",
                      "O envio de resumos foi encerrado em {date} (horário da Colômbia)."),
    # registration form
    "reg_h1": ("Inscripción", "Registration", "Inscrição"),
    "reg_intro": ("Asistencia presencial: pregrado COP {pre} · posgrado COP {pos} · profesional COP {pro}. "
                  "Participación virtual: <b>gratuita</b> para participantes externos e internacionales. "
                  "Límite de pago: {date}. Datos para la transferencia: <b>[PENDIENTE: banco, cuenta, titular]</b>.",
                  "In-person attendance: undergraduate COP {pre} · graduate COP {pos} · professional COP {pro}. "
                  "Online participation: <b>free</b> for external and international participants. "
                  "Payment deadline: {date}. Bank transfer details: <b>[to be announced]</b>.",
                  "Participação presencial: graduação COP {pre} · pós-graduação COP {pos} · profissional COP {pro}. "
                  "Participação on-line: <b>gratuita</b> para participantes externos e internacionais. "
                  "Prazo de pagamento: {date}. Dados para a transferência: <b>[a ser anunciado]</b>."),
    "l_email": ("Correo electrónico", "Email", "E-mail"),
    "l_phone": ("Teléfono", "Phone", "Telefone"),
    "l_document": ("Documento de identidad (tipo y número)", "ID document (type and number)",
                   "Documento de identidade (tipo e número)"),
    "l_country": ("País", "Country", "País"),
    "l_category": ("Categoría", "Category", "Categoria"),
    "l_attendance": ("Modalidad de asistencia", "Attendance", "Modalidade de participação"),
    "l_presents": ("Presento un trabajo", "I am presenting a work", "Vou apresentar um trabalho"),
    "l_subref": ("Referencia del resumen (SICVEC-###)", "Abstract reference (SICVEC-###)",
                 "Referência do resumo (SICVEC-###)"),
    "l_payref": ("Referencia o fecha de la transferencia", "Transfer reference or date",
                 "Referência ou data da transferência"),
    "l_receipt": ("Comprobante de pago", "Payment receipt", "Comprovante de pagamento"),
    "l_receipt_help": ("(PDF, PNG o JPG, máx. 5 MB; opcional ahora)", "(PDF, PNG or JPG, max. 5 MB; optional now)",
                       "(PDF, PNG ou JPG, máx. 5 MB; opcional agora)"),
    "btn_send_reg": ("Enviar inscripción", "Submit registration", "Enviar inscrição"),
    "regok_h1": ("Inscripción recibida", "Registration received", "Inscrição recebida"),
    "regok_text": ("Su referencia es <b>{ref}</b>. Valor: COP {fee}. Le enviamos los detalles por correo.",
                   "Your reference is <b>{ref}</b>. Amount: COP {fee}. We have sent you the details by email.",
                   "Sua referência é <b>{ref}</b>. Valor: COP {fee}. Enviamos os detalhes por e-mail."),
    # consent (Spanish legal text comes from config.CONSENT_TEXT / INSTITUTION_DATA)
    "consent": ("",
                "I freely, expressly and knowingly authorise Universidad de Sucre to process my personal data in order "
                "to manage my participation in SICVEC 2026 (abstract submission and review, registration, payments, "
                "certificates, proceedings and related communications), under Colombian Law 1581 of 2012 and the "
                "Personal Data Processing Policy of Universidad de Sucre (Resolution 1129 of 2021). I know my rights to "
                "access, update, correct and delete my data and to withdraw this authorisation. The Spanish version of "
                "this text prevails.",
                "Autorizo de forma livre, prévia, expressa e informada a Universidad de Sucre a tratar meus dados pessoais "
                "para gerenciar minha participação no SICVEC 2026 (envio e avaliação de resumos, inscrição, pagamentos, "
                "certificados, anais do evento e comunicações relacionadas), conforme a Lei colombiana 1581 de 2012 e a "
                "Política de Tratamento de Dados Pessoais da Universidad de Sucre (Resolução 1129 de 2021). Conheço meus "
                "direitos de acessar, atualizar, retificar e excluir meus dados e de revogar esta autorização. Prevalece "
                "a versão em espanhol deste texto."),
    "institution_data": ("",
                         "Data controller: Universidad de Sucre, NIT 892.200.323-9, Cra. 28 # 5-267, Barrio Puerta Roja, "
                         "Sincelejo (Sucre), Colombia. Policy: Resolution 1129 of 2021, available at unisucre.edu.co. "
                         "Requests and complaints: atencionalciudadano@unisucre.edu.co or in writing to the address "
                         "above (answer within 15 business days). Questions about the event: insilico@unisucre.edu.co.",
                         "Responsável pelo tratamento: Universidad de Sucre, NIT 892.200.323-9, Cra. 28 # 5-267, Barrio "
                         "Puerta Roja, Sincelejo (Sucre), Colômbia. Política: Resolução 1129 de 2021, disponível em "
                         "unisucre.edu.co. Consultas e reclamações: atencionalciudadano@unisucre.edu.co ou por escrito "
                         "no endereço indicado (resposta em até 15 dias úteis). Dúvidas sobre o evento: "
                         "insilico@unisucre.edu.co."),
    # validation messages
    "e_email": ("Correo de contacto no válido.", "Invalid contact email.", "E-mail de contato inválido."),
    "e_title": ("El título es obligatorio (máx. 200 caracteres).", "The title is required (max. 200 characters).",
                "O título é obrigatório (máx. 200 caracteres)."),
    "e_lang": ("Elija el idioma.", "Choose the language.", "Escolha o idioma."),
    "e_modality": ("Elija la modalidad.", "Choose the format.", "Escolha a modalidade."),
    "e_presentation": ("Elija presencial o virtual.", "Choose in person or online.", "Escolha presencial ou on-line."),
    "e_axis": ("Elija el eje temático.", "Choose the thematic axis.", "Escolha o eixo temático."),
    "e_keywords": ("Indique de 3 a 5 palabras clave separadas por comas.", "Give 3 to 5 keywords separated by commas.",
                   "Indique de 3 a 5 palavras-chave separadas por vírgulas."),
    "e_abstract": ("El resumen es obligatorio.", "The abstract is required.", "O resumo é obrigatório."),
    "e_words": ("El resumen tiene {wc} palabras; el máximo para esta modalidad es {limit}.",
                "The abstract has {wc} words; the limit for this format is {limit}.",
                "O resumo tem {wc} palavras; o máximo para esta modalidade é {limit}."),
    "e_presenter": ("Autor que presenta: falta {label}.", "Presenting author: {label} is missing.",
                    "Autor que apresenta: falta {label}."),
    "e_authors": ("Máximo 5 autores en total (4 en 'otros autores').", "At most 5 authors in total (4 under 'other authors').",
                  "No máximo 5 autores no total (4 em 'outros autores')."),
    "e_consent": ("Debe autorizar el tratamiento de datos personales.", "You must authorise the processing of personal data.",
                  "Você deve autorizar o tratamento de dados pessoais."),
    "e_orig": ("Debe confirmar la originalidad del trabajo.", "You must confirm that the work is original.",
               "Você deve confirmar a originalidade do trabalho."),
    "e_dup_sub": ("Ya existe un envío con ese correo y ese título.", "A submission with this email and title already exists.",
                  "Já existe um envio com esse e-mail e esse título."),
    "e_missing": ("Falta {label}.", "{label} is missing.", "Falta {label}."),
    "e_email2": ("Correo no válido.", "Invalid email.", "E-mail inválido."),
    "e_category": ("Elija la categoría.", "Choose the category.", "Escolha a categoria."),
    "e_catvirtual": ("La categoría virtual requiere asistencia virtual.", "The online category requires online attendance.",
                     "A categoria on-line exige participação on-line."),
    "e_seats": ("Los cupos en línea están agotados.", "Online seats are sold out.", "As vagas on-line estão esgotadas."),
    "e_receipt": ("El comprobante debe ser PDF, PNG o JPG válido.", "The receipt must be a valid PDF, PNG or JPG.",
                  "O comprovante deve ser um PDF, PNG ou JPG válido."),
    "e_dup_reg": ("Ya existe una inscripción con ese correo.", "A registration with this email already exists.",
                  "Já existe uma inscrição com esse e-mail."),
    "n_name": ("nombre", "name", "nome"),
    "n_institution": ("institución", "institution", "instituição"),
    "n_program": ("programa o profesión", "programme or profession", "curso ou profissão"),
    "n_country": ("país", "country", "país"),
    "n_phone": ("teléfono", "phone", "telefone"),
    "n_document": ("documento", "ID document", "documento"),
    # emails (plain text)
    "m_sub_subject": ("SICVEC 2026 — resumen recibido ({ref})", "SICVEC 2026 — abstract received ({ref})",
                      "SICVEC 2026 — resumo recebido ({ref})"),
    "m_sub_body": ("Hemos recibido su resumen «{title}».\nReferencia: {ref}\nCierre: {close} (hora Colombia). "
                   "La notificación se envía el 15 de octubre de 2026.",
                   "We have received your abstract “{title}”.\nReference: {ref}\nDeadline: {close} (Colombia time). "
                   "Decisions will be sent on 15 October 2026.",
                   "Recebemos seu resumo “{title}”.\nReferência: {ref}\nPrazo: {close} (horário da Colômbia). "
                   "O resultado será enviado em 15 de outubro de 2026."),
    "m_reg_subject": ("SICVEC 2026 — inscripción recibida ({ref})", "SICVEC 2026 — registration received ({ref})",
                      "SICVEC 2026 — inscrição recebida ({ref})"),
    "m_reg_body": ("Hemos recibido su inscripción ({ref}).\nValor: COP {fee}\nLímite de pago: {date} (hora Colombia).",
                   "We have received your registration ({ref}).\nAmount: COP {fee}\nPayment deadline: {date} (Colombia time).",
                   "Recebemos sua inscrição ({ref}).\nValor: COP {fee}\nPrazo de pagamento: {date} (horário da Colômbia)."),
    "m_dec_subject": ("SICVEC 2026 — resultado de su resumen ({ref})", "SICVEC 2026 — result for your abstract ({ref})",
                      "SICVEC 2026 — resultado do seu resumo ({ref})"),
    "m_dec_result": ("Resultado de su resumen «{title}» ({ref}): {decision}.",
                     "Result for your abstract “{title}” ({ref}): {decision}.",
                     "Resultado do seu resumo “{title}” ({ref}): {decision}."),
    "m_dec_note": ("Nota del comité: {note}", "Note from the committee: {note}", "Nota da comissão: {note}"),
    "m_dec_comments": ("Comentarios de los revisores (anónimos):", "Reviewers' comments (anonymous):",
                       "Comentários dos avaliadores (anônimos):"),
    "m_dec_final": ("Material final de los aceptados: hasta el 17 de octubre de 2026.",
                    "Final material for accepted works: by 17 October 2026.",
                    "Material final dos trabalhos aceitos: até 17 de outubro de 2026."),
    # blind-review flags shown to the author
    "flag_email": ("El texto contiene una dirección de correo.", "The text contains an email address.",
                   "O texto contém um endereço de e-mail."),
    "flag_author": ("El texto parece mencionar a un autor ({name}).", "The text seems to name an author ({name}).",
                    "O texto parece mencionar um autor ({name})."),
}
_IDX = {"es": 0, "en": 1, "pt": 2}


def plain(key, lang, **kw):
    """Plain text (emails, stored messages)."""
    return T[key][_IDX.get(lang, 0)].format(**kw)


def html(key, lang, **kw):
    """Markup for templates: our own strings are trusted, arguments are escaped."""
    return Markup(T[key][_IDX.get(lang, 0)]).format(**kw)


def axis_label(axis, lang):
    from .logic import AXES as ES
    return AXES[lang][ES.index(axis)] if lang in AXES and axis in ES else axis


def modality_label(key, lang):
    from .logic import MODALITIES as ES
    return MODALITIES.get(lang, ES).get(key, ES.get(key, key))


def category_label(key, lang):
    from .logic import CATEGORIES as ES
    return CATEGORIES.get(lang, ES).get(key, ES.get(key, key))


def decision_label(key, lang):
    from .logic import RECOMMENDATIONS as ES
    return DECISIONS.get(lang, ES).get(key, ES.get(key, key))
