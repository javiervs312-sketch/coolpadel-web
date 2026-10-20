/**
 * GOOGLE APPS SCRIPT - WEBHOOK OFICIAL COOLPADEL & SAVE MY PLAY
 * 
 * Columnas Limpias y Accionables (12 Columnas Estándar):
 * 1. Fecha: día/mes (ej: 20/10)
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
    if (!e) {
      return ContentService.createTextOutput(JSON.stringify({ status: "error", message: "Sin datos" })).setMimeType(ContentService.MimeType.JSON);
    }

    let raw = "";
    if (e.postData && e.postData.contents) {
      raw = e.postData.contents;
    } else if (e.parameter && e.parameter.data) {
      raw = e.parameter.data;
    }

    // Limpieza de caracteres BOM (\uFEFF)
    if (raw && typeof raw === "string") {
      raw = raw.replace(/^\uFEFF/, "").trim();
    }

    let data = {};
    if (raw) {
      try {
        data = JSON.parse(raw);
      } catch (errJson) {
        // Fallback si vino URL-encoded
        data = e.parameter || {};
      }
    } else if (e.parameter) {
      data = e.parameter;
    }

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

    // Descartar visitas rutinarias del Administrador (salvo si fuerza prueba con ?test=1 o ?yo=1)
    if (data.es_admin && !data.forzar_registro && !data.ver_admin) {
      return ContentService.createTextOutput(JSON.stringify({ status: "ignored_admin", message: "Navegación rutinaria de admin ignorada" })).setMimeType(ContentService.MimeType.JSON);
    }

    // Normalizar ruta de la página
    let pagina = data.pagina || data.path || data.url || "/";
    pagina = pagina.replace(/^https?:\/\/(?:www\.)?coolpadelstudios\.com/i, "").replace(/^https?:\/\/(?:www\.)?savemyplay\.com/i, "");
    if (!pagina) pagina = "/";

    // Lead / Club: Nombre/Tel si se conoce, o Javier (Admin) si es prueba explícita, o EN BLANCO si es anónimo
    let leadLabel = "";
    if (data.forzar_registro && data.es_admin) {
      leadLabel = "👤 Javier (Admin)";
    } else if (data.lead_name && data.lead_tel) {
      leadLabel = data.lead_name + " (" + data.lead_tel + ")";
    } else if (data.lead_name) {
      leadLabel = data.lead_name;
    } else if (data.lead_tel) {
      leadLabel = data.lead_tel;
    } else if (data.lead_label && !data.lead_label.startsWith("Anónimo") && !data.lead_label.startsWith("analitica_evento")) {
      leadLabel = data.lead_label;
    }

    // Origen de acceso / Canal (Priorizar siempre buscadores orgánicos e IA)
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

    // ID de Sesión e ID de Visitante
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

    // Medición de Tiempo Activo y Scroll
    const tActivo = data.tiempo_activo || (data.tiempo_segundos ? formatSecondsGas(data.tiempo_segundos) : "0s");
    const sMax = data.scroll_max || data.scroll_hito || "0%";

    // Evento Real comprensible
    let eventoReal = data.evento_desc || "";
    const evt = data.evento || "";

    if (evt === "visita_iniciada" || evt === "pageview" || evt === "visita_blog_pagina" || evt === "page_view_landing") {
      eventoReal = "🟢 Lectura Iniciada";
    } else if (evt === "sesion_finalizada") {
      eventoReal = "🏁 Fin Lectura (" + tActivo + ", " + sMax + ")";
    } else if (evt === "heartbeat_lectura") {
      eventoReal = "⏱️ Leyendo (" + tActivo + ", " + sMax + ")";
    } else if (evt === "scroll_hito") {
      eventoReal = data.evento_desc || ("📜 Scroll " + sMax);
    } else if (evt.indexOf("click_whatsapp") >= 0) {
      eventoReal = "🎯 Clic WhatsApp (" + (data.ubicacion || "Carta") + ")";
    } else if (evt === "copiar_telefono") {
      eventoReal = "📋 Copió Teléfono";
    } else if (evt === "copiar_email") {
      eventoReal = "📋 Copió Email";
    } else if (evt === "calculadora_interaccion") {
      eventoReal = "📊 Calculadora (" + (data.tier_pistas || "") + " pistas)";
    } else if (evt === "geo_actualizada") {
      eventoReal = "📍 Ubicación: " + ubicacion;
    } else if (!eventoReal) {
      eventoReal = "Lectura (" + tActivo + ", " + sMax + ")";
    }

    // Secciones Leídas
    const seccionesLeidas = data.secciones_recorridas || data.seccion_actual || "";

    // Buscar si ya existe ESTA MISMA SESIÓN en las primeras 100 filas para consolidarla
    let filaSesion = -1;
    let notaSesion = "";
    const lastRow = sheetAnalitica.getLastRow();
    
    if (lastRow > 1) {
      const numRows = Math.min(lastRow - 1, 100);
      const notasRange = sheetAnalitica.getRange(2, 5, numRows, 1).getNotes(); // Columna 5: Visitas

      for (let i = 0; i < numRows; i++) {
        const n = notasRange[i][0] || "";
        if (sessionId && n.indexOf(sessionId) >= 0) {
          filaSesion = 2 + i;
          notaSesion = n;
          break;
        }
      }
    }

    if (filaSesion > 1) {
      // ─────────────────────────────────────────────────────────────────
      // CASO A: MISMA SESIÓN ACTIVA -> ACTUALIZAR Y CONSOLIDAR EN SU FILA
      // ─────────────────────────────────────────────────────────────────
      const filaActual = sheetAnalitica.getRange(filaSesion, 1, 1, 12).getValues()[0];

      // Tiempo activo: nunca permitir retrocesos de segundos
      const secPrevio = parseSecondsGas(filaActual[10]);
      const secNuevo = Math.max(data.tiempo_segundos || 0, parseSecondsGas(tActivo));
      const secFinal = Math.max(secPrevio, secNuevo);
      const tiempoConsolidado = secFinal > 0 ? formatSecondsGas(secFinal) : (filaActual[10] || "0s");

      // % Scroll: nunca permitir retrocesos de porcentaje
      const scrollPrevio = parseScrollGas(filaActual[11]);
      const scrollNuevo = Math.max(parseScrollGas(data.scroll_max), parseScrollGas(sMax));
      const scrollFinal = Math.max(scrollPrevio, scrollNuevo);
      const scrollConsolidado = scrollFinal + "%";

      // Actualizar evento real sin redundancias de "Fin Lectura" o "Leyendo"
      let eventosPrevios = filaActual[8] || "";
      let eventosActualizados = eventosPrevios;

      if (!eventosPrevios || eventosPrevios === "🟢 Lectura Iniciada") {
        eventosActualizados = eventoReal;
      } else if (eventoReal.startsWith("⏱️ Leyendo") || eventoReal.startsWith("🏁 Fin Lectura")) {
        // Reemplazar latido o fin previo por el estado más reciente
        if (eventosPrevios.includes(" ➔ ⏱️ Leyendo")) {
          eventosActualizados = eventosPrevios.replace(/ ➔ ⏱️ Leyendo.*$/, " ➔ " + eventoReal);
        } else if (eventosPrevios.includes(" ➔ 🏁 Fin Lectura")) {
          eventosActualizados = eventosPrevios.replace(/ ➔ 🏁 Fin Lectura.*$/, " ➔ " + eventoReal);
        } else {
          eventosActualizados = eventosPrevios + " ➔ " + eventoReal;
        }
      } else if (eventoReal.startsWith("📍 Ubicación")) {
        // No ensuciar la cadena de eventos con la actualización de ubicación
        eventosActualizados = eventosPrevios;
      } else if (!eventosPrevios.includes(eventoReal)) {
        eventosActualizados = eventosPrevios + " ➔ " + eventoReal;
      }

      // Asegurar que el ID de sesión permanezca en la nota
      let nuevaNota = notaSesion;
      if (!nuevaNota.includes(sessionId)) {
        nuevaNota = (nuevaNota.replace(/\[id:[^\]]+\]/g, "").trim() + "\n[id: " + (visitorId || "v") + " | " + sessionId + "]").trim();
      }

      const filaConsolidada = [
        dia,                                                             // Col 1: Fecha (dd/MM)
        hora,                                                            // Col 2: Hora (HH:mm:ss)
        leadLabel || filaActual[2] || "",                               // Col 3: Lead / Club
        origenCanal || filaActual[3] || "🌐 Enlace Directo",            // Col 4: Origen / Canal
        visitasStr || filaActual[4] || "1ª visita",                      // Col 5: Visitas
        ubicacion || filaActual[5] || "",                               // Col 6: Ubicación (enriquecida si llega nueva)
        dispositivo || filaActual[6] || "",                             // Col 7: Dispositivo
        pagina || filaActual[7] || "",                                  // Col 8: Página
        eventosActualizados,                                             // Col 9: Evento Real
        seccionesLeidas || filaActual[9] || "",                         // Col 10: Secciones Leídas
        tiempoConsolidado,                                               // Col 11: Tiempo Activo (máximo alcanzado)
        scrollConsolidado                                                // Col 12: % Scroll (máximo alcanzado)
      ];

      sheetAnalitica.getRange(filaSesion, 1, 1, 12).setValues([filaConsolidada]);
      sheetAnalitica.getRange(filaSesion, 5).setNote(nuevaNota);

    } else {
      // ─────────────────────────────────────────────────────────────────
      // CASO B: NUEVA VISITA / NUEVA SESIÓN -> INSERTAR NUEVA FILA EN FILA 2
      // (NUNCA se borran visitas anteriores: cada sesión queda registrada)
      // ─────────────────────────────────────────────────────────────────
      let notaInicial = "📜 Visita registrada:\n• " + visitasStr + " (" + dia + " " + hora + ")\n  Pág: " + pagina + " | Origen: " + origenCanal + "\n[id: " + (visitorId || "v") + " | " + sessionId + "]";

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
        tActivo,
        sMax
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

/**
 * Soporte para GET (Image Beacon o fallback de navegadores restringidos)
 */
