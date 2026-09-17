import os
import json
from translations_data import TRANSLATIONS

def get_base_html(active_lang="es", is_subfolder=False):
    t = TRANSLATIONS[active_lang]
    asset_prefix = "../" if is_subfolder else ""
    
    # Pre-calcular JSON de traducciones para inyectar en JS
    translations_json = json.dumps(TRANSLATIONS, ensure_ascii=False)

    og_locales = {"es": "es_ES", "en": "en_US", "fr": "fr_FR", "it": "it_IT"}
    og_locale = og_locales.get(active_lang, "es_ES")

    html = f"""<!DOCTYPE html>
<html lang="{active_lang}" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{t['meta_title']}</title>
  <meta name="description" content="{t['meta_desc']}">
  <meta name="keywords" content="llaveros personalizados padel, llaveros personalizados tenis, merchandising clubes padel, regalos torneos padel, grabacion partidos padel, camaras padel ia, save my play, informe industria padel 2026, coolpadel">
  <meta name="author" content="CoolPadel">
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">
  <link rel="canonical" href="https://coolpadelstudios.com/{active_lang + '/' if is_subfolder else ''}">
  <link rel="icon" type="image/png" href="{asset_prefix}assets/images/Ojos logo.png">
  <link rel="apple-touch-icon" sizes="180x180" href="{asset_prefix}assets/images/Ojos logo.png">
  <link rel="manifest" href="{asset_prefix}site.webmanifest">
  <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
  <meta http-equiv="Pragma" content="no-cache">
  <meta http-equiv="Expires" content="0">
  <meta name="theme-color" content="#0b1626">
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
  <meta name="apple-mobile-web-app-title" content="CoolPadel">

  <!-- Etiquetas Hreflang para SEO Internacional Multilingüe -->
  <link rel="alternate" hreflang="es" href="https://coolpadelstudios.com/">
  <link rel="alternate" hreflang="en" href="https://coolpadelstudios.com/en/">
  <link rel="alternate" hreflang="fr" href="https://coolpadelstudios.com/fr/">
  <link rel="alternate" hreflang="it" href="https://coolpadelstudios.com/it/">
  <link rel="alternate" hreflang="x-default" href="https://coolpadelstudios.com/">
  
  <!-- Geo-Targeting & International SEO -->
  <meta name="geo.region" content="ES">
  <meta name="geo.placename" content="España">
  <meta name="geo.position" content="40.4168;-3.7038">
  <meta name="ICBM" content="40.4168, -3.7038">
  <meta name="language" content="{active_lang}">
  <meta name="coverage" content="Worldwide">
  <meta name="distribution" content="Global">
  <meta name="rating" content="General">

  <!-- Open Graph / WhatsApp / Facebook / LinkedIn Previews -->
  <meta property="og:type" content="website">
  <meta property="og:locale" content="{og_locale}">
  <meta property="og:site_name" content="CoolPadel">
  <meta property="og:url" content="https://coolpadelstudios.com/{active_lang + '/' if is_subfolder else ''}">
  <meta property="og:title" content="{t['meta_title']}">
  <meta property="og:description" content="{t['meta_desc']}">
  <meta property="og:image" content="https://coolpadelstudios.com/assets/images/slide-1.jpg">
  <meta property="og:image:alt" content="Llaveros personalizados CoolPadel para clubs de padel y tenis">

  <!-- Twitter / X Cards -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{t['meta_title']}">
  <meta name="twitter:description" content="{t['meta_desc']}">
  <meta name="twitter:image" content="https://coolpadelstudios.com/assets/images/slide-1.jpg">

  <!-- Datos Estructurados Schema.org JSON-LD (Google Rich Snippets & Generative AI / GEO) -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@graph": [
      {{
        "@type": "Organization",
        "@id": "https://coolpadelstudios.com/#organization",
        "name": "CoolPadel",
        "url": "https://coolpadelstudios.com",
        "logo": {{
          "@type": "ImageObject",
          "url": "https://coolpadelstudios.com/assets/images/coolpadel-mascot-hd.png"
        }},
        "description": "Ecosistema integral de merchandising y soluciones tecnológicas para clubes de padel, tenis, marcas y federaciones de todo el mundo.",
        "areaServed": [
          "ES", "IT", "FR", "PT", "SE", "DE", "GB", "US", "AE", "Worldwide"
        ],
        "knowsAbout": [
          "Llaveros personalizados de padel y tenis",
          "Merchandising para clubes deportivos",
          "Grabación en pista con Inteligencia Artificial",
          "Save my Play",
          "Industria del padel y tendencias de mercado"
        ],
        "contactPoint": {{
          "@type": "ContactPoint",
          "telephone": "+34-680-31-74-86",
          "contactType": "customer service",
          "email": "javier@coolpadelstudios.com",
          "availableLanguage": ["Spanish", "English", "French", "Italian"]
        }}
      }},
      {{
        "@type": "WebSite",
        "@id": "https://coolpadelstudios.com/#website",
        "url": "https://coolpadelstudios.com",
        "name": "CoolPadel",
        "publisher": {{ "@id": "https://coolpadelstudios.com/#organization" }},
        "inLanguage": "{active_lang}"
      }},
      {{
        "@type": "Product",
        "name": "Llaveros Personalizados para Clubs de Padel y Tenis",
        "description": "Llaveros de goma 3D personalizados con el logo oficial del club o comunidad. Muestras desde 15€, pedidos a partir de 100 unidades y envíos incluidos.",
        "brand": {{ "@type": "Brand", "name": "CoolPadel" }},
        "offers": {{
          "@type": "AggregateOffer",
          "priceCurrency": "EUR",
          "lowPrice": "1.50",
          "highPrice": "3.00",
          "offerCount": "4"
        }}
      }},
      {{
        "@type": "Service",
        "name": "Save my Play - Grabación de Pistas con Inteligencia Artificial",
        "description": "Sistema de cámaras inteligentes con IA para pistas de padel y tenis. Grabación de partidos, highlights automáticos y repeticiones instantáneas con instalación en 5 minutos.",
        "provider": {{ "@id": "https://coolpadelstudios.com/#organization" }}
      }},
      {{
        "@type": "FAQPage",
        "mainEntity": [
          {{
            "@type": "Question",
            "name": "{t['faq_q1']}",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "{t['faq_a1']}"
            }}
          }},
          {{
            "@type": "Question",
            "name": "{t['faq_q2']}",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "{t['faq_a2']}"
            }}
          }},
          {{
            "@type": "Question",
            "name": "{t['faq_q3']}",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "{t['faq_a3']}"
            }}
          }}
        ]
      }}
    ]
  }}
  </script>
  
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;600;700;800;900&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {{
      darkMode: 'class',
      theme: {{
        extend: {{
          fontFamily: {{
            outfit: ['Outfit', 'sans-serif'],
            jakarta: ['Plus Jakarta Sans', 'sans-serif'],
          }},
          colors: {{
            cool: {{
              navy: '#091322',
              dark: '#0e1d33',
              card: '#132845',
              blue: '#0284c7',
              cyan: '#76d3f6',
              orange: '#f2920b',
              amber: '#d97706'
            }}
          }},
          animation: {{
            'ticker-slow': 'tickerSlow 9s linear infinite',
            'ticker-trusted': 'tickerSlow 12s linear infinite',
          }},
          keyframes: {{
            tickerSlow: {{
              '0%': {{ transform: 'translateX(0%)' }},
              '100%': {{ transform: 'translateX(-50%)' }}
            }}
          }}
        }}
      }}
    }}
  </script>
  <script src="https://unpkg.com/lucide@latest"></script>
  <style>
    *, *::before, *::after {{
      box-sizing: border-box;
    }}
    html, body {{
      overflow-x: hidden;
      width: 100%;
      -webkit-text-size-adjust: 100%;
    }}
    body {{ font-family: 'Plus Jakarta Sans', sans-serif; }}
    h1, h2, h3, h4, .font-heading {{ font-family: 'Outfit', sans-serif; }}
    
    .ticker-wrap {{
      width: 100%;
      overflow: hidden;
      white-space: nowrap;
    }}
    .ticker-content {{
      display: inline-flex;
      white-space: nowrap;
    }}

    /* Coverflow 3D Styles */
    .coverflow-wrapper {{
      perspective: 1400px;
      overflow: hidden;
      width: 100%;
    }}
    .coverflow-slide {{
      position: absolute;
      transition: transform 0.65s cubic-bezier(0.25, 1, 0.5, 1), opacity 0.65s ease, filter 0.65s ease, box-shadow 0.65s ease;
      transform-style: preserve-3d;
      will-change: transform, opacity;
      backface-visibility: hidden;
      -webkit-backface-visibility: hidden;
      cursor: pointer;
    }}
    .coverflow-slide.active {{
      transform: translateX(0%) scale(1);
      z-index: 30;
      opacity: 1;
      filter: blur(0px);
      box-shadow: 0 20px 45px -12px rgba(0, 0, 0, 0.65);
      cursor: default;
    }}
    .coverflow-slide.prev {{
      transform: translateX(-56%) scale(0.88);
      z-index: 20;
      opacity: 0.65;
      filter: blur(1.5px);
      cursor: pointer;
      box-shadow: 0 16px 32px -8px rgba(0, 0, 0, 0.55);
    }}
    .coverflow-slide.next {{
      transform: translateX(56%) scale(0.88);
      z-index: 20;
      opacity: 0.65;
      filter: blur(1.5px);
      cursor: pointer;
      box-shadow: 0 16px 32px -8px rgba(0, 0, 0, 0.55);
    }}
    @media (min-width: 768px) {{
      .coverflow-slide.prev {{
        transform: translateX(-68%) scale(0.86);
      }}
      .coverflow-slide.next {{
        transform: translateX(68%) scale(0.86);
      }}
    }}
    @media (min-width: 1280px) {{
      .coverflow-slide.prev {{
        transform: translateX(-72%) scale(0.86);
      }}
      .coverflow-slide.next {{
        transform: translateX(72%) scale(0.86);
      }}
      .coverflow-slide.prev:hover {{
        transform: translateX(-69%) scale(0.88);
        opacity: 0.85;
      }}
      .coverflow-slide.next:hover {{
        transform: translateX(69%) scale(0.88);
        opacity: 0.85;
      }}
    }}
    .coverflow-slide.prev:hover, .coverflow-slide.next:hover {{
      opacity: 0.85;
    }}

    .glass-card-clean {{
      background: rgba(14, 29, 51, 0.75);
      backdrop-filter: blur(12px);
      border: 1px solid rgba(56, 189, 248, 0.18);
    }}

    /* Slider de calculadora sin marcas ni selección accidental */
    #calc-slider-box, #slider-track, #slider-thumb, .tier-btn {{
      touch-action: none;
      -webkit-touch-callout: none;
      -webkit-user-select: none;
      -khtml-user-select: none;
      -moz-user-select: none;
      -ms-user-select: none;
      user-select: none;
      outline: none !important;
      -webkit-tap-highlight-color: transparent;
    }}
  </style>
</head>
<body class="bg-[#0b1626] text-slate-100 min-h-screen relative selection:bg-cool-orange selection:text-white overflow-x-hidden w-full">

  <!-- 1. TOP BAR NEGRA: INFORME EXCLUSIVO INTERCALADO CON NEWSLETTER COOLPADEL -->
  <div class="bg-black border-b border-neutral-800 py-1.5 sm:py-2 ticker-wrap text-[11px] sm:text-xs text-neutral-200 tracking-wider z-50 relative">
    <div class="ticker-content animate-ticker-slow flex items-center font-medium">
      
      <!-- BLOQUE 1 -->
      <a href="#informe" class="inline-flex items-center hover:text-white transition px-5 sm:px-8 shrink-0">
        <span class="w-1.5 h-1.5 rounded-full bg-[#f2920b] inline-block mr-2.5"></span>
        <span data-i18n="top_ticker">{t['top_ticker']}</span>
      </a>
      <span class="text-neutral-600 select-none">·</span>

      <a href="https://www.linkedin.com/pulse/padel-world-summit-2026-startup-recap-javier-villoria-soleto-c7hle/" target="_blank" class="inline-flex items-center hover:text-white transition px-5 sm:px-8 text-neutral-300 hover:text-[#76d3f6] shrink-0">
        <span class="w-1.5 h-1.5 rounded-full bg-[#76d3f6] inline-block mr-2.5"></span>
        <span data-i18n="top_ticker_newsletter">{t['top_ticker_newsletter']}</span>
      </a>
      <span class="text-neutral-600 select-none">·</span>

      <a href="#informe" class="inline-flex items-center hover:text-white transition px-5 sm:px-8 shrink-0">
        <span class="w-1.5 h-1.5 rounded-full bg-[#f2920b] inline-block mr-2.5"></span>
        <span data-i18n="top_ticker">{t['top_ticker']}</span>
      </a>
      <span class="text-neutral-600 select-none">·</span>

      <a href="https://www.linkedin.com/pulse/padel-world-summit-2026-startup-recap-javier-villoria-soleto-c7hle/" target="_blank" class="inline-flex items-center hover:text-white transition px-5 sm:px-8 text-neutral-300 hover:text-[#76d3f6] shrink-0">
        <span class="w-1.5 h-1.5 rounded-full bg-[#76d3f6] inline-block mr-2.5"></span>
        <span data-i18n="top_ticker_newsletter">{t['top_ticker_newsletter']}</span>
      </a>
      <span class="text-neutral-600 select-none">·</span>

      <!-- BLOQUE 2 (DUPLICADO PARA ANIMACIÓN INFINITA SUAVE AL 50%) -->
      <a href="#informe" class="inline-flex items-center hover:text-white transition px-5 sm:px-8 shrink-0">
        <span class="w-1.5 h-1.5 rounded-full bg-[#f2920b] inline-block mr-2.5"></span>
        <span data-i18n="top_ticker">{t['top_ticker']}</span>
      </a>
      <span class="text-neutral-600 select-none">·</span>

      <a href="https://www.linkedin.com/pulse/padel-world-summit-2026-startup-recap-javier-villoria-soleto-c7hle/" target="_blank" class="inline-flex items-center hover:text-white transition px-5 sm:px-8 text-neutral-300 hover:text-[#76d3f6] shrink-0">
        <span class="w-1.5 h-1.5 rounded-full bg-[#76d3f6] inline-block mr-2.5"></span>
        <span data-i18n="top_ticker_newsletter">{t['top_ticker_newsletter']}</span>
      </a>
      <span class="text-neutral-600 select-none">·</span>

      <a href="#informe" class="inline-flex items-center hover:text-white transition px-5 sm:px-8 shrink-0">
        <span class="w-1.5 h-1.5 rounded-full bg-[#f2920b] inline-block mr-2.5"></span>
        <span data-i18n="top_ticker">{t['top_ticker']}</span>
      </a>
      <span class="text-neutral-600 select-none">·</span>

      <a href="https://www.linkedin.com/pulse/padel-world-summit-2026-startup-recap-javier-villoria-soleto-c7hle/" target="_blank" class="inline-flex items-center hover:text-white transition px-5 sm:px-8 text-neutral-300 hover:text-[#76d3f6] shrink-0">
        <span class="w-1.5 h-1.5 rounded-full bg-[#76d3f6] inline-block mr-2.5"></span>
        <span data-i18n="top_ticker_newsletter">{t['top_ticker_newsletter']}</span>
      </a>
      <span class="text-neutral-600 select-none">·</span>

    </div>
  </div>

  <!-- 2. NAVBAR BLANCA RESPONSIVE: SELECTOR DESPLEGABLE DE IDIOMA + LOGOS + CONTACTAR -->
  <header class="sticky top-0 z-40 bg-white text-slate-900 border-b border-slate-200 shadow-sm w-full">
    <div class="w-full max-w-[1700px] mx-auto px-3 sm:px-6 lg:px-10 py-1.5 sm:py-0 h-auto sm:h-20 lg:h-22">
      
      <!-- DESKTOP NAVBAR (3 COLUMNAS: IZQUIERDA + CENTRO 100% + DERECHA) -->
      <div class="hidden sm:grid grid-cols-[1fr_auto_1fr] items-center h-full w-full gap-2 lg:gap-4">
        
        <!-- COLUMNA 1: OJOS + TENIS Y PADEL (100% CENTRADO ENTRE OJOS Y MASCOTA) -->
        <div class="flex items-center justify-between min-w-0 h-full">
          <a href="#" class="group py-1 inline-flex items-center shrink-0">
            <img src="{asset_prefix}assets/images/Ojos logo.png" alt="CoolPadel Eyes" class="h-6 sm:h-7 lg:h-8 w-auto object-contain group-hover:scale-110 transition duration-300">
          </a>
          <div class="flex-1 flex items-center justify-center px-2">
            <span data-i18n="nav_tenis_padel" class="font-heading font-black text-xs sm:text-sm lg:text-base tracking-wider uppercase text-slate-950 select-none whitespace-nowrap">
              {t['nav_tenis_padel']}
            </span>
          </div>
        </div>

        <!-- COLUMNA 2: MASCOTA + COOLPADEL (MATEMÁTICAMENTE 100% CENTRADO EN PANTALLA) -->
        <div class="flex items-center justify-center shrink-0 px-2 lg:px-4">
          <a href="#" class="flex items-center justify-center gap-2 sm:gap-3 group py-1">
            <img src="{asset_prefix}assets/images/coolpadel-mascot-hd.png" alt="Mascota CoolPadel" class="h-9 sm:h-12 lg:h-14 w-auto object-contain group-hover:scale-105 transition max-h-[58px]">
            <img src="{asset_prefix}assets/images/coolpadel-typography-hd.png" alt="CoolPadel" class="h-5 sm:h-7 lg:h-9 w-auto object-contain">
          </a>
        </div>

        <!-- COLUMNA 3: IDIOMAS DROPDOWN + CONTACTAR + OJOS DERECHA (SIEMPRE 100% VISIBLES) -->
        <div class="flex items-center justify-end min-w-0 h-full gap-2 sm:gap-3 lg:gap-5">
          
          <!-- SELECTOR DE IDIOMA EN DESPLEGABLE COMPACTO -->
          <div class="relative inline-block text-left" id="lang-dropdown-container">
            <button type="button" onclick="toggleLangDropdown(event)" id="lang-dropdown-btn" class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-full bg-slate-100 hover:bg-slate-200 border border-slate-200 text-xs font-black text-slate-900 shadow-xs transition cursor-pointer" aria-expanded="false" aria-haspopup="true">
              <span id="current-lang-code" class="uppercase font-black">{active_lang.upper()}</span>
              <i data-lucide="chevron-down" class="w-3.5 h-3.5 stroke-[2.5] text-slate-600 transition-transform duration-200" id="lang-dropdown-arrow"></i>
            </button>

            <!-- MENÚ DESPLEGABLE FLOTANTE -->
            <div id="lang-dropdown-menu" class="hidden absolute right-0 mt-2 w-24 bg-white rounded-2xl shadow-[0_12px_30px_rgba(0,0,0,0.15)] border border-slate-200 py-1.5 z-50 transition-all overflow-hidden">
              <button type="button" onclick="switchLanguage('es')" data-lang-opt="es" class="lang-opt {'bg-[#f2920b] text-slate-950 font-black' if active_lang=='es' else 'text-slate-700 hover:bg-slate-100 font-bold'} w-full text-center px-4 py-2 text-xs transition cursor-pointer">
                ES
              </button>
              <button type="button" onclick="switchLanguage('en')" data-lang-opt="en" class="lang-opt {'bg-[#f2920b] text-slate-950 font-black' if active_lang=='en' else 'text-slate-700 hover:bg-slate-100 font-bold'} w-full text-center px-4 py-2 text-xs transition cursor-pointer">
                EN
              </button>
              <button type="button" onclick="switchLanguage('fr')" data-lang-opt="fr" class="lang-opt {'bg-[#f2920b] text-slate-950 font-black' if active_lang=='fr' else 'text-slate-700 hover:bg-slate-100 font-bold'} w-full text-center px-4 py-2 text-xs transition cursor-pointer">
                FR
              </button>
              <button type="button" onclick="switchLanguage('it')" data-lang-opt="it" class="lang-opt {'bg-[#f2920b] text-slate-950 font-black' if active_lang=='it' else 'text-slate-700 hover:bg-slate-100 font-bold'} w-full text-center px-4 py-2 text-xs transition cursor-pointer">
                IT
              </button>
            </div>
          </div>

          <!-- BOTÓN CONTACTAR -->
          <a id="nav-contact-btn" href="https://wa.me/34680317486?text={t['wa_prefilled_msg']}" 
             target="_blank" 
             class="group relative inline-flex items-center gap-1.5 sm:gap-2 px-3.5 sm:px-5 lg:px-6 py-2 sm:py-2.5 rounded-full bg-[#f2920b] hover:bg-[#76d3f6] active:bg-[#76d3f6] text-slate-950 active:scale-95 font-heading font-black text-xs sm:text-sm lg:text-base tracking-wider uppercase transition-all duration-300 shadow-[0_4px_15px_rgba(242,146,11,0.25)] hover:shadow-[0_10px_25px_rgba(118,211,246,0.4)] hover:scale-105 shrink-0 overflow-hidden">
            <span data-i18n="nav_contact" class="font-black">{t['nav_contact']}</span>
            <div class="w-5 h-5 sm:w-6 sm:h-6 rounded-full bg-slate-950/10 group-hover:bg-slate-950 group-hover:text-white flex items-center justify-center transition-all duration-300 shrink-0">
              <i data-lucide="arrow-up-right" class="w-3 h-3 sm:w-3.5 sm:h-3.5 stroke-[3] group-hover:translate-x-0.5 group-hover:-translate-y-0.5 transition-transform duration-300"></i>
            </div>
          </a>

          <!-- OJOS A LA DERECHA DEL TODO (SIEMPRE VISIBLE) -->
          <a href="#" class="group py-1 inline-flex items-center shrink-0">
            <img src="{asset_prefix}assets/images/Ojos logo.png" alt="CoolPadel Eyes" class="h-6 sm:h-7 lg:h-8 w-auto object-contain group-hover:scale-110 transition duration-300">
          </a>
        </div>

      </div>

      <!-- MÓVIL NAVBAR (2 FILAS RESPONSIVE PERFECTAMENTE ALINEADAS Y FLUIDAS) -->
      <div class="flex sm:hidden flex-col gap-1.5 py-1.5 w-full">
        <!-- FILA 1: OJOS IZQ + [MASCOTA + COOLPADEL CENTRADO] + OJOS DER -->
        <div class="flex items-center justify-between w-full">
          <a href="#" class="py-0.5 inline-flex items-center shrink-0">
            <img src="{asset_prefix}assets/images/Ojos logo.png" alt="CoolPadel Eyes" class="h-5 w-auto object-contain">
          </a>
          <a href="#" class="flex items-center justify-center gap-1.5 py-0.5">
            <img src="{asset_prefix}assets/images/coolpadel-mascot-hd.png" alt="Mascota CoolPadel" class="h-6.5 w-auto object-contain">
            <img src="{asset_prefix}assets/images/coolpadel-typography-hd.png" alt="CoolPadel" class="h-4.5 w-auto object-contain">
          </a>
          <a href="#" class="py-0.5 inline-flex items-center shrink-0">
            <img src="{asset_prefix}assets/images/Ojos logo.png" alt="CoolPadel Eyes" class="h-5 w-auto object-contain">
          </a>
        </div>
        
        <!-- FILA 2: TENIS Y PADEL + SELECTOR IDIOMAS DESPLEGABLE + BOTÓN CONTACTAR -->
        <div class="flex items-center justify-between w-full gap-1 pt-1 border-t border-slate-100">
          <span data-i18n="nav_tenis_padel" class="font-heading font-black text-[9.5px] tracking-wider uppercase text-slate-950 select-none whitespace-nowrap shrink-0">
            {t['nav_tenis_padel']}
          </span>

          <div class="flex items-center gap-1.5 shrink-0">
            <!-- DESPLEGABLE IDIOMA MÓVIL -->
            <div class="relative inline-block text-left" id="lang-dropdown-container-mob">
              <button type="button" onclick="toggleLangDropdownMob(event)" id="lang-dropdown-btn-mob" class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full bg-slate-100 hover:bg-slate-200 border border-slate-200 text-[10px] font-black text-slate-900 shadow-xs transition cursor-pointer">
                <span id="current-lang-code-mob" class="uppercase font-black">{active_lang.upper()}</span>
                <i data-lucide="chevron-down" class="w-3 h-3 stroke-[2.5] text-slate-600" id="lang-dropdown-arrow-mob"></i>
              </button>
              <div id="lang-dropdown-menu-mob" class="hidden absolute right-0 mt-1 w-20 bg-white rounded-2xl shadow-xl border border-slate-200 py-1 z-50 transition-all overflow-hidden">
                <button type="button" onclick="switchLanguage('es')" data-lang-opt="es" class="lang-opt {'bg-[#f2920b] text-slate-950 font-black' if active_lang=='es' else 'text-slate-700 hover:bg-slate-100 font-bold'} w-full text-center px-3 py-1.5 text-[11px] transition cursor-pointer">
                  ES
                </button>
                <button type="button" onclick="switchLanguage('en')" data-lang-opt="en" class="lang-opt {'bg-[#f2920b] text-slate-950 font-black' if active_lang=='en' else 'text-slate-700 hover:bg-slate-100 font-bold'} w-full text-center px-3 py-1.5 text-[11px] transition cursor-pointer">
                  EN
                </button>
                <button type="button" onclick="switchLanguage('fr')" data-lang-opt="fr" class="lang-opt {'bg-[#f2920b] text-slate-950 font-black' if active_lang=='fr' else 'text-slate-700 hover:bg-slate-100 font-bold'} w-full text-center px-3 py-1.5 text-[11px] transition cursor-pointer">
                  FR
                </button>
                <button type="button" onclick="switchLanguage('it')" data-lang-opt="it" class="lang-opt {'bg-[#f2920b] text-slate-950 font-black' if active_lang=='it' else 'text-slate-700 hover:bg-slate-100 font-bold'} w-full text-center px-3 py-1.5 text-[11px] transition cursor-pointer">
                  IT
                </button>
              </div>
            </div>

            <a id="nav-contact-btn-mob" href="https://wa.me/34680317486?text={t['wa_prefilled_msg']}" 
               target="_blank" 
               class="group relative inline-flex items-center justify-center gap-1 px-3 py-1 rounded-full bg-[#f2920b] active:bg-[#76d3f6] text-slate-950 active:scale-95 font-heading font-black text-[10px] uppercase tracking-wider transition-all duration-300 shadow-sm shrink-0">
              <span data-i18n="nav_contact" class="font-black">{t['nav_contact']}</span>
              <div class="w-3.5 h-3.5 rounded-full bg-slate-950/10 flex items-center justify-center">
                <i data-lucide="arrow-up-right" class="w-2.5 h-2.5 stroke-[3]"></i>
              </div>
            </a>
          </div>
        </div>
      </div>

    </div>
  </header>

  <!-- 3. COVERFLOW ROTATIVO (ALTURA BALANCEADA PARA VER LOGOS DE CLUBES EN PANTALLA COMPLETA) -->
  <section class="relative bg-white overflow-hidden select-none pt-2 pb-1 sm:pt-4 sm:pb-2">
    <div class="w-full max-w-full mx-auto px-0 sm:px-4">
      
      <div class="relative w-full h-[320px] sm:h-[380px] lg:h-[410px] flex items-center justify-center coverflow-wrapper">
        
        <!-- SLIDE 1: LLAVEROS PARA TU CLUB/COMUNIDAD (SLIDE-1.JPG) -->
        <div id="coverflow-0" class="coverflow-slide active w-[90%] sm:w-[72%] lg:w-[62%] max-w-[840px] h-[300px] sm:h-[360px] lg:h-[390px] rounded-3xl overflow-hidden bg-neutral-900">
          <img src="{asset_prefix}assets/images/slide-1.jpg" alt="Llaveros personalizados para club de padel y tenis CoolPadel" class="w-full h-full object-cover" fetchpriority="high" decoding="async">
          
          <!-- Slide Content (Nike Bottom Left Layout) -->
          <div class="slide-caption absolute bottom-4 sm:bottom-7 left-4 sm:left-8 z-30 space-y-2 sm:space-y-3 pointer-events-auto pr-4 max-w-[92%] sm:max-w-[85%]">
            <h1 data-i18n="slide1_title" class="text-xl sm:text-3xl lg:text-4xl font-black font-heading text-white uppercase tracking-tight leading-[1.15]">
              {t['slide1_title']}
            </h1>
            <div>
              <a href="#llaveros" class="group inline-flex items-center gap-2 sm:gap-2.5 px-4 sm:px-6 py-1.5 sm:py-2.5 rounded-full bg-[#f2920b] hover:bg-[#76d3f6] active:bg-[#76d3f6] text-slate-950 font-heading font-extrabold text-xs sm:text-sm tracking-wider uppercase shadow-[0_10px_25px_rgba(0,0,0,0.4)] hover:shadow-[0_14px_30px_rgba(118,211,246,0.5)] hover:scale-105 active:scale-95 transition-all duration-300 overflow-hidden">
                <span data-i18n="slide1_btn">{t['slide1_btn']}</span>
                <div class="w-5 h-5 sm:w-5.5 sm:h-5.5 rounded-full bg-slate-950/10 group-hover:bg-slate-950 group-hover:text-white flex items-center justify-center transition-all duration-300">
                  <i data-lucide="arrow-right" class="w-3 h-3 sm:w-3.5 sm:h-3.5 stroke-[3] group-hover:translate-x-1 transition-transform duration-300"></i>
                </div>
              </a>
            </div>
          </div>
        </div>

        <!-- SLIDE 2: SAVE MY PLAY - GRABACIÓN EN PISTA: HIGHLIGHTS Y PARTIDOS -->
        <div id="coverflow-1" class="coverflow-slide next w-[90%] sm:w-[72%] lg:w-[62%] max-w-[840px] h-[300px] sm:h-[360px] lg:h-[390px] rounded-3xl overflow-hidden bg-neutral-900">
          <img src="{asset_prefix}assets/images/slide-2.jpg" alt="Save my Play camaras inteligentes con IA para pistas de padel" class="w-full h-full object-cover" loading="lazy" decoding="async">
          
          <div class="slide-caption absolute bottom-4 sm:bottom-7 left-4 sm:left-8 z-30 space-y-2 sm:space-y-3 pointer-events-auto pr-4 max-w-[92%] sm:max-w-[85%]">
            <h2 data-i18n="slide2_title" class="text-xl sm:text-3xl lg:text-4xl font-black font-heading text-white uppercase tracking-tight leading-[1.15]">
              {t['slide2_title']}
            </h2>
            <div>
              <a href="#savemyplay" class="group inline-flex items-center gap-2 sm:gap-2.5 px-4 sm:px-6 py-1.5 sm:py-2.5 rounded-full bg-white hover:bg-neutral-100 active:bg-neutral-200 text-neutral-950 font-heading font-extrabold text-xs sm:text-sm tracking-wider uppercase shadow-[0_10px_25px_rgba(0,0,0,0.4)] hover:shadow-[0_14px_30px_rgba(0,0,0,0.6)] hover:scale-105 active:scale-95 transition-all duration-300 overflow-hidden">
                <span data-i18n="slide2_btn">{t['slide2_btn']}</span>
                <img src="{asset_prefix}assets/images/savemyplay-logo-cropped.png" alt="Save my Play" class="h-4.5 sm:h-6 lg:h-7 w-auto object-contain" loading="lazy">
                <div class="w-5 h-5 sm:w-5.5 sm:h-5.5 rounded-full bg-slate-950/10 group-hover:bg-slate-950/20 text-neutral-950 flex items-center justify-center transition-all duration-300">
                  <i data-lucide="arrow-up-right" class="w-3 h-3 sm:w-3.5 sm:h-3.5 stroke-[3] group-hover:translate-x-0.5 group-hover:-translate-y-0.5 transition-transform duration-300"></i>
                </div>
              </a>
            </div>
          </div>
        </div>

        <!-- SLIDE 3: EL NEGOCIO DEL PADEL INFORME (SLIDE-3.JPG) -->
        <div id="coverflow-2" class="coverflow-slide prev w-[90%] sm:w-[72%] lg:w-[62%] max-w-[840px] h-[300px] sm:h-[360px] lg:h-[390px] rounded-3xl overflow-hidden bg-neutral-900">
          <img src="{asset_prefix}assets/images/slide-3.jpg" alt="Informe exclusivo sobre la industria del padel 2026" class="w-full h-full object-cover" loading="lazy" decoding="async">
          
          <div class="slide-caption absolute bottom-4 sm:bottom-7 left-4 sm:left-8 z-30 space-y-2 sm:space-y-3 pointer-events-auto pr-4 max-w-[92%] sm:max-w-[85%]">
            <h2 data-i18n="slide3_title" class="text-xl sm:text-3xl lg:text-4xl font-black font-heading text-white uppercase tracking-tight leading-[1.15]">
              {t['slide3_title']}
            </h2>
            <div>
              <a href="#informe" class="group inline-flex items-center gap-2 sm:gap-2.5 px-4 sm:px-6 py-1.5 sm:py-2.5 rounded-full bg-[#76d3f6] hover:bg-[#f2920b] active:bg-[#f2920b] text-slate-950 font-heading font-extrabold text-xs sm:text-sm tracking-wider uppercase shadow-[0_10px_25px_rgba(0,0,0,0.4)] hover:shadow-[0_14px_30px_rgba(242,146,11,0.5)] hover:scale-105 active:scale-95 transition-all duration-300 overflow-hidden">
                <span data-i18n="slide3_btn">{t['slide3_btn']}</span>
                <div class="w-5 h-5 sm:w-5.5 sm:h-5.5 rounded-full bg-slate-950/10 group-hover:bg-slate-950 group-hover:text-white flex items-center justify-center transition-all duration-300">
                  <i data-lucide="download" class="w-3 h-3 sm:w-3.5 sm:h-3.5 stroke-[3] group-hover:translate-y-0.5 transition-transform duration-300"></i>
                </div>
              </a>
            </div>
          </div>
        </div>

      </div>

      <!-- TEXTO EN ZONA DEBAJO DE LAS FOTOS (SIEMPRE VISIBLE EN EL FOLD) -->
      <div class="mt-3 sm:mt-4 mb-0 text-center px-4">
        <p data-i18n="trusted_text" class="text-[12px] sm:text-[15px] lg:text-[17px] font-heading font-extrabold uppercase tracking-widest text-slate-950 leading-snug">
          {t['trusted_text']}
        </p>
      </div>

    </div>
  </section>

  <!-- 4. CARROUSEL PASARELA CLUBS (ALTURA AJUSTADA PARA ESTAR VISIBLE DE INMEDIATO) -->
  <section class="py-2.5 sm:py-3.5 bg-white border-y border-slate-200 overflow-hidden shadow-xs">
    <div class="ticker-wrap py-0.5">
      <div class="ticker-content animate-ticker-trusted flex items-center gap-5 sm:gap-10 lg:gap-12">
        {"".join([f'<div class="flex items-center justify-center shrink-0 px-2.5 sm:px-5 group"><img src="{asset_prefix}assets/images/Clubs/client-{str(i).zfill(2)}.png" alt="Club Deportivo Partner CoolPadel" class="h-10 sm:h-14 lg:h-16 w-auto max-w-[110px] sm:max-w-[180px] object-contain transition-all duration-300 hover:scale-110" loading="lazy" decoding="async"></div>' for i in (list(range(2, 28)) * 2)])}
      </div>
    </div>
  </section>

  <!-- 5. SECCIÓN DETALLADA: LLAVEROS PARA CLUBS (FONDO CELESTE #3478a6) -->
  <section id="llaveros" class="py-14 sm:py-20 bg-[#3478a6] relative border-b border-sky-700/40 text-white overflow-hidden">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
      
      <!-- CABECERA DE SECCIÓN LLAVEROS -->
      <div class="max-w-3xl mx-auto text-center space-y-2 sm:space-y-3 mb-10 sm:mb-16">
        <h2 data-i18n="llaveros_title" class="text-2xl sm:text-5xl font-black font-heading text-white uppercase tracking-tight leading-tight">
          {t['llaveros_title']}
        </h2>
        <p data-i18n="llaveros_subtitle" class="text-white/90 text-sm sm:text-lg font-medium">
          {t['llaveros_subtitle']}
        </p>
      </div>

      <!-- DOS FOTOS: TENIS (IZQ) & PADEL (DCHA) -->
      <div class="grid md:grid-cols-2 gap-6 sm:gap-8 lg:gap-12 max-w-5xl mx-auto mb-12 sm:mb-16">
        
        <!-- CARD IZQUIERDA: TENIS -->
        <div class="bg-white border border-slate-200/90 rounded-3xl p-5 sm:p-7 shadow-[0_25px_50px_-12px_rgba(0,0,0,0.25)] hover:shadow-[0_35px_65px_-10px_rgba(0,0,0,0.35)] transition-all duration-300 group flex flex-col justify-between hover:-translate-y-1">
          <div class="aspect-[4/3] rounded-2xl overflow-hidden mb-4 sm:mb-5 bg-slate-100 shadow-[0_20px_40px_-10px_rgba(0,0,0,0.3)] border border-slate-200/90">
            <img src="{asset_prefix}assets/images/llaveros 2.jpg" alt="Llaveros de tenis personalizados con logo para clubs y escuelas" class="w-full h-full object-cover group-hover:scale-105 transition duration-500" loading="lazy" decoding="async">
          </div>
          <h3 data-i18n="card_tenis" class="font-heading font-black text-2xl sm:text-3xl uppercase tracking-tight text-slate-950 text-center py-1">
            {t['card_tenis']}
          </h3>
        </div>

        <!-- CARD DERECHA: PADEL -->
        <div class="bg-white border border-slate-200/90 rounded-3xl p-5 sm:p-7 shadow-[0_25px_50px_-12px_rgba(0,0,0,0.25)] hover:shadow-[0_35px_65px_-10px_rgba(0,0,0,0.35)] transition-all duration-300 group flex flex-col justify-between hover:-translate-y-1">
          <div class="aspect-[4/3] rounded-2xl overflow-hidden mb-4 sm:mb-5 bg-slate-100 shadow-[0_20px_40px_-10px_rgba(0,0,0,0.3)] border border-slate-200/90">
            <img src="{asset_prefix}assets/images/llaveros 1.jpg" alt="Llaveros de padel de goma 3D personalizados para clubes" class="w-full h-full object-cover group-hover:scale-105 transition duration-500" loading="lazy" decoding="async">
          </div>
          <h3 data-i18n="card_padel" class="font-heading font-black text-2xl sm:text-3xl uppercase tracking-tight text-[#f2920b] text-center py-1">
            {t['card_padel']}
          </h3>
        </div>

      </div>

      <!-- CALCULADORA DE PRESUPUESTO OFICIAL (RECUADRO BLANCO OFICIAL) -->
      <div class="max-w-3xl mx-auto bg-white rounded-3xl p-5 sm:p-10 border border-white/60 shadow-2xl text-slate-950">
        <div class="text-center space-y-2 sm:space-y-4 mb-6 sm:mb-8">
          <h3 data-i18n="calc_title" class="text-xl sm:text-3xl font-black font-heading text-slate-950">
            {t['calc_title']}
          </h3>
          <div class="flex items-center justify-center gap-2 sm:gap-6 text-xs sm:text-base font-heading font-black uppercase tracking-wider text-slate-900 flex-wrap pt-1">
            <span data-i18n="step_1">{t['step_1']}</span>
            <i data-lucide="arrow-right" class="w-4 h-4 sm:w-6 sm:h-6 stroke-[3] text-[#f2920b]"></i>
            <span data-i18n="step_2">{t['step_2']}</span>
            <i data-lucide="arrow-right" class="w-4 h-4 sm:w-6 sm:h-6 stroke-[3] text-[#f2920b]"></i>
            <span data-i18n="step_3">{t['step_3']}</span>
          </div>
        </div>

        <div class="space-y-6">
          
          <!-- Slider y Contador -->
          <div>
            <div class="flex justify-between items-end mb-3">
              <div>
                <span data-i18n="calc_label_qty" class="text-xs sm:text-sm font-bold text-slate-500 uppercase tracking-wider block">{t['calc_label_qty']}</span>
                <span id="calc-qty-badge" class="text-xl sm:text-3xl font-black font-heading text-slate-950">100 {t['calc_unit_name']}</span>
              </div>
              <div class="text-right">
                <span data-i18n="calc_label_price" class="text-xs sm:text-sm font-bold text-slate-500 uppercase tracking-wider block">{t['calc_label_price']}</span>
                <div class="flex items-baseline justify-end gap-1 sm:gap-1.5">
                  <span id="calc-price-badge" class="text-xl sm:text-3xl font-black font-heading text-[#76d3f6]">300 €</span>
                  <span id="calc-unit-badge" class="text-xs sm:text-sm font-bold text-slate-500">(3,00 €/{t['calc_unit_price']})</span>
                </div>
              </div>
            </div>

            <!-- Slider interactivo con Ojos exactamente centrados en cada punto -->
            <div class="relative py-4 select-none" id="calc-slider-box">
              
              <div class="mx-5 sm:mx-8">
                <!-- Barra / Carril limpio -->
                <div id="slider-track" class="relative w-full h-3 bg-slate-200 rounded-full cursor-pointer touch-none">
                  <!-- Progreso azul oficial #76d3f6 -->
                  <div id="slider-progress" class="absolute top-0 left-0 h-full bg-[#76d3f6] rounded-full transition-all duration-300" style="width: 0%;"></div>

                  <!-- Logo de los Ojos centrado exactamente sobre la barra -->
                  <div id="slider-thumb" 
                       class="absolute top-1/2 -translate-x-1/2 -translate-y-1/2 w-10 sm:w-11 h-5 sm:h-6 flex items-center justify-center cursor-grab active:cursor-grabbing hover:scale-115 active:scale-125 transition-all duration-300 z-30 pointer-events-none"
                       style="left: 0%;">
                    <img src="{asset_prefix}assets/images/eyes-thumb.png" alt="Ojos CoolPadel" class="w-full h-full object-contain drop-shadow-[0_3px_5px_rgba(0,0,0,0.35)] select-none">
                  </div>
                </div>
                
                <!-- Marcas de escala rápida (sin salirse de los límites) -->
                <div class="relative w-full text-[11px] sm:text-sm font-extrabold text-slate-600 h-6 mt-4">
                  <button type="button" onclick="setTier(0)" class="tier-btn absolute left-0 translate-x-0 hover:text-[#f2920b] transition">100 uds</button>
                  <button type="button" onclick="setTier(1)" class="tier-btn absolute left-[33.333%] -translate-x-1/2 hover:text-[#f2920b] transition">250 uds</button>
                  <button type="button" onclick="setTier(2)" class="tier-btn absolute left-[66.666%] -translate-x-1/2 hover:text-[#f2920b] transition">500 uds</button>
                  <button type="button" onclick="setTier(3)" class="tier-btn absolute right-0 translate-x-0 hover:text-[#f2920b] transition">1.500 uds</button>
                </div>
              </div>

            </div>
          </div>

          <!-- 3 Condiciones Oficiales del Tarifario (15% más grandes) -->
          <div class="grid grid-cols-1 sm:grid-cols-3 gap-3 sm:gap-4 text-center pt-2">
            <div class="bg-white p-4 sm:p-5 rounded-2xl border border-slate-200/90 shadow-sm">
              <span data-i18n="badge_muestra" class="text-sm sm:text-base font-bold text-slate-500 uppercase tracking-wider block">{t['badge_muestra']}</span>
              <strong class="text-slate-950 text-lg sm:text-xl font-black block mt-0.5">15€</strong>
            </div>
            <div class="bg-white p-4 sm:p-5 rounded-2xl border border-slate-200/90 shadow-sm">
              <span data-i18n="badge_envios" class="text-sm sm:text-base font-bold text-slate-500 uppercase tracking-wider block">{t['badge_envios']}</span>
              <strong data-i18n="badge_envios_val" class="text-slate-950 text-lg sm:text-xl font-black block mt-0.5">{t['badge_envios_val']}</strong>
            </div>
            <div class="bg-white p-4 sm:p-5 rounded-2xl border border-slate-200/90 shadow-sm">
              <span data-i18n="badge_pago" class="text-sm sm:text-base font-bold text-slate-500 uppercase tracking-wider block">{t['badge_pago']}</span>
              <strong data-i18n="badge_pago_val" class="text-slate-950 text-lg sm:text-xl font-black block mt-0.5">{t['badge_pago_val']}</strong>
            </div>
          </div>

          <!-- Botón de WhatsApp Contactar Premium -->
          <div class="pt-2">
            <a id="calc-wa-btn" href="https://wa.me/34680317486?text={t['wa_prefilled_msg']}" target="_blank" class="group relative w-full py-4 sm:py-4.5 rounded-2xl font-heading font-black text-base sm:text-lg uppercase tracking-wider bg-[#f2920b] hover:bg-[#76d3f6] active:bg-[#76d3f6] text-slate-950 shadow-[0_10px_25px_rgba(242,146,11,0.35)] hover:shadow-[0_16px_35px_rgba(118,211,246,0.45)] hover:scale-[1.01] active:scale-[0.98] flex items-center justify-center gap-3 transition-all duration-300 overflow-hidden">
              <span data-i18n="btn_calc_wa" class="font-black">{t['btn_calc_wa']}</span>
              <div class="w-7 h-7 sm:w-8 sm:h-8 rounded-full bg-slate-950/10 group-hover:bg-slate-950 group-hover:text-white flex items-center justify-center transition-all duration-300">
                <i data-lucide="arrow-up-right" class="w-3.5 h-3.5 sm:w-4 sm:h-4 stroke-[3] group-hover:translate-x-0.5 group-hover:-translate-y-0.5 transition-transform duration-300"></i>
              </div>
            </a>
          </div>
        </div>
      </div>

    </div>
  </section>

  <!-- 6. SECCIÓN DETALLADA: SAVE MY PLAY (FONDO VERDE OFICIAL #4bbb81) -->
  <section id="savemyplay" class="py-16 sm:py-24 bg-[#4bbb81] relative border-b border-emerald-600/30 overflow-hidden">
    <div class="absolute inset-0 bg-gradient-to-b from-black/5 via-transparent to-black/10 pointer-events-none"></div>

    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
      
      <!-- CABECERA DE SECCIÓN -->
      <div class="max-w-3xl mx-auto text-center space-y-2 sm:space-y-3 mb-10 sm:mb-16">
        <h2 data-i18n="smp_title" class="text-2xl sm:text-5xl font-black font-heading text-slate-950 uppercase tracking-tight leading-tight">
          {t['smp_title']}
        </h2>
      </div>

      <!-- 3 FOTOS EN FILA CON BORDE NEGRO Y SOMBRA GIGANTE 3D -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-6 sm:gap-8 lg:gap-10 max-w-6xl sm:max-w-7xl mx-auto mb-12 sm:mb-16">
        
        <!-- FOTO 1 -->
        <div class="rounded-3xl overflow-hidden shadow-[0_20px_45px_-10px_rgba(0,0,0,0.65)] hover:shadow-[0_30px_60px_-10px_rgba(0,0,0,0.85)] transition-all duration-500 group border-2 border-slate-900 bg-slate-800 hover:-translate-y-1">
          <div class="relative aspect-[16/10] overflow-hidden">
            <img src="{asset_prefix}assets/images/savemyplay-1.jpg" alt="Camara Save my Play grabando partido en pista de padel" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700" loading="lazy" decoding="async">
            <div class="absolute inset-0 bg-gradient-to-t from-slate-950/40 via-transparent to-transparent"></div>
          </div>
        </div>

        <!-- FOTO 2 -->
        <div class="rounded-3xl overflow-hidden shadow-[0_20px_45px_-10px_rgba(0,0,0,0.65)] hover:shadow-[0_30px_60px_-10px_rgba(0,0,0,0.85)] transition-all duration-500 group border-2 border-slate-900 bg-slate-800 hover:-translate-y-1">
          <div class="relative aspect-[16/10] overflow-hidden">
            <img src="{asset_prefix}assets/images/savemyplay-2.jpg" alt="Jugadores de padel usando la app Save my Play para ver repeticiones" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700" loading="lazy" decoding="async">
            <div class="absolute inset-0 bg-gradient-to-t from-slate-950/40 via-transparent to-transparent"></div>
          </div>
        </div>

        <!-- FOTO 3 -->
        <div class="rounded-3xl overflow-hidden shadow-[0_20px_45px_-10px_rgba(0,0,0,0.65)] hover:shadow-[0_30px_60px_-10px_rgba(0,0,0,0.85)] transition-all duration-500 group border-2 border-slate-900 bg-slate-800 hover:-translate-y-1">
          <div class="relative aspect-[16/10] overflow-hidden">
            <img src="{asset_prefix}assets/images/savemyplay-3.jpg" alt="Pista panoramica con sistema de video inteligente Save my Play" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700" loading="lazy" decoding="async">
            <div class="absolute inset-0 bg-gradient-to-t from-slate-950/40 via-transparent to-transparent"></div>
          </div>
        </div>

      </div>

      <!-- 2 TARJETAS SAVE MY PLAY: TARJETA PLANES + TARJETA ¿POR QUÉ AÑADIR SMP A TU CLUB? -->
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 lg:gap-12 xl:gap-16 max-w-6xl sm:max-w-7xl mx-auto">
        
        <!-- TARJETA 1: PLANES SAVE MY PLAY -->
        <div class="bg-white rounded-3xl p-5 sm:p-7 border border-emerald-300 shadow-2xl text-slate-900 flex flex-col justify-between hover:-translate-y-1 transition duration-300">
          <div class="space-y-4">
            <div class="flex items-center justify-between border-b border-slate-200 pb-3 sm:pb-4">
              <h3 data-i18n="smp_plans_title" class="font-heading font-black text-lg sm:text-2xl text-slate-950 uppercase tracking-tight">
                {t['smp_plans_title']}
              </h3>
              <span class="w-8 h-8 rounded-full bg-[#4bbb81]/20 flex items-center justify-center text-slate-950">
                <i data-lucide="layers" class="w-4 h-4 stroke-[2.5]"></i>
              </span>
            </div>

            <!-- PLANES GRID -->
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 sm:gap-4">
              
              <!-- PLAN A: NARANJA 136€/mes -->
              <div class="p-4 sm:p-5 rounded-2xl bg-orange-50/70 border-2 border-[#f2920b] flex flex-col space-y-2.5">
                <div class="flex items-center justify-between">
                  <span data-i18n="smp_plan_a_title" class="font-black text-xs uppercase tracking-wider px-2.5 py-0.5 rounded-full bg-[#f2920b] text-slate-950">
                    {t['smp_plan_a_title']}
                  </span>
                  <i data-lucide="sparkles" class="w-4 h-4 text-[#f2920b]"></i>
                </div>
                <strong data-i18n="smp_plan_a_price" class="text-2xl sm:text-3xl font-black font-heading text-slate-950 block">
                  {t['smp_plan_a_price']}
                </strong>
                <p data-i18n="smp_plan_a_desc" class="text-xs text-slate-700 font-medium leading-relaxed">
                  {t['smp_plan_a_desc']}
                </p>
              </div>

              <!-- PLAN B: AZUL 45€/mes -->
              <div class="p-4 sm:p-5 rounded-2xl bg-sky-50/70 border-2 border-[#76d3f6] flex flex-col space-y-2.5">
                <div class="flex items-center justify-between">
                  <span data-i18n="smp_plan_b_title" class="font-black text-xs uppercase tracking-wider px-2.5 py-0.5 rounded-full bg-[#76d3f6] text-slate-950">
                    {t['smp_plan_b_title']}
                  </span>
                  <i data-lucide="video" class="w-4 h-4 text-sky-600"></i>
                </div>
                <strong data-i18n="smp_plan_b_price" class="text-2xl sm:text-3xl font-black font-heading text-slate-950 block">
                  {t['smp_plan_b_price']}
                </strong>
                <p data-i18n="smp_plan_b_desc" class="text-xs text-slate-700 font-medium leading-relaxed">
                  {t['smp_plan_b_desc']}
                </p>
              </div>

            </div>

            <!-- INVERSIÓN INICIAL CÁMARAS: 180 € / PISTA CENTRADO ABAJO -->
            <div class="py-2.5 px-4 max-w-xs sm:max-w-sm mx-auto rounded-xl bg-slate-100 border border-slate-200 text-center">
              <span data-i18n="smp_cam_invest" class="font-black text-xs sm:text-sm text-slate-950 block">
                {t['smp_cam_invest']}
              </span>
            </div>
          </div>

          <!-- BOTÓN CONTACTAR PLANES -->
          <div class="pt-4 border-t border-slate-200 mt-4">
            <a id="smp-plan-btn" href="https://wa.me/34680317486?text={t['wa_prefilled_msg']}" 
               target="_blank" 
               class="group relative w-full inline-flex items-center justify-center gap-2.5 px-6 py-3.5 rounded-full bg-[#f2920b] hover:bg-[#76d3f6] active:bg-[#76d3f6] text-slate-950 active:scale-95 font-heading font-black text-xs sm:text-sm uppercase tracking-wider transition-all duration-300 shadow-[0_4px_15px_rgba(242,146,11,0.25)] hover:shadow-[0_8px_25px_rgba(118,211,246,0.35)] hover:scale-[1.01] overflow-hidden">
              <span data-i18n="smp_btn" class="font-black">{t['smp_btn']}</span>
              <div class="w-6 h-6 rounded-full bg-slate-950/10 group-hover:bg-slate-950 group-hover:text-white flex items-center justify-center transition-all duration-300">
                <i data-lucide="arrow-up-right" class="w-3.5 h-3.5 stroke-[3] group-hover:translate-x-0.5 group-hover:-translate-y-0.5 transition-transform duration-300"></i>
              </div>
            </a>
          </div>
        </div>

        <!-- TARJETA 2: ¿POR QUÉ AÑADIR SAVE MY PLAY A TU CLUB? -->
        <div class="bg-white rounded-3xl p-5 sm:p-7 border border-emerald-300 shadow-2xl text-slate-900 flex flex-col justify-between hover:-translate-y-1 transition duration-300">
          <div class="space-y-4">
            <div class="flex items-center gap-1.5 sm:gap-2 flex-wrap border-b border-slate-200 pb-3 sm:pb-4">
              <span data-i18n="smp_why_title_prefix" class="font-heading font-black text-lg sm:text-2xl text-slate-950 uppercase tracking-tight">{t['smp_why_title_prefix']}</span>
              <img src="{asset_prefix}assets/images/savemyplay-logo-clean.png" alt="Save my Play" class="h-6 sm:h-8 w-auto object-contain" loading="lazy">
              <span data-i18n="smp_why_title_suffix" class="font-heading font-black text-lg sm:text-2xl text-slate-950 uppercase tracking-tight">{t['smp_why_title_suffix']}</span>
            </div>

            <!-- 4 RAZONES COMERCIALES -->
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 sm:gap-4">
              <div class="flex items-start gap-2.5 sm:gap-3 p-1">
                <div class="w-7 h-7 sm:w-8 sm:h-8 rounded-xl bg-[#4bbb81]/20 flex items-center justify-center shrink-0 mt-0.5 text-slate-950">
                  <i data-lucide="sparkles" class="w-3.5 h-3.5 sm:w-4 sm:h-4 stroke-[2.5]"></i>
                </div>
                <div>
                  <h5 data-i18n="feat1_title" class="text-xs sm:text-sm font-bold text-slate-950 uppercase leading-tight">{t['feat1_title']}</h5>
                  <p data-i18n="feat1_desc" class="text-[11px] sm:text-xs text-slate-600 font-medium leading-relaxed mt-0.5">{t['feat1_desc']}</p>
                </div>
              </div>

              <div class="flex items-start gap-2.5 sm:gap-3 p-1">
                <div class="w-7 h-7 sm:w-8 sm:h-8 rounded-xl bg-[#4bbb81]/20 flex items-center justify-center shrink-0 mt-0.5 text-slate-950">
                  <i data-lucide="share-2" class="w-3.5 h-3.5 sm:w-4 sm:h-4 stroke-[2.5]"></i>
                </div>
                <div>
                  <h5 data-i18n="feat2_title" class="text-xs sm:text-sm font-bold text-slate-950 uppercase leading-tight">{t['feat2_title']}</h5>
                  <p data-i18n="feat2_desc" class="text-[11px] sm:text-xs text-slate-600 font-medium leading-relaxed mt-0.5">{t['feat2_desc']}</p>
                </div>
              </div>

              <div class="flex items-start gap-2.5 sm:gap-3 p-1">
                <div class="w-7 h-7 sm:w-8 sm:h-8 rounded-xl bg-[#4bbb81]/20 flex items-center justify-center shrink-0 mt-0.5 text-slate-950">
                  <i data-lucide="shield-check" class="w-3.5 h-3.5 sm:w-4 sm:h-4 stroke-[2.5]"></i>
                </div>
                <div>
                  <h5 data-i18n="feat3_title" class="text-xs sm:text-sm font-bold text-slate-950 uppercase leading-tight">{t['feat3_title']}</h5>
                  <p data-i18n="feat3_desc" class="text-[11px] sm:text-xs text-slate-600 font-medium leading-relaxed mt-0.5">{t['feat3_desc']}</p>
                </div>
              </div>

              <div class="flex items-start gap-2.5 sm:gap-3 p-1">
                <div class="w-7 h-7 sm:w-8 sm:h-8 rounded-xl bg-[#4bbb81]/20 flex items-center justify-center shrink-0 mt-0.5 text-slate-950">
                  <i data-lucide="trending-up" class="w-3.5 h-3.5 sm:w-4 sm:h-4 stroke-[2.5]"></i>
                </div>
                <div>
                  <h5 data-i18n="feat4_title" class="text-xs sm:text-sm font-bold text-slate-950 uppercase leading-tight">{t['feat4_title']}</h5>
                  <p data-i18n="feat4_desc" class="text-[11px] sm:text-xs text-slate-600 font-medium leading-relaxed mt-0.5">{t['feat4_desc']}</p>
                </div>
              </div>
            </div>
          </div>

          <!-- BOTÓN CONTACTAR POR QUÉ SMP -->
          <div class="pt-4 border-t border-slate-200 mt-4">
            <a id="smp-contact-btn" href="https://wa.me/34680317486?text={t['wa_prefilled_msg']}" 
               target="_blank" 
               class="group relative w-full inline-flex items-center justify-center gap-2.5 px-6 py-3.5 rounded-full bg-[#f2920b] hover:bg-[#76d3f6] active:bg-[#76d3f6] text-slate-950 active:scale-95 font-heading font-black text-xs sm:text-sm uppercase tracking-wider transition-all duration-300 shadow-[0_4px_15px_rgba(242,146,11,0.25)] hover:shadow-[0_8px_25px_rgba(118,211,246,0.35)] hover:scale-[1.01] overflow-hidden">
              <span data-i18n="smp_btn" class="font-black">{t['smp_btn']}</span>
              <div class="w-6 h-6 rounded-full bg-slate-950/10 group-hover:bg-slate-950 group-hover:text-white flex items-center justify-center transition-all duration-300">
                <i data-lucide="arrow-up-right" class="w-3.5 h-3.5 stroke-[3] group-hover:translate-x-0.5 group-hover:-translate-y-0.5 transition-transform duration-300"></i>
              </div>
            </a>
          </div>
        </div>

      </div>

    </div>
  </section>

  <!-- 7. SECCIÓN DETALLADA: REPORTAJE INDUSTRIA PADEL 2026 & NEWSLETTER COOLPADEL -->
  <section id="informe" class="py-16 sm:py-24 bg-white relative border-b border-slate-200">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <!-- CABECERA DE SECCIÓN -->
      <div class="max-w-3xl mx-auto text-center space-y-2 sm:space-y-3 mb-10 sm:mb-16">
        <h2 data-i18n="report_section_title" class="text-2xl sm:text-4xl font-black font-heading text-slate-950 uppercase tracking-tight">
          {t['report_section_title']}
        </h2>
        <p data-i18n="report_section_subtitle" class="text-slate-600 text-sm sm:text-lg font-medium">
          {t['report_section_subtitle']}
        </p>
      </div>

      <div class="grid md:grid-cols-2 gap-6 sm:gap-8 lg:gap-12 max-w-6xl mx-auto">
        
        <!-- CARD 1: REPORTAJE INDUSTRIA PADEL 2026 -->
        <div class="bg-white border border-slate-200/90 rounded-3xl p-5 sm:p-6 shadow-[0_25px_50px_-12px_rgba(0,0,0,0.18)] hover:shadow-[0_35px_65px_-10px_rgba(0,0,0,0.28)] transition-all duration-300 flex flex-col justify-between group hover:-translate-y-1">
          <div class="space-y-3 sm:space-y-4">
            <div class="aspect-[16/10] rounded-2xl overflow-hidden bg-slate-900 border border-slate-200/90 shadow-[0_20px_40px_-10px_rgba(0,0,0,0.4)] group-hover:scale-[1.01] transition duration-500 relative">
              <img src="{asset_prefix}assets/images/foto-reportaje.jpg" alt="Informe PDF sobre tendencias de la industria del padel 2026" class="w-full h-full object-cover group-hover:scale-105 transition duration-700" loading="lazy" decoding="async">
              <div class="absolute inset-0 bg-gradient-to-t from-black/50 via-transparent to-transparent"></div>
              <span data-i18n="report_card1_tag" class="absolute bottom-3 left-3 text-[11px] font-black uppercase tracking-wider px-3 py-1 rounded-full bg-white text-slate-950 shadow-md">
                {t['report_card1_tag']}
              </span>
            </div>

            <div class="space-y-1.5 pt-0.5">
              <h3 data-i18n="report_card1_title" class="font-heading font-bold text-xl sm:text-2xl text-slate-950">
                {t['report_card1_title']}
              </h3>
              <p data-i18n="report_card1_desc" class="text-xs sm:text-sm text-slate-600 font-medium leading-relaxed">
                {t['report_card1_desc']}
              </p>
            </div>
          </div>

          <!-- FORMULARIO RECOLECCIÓN DE EMAIL + BOTÓN DESCARGAR -->
          <div class="pt-3 sm:pt-4 border-t border-slate-200 mt-3 sm:mt-4">
            <form onsubmit="handleReportDownload(event)" class="space-y-2.5">
              <div class="relative">
                <input type="email" id="report-email-input" required placeholder="{t['report_card1_placeholder']}" data-i18n-placeholder="report_card1_placeholder" class="w-full px-4 sm:px-5 py-2.5 sm:py-3 rounded-full bg-white border border-slate-300 text-slate-950 text-base font-medium focus:outline-none focus:border-[#f2920b] shadow-inner transition">
              </div>
              <button type="submit" class="group relative w-full inline-flex items-center justify-center gap-2.5 px-6 py-3 rounded-full bg-[#f2920b] hover:bg-[#76d3f6] active:bg-[#76d3f6] text-slate-950 active:scale-95 font-heading font-black text-xs sm:text-sm uppercase tracking-wider transition-all duration-300 shadow-[0_4px_15px_rgba(242,146,11,0.25)] hover:shadow-[0_8px_25px_rgba(118,211,246,0.35)] hover:scale-[1.01] overflow-hidden cursor-pointer">
                <span data-i18n="report_card1_btn">{t['report_card1_btn']}</span>
                <div class="w-6 h-6 rounded-full bg-slate-950/10 group-hover:bg-slate-950 group-hover:text-white flex items-center justify-center transition-all duration-300">
                  <i data-lucide="download" class="w-3.5 h-3.5 stroke-[3] group-hover:translate-y-0.5 transition-transform duration-300"></i>
                </div>
              </button>
            </form>
          </div>
        </div>

        <!-- CARD 2: NEWSLETTER COOLPADEL -->
        <div class="bg-white border border-slate-200/90 rounded-3xl p-5 sm:p-6 shadow-[0_25px_50px_-12px_rgba(0,0,0,0.18)] hover:shadow-[0_35px_65px_-10px_rgba(0,0,0,0.28)] transition-all duration-300 flex flex-col justify-between group hover:-translate-y-1">
          <div class="space-y-3 sm:space-y-4">
            <div class="aspect-[16/10] rounded-2xl overflow-hidden bg-slate-900 border border-slate-200/90 shadow-[0_20px_40px_-10px_rgba(0,0,0,0.4)] group-hover:scale-[1.01] transition duration-500 relative">
              <img src="{asset_prefix}assets/images/coolpadels-newsletter.jpg" alt="Newsletter CoolPadel en LinkedIn Pulse sobre el sector de raqueta" class="w-full h-full object-cover group-hover:scale-105 transition duration-700" loading="lazy" decoding="async">
              <div class="absolute inset-0 bg-gradient-to-t from-black/50 via-transparent to-transparent"></div>
              <span data-i18n="report_card2_tag" class="absolute bottom-3 left-3 text-[11px] font-black uppercase tracking-wider px-3 py-1 rounded-full bg-white text-slate-950 shadow-md">
                {t['report_card2_tag']}
              </span>
            </div>

            <div class="space-y-1.5 pt-0.5">
              <h3 data-i18n="report_card2_title" class="font-heading font-bold text-xl sm:text-2xl text-slate-950">
                {t['report_card2_title']}
              </h3>
              <p data-i18n="report_card2_desc" class="text-xs sm:text-sm text-slate-600 font-medium leading-relaxed">
                {t['report_card2_desc']}
              </p>
            </div>
          </div>

          <!-- BOTÓN LINK A LINKEDIN -->
          <div class="pt-3 sm:pt-4 border-t border-slate-200 mt-3 sm:mt-4">
            <a href="https://www.linkedin.com/pulse/padel-world-summit-2026-startup-recap-javier-villoria-soleto-c7hle/" 
               target="_blank" 
               class="group relative w-full inline-flex items-center justify-center gap-2.5 px-6 py-3 rounded-full bg-[#f2920b] hover:bg-[#76d3f6] active:bg-[#76d3f6] text-slate-950 active:scale-95 font-heading font-black text-xs sm:text-sm uppercase tracking-wider transition-all duration-300 shadow-[0_4px_15px_rgba(242,146,11,0.25)] hover:shadow-[0_8px_25px_rgba(118,211,246,0.35)] hover:scale-[1.01] overflow-hidden">
              <span data-i18n="report_card2_btn">{t['report_card2_btn']}</span>
              <div class="w-6 h-6 rounded-full bg-slate-950/10 group-hover:bg-slate-950 group-hover:text-white flex items-center justify-center transition-all duration-300">
                <i data-lucide="arrow-up-right" class="w-3.5 h-3.5 stroke-[3] group-hover:translate-x-0.5 group-hover:-translate-y-0.5 transition-transform duration-300"></i>
              </div>
            </a>
          </div>
        </div>

      </div>

    </div>
  </section>

  <!-- 7.5. SECCIÓN PREGUNTAS FRECUENTES (FAQ ACORDEÓN INTERACTIVO + GEO/SEO) -->
  <section id="faq" class="py-16 sm:py-24 bg-slate-50 relative border-b border-slate-200">
    <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <!-- CABECERA FAQ -->
      <div class="text-center mb-10 sm:mb-14">
        <h2 data-i18n="faq_section_title" class="text-2xl sm:text-4xl font-black font-heading text-slate-950 uppercase tracking-tight">
          {t['faq_section_title']}
        </h2>
      </div>

      <!-- ACORDEÓN DE PREGUNTAS (3 PREGUNTAS OFICIALES) -->
      <div class="space-y-3 sm:space-y-4" id="faq-accordion">
        
        <!-- PREGUNTA 1 -->
        <div class="faq-item bg-white border border-slate-200/90 rounded-2xl overflow-hidden shadow-xs transition-all duration-200">
          <button type="button" onclick="toggleFaq(this)" class="w-full px-5 sm:px-6 py-4 sm:py-5 flex items-center justify-between text-left font-sans font-bold text-base sm:text-lg text-slate-900 hover:text-[#f2920b] transition gap-4 cursor-pointer">
            <span data-i18n="faq_q1">{t['faq_q1']}</span>
            <i data-lucide="chevron-down" class="faq-icon w-5 h-5 stroke-[2.5] text-slate-400 shrink-0 transition-transform duration-300"></i>
          </button>
          <div class="faq-answer hidden px-5 sm:px-6 pb-5 pt-3 text-slate-700 text-sm sm:text-base font-normal leading-relaxed sm:leading-loose border-t border-slate-100">
            <p data-i18n="faq_a1">{t['faq_a1']}</p>
          </div>
        </div>

        <!-- PREGUNTA 2 -->
        <div class="faq-item bg-white border border-slate-200/90 rounded-2xl overflow-hidden shadow-xs transition-all duration-200">
          <button type="button" onclick="toggleFaq(this)" class="w-full px-5 sm:px-6 py-4 sm:py-5 flex items-center justify-between text-left font-sans font-bold text-base sm:text-lg text-slate-900 hover:text-[#f2920b] transition gap-4 cursor-pointer">
            <span data-i18n="faq_q2">{t['faq_q2']}</span>
            <i data-lucide="chevron-down" class="faq-icon w-5 h-5 stroke-[2.5] text-slate-400 shrink-0 transition-transform duration-300"></i>
          </button>
          <div class="faq-answer hidden px-5 sm:px-6 pb-5 pt-3 text-slate-700 text-sm sm:text-base font-normal leading-relaxed sm:leading-loose border-t border-slate-100">
            <p data-i18n="faq_a2">{t['faq_a2']}</p>
          </div>
        </div>

        <!-- PREGUNTA 3 -->
        <div class="faq-item bg-white border border-slate-200/90 rounded-2xl overflow-hidden shadow-xs transition-all duration-200">
          <button type="button" onclick="toggleFaq(this)" class="w-full px-5 sm:px-6 py-4 sm:py-5 flex items-center justify-between text-left font-sans font-bold text-base sm:text-lg text-slate-900 hover:text-[#f2920b] transition gap-4 cursor-pointer">
            <span data-i18n="faq_q3">{t['faq_q3']}</span>
            <i data-lucide="chevron-down" class="faq-icon w-5 h-5 stroke-[2.5] text-slate-400 shrink-0 transition-transform duration-300"></i>
          </button>
          <div class="faq-answer hidden px-5 sm:px-6 pb-5 pt-3 text-slate-700 text-sm sm:text-base font-normal leading-relaxed sm:leading-loose border-t border-slate-100">
            <p data-i18n="faq_a3">{t['faq_a3']}</p>
          </div>
        </div>

      </div>

    </div>
  </section>

  <!-- 8. SECCIÓN CONTACTO (FONDO CELESTE #3478a6 & SIMETRÍA RESPONSIVE) -->
  <section id="contacto" class="py-14 sm:py-20 bg-[#3478a6] relative border-t border-sky-700/40 text-white overflow-hidden">
    <div class="max-w-[1550px] mx-auto px-4 sm:px-8 lg:px-12 relative z-10">
      
      <!-- TÍTULO DE LA SECCIÓN -->
      <div class="max-w-3xl mx-auto text-center mb-10 sm:mb-14">
        <h2 data-i18n="contact_title" class="text-2xl sm:text-5xl font-black font-heading text-white uppercase tracking-tight leading-tight">
          {t['contact_title']}
        </h2>
      </div>

      <!-- 3 BLOQUES MATEMÁTICAMENTE SIMÉTRICOS RESPECTO AL CORREO -->
      <div class="grid grid-cols-1 md:grid-cols-[1fr_auto_1fr] items-center gap-8 md:gap-0 w-full">
        
        <!-- IZQUIERDA: COOLPADEL ALINEADO HACIA EL CORREO -->
        <div class="flex items-center justify-center md:justify-end gap-3 sm:gap-4 md:pr-16 lg:pr-24 xl:pr-28">
          <img src="{asset_prefix}assets/images/coolpadel-mascot-hd.png" alt="CoolPadel Mascota" class="h-12 sm:h-18 lg:h-20 w-auto object-contain drop-shadow-md" loading="lazy">
          <img src="{asset_prefix}assets/images/coolpadel-typography-hd.png" alt="CoolPadel" class="h-6 sm:h-9 lg:h-10 w-auto object-contain drop-shadow-md" loading="lazy">
        </div>

        <!-- CENTRO: CORREO Y WHATSAPP OFICIAL DE JAVIER -->
        <div class="flex flex-col items-center justify-center text-center gap-4 sm:gap-6 px-2 sm:px-4">
          <a href="mailto:javier@coolpadelstudios.com" 
             class="group inline-flex items-center gap-2.5 text-white hover:text-[#f2920b] font-sans font-bold text-sm sm:text-xl lg:text-2xl tracking-normal transition-all duration-300 hover:scale-105 active:scale-95 break-all sm:break-normal -mt-1 sm:-mt-2">
            <i data-lucide="mail" class="w-4 h-4 sm:w-6 sm:h-6 text-[#f2920b] group-hover:text-white transition-colors shrink-0"></i>
            <span class="underline decoration-white/40 group-hover:decoration-[#f2920b] underline-offset-6">javier@coolpadelstudios.com</span>
          </a>

          <!-- BOTÓN WHATSAPP OFICIAL EN CONTACTO -->
          <a id="contact-wa-btn" href="https://wa.me/34680317486?text={t['wa_prefilled_msg']}" 
             target="_blank" 
             class="group inline-flex items-center gap-2.5 px-5 sm:px-6 py-2.5 rounded-full bg-[#25D366] hover:bg-[#20ba59] active:bg-[#20ba59] text-white font-sans font-black text-xs sm:text-sm tracking-wider uppercase shadow-md hover:shadow-xl hover:scale-105 active:scale-95 transition-all duration-300 mt-1 sm:mt-2">
            <svg class="w-4 h-4 sm:w-5 sm:h-5 fill-current" viewBox="0 0 24 24">
              <path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981zm11.387-5.464c-.074-.124-.272-.198-.57-.347-.297-.149-1.758-.868-2.031-.967-.272-.099-.47-.149-.669.149-.198.297-.768.967-.941 1.165-.173.198-.347.223-.644.074-.297-.149-1.255-.462-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.297-.347.446-.521.151-.172.2-.296.3-.495.099-.198.05-.372-.025-.521-.075-.148-.669-1.611-.916-2.206-.242-.579-.487-.501-.669-.51l-.57-.01c-.198 0-.52.074-.792.372s-1.04 1.016-1.04 2.479 1.065 2.876 1.213 3.074c.149.198 2.095 3.2 5.076 4.487.709.306 1.263.489 1.694.626.712.226 1.36.194 1.872.118.571-.085 1.758-.719 2.006-1.413.248-.695.248-1.29.173-1.414z"/>
            </svg>
            <span data-i18n="contact_wa_btn">{t['contact_wa_btn']}</span>
          </a>
        </div>

        <!-- DERECHA: SAVE MY PLAY ALINEADO HACIA EL CORREO -->
        <div class="flex items-center justify-center md:justify-start md:pl-16 lg:pl-24 xl:pl-28">
          <img src="{asset_prefix}assets/images/savemyplay-logo-white-text-hd.png" alt="Save my Play" class="h-10 sm:h-14 lg:h-16 w-auto object-contain drop-shadow-md" loading="lazy">
        </div>

      </div>

    </div>
  </section>

  <!-- BOTÓN FLOTANTE OFICIAL DE WHATSAPP -->
  <a id="floating-wa-btn" href="https://wa.me/34680317486?text={t['wa_prefilled_msg']}" 
     target="_blank" 
     class="fixed bottom-5 right-5 sm:bottom-6 sm:right-6 z-50 p-3.5 sm:p-4 rounded-full bg-[#25D366] text-white shadow-[0_10px_30px_rgba(37,211,102,0.45)] hover:bg-[#20ba59] hover:scale-110 active:scale-95 transition flex items-center justify-center group"
     title="Hablar por WhatsApp con Javier">
    <svg class="w-6 h-6 sm:w-8 sm:h-8 fill-current" viewBox="0 0 24 24">
      <path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981zm11.387-5.464c-.074-.124-.272-.198-.57-.347-.297-.149-1.758-.868-2.031-.967-.272-.099-.47-.149-.669.149-.198.297-.768.967-.941 1.165-.173.198-.347.223-.644.074-.297-.149-1.255-.462-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.297-.347.446-.521.151-.172.2-.296.3-.495.099-.198.05-.372-.025-.521-.075-.148-.669-1.611-.916-2.206-.242-.579-.487-.501-.669-.51l-.57-.01c-.198 0-.52.074-.792.372s-1.04 1.016-1.04 2.479 1.065 2.876 1.213 3.074c.149.198 2.095 3.2 5.076 4.487.709.306 1.263.489 1.694.626.712.226 1.36.194 1.872.118.571-.085 1.758-.719 2.006-1.413.248-.695.248-1.29.173-1.414z"/>
    </svg>
    <span data-i18n="wa_floating_tooltip" class="max-w-0 overflow-hidden whitespace-nowrap group-hover:max-w-xs transition-all duration-300 ease-in-out text-xs font-black px-0 group-hover:px-2">
      {t['wa_floating_tooltip']}
    </span>
  </a>

  <!-- 9. MODAL POP-UP LEAD MAGNET (INFORME EXCLUSIVO INDUSTRIA PADEL) -->
  <div id="lead-modal" class="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/75 backdrop-blur-md opacity-0 pointer-events-none transition-opacity duration-300">
    <div id="lead-modal-content" class="relative w-full max-w-lg max-h-[90vh] overflow-y-auto bg-[#3478a6] border border-white/20 rounded-3xl p-6 sm:p-8 text-white shadow-[0_25px_60px_-15px_rgba(0,0,0,0.6)] transform scale-95 transition-transform duration-300">
      
      <!-- BOTÓN CERRAR (X) -->
      <button type="button" onclick="closeLeadModal()" class="absolute top-4 right-4 w-8 h-8 rounded-full bg-white/15 hover:bg-white/25 text-white flex items-center justify-center transition cursor-pointer" aria-label="Cerrar modal">
        <i data-lucide="x" class="w-4 h-4"></i>
      </button>

      <!-- CABECERA POPUP -->
      <div class="space-y-2.5 text-center sm:text-left pr-6">
        <h3 data-i18n="popup_title" class="font-heading font-black text-xl sm:text-2xl uppercase tracking-tight text-white leading-tight">
          {t['popup_title']}
        </h3>
        
        <p data-i18n="popup_desc" class="text-xs sm:text-sm text-white/90 font-medium leading-relaxed">
          {t['popup_desc']}
        </p>
      </div>

      <!-- FORMULARIO RECOLECCIÓN EMAIL POPUP -->
      <form onsubmit="handlePopupDownload(event)" class="mt-6 space-y-3.5">
        <div class="relative">
          <input type="email" id="popup-email-input" required placeholder="{t['popup_placeholder']}" data-i18n-placeholder="popup_placeholder" class="w-full px-5 py-3.5 rounded-full bg-white border border-slate-200 text-slate-950 text-base font-medium placeholder:text-slate-400 focus:outline-none focus:border-[#f2920b] shadow-inner transition">
        </div>
        <button type="submit" class="group relative w-full inline-flex items-center justify-center gap-2.5 px-6 py-4 rounded-full bg-[#f2920b] hover:bg-[#76d3f6] active:bg-[#76d3f6] text-slate-950 active:scale-95 font-heading font-black text-sm uppercase tracking-wider transition-all duration-300 shadow-[0_6px_20px_rgba(0,0,0,0.2)] hover:shadow-[0_10px_25px_rgba(0,0,0,0.3)] hover:scale-[1.01] cursor-pointer">
          <span data-i18n="popup_btn">{t['popup_btn']}</span>
          <div class="w-6 h-6 rounded-full bg-slate-950/10 group-hover:bg-slate-950 group-hover:text-white flex items-center justify-center transition-all duration-300">
            <i data-lucide="download" class="w-3.5 h-3.5 stroke-[3] group-hover:translate-y-0.5 transition-transform duration-300"></i>
          </div>
        </button>
      </form>

    </div>
  </div>

  <!-- SCRIPTS & SISTEMA DE INTERNACIONALIZACIÓN (I18N) -->
  <script>
    lucide.createIcons();

    // DICCIONARIO REACTIVO MULTI-IDIOMA
    const I18N_DATA = {translations_json};
    let currentLang = '{active_lang}';
    const langFlags = {{ 'es': '🇪🇸', 'en': '🇬🇧', 'fr': '🇫🇷', 'it': '🇮🇹' }};

    function toggleLangDropdown(e) {{
      e.stopPropagation();
      const menu = document.getElementById('lang-dropdown-menu');
      const arrow = document.getElementById('lang-dropdown-arrow');
      if (!menu) return;
      const isHidden = menu.classList.contains('hidden');
      document.querySelectorAll('#lang-dropdown-menu, #lang-dropdown-menu-mob').forEach(m => m.classList.add('hidden'));
      if (isHidden) {{
        menu.classList.remove('hidden');
        if (arrow) arrow.style.transform = 'rotate(180deg)';
      }} else {{
        if (arrow) arrow.style.transform = 'rotate(0deg)';
      }}
    }}

    function toggleLangDropdownMob(e) {{
      e.stopPropagation();
      const menu = document.getElementById('lang-dropdown-menu-mob');
      const arrow = document.getElementById('lang-dropdown-arrow-mob');
      if (!menu) return;
      const isHidden = menu.classList.contains('hidden');
      document.querySelectorAll('#lang-dropdown-menu, #lang-dropdown-menu-mob').forEach(m => m.classList.add('hidden'));
      if (isHidden) {{
        menu.classList.remove('hidden');
        if (arrow) arrow.style.transform = 'rotate(180deg)';
      }} else {{
        if (arrow) arrow.style.transform = 'rotate(0deg)';
      }}
    }}

    document.addEventListener('click', () => {{
      const menu = document.getElementById('lang-dropdown-menu');
      const arrow = document.getElementById('lang-dropdown-arrow');
      if (menu) menu.classList.add('hidden');
      if (arrow) arrow.style.transform = 'rotate(0deg)';
      const menuMob = document.getElementById('lang-dropdown-menu-mob');
      const arrowMob = document.getElementById('lang-dropdown-arrow-mob');
      if (menuMob) menuMob.classList.add('hidden');
      if (arrowMob) arrowMob.style.transform = 'rotate(0deg)';
    }});

    function switchLanguage(lang) {{
      if (!I18N_DATA[lang]) return;
      currentLang = lang;
      
      try {{
        localStorage.setItem('coolpadel_lang', lang);
      }} catch(e) {{}}

      const dict = I18N_DATA[lang];

      // 1. Actualizar textos simples con data-i18n
      document.querySelectorAll('[data-i18n]').forEach(el => {{
        const key = el.getAttribute('data-i18n');
        if (dict[key]) {{
          el.innerHTML = dict[key];
        }}
      }});

      // 2. Actualizar placeholders
      document.querySelectorAll('[data-i18n-placeholder]').forEach(el => {{
        const key = el.getAttribute('data-i18n-placeholder');
        if (dict[key]) {{
          el.setAttribute('placeholder', dict[key]);
        }}
      }});

      // 3. Actualizar botones de WhatsApp
      const waMsg = encodeURIComponent(dict.wa_prefilled_msg);
      const waUrl = `https://wa.me/34680317486?text=${{waMsg}}`;
      
      const navWaBtn = document.getElementById('nav-contact-btn');
      if (navWaBtn) navWaBtn.href = waUrl;

      const navWaBtnMob = document.getElementById('nav-contact-btn-mob');
      if (navWaBtnMob) navWaBtnMob.href = waUrl;
      
      const smpWaBtn = document.getElementById('smp-contact-btn');
      if (smpWaBtn) smpWaBtn.href = waUrl;

      const contactWaBtn = document.getElementById('contact-wa-btn');
      if (contactWaBtn) contactWaBtn.href = waUrl;

      const floatWaBtn = document.getElementById('floating-wa-btn');
      if (floatWaBtn) floatWaBtn.href = waUrl;

      // 4. Actualizar labels y estilos del desplegable de idioma
      const codeEl = document.getElementById('current-lang-code');
      if (codeEl) codeEl.textContent = lang.toUpperCase();

      const codeElMob = document.getElementById('current-lang-code-mob');
      if (codeElMob) codeElMob.textContent = lang.toUpperCase();

      // Resaltar idioma activo con fondo naranja (#f2920b) y texto negro
      document.querySelectorAll('[data-lang-opt]').forEach(btn => {{
        const optLang = btn.getAttribute('data-lang-opt');
        if (optLang === lang) {{
          btn.className = 'lang-opt bg-[#f2920b] text-slate-950 font-black w-full text-center px-4 py-2 text-xs transition cursor-pointer';
          if (btn.closest('#lang-dropdown-menu-mob')) {{
            btn.className = 'lang-opt bg-[#f2920b] text-slate-950 font-black w-full text-center px-3 py-1.5 text-[11px] transition cursor-pointer';
          }}
        }} else {{
          btn.className = 'lang-opt text-slate-700 hover:bg-slate-100 font-bold w-full text-center px-4 py-2 text-xs transition cursor-pointer';
          if (btn.closest('#lang-dropdown-menu-mob')) {{
            btn.className = 'lang-opt text-slate-700 hover:bg-slate-100 font-bold w-full text-center px-3 py-1.5 text-[11px] transition cursor-pointer';
          }}
        }}
      }});

      // Cerrar dropdowns tras seleccionar
      const menu = document.getElementById('lang-dropdown-menu');
      if (menu) menu.classList.add('hidden');
      const menuMob = document.getElementById('lang-dropdown-menu-mob');
      if (menuMob) menuMob.classList.add('hidden');

      // 5. Actualizar calculadora
      updateCalculator(currentTierIdx, false);

      // Re-renderizar iconos de Lucide
      lucide.createIcons();
    }}

    // COVERFLOW 3D INFINITE CAROUSEL SCRIPT + GESTOS TÁCTILES SWIPE
    const slides = [
      document.getElementById('coverflow-0'),
      document.getElementById('coverflow-1'),
      document.getElementById('coverflow-2')
    ];
    let currentIndex = 0;
    const total = 3;
    let autoSlideInterval;
    let isPaused = false;

    function updateCoverflow() {{
      slides.forEach((slide, idx) => {{
        slide.classList.remove('active', 'prev', 'next');
        const diff = (idx - currentIndex + total) % total;
        
        if (diff === 0) {{
          slide.classList.add('active');
        }} else if (diff === 1) {{
          slide.classList.add('next');
        }} else if (diff === 2) {{
          slide.classList.add('prev');
        }}
      }});
    }}

    function nextSlide() {{
      currentIndex = (currentIndex + 1) % total;
      updateCoverflow();
    }}

    function prevSlide() {{
      currentIndex = (currentIndex - 1 + total) % total;
      updateCoverflow();
    }}

    // Clic directo en slides
    slides.forEach((slide, idx) => {{
      slide.addEventListener('click', (e) => {{
        if (idx !== currentIndex) {{
          e.preventDefault();
          currentIndex = idx;
          updateCoverflow();
          resetAutoSlide();
        }}
      }});
    }});

    function startAutoSlide() {{
      if (!isPaused) {{
        autoSlideInterval = setInterval(nextSlide, 4500);
      }}
    }}

    function resetAutoSlide() {{
      clearInterval(autoSlideInterval);
      startAutoSlide();
    }}

    startAutoSlide();

    // SOPORTE DE SWIPE TÁCTIL EN MÓVIL (DEDO IZQUIERDA / DERECHA)
    let touchStartX = 0;
    let touchEndX = 0;
    const coverflowEl = document.querySelector('.coverflow-wrapper');
    if (coverflowEl) {{
      coverflowEl.addEventListener('touchstart', (e) => {{
        touchStartX = e.changedTouches[0].screenX;
      }}, {{ passive: true }});

      coverflowEl.addEventListener('touchend', (e) => {{
        touchEndX = e.changedTouches[0].screenX;
        const diff = touchEndX - touchStartX;
        if (Math.abs(diff) > 40) {{
          if (diff < 0) nextSlide();
          else prevSlide();
          resetAutoSlide();
        }}
      }}, {{ passive: true }});
    }}

    // Calculadora presupuesto con tarifario oficial e i18n
    const tiers = [
      {{ qty: '100', price: '300', unit: '3,00', pct: 0 }},
      {{ qty: '250', price: '625', unit: '2,50', pct: 33.333 }},
      {{ qty: '500', price: '1.000', unit: '2,00', pct: 66.666 }},
      {{ qty: '1500', price: '2.250', unit: '1,50', pct: 100 }}
    ];

    let currentTierIdx = 0;
    const qtyBadge = document.getElementById('calc-qty-badge');
    const priceBadge = document.getElementById('calc-price-badge');
    const unitBadge = document.getElementById('calc-unit-badge');
    const waBtn = document.getElementById('calc-wa-btn');
    const sliderThumb = document.getElementById('slider-thumb');
    const sliderProgress = document.getElementById('slider-progress');
    const sliderTrack = document.getElementById('slider-track');

    function updateCalculator(idx, isLiveDrag = false) {{
      currentTierIdx = idx;
      const tier = tiers[idx];
      const dict = I18N_DATA[currentLang] || I18N_DATA['es'];
      
      qtyBadge.textContent = `${{tier.qty}} ${{dict.calc_unit_name}}`;
      priceBadge.textContent = `${{tier.price}}€`;
      unitBadge.textContent = `(${{tier.unit}}€/${{dict.calc_unit_price}})`;
      
      if (sliderThumb && sliderProgress) {{
        if (isLiveDrag) {{
          sliderThumb.style.transition = 'none';
          sliderProgress.style.transition = 'none';
        }} else {{
          sliderThumb.style.transition = 'left 0.25s cubic-bezier(0.25, 1, 0.5, 1)';
          sliderProgress.style.transition = 'width 0.25s cubic-bezier(0.25, 1, 0.5, 1)';
        }}
        sliderThumb.style.left = `${{tier.pct}}%`;
        sliderProgress.style.width = `${{tier.pct}}%`;
      }}
      
      const customMsg = encodeURIComponent(`${{dict.wa_prefilled_msg}}, me interesa solicitar presupuesto de ${{tier.qty}} llaveros para mi club.`);
      waBtn.href = `https://wa.me/34680317486?text=${{customMsg}}`;
    }}

    window.setTier = function(idx) {{
      updateCalculator(idx, false);
    }};

    // Control táctil y ratón del Slider optimizado (arrastre instantáneo sin marcas ni retardo)
    let isDragging = false;
    const sliderBox = document.getElementById('calc-slider-box');

    function handleSliderInteraction(clientX, isLive = false) {{
      if (!sliderTrack) return;
      const rect = sliderTrack.getBoundingClientRect();
      const x = Math.max(0, Math.min(clientX - rect.left, rect.width));
      const ratio = x / rect.width;
      
      let closestIdx = 0;
      let minDiff = 999;
      tiers.forEach((t, i) => {{
        const diff = Math.abs((t.pct / 100) - ratio);
        if (diff < minDiff) {{
          minDiff = diff;
          closestIdx = i;
        }}
      }});
      updateCalculator(closestIdx, isLive);
    }}

    if (sliderBox) {{
      // Eventos táctiles
      sliderBox.addEventListener('touchstart', (e) => {{
        isDragging = true;
        if (e.touches && e.touches.length > 0) {{
          handleSliderInteraction(e.touches[0].clientX, true);
        }}
      }}, {{ passive: true }});

      sliderBox.addEventListener('touchmove', (e) => {{
        if (!isDragging) return;
        if (e.touches && e.touches.length > 0) {{
          handleSliderInteraction(e.touches[0].clientX, true);
          if (e.cancelable) e.preventDefault();
        }}
      }}, {{ passive: false }});

      sliderBox.addEventListener('touchend', () => {{
        if (isDragging) {{
          isDragging = false;
          updateCalculator(currentTierIdx, false);
        }}
      }}, {{ passive: true }});

      sliderBox.addEventListener('touchcancel', () => {{
        isDragging = false;
        updateCalculator(currentTierIdx, false);
      }}, {{ passive: true }});

      // Eventos de ratón / puntero
      sliderBox.addEventListener('pointerdown', (e) => {{
        isDragging = true;
        handleSliderInteraction(e.clientX, true);
        window.addEventListener('pointermove', onPointerMove);
        window.addEventListener('pointerup', onPointerUp);
      }});

      function onPointerMove(e) {{
        if (isDragging) handleSliderInteraction(e.clientX, true);
      }}

      function onPointerUp() {{
        if (isDragging) {{
          isDragging = false;
          updateCalculator(currentTierIdx, false);
        }}
        window.removeEventListener('pointermove', onPointerMove);
        window.removeEventListener('pointerup', onPointerUp);
      }}
    }}

    // TOGGLE ACORDEÓN FAQ
    window.toggleFaq = function(btn) {{
      const answer = btn.nextElementSibling;
      const icon = btn.querySelector('.faq-icon');
      const isHidden = answer.classList.contains('hidden');
      
      document.querySelectorAll('.faq-answer').forEach(el => el.classList.add('hidden'));
      document.querySelectorAll('.faq-icon').forEach(el => el.classList.remove('rotate-180'));

      if (isHidden) {{
        answer.classList.remove('hidden');
        if (icon) icon.classList.add('rotate-180');
      }}
    }};

    // URL del Webhook de Google Apps Script (Recepción de Leads y Analítica de Eventos)
    const GOOGLE_SHEETS_WEBHOOK_URL = 'https://script.google.com/macros/s/AKfycbwm-6rDF4hpJMJeCJ26Vqfy-mg9Zvn7i4UJ-hWWx7xsvzreBU2WCGnCDoyKmR2Qt6CFSA/exec';

    // SISTEMA DE ANALÍTICA PRIVACY-FIRST (SIN COOKIES INVASIVAS)
    function trackEvent(eventName, extraData = {{}}) {{
      if (!GOOGLE_SHEETS_WEBHOOK_URL) return;
      try {{
        const payload = {{
          tipo: 'analitica_evento',
          evento: eventName,
          idioma: currentLang,
          zona_horaria: Intl.DateTimeFormat().resolvedOptions().timeZone || 'unknown',
          url: window.location.href,
          referrer: document.referrer || 'direct',
          fecha: new Date().toISOString(),
          ...extraData
        }};
        fetch(GOOGLE_SHEETS_WEBHOOK_URL, {{
          method: 'POST',
          mode: 'no-cors',
          headers: {{ 'Content-Type': 'application/json' }},
          body: JSON.stringify(payload)
        }}).catch(() => {{}});
      }} catch(e) {{}}
    }}

    // Descarga de PDF Informe con recolección de email a Google Sheets
    async function handleReportDownload(e) {{
      e.preventDefault();
      const emailInput = document.getElementById('report-email-input');
      const email = emailInput ? emailInput.value.trim() : '';
      if (!email) return;

      const reportFiles = {{
        'es': {{ url: '{asset_prefix}assets/reports/padel-industry-report-es.pdf', name: 'CoolPadel-Reportaje-Industria-Padel-2026-ES.pdf' }},
        'en': {{ url: '{asset_prefix}assets/reports/padel-industry-report-en.pdf', name: 'CoolPadel-Padel-Industry-Report-2026-ENG.pdf' }},
        'it': {{ url: '{asset_prefix}assets/reports/padel-industry-report-it.pdf', name: 'CoolPadel-Report-Industria-Padel-2026-IT.pdf' }},
        'fr': {{ url: '{asset_prefix}assets/reports/padel-industry-report-en.pdf', name: 'CoolPadel-Padel-Industry-Report-2026.pdf' }}
      }};
      const activeReport = reportFiles[currentLang] || reportFiles['es'];

      const link = document.createElement('a');
      link.href = activeReport.url;
      link.download = activeReport.name;
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);

      if (GOOGLE_SHEETS_WEBHOOK_URL) {{
        try {{
          fetch(GOOGLE_SHEETS_WEBHOOK_URL, {{
            method: 'POST',
            mode: 'no-cors',
            headers: {{ 'Content-Type': 'application/json' }},
            body: JSON.stringify({{
              email: email,
              origen: `Descarga Reportaje Industria Padel 2026 [${{currentLang.toUpperCase()}}]`,
              fecha: new Date().toISOString()
            }})
          }}).catch(err => console.log('Log Sheets:', err));
        }} catch (err) {{
          console.log('Error enviando al Sheet:', err);
        }}
      }}

      const dict = I18N_DATA[currentLang] || I18N_DATA['es'];
      const btn = e.target.querySelector('button[type="submit"] span');
      if (btn) {{
        const originalText = btn.textContent;
        btn.textContent = dict.report_card1_btn_success || '¡Informe Descargado!';
        setTimeout(() => {{
          btn.textContent = originalText;
          emailInput.value = '';
        }}, 3500);
      }}
    }}

    // POP-UP LEAD MAGNET LOGIC (TEMPORIZADOR PROGRESIVO Y NO INTRUSIVO)
    let modalTriggered = false;
    const pageStartTime = Date.now();

    window.openLeadModal = function() {{
      if (modalTriggered || sessionStorage.getItem('coolpadel_lead_dismissed')) return;
      modalTriggered = true;
      const modal = document.getElementById('lead-modal');
      const content = document.getElementById('lead-modal-content');
      if (modal && content) {{
        modal.classList.remove('opacity-0', 'pointer-events-none');
        modal.classList.add('opacity-100', 'pointer-events-auto');
        content.classList.remove('scale-95');
        content.classList.add('scale-100');
      }}
    }};

    window.closeLeadModal = function() {{
      sessionStorage.setItem('coolpadel_lead_dismissed', 'true');
      const modal = document.getElementById('lead-modal');
      const content = document.getElementById('lead-modal-content');
      if (modal && content) {{
        modal.classList.add('opacity-0', 'pointer-events-none');
        modal.classList.remove('opacity-100', 'pointer-events-auto');
        content.classList.add('scale-95');
        content.classList.remove('scale-100');
      }}
    }};

    // Triggers para el Pop-up: 50 segundos, scroll profundo (> 88%), o exit-intent tras 30s
    setTimeout(() => {{ openLeadModal(); }}, 50000);

    window.addEventListener('scroll', () => {{
      const scrollPct = (window.scrollY + window.innerHeight) / document.documentElement.scrollHeight;
      if (scrollPct > 0.88) openLeadModal();
    }}, {{ passive: true }});

    document.addEventListener('mouseleave', (e) => {{
      if (Date.now() - pageStartTime > 30000 && e.clientY <= 0) openLeadModal();
    }});

    async function handlePopupDownload(e) {{
      e.preventDefault();
      const emailInput = document.getElementById('popup-email-input');
      const email = emailInput ? emailInput.value.trim() : '';
      if (!email) return;

      const reportFiles = {{
        'es': {{ url: '{asset_prefix}assets/reports/padel-industry-report-es.pdf', name: 'CoolPadel-Reportaje-Industria-Padel-2026-ES.pdf' }},
        'en': {{ url: '{asset_prefix}assets/reports/padel-industry-report-en.pdf', name: 'CoolPadel-Padel-Industry-Report-2026-ENG.pdf' }},
        'it': {{ url: '{asset_prefix}assets/reports/padel-industry-report-it.pdf', name: 'CoolPadel-Report-Industria-Padel-2026-IT.pdf' }},
        'fr': {{ url: '{asset_prefix}assets/reports/padel-industry-report-en.pdf', name: 'CoolPadel-Padel-Industry-Report-2026.pdf' }}
      }};
      const activeReport = reportFiles[currentLang] || reportFiles['es'];

      const link = document.createElement('a');
      link.href = activeReport.url;
      link.download = activeReport.name;
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);

      if (GOOGLE_SHEETS_WEBHOOK_URL) {{
        try {{
          fetch(GOOGLE_SHEETS_WEBHOOK_URL, {{
            method: 'POST',
            mode: 'no-cors',
            headers: {{ 'Content-Type': 'application/json' }},
            body: JSON.stringify({{
              email: email,
              origen: `Lead Magnet Pop-up Modal [${{currentLang.toUpperCase()}}]`,
              fecha: new Date().toISOString()
            }})
          }}).catch(err => console.log('Log Sheets Modal:', err));
        }} catch (err) {{}}
      }}

      const dict = I18N_DATA[currentLang] || I18N_DATA['es'];
      const btn = e.target.querySelector('button[type="submit"] span');
      if (btn) {{
        btn.textContent = dict.popup_btn_success || '¡Descargando Informe!';
        setTimeout(() => {{
          closeLeadModal();
        }}, 2200);
      }}
    }}

    // INICIALIZACIÓN DE IDIOMA CON AUTO-DETECCIÓN INTELIGENTE POR NAVEGADOR
    try {{
      const urlParams = new URLSearchParams(window.location.search);
      const urlLang = urlParams.get('lang');
      const savedLang = localStorage.getItem('coolpadel_lang');
      
      let detectedLang = null;
      if (!savedLang && !urlLang) {{
        const navLang = (navigator.language || navigator.userLanguage || '').toLowerCase();
        if (navLang.startsWith('fr')) detectedLang = 'fr';
        else if (navLang.startsWith('it')) detectedLang = 'it';
        else if (navLang.startsWith('es')) detectedLang = 'es';
        else detectedLang = 'en'; // default internacional para el resto del mundo
      }}

      const initialLang = urlLang || savedLang || detectedLang;
      if (initialLang && I18N_DATA[initialLang] && initialLang !== '{active_lang}') {{
        switchLanguage(initialLang);
      }} else {{
        updateCalculator(0);
      }}
    }} catch(e) {{
      updateCalculator(0);
    }}

    // TRACKING AUTOMÁTICO DE VISITA Y CLICS EN BOTONES WHATSAPP / DESCARGAS
    try {{
      trackEvent('pageview', {{ path: window.location.pathname, lang_activa: currentLang }});
      
      const attachClick = (id, eventName, getExtra) => {{
        const el = document.getElementById(id);
        if (el) {{
          el.addEventListener('click', () => {{
            trackEvent(eventName, getExtra ? getExtra() : {{}});
          }});
        }}
      }};

      attachClick('nav-contact-btn', 'click_whatsapp_nav');
      attachClick('nav-contact-btn-mob', 'click_whatsapp_nav_mob');
      attachClick('calc-wa-btn', 'click_whatsapp_calc', () => ({{ tier_qty: tiers[currentTierIdx]?.qty, tier_price: tiers[currentTierIdx]?.price }}));
      attachClick('smp-contact-btn', 'click_whatsapp_savemyplay');
      attachClick('contact-wa-btn', 'click_whatsapp_footer');
      attachClick('floating-wa-btn', 'click_whatsapp_floating');
    }} catch(e) {{}}
  </script>
</body>
</html>"""
    return html

