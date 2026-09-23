/**
 * GOOGLE APPS SCRIPT - WEBHOOK OFICIAL COOLPADEL & SAVE MY PLAY
 * 
 * Funciones:
 * 1. Recepción de LEADS (Email) con validación estricta (no guarda filas vacías).
 * 2. ENVÍO DE CORREO INMEDIATO a Javier cada vez que alguien introduce su email.
 * 3. Recepción de ANALÍTICAS (visitas, clics WhatsApp, scroll, tiempo) sin ensuciar la pestaña de emails.
 * 
 * Instrucciones de instalación:
 * 1. En Google Sheets, ve a: Extensiones > Apps Script.
 * 2. Pega este código reemplazando todo lo anterior.
 * 3. Pulsa "Implementar" > "Gestionar implementaciones" > Editar (icono lápiz) > "Nueva versión" > "Implementar".
 */

const NOTIFICAR_EMAIL = "javier@coolpadelstudios.com"; // Email de Javier donde recibir alertas
const EMAIL_BACKUP = "javiervilloriasoleto@gmail.com";  // Email backup opcional

function doPost(e) {
  try {
    if (!e || !e.postData || !e.postData.contents) {
      return ContentService.createTextOutput(JSON.stringify({ status: "error", message: "Sin datos" }))
        .setMimeType(ContentService.MimeType.JSON);
    }

    const data = JSON.parse(e.postData.contents);
    const ss = SpreadsheetApp.getActiveSpreadsheet();

    // ─────────────────────────────────────────────────────────────────
    // 1. CASO: CAPTURA DE LEAD (EMAIL)
    // ─────────────────────────────────────────────────────────────────
    const esLeadEmail = data.tipo === "lead_email" || (data.email && typeof data.email === "string" && data.email.trim().includes("@"));
    
    if (esLeadEmail) {
      const emailLimpio = (data.email || "").trim();
      
      // FILTRO DE SEGURIDAD: Nunca guardar si el email está vacío o no tiene formato válido
      if (!emailLimpio || !emailLimpio.includes("@") || emailLimpio.length < 5) {
        return ContentService.createTextOutput(JSON.stringify({ status: "ignored", message: "Email no válido o vacío" }))
          .setMimeType(ContentService.MimeType.JSON);
      }

      let sheetEmails = ss.getSheetByName("email página web");
      if (!sheetEmails) {
        sheetEmails = ss.insertSheet("email página web");
        sheetEmails.appendRow(["Fecha y Hora", "Email", "Origen", "Notas"]);
      }

      const ahora = Utilities.formatDate(new Date(), "Europe/Madrid", "yyyy-MM-dd HH:mm:ss");
      const origen = data.origen || "Descarga Reportaje Industria Padel 2026";
      const notas = data.notas || "";

      // 1.1 Guardar fila en el Sheet
      sheetEmails.appendRow([ahora, emailLimpio, origen, notas]);

      // 1.2 Enviar Alerta por Correo a Javier
      try {
        const asunto = "🎯 Nuevo Lead Web CoolPadel: " + emailLimpio;
        const cuerpoTexto = "¡Hola Javier!\n\n" +
          "Acaban de introducir un nuevo correo en la web de CoolPadel:\n\n" +
          "📧 Email: " + emailLimpio + "\n" +
          "📍 Origen: " + origen + "\n" +
          "⏰ Fecha: " + ahora + " (Hora Madrid)\n\n" +
          "Puedes consultar todos los leads en la pestaña 'email página web' de tu Google Sheet.\n\n" +
          "— Sistema Automatizado CoolPadel";

        const cuerpoHtml = "<div style='font-family: Arial, sans-serif; max-width: 600px; padding: 20px; border: 1px solid #e2e8f0; border-radius: 12px; background-color: #ffffff;'>" +
          "<h2 style='color: #0b1626; margin-top: 0;'>🎯 Nuevo Lead en CoolPadel</h2>" +
          "<p style='font-size: 15px; color: #334155;'>Alguien acaba de solicitar información o descargar el informe en la web:</p>" +
          "<div style='background-color: #f8fafc; border-left: 4px solid #f2920b; padding: 15px; border-radius: 6px; margin: 15px 0;'>" +
            "<p style='margin: 4px 0; font-size: 16px;'><strong>📧 Email:</strong> <span style='color: #0284c7; font-weight: bold;'>" + emailLimpio + "</span></p>" +
            "<p style='margin: 4px 0; font-size: 14px;'><strong>📍 Origen:</strong> " + origen + "</p>" +
            "<p style='margin: 4px 0; font-size: 14px;'><strong>⏰ Fecha:</strong> " + ahora + "</p>" +
          "</div>" +
          "<p style='font-size: 13px; color: #64748b;'>Este lead ya ha quedado registrado en la pestaña <em>'email página web'</em> del Google Sheet.</p>" +
          "</div>";

        MailApp.sendEmail({
          to: NOTIFICAR_EMAIL,
          subject: asunto,
          body: cuerpoTexto,
          htmlBody: cuerpoHtml
        });
      } catch (errMail) {
        console.error("Error enviando alerta por email:", errMail);
      }

      return ContentService.createTextOutput(JSON.stringify({ status: "success", tipo: "lead_guardado" }))
        .setMimeType(ContentService.MimeType.JSON);
    }

    // ─────────────────────────────────────────────────────────────────
    // 2. CASO: EVENTOS DE ANALÍTICA (VISITAS, CLICS, SCROLL, TIEMPO)
    // ─────────────────────────────────────────────────────────────────
    if (data.tipo === "analitica_evento" || data.tipo === "analitica_camaras") {
      let sheetAnalitica = ss.getSheetByName("Analitica Web");
      if (!sheetAnalitica) {
        sheetAnalitica = ss.insertSheet("Analitica Web");
        sheetAnalitica.appendRow([
          "Fecha y Hora", "Tipo", "Evento", "Página / URL", "Dispositivo", 
          "Tiempo", "Scroll", "Idioma", "Referrer", "Zona Horaria", "Extra"
        ]);
      }

      const ahora = Utilities.formatDate(new Date(), "Europe/Madrid", "yyyy-MM-dd HH:mm:ss");
      const evento = data.evento || "evento";
      const tipo = data.tipo;
      const paginaUrl = data.url || data.pagina || "";
      const dispositivo = data.dispositivo || "";
      const tiempo = data.tiempo_formato || (data.tiempo_segundos ? data.tiempo_segundos + "s" : "");
      const scroll = data.scroll_max || data.scroll_alcanzado || "";
      const idioma = data.idioma || "";
      const referrer = data.referrer || "";
      const zonaHoraria = data.zona_horaria || "";
      
      const copiaData = Object.assign({}, data);
      delete copiaData.tipo;
      delete copiaData.evento;
      delete copiaData.url;
      delete copiaData.pagina;
      delete copiaData.dispositivo;
      delete copiaData.tiempo_formato;
      delete copiaData.tiempo_segundos;
      delete copiaData.scroll_max;
      delete copiaData.scroll_alcanzado;
      delete copiaData.idioma;
      delete copiaData.referrer;
      delete copiaData.zona_horaria;
      delete copiaData.fecha;

      const extraJson = Object.keys(copiaData).length > 0 ? JSON.stringify(copiaData) : "";

      sheetAnalitica.appendRow([
        ahora, tipo, evento, paginaUrl, dispositivo, tiempo, scroll, idioma, referrer, zonaHoraria, extraJson
      ]);

      return ContentService.createTextOutput(JSON.stringify({ status: "success", tipo: "analitica_guardada" }))
        .setMimeType(ContentService.MimeType.JSON);
    }

    return ContentService.createTextOutput(JSON.stringify({ status: "ignored", message: "Tipo no reconocido" }))
      .setMimeType(ContentService.MimeType.JSON);

  } catch (error) {
    console.error("Error en doPost:", error);
    return ContentService.createTextOutput(JSON.stringify({ status: "error", error: error.toString() }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}

function doGet(e) {
  return ContentService.createTextOutput("CoolPadel & Save my Play Webhook Activo")
    .setMimeType(ContentService.MimeType.TEXT);
}
