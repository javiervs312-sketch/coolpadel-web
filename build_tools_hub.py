"""
Script de generacion para el Hub de Herramientas (/herramientas/) en 4 idiomas (ES, EN, FR, IT).
"""
import os
from translations_tools import TOOLS_HUB_DATA

def get_hub_nav(lang):
    prefix = "../" if lang == "es" else "../../"
    home_href = "../" if lang == "es" else f"../../{lang}/"
    llaveros_href = f"{home_href}#llaveros"
    camaras_href = f"{home_href}camaras/"
    franquicias_href = f"{home_href}franquicias-padel/"
    blog_href = f"{home_href}blog/"
    contacto_href = f"{home_href}#contacto"
    
    return f"""  <!-- CABECERA OFICIAL COOLPADEL (EXACTA A HOME) -->
  <header class="fixed top-0 left-0 w-full z-50 bg-white/95 backdrop-blur-md border-b border-slate-200/80 shadow-xs w-full">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 sm:h-20 flex items-center justify-between">
      
      <!-- LOGO: MASCOTA + TIPOGRAFÍA -->
      <a href="{home_href}" class="flex items-center gap-2 group shrink-0" aria-label="CoolPadel Home">
        <img src="{prefix}assets/images/coolpadel-mascot-hd.png" alt="Mascota CoolPadel" width="44" height="44" class="h-8 sm:h-11 w-auto object-contain group-hover:scale-105 transition" fetchpriority="high">
        <img src="{prefix}assets/images/coolpadel-typography-hd.png" alt="CoolPadel" width="140" height="28" class="h-5 sm:h-7 w-auto object-contain" fetchpriority="high">
      </a>

      <!-- BLOQUE DE NAVEGACIÓN Y ACCIONES A LA DERECHA (ESTILO EXACTO LANDINGS Y HOME) -->
      <div class="flex items-center gap-2 sm:gap-4 lg:gap-6">
        <a href="{llaveros_href}" class="hidden sm:inline-block font-heading font-black text-xs uppercase tracking-wider text-slate-700 hover:text-[#f2920b] transition whitespace-nowrap">LLAVEROS</a>
        <a href="{camaras_href}" class="hidden sm:inline-block font-heading font-black text-xs uppercase tracking-wider text-slate-700 hover:text-[#f2920b] transition whitespace-nowrap">CÁMARAS</a>
        <a href="{blog_href}" class="hidden sm:inline-block font-heading font-black text-xs uppercase tracking-wider text-slate-700 hover:text-[#f2920b] transition whitespace-nowrap">Blog</a>
        <a href="{franquicias_href}" class="hidden sm:inline-block font-heading font-black text-xs uppercase tracking-wider text-slate-700 hover:text-[#f2920b] transition whitespace-nowrap">Cadenas de clubs</a>

        <!-- SELECTOR DE IDIOMA EN DESPLEGABLE COMPACTO -->
        <div class="relative inline-block text-left" id="lang-dropdown-container">
          <button type="button" onclick="toggleLangDropdown(event)" id="lang-dropdown-btn" class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-full bg-slate-100 hover:bg-slate-200 border border-slate-200 text-xs font-black text-slate-900 shadow-xs transition cursor-pointer" aria-expanded="false" aria-haspopup="true">
            <span id="current-lang-code" class="uppercase font-black">{lang.upper()}</span>
            <i data-lucide="chevron-down" class="w-3.5 h-3.5 stroke-[2.5] text-slate-600 transition-transform duration-200" id="lang-dropdown-arrow"></i>
          </button>

          <!-- MENÚ DESPLEGABLE FLOTANTE -->
          <div id="lang-dropdown-menu" class="hidden absolute right-0 mt-2 w-24 bg-white rounded-2xl shadow-[0_12px_30px_rgba(0,0,0,0.15)] border border-slate-200 py-1.5 z-50 transition-all overflow-hidden">
            <a href="/herramientas/" data-lang-opt="es" class="lang-opt block {'lang-opt-active font-black' if lang=='es' else 'text-slate-700 hover:bg-[#f2920b] hover:text-slate-950 font-bold'} w-full text-center px-4 py-2 text-xs transition duration-150">
              ES
            </a>
            <a href="/en/herramientas/" data-lang-opt="en" class="lang-opt block {'lang-opt-active font-black' if lang=='en' else 'text-slate-700 hover:bg-[#f2920b] hover:text-slate-950 font-bold'} w-full text-center px-4 py-2 text-xs transition duration-150">
              EN
            </a>
            <a href="/fr/herramientas/" data-lang-opt="fr" class="lang-opt block {'lang-opt-active font-black' if lang=='fr' else 'text-slate-700 hover:bg-[#f2920b] hover:text-slate-950 font-bold'} w-full text-center px-4 py-2 text-xs transition duration-150">
              FR
            </a>
            <a href="/it/herramientas/" data-lang-opt="it" class="lang-opt block {'lang-opt-active font-black' if lang=='it' else 'text-slate-700 hover:bg-[#f2920b] hover:text-slate-950 font-bold'} w-full text-center px-4 py-2 text-xs transition duration-150">
              IT
            </a>
          </div>
        </div>

        <!-- BOTÓN CONTACTAR -->
        <a id="nav-contact-btn" href="{contacto_href}" class="inline-flex items-center gap-1.5 px-3.5 sm:px-4 py-1.5 sm:py-2 rounded-full bg-[#f2920b] hover:bg-[#76d3f6] text-slate-950 font-heading font-black text-xs uppercase tracking-wider transition shadow-sm hover:scale-105 active:scale-95 cursor-pointer">
          <span data-i18n="nav_contact">Contactar</span>
          <i data-lucide="arrow-down" class="w-3 h-3 stroke-[3]"></i>
        </a>

        <!-- OJOS DEL LOGO A LA DERECHA DEL TODO -->
        <a href="{home_href}" class="group py-1 inline-flex items-center shrink-0 pl-1" aria-label="CoolPadel Eyes">
          <img src="{prefix}assets/images/eyes-thumb.png?v=fixed_eyes" alt="CoolPadel Eyes" width="28" height="28" style="height: 26px; max-height: 26px; width: auto;" class="object-contain group-hover:scale-110 transition duration-300">
        </a>
      </div>
    </div>
  </header>

  <!-- Espaciador para compensar cabecera fija que acompaña al scroll -->
  <div class="h-16 sm:h-20 w-full shrink-0" aria-hidden="true"></div>"""