def build_all():
    import sys
    if sys.platform == "win32" and hasattr(sys.stdout, "reconfigure"):
        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except Exception:
            pass
    print(">> Generando versiones con Responsive Movil y Multilingue (ES, EN, FR, IT)...")
    
    # 1. Página principal (Español)
    es_html = get_base_html("es", is_subfolder=False)
    with open("coolpadel-web/index.html", "w", encoding="utf-8") as f:
        f.write(es_html)
    print("  [OK] coolpadel-web/index.html (ES Principal)")

    # 2. Subcarpetas para indexación SEO multilingüe
    for lang in ["en", "fr", "it"]:
        os.makedirs(f"coolpadel-web/{lang}", exist_ok=True)
        lang_html = get_base_html(lang, is_subfolder=True)
        with open(f"coolpadel-web/{lang}/index.html", "w", encoding="utf-8") as f:
            f.write(lang_html)
        print(f"  [OK] coolpadel-web/{lang}/index.html ({lang.upper()} SEO Landing)")

    # 3. Sitemap Multilingüe
    sitemap_xml = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:xhtml="http://www.w3.org/1999/xhtml"
        xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">
  <url>
    <loc>https://coolpadelstudios.com/</loc>
    <xhtml:link rel="alternate" hreflang="es" href="https://coolpadelstudios.com/"/>
    <xhtml:link rel="alternate" hreflang="en" href="https://coolpadelstudios.com/en/"/>
    <xhtml:link rel="alternate" hreflang="fr" href="https://coolpadelstudios.com/fr/"/>
    <xhtml:link rel="alternate" hreflang="it" href="https://coolpadelstudios.com/it/"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="https://coolpadelstudios.com/"/>
    <lastmod>2026-09-16</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
    <image:image>
      <image:loc>https://coolpadelstudios.com/assets/images/slide-1.jpg</image:loc>
      <image:title>Llaveros personalizados para clubs de padel y tenis</image:title>
    </image:image>
  </url>
  <url>
    <loc>https://coolpadelstudios.com/en/</loc>
    <xhtml:link rel="alternate" hreflang="es" href="https://coolpadelstudios.com/"/>
    <xhtml:link rel="alternate" hreflang="en" href="https://coolpadelstudios.com/en/"/>
    <xhtml:link rel="alternate" hreflang="fr" href="https://coolpadelstudios.com/fr/"/>
    <xhtml:link rel="alternate" hreflang="it" href="https://coolpadelstudios.com/it/"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="https://coolpadelstudios.com/"/>
    <lastmod>2026-09-16</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
  </url>
  <url>
    <loc>https://coolpadelstudios.com/fr/</loc>
    <xhtml:link rel="alternate" hreflang="es" href="https://coolpadelstudios.com/"/>
    <xhtml:link rel="alternate" hreflang="en" href="https://coolpadelstudios.com/en/"/>
    <xhtml:link rel="alternate" hreflang="fr" href="https://coolpadelstudios.com/fr/"/>
    <xhtml:link rel="alternate" hreflang="it" href="https://coolpadelstudios.com/it/"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="https://coolpadelstudios.com/"/>
    <lastmod>2026-09-16</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
  </url>
  <url>
    <loc>https://coolpadelstudios.com/it/</loc>
    <xhtml:link rel="alternate" hreflang="es" href="https://coolpadelstudios.com/"/>
    <xhtml:link rel="alternate" hreflang="en" href="https://coolpadelstudios.com/en/"/>
    <xhtml:link rel="alternate" hreflang="fr" href="https://coolpadelstudios.com/fr/"/>
    <xhtml:link rel="alternate" hreflang="it" href="https://coolpadelstudios.com/it/"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="https://coolpadelstudios.com/"/>
    <lastmod>2026-09-16</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
  </url>
</urlset>
"""
    with open("coolpadel-web/sitemap.xml", "w", encoding="utf-8") as f:
        f.write(sitemap_xml)
    print("  [OK] coolpadel-web/sitemap.xml (Multilingue con Hreflang)")

if __name__ == "__main__":
    build_all()
