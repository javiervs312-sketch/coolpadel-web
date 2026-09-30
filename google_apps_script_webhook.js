/**
 * GOOGLE APPS SCRIPT - WEBHOOK OFICIAL COOLPADEL & SAVE MY PLAY
 * 
 * Funciones:
 * 1. Recepción de LEADS (Email) con validación estricta y alertas inmediatas por correo a Javier.
 * 2. ANALÍTICA WEB COMERCIAL AVANZADA:
 *    - Diferenciación automática de tráfico de Javier (Admin) vs Clientes/Leads.
 *    - Atribución de quién entra (Nombre del club, teléfono, campaña de WhatsApp/Email).
 *    - Medición de Scroll real por secciones (Hero, Calculadora, Save my Play, FAQ, Cámaras).
 *    - Registro de interacción con la calculadora (cuántas pistas y precio calculó).
 *    - Registro de preguntas FAQ que abrió el usuario.
 *    - Medición de tiempo activo real (Attention Time).
 *    - Detección precisa de dispositivo (Móvil/PC, iPhone, Android, WhatsApp Browser).
 * 
 * Instrucciones de instalación / actualización:
 * 1. En Google Sheets, ve a: Extensiones > Apps Script.
 * 2. Pega este código reemplazando todo lo anterior.
 * 3. Pulsa "Implementar" > "Gestionar implementaciones" > Editar (icono lápiz) > "Nueva versión" > "Implementar".
 * 4. (Opcional): Ejecuta la función `configurarHojaAnalitica` una vez para darle formato profesional con colores a la hoja.
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
    // 1. CAPTURA DE LEAD (EMAIL / DESCARGA INFORME)
    // ─────────────────────────────────────────────────────────────────
    const esLeadEmail = data.tipo === "lead_email" || (data.email && typeof data.email === "string" && data.email.trim().includes("@"));
    
    if (esLeadEmail) {
      const emailLimpio = (data.email || "").trim();
      
      // Filtro de seguridad
      if (!emailLimpio || !emailLimpio.includes("@") || emailLimpio.length < 5) {
        return ContentService.createTextOutput(JSON.stringify({ status: "ignored", message: "Email no válido o vacío" }))
          .setMimeType(ContentService.MimeType.JSON);
      }

      let sheetEmails = ss.getSheetByName("email página web");
      if (!sheetEmails) {
        sheetEmails = ss.insertSheet("email página web");
        sheetEmails.appendRow(["Fecha y Hora", "Email", "Origen", "Lead / Club", "Campaña", "Dispositivo", "Notas"]);
        formatearCabecera(sheetEmails, "#0f172a", "#ffffff");
      }

      const ahora = Utilities.formatDate(new Date(), "Europe/Madrid", "yyyy-MM-dd HH:mm:ss");
      const origen = data.origen || "Descarga Reportaje Industria Padel 2026";
      const leadLabel = data.lead_label || data.lead_name || data.lead_tel || "Web Directa";
      const campana = data.campana_utm || data.campana || "";
      const dispositivo = data.dispositivo || "";
      const notas = data.notas || "";

      // Guardar fila en el Sheet
      sheetEmails.appendRow([ahora, emailLimpio, origen, leadLabel, campana, dispositivo, notas]);

      // Enviar Alerta por Correo a Javier
      try {
        const asunto = "🎯 Nuevo Lead Web CoolPadel: " + emailLimpio + (leadLabel !== "Web Directa" ? " (" + leadLabel + ")" : "");
        const cuerpoTexto = "¡Hola Javier!\n\n" +
          "Acaban de introducir un nuevo correo en la web de CoolPadel:\n\n" +
          "📧 Email: " + emailLimpio + "\n" +
          "👤 Lead / Club: " + leadLabel + "\n" +
          "📍 Origen: " + origen + "\n" +
          "📱 Dispositivo: " + dispositivo + "\n" +
          "⏰ Fecha: " + ahora + " (Hora Madrid)\n\n" +
          "Puedes consultar todos los leads en la pestaña 'email página web' de tu Google Sheet.\n\n" +
          "— Sistema Automatizado CoolPadel";

        const cuerpoHtml = "<div style='font-family: Arial, sans-serif; max-width: 600px; padding: 22px; border: 1px solid #e2e8f0; border-radius: 12px; background-color: #ffffff;'>" +
          "<h2 style='color: #0b1626; margin-top: 0;'>🎯 Nuevo Lead en CoolPadel</h2>" +
          "<p style='font-size: 15px; color: #334155;'>Alguien acaba de solicitar información o descargar el informe en la web:</p>" +
          "<div style='background-color: #f8fafc; border-left: 4px solid #f2920b; padding: 15px; border-radius: 6px; margin: 15px 0;'>" +
            "<p style='margin: 4px 0; font-size: 16px;'><strong>📧 Email:</strong> <span style='color: #0284c7; font-weight: bold;'>" + emailLimpio + "</span></p>" +
            "<p style='margin: 4px 0; font-size: 14px;'><strong>👤 Lead / Club:</strong> " + leadLabel + "</p>" +
            "<p style='margin: 4px 0; font-size: 14px;'><strong>📍 Origen:</strong> " + origen + "</p>" +
            "<p style='margin: 4px 0; font-size: 14px;'><strong>📱 Dispositivo:</strong> " + dispositivo + "</p>" +
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
    // 2. ANALÍTICA DE SESIONES Y EVENTOS COMERCIALES
    // ─────────────────────────────────────────────────────────────────
    let sheetAnalitica = ss.getSheetByName("Analitica Web");
    if (!sheetAnalitica) {
      sheetAnalitica = ss.insertSheet("Analitica Web");
      crearCabecerasAnalitica(sheetAnalitica);
    }

    const ahora = Utilities.formatDate(new Date(), "Europe/Madrid", "yyyy-MM-dd HH:mm:ss");
    
    // Extracción y formateo inteligente de datos
    const leadLabel = data.lead_label || data.lead_name || data.lead_tel || (data.es_admin ? "👤 Javier (Admin)" : "Anónimo");
    const tipoTrafico = data.tipo_trafico || (data.es_admin ? "👤 Propio (Admin)" : (data.lead_tel ? "🎯 Lead WhatsApp" : "🌐 Tráfico Web"));
    
    // Normalizar Acción / Evento con emojis para legibilidad instantánea
    let eventoFormateado = data.evento_desc || data.evento || "Visita Web";
    if (data.evento === "pageview" || data.evento === "visita_iniciada") {
      eventoFormateado = "🟢 Visita Web";
    } else if (data.evento && data.evento.startsWith("click_whatsapp")) {
      eventoFormateado = "🎯 Clic WhatsApp (" + (data.ubicacion || data.evento.replace("click_whatsapp_", "")) + ")";
    } else if (data.evento === "calculadora_interaccion") {
      eventoFormateado = "📊 Interacción Calculadora";
    } else if (data.evento === "faq_abierto") {
      eventoFormateado = "❓ Pregunta FAQ Abierta";
    } else if (data.evento === "scroll_hito") {
      eventoFormateado = "📜 Scroll " + (data.scroll_hito || data.scroll_max || "");
    } else if (data.evento === "sesion_finalizada") {
      eventoFormateado = "🏁 Fin de Sesión";
    }

    const pagina = data.pagina || data.url || "/";
    const seccion = data.seccion_actual || data.seccion || "-";
    const scrollMax = data.scroll_max || data.scroll_alcanzado || "-";
    const tiempoActivo = data.tiempo_activo || (data.tiempo_segundos ? data.tiempo_segundos + "s" : "-");
    const dispositivo = data.dispositivo || "";
    const origenCanal = data.origen_canal || data.referrer || "Directo";
    const campana = data.campana_utm || data.campana || "-";
    const sessionId = data.session_id || "";

    // Construir bloque de detalles legibles
    let detallesArr = [];
    if (data.tier_pistas) detallesArr.push("Pistas: " + data.tier_pistas + " (" + (data.tier_precio || "") + "€/mes)");
    if (data.faq_pregunta) detallesArr.push("FAQ: " + data.faq_pregunta);
    if (data.secciones_recorridas) detallesArr.push("Ruta: " + data.secciones_recorridas);
    if (data.idioma) detallesArr.push("Idioma: " + data.idioma.toUpperCase());
    if (data.resolucion) detallesArr.push("Res: " + data.resolucion);
    if (data.visita_num && data.visita_num > 1) detallesArr.push("Visita #" + data.visita_num);
    const detallesStr = detallesArr.join(" | ");

    // Insertar fila
    sheetAnalitica.appendRow([
      ahora,
      leadLabel,
      tipoTrafico,
      eventoFormateado,
      pagina,
      seccion,
      scrollMax,
      tiempoActivo,
      dispositivo,
      origenCanal,
      campana,
      detallesStr,
      sessionId
    ]);

    return ContentService.createTextOutput(JSON.stringify({ status: "success", tipo: "analitica_guardada" }))
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

/**
 * Crea y formatea las cabeceras de la hoja de analítica
 */