def get_hub_footer(lang):
    prefix = "../" if lang == "es" else "../../"
    root_url = "" if lang == "es" else f"/{lang}"
    
    col_titles = {
        "es": ("Soluciones B2B", "Herramientas & SaaS", "Directorio & Hubs", "Guías & Blog B2B"),
        "en": ("B2B Solutions", "Tools & SaaS", "Directory & Hubs", "Guides & B2B Blog"),
        "fr": ("Solutions B2B", "Outils & SaaS", "Annuaire & Hubs", "Guides & Blog B2B"),
        "it": ("Soluzioni B2B", "Strumenti & SaaS", "Directory & Hub", "Guide & Blog B2B")
    }[lang]

    desc = {
        "es": "Fabricación de llaveros de pádel personalizados 3D y sistemas de cámaras de grabación en pista Save my Play.",
        "en": "Custom 3D padel keychains manufacturing and Save my Play on-court smart camera recording systems.",
        "fr": "Fabrication de porte-clés padel 3D personnalisés et systèmes de caméras connectées Save my Play.",
        "it": "Produzione portachiavi padel personalizzati 3D e telecamere intelligenti da campo Save my Play."
    }[lang]

    return f"""  <!-- FOOTER INFERIOR -->
  <footer class="relative z-20 bg-[#3478a6] bg-textured-blue text-white pt-14 pb-10 border-t border-sky-700/40 text-xs">
    <div class="max-w-[1700px] mx-auto px-4 sm:px-8 space-y-10">
      
      <div class="flex flex-col sm:flex-row items-center justify-between gap-4 pb-8 border-b border-white/20">
        <div class="flex items-center gap-3.5">
          <img src="{prefix}assets/images/coolpadel-mascot-hd.png" alt="CoolPadel Mascota" width="60" height="60" class="h-10 sm:h-12 w-auto object-contain drop-shadow-sm" loading="lazy">
          <img src="{prefix}assets/images/coolpadel-typography-hd.png" alt="CoolPadel" width="160" height="32" class="h-5 sm:h-6 w-auto object-contain drop-shadow-sm" loading="lazy">
        </div>
        
      </div>

      <nav aria-label="Silos SEO" class="grid grid-cols-2 lg:grid-cols-4 gap-8 text-left">
        <div class="space-y-3">
          <div class="font-heading font-black text-sm uppercase tracking-wider text-white">{col_titles[0]}</div>
          <ul class="space-y-2 text-white/80 font-normal">
            <li><a href="{root_url}/llaveros-padel-personalizados/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">Llaveros Pádel 3D</a></li>
            <li><a href="{root_url}/llaveros-tenis-personalizados/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">Llaveros Tenis & Pickleball</a></li>
            <li><a href="{root_url}/welcome-packs-torneos-padel/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">Welcome Packs Torneos</a></li>
            <li><a href="{root_url}/save-my-play/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">Cámaras Save my Play</a></li>
            <li><a href="{root_url}/camaras-grabacion-pistas-padel/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">Grabación en Pista</a></li>
          </ul>
        </div>

        <div class="space-y-3">
          <div class="font-heading font-black text-sm uppercase tracking-wider text-white">{col_titles[1]}</div>
          <ul class="space-y-2 text-white/80 font-normal">
            <li><a href="{root_url}/herramientas/generador-americana-padel/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">Generador Americana</a></li>
            <li><a href="{root_url}/herramientas/generador-cuadros-torneo-padel/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">Generador Brackets</a></li>
            <li><a href="{root_url}/herramientas/calculadora-coste-pistas-padel/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">Calculadora Coste Pistas</a></li>
            <li><a href="{root_url}/herramientas/calculadora-roi-camaras-padel/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">Calculadora ROI Cámaras</a></li>
            <li><a href="{root_url}/camaras-padel-playtomic/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">Integración Playtomic</a></li>
          </ul>
        </div>

        <div class="space-y-3">
          <div class="font-heading font-black text-sm uppercase tracking-wider text-white">{col_titles[2]}</div>
          <ul class="space-y-2 text-white/80 font-normal">
            <li><a href="{root_url}/franquicias-padel/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">Directorio Franquicias (+167)</a></li>
            <li><a href="{root_url}/blog/barometro-camaras-padel-2026/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">Barómetro Pádel 2026</a></li>
            <li><a href="{root_url}/camaras-padel-madrid/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">Clubes Madrid</a></li>
            <li><a href="{root_url}/camaras-padel-barcelona/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">Clubes Barcelona</a></li>
          </ul>
        </div>

        <div class="space-y-3">
          <div class="font-heading font-black text-sm uppercase tracking-wider text-white">{col_titles[3]}</div>
          <ul class="space-y-2 text-white/80 font-normal">
            <li><a href="{root_url}/blog/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition font-bold text-white">Blog & Newsletter</a></li>
            <li><a href="{root_url}/blog/como-organizar-torneo-padel-americana-reglas-cuadros/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">Cómo Organizar una Americana</a></li>
            <li><a href="{root_url}/blog/cuanto-cuesta-montar-pista-padel-presupuesto-rentabilidad/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">Coste de Pistas 2026</a></li>
            <li><a href="{root_url}/blog/rentabilidad-camaras-pistas-padel/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">Precios y ROI Cámaras</a></li>
            <li><a href="{root_url}/blog/sistemas-grabacion-pistas-padel-comparativa/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">Cámaras vs Trípodes RGPD</a></li>
          </ul>
        </div>
      </nav>

      <div class="pt-8 border-t border-white/20 flex flex-col sm:flex-row items-center justify-between gap-3 text-white/75 text-center sm:text-left">
        <span>© 2026 CoolPadel Studios · All rights reserved</span>
        <div class="flex items-center gap-3">
          <a href="/politica-de-devoluciones.html" class="hover:text-white/90 underline decoration-white/30 underline-offset-2 transition">Política de Devoluciones</a>
          <span class="opacity-40">·</span>
          <a href="https://www.instagram.com/coolpadel_/" target="_blank" rel="noopener noreferrer" class="opacity-75 hover:opacity-100 transition text-white">@coolpadel_</a>
        </div>
      </div>
    </div>
  </footer>"""

