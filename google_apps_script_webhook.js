/**
 * GOOGLE APPS SCRIPT - WEBHOOK OFICIAL COOLPADEL & SAVE MY PLAY
 * 
 * Columnas Limpias y Accionables:
 * 1. Fecha: día/mes (ej: 04/10)
 * 2. Hora: HH:mm:ss (ej: 16:01:19)
 * 3. Lead / Club: Nombre/Tel si se conoce, o EN BLANCO si es anónimo
 * 4. Nº Visitas: 1ª visita, 2ª visita, 5ª visita...
 * 5. Ubicación: Madrid, Madrid, ES (Ciudad, Región, País)
 * 6. Dispositivo: iPhone, Android, Windows, Mac, iPad...
 * 7. Página: /camaras/, /, etc.
 * 8. Evento Real: Acción clara realizada (Lectura, Clic WhatsApp, Copió Teléfono...)
 * 9. Secciones Leídas: Ruta de secciones leídas en orden
 * 10. Tiempo Activo: Tiempo real de lectura (ej: 1m 14s)
 * 11. % Scroll: Porcentaje máximo de lectura (ej: 75%)
 * 12. ID Sesión: Identificador técnico de sesión para agrupar en 1 sola fila
 */

const NOTIFICAR_EMAIL = "javier@coolpadelstudios.com";

