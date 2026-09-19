# Especificación de formularios — SICVEC 2026

Crear con la cuenta institucional `insilico@unisucre.edu.co` (decidido AC 19 sept). Idioma del formulario: español; título y
descripción en español e inglés. Origen de los campos: `Guia_Presentacion_Resumenes.tex`,
`Rubrica_PeerReview.tex`, `TAREAS.md`. Los valores `[PENDIENTE]` no están en el repo.

## Formulario A — Envío de resúmenes (abierto sin iniciar sesión)

Configuración: no exigir inicio de sesión; recoger correo; mensaje de confirmación con el texto de la
sección "Confirmación" del final; cierre 4 oct 2026 23:59 (hora Colombia).

| # | Campo | Tipo | Regla |
|---|---|---|---|
| 1 | Correo de contacto | correo | obligatorio |
| 2 | Título del trabajo | texto corto | obligatorio, máx. 200 caracteres |
| 3 | Idioma del resumen | opción | Español / English |
| 4 | Modalidad | opción | Ponencia oral (20 min) / Póster científico (90×120 cm) |
| 5 | Presentación | opción | Presencial / Virtual |
| 6 | Eje temático principal | opción | los seis ejes: Economía Circular; Química Verde y Procesos Sostenibles; Biotecnología Sostenible; Tecnologías Verdes y Energías Renovables; Sostenibilidad en Cadenas de Suministro; Política Pública y Gobernanza Ambiental |
| 7 | Resumen (sin nombres de autores ni afiliaciones) | párrafo | obligatorio, máx. 3.600 caracteres; oral 300 palabras, póster 250 (se verifica en admisibilidad) |
| 8 | Palabras clave (3 a 5, separadas por comas) | texto corto | obligatorio |
| 9 | Autor 1: nombre, institución, programa o profesión, país | texto corto ×4 | obligatorio; autor que presenta |
| 10 | Autores 2 a 5 (opcionales): nombre, institución | párrafo | máx. 5 autores en total |
| 11 | Autorización de tratamiento de datos | casilla | obligatorio; texto `[PENDIENTE: política de UNISUCRE]` |
| 12 | Declaración de originalidad | casilla | "El trabajo es original y no está en evaluación en otro evento" |

## Formulario B — Inscripción

| # | Campo | Tipo | Regla |
|---|---|---|---|
| 1 | Nombre completo, correo, teléfono | texto | obligatorio |
| 2 | Documento de identidad (tipo y número) | texto | obligatorio (para el certificado) |
| 3 | Institución y país | texto | obligatorio |
| 4 | Categoría | opción | Pregrado COP 20.000 / Posgrado COP 30.000 / Profesional COP 40.000 / Asistencia virtual gratuita (número de cupos por confirmar, ver pregunta abierta 4 del plan 02) |
| 5 | Modalidad de asistencia | opción | Presencial / Virtual |
| 6 | Presenta trabajo | opción | No / Sí (referencia SICVEC-###) |
| 7 | Comprobante de pago | subir archivo (PDF/imagen) | solo categorías de pago; pide inicio de sesión de Google |
| 8 | Datos para la transferencia | texto de ayuda | `[PENDIENTE: banco, cuenta, titular]`; límite de pago 15 oct 2026 |
| 9 | Autorización de tratamiento de datos | casilla | obligatorio |

Alternativa sin inicio de sesión: pedir el comprobante por correo a `[PENDIENTE: correo de inscripciones]`.

## Formulario C — Evaluación de revisores (una respuesta por resumen)

| # | Campo | Tipo |
|---|---|---|
| 1 | Correo del revisor | correo |
| 2 | Referencia del resumen (SICVEC-###) | texto corto |
| 3 | Relevancia al evento (25 %) | escala 1-5 |
| 4 | Originalidad e innovación (25 %) | escala 1-5 |
| 5 | Calidad científica (25 %) | escala 1-5 |
| 6 | Claridad y redacción (15 %) | escala 1-5 |
| 7 | Impacto potencial (10 %) | escala 1-5 |
| 8 | Comentarios para los autores | párrafo |
| 9 | Recomendación | opción: Aceptado / Aceptado con cambios / Rechazado |
| 10 | Confidencialidad y conflicto de interés | casillas obligatorias: mantengo la confidencialidad; no tengo conflicto de interés con los autores; mi evaluación es objetiva y no la compartiré |

Escala 1 = Insuficiente, 2 = Deficiente, 3 = Aceptable, 4 = Bueno, 5 = Excelente (texto de la rúbrica).

## Confirmación (mensaje tras enviar el Formulario A)

"Hemos recibido su resumen. Su referencia será enviada por correo. El cierre es el 4 de octubre de 2026
a las 23:59 (hora Colombia); la notificación se envía el 8-9 de octubre."