function doGet(e) {
  if (e && e.parameter && (e.parameter.tipo || e.parameter.evento || e.parameter.session_id)) {
    return doPost(e);
  }
  return ContentService.createTextOutput("CoolPadel Webhook Activo").setMimeType(ContentService.MimeType.TEXT);
}

// Utilidades auxiliares de formato y parsing
function formatSecondsGas(sec) {
  const sNum = parseInt(sec, 10) || 0;
  const m = Math.floor(sNum / 60);
  const s = sNum % 60;
  return m + "m " + (s < 10 ? "0" : "") + s + "s";
}

function parseSecondsGas(str) {
  if (!str) return 0;
  let sec = 0;
  const matchM = str.toString().match(/(\d+)\s*m/);
  const matchS = str.toString().match(/(\d+)\s*s/);
  if (matchM) sec += parseInt(matchM[1], 10) * 60;
  if (matchS) sec += parseInt(matchS[1], 10);
  if (!matchM && !matchS && /^\d+$/.test(str.toString().trim())) {
    sec = parseInt(str.toString().trim(), 10);
  }
  return sec;
}

function parseScrollGas(str) {
  if (!str) return 0;
  const match = str.toString().match(/(\d+)/);
  return match ? parseInt(match[1], 10) : 0;
}

/**
 * MENÚ Y VISOR DE HISTORIAL EN GOOGLE SHEETS
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