function doPost(e) {
  const lock = LockService.getScriptLock();
  try {
    lock.waitLock(10000);
  } catch (errLock) {}

  try {
    if (!e || !e.postData || !e.postData.contents) {
      return ContentService.createTextOutput(JSON.stringify({ status: "error", message: "Sin datos" })).setMimeType(ContentService.MimeType.JSON);
    }

    const data = JSON.parse(e.postData.contents);
    const ss = SpreadsheetApp.getActiveSpreadsheet();

    const ahoraDate = new Date();
    const dia = Utilities.formatDate(ahoraDate, "Europe/Madrid", "dd/MM");
    const hora = Utilities.formatDate(ahoraDate, "Europe/Madrid", "HH:mm:ss");

    // ─────────────────────────────────────────────────────────────────
    // 0. CAPTURA DE DEMO AGENDADA POR CALENDLY EN PESTAÑA 'Reuniones'
    // ─────────────────────────────────────────────────────────────────
    if (data.tipo === "reunion_calendly" || data.evento === "demo_agendada") {
      let sheetReuniones = ss.getSheetByName("Reuniones");
      if (!sheetReuniones) {
        sheetReuniones = ss.insertSheet("Reuniones");
      }
      if (sheetReuniones.getLastRow() === 0) {
        sheetReuniones.appendRow([
          "estado", "fecha", "hora_es", "pais", "hora_local", "num_lead",
          "nombre_club", "email", "cc", "titulo", "meet_link", "id_evento", "notas", "fecha_creacion"
        ]);
      }

      const fCreacion = dia + " " + hora;
      const nombreClub = data.lead_nombre || data.lead_name || data.lead_label || "Club Web";
      const telLead = data.lead_tel || "";
      const notas = "Agendada desde carta de ventas (Calendly)" + (telLead ? " | Tel: " + telLead : "");
      
      sheetReuniones.appendRow([
        "creada",
        dia,
        hora,
        "ES",
        hora + " (Madrid time)",
        telLead,
        nombreClub,
        "",
        NOTIFICAR_EMAIL,
        "Demo Save my Play - " + nombreClub,
        "",
        "",
        notas,
        fCreacion
      ]);

      try {
        MailApp.sendEmail({
          to: NOTIFICAR_EMAIL,
          subject: "🎯 DEMO AGENDADA: " + nombreClub + (telLead ? " (" + telLead + ")" : ""),
          body: "¡Nuevo club ha agendado una demo desde la carta de ventas!\n\nClub: " + nombreClub + "\nTeléfono: " + telLead + "\nFecha registro: " + dia + " " + hora + "\n\nRevisa tu Google Calendar para ver los detalles exactos."
        });
      } catch (errMail) {}
    }

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
        sheetEmails.appendRow(["Fecha", "Hora", "Email", "Origen", "Lead / Club", "Campaña", "Dispositivo"]);
      }

      const origen = data.origen || "Descarga Informe";
      const leadLabel = data.lead_label || data.lead_name || data.lead_tel || "";
      const campana = data.campana_utm || data.campana || "";
      const dispositivo = data.dispositivo || data.so || "";

      sheetEmails.insertRowBefore(2);
      sheetEmails.getRange(2, 1, 1, 7).setValues([[dia, hora, emailLimpio, origen, leadLabel, campana, dispositivo]]);

      try {
        MailApp.sendEmail({
          to: NOTIFICAR_EMAIL,
          subject: "🎯 Nuevo Lead Web: " + emailLimpio + (leadLabel ? " (" + leadLabel + ")" : ""),
          body: "Nuevo lead en CoolPadel:\n\nEmail: " + emailLimpio + "\nLead: " + leadLabel + "\nOrigen: " + origen + "\nFecha: " + dia + " " + hora
        });
      } catch (errMail) {}

      return ContentService.createTextOutput(JSON.stringify({ status: "success" })).setMimeType(ContentService.MimeType.JSON);
    }

    // ─────────────────────────────────────────────────────────────────
    // 2. ANALÍTICA LIMPIA AGRUPADA POR SESIÓN (1 FILA POR VISITA)
    // ─────────────────────────────────────────────────────────────────
    let sheetAnalitica = ss.getSheetByName("Analitica Web");
    if (!sheetAnalitica) {
      sheetAnalitica = ss.insertSheet("Analitica Web");
    }
    if (sheetAnalitica.getLastRow() === 0) {
      sheetAnalitica.appendRow([
        "Fecha", "Hora", "Lead / Club", "Visitas", "Ubicación", "Dispositivo", 
        "Página", "Evento Real", "Secciones Leídas", "Tiempo Activo", "% Scroll", "ID Sesión"
      ]);
    }

    const sessionId = (data.session_id || "").trim();
    
    // Lead / Club: EN BLANCO si es anónimo o no se sabe quién es
    let leadLabel = "";
    if (data.es_admin) {
      leadLabel = "Javier (Admin)";
    } else if (data.lead_name && data.lead_tel) {
      leadLabel = data.lead_name + " (" + data.lead_tel + ")";
    } else if (data.lead_name) {
      leadLabel = data.lead_name;
    } else if (data.lead_tel) {
      leadLabel = data.lead_tel;
    } else if (data.lead_label && !data.lead_label.startsWith("Anónimo") && !data.lead_label.startsWith("analitica_evento")) {
      leadLabel = data.lead_label;
    }

    // Nº de visitas (1ª visita, 2ª visita, 5ª visita...)
    let visitasStr = "1ª visita";
    if (data.visita_num) {
      visitasStr = data.visita_num + "ª visita";
    }

    // Ubicación
    const ubicacion = data.geo_ubicacion || data.ubicacion || "";

    // Dispositivo limpio (iPhone, Android, Windows, Mac, etc.)
    const dispositivo = data.dispositivo || data.so || "Web";

    // Página
    const pagina = data.pagina || data.url || "/camaras/";

    // Evento Real comprensible
    let eventoReal = data.evento_desc || "";
    const evt = data.evento || "";
    const tActivo = data.tiempo_activo || (data.tiempo_segundos ? data.tiempo_segundos + "s" : "0s");
    const sMax = data.scroll_max || data.scroll_hito || "0%";

    if (evt === "visita_iniciada" || evt === "pageview") {
      eventoReal = "🟢 Lectura Iniciada";
    } else if (evt === "sesion_finalizada") {
      eventoReal = "🏁 Fin Lectura (" + tActivo + ", " + sMax + ")";
    } else if (evt.indexOf("click_whatsapp") >= 0) {
      eventoReal = "🎯 Clic WhatsApp (" + (data.ubicacion || "Carta") + ")";
    } else if (evt === "copiar_telefono") {
      eventoReal = "📋 Copió Teléfono";
    } else if (evt === "copiar_email") {
      eventoReal = "📋 Copió Email";
    } else if (evt === "calculadora_interaccion") {
      eventoReal = "📊 Calculadora (" + (data.tier_pistas || "") + " pistas)";
    } else if (!eventoReal) {
      eventoReal = "Lectura (" + tActivo + ", " + sMax + ")";
    }

    // Secciones Leídas
    const seccionesLeidas = data.secciones_recorridas || data.seccion_actual || "";
    const tiempoActivo = tActivo;
    const scrollMax = sMax;

    // Buscar si ya existe la sesión en las primeras 100 filas para AGRUPAR (más recientes arriba)
    let filaExistente = -1;
    const lastRow = sheetAnalitica.getLastRow();
    if (sessionId && lastRow > 1) {
      const numRows = Math.min(lastRow - 1, 100);
      const idsRange = sheetAnalitica.getRange(2, 12, numRows, 1).getValues();
      for (let i = 0; i < idsRange.length; i++) {
        if (idsRange[i][0] === sessionId) {
          filaExistente = 2 + i;
          break;
        }
      }
    }

    if (filaExistente > 1) {
      // CONSOLIDAR EN LA SESIÓN EXISTENTE
      const filaActual = sheetAnalitica.getRange(filaExistente, 1, 1, 12).getValues()[0];
      
      // Actualizar evento real sin redundancia
      let eventosPrevios = filaActual[7] || "";
      let eventosActualizados = eventosPrevios;
      if (eventoReal && !eventosPrevios.includes(eventoReal)) {
        if (eventosPrevios.startsWith("🟢 Lectura Iniciada") && (eventoReal.startsWith("🏁 Fin Lectura") || eventoReal.startsWith("🎯 Clic"))) {
          eventosActualizados = eventoReal;
        } else {
          eventosActualizados = eventosPrevios + " ➔ " + eventoReal;
        }
      }

      const filaConsolidada = [
        dia,                                                             // Col 1: Fecha (dd/MM)
        hora,                                                            // Col 2: Hora (HH:mm:ss)
        leadLabel || filaActual[2] || "",                               // Col 3: Lead / Club (en blanco si no se conoce)
        visitasStr || filaActual[3] || "1ª visita",                      // Col 4: Visitas
        ubicacion || filaActual[4] || "",                               // Col 5: Ubicación
        dispositivo || filaActual[5] || "",                             // Col 6: Dispositivo
        pagina || filaActual[6] || "",                                  // Col 7: Página
        eventosActualizados,                                             // Col 8: Evento Real
        seccionesLeidas || filaActual[8] || "",                         // Col 9: Secciones Leídas
        tiempoActivo !== "0s" ? tiempoActivo : (filaActual[9] || tiempoActivo), // Col 10: Tiempo Activo
        scrollMax !== "0%" ? scrollMax : (filaActual[10] || scrollMax), // Col 11: % Scroll
        sessionId                                                        // Col 12: ID Sesión
      ];

      if (filaExistente === 2) {
        // Ya está en la fila 2 (arriba del todo), actualizar directamente
        sheetAnalitica.getRange(2, 1, 1, 12).setValues([filaConsolidada]);
      } else {
        // Mover a la fila 2 para mantener la sesión más reciente/activa arriba
        sheetAnalitica.deleteRow(filaExistente);
        sheetAnalitica.insertRowBefore(2);
        sheetAnalitica.getRange(2, 1, 1, 12).setValues([filaConsolidada]);
      }

    } else {
      // NUEVA SESIÓN: Insertar en la fila 2 (arriba del todo, debajo del encabezado)
      sheetAnalitica.insertRowBefore(2);
      sheetAnalitica.getRange(2, 1, 1, 12).setValues([[
        dia,
        hora,
        leadLabel,
        visitasStr,
        ubicacion,
        dispositivo,
        pagina,
        eventoReal,
        seccionesLeidas,
        tiempoActivo,
        scrollMax,
        sessionId
      ]]);
    }

    return ContentService.createTextOutput(JSON.stringify({ status: "success" })).setMimeType(ContentService.MimeType.JSON);

  } catch (error) {
    return ContentService.createTextOutput(JSON.stringify({ status: "error", error: error.toString() })).setMimeType(ContentService.MimeType.JSON);
  } finally {
    try {
      lock.releaseLock();
    } catch (errRel) {}
  }
}

function doGet(e) {
  return ContentService.createTextOutput("CoolPadel Webhook Activo").setMimeType(ContentService.MimeType.TEXT);
}
