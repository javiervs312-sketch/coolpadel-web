#!/usr/bin/env python3
"""
Generador del Blog y Artículos de Newsletter de CoolPadel Studios:
1. coolpadel-web/blog/index.html (Portada del Blog con 3 newsletters en fila, más grandes, títulos con Highlights #0X: y salto de línea, franja azul #3478a6 y reportaje centrado)
2. coolpadel-web/blog/highlights-03/index.html (Artículo completo en español con suscripción final por email)
3. coolpadel-web/blog/highlights-02/index.html (Artículo completo en español con suscripción final por email)
4. coolpadel-web/blog/highlights-01/index.html (Artículo completo en español con suscripción final por email)
"""
import os

WEBHOOK_URL = 'https://script.google.com/macros/s/AKfycbxnF9JmVrikeAW7PdLc02r_1kkuSJVz1Ncl71ZeVGT37H0ji5DQ3DVw60122pcuYnxCgA/exec'

COMMON_HEAD = """
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="author" content="Javier Villoria - CoolPadel Studios">
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">
  <link rel="icon" type="image/png" href="{root_prefix}assets/images/favicon_transparente.png?v=transp3">
  <link rel="apple-touch-icon" sizes="180x180" href="{root_prefix}assets/images/favicon_transparente.png?v=transp3">
  <meta name="theme-color" content="#0b1626">

  <!-- Tailwind CSS & Lucide Icons -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script src="https://unpkg.com/lucide@0.468.0/dist/umd/lucide.min.js"></script>

  <!-- Google Fonts: Plus Jakarta Sans & Outfit -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@600;700;800;900&family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">

  <!-- Microsoft Clarity -->
  <script type="text/javascript">
    (function(c,l,a,r,i,t,y){{
      c[a]=c[a]||function(){{(c[a].q=c[a].q||[]).push(arguments)}};
      t=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i;
      y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);
    }})(window, document, "clarity", "script", "q7p8g52y9e");
  </script>

  <style>
    body {{ font-family: 'Plus Jakarta Sans', sans-serif; }}
    h1, h2, h3, h4, .font-heading {{ font-family: 'Outfit', sans-serif; }}
    .lang-opt-active {{
      background-color: #f2920b !important;
      color: #0b1626 !important;
      font-weight: 800 !important;
    }}
  </style>
"""

COMMON_TRACKING_JS = f"""
  <script>
    lucide.createIcons();

    // Tracking de visitas a Google Sheets Webhook
    const GOOGLE_SHEETS_WEBHOOK_URL = '{WEBHOOK_URL}';
    
    function trackEvent(nombreEvento, metadata) {{
      try {{
        const payload = {{
          tipo: 'evento',
          evento: nombreEvento,
          url: window.location.href,
          path: window.location.pathname,
          referrer: document.referrer || '',
          timestamp: new Date().toISOString(),
          metadata: metadata || {{}}
        }};
        fetch(GOOGLE_SHEETS_WEBHOOK_URL, {{
          method: 'POST',
          mode: 'no-cors',
          headers: {{ 'Content-Type': 'application/json' }},
          body: JSON.stringify(payload)
        }}).catch(() => {{}});
      }} catch(e) {{}}
    }}

    trackEvent('visita_blog_pagina', {{ pagina: window.location.pathname }});

    function handleNewsletterSub(e, edicion) {{
      e.preventDefault();
      const form = e.target;
      const input = form.querySelector('input[type="email"]');
      const btn = form.querySelector('button');
      const email = input.value.trim();
      if (!email) return;

      btn.disabled = true;
      const originalText = btn.innerHTML;
      btn.innerHTML = '<span>¡Suscrito con éxito!</span>';
      btn.classList.add('bg-emerald-500', 'text-white');

      try {{
        fetch(GOOGLE_SHEETS_WEBHOOK_URL, {{
          method: 'POST',
          mode: 'no-cors',
          headers: {{ 'Content-Type': 'application/json' }},
          body: JSON.stringify({{
            tipo: 'lead',
            email: email,
            fuente: 'Suscripción Newsletter ' + edicion,
            url: window.location.href,
            fecha: new Date().toISOString()
          }})
        }}).catch(() => {{}});
      }} catch(err) {{}}

      setTimeout(() => {{
        input.value = '';
        btn.disabled = false;
        btn.innerHTML = originalText;
        btn.classList.remove('bg-emerald-500', 'text-white');
      }}, 3500);
    }}

    // Control de idiomas (Desktop y Móvil)
    function toggleLangDropdown(e) {{
      if (e) e.stopPropagation();
      const menu = document.getElementById('lang-dropdown-menu');
      const arrow = document.getElementById('lang-dropdown-arrow');
      if (!menu) return;
      const isHidden = menu.classList.contains('hidden');
      if (isHidden) {{
        menu.classList.remove('hidden');
        if (arrow) arrow.classList.add('rotate-180');
      }} else {{
        menu.classList.add('hidden');
        if (arrow) arrow.classList.remove('rotate-180');
      }}
    }}

    function toggleLangDropdownMob(e) {{
      if (e) e.stopPropagation();
      const menu = document.getElementById('lang-dropdown-menu-mob');
      const arrow = document.getElementById('lang-dropdown-arrow-mob');
      if (!menu) return;
      const isHidden = menu.classList.contains('hidden');
      if (isHidden) {{
        menu.classList.remove('hidden');
        if (arrow) arrow.classList.add('rotate-180');
      }} else {{
        menu.classList.add('hidden');
        if (arrow) arrow.classList.remove('rotate-180');
      }}
    }}

    function switchLanguage(lang) {{
      try {{
        localStorage.setItem('coolpadel_lang', lang);
      }} catch(e) {{}}
      const isArticle = window.location.pathname.includes('/highlights-');
      const root = isArticle ? '../../' : '../';
      if (lang === 'es') {{
        const menu = document.getElementById('lang-dropdown-menu');
        if (menu) menu.classList.add('hidden');
        const menuMob = document.getElementById('lang-dropdown-menu-mob');
        if (menuMob) menuMob.classList.add('hidden');
      }} else if (lang === 'en') {{
        window.location.href = root + 'en/';
      }} else if (lang === 'fr') {{
        window.location.href = root + 'fr/';
      }} else if (lang === 'it') {{
        window.location.href = root + 'it/';
      }}
    }}

    document.addEventListener('click', function(e) {{
      const container = document.getElementById('lang-dropdown-container');
      const menu = document.getElementById('lang-dropdown-menu');
      const arrow = document.getElementById('lang-dropdown-arrow');
      if (container && menu && !container.contains(e.target)) {{
        menu.classList.add('hidden');
        if (arrow) arrow.classList.remove('rotate-180');
      }}
      const containerMob = document.getElementById('lang-dropdown-container-mob');
      const menuMob = document.getElementById('lang-dropdown-menu-mob');
      const arrowMob = document.getElementById('lang-dropdown-arrow-mob');
      if (containerMob && menuMob && !containerMob.contains(e.target)) {{
        menuMob.classList.add('hidden');
        if (arrowMob) arrowMob.classList.remove('rotate-180');
      }}
    }});
  </script>
"""

