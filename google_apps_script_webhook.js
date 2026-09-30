/**
 * GOOGLE APPS SCRIPT - WEBHOOK OFICIAL COOLPADEL & SAVE MY PLAY
 * 
 * Funciones:
 * 1. Recepción de LEADS (Email) con validación estricta y alertas inmediatas a Javier.
 * 2. ANALÍTICA DE LEADS AGRUPADA POR SESIÓN (1 FILA POR LEAD):
 *    - Geolocalización por IP (Ciudad, Región, País).
 *    - Termómetro de Interés / Lead Scoring (🔥 Muy Caliente / ⚡ Interesado / 👀 Curioso).
 *    - Detección de Copy-Paste de teléfono/email y clics de contacto.
 *    - Desglose de tiempo de atención por sección.
 *    - Cada visita/lead se consolida en SU PROPIA FILA ÚNICA.
 */

const NOTIFICAR_EMAIL = "javier@coolpadelstudios.com";

function doPost(e) {
  try {
    if (!e || !e.postData || !e.postData.contents) {
      return ContentService.createTextOutput(JSON.stringify({ status: "error", message: "Sin datos" })).setMimeType(ContentService.MimeType.JSON);
    }

    const data = JSON.parse(e.postData.contents);
    const ss = SpreadsheetApp.getActiveSpreadsheet();

    // ─────────────────────────────────────────────────────────────────
    // 1. CAPTURA DE LEAD (EMAIL / DESCARGA INFORME)
    // ─────────────────────────────────────────────────────────────────
    const esLeadEmail = data.tipo === "lead_email" || (data.email && typeof data.email === "string" && data.email.includes("@"));
    
    if (esLeadEmail) {
      const emailLimpio = (data.email || "").trim();
      if (!emailLimpio || !emailLimpio.includes("@") || emailLimpio.length < 5) {
        return ContentService.createTextOutput(JSON.stringify({ status: "ignored" })).setMimeType(ContentService.MimeType.JSON);
      }

      let sheetEmails = ss.getSheetByName("email página web");
      if (!sheetEmails) {
        sheetEmails = ss.insertSheet("email página web");
        sheetEmails.appendRow(["Fecha y Hora", "Email", "Origen", "Lead / Club", "Campaña", "Dispositivo", "Notas"]);
      }

      const ahora = Utilities.formatDate(new Date(), "Europe/Madrid", "yyyy-MM-dd HH:mm:ss");
      const origen = data.origen || "Descarga Informe";
      const leadLabel = data.lead_label || data.lead_name || data.lead_tel || "Web Directa";
      const campana = data.campana_utm || data.campana || "";
      const dispositivo = data.dispositivo || "";
      const notas = data.notas || "";

      sheetEmails.appendRow([ahora, emailLimpio, origen, leadLabel, campana, dispositivo, notas]);

      try {
        MailApp.sendEmail({
          to: NOTIFICAR_EMAIL,
          subject: "🎯 Nuevo Lead Web: " + emailLimpio + " (" + leadLabel + ")",
          body: "Nuevo lead en CoolPadel:\n\nEmail: " + emailLimpio + "\nLead: " + leadLabel + "\nOrigen: " + origen + "\nFecha: " + ahora
        });
      } catch (errMail) {}

      return ContentService.createTextOutput(JSON.stringify({ status: "success" })).setMimeType(ContentService.MimeType.JSON);
    }

    // ─────────────────────────────────────────────────────────────────
    // 2. ANALÍTICA AGRUPADA POR LEAD (16 COLUMNAS CON GEO & SCORE)
    // ─────────────────────────────────────────────────────────────────
    let sheetAnalitica = ss.getSheetByName("Analitica Web");
    if (!sheetAnalitica) {
      sheetAnalitica = ss.insertSheet("Analitica Web");
      sheetAnalitica.appendRow([
        "Fecha y Hora", "Lead / Club", "Ubicación (IP)", "Interés (Score)", "Tipo Tráfico", 
        "Acción / Eventos Realizados", "Página", "Sección Alcanzada", "% Scroll", "Tiempo Activo", 
        "Tiempos x Sección", "Dispositivo / SO", "Origen / Canal", "Campaña / Ruta", "Detalles Clave", "ID Sesión"
      ]);
    }

    const ahora = Utilities.formatDate(new Date(), "Europe/Madrid", "yyyy-MM-dd HH:mm:ss");
    const sessionId = (data.session_id || "").trim();
    const leadLabel = data.lead_label || data.lead_name || data.lead_tel || (data.es_admin ? "👤 Javier (Admin)" : "Anónimo");
    const tipoTrafico = data.tipo_trafico || (data.es_admin ? "👤 Propio (Admin)" : (data.lead_tel ? "🎯 Lead WhatsApp" : "🌐 Tráfico Web"));
    
    // Normalizar Acción actual
    let accionActual = data.evento_desc || data.evento || "Visita Web";
    if (data.evento === "pageview" || data.evento === "visita_iniciada") {
      accionActual = "🟢 Visita";
    } else if (data.evento && data.evento.indexOf("click_whatsapp") >= 0) {
      accionActual = "🎯 Clic WA (" + (data.ubicacion || "Web") + ")";
    } else if (data.evento === "calculadora_interaccion") {
      accionActual = "📊 Calc (" + (data.tier_pistas || "") + " pistas)";
    } else if (data.evento === "faq_abierto") {
      accionActual = "❓ FAQ";
    } else if (data.evento === "copiar_telefono") {
      accionActual = "📋 Copió Teléfono";
    } else if (data.evento === "copiar_email") {
      accionActual = "📋 Copió Email";
    } else if (data.evento === "scroll_hito") {
      accionActual = "📜 Scroll " + (data.scroll_hito || data.scroll_max || "");
    } else if (data.evento === "sesion_finalizada") {
      accionActual = "🏁 Fin Sesión";
    }

    const ubicacion = data.geo_ubicacion || data.zona_horaria || "España";
    const score = data.lead_score || "⚡ Interesado (B)";
    const pagina = data.pagina || data.url || "/";
    const seccion = data.seccion_actual || data.seccion || "-";
    const scrollMax = data.scroll_max || data.scroll_alcanzado || "-";
    const tiempoActivo = data.tiempo_activo || (data.tiempo_segundos ? data.tiempo_segundos + "s" : "-");
    const tiemposSeccion = data.tiempos_seccion || "-";
    const dispositivo = data.dispositivo || "";
    const origenCanal = data.origen_canal || data.referrer || "Directo";
    const campana = data.campana_utm || data.campana || "-";

    // Construir detalles clave
    let detallesArr = [];
    if (data.tier_pistas) detallesArr.push("Pistas: " + data.tier_pistas + " (" + (data.tier_precio || "") + "€/m)");
    if (data.faq_pregunta) detallesArr.push("FAQ: " + data.faq_pregunta);
    if (data.secciones_recorridas) detallesArr.push("Ruta: " + data.secciones_recorridas);
    if (data.idioma) detallesArr.push("Idioma: " + data.idioma.toUpperCase());
    const detallesStr = detallesArr.join(" | ");

    // Buscar si ya existe la sesión en las últimas 60 filas para AGRUPAR
    let filaExistente = -1;
    const lastRow = sheetAnalitica.getLastRow();
    if (sessionId && lastRow > 1) {
      const startRow = Math.max(2, lastRow - 60);
      const numRows = lastRow - startRow + 1;
      const idsRange = sheetAnalitica.getRange(startRow, 16, numRows, 1).getValues();
      for (let i = idsRange.length - 1; i >= 0; i--) {
        if (idsRange[i][0] === sessionId) {
          filaExistente = startRow + i;
          break;
        }
      }
    }

    if (filaExistente > 1) {
      // ACTUALIZAR Y CONSOLIDAR EN LA MISMA FILA DEL LEAD
      const filaActual = sheetAnalitica.getRange(filaExistente, 1, 1, 16).getValues()[0];
      
      let accionesPrevias = filaActual[5] || "";
      let accionesActualizadas = accionesPrevias;
      if (!accionesPrevias.includes(accionActual)) {
        accionesActualizadas = accionesPrevias ? accionesPrevias + " ➔ " + accionActual : accionActual;
      }

      let detallesPrevios = filaActual[14] || "";
      let detallesActualizados = detallesPrevios;
      if (detallesStr && !detallesPrevios.includes(detallesStr)) {
        detallesActualizados = detallesPrevios ? detallesPrevios + " | " + detallesStr : detallesStr;
      }

      sheetAnalitica.getRange(filaExistente, 1, 1, 16).setValues([[
        ahora,                                                   // Col 1: Fecha y Hora
        leadLabel !== "Anónimo" ? leadLabel : (filaActual[1] || leadLabel), // Col 2: Lead / Club
        ubicacion !== "España" ? ubicacion : (filaActual[2] || ubicacion),  // Col 3: Ubicación (IP)
        score !== "⚡ Interesado (B)" ? score : (filaActual[3] || score),   // Col 4: Interés (Score)
        tipoTrafico,                                             // Col 5: Tipo Tráfico
        accionesActualizadas,                                    // Col 6: Acciones
        pagina,                                                  // Col 7: Página
        seccion !== "-" ? seccion : filaActual[7],               // Col 8: Sección Alcanzada
        scrollMax !== "-" ? scrollMax : filaActual[8],           // Col 9: % Scroll
        tiempoActivo !== "-" ? tiempoActivo : filaActual[9],     // Col 10: Tiempo Activo
        tiemposSeccion !== "-" ? tiemposSeccion : filaActual[10],// Col 11: Tiempos x Sección
        dispositivo || filaActual[11],                           // Col 12: Dispositivo / SO
        origenCanal || filaActual[12],                           // Col 13: Origen / Canal
        campana !== "-" ? campana : filaActual[13],              // Col 14: Campaña / Ruta
        detallesActualizados,                                    // Col 15: Detalles Clave
        sessionId                                                // Col 16: ID Sesión
      ]]);

    } else {
      // NUEVA FILA PARA UN NUEVO LEAD
      sheetAnalitica.appendRow([
        ahora,
        leadLabel,
        ubicacion,
        score,
        tipoTrafico,
        accionActual,
        pagina,
        seccion,
        scrollMax,
        tiempoActivo,
        tiemposSeccion,
        dispositivo,
        origenCanal,
        campana,
        detallesStr,
        sessionId
      ]);
    }

    return ContentService.createTextOutput(JSON.stringify({ status: "success" })).setMimeType(ContentService.MimeType.JSON);

  } catch (error) {
    return ContentService.createTextOutput(JSON.stringify({ status: "error", error: error.toString() })).setMimeType(ContentService.MimeType.JSON);
  }
}

function doGet(e) {
  return ContentService.createTextOutput("CoolPadel Webhook Activo").setMimeType(ContentService.MimeType.TEXT);
}
