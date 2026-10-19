/**
 * GOOGLE APPS SCRIPT - WEBHOOK OFICIAL COOLPADEL & SAVE MY PLAY
 * 
 * Columnas Limpias y Accionables (12 Columnas Estándar):
 * 1. Fecha: día/mes (ej: 17/10)
 * 2. Hora: HH:mm:ss (ej: 14:01:19)
 * 3. Lead / Club: Nombre/Tel si se conoce, o EN BLANCO si es anónimo
 * 4. Origen / Canal: WhatsApp, Email, Carta /camaras/, Blog, Home, Directo...
 * 5. Visitas: 1ª visita, 2ª visita... (con Nota emergente que despliega el historial completo)
 * 6. Ubicación: Madrid, Madrid, ES (Ciudad, Región, País)
 * 7. Dispositivo: iPhone, Android, Windows, Mac, iPad...
 * 8. Página: /camaras/, /, /blog/..., etc.
 * 9. Evento Real: Acción clara realizada (Lectura Iniciada, Fin Lectura, Clic WhatsApp...)
 * 10. Secciones Leídas: Ruta de secciones leídas en orden
 * 11. Tiempo Activo: Tiempo real de lectura (ej: 1m 14s)
 * 12. % Scroll: Porcentaje máximo de lectura (ej: 75%)
 * (El ID técnico de sesión se guarda dentro de la Nota de la celda 'Visitas', manteniendo la tabla 100% limpia)
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
        "Fecha", "Hora", "Lead / Club", "Origen / Canal", "Visitas", "Ubicación", "Dispositivo", 
        "Página", "Evento Real", "Secciones Leídas", "Tiempo Activo", "% Scroll"
      ]);
    }
    try {
      sheetAnalitica.setFrozenRows(1);
    } catch(e) {}

    // Descartar pruebas en local (file://, localhost, etc.)
    const urlRaw = ((data.url || "") + " " + (data.pagina || "") + " " + (data.path || "")).toLowerCase();
    if (urlRaw.includes("file:") || urlRaw.includes("localhost") || urlRaw.includes("127.0.0.1") || urlRaw.includes("users/javie") || urlRaw.includes("c:/users")) {
      return ContentService.createTextOutput(JSON.stringify({ status: "ignored_local", message: "Entorno local de desarrollo ignorado" })).setMimeType(ContentService.MimeType.JSON);
    }

    // Descartar visitas del Administrador (Javier)
    const leadRaw = ((data.lead_name || "") + " " + (data.lead_label || "")).toLowerCase();
    if (data.es_admin || leadRaw.includes("admin") || leadRaw.includes("javier")) {
      return ContentService.createTextOutput(JSON.stringify({ status: "ignored_admin", message: "Visita de admin ignorada" })).setMimeType(ContentService.MimeType.JSON);
    }

    // Normalizar ruta de la página
    let pagina = data.pagina || data.path || data.url || "/";
    pagina = pagina.replace(/^https?:\/\/(?:www\.)?coolpadelstudios\.com/i, "").replace(/^https?:\/\/(?:www\.)?savemyplay\.com/i, "");
    if (!pagina) pagina = "/";

    // Lead / Club: EN BLANCO si es anónimo o no se sabe quién es
    let leadLabel = "";
    if (data.lead_name && data.lead_tel) {
      leadLabel = data.lead_name + " (" + data.lead_tel + ")";
    } else if (data.lead_name) {
      leadLabel = data.lead_name;
    } else if (data.lead_tel) {
      leadLabel = data.lead_tel;
    } else if (data.lead_label && !data.lead_label.startsWith("Anónimo") && !data.lead_label.startsWith("analitica_evento")) {
      leadLabel = data.lead_label;
    }

    // Origen de acceso / Canal (Priorizar siempre buscadores orgánicos e IA sobre etiquetas estáticas de página)
    let origenCanal = (data.origen_canal || "").trim();
    const src = (data.campana_utm || data.origen || "").toLowerCase();
    const ref = (data.referrer || "").toLowerCase();
    const urlFull = (data.url_completa || data.url || "").toLowerCase();

    if (ref.includes("chatgpt.com") || ref.includes("openai.com") || src.includes("chatgpt")) {
      origenCanal = "🤖 IA: ChatGPT / SearchGPT";
    } else if (ref.includes("perplexity.ai") || src.includes("perplexity")) {
      origenCanal = "🤖 IA: Perplexity";
    } else if (ref.includes("claude.ai") || src.includes("claude")) {
      origenCanal = "🤖 IA: Claude";
    } else if (ref.includes("gemini.google.com") || ref.includes("bard.google.com")) {
      origenCanal = "🤖 IA: Google Gemini";
    } else if (ref.includes("copilot.microsoft.com")) {
      origenCanal = "🤖 IA: Microsoft Copilot";
    } else if (ref.includes("google.") || ref.includes("googlequicksearchbox") || urlFull.includes("srsltid=") || urlFull.includes("gclid=")) {
      origenCanal = "🔍 Búsqueda Google";
    } else if (ref.includes("bing.com") || ref.includes("msn.com") || urlFull.includes("msclkid=")) {
      origenCanal = "🔍 Búsqueda Bing";
    } else if (ref.includes("duckduckgo.com")) {
      origenCanal = "🔍 Búsqueda DuckDuckGo";
    } else if (ref.includes("yahoo.")) {
      origenCanal = "🔍 Búsqueda Yahoo";
    } else if (ref.includes("ecosia.org") || ref.includes("search.brave.com")) {
      origenCanal = "🔍 Búsqueda Orgánica";
    } else if (!origenCanal || origenCanal.includes("Enlace Directo")) {
      if (src.includes("whatsapp") || src.includes("wa") || data.lead_tel) {
        origenCanal = "📲 Link WhatsApp" + (data.campana_utm ? " (" + data.campana_utm + ")" : "");
      } else if (src.includes("email") || src.includes("resend")) {
        origenCanal = "✉️ Link Email";
      } else if (ref.includes("coolpadel") || ref.includes("savemyplay")) {
        origenCanal = "🌐 Desde la Web";
      } else if (pagina.indexOf("/herramientas/") >= 0) {
        origenCanal = "🛠️ Herramientas Gratuitas";
      } else if (pagina.indexOf("/camaras/") >= 0) {
        origenCanal = "🌐 Carta de Ventas (/camaras/)";
      } else if (pagina.indexOf("/blog/") >= 0) {
        origenCanal = "📝 Blog CoolPadel";
      } else if (pagina.indexOf("llaveros") >= 0 || pagina.indexOf("welcome-packs") >= 0) {
        origenCanal = "🏷️ Landing Llaveros";
      } else if (pagina.indexOf("franquicias") >= 0) {
        origenCanal = "🏢 Franquicias Padel";
      } else if (pagina === "/") {
        origenCanal = "🌐 Home (coolpadelstudios.com)";
      } else {
        origenCanal = "🌐 Enlace Directo";
      }
    }

    // Generar fallback de sesión si la página no envió session_id
    const sessionId = (data.session_id || "").trim() || ("s_" + dia.replace("/", "") + "_" + (data.dispositivo || "web").toLowerCase() + "_" + Math.random().toString(36).substring(2, 6));
    const visitorId = (data.visitor_id || "").trim();

    // Nº de visitas (1ª visita, 2ª visita, 5ª visita...)
    let visitasStr = "1ª visita";
    if (data.visita_num) {
      visitasStr = data.visita_num + "ª visita";
    }

    // Ubicación
    const ubicacion = data.geo_ubicacion || data.ubicacion || "";

    // Dispositivo limpio (iPhone, Android, Windows, Mac, etc.)
    const dispositivo = data.dispositivo || data.so || "Web";

    // Evento Real comprensible
    let eventoReal = data.evento_desc || "";
    const evt = data.evento || "";
    const tActivo = data.tiempo_activo || (data.tiempo_segundos ? data.tiempo_segundos + "s" : "0s");
    const sMax = data.scroll_max || data.scroll_hito || "0%";

    if (evt === "visita_iniciada" || evt === "pageview" || evt === "visita_blog_pagina" || evt === "page_view_landing") {
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

    // Buscar si ya existe este visitante o sesión en las primeras 120 filas
    let filaExistente = -1;
    let notaExistente = "";
    const lastRow = sheetAnalitica.getLastRow();
    
    if (lastRow > 1) {
      const numRows = Math.min(lastRow - 1, 120);
      const notasRange = sheetAnalitica.getRange(2, 5, numRows, 1).getNotes(); // Columna 5: Visitas
      const valsLead = sheetAnalitica.getRange(2, 3, numRows, 1).getValues();  // Columna 3: Lead / Club

      for (let i = 0; i < numRows; i++) {
        const n = notasRange[i][0] || "";
        const rLead = valsLead[i][0] || "";
        
        const matchSession = sessionId && n.indexOf(sessionId) >= 0;
        const matchVisitor = visitorId && n.indexOf(visitorId) >= 0;
        const matchTel = data.lead_tel && rLead.indexOf(data.lead_tel) >= 0;

        if (matchSession || matchVisitor || matchTel) {
          filaExistente = 2 + i;
          notaExistente = n;
          break;
        }
      }
    }

    if (filaExistente > 1) {
      // CONSOLIDAR EN LA SESIÓN O VISITAS ANTERIORES DEL LEAD
      const filaActual = sheetAnalitica.getRange(filaExistente, 1, 1, 12).getValues()[0];
      const isMismaSesion = sessionId && notaExistente.indexOf(sessionId) >= 0;
      
      let nuevaNota = notaExistente;

      if (!isMismaSesion) {
        // ES UNA VISITA NUEVA / REINCIDENTE DEL MISMO USUARIO:
        // Guardar la visita anterior en el historial de la nota emergente
        const prevFecha = filaActual[0] || dia;
        const prevHora = filaActual[1] || hora;
        const prevVisita = filaActual[4] || "1ª visita";
        const prevOrigen = filaActual[3] || "Web";
        const prevPagina = filaActual[7] || "/";
        const prevEvento = filaActual[8] || "-";
        const prevTiempo = filaActual[10] || "0s";
        const prevScroll = filaActual[11] || "0%";

        const entradaHistorial = "• " + prevVisita + " (" + prevFecha + " " + prevHora + "):\n" +
          "  Pág: " + prevPagina + " | Origen: " + prevOrigen + "\n" +
          "  Lectura: " + prevTiempo + " (" + prevScroll + ") ➔ " + prevEvento;

        let cuerpoNota = notaExistente.replace(/\[id:[^\]]+\]/g, "").trim();
        if (!cuerpoNota.includes("HISTORIAL DE VISITAS")) {
          cuerpoNota = "📜 HISTORIAL DE VISITAS DE ESTE LEAD:\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n" + (cuerpoNota ? cuerpoNota + "\n\n" : "");
        }
        cuerpoNota += "\n" + entradaHistorial + "\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━";

        nuevaNota = cuerpoNota + "\n[id: " + (visitorId || "v") + " | " + sessionId + "]";

      } else {
        // MISMA SESIÓN ACTIVA: asegurar IDs técnicos en la nota
        if (!nuevaNota.includes(sessionId)) {
          nuevaNota = (nuevaNota.replace(/\[id:[^\]]+\]/g, "").trim() + "\n[id: " + (visitorId || "v") + " | " + sessionId + "]").trim();
        }
      }

      // Actualizar evento real sin redundancia
      let eventosPrevios = filaActual[8] || "";
      let eventosActualizados = isMismaSesion ? eventosPrevios : eventoReal;
      if (isMismaSesion && eventoReal && !eventosPrevios.includes(eventoReal)) {
        if (eventosPrevios.startsWith("🟢 Lectura Iniciada") && (eventoReal.startsWith("🏁 Fin Lectura") || eventoReal.startsWith("🎯 Clic"))) {
          eventosActualizados = eventoReal;
        } else {
          eventosActualizados = eventosPrevios + " ➔ " + eventoReal;
        }
      }

      const filaConsolidada = [
        dia,                                                             // Col 1: Fecha (dd/MM)
        hora,                                                            // Col 2: Hora (HH:mm:ss)
        leadLabel || filaActual[2] || "",                               // Col 3: Lead / Club
        origenCanal || filaActual[3] || "🌐 Enlace Directo",            // Col 4: Origen / Canal
        visitasStr || filaActual[4] || "1ª visita",                      // Col 5: Visitas (con nota emergente al pulsar)
        ubicacion || filaActual[5] || "",                               // Col 6: Ubicación
        dispositivo || filaActual[6] || "",                             // Col 7: Dispositivo
        pagina || filaActual[7] || "",                                  // Col 8: Página
        eventosActualizados,                                             // Col 9: Evento Real
        seccionesLeidas || filaActual[9] || "",                         // Col 10: Secciones Leídas
        tiempoActivo !== "0s" ? tiempoActivo : (isMismaSesion ? (filaActual[10] || tiempoActivo) : tiempoActivo), // Col 11: Tiempo Activo
        scrollMax !== "0%" ? scrollMax : (isMismaSesion ? (filaActual[11] || scrollMax) : scrollMax) // Col 12: % Scroll
      ];

      if (filaExistente === 2) {
        // Ya está en la fila 2 (arriba del todo), actualizar directamente
        sheetAnalitica.getRange(2, 1, 1, 12).setValues([filaConsolidada]);
        sheetAnalitica.getRange(2, 5).setNote(nuevaNota);
      } else {
        // Mover a la fila 2 para mantener la sesión más reciente/activa arriba
        sheetAnalitica.deleteRow(filaExistente);
        sheetAnalitica.insertRowBefore(2);
        sheetAnalitica.getRange(2, 1, 1, 12).setValues([filaConsolidada]);
        sheetAnalitica.getRange(2, 5).setNote(nuevaNota);
      }

    } else {
      // NUEVA SESIÓN: Insertar en la fila 2 (arriba del todo, debajo del encabezado)
      const notaInicial = "📜 Primera visita registrada:\n• 1ª visita: " + dia + " " + hora + "\n  Pág: " + pagina + " | Origen: " + origenCanal + "\n[id: " + (visitorId || "v") + " | " + sessionId + "]";

      sheetAnalitica.insertRowBefore(2);
      sheetAnalitica.getRange(2, 1, 1, 12).setValues([[
        dia,
        hora,
        leadLabel,
        origenCanal,
        visitasStr,
        ubicacion,
        dispositivo,
        pagina,
        eventoReal,
        seccionesLeidas,
        tiempoActivo,
        scrollMax
      ]]);
      sheetAnalitica.getRange(2, 5).setNote(notaInicial);
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

/**
 * MENÚ Y VISOR DE HISTORIAL EN GOOGLE SHEETS
 * Permite ver las visitas anteriores tanto al pulsar sobre la celda (nota emergente)
 * como seleccionando la fila y haciendo clic en 'Analítica Web > Ver Historial'.
 */
