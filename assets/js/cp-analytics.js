/**
 * COOLPADEL STUDIOS & SAVE MY PLAY - MOTOR UNIFICADO DE ANALÍTICA COMERCIAL Y ORGÁNICA (SEO / GEO / AEO)
 * Registra visitas en tiempo real en la pestaña 'Analitica Web' de Google Sheets:
 * - Detección precisa de tráfico orgánico (Google, Bing, DuckDuckGo, Yahoo, Brave, Ecosia)
 * - Detección de motores de IA generativa (ChatGPT, SearchGPT, Perplexity, Claude, Gemini, Copilot)
 * - Atribución comercial B2B (WhatsApp rutas 1A..4A, Email, Redes Sociales, Navegación interna)
 * - Geolocalización dual (Timezone instantáneo 0ms + enriquecimiento async por IP)
 * - Medición de tiempo activo real con latidos periódicos (15s, 45s, 90s, 180s)
 * - Hitos de scroll automático (25%, 50%, 75%, 90%) para capturar lectura real sin depender de salida
 * - Transporte ultra-resiliente con triple fallback (sendBeacon con Blob -> fetch no-cors -> Image beacon)
 */
(function () {
  if (window.__CP_ANALYTICS_LOADED__) return;
  window.__CP_ANALYTICS_LOADED__ = true;

  const WEBHOOK_URL = 'https://script.google.com/macros/s/AKfycbxnF9JmVrikeAW7PdLc02r_1kkuSJVz1Ncl71ZeVGT37H0ji5DQ3DVw60122pcuYnxCgA/exec';

  // 1. Modo Administrador (Javier)
  const urlParams = new URLSearchParams(window.location.search);
  const paramAdmin = (urlParams.get('admin') || '').toLowerCase();
  const paramYo = urlParams.get('yo') === '1';
  const paramTest = urlParams.get('test') === '1' || urlParams.get('debug') === '1';

  if (['1', 'true', 'javier'].includes(paramAdmin) || paramYo) {
    try { localStorage.setItem('cp_is_admin', 'true'); } catch (e) {}
  } else if (['0', 'false'].includes(paramAdmin) || urlParams.get('reset_admin') === '1') {
    try { localStorage.removeItem('cp_is_admin'); } catch (e) {}
  }

  let isAdmin = false;
  try {
    isAdmin = localStorage.getItem('cp_is_admin') === 'true';
  } catch (e) {}

  // Si Javier fuerza prueba explícita con ?test=1, ?yo=1 o ?admin=1, registrar como Admin visible
  const forzarRegistroAdmin = paramTest || paramYo || ['1', 'true', 'javier'].includes(paramAdmin);

  // 2. Atribución de Leads y Parámetros UTM / Buscadores
  const pLead = urlParams.get('lead') || urlParams.get('club') || urlParams.get('nombre') || urlParams.get('director') || '';
  const pTel = urlParams.get('tel') || urlParams.get('phone') || urlParams.get('c') || '';
  const pSource = urlParams.get('utm_source') || urlParams.get('src') || '';
  const pCampaign = urlParams.get('utm_campaign') || urlParams.get('camp') || urlParams.get('ruta') || '';

  try {
    if (pLead) localStorage.setItem('cp_lead_name', pLead);
    if (pTel) localStorage.setItem('cp_lead_tel', pTel);
    if (pSource) localStorage.setItem('cp_utm_source', pSource);
    if (pCampaign) localStorage.setItem('cp_utm_campaign', pCampaign);
  } catch (e) {}

  const leadName = pLead || (function () { try { return localStorage.getItem('cp_lead_name') || ''; } catch (e) { return ''; } })();
  const leadTel = pTel || (function () { try { return localStorage.getItem('cp_lead_tel') || ''; } catch (e) { return ''; } })();
  const utmSource = pSource || (function () { try { return localStorage.getItem('cp_utm_source') || ''; } catch (e) { return ''; } })();
  const utmCampaign = pCampaign || (function () { try { return localStorage.getItem('cp_utm_campaign') || ''; } catch (e) { return ''; } })();

  // 3. ID de Sesión e ID de Visitante
  function generateUid(prefix) {
    return prefix + '_' + Date.now().toString(36) + '_' + Math.random().toString(36).substring(2, 6);
  }

  let sessionId = '';
  try {
    sessionId = sessionStorage.getItem('cp_session_id');
    if (!sessionId) {
      sessionId = generateUid('s');
      sessionStorage.setItem('cp_session_id', sessionId);
    }
  } catch (e) {
    sessionId = generateUid('s');
  }

  let visitorId = '';
  let visitCount = 1;
  let isReturningVisitor = false;
  try {
    visitorId = localStorage.getItem('cp_visitor_id');
    const nowMs = Date.now();
    if (!visitorId) {
      visitorId = generateUid('v');
      localStorage.setItem('cp_visitor_id', visitorId);
      localStorage.setItem('cp_visit_count', '1');
      localStorage.setItem('cp_first_visit', nowMs.toString());
      localStorage.setItem('cp_last_visit', nowMs.toString());
    } else {
      let count = parseInt(localStorage.getItem('cp_visit_count') || '1', 10);
      if (!sessionStorage.getItem('cp_counted_in_session')) {
        count++;
        localStorage.setItem('cp_visit_count', count.toString());
        sessionStorage.setItem('cp_counted_in_session', 'true');
        localStorage.setItem('cp_last_visit', nowMs.toString());
      }
      visitCount = count;
      if (visitCount > 1) isReturningVisitor = true;
    }
  } catch (e) {
    visitorId = generateUid('v');
  }

  // 4. Detección de Dispositivo y Entorno (Webviews de WhatsApp, Instagram, LinkedIn, etc.)
  function getDeviceInfo() {
    const ua = navigator.userAgent || '';
    const platform = navigator.platform || '';
    const maxTouchPoints = navigator.maxTouchPoints || 0;

    let os = 'Web';
    if (/iPhone/i.test(ua)) os = 'iPhone';
    else if (/iPad/i.test(ua) || (platform === 'MacIntel' && maxTouchPoints > 1)) os = 'iPad';
    else if (/Android/i.test(ua)) os = 'Android';
    else if (/Windows|Win32|Win64|WOW64/i.test(ua)) os = 'Windows';
    else if (/Macintosh|MacIntel|MacPPC|Mac68K/i.test(ua)) os = 'Mac';
    else if (/CrOS/i.test(ua)) os = 'ChromeOS';
    else if (/Linux/i.test(ua) || /X11/i.test(ua)) os = 'Linux';
    else if (/mobile/i.test(ua)) os = 'Móvil';

    let app = '';
    if (/WhatsApp/i.test(ua)) app = ' (WhatsApp)';
    else if (/Instagram/i.test(ua)) app = ' (Instagram)';
    else if (/FBAN|FBAV/i.test(ua)) app = ' (Facebook)';
    else if (/LinkedIn/i.test(ua)) app = ' (LinkedIn)';
    else if (/Telegram/i.test(ua)) app = ' (Telegram)';
    else if (/GoogleApp|GSA\//i.test(ua)) app = ' (Google App)';

    return {
      dispositivo: os + app,
      so: os,
      resolucion: (window.screen ? window.screen.width + 'x' + window.screen.height : '')
    };
  }

  function getLeadIdentification() {
    if (isAdmin) return '👤 Javier (Admin)';
    if (leadName && leadTel) return leadName + ' (' + leadTel + ')';
    if (leadName) return leadName;
    if (leadTel) return leadTel;
    return '';
  }

  // 5. Clasificación Exacta de Origen / Canal (SEO, GEO/AEO, WhatsApp, Email, Redes)
  function getChannelOrigin() {
    const ref = (document.referrer || '').toLowerCase();
    const ua = navigator.userAgent || '';
    const src = (utmSource || '').toLowerCase();
    const camp = (utmCampaign || '').toUpperCase();

    // 1. Motores de IA Generativa (GEO / AEO)
    if (ref.includes('chatgpt.com') || ref.includes('openai.com') || src.includes('chatgpt') || src.includes('openai')) {
      return '🤖 IA: ChatGPT / SearchGPT';
    }
    if (ref.includes('perplexity.ai') || src.includes('perplexity')) {
      return '🤖 IA: Perplexity';
    }
    if (ref.includes('claude.ai') || src.includes('claude')) {
      return '🤖 IA: Claude';
    }
    if (ref.includes('gemini.google.com') || ref.includes('bard.google.com') || src.includes('gemini')) {
      return '🤖 IA: Google Gemini';
    }
    if (ref.includes('copilot.microsoft.com') || src.includes('copilot')) {
      return '🤖 IA: Microsoft Copilot';
    }
    if (ref.includes('you.com')) {
      return '🤖 IA: You.com';
    }

    // 2. Búsqueda Orgánica en Buscadores (SEO)
    const isGoogle = ref.includes('google') || urlParams.has('srsltid') || urlParams.has('gclid') || /GoogleApp|GSA\//i.test(ua);
    if (isGoogle) return '🔍 Búsqueda Google';
    if (ref.includes('bing.com') || ref.includes('msn.com') || urlParams.has('msclkid')) return '🔍 Búsqueda Bing';
    if (ref.includes('duckduckgo.com')) return '🔍 Búsqueda DuckDuckGo';
    if (ref.includes('yahoo.')) return '🔍 Búsqueda Yahoo';
    if (ref.includes('ecosia.org')) return '🔍 Búsqueda Ecosia';
    if (ref.includes('search.brave.com')) return '🔍 Búsqueda Brave';
    if (ref.includes('yandex.')) return '🔍 Búsqueda Yandex';

    // 3. Link recibido por WhatsApp
    const hasWaParam = src.includes('wa') || src.includes('whatsapp') || camp.startsWith('1A') || camp.startsWith('2A') || camp.startsWith('3A') || camp.startsWith('4A') || Boolean(pTel);
    const isWaApp = /WhatsApp/i.test(ua) || ref.includes('whatsapp.com');
    if (hasWaParam || isWaApp) {
      let detalle = '📲 Link WhatsApp';
      if (camp) detalle += ' (Ruta ' + camp + ')';
      else if (leadName) detalle += ' (' + leadName + ')';
      return detalle;
    }

    // 4. Link recibido por Email
    if (src.includes('email') || src.includes('resend') || src.includes('mail')) {
      return '✉️ Link Email' + (camp ? ' (' + camp + ')' : '');
    }

    // 5. Navegación interna desde otra página de la web
    if (ref && (ref.includes('coolpadelstudios.com') || ref.includes('savemyplay.com') || (window.location.host && ref.includes(window.location.host.toLowerCase())))) {
      try {
        const urlRef = new URL(document.referrer);
        const pathRef = urlRef.pathname || '/';
        if (pathRef !== window.location.pathname) {
          return '🌐 Desde la Web (de ' + pathRef + ')';
        }
      } catch (e) {
        return '🌐 Desde la Web';
      }
    }

    // 6. Redes Sociales
    if (/Instagram/i.test(ua) || ref.includes('instagram.com')) return '📷 Instagram';
    if (/LinkedIn/i.test(ua) || ref.includes('linkedin.com') || ref.includes('lnkd.in')) return '💼 LinkedIn';
    if (/FBAN|FBAV/i.test(ua) || ref.includes('facebook.com') || ref.includes('fb.me')) return '👥 Facebook';
    if (ref.includes('youtube.com') || ref.includes('youtu.be')) return '▶️ YouTube';
    if (ref.includes('t.co') || ref.includes('twitter.com') || ref.includes('x.com')) return '🐦 X / Twitter';
    if (/TikTok/i.test(ua) || ref.includes('tiktok.com')) return '🎵 TikTok';

    // 7. Otras webs externas (Backlinks / Referrals)
    if (ref) {
      try {
        const host = new URL(document.referrer).hostname.replace(/^www\./, '');
        return '🔗 Web externa: ' + host;
      } catch (e) {}
    }

    // 8. Acceso sin referrer según sección de entrada
    const path = window.location.pathname || '/';
    if (path.indexOf('/herramientas/') >= 0) return '🛠️ Herramientas Gratuitas';
    if (path.indexOf('/franquicias-padel/') >= 0) return '🏢 Directorio Franquicias';
    if (path.indexOf('/blog/') >= 0) return '📝 Blog CoolPadel';
    if (path.indexOf('/camaras/') >= 0) return '🌐 Carta de Ventas (/camaras/)';
    if (path.indexOf('llaveros') >= 0 || path.indexOf('welcome-packs') >= 0) return '🏷️ Landing Llaveros';
    if (path.indexOf('camaras-padel') >= 0 || path.indexOf('camaras-grabacion') >= 0) return '🎥 Landing Cámaras';
    return '🌐 Home (coolpadelstudios.com)';
  }

  // 6. Geolocalización Dual: Fallback Timezone Inmediato (0ms) + Enriquecimiento Async por IP
  let geoUbicacion = '';
  try {
    geoUbicacion = sessionStorage.getItem('cp_geo') || '';
  } catch (e) {}

  function resolveFallbackTimezoneGeo() {
    try {
      const tz = Intl.DateTimeFormat().resolvedOptions().timeZone || '';
      const lang = (navigator.language || 'es-ES').toUpperCase();
      if (tz.includes('Madrid') || tz.includes('Canary')) return 'España (' + tz.split('/')[1] + ')';
      if (tz.includes('/')) return tz.replace('_', ' ').split('/').reverse().join(', ');
      return lang;
    } catch (e) {
      return 'España';
    }
  }

  function fetchGeoLocation() {
    if (geoUbicacion && geoUbicacion !== 'España') return Promise.resolve(geoUbicacion);
    return new Promise((resolve) => {
      let settled = false;
      const done = (val) => {
        if (settled) return;
        settled = true;
        if (val) {
          geoUbicacion = val;
          try { sessionStorage.setItem('cp_geo', val); } catch (e) {}
        } else if (!geoUbicacion) {
          geoUbicacion = resolveFallbackTimezoneGeo();
        }
        resolve(geoUbicacion);
      };

      const timer = setTimeout(() => done(geoUbicacion || resolveFallbackTimezoneGeo()), 600);

      fetch('https://ipwho.is/')
        .then(r => r.json())
        .then(d => {
          if (d && d.city) {
            clearTimeout(timer);
            const loc = [d.city, d.region, d.country_code || 'ES'].filter(Boolean).join(', ');
            done(loc);
          } else {
            throw new Error('no city');
          }
        })
        .catch(() => {
          fetch('https://ipapi.co/json/')
            .then(r => r.json())
            .then(d => {
              clearTimeout(timer);
              if (d && d.city) {
                const loc = [d.city, d.region, d.country_code || 'ES'].filter(Boolean).join(', ');
                done(loc);
              } else {
                done(resolveFallbackTimezoneGeo());
              }
            })
            .catch(() => {
              clearTimeout(timer);
              done(resolveFallbackTimezoneGeo());
            });
        });
    });
  }

  // 7. Medición de Tiempo Activo, Scroll y Secciones Leídas
  let activeSeconds = 0;
  let lastTick = Date.now();
  let maxScrollPercent = 0;
  let currentSection = document.title ? document.title.split('|')[0].trim().slice(0, 42) : 'Inicio';
  const visitedSectionsList = [currentSection];

  setInterval(() => {
    if (!document.hidden) {
      const now = Date.now();
      const diff = Math.round((now - lastTick) / 1000);
      if (diff > 0 && diff < 5) {
        activeSeconds += diff;
      }
      lastTick = now;
    } else {
      lastTick = Date.now();
    }
  }, 1000);

  function formatTime(sec) {
    const m = Math.floor(sec / 60);
    const s = sec % 60;
    return m + 'm ' + (s < 10 ? '0' : '') + s + 's';
  }

  // Medición continua de Scroll con detección de hitos clave (25%, 50%, 75%, 90%)
  const scrollMilestonesReached = {};
  window.addEventListener('scroll', () => {
    const h = document.documentElement;
    const b = document.body;
    const scrollable = (h.scrollHeight || b.scrollHeight) - h.clientHeight;
    if (scrollable <= 0) return;
    const pct = Math.min(100, Math.round(((h.scrollTop || b.scrollTop) / scrollable) * 100));
    if (pct > maxScrollPercent) maxScrollPercent = pct;

    // Hitos automáticos de scroll que enriquecen la sesión en Google Sheets en vivo
    [25, 50, 75, 90].forEach(m => {
      if (pct >= m && !scrollMilestonesReached[m]) {
        scrollMilestonesReached[m] = true;
        sendToWebhook('scroll_hito', {
          scroll_max: maxScrollPercent + '%',
          evento_desc: '📜 Scroll ' + m + '% (' + formatTime(activeSeconds) + ')'
        });
      }
    });
  }, { passive: true });

  function setupSectionObserver() {
    if (!('IntersectionObserver' in window)) return;
    try {
      const obs = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            const label = entry.target.getAttribute('data-sec-label');
            if (label && !visitedSectionsList.includes(label)) {
              currentSection = label;
              if (visitedSectionsList.length < 8) {
                visitedSectionsList.push(label);
              }
            }
          }
        });
      }, { threshold: 0.25 });

      const nodes = document.querySelectorAll('h2, section[id]');
      nodes.forEach((el) => {
        const txt = (el.innerText || el.id || '').replace(/\s+/g, ' ').trim().slice(0, 38);
        if (txt && txt.length > 2) {
          el.setAttribute('data-sec-label', txt);
          obs.observe(el);
        }
      });
    } catch (e) {}
  }

  // 8. Envío Centralizado al Webhook de Google Sheets con Triple Capa de Transporte
  function sendToWebhook(eventName, extraData) {
    extraData = extraData || {};
    
    // Ignorar archivos locales en disco
    if (window.location.protocol === 'file:' || window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1') {
      return;
    }

    // Si es admin pero NO está forzando prueba explícita, ignorar para no ensuciar navegación de mantenimiento
    if (isAdmin && !forzarRegistroAdmin) {
      return;
    }

    try {
      const dev = getDeviceInfo();
      const payload = {
        tipo: 'analitica_evento',
        session_id: sessionId,
        visitor_id: visitorId,
        visita_num: visitCount,
        lead_label: getLeadIdentification(),
        lead_name: leadName,
        lead_tel: leadTel,
        geo_ubicacion: geoUbicacion || resolveFallbackTimezoneGeo(),
        es_admin: isAdmin,
        forzar_registro: forzarRegistroAdmin,
        evento: eventName,
        evento_desc: extraData.evento_desc || eventName,
        pagina: window.location.pathname || '/',
        path: window.location.pathname || '/',
        url: window.location.href,
        url_completa: window.location.href,
        referrer: document.referrer || '',
        seccion_actual: currentSection,
        secciones_recorridas: visitedSectionsList.join(' > '),
        scroll_max: maxScrollPercent + '%',
        tiempo_activo: formatTime(activeSeconds),
        tiempo_segundos: activeSeconds,
        dispositivo: dev.dispositivo,
        resolucion: dev.resolucion,
        idioma: (document.documentElement.lang || navigator.language || 'es').toLowerCase(),
        origen_canal: getChannelOrigin(),
        campana_utm: utmCampaign || utmSource || '',
        ...extraData
      };

      const jsonPayload = JSON.stringify(payload);

      // Capa 1: navigator.sendBeacon con Blob text/plain (CORS-safe, sobrevive a descargas de página)
      let beaconSent = false;
      if (typeof navigator.sendBeacon === 'function') {
        try {
          const blob = new Blob([jsonPayload], { type: 'text/plain;charset=UTF-8' });
          beaconSent = navigator.sendBeacon(WEBHOOK_URL, blob);
        } catch (eBeacon) {
          beaconSent = false;
        }
      }

      // Capa 2: Fetch keepalive no-cors con text/plain (CORS-safelisted, nunca lanza TypeError)
      if (!beaconSent && typeof fetch === 'function') {
        fetch(WEBHOOK_URL, {
          method: 'POST',
          mode: 'no-cors',
          headers: { 'Content-Type': 'text/plain;charset=UTF-8' },
          body: jsonPayload,
          keepalive: true
        }).catch(() => {
          // Fallback fetch normal sin keepalive si la cuota de keepalive del navegador está saturada
          fetch(WEBHOOK_URL, {
            method: 'POST',
            mode: 'no-cors',
            headers: { 'Content-Type': 'text/plain;charset=UTF-8' },
            body: jsonPayload
          }).catch(() => {
            // Capa 3: Image beacon de emergencia como último recurso
            try {
              const img = new Image();
              img.src = WEBHOOK_URL + '?tipo=analitica_evento&session_id=' + encodeURIComponent(sessionId) +
                '&evento=' + encodeURIComponent(eventName) +
                '&pagina=' + encodeURIComponent(window.location.pathname || '/') +
                '&lead=' + encodeURIComponent(getLeadIdentification()) +
                '&tiempo=' + activeSeconds +
                '&scroll=' + maxScrollPercent +
                '&_t=' + Date.now();
            } catch (eImg) {}
          });
        });
      }
    } catch (e) {}
  }

  // Exponer globalmente para calculadoras, formularios y botones
  window.cpTrackEvent = sendToWebhook;
  if (typeof window.trackEvent !== 'function') {
    window.trackEvent = sendToWebhook;
  }

  // 9. Inicialización Automática en Carga, Latidos y Salida
  function initTracking() {
    setupSectionObserver();

    // Trigger de activación Admin por triple clic en copyright
    try {
      let adminClickCount = 0;
      let adminClickTimer = null;
      const adminTrigger = document.getElementById('admin-toggle-trigger');
      if (adminTrigger) {
        adminTrigger.addEventListener('click', () => {
          adminClickCount++;
          clearTimeout(adminClickTimer);
          adminClickTimer = setTimeout(() => { adminClickCount = 0; }, 700);
          if (adminClickCount >= 3) {
            adminClickCount = 0;
            const current = localStorage.getItem('cp_is_admin') === 'true';
            if (current) {
              localStorage.removeItem('cp_is_admin');
              alert('👤 Modo Admin DESACTIVADO. Ahora se registrará como visitante normal.');
            } else {
              localStorage.setItem('cp_is_admin', 'true');
              alert('👤 Modo Admin ACTIVADO. Tus visitas de prueba aparecerán marcadas como "👤 Javier (Admin)".');
            }
            window.location.reload();
          }
        });
      }
    } catch (e) {}

    // PASO 1: Envío INMEDIATO de Visita Iniciada (0ms de espera, 100% capturado)
    sendToWebhook('visita_iniciada', {
      evento_desc: '🟢 Lectura Iniciada'
    });

    // PASO 2: Enriquecimiento async de geolocalización por IP en segundo plano
    if (!geoUbicacion || geoUbicacion === 'España') {
      fetchGeoLocation().then((loc) => {
        if (loc && loc !== 'España') {
          geoUbicacion = loc;
          sendToWebhook('geo_actualizada', {
            geo_ubicacion: loc,
            evento_desc: '📍 Ubicación: ' + loc
          });
        }
      });
    }

    // PASO 3: Latidos periódicos de lectura activa (15s, 45s, 90s, 180s y cada 120s)
    const heartbeats = [15, 45, 90, 180];
    const heartbeatsSent = {};
    setInterval(() => {
      if (!document.hidden && activeSeconds > 0) {
        heartbeats.forEach(sec => {
          if (activeSeconds >= sec && !heartbeatsSent[sec]) {
            heartbeatsSent[sec] = true;
            sendToWebhook('heartbeat_lectura', {
              evento_desc: '⏱️ Leyendo (' + formatTime(activeSeconds) + ', ' + maxScrollPercent + '%)'
            });
          }
        });
        if (activeSeconds > 180 && activeSeconds % 120 === 0 && !heartbeatsSent[activeSeconds]) {
          heartbeatsSent[activeSeconds] = true;
          sendToWebhook('heartbeat_lectura', {
            evento_desc: '⏱️ Leyendo (' + formatTime(activeSeconds) + ', ' + maxScrollPercent + '%)'
          });
        }
      }
    }, 2000);

    // PASO 4: Detectar clics en enlaces de WhatsApp y botones de herramientas
    document.addEventListener('click', (e) => {
      try {
        const a = e.target.closest ? e.target.closest('a, button') : null;
        if (!a) return;
        const href = (a.getAttribute('href') || '').toLowerCase();
        const txt = (a.innerText || '').replace(/\s+/g, ' ').trim().slice(0, 35);
        if (href.includes('wa.me') || href.includes('whatsapp.com')) {
          sendToWebhook('click_whatsapp', {
            ubicacion: txt || 'Botón WhatsApp',
            evento_desc: '🎯 Clic WhatsApp (' + (txt || 'Web') + ')'
          });
        } else if (a.tagName === 'BUTTON' && (txt.includes('Generar') || txt.includes('Copiar') || txt.includes('Imprimir') || txt.includes('Calcular'))) {
          sendToWebhook('herramienta_uso', {
            evento_desc: '🛠️ Usó Herramienta: ' + txt
          });
        }
      } catch (err) {}
    }, { passive: true });

    // PASO 5: Detectar copia de teléfono o email
    document.addEventListener('copy', () => {
      try {
        const sel = (window.getSelection() ? window.getSelection().toString() : '').trim();
        if (sel.includes('680') || sel.includes('317486') || sel.includes('+34')) {
          sendToWebhook('copiar_telefono', { evento_desc: '📋 Copió Teléfono' });
        } else if (sel.includes('@coolpadel') || sel.includes('javier@')) {
          sendToWebhook('copiar_email', { evento_desc: '📋 Copió Email' });
        }
      } catch (err) {}
    });

    // PASO 6: Reportar salida / fin de lectura con soporte para reanudación
    let exitSent = false;
    function reportSessionExit() {
      if (exitSent) return;
      exitSent = true;
      sendToWebhook('sesion_finalizada', {
        evento_desc: '🏁 Fin Lectura (' + formatTime(activeSeconds) + ', ' + maxScrollPercent + '%)'
      });
    }

    window.addEventListener('visibilitychange', () => {
      if (document.visibilityState === 'hidden') {
        reportSessionExit();
      } else if (document.visibilityState === 'visible') {
        exitSent = false;
      }
    });
    window.addEventListener('pagehide', reportSessionExit);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initTracking);
  } else {
    initTracking();
  }
})();
