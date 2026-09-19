/**
 * SICVEC 2026 — creates the three Google Forms of the plan (docs/02_google_forms_plan.md).
 * Source of the fields: 04_Inscripcion/Formularios/Especificacion_Formularios.md.
 * Run createSicvecForms() once from the account insilico@unisucre.edu.co.
 * All three forms are created CLOSED (not accepting responses); open them by hand after
 * filling the [PENDIENTE] texts. Links are written to the execution log.
 * Limits of Apps Script: it cannot add a file-upload question, so the payment receipt is sent by
 * email, and it cannot create the reviewer Sheet (IMPORTRANGE needs a manual permission click).
 */
var EJES = [
  'Economía Circular',
  'Química Verde y Procesos Sostenibles',
  'Biotecnología Sostenible',
  'Tecnologías Verdes y Energías Renovables',
  'Sostenibilidad en Cadenas de Suministro',
  'Política Pública y Gobernanza Ambiental'
];
var CONSENT = 'Autorizo el tratamiento de mis datos personales. [PENDIENTE: texto oficial de la política de tratamiento de datos de UNISUCRE]';

function createSicvecForms() {
  var a = formA_();
  var b = formB_();
  var c = formC_();
  // Form A closes at the call deadline (approximate: time triggers do not fire to the minute).
  PropertiesService.getScriptProperties().setProperty('FORM_A_ID', a.getId());
  ScriptApp.newTrigger('closeFormA_').timeBased().at(new Date('2026-10-04T23:59:00-05:00')).create();
  Logger.log('FORM A edit: ' + a.getEditUrl() + '\nFORM A public: ' + a.getPublishedUrl());
  Logger.log('FORM B edit: ' + b.getEditUrl() + '\nFORM B public: ' + b.getPublishedUrl());
  Logger.log('FORM C edit: ' + c.getEditUrl() + '\nFORM C public: ' + c.getPublishedUrl());
}

function closeFormA_() {
  var id = PropertiesService.getScriptProperties().getProperty('FORM_A_ID');
  FormApp.openById(id).setAcceptingResponses(false);
}

function base_(title, description) {
  var f = FormApp.create(title);
  f.setDescription(description);
  f.setAllowResponseEdits(false);
  f.setShowLinkToRespondAgain(false);
  return f;
}

function text_(f, title, required, help) {
  var i = f.addTextItem().setTitle(title).setRequired(required);
  if (help) i.setHelpText(help);
  return i;
}

function email_(f, title) {
  var i = f.addTextItem().setTitle(title).setRequired(true);
  i.setValidation(FormApp.createTextValidation().requireTextIsEmail().build());
  return i;
}

function choice_(f, title, values, required) {
  return f.addMultipleChoiceItem().setTitle(title).setChoiceValues(values).setRequired(required);
}

function consent_(f) {
  return f.addCheckboxItem().setTitle('Tratamiento de datos personales')
    .setChoiceValues([CONSENT]).setRequired(true);
}

function formA_() {
  var f = base_('SICVEC 2026 — Envío de resúmenes / Abstract submission',
    'Simposio Internacional de Ciencia Verde y Economía Circular. Cierre: 4 de octubre de 2026, 23:59 (hora Colombia). ' +
    'El resumen se pega como texto y NO debe incluir nombres de autores ni afiliaciones (revisión ciega). ' +
    'Ponencia oral: máx. 300 palabras; póster: máx. 250; taller práctico: propuesta descriptiva de máx. 500.');
  f.setConfirmationMessage('Hemos recibido su resumen. Su referencia será enviada por correo. El cierre es el 4 de octubre de 2026 a las 23:59 (hora Colombia); la notificación se envía el 8-9 de octubre.');
  email_(f, 'Correo de contacto');
  var t = f.addTextItem().setTitle('Título del trabajo').setRequired(true);
  t.setValidation(FormApp.createTextValidation().requireTextLengthLessThanOrEqualTo(200).build());
  choice_(f, 'Idioma del resumen', ['Español', 'English'], true);
  choice_(f, 'Modalidad', ['Ponencia oral (20 min)', 'Póster científico (90 × 120 cm)', 'Taller práctico'], true);
  choice_(f, 'Presentación', ['Presencial', 'Virtual'], true);
  choice_(f, 'Eje temático principal', EJES, true);
  var r = f.addParagraphTextItem().setTitle('Resumen (sin nombres de autores ni afiliaciones)').setRequired(true)
    .setHelpText('Oral: máx. 300 palabras. Póster: máx. 250. Taller: máx. 500. Se verifica en la revisión de admisibilidad.');
  r.setValidation(FormApp.createParagraphTextValidation().requireTextLengthLessThanOrEqualTo(3600).build());
  text_(f, 'Palabras clave (3 a 5, separadas por comas)', true);
  f.addSectionHeaderItem().setTitle('Autor que presenta (autor 1)');
  text_(f, 'Nombre completo', true);
  text_(f, 'Institución', true);
  text_(f, 'Programa académico o profesión', true);
  text_(f, 'País de procedencia', true);
  f.addParagraphTextItem().setTitle('Otros autores (opcional; máximo 5 autores en total)')
    .setHelpText('Un autor por línea: nombre, institución.');
  consent_(f);
  f.addCheckboxItem().setTitle('Declaración de originalidad').setRequired(true)
    .setChoiceValues(['El trabajo es original y no está en evaluación en otro evento.']);
  f.setDestination(FormApp.DestinationType.SPREADSHEET, SpreadsheetApp.create('SICVEC 2026 — Respuestas Envío de resúmenes (maestro)').getId());
  f.setAcceptingResponses(false);
  return f;
}