function onOpen() {
  try {
    SpreadsheetApp.getUi()
      .createMenu("📊 Analítica Web")
      .addItem("🔍 Ver Historial del Lead Seleccionado", "verHistorialSeleccionado")
      .addToUi();
  } catch (e) {}
}

function verHistorialSeleccionado() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const sheet = ss.getActiveSheet();
  if (sheet.getName() !== "Analitica Web") {
    SpreadsheetApp.getUi().alert("Por favor sitúate en la pestaña 'Analitica Web' primero.");
    return;
  }
  const row = sheet.getActiveCell().getRow();
  if (row <= 1) {
    SpreadsheetApp.getUi().alert("Por favor selecciona una fila de visita para ver su historial.");
    return;
  }
  const rowVals = sheet.getRange(row, 1, 1, 12).getValues()[0];
  const nota = sheet.getRange(row, 5).getNote();
  const lead = rowVals[2] || "Visitante Anónimo";
  const visitas = rowVals[4] || "1ª visita";
  const textoLimpio = nota ? nota.replace(/\[id:[^\]]+\]/g, "").trim() : "Primera visita registrada (" + rowVals[0] + " " + rowVals[1] + ")";

  SpreadsheetApp.getUi().alert(
    "Historial de Visitas - " + lead + " (" + visitas + ")",
    textoLimpio,
    SpreadsheetApp.getUi().ButtonSet.OK
  );
}