def build_hub(lang):
    d = TOOLS_HUB_DATA[lang]
    canonical = "https://coolpadelstudios.com/herramientas/" if lang == "es" else f"https://coolpadelstudios.com/{lang}/herramientas/"
    prefix = "../" if lang == "es" else "../../"
    og_locale = {"es": "es_ES", "en": "en_US", "fr": "fr_FR", "it": "it_IT"}[lang]
    tool_prefix = "./" if lang == "es" else f"/{lang}/herramientas/"
    barometro_href = f"/{lang}/blog/barometro-camaras-padel-2026/" if lang != "es" else "/blog/barometro-camaras-padel-2026/"

    html = f"""<!DOCTYPE html>
<html lang="{lang}" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{d['title']}</title>
  <meta name="description" content="{d['desc']}">
  <link rel="canonical" href="{canonical}">
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">

  <!-- SEO Multilingüe Hreflang -->
  <link rel="alternate" hreflang="es" href="https://coolpadelstudios.com/herramientas/">
  <link rel="alternate" hreflang="en" href="https://coolpadelstudios.com/en/herramientas/">
  <link rel="alternate" hreflang="fr" href="https://coolpadelstudios.com/fr/herramientas/">
  <link rel="alternate" hreflang="it" href="https://coolpadelstudios.com/it/herramientas/">
  <link rel="alternate" hreflang="x-default" href="https://coolpadelstudios.com/herramientas/">
  <meta name="language" content="{lang}">

  <!-- Open Graph -->
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="CoolPadel Studios & Save my Play">
  <meta property="og:locale" content="{og_locale}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:title" content="{d['title']}">
  <meta property="og:description" content="{d['desc']}">
  <meta property="og:image" content="https://coolpadelstudios.com/assets/images/savemyplay-1.jpg">

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{d['title']}">
  <meta name="twitter:description" content="{d['desc']}">
  <meta name="twitter:image" content="https://coolpadelstudios.com/assets/images/savemyplay-1.jpg">

  <!-- Favicons -->
  <link rel="icon" type="image/png" href="{prefix}assets/images/favicon_transparente.png?v=transp3">
  <link rel="apple-touch-icon" sizes="180x180" href="{prefix}assets/images/favicon_transparente.png?v=transp3">
  <meta name="theme-color" content="#0b1626">

  <!-- LLM & AI Discovery -->
  <link rel="alternate" type="text/markdown" href="https://coolpadelstudios.com/llms.txt" title="LLMs.txt">
  <link rel="alternate" type="text/markdown" href="https://coolpadelstudios.com/llms-full.txt" title="LLMs-Full.txt">

  <!-- Fonts & Icons -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@600;700;800;900&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <script src="https://cdn.tailwindcss.com"></script>
  <script src="https://unpkg.com/lucide@0.468.0/dist/umd/lucide.min.js"></script>

  <style>
    body {{ font-family: 'Plus Jakarta Sans', sans-serif; }}
    h1, h2, h3, h4, .font-heading {{ font-family: 'Outfit', sans-serif; }}
    .bg-textured-blue {{
      background-color: #3478a6;
      background-image: linear-gradient(rgba(52, 120, 166, 0.40), rgba(52, 120, 166, 0.40)), url('/assets/images/branding/textura_editorial_coolpadel.webp');
      background-blend-mode: normal, soft-light;
      background-size: cover;
      background-position: center;
    }}
  </style>

  <!-- Schema.org CollectionPage & BreadcrumbList -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@graph": [
      {{
        "@type": "CollectionPage",
        "@id": "{canonical}#page",
        "url": "{canonical}",
        "name": "{d['title']}",
        "description": "{d['desc']}",
        "publisher": {{
          "@type": "Organization",
          "name": "CoolPadel Studios",
          "url": "https://coolpadelstudios.com"
        }}
      }},
      {{
        "@type": "BreadcrumbList",
        "itemListElement": [
          {{
            "@type": "ListItem",
            "position": 1,
            "name": "{'Inicio' if lang == 'es' else 'Home' if lang == 'en' else 'Accueil' if lang == 'fr' else 'Home'}",
            "item": "https://coolpadelstudios.com{'' if lang == 'es' else '/' + lang + '/'}"
          }},
          {{
            "@type": "ListItem",
            "position": 2,
            "name": "{'Herramientas' if lang == 'es' else 'Tools' if lang == 'en' else 'Outils' if lang == 'fr' else 'Strumenti'}",
            "item": "{canonical}"
          }}
        ]
      }}
    ]
  }}
  </script>
  <!-- Microsoft Clarity -->
  <script type="text/javascript">
    (function(c,l,a,r,i,t,y){{
      c[a]=c[a]||function(){{(c[a].q=c[a].q||[]).push(arguments)}};
      t=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i;
      y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);
    }})(window, document, "clarity", "script", "q7p8g52y9e");
  </script>
</head>
<body class="bg-slate-50 text-slate-900 min-h-screen flex flex-col selection:bg-[#f2920b] selection:text-slate-950">

{get_hub_nav(lang)}

  <!-- HERO -->
  <main class="flex-1">
    <section class="py-12 sm:py-20 px-4 sm:px-6 max-w-5xl mx-auto text-center space-y-4">
      <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-white border border-slate-200 text-xs font-bold text-slate-800 uppercase tracking-wider shadow-xs">
        <i data-lucide="wrench" class="w-3.5 h-3.5"></i>
        <span>{d['badge']}</span>
      </div>
      <h1 class="text-3xl sm:text-5xl font-black font-heading text-slate-950 tracking-tight leading-tight max-w-3xl mx-auto">
        {d['h1_prefix']} <span class="text-[#f2920b]">{d['h1_highlight']}</span> {d['h1_suffix']}
      </h1>
      <p class="text-sm sm:text-base text-slate-600 max-w-2xl mx-auto font-medium leading-relaxed">
        {d['lead']}
      </p>
    </section>

    <!-- GRID DE HERRAMIENTAS -->
    <section class="max-w-6xl mx-auto px-4 sm:px-6 pb-20">
      <div class="grid grid-cols-1 md:grid-cols-2 gap-6 lg:gap-8">

        <!-- HERRAMIENTA 1: CALCULADORA DE ROI CÁMARAS -->
        <article class="bg-white border-2 border-slate-200/90 rounded-3xl p-6 sm:p-8 flex flex-col justify-between hover:border-[#f2920b] hover:ring-4 hover:ring-[#f2920b]/20 hover:-translate-y-1 hover:shadow-xl transition-all duration-300 group shadow-sm text-slate-900">
          <div class="space-y-4">
            <div class="w-12 h-12 rounded-2xl bg-amber-500/10 border border-amber-400/20 text-[#f2920b] flex items-center justify-center">
              <i data-lucide="calculator" class="w-6 h-6 stroke-[2.5]"></i>
            </div>
            <div>
              <span class="text-xs font-black uppercase tracking-wider text-[#f2920b]">{d['t1_tag']}</span>
              <h2 class="text-xl sm:text-2xl font-black font-heading text-slate-950 mt-1 group-hover:text-[#f2920b] transition">
                {d['t1_title']}
              </h2>
            </div>
            <p class="text-xs sm:text-sm text-slate-600 leading-relaxed font-medium">
              {d['t1_desc']}
            </p>
            <ul class="text-xs text-slate-600 space-y-1.5 pt-2">
              <li class="flex items-center gap-2"><i data-lucide="check-circle-2" class="w-3.5 h-3.5 text-emerald-500"></i> {d['t1_b1']}</li>
              <li class="flex items-center gap-2"><i data-lucide="check-circle-2" class="w-3.5 h-3.5 text-emerald-500"></i> {d['t1_b2']}</li>
              <li class="flex items-center gap-2"><i data-lucide="check-circle-2" class="w-3.5 h-3.5 text-emerald-500"></i> {d['t1_b3']}</li>
            </ul>
          </div>
          <div class="pt-6 border-t border-slate-100 mt-6">
            <a href="{tool_prefix}calculadora-roi-camaras-padel/" class="w-full inline-flex items-center justify-center gap-2 py-3.5 rounded-2xl bg-[#f2920b] hover:bg-[#76d3f6] active:bg-[#76d3f6] text-slate-950 font-heading font-black text-xs sm:text-sm uppercase tracking-wider transition-all duration-300 shadow-sm hover:scale-[1.01] active:scale-[0.98] cursor-pointer">
              <span>{d['t1_btn']}</span>
              <i data-lucide="arrow-right" class="w-4 h-4 stroke-[3] group-hover:translate-x-1 transition-transform"></i>
            </a>
          </div>
        </article>

        <!-- HERRAMIENTA 2: GENERADOR DE AMERICANA -->
        <article class="bg-white border-2 border-slate-200/90 rounded-3xl p-6 sm:p-8 flex flex-col justify-between hover:border-[#f2920b] hover:ring-4 hover:ring-[#f2920b]/20 hover:-translate-y-1 hover:shadow-xl transition-all duration-300 group shadow-sm text-slate-900">
          <div class="space-y-4">
            <div class="w-12 h-12 rounded-2xl bg-amber-500/10 border border-amber-400/20 text-[#f2920b] flex items-center justify-center">
              <i data-lucide="trophy" class="w-6 h-6 stroke-[2.5]"></i>
            </div>
            <div>
              <span class="text-xs font-black uppercase tracking-wider text-[#f2920b]">{d['t2_tag']}</span>
              <h2 class="text-xl sm:text-2xl font-black font-heading text-slate-950 mt-1 group-hover:text-[#f2920b] transition">
                {d['t2_title']}
              </h2>
            </div>
            <p class="text-xs sm:text-sm text-slate-600 leading-relaxed font-medium">
              {d['t2_desc']}
            </p>
            <ul class="text-xs text-slate-600 space-y-1.5 pt-2">
              <li class="flex items-center gap-2"><i data-lucide="check-circle-2" class="w-3.5 h-3.5 text-emerald-500"></i> {d['t2_b1']}</li>
              <li class="flex items-center gap-2"><i data-lucide="check-circle-2" class="w-3.5 h-3.5 text-emerald-500"></i> {d['t2_b2']}</li>
              <li class="flex items-center gap-2"><i data-lucide="check-circle-2" class="w-3.5 h-3.5 text-emerald-500"></i> {d['t2_b3']}</li>
            </ul>
          </div>
          <div class="pt-6 border-t border-slate-100 mt-6">
            <a href="{tool_prefix}generador-americana-padel/" class="w-full inline-flex items-center justify-center gap-2 py-3.5 rounded-2xl bg-[#f2920b] hover:bg-[#76d3f6] active:bg-[#76d3f6] text-slate-950 font-heading font-black text-xs sm:text-sm uppercase tracking-wider transition-all duration-300 shadow-sm hover:scale-[1.01] active:scale-[0.98] cursor-pointer">
              <span>{d['t2_btn']}</span>
              <i data-lucide="arrow-right" class="w-4 h-4 stroke-[3] group-hover:translate-x-1 transition-transform"></i>
            </a>
          </div>
        </article>

        <!-- HERRAMIENTA 3: GENERADOR DE CUADROS DE TORNEO -->
        <article class="bg-white border-2 border-slate-200/90 rounded-3xl p-6 sm:p-8 flex flex-col justify-between hover:border-[#f2920b] hover:ring-4 hover:ring-[#f2920b]/20 hover:-translate-y-1 hover:shadow-xl transition-all duration-300 group shadow-sm text-slate-900">
          <div class="space-y-4">
            <div class="w-12 h-12 rounded-2xl bg-amber-500/10 border border-amber-400/20 text-[#f2920b] flex items-center justify-center">
              <i data-lucide="git-merge" class="w-6 h-6 stroke-[2.5]"></i>
            </div>
            <div>
              <span class="text-xs font-black uppercase tracking-wider text-[#f2920b]">{d['t3_tag']}</span>
              <h2 class="text-xl sm:text-2xl font-black font-heading text-slate-950 mt-1 group-hover:text-[#f2920b] transition">
                {d['t3_title']}
              </h2>
            </div>
            <p class="text-xs sm:text-sm text-slate-600 leading-relaxed font-medium">
              {d['t3_desc']}
            </p>
            <ul class="text-xs text-slate-600 space-y-1.5 pt-2">
              <li class="flex items-center gap-2"><i data-lucide="check-circle-2" class="w-3.5 h-3.5 text-emerald-500"></i> {d['t3_b1']}</li>
              <li class="flex items-center gap-2"><i data-lucide="check-circle-2" class="w-3.5 h-3.5 text-emerald-500"></i> {d['t3_b2']}</li>
              <li class="flex items-center gap-2"><i data-lucide="check-circle-2" class="w-3.5 h-3.5 text-emerald-500"></i> {d['t3_b3']}</li>
            </ul>
          </div>
          <div class="pt-6 border-t border-slate-100 mt-6">
            <a href="{tool_prefix}generador-cuadros-torneo-padel/" class="w-full inline-flex items-center justify-center gap-2 py-3.5 rounded-2xl bg-[#f2920b] hover:bg-[#76d3f6] active:bg-[#76d3f6] text-slate-950 font-heading font-black text-xs sm:text-sm uppercase tracking-wider transition-all duration-300 shadow-sm hover:scale-[1.01] active:scale-[0.98] cursor-pointer">
              <span>{d['t3_btn']}</span>
              <i data-lucide="arrow-right" class="w-4 h-4 stroke-[3] group-hover:translate-x-1 transition-transform"></i>
            </a>
          </div>
        </article>

        <!-- HERRAMIENTA 4: CALCULADORA DE COSTE Y MONTAJE DE PISTAS -->
        <article class="bg-white border-2 border-slate-200/90 rounded-3xl p-6 sm:p-8 flex flex-col justify-between hover:border-[#f2920b] hover:ring-4 hover:ring-[#f2920b]/20 hover:-translate-y-1 hover:shadow-xl transition-all duration-300 group shadow-sm text-slate-900">
          <div class="space-y-4">
            <div class="w-12 h-12 rounded-2xl bg-amber-500/10 border border-amber-400/20 text-[#f2920b] flex items-center justify-center">
              <i data-lucide="trending-up" class="w-6 h-6 stroke-[2.5]"></i>
            </div>
            <div>
              <span class="text-xs font-black uppercase tracking-wider text-[#f2920b]">{d['t4_tag']}</span>
              <h2 class="text-xl sm:text-2xl font-black font-heading text-slate-950 mt-1 group-hover:text-[#f2920b] transition">
                {d['t4_title']}
              </h2>
            </div>
            <p class="text-xs sm:text-sm text-slate-600 leading-relaxed font-medium">
              {d['t4_desc']}
            </p>
            <ul class="text-xs text-slate-600 space-y-1.5 pt-2">
              <li class="flex items-center gap-2"><i data-lucide="check-circle-2" class="w-3.5 h-3.5 text-emerald-500"></i> {d['t4_b1']}</li>
              <li class="flex items-center gap-2"><i data-lucide="check-circle-2" class="w-3.5 h-3.5 text-emerald-500"></i> {d['t4_b2']}</li>
              <li class="flex items-center gap-2"><i data-lucide="check-circle-2" class="w-3.5 h-3.5 text-emerald-500"></i> {d['t4_b3']}</li>
            </ul>
          </div>
          <div class="pt-6 border-t border-slate-100 mt-6">
            <a href="{tool_prefix}calculadora-coste-pistas-padel/" class="w-full inline-flex items-center justify-center gap-2 py-3.5 rounded-2xl bg-[#f2920b] hover:bg-[#76d3f6] active:bg-[#76d3f6] text-slate-950 font-heading font-black text-xs sm:text-sm uppercase tracking-wider transition-all duration-300 shadow-sm hover:scale-[1.01] active:scale-[0.98] cursor-pointer">
              <span>{d['t4_btn']}</span>
              <i data-lucide="arrow-right" class="w-4 h-4 stroke-[3] group-hover:translate-x-1 transition-transform"></i>
            </a>
          </div>
        </article>

      </div>

      <!-- BANNER DE RECURSOS DESCARGABLES ADICIONALES (FORMATO CLARO / TEXTURA) -->
      <div class="mt-12 bg-white border-2 border-slate-200/90 rounded-3xl p-6 sm:p-8 flex flex-col md:flex-row items-center justify-between gap-6 shadow-sm hover:border-[#f2920b] hover:ring-4 hover:ring-[#f2920b]/20 hover:-translate-y-1 hover:shadow-xl transition-all duration-300">
        <div class="space-y-2 text-center md:text-left">
          <span class="text-xs font-black text-[#f2920b] uppercase tracking-wider">{d['banner_tag']}</span>
          <h3 class="text-xl sm:text-2xl font-black font-heading text-slate-950">{d['banner_title']}</h3>
          <p class="text-xs sm:text-sm text-slate-600 max-w-xl font-medium leading-relaxed">
            {d['banner_desc']}
          </p>
        </div>
        <a href="{barometro_href}" class="px-6 py-3 rounded-2xl bg-[#f2920b] hover:bg-[#76d3f6] text-slate-950 font-heading font-black text-xs uppercase tracking-wider transition shrink-0 shadow-sm hover:scale-105 active:scale-95 cursor-pointer">
          <span>{d['banner_btn']}</span>
        </a>
      </div>
    </section>
  </main>

{get_hub_footer(lang)}

  <script>
    lucide.createIcons();
  </script>
  <script src="/assets/js/cp-analytics.js" defer></script>

  <script>
    function toggleLangDropdown(e) {{
      if (e) e.stopPropagation();
      const menu = document.getElementById('lang-dropdown-menu');
      const arrow = document.getElementById('lang-dropdown-arrow');
      if (!menu) return;
      const isHidden = menu.classList.contains('hidden');
      if (isHidden) {{
        menu.classList.remove('hidden');
        if (arrow) arrow.style.transform = 'rotate(180deg)';
      }} else {{
        menu.classList.add('hidden');
        if (arrow) arrow.style.transform = 'rotate(0deg)';
      }}
    }}
    document.addEventListener('click', function(e) {{
      const container = document.getElementById('lang-dropdown-container');
      const menu = document.getElementById('lang-dropdown-menu');
      const arrow = document.getElementById('lang-dropdown-arrow');
      if (container && !container.contains(e.target) && menu && !menu.classList.contains('hidden')) {{
        menu.classList.add('hidden');
        if (arrow) arrow.style.transform = 'rotate(0deg)';
      }}
    }});
  </script>
</body>
</html>
"""
    return html

def run():
    print(">> Generando Hub de Herramientas en 4 idiomas (ES, EN, FR, IT)...")
    for lang in ["es", "en", "fr", "it"]:
        html = build_hub(lang)
        if lang == "es":
            out_path = "coolpadel-web/herramientas/index.html"
        else:
            os.makedirs(f"coolpadel-web/{lang}/herramientas", exist_ok=True)
            out_path = f"coolpadel-web/{lang}/herramientas/index.html"
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"  [OK] {out_path} ({lang.upper()})")

if __name__ == "__main__":
    run()