function crearCabecerasAnalitica(sheet) {
  const headers = [
    "Fecha y Hora", 
    "Lead / Club", 
    "Tipo Tráfico", 
    "Acción / Evento", 
    "Página", 
    "Sección Alcanzada", 
    "% Scroll", 
    "Tiempo Activo", 
    "Dispositivo / SO", 
    "Origen / Canal", 
    "Campaña / Ruta", 
    "Detalles Clave", 
    "ID Sesión"
  ];
  sheet.appendRow(headers);
  formatearCabecera(sheet, "#0f172a", "#38bdf8");
}

/**
 * Función para dar estilo profesional a las hojas
 */
function formatearCabecera(sheet, colorFondo, colorTexto) {
  try {
    const range = sheet.getRange(1, 1, 1, sheet.getLastColumn());
    range.setBackground(colorFondo);
    range.setFontColor(colorTexto);
    range.setFontWeight("bold");
    range.setFontSize(10);
    range.setHorizontalAlignment("center");
    sheet.setFrozenRows(1);
    sheet.setRowHeight(1, 32);
    
    // Auto-ajustar anchos
    for (let c = 1; c <= sheet.getLastColumn(); c++) {
      sheet.autoResizeColumn(c);
    }
  } catch(e) {}
}

/**
 * UTILIDAD MANUAL: Ejecuta esta función desde Apps Script para embellecer la pestaña 'Analitica Web'
 */
function configurarHojaAnalitica() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  let sheet = ss.getSheetByName("Analitica Web");
  if (!sheet) {
    sheet = ss.insertSheet("Analitica Web");
    crearCabecerasAnalitica(sheet);
  } else {
    // Si la primera fila no tiene las nuevas cabeceras, crearlas
    const primeraCelda = sheet.getRange(1, 1).getValue();
    if (!primeraCelda) {
      crearCabecerasAnalitica(sheet);
    }
  }
  
  formatearCabecera(sheet, "#0f172a", "#38bdf8");
  
  // Establecer anchos amigables
  const anchos = [150, 220, 150, 190, 110, 170, 90, 110, 220, 160, 130, 280, 130];
  anchos.forEach((ancho, i) => {
    if (i + 1 <= sheet.getMaxColumns()) {
      sheet.setColumnWidth(i + 1, ancho);
    }
  });
  
  SpreadsheetApp.getUi().alert("✅ Pestaña 'Analitica Web' configurada y formateada con éxito.");
}