def generate_blog_index():
    root_prefix = "../"
    html = f"""<!DOCTYPE html>
<html lang="es" class="scroll-smooth">
<head>
  <title>Blog & Newsletter de la Industria del Pádel | CoolPadel</title>
  <meta name="description" content="Artículos y análisis estratégicos sobre la industria del pádel por Javier Villoria. Noticias, mercado, clubes y descarga del Informe 2026.">
  <link rel="canonical" href="https://coolpadelstudios.com/blog/">
  
  <!-- Open Graph / Redes Sociales -->
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="CoolPadel Studios">
  <meta property="og:locale" content="es_ES">
  <meta property="og:url" content="https://coolpadelstudios.com/blog/">
  <meta property="og:title" content="Blog & Newsletter de la Industria del Pádel | CoolPadel">
  <meta property="og:description" content="Artículos y análisis estratégicos sobre la industria del pádel por Javier Villoria. Noticias, mercado, clubes y descarga del Informe 2026.">
  <meta property="og:image" content="https://coolpadelstudios.com/assets/images/foto-reportaje.jpg">
  
  <!-- Twitter Cards -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Blog & Newsletter de la Industria del Pádel | CoolPadel">
  <meta name="twitter:description" content="Artículos y análisis estratégicos sobre la industria del pádel por Javier Villoria.">
  <meta name="twitter:image" content="https://coolpadelstudios.com/assets/images/foto-reportaje.jpg">

  <!-- Schema.org Blog & CollectionPage -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@graph": [
      {{
        "@type": "Blog",
        "@id": "https://coolpadelstudios.com/blog/#blog",
        "name": "Blog de la Industria del Pádel - CoolPadel Studios",
        "url": "https://coolpadelstudios.com/blog/",
        "description": "Análisis estratégico y noticias del ecosistema de raqueta por Javier Villoria.",
        "inLanguage": "es",
        "publisher": {{
          "@type": "Organization",
          "name": "CoolPadel Studios",
          "url": "https://coolpadelstudios.com",
          "logo": "https://coolpadelstudios.com/assets/images/coolpadel-mascot-hd.png"
        }},
        "author": {{
          "@type": "Person",
          "name": "Javier Villoria",
          "sameAs": "https://www.linkedin.com/in/javier-villoria-soleto-606737298/"
        }}
      }},
      {{
        "@type": "BreadcrumbList",
        "itemListElement": [
          {{
            "@type": "ListItem",
            "position": 1,
            "name": "Inicio",
            "item": "https://coolpadelstudios.com/"
          }},
          {{
            "@type": "ListItem",
            "position": 2,
            "name": "Blog & Newsletter",
            "item": "https://coolpadelstudios.com/blog/"
          }}
        ]
      }}
    ]
  }}
  </script>
  {COMMON_HEAD.format(root_prefix=root_prefix)}
</head>
<body class="bg-white text-slate-900 min-h-screen relative selection:bg-[#f2920b] selection:text-white flex flex-col justify-between">

  <div>
    <!-- 2. NAVBAR BLANCA IDÉNTICA A LA PRINCIPAL -->
    <header class="sticky top-0 z-40 bg-white text-slate-900 border-b border-slate-200 shadow-sm w-full">
      <div class="w-full max-w-[1700px] mx-auto px-3 sm:px-6 lg:px-10 py-1.5 sm:py-0 h-auto sm:h-16 lg:h-18">
        
        <!-- DESKTOP NAVBAR (3 COLUMNAS: IZQUIERDA + CENTRO 100% + DERECHA) -->
        <div class="hidden sm:grid grid-cols-[1fr_auto_1fr] items-center h-full w-full gap-2 lg:gap-4">
          
          <!-- COLUMNA 1: OJOS + LLAVEROS, CÁMARAS PISTAS Y BLOG CENTRADOS ENTRE OJOS Y LOGO -->
          <div class="flex items-center justify-between min-w-0 h-full">
            <a href="../" class="group py-1 inline-flex items-center shrink-0">
              <img src="../assets/images/eyes-thumb.png?v=fixed_eyes" alt="CoolPadel Eyes" width="24" height="24" style="height: 24px; max-height: 24px; width: auto;" class="object-contain group-hover:scale-110 transition duration-300">
            </a>
            <div class="flex-1 flex items-center justify-center min-w-0 gap-5 sm:gap-6 lg:gap-9 xl:gap-11 pl-2 sm:pl-4 lg:pl-6">
              <a href="../#llaveros" class="font-heading font-black text-xs lg:text-[13px] tracking-wider uppercase text-slate-950 hover:text-[#f2920b] transition select-none whitespace-nowrap">
                Llaveros
              </a>
              <a href="../camaras/" class="font-heading font-black text-xs lg:text-[13px] tracking-wider uppercase text-slate-950 hover:text-[#f2920b] transition select-none whitespace-nowrap">
                Cámaras pistas
              </a>
              <a href="./" class="font-heading font-black text-xs lg:text-[13px] tracking-wider uppercase text-[#f2920b] transition select-none whitespace-nowrap border-b-2 border-[#f2920b] pb-0.5">
                Blog
              </a>
            </div>
          </div>

          <!-- COLUMNA 2: MASCOTA + COOLPADEL CENTRADO -->
          <div class="flex items-center justify-center shrink-0 px-2 lg:px-4">
            <a href="../" class="flex items-center justify-center gap-2 sm:gap-3 group py-1">
              <img src="../assets/images/coolpadel-mascot-hd.png" alt="Mascota CoolPadel" width="46" height="46" style="height: 46px; max-height: 46px; width: auto;" class="object-contain group-hover:scale-105 transition">
              <img src="../assets/images/coolpadel-typography-hd.png" alt="CoolPadel" width="130" height="26" style="height: 26px; max-height: 26px; width: auto;" class="object-contain">
            </a>
          </div>

          <!-- COLUMNA 3: CADENAS DE CLUBS CENTRADO ENTRE LOGO Y SELECTOR DE IDIOMA + CONTROLES A LA DERECHA -->
          <div class="flex items-center justify-between min-w-0 h-full">
            <div class="flex-1 flex items-center justify-center min-w-0 pr-4 lg:pr-8">
              <a href="../franquicias-padel/" class="font-heading font-black text-xs lg:text-[13px] tracking-wider uppercase text-slate-950 hover:text-[#f2920b] transition select-none whitespace-nowrap">
                Cadenas de clubs
              </a>
            </div>

            <!-- BLOQUE A LA DERECHA DEL TODO: SELECTOR IDIOMA + CONTACTAR (SIN OJOS) -->
            <div class="flex items-center gap-2 sm:gap-3 shrink-0 ml-auto">
              <!-- SELECTOR DE IDIOMA EN DESPLEGABLE COMPACTO -->
              <div class="relative inline-block text-left" id="lang-dropdown-container">
                <button type="button" onclick="toggleLangDropdown(event)" id="lang-dropdown-btn" class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-full bg-slate-100 hover:bg-slate-200 border border-slate-200 text-xs font-black text-slate-900 shadow-xs transition cursor-pointer" aria-expanded="false" aria-haspopup="true">
                  <span id="current-lang-code" class="uppercase font-black">ES</span>
                  <i data-lucide="chevron-down" class="w-3.5 h-3.5 stroke-[2.5] text-slate-600 transition-transform duration-200" id="lang-dropdown-arrow"></i>
                </button>

                <!-- MENÚ DESPLEGABLE FLOTANTE -->
                <div id="lang-dropdown-menu" class="hidden absolute right-0 mt-2 w-24 bg-white rounded-2xl shadow-[0_12px_30px_rgba(0,0,0,0.15)] border border-slate-200 py-1.5 z-50 transition-all overflow-hidden">
                  <button type="button" onclick="switchLanguage('es')" data-lang-opt="es" class="lang-opt lang-opt-active w-full text-center px-4 py-2 text-xs transition duration-150 cursor-pointer">
                    ES
                  </button>
                  <button type="button" onclick="switchLanguage('en')" data-lang-opt="en" class="lang-opt text-slate-700 hover:bg-[#f2920b] hover:text-slate-950 font-bold w-full text-center px-4 py-2 text-xs transition duration-150 cursor-pointer">
                    EN
                  </button>
                  <button type="button" onclick="switchLanguage('fr')" data-lang-opt="fr" class="lang-opt text-slate-700 hover:bg-[#f2920b] hover:text-slate-950 font-bold w-full text-center px-4 py-2 text-xs transition duration-150 cursor-pointer">
                    FR
                  </button>
                  <button type="button" onclick="switchLanguage('it')" data-lang-opt="it" class="lang-opt text-slate-700 hover:bg-[#f2920b] hover:text-slate-950 font-bold w-full text-center px-4 py-2 text-xs transition duration-150 cursor-pointer">
                    IT
                  </button>
                </div>
              </div>

              <!-- BOTÓN CONTACTAR -->
              <a href="https://wa.me/34680317486?text=Hola%20Javier" target="_blank" rel="noopener noreferrer" class="group relative inline-flex items-center gap-1.5 px-3.5 sm:px-4 py-1.5 sm:py-2 rounded-full bg-[#f2920b] hover:bg-[#76d3f6] active:bg-[#76d3f6] text-slate-950 active:scale-95 font-heading font-black text-xs sm:text-xs lg:text-sm tracking-wider uppercase transition-all duration-300 shadow-[0_4px_12px_rgba(242,146,11,0.2)] hover:scale-105 shrink-0 overflow-hidden">
                <span class="font-black">Contactar</span>
                <div class="w-4 h-4 sm:w-5 sm:h-5 rounded-full bg-slate-950/10 group-hover:bg-slate-950 group-hover:text-white flex items-center justify-center transition-all duration-300 shrink-0">
                  <i data-lucide="arrow-up-right" class="w-2.5 h-2.5 sm:w-3 sm:h-3 stroke-[3]"></i>
                </div>
              </a>
            </div>
          </div>
        </div>

        <!-- MÓVIL NAVBAR -->
        <div class="flex sm:hidden flex-col gap-1.5 py-1.5 w-full">
          <!-- FILA 1: LOGO CENTRADO (SIN OJOS A LA DERECHA) -->
          <div class="flex items-center justify-between w-full px-2">
            <a href="../" class="py-0.5 inline-flex items-center shrink-0">
              <img src="../assets/images/eyes-thumb.png?v=fixed_eyes" alt="CoolPadel Eyes" width="18" height="18" style="height: 18px; max-height: 18px; width: auto;" class="object-contain">
            </a>
            <a href="../" class="flex items-center justify-center gap-1.5 py-0.5">
              <img src="../assets/images/coolpadel-mascot-hd.png" alt="Mascota CoolPadel" width="28" height="28" style="height: 28px; max-height: 28px; width: auto;" class="object-contain">
              <img src="../assets/images/coolpadel-typography-hd.png" alt="CoolPadel" width="90" height="18" style="height: 18px; max-height: 18px; width: auto;" class="object-contain">
            </a>
            <div class="w-[18px]"></div>
          </div>
          <!-- FILA 2: LLAVEROS + CÁMARAS PISTAS + BLOG + CADENAS DE CLUBS + IDIOMA + CONTACTAR -->
          <div class="flex items-center justify-between w-full gap-1 pt-1 border-t border-slate-100 px-1 overflow-x-auto">
            <div class="flex items-center gap-3.5 sm:gap-4 shrink-0">
              <a href="../#llaveros" class="font-heading font-black text-[10px] tracking-wider uppercase text-slate-950 hover:text-[#f2920b] transition whitespace-nowrap">
                Llaveros
              </a>
              <a href="../camaras/" class="font-heading font-black text-[10px] tracking-wider uppercase text-slate-950 hover:text-[#f2920b] transition whitespace-nowrap">
                Cámaras pistas
              </a>
              <a href="./" class="font-heading font-black text-[10px] tracking-wider uppercase text-[#f2920b] whitespace-nowrap border-b border-[#f2920b]">
                Blog
              </a>
              <a href="../franquicias-padel/" class="font-heading font-black text-[10px] tracking-wider uppercase text-slate-950 hover:text-[#f2920b] transition whitespace-nowrap">
                Cadenas de clubs
              </a>
            </div>

            <div class="flex items-center gap-1 shrink-0">
              <!-- DESPLEGABLE IDIOMA MÓVIL -->
              <div class="relative inline-block text-left" id="lang-dropdown-container-mob">
                <button type="button" onclick="toggleLangDropdownMob(event)" id="lang-dropdown-btn-mob" class="inline-flex items-center gap-1 px-2 py-0.5 rounded-full bg-slate-100 hover:bg-slate-200 border border-slate-200 text-[10px] font-black text-slate-900 shadow-xs transition cursor-pointer">
                  <span id="current-lang-code-mob" class="uppercase font-black">ES</span>
                  <i data-lucide="chevron-down" class="w-2.5 h-2.5 stroke-[2.5] text-slate-600" id="lang-dropdown-arrow-mob"></i>
                </button>
                <div id="lang-dropdown-menu-mob" class="hidden absolute right-0 mt-1 w-20 bg-white rounded-2xl shadow-xl border border-slate-200 py-1 z-50 transition-all overflow-hidden">
                  <button type="button" onclick="switchLanguage('es')" data-lang-opt="es" class="lang-opt lang-opt-active w-full text-center px-3 py-1.5 text-[11px] transition duration-150 cursor-pointer">
                    ES
                  </button>
                  <button type="button" onclick="switchLanguage('en')" data-lang-opt="en" class="lang-opt text-slate-700 hover:bg-[#f2920b] hover:text-slate-950 font-bold w-full text-center px-3 py-1.5 text-[11px] transition duration-150 cursor-pointer">
                    EN
                  </button>
                  <button type="button" onclick="switchLanguage('fr')" data-lang-opt="fr" class="lang-opt text-slate-700 hover:bg-[#f2920b] hover:text-slate-950 font-bold w-full text-center px-3 py-1.5 text-[11px] transition duration-150 cursor-pointer">
                    FR
                  </button>
                  <button type="button" onclick="switchLanguage('it')" data-lang-opt="it" class="lang-opt text-slate-700 hover:bg-[#f2920b] hover:text-slate-950 font-bold w-full text-center px-3 py-1.5 text-[11px] transition duration-150 cursor-pointer">
                    IT
                  </button>
                </div>
              </div>

              <!-- BOTÓN CONTACTAR MÓVIL -->
              <a href="https://wa.me/34680317486?text=Hola%20Javier" target="_blank" rel="noopener noreferrer" class="group relative inline-flex items-center justify-center gap-1 px-2.5 py-1 rounded-full bg-[#f2920b] active:bg-[#76d3f6] text-slate-950 active:scale-95 font-heading font-black text-[10px] uppercase tracking-wider transition shadow-xs shrink-0">
                <span class="font-black">Contactar</span>
                <div class="w-3 h-3 rounded-full bg-slate-950/10 flex items-center justify-center">
                  <i data-lucide="arrow-up-right" class="w-2 h-2 stroke-[3]"></i>
                </div>
              </a>
            </div>
          </div>
        </div>

      </div>
    </header>

    <!-- 3. SECCIÓN: BLOG & CONTENIDO EXCLUSIVO -->
    <main class="py-10 sm:py-16 bg-white relative">
      <div class="max-w-[1700px] mx-auto px-4 sm:px-6 lg:px-10">
        
        <!-- CABECERA DE SECCIÓN -->
        <div class="max-w-3xl mx-auto text-center space-y-2 mb-10 sm:mb-14">
          <h1 class="text-2xl sm:text-4xl font-black font-heading text-slate-950 uppercase tracking-tight">
            CONTENIDO EXCLUSIVO COOLPADEL
          </h1>
          <p class="text-slate-600 text-xs sm:text-base font-medium">
            Perspectivas, reflexiones y opiniones sobre la industria del pádel
          </p>
        </div>

        <!-- 3 NEWSLETTERS EN FILA DE IZQ A DCHA (MÁS ANCHAS Y LEGIBLES) -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6 lg:gap-8 max-w-[1700px] w-full mx-auto">
          
          <!-- 1. HIGHLIGHTS #03 (IZQUIERDA - MÁS RECIENTE) -->
          <div class="bg-white border border-slate-200/90 rounded-3xl p-6 sm:p-7 shadow-[0_20px_45px_-12px_rgba(0,0,0,0.14)] hover:shadow-[0_30px_60px_-10px_rgba(0,0,0,0.22)] transition-all duration-300 flex flex-col justify-between group hover:-translate-y-1">
            <div class="space-y-4">
              <a href="./highlights-03/" class="block aspect-[16/9] rounded-2xl overflow-hidden bg-slate-900 border border-slate-200/90 shadow-[0_15px_30px_-10px_rgba(0,0,0,0.35)] relative">
                <img src="../assets/images/cover_highlights_03.jpg" alt="Highlights #03: ¿Cómo crece realmente la industria del pádel?" width="800" height="450" class="w-full h-full object-cover group-hover:scale-105 transition duration-700" loading="eager" decoding="async">
              </a>

              <div class="pt-1">
                <span class="block text-xs sm:text-sm font-extrabold text-[#f2920b] uppercase tracking-wider mb-1">Highlights #03:</span>
                <h2 class="font-sans font-extrabold text-lg sm:text-xl lg:text-2xl text-slate-900 leading-snug tracking-tight">
                  ¿Cómo crece realmente la industria del pádel?
                </h2>
                <p class="text-slate-600 text-xs sm:text-sm font-normal leading-relaxed mt-2 line-clamp-2">
                  Nuevas oportunidades en mercados emergentes, desafíos en mercados maduros y las 5 etapas del desarrollo del pádel.
                </p>
              </div>
            </div>

            <!-- BOTÓN ABRIR ARTÍCULO -->
            <div class="pt-5 border-t border-slate-100 mt-5">
              <a href="./highlights-03/" 
                 class="group relative w-full inline-flex items-center justify-center gap-2 px-6 py-3.5 rounded-full bg-[#f2920b] hover:bg-[#76d3f6] active:bg-[#76d3f6] text-slate-950 active:scale-95 font-heading font-black text-xs sm:text-sm uppercase tracking-wider transition-all duration-300 shadow-[0_4px_15px_rgba(242,146,11,0.25)] hover:shadow-[0_8px_25px_rgba(118,211,246,0.35)] hover:scale-[1.01] overflow-hidden">
                <span class="font-black">Leer Highlights #03</span>
                <div class="w-5 h-5 rounded-full bg-slate-950/10 group-hover:bg-slate-950 group-hover:text-white flex items-center justify-center transition-all duration-300">
                  <i data-lucide="arrow-right" class="w-3.5 h-3.5 stroke-[3] group-hover:translate-x-0.5 transition-transform duration-300"></i>
                </div>
              </a>
            </div>
          </div>

          <!-- 2. HIGHLIGHTS #02 (CENTRO) -->
          <div class="bg-white border border-slate-200/90 rounded-3xl p-6 sm:p-7 shadow-[0_20px_45px_-12px_rgba(0,0,0,0.14)] hover:shadow-[0_30px_60px_-10px_rgba(0,0,0,0.22)] transition-all duration-300 flex flex-col justify-between group hover:-translate-y-1">
            <div class="space-y-4">
              <a href="./highlights-02/" class="block aspect-[16/9] rounded-2xl overflow-hidden bg-slate-900 border border-slate-200/90 shadow-[0_15px_30px_-10px_rgba(0,0,0,0.35)] relative">
                <img src="../assets/images/cover_highlights_02.jpg" alt="Highlights #02: El Pádel debería estar lejos de ser un deporte olímpico" width="800" height="450" class="w-full h-full object-cover group-hover:scale-105 transition duration-700" loading="lazy" decoding="async">
              </a>

              <div class="pt-1">
                <span class="block text-xs sm:text-sm font-extrabold text-[#f2920b] uppercase tracking-wider mb-1">Highlights #02:</span>
                <h2 class="font-sans font-extrabold text-lg sm:text-xl lg:text-2xl text-slate-900 leading-snug tracking-tight">
                  El Pádel debería estar lejos de ser un deporte olímpico. ¿Por qué?
                </h2>
                <p class="text-slate-600 text-xs sm:text-sm font-normal leading-relaxed mt-2 line-clamp-2">
                  Por qué la cultura del pádel necesita consolidarse fuera de los países tradicionales antes de dar el salto olímpico.
                </p>
              </div>
            </div>

            <!-- BOTÓN ABRIR ARTÍCULO -->
            <div class="pt-5 border-t border-slate-100 mt-5">
              <a href="./highlights-02/" 
                 class="group relative w-full inline-flex items-center justify-center gap-2 px-6 py-3.5 rounded-full bg-[#f2920b] hover:bg-[#76d3f6] active:bg-[#76d3f6] text-slate-950 active:scale-95 font-heading font-black text-xs sm:text-sm uppercase tracking-wider transition-all duration-300 shadow-[0_4px_15px_rgba(242,146,11,0.25)] hover:shadow-[0_8px_25px_rgba(118,211,246,0.35)] hover:scale-[1.01] overflow-hidden">
                <span class="font-black">Leer Highlights #02</span>
                <div class="w-5 h-5 rounded-full bg-slate-950/10 group-hover:bg-slate-950 group-hover:text-white flex items-center justify-center transition-all duration-300">
                  <i data-lucide="arrow-right" class="w-3.5 h-3.5 stroke-[3] group-hover:translate-x-0.5 transition-transform duration-300"></i>
                </div>
              </a>
            </div>
          </div>

          <!-- 3. HIGHLIGHTS #01 (DERECHA) -->
          <div class="bg-white border border-slate-200/90 rounded-3xl p-6 sm:p-7 shadow-[0_20px_45px_-12px_rgba(0,0,0,0.14)] hover:shadow-[0_30px_60px_-10px_rgba(0,0,0,0.22)] transition-all duration-300 flex flex-col justify-between group hover:-translate-y-1">
            <div class="space-y-4">
              <a href="./highlights-01/" class="block aspect-[16/9] rounded-2xl overflow-hidden bg-slate-900 border border-slate-200/90 shadow-[0_15px_30px_-10px_rgba(0,0,0,0.35)] relative">
                <img src="../assets/images/cover_highlights_01.jpg" alt="Highlights #01: Padel World Summit 2026: Startup Recap" width="800" height="450" class="w-full h-full object-cover group-hover:scale-105 transition duration-700" loading="lazy" decoding="async">
              </a>

              <div class="pt-1">
                <span class="block text-xs sm:text-sm font-extrabold text-[#f2920b] uppercase tracking-wider mb-1">Highlights #01:</span>
                <h2 class="font-sans font-extrabold text-lg sm:text-xl lg:text-2xl text-slate-900 leading-snug tracking-tight">
                  Padel World Summit 2026: Startup Recap
                </h2>
                <p class="text-slate-600 text-xs sm:text-sm font-normal leading-relaxed mt-2 line-clamp-2">
                  Conversaciones una a una con las 20 startups del Innovation Arena: software, pistas inteligentes y diferenciación real.
                </p>
              </div>
            </div>

            <!-- BOTÓN ABRIR ARTÍCULO -->
            <div class="pt-5 border-t border-slate-100 mt-5">
              <a href="./highlights-01/" 
                 class="group relative w-full inline-flex items-center justify-center gap-2 px-6 py-3.5 rounded-full bg-[#f2920b] hover:bg-[#76d3f6] active:bg-[#76d3f6] text-slate-950 active:scale-95 font-heading font-black text-xs sm:text-sm uppercase tracking-wider transition-all duration-300 shadow-[0_4px_15px_rgba(242,146,11,0.25)] hover:shadow-[0_8px_25px_rgba(118,211,246,0.35)] hover:scale-[1.01] overflow-hidden">
                <span class="font-black">Leer Highlights #01</span>
                <div class="w-5 h-5 rounded-full bg-slate-950/10 group-hover:bg-slate-950 group-hover:text-white flex items-center justify-center transition-all duration-300">
                  <i data-lucide="arrow-right" class="w-3.5 h-3.5 stroke-[3] group-hover:translate-x-0.5 transition-transform duration-300"></i>
                </div>
              </a>
            </div>
          </div>

        </div>

        <!-- DEBAJO AL DESLIZAR: REPORTAJE DE LA INDUSTRIA DEL PÁDEL CENTRADO -->
        <div class="max-w-2xl mx-auto mt-14 sm:mt-20">
          <div class="bg-white border border-slate-200/90 rounded-3xl p-5 sm:p-7 shadow-[0_25px_50px_-12px_rgba(0,0,0,0.18)] hover:shadow-[0_35px_65px_-10px_rgba(0,0,0,0.28)] transition-all duration-300 flex flex-col justify-between group">
            <div class="space-y-4">
              <div class="aspect-[16/10] rounded-2xl overflow-hidden bg-slate-900 border border-slate-200/90 shadow-[0_20px_40px_-10px_rgba(0,0,0,0.4)] group-hover:scale-[1.01] transition duration-500 relative">
                <img src="../assets/images/foto-reportaje.jpg" alt="Informe PDF sobre tendencias de la industria del padel 2026" width="800" height="450" class="w-full h-full object-cover group-hover:scale-105 transition duration-700" loading="lazy" decoding="async">
                <div class="absolute inset-0 bg-gradient-to-t from-black/50 via-transparent to-transparent"></div>
                <span class="absolute bottom-3 left-3 text-[11px] font-black uppercase tracking-wider px-3 py-1 rounded-full bg-white text-slate-950 shadow-md">
                  Reportaje Oficial
                </span>
              </div>

              <div class="space-y-1.5 pt-1 text-center sm:text-left">
                <h2 class="font-heading font-black text-xl sm:text-2xl text-slate-950">
                  Reportaje de la Industria del Pádel 2026
                </h2>
                <p class="text-xs sm:text-sm text-slate-600 font-medium leading-relaxed">
                  ¿Hacia dónde va la industria del pádel? Radiografía de 116 empresas del sector: pistas, software, tendencias y proyección internacional.
                </p>
              </div>
            </div>

            <!-- FORMULARIO DESCARGA PDF -->
            <div class="pt-4 border-t border-slate-200 mt-5">
              <form onsubmit="handleReportDownload(event)" class="space-y-2.5">
                <div class="relative">
                  <input type="email" id="report-email-input" required placeholder="Introduce tu email para recibir el reportaje..." class="w-full px-4 sm:px-5 py-2.5 sm:py-3 rounded-full bg-white border border-slate-300 text-slate-950 text-xs sm:text-sm font-medium focus:outline-none focus:border-[#f2920b] shadow-inner transition">
                </div>
                <button type="submit" id="report-btn" class="group relative w-full inline-flex items-center justify-center gap-2.5 px-6 py-3 rounded-full bg-[#f2920b] hover:bg-[#76d3f6] active:bg-[#76d3f6] text-slate-950 active:scale-95 font-heading font-black text-xs sm:text-sm uppercase tracking-wider transition-all duration-300 shadow-[0_4px_15px_rgba(242,146,11,0.25)] hover:shadow-[0_8px_25px_rgba(118,211,246,0.35)] hover:scale-[1.01] overflow-hidden cursor-pointer">
                  <span id="report-btn-text">Descargar Reportaje PDF</span>
                  <div class="w-6 h-6 rounded-full bg-slate-950/10 group-hover:bg-slate-950 group-hover:text-white flex items-center justify-center transition-all duration-300">
                    <i data-lucide="download" class="w-3.5 h-3.5 stroke-[3] group-hover:translate-y-0.5 transition-transform duration-300"></i>
                  </div>
                </button>
              </form>
            </div>
          </div>
        </div>

      </div>
    </main>
  </div>

  <!-- FOOTER EN AZUL DE LLAVEROS #3478a6 -->
  <footer class="bg-[#3478a6] text-white py-8 border-t border-sky-700/40 text-xs">
    <div class="max-w-6xl mx-auto px-4 sm:px-6 flex flex-col items-center justify-between gap-4">
      <div class="flex flex-wrap items-center justify-center gap-x-4 gap-y-2 text-white/90 font-semibold">
        <a href="../" class="hover:text-white transition">Inicio</a>
        <a href="../llaveros-padel-personalizados/" class="hover:text-white transition">Llaveros de Pádel</a>
        <a href="../llaveros-tenis-personalizados/" class="hover:text-white transition">Llaveros de Tenis</a>
        <a href="../welcome-packs-torneos-padel/" class="hover:text-white transition">Welcome Packs Torneos</a>
        <a href="../llaveros-personalizados-clubs-padel/" class="hover:text-white transition">Merchandising Clubs</a>
        <a href="../camaras/" class="hover:text-white transition">Cámaras Save my Play</a>
        <a href="../franquicias-padel/" class="hover:text-white transition">Directorio Franquicias</a>
        <a href="./" class="hover:text-white transition">Blog</a>
        <a href="../politica-de-devoluciones.html" class="hover:text-white transition">Política de Devoluciones</a>
      </div>
      <div class="flex items-center gap-3">
        <img src="../assets/images/coolpadel-mascot-hd.png" alt="CoolPadel" width="32" height="32" class="h-8 w-auto">
        <span class="font-bold text-white/90">© 2026 CoolPadel Studios · All rights reserved</span>
        <span>·</span>
        <a href="https://www.instagram.com/coolpadel_/" target="_blank" rel="noopener noreferrer" class="opacity-60 hover:opacity-100 text-[11px] text-white transition">@coolpadel_</a>
      </div>
    </div>
  </footer>

  {COMMON_TRACKING_JS}
  <script>
    function handleReportDownload(e) {{
      e.preventDefault();
      const email = document.getElementById('report-email-input').value;
      const btn = document.getElementById('report-btn');
      const btnText = document.getElementById('report-btn-text');

      btn.disabled = true;
      btnText.innerText = '¡Reportaje Descargado!';
      btn.classList.add('bg-emerald-500', 'text-white');

      try {{
        fetch(GOOGLE_SHEETS_WEBHOOK_URL, {{
          method: 'POST',
          mode: 'no-cors',
          headers: {{ 'Content-Type': 'application/json' }},
          body: JSON.stringify({{ email: email, fuente: 'Blog Card Descarga PDF' }})
        }}).catch(() => {{}});
      }} catch (err) {{}}

      const link = document.createElement('a');
      link.href = '../assets/reports/padel-industry-report-es.pdf';
      link.download = 'CoolPadel-Reportaje-Industria-Padel-2026-ES.pdf';
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
    }}
  </script>
</body>
</html>"""

    os.makedirs("coolpadel-web/blog", exist_ok=True)
    with open("coolpadel-web/blog/index.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("  [OK] coolpadel-web/blog/index.html")

def generate_article_page(slug, edition_num, title, date_str, read_time, cover_img, paragraphs):
    root_prefix = "../../"
    html_paragraphs = "".join([f'<p class="text-slate-800 text-base sm:text-lg leading-relaxed">{p}</p>' if not p.startswith('<h') and not p.startswith('<ul') and not p.startswith('<ol') and not p.startswith('<div') else p for p in paragraphs])

    date_iso_map = {
        "01": "2026-08-15",
        "02": "2026-09-18",
        "03": "2026-10-14"
    }
    date_iso = date_iso_map.get(edition_num, "2026-10-14")

    html = f"""<!DOCTYPE html>
<html lang="es" class="scroll-smooth">
<head>
  <title>Highlights #{edition_num}: {title} | CoolPadel Studios</title>
  <meta name="description" content="Highlights #{edition_num}: {title}. Análisis y reflexiones sobre la industria del pádel por Javier Villoria.">
  <link rel="canonical" href="https://coolpadelstudios.com/blog/{slug}/">
  
  <!-- Open Graph / Redes Sociales -->
  <meta property="og:type" content="article">
  <meta property="og:site_name" content="CoolPadel Studios">
  <meta property="og:locale" content="es_ES">
  <meta property="og:url" content="https://coolpadelstudios.com/blog/{slug}/">
  <meta property="og:title" content="Highlights #{edition_num}: {title}">
  <meta property="og:description" content="Análisis y reflexiones sobre la industria del pádel por Javier Villoria.">
  <meta property="og:image" content="https://coolpadelstudios.com/assets/images/{cover_img}">
  <meta property="og:image:alt" content="Highlights #{edition_num}: {title}">
  
  <!-- Twitter Cards -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Highlights #{edition_num}: {title}">
  <meta name="twitter:description" content="Análisis y reflexiones sobre la industria del pádel por Javier Villoria.">
  <meta name="twitter:image" content="https://coolpadelstudios.com/assets/images/{cover_img}">

  <!-- Schema.org BlogPosting & BreadcrumbList -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@graph": [
      {{
        "@type": "BlogPosting",
        "@id": "https://coolpadelstudios.com/blog/{slug}/#article",
        "headline": "Highlights #{edition_num}: {title}",
        "description": "Highlights #{edition_num}: {title}. Análisis y reflexiones sobre la industria del pádel por Javier Villoria.",
        "image": "https://coolpadelstudios.com/assets/images/{cover_img}",
        "datePublished": "{date_iso}T10:00:00+02:00",
        "dateModified": "{date_iso}T10:00:00+02:00",
        "inLanguage": "es",
        "mainEntityOfPage": "https://coolpadelstudios.com/blog/{slug}/",
        "author": {{
          "@type": "Person",
          "name": "Javier Villoria",
          "jobTitle": "Founder",
          "url": "https://www.linkedin.com/in/javier-villoria-soleto-606737298/",
          "sameAs": "https://www.linkedin.com/in/javier-villoria-soleto-606737298/"
        }},
        "publisher": {{
          "@type": "Organization",
          "name": "CoolPadel Studios",
          "url": "https://coolpadelstudios.com",
          "logo": {{
            "@type": "ImageObject",
            "url": "https://coolpadelstudios.com/assets/images/coolpadel-mascot-hd.png"
          }}
        }}
      }},
      {{
        "@type": "BreadcrumbList",
        "itemListElement": [
          {{
            "@type": "ListItem",
            "position": 1,
            "name": "Inicio",
            "item": "https://coolpadelstudios.com/"
          }},
          {{
            "@type": "ListItem",
            "position": 2,
            "name": "Blog",
            "item": "https://coolpadelstudios.com/blog/"
          }},
          {{
            "@type": "ListItem",
            "position": 3,
            "name": "Highlights #{edition_num}: {title}",
            "item": "https://coolpadelstudios.com/blog/{slug}/"
          }}
        ]
      }}
    ]
  }}
  </script>
  {COMMON_HEAD.format(root_prefix=root_prefix)}
</head>
<body class="bg-white text-slate-900 min-h-screen relative selection:bg-[#f2920b] selection:text-white flex flex-col justify-between">

  <div>
    <!-- NAVBAR BLANCA -->
    <header class="sticky top-0 z-40 bg-white text-slate-900 border-b border-slate-200 shadow-sm w-full">
      <div class="w-full max-w-[1700px] mx-auto px-3 sm:px-6 lg:px-10 py-1.5 sm:py-0 h-auto sm:h-16 lg:h-18">
        
        <!-- DESKTOP NAVBAR (3 COLUMNAS: IZQUIERDA + CENTRO 100% + DERECHA) -->
        <div class="hidden sm:grid grid-cols-[1fr_auto_1fr] items-center h-full w-full gap-2 lg:gap-4">
          
          <!-- COLUMNA 1: OJOS + LLAVEROS, CÁMARAS PISTAS Y BLOG CENTRADOS ENTRE OJOS Y LOGO -->
          <div class="flex items-center justify-between min-w-0 h-full">
            <a href="../../" class="group py-1 inline-flex items-center shrink-0">
              <img src="../../assets/images/eyes-thumb.png?v=fixed_eyes" alt="CoolPadel Eyes" width="24" height="24" style="height: 24px; max-height: 24px; width: auto;" class="object-contain group-hover:scale-110 transition duration-300">
            </a>
            <div class="flex-1 flex items-center justify-center min-w-0 gap-5 sm:gap-6 lg:gap-9 xl:gap-11 pl-2 sm:pl-4 lg:pl-6">
              <a href="../../#llaveros" class="font-heading font-black text-xs lg:text-[13px] tracking-wider uppercase text-slate-950 hover:text-[#f2920b] transition select-none whitespace-nowrap">
                Llaveros
              </a>
              <a href="../../camaras/" class="font-heading font-black text-xs lg:text-[13px] tracking-wider uppercase text-slate-950 hover:text-[#f2920b] transition select-none whitespace-nowrap">
                Cámaras pistas
              </a>
              <a href="../" class="font-heading font-black text-xs lg:text-[13px] tracking-wider uppercase text-[#f2920b] transition select-none whitespace-nowrap border-b-2 border-[#f2920b] pb-0.5">
                Blog
              </a>
            </div>
          </div>

          <!-- COLUMNA 2: MASCOTA + COOLPADEL CENTRADO -->
          <div class="flex items-center justify-center shrink-0 px-2 lg:px-4">
            <a href="../../" class="flex items-center justify-center gap-2 sm:gap-3 group py-1">
              <img src="../../assets/images/coolpadel-mascot-hd.png" alt="Mascota CoolPadel" width="46" height="46" style="height: 46px; max-height: 46px; width: auto;" class="object-contain group-hover:scale-105 transition">
              <img src="../../assets/images/coolpadel-typography-hd.png" alt="CoolPadel" width="130" height="26" style="height: 26px; max-height: 26px; width: auto;" class="object-contain">
            </a>
          </div>

          <!-- COLUMNA 3: CADENAS DE CLUBS CENTRADO ENTRE LOGO Y SELECTOR DE IDIOMA + CONTROLES A LA DERECHA -->
          <div class="flex items-center justify-between min-w-0 h-full">
            <div class="flex-1 flex items-center justify-center min-w-0 pr-4 lg:pr-8">
              <a href="../../franquicias-padel/" class="font-heading font-black text-xs lg:text-[13px] tracking-wider uppercase text-slate-950 hover:text-[#f2920b] transition select-none whitespace-nowrap">
                Cadenas de clubs
              </a>
            </div>

            <!-- BLOQUE A LA DERECHA DEL TODO: SELECTOR IDIOMA + CONTACTAR (SIN OJOS) -->
            <div class="flex items-center gap-2 sm:gap-3 shrink-0 ml-auto">
              <!-- SELECTOR DE IDIOMA EN DESPLEGABLE COMPACTO -->
              <div class="relative inline-block text-left" id="lang-dropdown-container">
                <button type="button" onclick="toggleLangDropdown(event)" id="lang-dropdown-btn" class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-full bg-slate-100 hover:bg-slate-200 border border-slate-200 text-xs font-black text-slate-900 shadow-xs transition cursor-pointer" aria-expanded="false" aria-haspopup="true">
                  <span id="current-lang-code" class="uppercase font-black">ES</span>
                  <i data-lucide="chevron-down" class="w-3.5 h-3.5 stroke-[2.5] text-slate-600 transition-transform duration-200" id="lang-dropdown-arrow"></i>
                </button>

                <!-- MENÚ DESPLEGABLE FLOTANTE -->
                <div id="lang-dropdown-menu" class="hidden absolute right-0 mt-2 w-24 bg-white rounded-2xl shadow-[0_12px_30px_rgba(0,0,0,0.15)] border border-slate-200 py-1.5 z-50 transition-all overflow-hidden">
                  <button type="button" onclick="switchLanguage('es')" data-lang-opt="es" class="lang-opt lang-opt-active w-full text-center px-4 py-2 text-xs transition duration-150 cursor-pointer">
                    ES
                  </button>
                  <button type="button" onclick="switchLanguage('en')" data-lang-opt="en" class="lang-opt text-slate-700 hover:bg-[#f2920b] hover:text-slate-950 font-bold w-full text-center px-4 py-2 text-xs transition duration-150 cursor-pointer">
                    EN
                  </button>
                  <button type="button" onclick="switchLanguage('fr')" data-lang-opt="fr" class="lang-opt text-slate-700 hover:bg-[#f2920b] hover:text-slate-950 font-bold w-full text-center px-4 py-2 text-xs transition duration-150 cursor-pointer">
                    FR
                  </button>
                  <button type="button" onclick="switchLanguage('it')" data-lang-opt="it" class="lang-opt text-slate-700 hover:bg-[#f2920b] hover:text-slate-950 font-bold w-full text-center px-4 py-2 text-xs transition duration-150 cursor-pointer">
                    IT
                  </button>
                </div>
              </div>

              <!-- BOTÓN CONTACTAR -->
              <a href="https://wa.me/34680317486?text=Hola%20Javier" target="_blank" rel="noopener noreferrer" class="group relative inline-flex items-center gap-1.5 px-3.5 sm:px-4 py-1.5 sm:py-2 rounded-full bg-[#f2920b] hover:bg-[#76d3f6] active:bg-[#76d3f6] text-slate-950 active:scale-95 font-heading font-black text-xs sm:text-xs lg:text-sm tracking-wider uppercase transition-all duration-300 shadow-[0_4px_12px_rgba(242,146,11,0.2)] hover:scale-105 shrink-0 overflow-hidden">
                <span class="font-black">Contactar</span>
                <div class="w-4 h-4 sm:w-5 sm:h-5 rounded-full bg-slate-950/10 group-hover:bg-slate-950 group-hover:text-white flex items-center justify-center transition-all duration-300 shrink-0">
                  <i data-lucide="arrow-up-right" class="w-2.5 h-2.5 sm:w-3 sm:h-3 stroke-[3]"></i>
                </div>
              </a>
            </div>
          </div>
        </div>

        <!-- MÓVIL NAVBAR -->
        <div class="flex sm:hidden flex-col gap-1.5 py-1.5 w-full">
          <!-- FILA 1: LOGO CENTRADO (SIN OJOS A LA DERECHA) -->
          <div class="flex items-center justify-between w-full px-2">
            <a href="../../" class="py-0.5 inline-flex items-center shrink-0">
              <img src="../../assets/images/eyes-thumb.png?v=fixed_eyes" alt="CoolPadel Eyes" width="18" height="18" style="height: 18px; max-height: 18px; width: auto;" class="object-contain">
            </a>
            <a href="../../" class="flex items-center justify-center gap-1.5 py-0.5">
              <img src="../../assets/images/coolpadel-mascot-hd.png" alt="Mascota CoolPadel" width="28" height="28" style="height: 28px; max-height: 28px; width: auto;" class="object-contain">
              <img src="../../assets/images/coolpadel-typography-hd.png" alt="CoolPadel" width="90" height="18" style="height: 18px; max-height: 18px; width: auto;" class="object-contain">
            </a>
            <div class="w-[18px]"></div>
          </div>
          <!-- FILA 2: LLAVEROS + CÁMARAS PISTAS + BLOG + CADENAS DE CLUBS + IDIOMA + CONTACTAR -->
          <div class="flex items-center justify-between w-full gap-1 pt-1 border-t border-slate-100 px-1 overflow-x-auto">
            <div class="flex items-center gap-3.5 sm:gap-4 shrink-0">
              <a href="../../#llaveros" class="font-heading font-black text-[10px] tracking-wider uppercase text-slate-950 hover:text-[#f2920b] transition whitespace-nowrap">
                Llaveros
              </a>
              <a href="../../camaras/" class="font-heading font-black text-[10px] tracking-wider uppercase text-slate-950 hover:text-[#f2920b] transition whitespace-nowrap">
                Cámaras pistas
              </a>
              <a href="../" class="font-heading font-black text-[10px] tracking-wider uppercase text-[#f2920b] whitespace-nowrap border-b border-[#f2920b]">
                Blog
              </a>
              <a href="../../franquicias-padel/" class="font-heading font-black text-[10px] tracking-wider uppercase text-slate-950 hover:text-[#f2920b] transition whitespace-nowrap">
                Cadenas de clubs
              </a>
            </div>

            <div class="flex items-center gap-1 shrink-0">
              <!-- DESPLEGABLE IDIOMA MÓVIL -->
              <div class="relative inline-block text-left" id="lang-dropdown-container-mob">
                <button type="button" onclick="toggleLangDropdownMob(event)" id="lang-dropdown-btn-mob" class="inline-flex items-center gap-1 px-2 py-0.5 rounded-full bg-slate-100 hover:bg-slate-200 border border-slate-200 text-[10px] font-black text-slate-900 shadow-xs transition cursor-pointer">
                  <span id="current-lang-code-mob" class="uppercase font-black">ES</span>
                  <i data-lucide="chevron-down" class="w-2.5 h-2.5 stroke-[2.5] text-slate-600" id="lang-dropdown-arrow-mob"></i>
                </button>
                <div id="lang-dropdown-menu-mob" class="hidden absolute right-0 mt-1 w-20 bg-white rounded-2xl shadow-xl border border-slate-200 py-1 z-50 transition-all overflow-hidden">
                  <button type="button" onclick="switchLanguage('es')" data-lang-opt="es" class="lang-opt lang-opt-active w-full text-center px-3 py-1.5 text-[11px] transition duration-150 cursor-pointer">
                    ES
                  </button>
                  <button type="button" onclick="switchLanguage('en')" data-lang-opt="en" class="lang-opt text-slate-700 hover:bg-[#f2920b] hover:text-slate-950 font-bold w-full text-center px-3 py-1.5 text-[11px] transition duration-150 cursor-pointer">
                    EN
                  </button>
                  <button type="button" onclick="switchLanguage('fr')" data-lang-opt="fr" class="lang-opt text-slate-700 hover:bg-[#f2920b] hover:text-slate-950 font-bold w-full text-center px-3 py-1.5 text-[11px] transition duration-150 cursor-pointer">
                    FR
                  </button>
                  <button type="button" onclick="switchLanguage('it')" data-lang-opt="it" class="lang-opt text-slate-700 hover:bg-[#f2920b] hover:text-slate-950 font-bold w-full text-center px-3 py-1.5 text-[11px] transition duration-150 cursor-pointer">
                    IT
                  </button>
                </div>
              </div>

              <!-- BOTÓN CONTACTAR MÓVIL -->
              <a href="https://wa.me/34680317486?text=Hola%20Javier" target="_blank" rel="noopener noreferrer" class="group relative inline-flex items-center justify-center gap-1 px-2.5 py-1 rounded-full bg-[#f2920b] active:bg-[#76d3f6] text-slate-950 active:scale-95 font-heading font-black text-[10px] uppercase tracking-wider transition shadow-xs shrink-0">
                <span class="font-black">Contactar</span>
                <div class="w-3 h-3 rounded-full bg-slate-950/10 flex items-center justify-center">
                  <i data-lucide="arrow-up-right" class="w-2 h-2 stroke-[3]"></i>
                </div>
              </a>
            </div>
          </div>
        </div>

      </div>
    </header>

    <!-- ARTÍCULO COMPLETO -->
    <main class="py-10 sm:py-16 bg-white relative">
      <article class="max-w-3xl mx-auto px-4 sm:px-6">
        
        <!-- HEADER DEL ARTÍCULO -->
        <div class="space-y-4 mb-8 sm:mb-12">
          <div class="flex items-center gap-2.5 text-xs font-bold text-slate-500">
            <span class="px-3 py-1 rounded-full bg-orange-100 text-[#f2920b] font-black uppercase tracking-wider text-[11px]">
              Highlights #{edition_num}
            </span>
            <span>•</span>
            <span>{date_str}</span>
            <span>•</span>
            <span>{read_time}</span>
          </div>

          <h1 class="text-2xl sm:text-4xl font-extrabold font-sans text-slate-900 tracking-tight leading-tight">
            {title}
          </h1>

          <div class="flex items-center gap-3 pt-2 border-t border-slate-100">
            <div class="w-10 h-10 rounded-full bg-slate-950 text-white font-heading font-black flex items-center justify-center text-sm">
              JV
            </div>
            <div>
              <div class="font-heading font-black text-sm text-slate-950">Javier Villoria</div>
              <div class="text-xs text-slate-500 font-medium">Fundador de CoolPadel Studios</div>
            </div>
          </div>
        </div>

        <!-- FOTO PORTADA DEL ARTÍCULO -->
        <div class="aspect-[16/9] rounded-3xl overflow-hidden bg-slate-900 border border-slate-200/90 shadow-lg mb-8 sm:mb-12">
          <img src="../../assets/images/{cover_img}" alt="{title}" width="800" height="450" class="w-full h-full object-cover">
        </div>

        <!-- CUERPO DE TEXTO -->
        <div class="space-y-5 text-slate-800 text-base sm:text-lg leading-relaxed pt-2">
          {html_paragraphs}
        </div>

        <!-- ENLACE DISCRETO A HOME -->
        <div class="pt-6 border-t border-slate-200 mt-10 text-xs text-slate-400 text-center sm:text-left">
          <a href="../../" class="text-slate-600 hover:text-[#f2920b] underline underline-offset-2 transition font-medium">← Volver a CoolPadel Studios (Llaveros de Pádel Personalizados)</a>
        </div>

        <!-- CAJA DE SUSCRIPCIÓN FINAL A LA NEWSLETTER -->
        <div class="bg-slate-50 border border-slate-200/90 rounded-3xl p-6 sm:p-8 mt-12 sm:mt-16 text-center space-y-4 shadow-sm">
          <div class="w-12 h-12 rounded-full bg-[#f2920b]/10 text-[#f2920b] flex items-center justify-center mx-auto">
            <i data-lucide="mail" class="w-6 h-6 stroke-[2.5]"></i>
          </div>
          <div class="space-y-1.5">
            <h2 class="font-sans font-extrabold text-xl sm:text-2xl text-slate-900 tracking-tight">
              Suscríbete a Highlights by CoolPadel
            </h2>
            <p class="text-xs sm:text-sm text-slate-600 font-medium max-w-md mx-auto">
              Perspectivas, reflexiones y opiniones sobre la industria del pádel.
            </p>
          </div>
          <form onsubmit="handleNewsletterSub(event, 'Highlights #{edition_num}')" class="space-y-2.5 max-w-md mx-auto pt-2">
            <input type="email" required placeholder="Introduce tu email para suscribirte..." class="w-full px-5 py-3 rounded-full bg-white border border-slate-300 text-slate-950 text-xs sm:text-sm font-medium focus:outline-none focus:border-[#f2920b] shadow-inner transition">
            <button type="submit" class="w-full inline-flex items-center justify-center gap-2 px-6 py-3.5 rounded-full bg-[#f2920b] hover:bg-[#76d3f6] active:bg-[#76d3f6] text-slate-950 active:scale-95 font-heading font-black text-xs sm:text-sm uppercase tracking-wider transition-all duration-300 shadow-[0_4px_15px_rgba(242,146,11,0.25)] hover:shadow-[0_8px_25px_rgba(118,211,246,0.35)] hover:scale-[1.01] cursor-pointer">
              <span>Suscribirme a la Newsletter</span>
              <i data-lucide="send" class="w-3.5 h-3.5 stroke-[3]"></i>
            </button>
          </form>
        </div>

        <!-- BOTÓN VOLVER AL BLOG INFERIOR -->
        <div class="text-center pt-10">
          <a href="../" class="inline-flex items-center gap-2 px-5 py-2.5 rounded-full bg-slate-100 hover:bg-slate-200 text-slate-800 font-heading font-bold text-xs uppercase tracking-wider transition">
            <i data-lucide="arrow-left" class="w-4 h-4 stroke-[3]"></i>
            <span>Volver a todas las newsletters</span>
          </a>
        </div>

      </article>
    </main>
  </div>

  <!-- FOOTER AZUL LLAVEROS #3478a6 -->
  <footer class="bg-[#3478a6] text-white py-8 border-t border-[#2c668d] text-xs">
    <div class="max-w-6xl mx-auto px-4 sm:px-6 flex flex-col items-center justify-between gap-4">
      <div class="flex flex-wrap items-center justify-center gap-x-4 gap-y-2 text-white/90 font-semibold">
        <a href="../../" class="hover:text-white transition">Inicio</a>
        <a href="../../llaveros-padel-personalizados/" class="hover:text-white transition">Llaveros de Pádel</a>
        <a href="../../llaveros-tenis-personalizados/" class="hover:text-white transition">Llaveros de Tenis</a>
        <a href="../../welcome-packs-torneos-padel/" class="hover:text-white transition">Welcome Packs Torneos</a>
        <a href="../../llaveros-personalizados-clubs-padel/" class="hover:text-white transition">Merchandising Clubs</a>
        <a href="../../camaras/" class="hover:text-white transition">Cámaras Save my Play</a>
        <a href="../../franquicias-padel/" class="hover:text-white transition">Directorio Franquicias</a>
        <a href="../" class="hover:text-white transition">Blog</a>
        <a href="../../politica-de-devoluciones.html" class="hover:text-white transition">Política de Devoluciones</a>
      </div>
      <div class="flex items-center gap-3">
        <img src="../../assets/images/coolpadel-mascot-hd.png" alt="CoolPadel" width="32" height="32" class="h-8 w-auto">
        <span class="font-bold text-white/90">© 2026 CoolPadel Studios · All rights reserved</span>
        <span>·</span>
        <a href="https://www.instagram.com/coolpadel_/" target="_blank" rel="noopener noreferrer" class="opacity-60 hover:opacity-100 text-[11px] text-white/80 transition">@coolpadel_</a>
      </div>
    </div>
  </footer>

  {COMMON_TRACKING_JS}
</body>
</html>"""

    dest_dir = f"coolpadel-web/blog/{slug}"
    os.makedirs(dest_dir, exist_ok=True)
    with open(f"{dest_dir}/index.html", "w", encoding="utf-8") as f:
        f.write(html)
    print(f"  [OK] {dest_dir}/index.html")

def generate_all():
    print(">> Compilando Blog y Artículos dedicados...")
    generate_blog_index()

    # 1. Highlights #03
    p03 = [
        "Como todos sabemos, España y Argentina han monopolizado el pádel durante las últimas décadas, incluida toda la industria.",
        "Pero ya no son mercados atractivos para la mayoría de las marcas.",
        "Las empresas que operan allí tienen el know-how, pero las nuevas oportunidades de crecimiento son mínimas.",
        "<strong>¿Por qué?</strong>",
        "Márgenes bajos. Pocos clubes nuevos. Demanda saturada. Hace poco, un fabricante de pistas me comentaba que España representaba menos del 2% de su facturación total.",
        "<strong>¿Dónde está la verdadera oportunidad de negocio entonces?</strong>",
        "En los mercados emergentes, donde el pádel crece a gran velocidad.",
        "Pero las marcas internacionales no conocen el mercado local. ¿Cuál es la solución habitual? Encontrar un distribuidor local. Alguien consolidado en ese país, con una red activa de clubes, entrenadores y jugadores que les dé acceso inmediato al mercado.",
        '<h2 class="font-heading font-black text-xl sm:text-2xl text-slate-950 pt-4">El proceso de desarrollo del pádel en un país</h2>',
        "Normalmente suele seguir siempre el mismo patrón de 5 etapas:",
        '<ol class="list-decimal pl-6 space-y-2 font-medium text-slate-800"><li><strong>Clubes pioneros:</strong> Se construyen las primeras pistas y se introducen los primeros jugadores entusiastas.</li><li><strong>Competencia inicial:</strong> Unas pocas marcas de palas, ropa, software y tecnología compiten por la cuota inicial de mercado.</li><li><strong>Alternativas locales:</strong> Surgen marcas y proyectos locales que compiten con las grandes gracias a su ventaja geográfica y cercanía.</li><li><strong>Profesionalización técnica:</strong> Aparece la necesidad de traer entrenadores y academias internacionales para desarrollar jugadores y elevar el nivel medio.</li><li><strong>Ecosistema maduro:</strong> Llega el resto del ecosistema: agencias de marketing, medios especializados, grandes patrocinadores y torneos Premier Padel.</li></ol>',
        '<h2 class="font-heading font-black text-xl sm:text-2xl text-slate-950 pt-4">¿A qué velocidad avanza este proceso?</h2>',
        "Necesitas dos cosas fundamentales: <strong>jugadores y capital</strong>. Y tienen que crecer exactamente al mismo ritmo. Ya hemos visto varias veces (como en Suecia o Chile) lo que ocurre cuando la inversión se precipita antes de que exista una base real y fiel de jugadores.",
        "En mercados como Estados Unidos, muchas marcas y clubes están invirtiendo fuerte para posicionarse pronto. Verán el retorno cuando el mercado madure, pero está llevando más tiempo del previsto porque el deporte aún es poco conocido. Todavía no hay suficientes jugadores para rentabilizar inversiones iniciales tan grandes.",
        "Cuando un mercado llega a esa fase de competencia, la batalla pasa al interior del club: retención, experiencia del jugador y diferenciación.",
        "Para un club o academia, retener a sus jugadores es clave, y eso se consigue cuidando la identidad y haciendo que su experiencia dentro y fuera de la pista sea memorable."
    ]
    generate_article_page(
        slug="highlights-03",
        edition_num="03",
        title="¿Cómo crece realmente la industria del pádel?",
        date_str="Octubre 2026",
        read_time="Lectura 3 min",
        cover_img="cover_highlights_03.jpg",
        paragraphs=p03
    )

    # 2. Highlights #02
    p02 = [
        "Si estás metido en la industria del pádel y no te acabas de caer de un árbol, habrás oído hablar una y otra vez del sueño de ser deporte olímpico.",
        "Los Ángeles 2028, Brisbane 2032… o tal vez ya para 2040.",
        "La realidad es que estamos lejos de serlo.",
        "O, al menos, deberíamos estarlo.",
        '<h2 class="font-heading font-black text-xl sm:text-2xl text-slate-950 pt-4">¿Por qué un deporte global precede al sueño olímpico?</h2>',
        "Que sí, que el breakdance lo fue en París 2024. Justo por eso no deberíamos precipitarnos.",
        "Para llegar a ser olímpico, antes deberías ser un deporte global. Y no al revés.",
        "Debería ser un premio, más que un medio. O eso pienso yo.",
        "Y sí, el pádel está lejos de ser un deporte global. Muy lejos. Nos guste o no. Por mucho que sea el <em>“fastest-growing sport”</em> del mundo.",
        "En España cuesta hacerse a la idea de esto porque es uno de los deportes más practicados con mucha diferencia. Esta semana, un amigo me preguntaba si era más popular a nivel mundial el pádel o el golf.",
        "La realidad es que, fuera de los países con gran tradición, en vez de decir que vas a jugar al pádel, dices que vas a jugar al tenis, pero con paredes. Porque, si no, la gente no te entiende. Y acabas teniendo que enseñarles un vídeo porque siguen sin pillarlo.",
        "Solo es cuestión de tiempo. Las pistas no se construyen de la noche a la mañana. Y, en los países sin tradición padelística, lleva años concienciar a la población.",
        "Antes de que el pádel se vuelva deporte olímpico, enfócate en lo que hace sostenible a tu club hoy: comunidad, identidad y fidelización real de jugadores."
    ]
    generate_article_page(
        slug="highlights-02",
        edition_num="02",
        title="El Pádel debería estar lejos de ser un deporte olímpico. ¿Por qué?",
        date_str="Septiembre 2026",
        read_time="Lectura 3 min",
        cover_img="cover_highlights_02.jpg",
        paragraphs=p02
    )

    # 3. Highlights #01
    p01 = [
        "Hablar con las 20 startups del Innovation Arena en el Padel World Summit, una por una, es uno de los mejores termómetros para saber en qué punto real se encuentra la industria del pádel.",
        "En términos generales, el mercado del pádel todavía está en una fase temprana: está fragmentado, es local y es tremendamente dinámico. Cada país tiene sus propios modelos de negocio y, en muchos casos, cuesta ver una diferenciación clara entre soluciones.",
        "Sin embargo, en mercados consolidados como España, unas pocas marcas ya dominan de forma casi indiscutible. Para una startup que empieza, intentar batirlas en su propio terreno es una batalla cuesta arriba.",
        '<h2 class="font-heading font-black text-xl sm:text-2xl text-slate-950 pt-4">Construir sobre los gigantes vs Intentar reemplazarlos</h2>',
        "Un ejemplo claro es el software de gestión y reservas: aunque tu herramienta sea algo mejor que Playtomic, desbancarlos de un club consolidado es extremadamente difícil.",
        "Una opción es centrarse en nuevos mercados emergentes, pero las probabilidades juegan en contra. Por eso, los proyectos que más me gustaron fueron los que no intentan reemplazar el sistema existente del club, sino integrarse sobre él aportando un valor claro y diferencial sin fricción técnica.",
        "La clave en esta etapa del pádel no es reinventar la rueda, sino resolver cuellos de botella reales para los gerentes: aumentar la ocupación en horas valle, mejorar la recurrencia de los jugadores y profesionalizar la imagen y el merchandising oficial del club."
    ]
    generate_article_page(
        slug="highlights-01",
        edition_num="01",
        title="Padel World Summit 2026: Startup Recap",
        date_str="Agosto 2026",
        read_time="Lectura 4 min",
        cover_img="cover_highlights_01.jpg",
        paragraphs=p01
    )

generate_blog_html = generate_all

if __name__ == "__main__":
    generate_all()
