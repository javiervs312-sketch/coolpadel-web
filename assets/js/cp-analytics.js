/**
 * COOLPADEL STUDIOS & SAVE MY PLAY - MOTOR UNIFICADO DE ANALÍTICA COMERCIAL Y ORGÁNICA (SEO / GEO / AEO)
 * Registra visitas en tiempo real en la pestaña 'Analitica Web' de Google Sheets:
 * - Detección precisa de tráfico orgánico (Google, Bing, DuckDuckGo, Yahoo, Brave, Ecosia)
 * - Detección de motores de IA generativa (ChatGPT, SearchGPT, Perplexity, Claude, Gemini, Copilot)
 * - Atribución comercial B2B (WhatsApp rutas 1A..4A, Email, Redes Sociales, Navegación interna)
 * - Geolocalización rápida por IP (ipwho.is + ipapi.co + fallback Timezone)
 * - Medición en vivo de tiempo activo, % de scroll y secciones leídas compatible con Google Apps Script
 * - Transporte primario por fetch keepalive no-cors + fallback sendBeacon/Image
 */
(function () {
  if (window.__CP_ANALYTICS_LOADED__) return;
  window.__CP_ANALYTICS_LOADED__ = true;

  const WEBHOOK_URL = 'https://script.google.com/macros/s/AKfycbxnF9JmVrikeAW7PdLc02r_1kkuSJVz1Ncl71ZeVGT37H0ji5DQ3DVw60122pcuYnxCgA/exec';

  // 1. Detección y Exclusión de Bots, Rastreadores y Automatizaciones (Googlebot, Lighthouse, Headless Chrome, etc.)
  function isBotOrAutomation() {
    try {
      // Navegadores automatizados (Puppeteer, Selenium, Playwright, Lighthouse)
      if (navigator.webdriver) return true;
      if (window.__nightmare || window._phantom || window.callPhantom) return true;
      if (document.visibilityState === 'prerender') return true;

      const ua = (navigator.userAgent || '').toLowerCase();
      // Firmas comunes de rastreadores conocidos
      const botKeywords = [
        'googlebot', 'google-inspectiontool', 'chrome-lighthouse', 'adsbot-google', 'feedfetcher-google',
        'bingbot', 'msnbot', 'bingpreview', 'slurp', 'duckduckbot', 'baiduspider', 'yandexbot',
        'bytespider', 'sogou', 'exabot', 'facebot', 'facebookexternalhit', 'ia_archiver',
        'semrushbot', 'ahrefsbot', 'dotbot', 'mj12bot', 'screaming frog', 'headlesschrome',
        'ptst/', 'pingdom', 'uptime', 'crawler', 'spider'
      ];
      if (botKeywords.some(function (k) { return ua.indexOf(k) !== -1; })) {
        return true;
      }
    } catch (e) {}
    return false;
  }

  if (isBotOrAutomation()) {
    return;
  }

  // 2. Gestión Robusta de Exclusión de Administrador / Dueño (ignorar tus propias visitas)
  // Métodos de activación:
  // - Abrir https://coolpadelstudios.com/yo/ o /admin/
  // - Añadir a cualquier URL: ?yo, ?admin, ?javier, ?soyyo, #yo, #admin
  // - Pulsar 5 veces seguidas en el footer de cualquier página
  // - Detección automática por IP conocida del dueño (85.60.187.52)
  function showAdminToast(msg) {
    try {
      let t = document.getElementById('cp-admin-toast');
      if (!t) {
        t = document.createElement('div');
        t.id = 'cp-admin-toast';
        t.style.cssText = 'position:fixed;bottom:24px;left:50%;transform:translateX(-50%);background:#0b1626;color:#10b981;border:1px solid #10b981;padding:12px 20px;border-radius:12px;font-size:14px;font-weight:600;z-index:999999;box-shadow:0 10px 25px rgba(0,0,0,0.5);text-align:center;max-width:90%;font-family:system-ui,-apple-system,sans-serif;transition:opacity 0.3s;pointer-events:none;';
        document.body.appendChild(t);
      }
      t.innerText = msg;
      t.style.opacity = '1';
      setTimeout(function () {
        if (t) {
          t.style.opacity = '0';
          setTimeout(function () { if (t && t.parentNode) t.parentNode.removeChild(t); }, 400);
        }
      }, 4000);
    } catch (e) {}
  }

  function hasOwnerCookie() {
    try {
      return document.cookie.split(';').some(function (c) {
        return c.trim().indexOf('cp_ignore_owner=1') === 0;
      });
    } catch (e) {
      return false;
    }
  }

  function setOwnerCookie(val) {
    try {
      if (val) {
        document.cookie = 'cp_ignore_owner=1; path=/; max-age=315360000; SameSite=Lax';
      } else {
        document.cookie = 'cp_ignore_owner=; path=/; expires=Thu, 01 Jan 1970 00:00:00 GMT; SameSite=Lax';
      }
    } catch (e) {}
  }

  const urlParams = new URLSearchParams(window.location.search);
  const rawHash = (window.location.hash || '').toLowerCase();

  const hasAdminQuery = (
    urlParams.has('yo') ||
    urlParams.has('admin') ||
    urlParams.has('no_track') ||
    urlParams.has('javier') ||
    urlParams.has('soyyo') ||
    urlParams.has('owner') ||
    rawHash === '#yo' ||
    rawHash === '#admin' ||
    rawHash === '#javier' ||
    rawHash === '#soyyo'
  );

  const hasResetQuery = (
    urlParams.has('borrar_yo') ||
    urlParams.has('track_me') ||
    rawHash === '#track_me' ||
    rawHash === '#borrar_yo'
  );

  if (hasAdminQuery) {
    try {
      localStorage.setItem('cp_ignore_owner', '1');
      localStorage.setItem('cp_admin', '1');
      sessionStorage.setItem('cp_ignore_owner', '1');
      setOwnerCookie(true);
    } catch (e) {}
    showAdminToast('🛡️ Modo Administrador ACTIVADO (Tus visitas no se registrarán)');
  } else if (hasResetQuery) {
    try {
      localStorage.removeItem('cp_ignore_owner');
      localStorage.removeItem('cp_admin');
      sessionStorage.removeItem('cp_ignore_owner');
      setOwnerCookie(false);
    } catch (e) {}
    showAdminToast('⚠️ Modo Administrador DESACTIVADO (Rastreo reactivado para pruebas)');
  }

  let isOwner = false;
  try {
    isOwner = (
      localStorage.getItem('cp_ignore_owner') === '1' ||
      localStorage.getItem('cp_admin') === '1' ||
      sessionStorage.getItem('cp_ignore_owner') === '1' ||
      hasOwnerCookie()
    );
  } catch (e) {}

  let isAdmin = isOwner;

  // Gesto táctil en footer: 5 pulsaciones consecutivas alternan el modo administrador en cualquier móvil
  let footerTapCount = 0;
  let footerTapTimer = null;
  document.addEventListener('click', function (e) {
    const footer = e.target.closest ? e.target.closest('footer') : null;
    if (footer) {
      footerTapCount++;
      clearTimeout(footerTapTimer);
      footerTapTimer = setTimeout(function () { footerTapCount = 0; }, 2500);
      if (footerTapCount >= 5) {
        footerTapCount = 0;
        let currentAdmin = false;
        try { currentAdmin = localStorage.getItem('cp_ignore_owner') === '1' || hasOwnerCookie(); } catch (err) {}
        if (!currentAdmin) {
          try {
            localStorage.setItem('cp_ignore_owner', '1');
            localStorage.setItem('cp_admin', '1');
            sessionStorage.setItem('cp_ignore_owner', '1');
            setOwnerCookie(true);
          } catch (err) {}
          isAdmin = true;
          isOwner = true;
          showAdminToast('🛡️ Modo Administrador ACTIVADO (Tus visitas no se registrarán)');
        } else {
          try {
            localStorage.removeItem('cp_ignore_owner');
            localStorage.removeItem('cp_admin');
            sessionStorage.removeItem('cp_ignore_owner');
            setOwnerCookie(false);
          } catch (err) {}
          isAdmin = false;
          isOwner = false;
          showAdminToast('⚠️ Modo Administrador DESACTIVADO (Rastreo reactivado para pruebas)');
        }
      }
    }
  });

  // Si ya es Administrador/Dueño, abortar toda la ejecución de analítica (Cero rastreo, cero webhooks, cero GA4)
  if (isOwner) {
    try {
      localStorage.setItem('cp_ignore_owner', '1');
      localStorage.setItem('cp_admin', '1');
      sessionStorage.setItem('cp_ignore_owner', '1');
      setOwnerCookie(true);
    } catch (e) {}
    try {
      window['ga-disable-G-1J92M58GCM'] = true;
      window['ga-disable-G-JHG20W056P'] = true;
      window['clarity'] = function () {};
    } catch (e) {}
    return;
  }

  // 2. Atribución de Leads y Parámetros UTM / Buscadores / Subruta de Club (/camaras/nombre-club/)
  // Slugs reservados del sistema (artículos, países, categorías) que NUNCA deben asignarse como nombre de Lead/Club
  const SLUGS_RESERVADOS_CAMARAS = new Set([
    'articulos', 'assets', 'index.html',
    'alemania', 'andorra', 'arabia-saudi', 'argentina', 'australia', 'austria',
    'bahrain', 'bahrein', 'belgica', 'belgique', 'brasil',
    'camaras-padel-playtomic-matchi-padelmates', 'camaras-padel-urbanizaciones-comunidades',
    'camaras-para-clubes-indoor-padel', 'camaras-para-pistas-outdoor-padel',
    'camaras-retransmision-torneos-padel', 'ceska-republika', 'chile', 'colombia',
    'como-ver-highlights-sin-app', 'costa-rica', 'croacia',
    'cuanto-cuesta-poner-camaras-pistas-padel', 'danmark', 'deutschland', 'dinamarca',
    'ecuador', 'egipto', 'egypt', 'ellada', 'emiratos-arabes-unidos', 'espana',
    'estados-unidos', 'finlandia', 'france', 'francia', 'gran-bretana', 'grecia',
    'hrvatska', 'india', 'indonesia', 'ireland', 'irlanda', 'italia', 'japan', 'japon',
    'kuwait', 'lebanon', 'libano', 'maroc', 'marruecos', 'mexico', 'nederland', 'norge',
    'noruega', 'oesterreich', 'oman', 'paises-bajos', 'panama', 'paraguay', 'polonia',
    'polska', 'portugal', 'qatar', 'republica-checa', 'republica-dominicana', 'romania',
    'rumania', 'saudi-arabia', 'save-my-play-vs-camaras-vigilancia',
    'save-my-play-vs-sistemas-con-obras', 'schweiz', 'south-africa', 'sudafrica',
    'suecia', 'suiza', 'suomi', 'sverige', 'tunez', 'tunisie', 'turkiye', 'turquia',
    'uae', 'united-kingdom', 'united-states', 'uruguay', 'venezuela'
  ]);

  let slugClub = '';
  const camarasMatch = window.location.pathname.match(/\/(?:(?:en|fr|it|de)\/)?camaras\/([a-z0-9\-]+)\/?$/i);
  if (camarasMatch) {
    const rawSlug = camarasMatch[1].toLowerCase();
    if (!SLUGS_RESERVADOS_CAMARAS.has(rawSlug)) {
      slugClub = camarasMatch[1].replace(/-/g, ' ').replace(/\b\w/g, l => l.toUpperCase());
    }
  }

  const pLead = urlParams.get('lead') || urlParams.get('club') || urlParams.get('nombre') || urlParams.get('director') || slugClub || '';
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

  // 3. ID de Sesión e ID de Visitante persistentes
  // Mantiene el mismo sessionId a lo largo de toda la navegación del usuario en la sesión activa (pestaña / 30 min)
  function generateUid(prefix) {
    return prefix + '_' + Date.now().toString(36) + '_' + Math.random().toString(36).substring(2, 6);
  }

  const nowMs = Date.now();
  let sessionId = '';
  const currentPageKey = (window.location.pathname || '/').replace(/[^a-zA-Z0-9]/g, '_').slice(0, 48);
  try {
    const storageKey = 'cp_sid_' + currentPageKey;
    sessionId = sessionStorage.getItem(storageKey) || '';
    const lastActivity = parseInt(sessionStorage.getItem('cp_session_activity') || '0', 10);
    if (!sessionId || (nowMs - lastActivity > 30 * 60 * 1000)) {
      sessionId = generateUid('s');
      sessionStorage.setItem(storageKey, sessionId);
    }
    sessionStorage.setItem('cp_session_activity', nowMs.toString());
  } catch (e) {
    sessionId = generateUid('s');
  }

  // Contador de visitas del usuario en localStorage
  let visitorId = '';
  let visitCount = 1;
  try {
    visitorId = localStorage.getItem('cp_visitor_id') || '';
    const lastVisitMs = parseInt(localStorage.getItem('cp_last_visit') || '0', 10);
    if (!visitorId) {
      visitorId = generateUid('v');
      localStorage.setItem('cp_visitor_id', visitorId);
      localStorage.setItem('cp_visit_count', '1');
      localStorage.setItem('cp_first_visit', nowMs.toString());
      localStorage.setItem('cp_last_visit', nowMs.toString());
      sessionStorage.setItem('cp_counted_in_session', 'true');
    } else {
      let count = parseInt(localStorage.getItem('cp_visit_count') || '1', 10);
      // Incrementar si es una nueva sesión o si pasaron más de 30 minutos sin actividad
      if (!sessionStorage.getItem('cp_counted_in_session') || (nowMs - lastVisitMs > 30 * 60 * 1000)) {
        count++;
        localStorage.setItem('cp_visit_count', count.toString());
        sessionStorage.setItem('cp_counted_in_session', 'true');
      }
      localStorage.setItem('cp_last_visit', nowMs.toString());
      visitCount = count;
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

    // 5. Navegación interna desde otra página de la web (Preservar canal de adquisición inicial si existe)
    if (ref && (ref.includes('coolpadelstudios.com') || ref.includes('savemyplay.com') || (window.location.host && ref.includes(window.location.host.toLowerCase())))) {
      try {
        const urlRef = new URL(document.referrer);
        const pathRef = urlRef.pathname || '/';
        const canalInicial = (function () { try { return sessionStorage.getItem('cp_initial_channel') || ''; } catch (e) { return ''; } })();
        if (canalInicial && !canalInicial.startsWith('🌐 Desde la Web')) {
          return canalInicial;
        }
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

    // 8. Acceso directo según sección de entrada
    const path = window.location.pathname || '/';
    if (path.indexOf('/herramientas/') >= 0) return '🛠️ Herramientas Gratuitas';
    if (path.indexOf('/franquicias-padel/') >= 0) return '🏢 Directorio Franquicias';
    if (path.indexOf('/blog/') >= 0) return '📝 Blog CoolPadel';
    if (path.indexOf('/camaras/') >= 0) return '🌐 Carta de Ventas (/camaras/)';
    if (path.indexOf('llaveros') >= 0 || path.indexOf('welcome-packs') >= 0) return '🏷️ Landing Llaveros';
    if (path.indexOf('camaras-padel') >= 0 || path.indexOf('camaras-grabacion') >= 0) return '🎥 Landing Cámaras';
    return '🌐 Home (coolpadelstudios.com)';
  }

  // 6. Geolocalización Rápida por IP con Fallback Timezone
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

  function fetchGeoLocation(timeoutMs) {
    if (geoUbicacion && !geoUbicacion.startsWith('España')) return Promise.resolve(geoUbicacion);
    return new Promise((resolve) => {
      let settled = false;
      const done = (val) => {
        if (settled) return;
        settled = true;
        if (val) {
          geoUbicacion = val;
          try { sessionStorage.setItem('cp_geo', val); } catch (e) {}
        }
        resolve(geoUbicacion || resolveFallbackTimezoneGeo());
      };

      const timer = setTimeout(() => done(geoUbicacion || resolveFallbackTimezoneGeo()), timeoutMs || 350);

      fetch('https://ipwho.is/')
        .then(r => r.json())
        .then(d => {
          if (d && d.city) {
            clearTimeout(timer);
            // Detección automática de Javier por IP (Orange Madrid - 85.60.187.52)
            const JAVIER_IPS = ['85.60.187.52'];
            if (JAVIER_IPS.indexOf(d.ip) !== -1) {
              isAdmin = true;
              isOwner = true;
              try {
                localStorage.setItem('cp_ignore_owner', '1');
                localStorage.setItem('cp_admin', '1');
                sessionStorage.setItem('cp_ignore_owner', '1');
                setOwnerCookie(true);
              } catch (e) {}
              try {
                window['ga-disable-G-1J92M58GCM'] = true;
                window['ga-disable-G-JHG20W056P'] = true;
                window['clarity'] = function () {};
              } catch (e) {}
              return;
            }
            const loc = [d.city, d.region, d.country_code || 'ES'].filter(Boolean).join(', ');
            done(loc);
          } else {
            throw new Error('no city');
          }
        })
        .catch(() => {
          Promise.reject('ipapi_disabled')
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

  // IMPORTANTE: Devolver '0s' cuando es 0 para que el Webhook en Google Apps Script no sobrescriba tiempos previos
  function formatTime(sec) {
    if (!sec || sec <= 0) return '0s';
    const m = Math.floor(sec / 60);
    const s = sec % 60;
    return m + 'm ' + (s < 10 ? '0' : '') + s + 's';
  }

  const scrollMilestonesReached = {};
  window.addEventListener('scroll', () => {
    const h = document.documentElement;
    const b = document.body;
    const scrollable = (h.scrollHeight || b.scrollHeight) - h.clientHeight;
    if (scrollable <= 0) return;
    const pct = Math.min(100, Math.round(((h.scrollTop || b.scrollTop) / scrollable) * 100));
    if (pct > maxScrollPercent) maxScrollPercent = pct;

    // Actualizar tiempo activo y % scroll en la fila de la sesión sin ensuciar la columna Evento Real
    [10, 25, 50, 75, 90].forEach(m => {
      if (pct >= m && !scrollMilestonesReached[m]) {
        scrollMilestonesReached[m] = true;
        sendToWebhook('visita_iniciada', {
          scroll_max: maxScrollPercent + '%',
          evento_desc: '🟢 Lectura Iniciada'
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

  // 8. Envío Centralizado al Webhook de Google Sheets
  // Usa fetch keepalive no-cors como transporte primario (sigue el redirect 302 de Google Apps Script sin perder datos)
  function sendToWebhook(eventName, extraData) {
    extraData = extraData || {};

    if (window.location.protocol === 'file:' || window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1') {
      return;
    }

    if (isAdmin) {
      return;
    }

    try {
      const dev = getDeviceInfo();
      delete extraData._unload;
      const origenActual = getChannelOrigin();
      try {
        if (!sessionStorage.getItem('cp_initial_channel') && !origenActual.startsWith('🌐 Desde la Web')) {
          sessionStorage.setItem('cp_initial_channel', origenActual);
        }
      } catch (e) {}

      // Incluimos visitor_id para vincular visitas del mismo usuario/dispositivo
      // e incluimos el origen real tras '||' en session_id para que el normalizador lo extraiga con precisión.
      const payload = {
        tipo: 'analitica_evento',
        session_id: sessionId + '||' + origenActual,
        visitor_id: visitorId,
        visita_num: visitCount,
        lead_label: getLeadIdentification(),
        lead_name: leadName,
        lead_tel: leadTel,
        geo_ubicacion: geoUbicacion || resolveFallbackTimezoneGeo(),
        es_admin: false,
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
        origen_canal: origenActual,
        campana_utm: utmCampaign || utmSource || '',
        ...extraData
      };

      const jsonPayload = JSON.stringify(payload);

      if (typeof fetch === 'function') {
        fetch(WEBHOOK_URL, {
          method: 'POST',
          mode: 'no-cors',
          headers: { 'Content-Type': 'text/plain;charset=UTF-8' },
          body: jsonPayload,
          keepalive: true
        }).catch(() => {
          fetch(WEBHOOK_URL, {
            method: 'POST',
            mode: 'no-cors',
            headers: { 'Content-Type': 'text/plain;charset=UTF-8' },
            body: jsonPayload
          }).catch(() => {
            if (typeof navigator.sendBeacon === 'function') {
              try {
                const blob = new Blob([jsonPayload], { type: 'text/plain;charset=UTF-8' });
                navigator.sendBeacon(WEBHOOK_URL, blob);
              } catch (eB) {}
            }
          });
        });
      } else if (typeof navigator.sendBeacon === 'function') {
        try {
          const blob = new Blob([jsonPayload], { type: 'text/plain;charset=UTF-8' });
          navigator.sendBeacon(WEBHOOK_URL, blob);
        } catch (eB) {}
      }
    } catch (e) {}
  }

  window.cpTrackEvent = sendToWebhook;
  window.cpTrack = sendToWebhook;
  if (typeof window.trackEvent !== 'function') {
    window.trackEvent = sendToWebhook;
  }

  // 9. Inicialización Automática en Carga, Latidos y Salida
  function initTracking() {
    setupSectionObserver();

    let initialVisitSent = false;
    function dispatchInitialVisit() {
      if (initialVisitSent) return;
      initialVisitSent = true;
      sendToWebhook('visita_iniciada', {
        evento_desc: '🟢 Lectura Iniciada'
      });
    }

    // Obtener geolocalización rápida (máx 350ms) antes del primer envío para evitar condiciones de carrera
    fetchGeoLocation(350).then((loc) => {
      dispatchInitialVisit();
      // Si el primer envío salió con el fallback de zona horaria, enriquecer en segundo plano
      if (!loc || loc.startsWith('España')) {
        fetchGeoLocation(2500).then((realLoc) => {
          if (realLoc && !realLoc.startsWith('España')) {
            geoUbicacion = realLoc;
            sendToWebhook('visita_iniciada', {
              geo_ubicacion: realLoc,
              evento_desc: '🟢 Lectura Iniciada'
            });
          }
        });
      }
    });

    // Latidos periódicos de lectura activa (actualizan Tiempo Activo y % Scroll manteniendo el estado limpio)
    const heartbeats = [4, 8, 15, 45, 90, 180];
    const heartbeatsSent = {};
    setInterval(() => {
      if (!document.hidden && activeSeconds > 0 && initialVisitSent) {
        heartbeats.forEach(sec => {
          if (activeSeconds >= sec && !heartbeatsSent[sec]) {
            heartbeatsSent[sec] = true;
            sendToWebhook('visita_iniciada', {
              evento_desc: '🟢 Lectura Iniciada'
            });
          }
        });
        if (activeSeconds > 180 && activeSeconds % 120 === 0 && !heartbeatsSent[activeSeconds]) {
          heartbeatsSent[activeSeconds] = true;
          sendToWebhook('visita_iniciada', {
            evento_desc: '🟢 Lectura Iniciada'
          });
        }
      }
    }, 2000);

    // Detectar copia de teléfono o email
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

    // Reportar salida / fin de lectura
    let exitSent = false;
    function reportSessionExit() {
      if (!initialVisitSent) {
        dispatchInitialVisit();
      }
      if (exitSent) return;
      exitSent = true;
      sendToWebhook('sesion_finalizada', {
        _unload: true,
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

  const buyingFunnelEntries = {
    '/blog/sistemas-grabacion-pistas-padel-comparativa/': ['camaras', 'comparativa_camaras'],
    '/blog/regalos-padel-originales-baratos-ideas-detalles-torneos/': ['llaveros', 'regalos_padel'],
    '/blog/welcome-pack-torneo-padel-ideas/': ['llaveros', 'ideas_welcome_packs']
  };
  try {
    const entry = buyingFunnelEntries[window.location.pathname];
    if (entry) sessionStorage.setItem('cp_buying_entry_' + entry[0], entry[1]);
  } catch (err) {}

  window.addEventListener('cp:keyring-calculation', (event) => {
    if (isAdmin) return;
    let funnel_entry = '';
    try { funnel_entry = sessionStorage.getItem('cp_buying_entry_llaveros') || ''; } catch (err) {}
    const payload = {
      event_category: 'lead',
      intent: 'calculo_llaveros',
      product: 'llaveros',
      funnel_entry,
      delivery_market: event.detail.market,
      page_path: window.location.pathname,
      button_position: 'calculator'
    };
    if (typeof window.gtag === 'function') window.gtag('event', 'keyring_calculation_start', payload);
    sendToWebhook('keyring_calculation_start', { ...payload, evento_desc: 'Inició cálculo de llaveros' });
  });

  // Detectar clics en enlaces de WhatsApp y botones de herramientas
  document.addEventListener('click', (e) => {
    try {
      const a = e.target.closest ? e.target.closest('a, button') : null;
      if (!a) return;
      const href = (a.getAttribute('href') || '').toLowerCase();
      const txt = (a.innerText || '').replace(/\s+/g, ' ').trim().slice(0, 35);
      const isWhatsApp = href.includes('wa.me') || href.includes('whatsapp.com');
      const intent = a.dataset.leadIntent;
      let funnelEntry = '';
      try { funnelEntry = sessionStorage.getItem('cp_buying_entry_' + a.dataset.product) || ''; } catch (err) {}
      const lead = intent ? {
        event_category: 'lead',
        intent,
        product: a.dataset.product || '',
        delivery_market: a.dataset.deliveryMarket || '',
        funnel_entry: funnelEntry,
        button_position: a.dataset.buttonPosition || 'content',
        page_path: window.location.pathname,
        evento_desc: 'Intención: ' + intent + ' · ' + (a.dataset.buttonPosition || 'content')
      } : {};
      if (intent && !isAdmin && typeof window.gtag === 'function') {
        const { event_category, button_position, page_path, product, delivery_market, funnel_entry } = lead;
        window.gtag('event', 'lead_intent', { event_category, intent, button_position, page_path, product, delivery_market, funnel_entry });
      }
      if (isWhatsApp) {
        sendToWebhook('click_whatsapp', {
          ...lead,
          ubicacion: intent ? intent + ' · ' + lead.button_position : (txt || 'Botón WhatsApp'),
          evento_desc: '🎯 Clic WhatsApp (' + (txt || 'Web') + ')'
        });
      } else if (intent) {
        sendToWebhook('lead_intent', lead);
      } else if (a.tagName === 'BUTTON' && (txt.includes('Generar') || txt.includes('Copiar') || txt.includes('Imprimir') || txt.includes('Calcular'))) {
        sendToWebhook('herramienta_uso', {
          evento_desc: '🛠️ Usó Herramienta: ' + txt
        });
      }
    } catch (err) {}
  }, { passive: true });

  if (document.readyState === 'loading') {
    window.addEventListener('load', () => {
      if ('requestIdleCallback' in window) {
        requestIdleCallback(initTracking, { timeout: 2000 });
      } else {
        setTimeout(initTracking, 500);
      }
    });
  } else {
    if ('requestIdleCallback' in window) {
      requestIdleCallback(initTracking, { timeout: 2000 });
    } else {
      setTimeout(initTracking, 300);
    }
  }
})();

// SISTEMA GLOBAL DE DESPLEGABLE DE IDIOMA COOLPADEL
(function () {
  window.toggleLangDropdown = function (e) {
    if (e) {
      e.preventDefault();
      e.stopPropagation();
    }
    var menu = document.getElementById('lang-dropdown-menu');
    var arrow = document.getElementById('lang-dropdown-arrow');
    if (!menu) return;
    var isHidden = menu.classList.contains('hidden');
    document.querySelectorAll('#lang-dropdown-menu, #lang-dropdown-menu-mob').forEach(function (m) {
      m.classList.add('hidden');
    });
    if (isHidden) {
      menu.classList.remove('hidden');
      if (arrow) {
        arrow.style.transform = 'rotate(180deg)';
        arrow.classList.add('rotate-180');
      }
    } else {
      if (arrow) {
        arrow.style.transform = 'rotate(0deg)';
        arrow.classList.remove('rotate-180');
      }
    }
  };

  window.toggleLangDropdownMob = function (e) {
    if (e) {
      e.preventDefault();
      e.stopPropagation();
    }
    var menu = document.getElementById('lang-dropdown-menu-mob');
    var arrow = document.getElementById('lang-dropdown-arrow-mob');
    if (!menu) return;
    var isHidden = menu.classList.contains('hidden');
    document.querySelectorAll('#lang-dropdown-menu, #lang-dropdown-menu-mob').forEach(function (m) {
      m.classList.add('hidden');
    });
    if (isHidden) {
      menu.classList.remove('hidden');
      if (arrow) {
        arrow.style.transform = 'rotate(180deg)';
        arrow.classList.add('rotate-180');
      }
    } else {
      if (arrow) {
        arrow.style.transform = 'rotate(0deg)';
        arrow.classList.remove('rotate-180');
      }
    }
  };

  document.addEventListener('click', function (e) {
    var container = document.getElementById('lang-dropdown-container');
    var menu = document.getElementById('lang-dropdown-menu');
    var arrow = document.getElementById('lang-dropdown-arrow');
    if (menu && (!container || !container.contains(e.target))) {
      menu.classList.add('hidden');
      if (arrow) {
        arrow.style.transform = 'rotate(0deg)';
        arrow.classList.remove('rotate-180');
      }
    }
    var containerMob = document.getElementById('lang-dropdown-container-mob');
    var menuMob = document.getElementById('lang-dropdown-menu-mob');
    var arrowMob = document.getElementById('lang-dropdown-arrow-mob');
    if (menuMob && (!containerMob || !containerMob.contains(e.target))) {
      menuMob.classList.add('hidden');
      if (arrowMob) {
        arrowMob.style.transform = 'rotate(0deg)';
        arrowMob.classList.remove('rotate-180');
      }
    }
  });
})();