function formB_() {
  var f = base_('SICVEC 2026 — Inscripción / Registration',
    'Simposio Internacional de Ciencia Verde y Economía Circular, 19-20 de octubre de 2026, Sincelejo. ' +
    'Tarifas: pregrado COP 20.000, posgrado COP 30.000, profesionales COP 40.000. Límite de pago: 15 de octubre de 2026. ' +
    'Datos para la transferencia: [PENDIENTE: banco, cuenta, titular]. Envíe el comprobante a [PENDIENTE: correo de inscripciones].');
  f.setConfirmationMessage('Hemos recibido su inscripción. Recuerde enviar el comprobante de pago antes del 15 de octubre de 2026.');
  text_(f, 'Nombre completo', true);
  email_(f, 'Correo electrónico');
  text_(f, 'Teléfono', true);
  text_(f, 'Documento de identidad (tipo y número)', true, 'Se usa para el certificado.');
  text_(f, 'Institución', true);
  text_(f, 'País', true);
  choice_(f, 'Categoría', ['Pregrado — COP 20.000', 'Posgrado — COP 30.000', 'Profesional — COP 40.000',
    'Asistencia virtual (cupos en línea)'], true);
  choice_(f, 'Modalidad de asistencia', ['Presencial', 'Virtual'], true);
  choice_(f, '¿Presenta un trabajo?', ['No', 'Sí'], true);
  text_(f, 'Referencia del resumen (SICVEC-###), si presenta trabajo', false);
  text_(f, 'Referencia o fecha de la transferencia (categorías de pago)', false,
    'Envíe el comprobante por correo a [PENDIENTE: correo de inscripciones].');
  consent_(f);
  f.setDestination(FormApp.DestinationType.SPREADSHEET, SpreadsheetApp.create('SICVEC 2026 — Respuestas Inscripción').getId());
  f.setAcceptingResponses(false);
  return f;
}

function formC_() {
  var f = base_('SICVEC 2026 — Evaluación científica (revisores)',
    'Un formulario por resumen. Escala: 1 Insuficiente, 2 Deficiente, 3 Aceptable, 4 Bueno, 5 Excelente. ' +
    'Ponderación: relevancia 25 %, originalidad 25 %, calidad científica 25 %, claridad 15 %, impacto 10 %. Plazo: 7 de octubre de 2026.');
  f.setConfirmationMessage('Evaluación registrada. Gracias.');
  email_(f, 'Correo del revisor');
  text_(f, 'Referencia del resumen (SICVEC-###)', true);
  var crit = ['Relevancia al evento (25 %)', 'Originalidad e innovación (25 %)', 'Calidad científica (25 %)',
    'Claridad y redacción (15 %)', 'Impacto potencial (10 %)'];
  crit.forEach(function (c) {
    f.addScaleItem().setTitle(c).setBounds(1, 5).setLabels('Insuficiente', 'Excelente').setRequired(true);
  });
  f.addParagraphTextItem().setTitle('Comentarios para los autores').setRequired(true);
  choice_(f, 'Recomendación', ['Aceptado', 'Aceptado con cambios', 'Rechazado'], true);
  f.addCheckboxItem().setTitle('Confidencialidad y conflicto de interés').setRequired(true).setChoiceValues([
    'Mantengo la confidencialidad de la identidad de los autores.',
    'No tengo conflicto de interés con los autores.',
    'Mi evaluación es objetiva y no la compartiré con personas no autorizadas.']);
  f.setDestination(FormApp.DestinationType.SPREADSHEET, SpreadsheetApp.create('SICVEC 2026 — Respuestas Evaluación (maestro)').getId());
  f.setAcceptingResponses(false);
  return f;
}
