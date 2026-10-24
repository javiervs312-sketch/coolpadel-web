#!/usr/bin/env python3
"""
Compilador Maestro de la Suite de Herramientas de CoolPadel Studios en 4 Idiomas:
- Hub de Herramientas (/herramientas/ y /{lang}/herramientas/)
- Calculadora ROI de Cámaras Save my Play (/herramientas/calculadora-roi-camaras-padel/)
- Calculadora Coste y Rentabilidad Pistas (/herramientas/calculadora-coste-pistas-padel/)
- Generador de Torneos de Americana (/herramientas/generador-americana-padel/)
- Generador de Cuadros de Torneo Brackets (/herramientas/generador-cuadros-torneo-padel/)
"""
import os
import sys

# Asegurar path local
cur_dir = os.path.dirname(os.path.abspath(__file__))
if cur_dir not in sys.path:
    sys.path.insert(0, cur_dir)

from translations_tools import (
    TOOLS_HUB_DATA,
    CALCULADORA_ROI_DATA,
    CALCULADORA_COSTES_DATA,
    GENERADOR_AMERICANA_DATA,
    GENERADOR_CUADROS_DATA
)
from build_tools_hub import build_hub

def get_tool_header(lang, slug, active_title):
    is_es = (lang == "es")
    prefix = "../../" if is_es else "../../../"
    home_href = "../../" if is_es else f"../../../{lang}/"
    camaras_href = "../../camaras/" if is_es else f"../../../{lang}/camaras/"
    llaveros_href = "../../#llaveros" if is_es else f"../../../{lang}/#llaveros"
    herramientas_href = "../" if is_es else f"../../../{lang}/herramientas/"
    barometro_href = "../../blog/barometro-camaras-padel-2026/" if is_es else f"../../../{lang}/blog/barometro-camaras-padel-2026/"
    blog_href = "../../blog/" if is_es else f"../../../{lang}/blog/"

    nav_labels = {
        "es": {"camaras": "Cámaras IA", "llaveros": "Llaveros 3D", "herramientas": "Herramientas", "barometro": "Barómetro", "blog": "Blog", "cta": "Ver Save my Play"},
        "en": {"camaras": "AI Cameras", "llaveros": "3D Keychains", "herramientas": "Tools", "barometro": "Barometer", "blog": "Blog", "cta": "Explore Save my Play"},
        "fr": {"camaras": "Caméras IA", "llaveros": "Porte-clés 3D", "herramientas": "Outils", "barometro": "Baromètre", "blog": "Blog", "cta": "Voir Save my Play"},
        "it": {"camaras": "Telecamere IA", "llaveros": "Portachiavi 3D", "herramientas": "Strumenti", "barometro": "Barometro", "blog": "Blog", "cta": "Scopri Save my Play"}
    }[lang]

    langs = ["es", "en", "fr", "it"]
    lang_links = []
    for l in langs:
        url = f"/herramientas/{slug}/" if l == "es" else f"/{l}/herramientas/{slug}/"
        if l == lang:
            lang_links.append(f'<a href="{url}" class="px-2 py-1 rounded text-xs transition bg-[#f2920b] text-slate-950 font-black">{l.upper()}</a>')
        else:
            lang_links.append(f'<a href="{url}" class="px-2 py-1 rounded text-xs transition text-slate-300 hover:text-white">{l.upper()}</a>')
    lang_switcher = f'<div class="flex items-center gap-1 border border-slate-700 rounded-lg p-0.5 bg-slate-800/80">{"".join(lang_links)}</div>'

    bc_home = {"es": "Inicio", "en": "Home", "fr": "Accueil", "it": "Home"}[lang]
    bc_tools = {"es": "Herramientas", "en": "Tools", "fr": "Outils", "it": "Strumenti"}[lang]

    return f"""  <!-- HEADER -->
  <header class="fixed top-0 left-0 w-full z-50 bg-white/95 backdrop-blur-md border-b border-slate-200/80 shadow-xs w-full">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 sm:h-20 flex items-center justify-between">
      
      <!-- LOGO: MASCOTA + TIPOGRAFÍA -->
      <a href="{home_href}" class="flex items-center gap-2 group shrink-0" aria-label="CoolPadel Home">
        <img src="{prefix}assets/images/coolpadel-mascot-hd.png" alt="Mascota CoolPadel" width="44" height="44" class="h-8 sm:h-11 w-auto object-contain group-hover:scale-105 transition" fetchpriority="high">
        <img src="{prefix}assets/images/coolpadel-typography-hd.png" alt="CoolPadel" width="140" height="28" class="h-5 sm:h-7 w-auto object-contain" fetchpriority="high">
      </a>

      <!-- BLOQUE DE NAVEGACIÓN Y ACCIONES A LA DERECHA (ESTILO EXACTO LANDINGS) -->
      <div class="flex items-center gap-2 sm:gap-4 lg:gap-6">
        <a href="{home_href}#llaveros" class="hidden sm:inline-block font-heading font-black text-xs uppercase tracking-wider text-slate-700 hover:text-[#f2920b] transition whitespace-nowrap">Llaveros</a>
        <a href="{herramientas_href}" class="hidden sm:inline-block font-heading font-black text-xs uppercase tracking-wider text-[#f2920b] transition whitespace-nowrap">{nav_labels['herramientas']}</a>
        <a href="{blog_href}" class="hidden sm:inline-block font-heading font-black text-xs uppercase tracking-wider text-slate-700 hover:text-[#f2920b] transition whitespace-nowrap">Blog</a>
        <a href="{home_href}franquicias-padel/" class="hidden sm:inline-block font-heading font-black text-xs uppercase tracking-wider text-slate-700 hover:text-[#f2920b] transition whitespace-nowrap">Cadenas de clubs</a>

        <!-- SELECTOR DE IDIOMA EN DESPLEGABLE COMPACTO -->
        <div class="relative inline-block text-left" id="lang-dropdown-container">
          <button type="button" onclick="toggleLangDropdown(event)" id="lang-dropdown-btn" class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-full bg-slate-100 hover:bg-slate-200 border border-slate-200 text-xs font-black text-slate-900 shadow-xs transition cursor-pointer" aria-expanded="false" aria-haspopup="true">
            <span class="uppercase font-black">{lang.upper()}</span>
            <i data-lucide="chevron-down" class="w-3.5 h-3.5 stroke-[2.5] text-slate-600 transition-transform duration-200" id="lang-dropdown-arrow"></i>
          </button>
          <div id="lang-dropdown-menu" class="hidden absolute right-0 mt-2 w-24 bg-white rounded-2xl shadow-[0_12px_30px_rgba(0,0,0,0.15)] border border-slate-200 py-1.5 z-50 transition-all overflow-hidden">
            <a href="/herramientas/" class="lang-opt block {'lang-opt-active' if lang=='es' else 'text-slate-700 hover:bg-[#f2920b] hover:text-slate-950 font-bold'} w-full text-center px-4 py-2 text-xs transition duration-150">ES</a>
            <a href="/en/herramientas/" class="lang-opt block {'lang-opt-active' if lang=='en' else 'text-slate-700 hover:bg-[#f2920b] hover:text-slate-950 font-bold'} w-full text-center px-4 py-2 text-xs transition duration-150">EN</a>
            <a href="/fr/herramientas/" class="lang-opt block {'lang-opt-active' if lang=='fr' else 'text-slate-700 hover:bg-[#f2920b] hover:text-slate-950 font-bold'} w-full text-center px-4 py-2 text-xs transition duration-150">FR</a>
            <a href="/it/herramientas/" class="lang-opt block {'lang-opt-active' if lang=='it' else 'text-slate-700 hover:bg-[#f2920b] hover:text-slate-950 font-bold'} w-full text-center px-4 py-2 text-xs transition duration-150">IT</a>
          </div>
        </div>

        <!-- BOTÓN CONTACTAR (ESTILO EXACTO LANDINGS) -->
        <a href="{home_href}#contacto" class="inline-flex items-center gap-1.5 px-3.5 sm:px-4 py-1.5 sm:py-2 rounded-full bg-[#f2920b] hover:bg-[#76d3f6] text-slate-950 font-heading font-black text-xs uppercase tracking-wider transition shadow-sm hover:scale-105 active:scale-95 cursor-pointer">
          <span>Contactar</span>
          <i data-lucide="arrow-down" class="w-3 h-3 stroke-[3]"></i>
        </a>

        <!-- OJOS DEL LOGO A LA DERECHA DEL TODO -->
        <a href="{home_href}" class="group py-1 inline-flex items-center shrink-0 pl-1" aria-label="CoolPadel Eyes">
          <img src="{prefix}assets/images/eyes-thumb.png?v=fixed_eyes" alt="CoolPadel Eyes" width="28" height="28" style="height: 26px; max-height: 26px; width: auto;" class="object-contain group-hover:scale-110 transition duration-300">
        </a>
      </div>
    </div>
  </header>
  <div class="h-16 sm:h-20 w-full shrink-0" aria-hidden="true"></div>


  <!-- BREADCRUMBS -->
  <div class="max-w-6xl mx-auto px-4 sm:px-6 pt-6 pb-2 text-xs text-slate-400 flex items-center gap-2">
    <a href="{home_href}" class="hover:text-white transition">{bc_home}</a>
    <i data-lucide="chevron-right" class="w-3.5 h-3.5"></i>
    <a href="{herramientas_href}" class="hover:text-white transition">{bc_tools}</a>
    <i data-lucide="chevron-right" class="w-3.5 h-3.5"></i>
    <span class="text-slate-200 font-bold">{active_title}</span>
  </div>"""

def get_tool_footer(lang):
    prefix = "../../" if lang == "es" else "../../../"
    desc = {
        "es": "CoolPadel Studios & Save my Play · Sistemas Inteligentes de Grabación en Pista y Soluciones B2B",
        "en": "CoolPadel Studios & Save my Play · Smart On-Court Camera Systems and B2B Club Solutions",
        "fr": "CoolPadel Studios & Save my Play · Systèmes Connectés d'Enregistrement sur Piste et Solutions B2B",
        "it": "CoolPadel Studios & Save my Play · Telecamere Intelligenti da Campo e Soluzioni B2B"
    }[lang]
    pol = {"es": "Política de Devoluciones", "en": "Return Policy", "fr": "Politique de Retour", "it": "Politica di Reso"}[lang]

    return f"""  <!-- FOOTER INFERIOR -->
  <footer class="relative z-20 bg-[#3478a6] bg-textured-blue text-white pt-14 pb-10 border-t border-sky-700/40 text-xs">
    <div class="max-w-[1700px] mx-auto px-4 sm:px-8 space-y-10">
      <div class="flex flex-col sm:flex-row items-center justify-between gap-4 pb-8 border-b border-white/20">
        <div class="flex items-center gap-3.5">
          <img src="{prefix}assets/images/coolpadel-mascot-hd.png" alt="CoolPadel Mascota" width="60" height="60" class="h-10 sm:h-12 w-auto object-contain drop-shadow-sm" loading="lazy">
          <img src="{prefix}assets/images/coolpadel-typography-hd.png" alt="CoolPadel" width="160" height="32" class="h-5 sm:h-6 w-auto object-contain drop-shadow-sm" loading="lazy">
        </div>
        
      </div>

      <div class="pt-8 border-t border-white/20 flex flex-col sm:flex-row items-center justify-between gap-3 text-white/75 text-center sm:text-left">
        <span>© 2026 CoolPadel Studios · All rights reserved</span>
        <div class="flex items-center gap-3">
          <a href="/politica-de-devoluciones.html" class="hover:text-white/90 underline decoration-white/30 underline-offset-2 transition">{pol}</a>
          <span class="opacity-40">·</span>
          <a href="https://www.instagram.com/coolpadel_/" target="_blank" rel="noopener noreferrer" class="opacity-75 hover:opacity-100 transition text-white">@coolpadel_</a>
        </div>
      </div>
    </div>
  </footer>"""

def build_roi_page(lang):
    d = CALCULADORA_ROI_DATA[lang]
    slug = "calculadora-roi-camaras-padel"
    is_es = (lang == "es")
    canonical = f"https://coolpadelstudios.com/herramientas/{slug}/" if is_es else f"https://coolpadelstudios.com/{lang}/herramientas/{slug}/"
    asset_prefix = "../../" if is_es else "../../../"
    og_locale = {"es": "es_ES", "en": "en_US", "fr": "fr_FR", "it": "it_IT"}[lang]
    bc_current = {"es": "Calculadora ROI Cámaras", "en": "Camera ROI Calculator", "fr": "Calculateur ROI Caméras", "it": "Calcolatore ROI Telecamere"}[lang]

    # FAQs
    faqs_schema_items = [f'''          {{
            "@type": "Question",
            "name": "{item['q']}",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "{item['a']}"
            }}
          }}''' for item in d["faqs"]]
    faqs_cards_html = [f'''          <div class="bg-white border border-slate-200/90 rounded-2xl p-5 space-y-2 text-slate-900 shadow-xs">
            <h3 class="text-sm font-bold text-slate-950">{item['q']}</h3>
            <p class="text-xs text-slate-600 leading-relaxed">{item['a']}</p>
          </div>''' for item in d["faqs"]]

    pistas_word = {"es": "pistas", "en": "courts", "fr": "pistes", "it": "campi"}[lang]
    pista_sing = {"es": "pista", "en": "court", "fr": "piste", "it": "campo"}[lang]
    mes_word = {"es": "mes", "en": "mo", "fr": "mois", "it": "mese"}[lang]

    return f"""<!DOCTYPE html>
<html lang="{lang}" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{d['title']}</title>
  <meta name="description" content="{d['desc']}">
  <link rel="canonical" href="{canonical}">
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">

  <!-- SEO Multilingüe Hreflang -->
  <link rel="alternate" hreflang="es" href="https://coolpadelstudios.com/herramientas/{slug}/">
  <link rel="alternate" hreflang="en" href="https://coolpadelstudios.com/en/herramientas/{slug}/">
  <link rel="alternate" hreflang="fr" href="https://coolpadelstudios.com/fr/herramientas/{slug}/">
  <link rel="alternate" hreflang="it" href="https://coolpadelstudios.com/it/herramientas/{slug}/">
  <link rel="alternate" hreflang="x-default" href="https://coolpadelstudios.com/herramientas/{slug}/">
  <meta name="language" content="{lang}">

  <!-- Open Graph -->
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="Save my Play & CoolPadel Studios">
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
  <link rel="icon" type="image/png" href="{asset_prefix}assets/images/favicon_transparente.png?v=transp3">
  <link rel="apple-touch-icon" sizes="180x180" href="{asset_prefix}assets/images/favicon_transparente.png?v=transp3">
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
    input[type=range] {{ accent-color: #f2920b; }}
  </style>

  <!-- Schema.org WebApplication & FAQPage -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@graph": [
      {{
        "@type": "WebApplication",
        "@id": "{canonical}#app",
        "name": "{d['title']}",
        "applicationCategory": "BusinessApplication",
        "operatingSystem": "All",
        "description": "{d['desc']}",
        "offers": {{ "@type": "Offer", "price": "0", "priceCurrency": "EUR" }}
      }},
      {{
        "@type": "BreadcrumbList",
        "itemListElement": [
          {{ "@type": "ListItem", "position": 1, "name": "{'Inicio' if is_es else 'Home'}", "item": "https://coolpadelstudios.com{'' if is_es else '/' + lang + '/'}" }},
          {{ "@type": "ListItem", "position": 2, "name": "{'Herramientas' if is_es else 'Tools' if lang == 'en' else 'Outils' if lang == 'fr' else 'Strumenti'}", "item": "https://coolpadelstudios.com{'/herramientas/' if is_es else '/' + lang + '/herramientas/'}" }},
          {{ "@type": "ListItem", "position": 3, "name": "{bc_current}", "item": "{canonical}" }}
        ]
      }},
      {{
        "@type": "FAQPage",
        "mainEntity": [
{',\n'.join(faqs_schema_items)}
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

{get_tool_header(lang, slug, bc_current)}

  <main class="flex-1 py-6 sm:py-10">
    <div class="max-w-5xl mx-auto px-4 sm:px-6">

      <!-- HERO HEAD -->
      <div class="text-center space-y-3 mb-10 max-w-3xl mx-auto">
        <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-sky-950/80 border border-sky-800/80 text-xs font-bold text-[#76d3f6] uppercase tracking-wider">
          <i data-lucide="line-chart" class="w-3.5 h-3.5"></i>
          <span>{d['badge']}</span>
        </div>
        <h1 class="text-3xl sm:text-5xl font-black font-heading text-white tracking-tight leading-tight">
          {d['h1']}
        </h1>
        <p class="text-xs sm:text-sm text-slate-300 leading-relaxed">
          {d['lead']}
        </p>
      </div>

      <!-- CALCULADORA INTERACTIVA -->
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start bg-white border border-slate-200/90 rounded-3xl p-6 sm:p-10 shadow-lg text-slate-900">

        <!-- PANEL IZQUIERDO -->
        <div class="lg:col-span-7 space-y-6">
          <h2 class="text-lg sm:text-xl font-black font-heading text-white border-b border-slate-800 pb-3 flex items-center gap-2">
            <i data-lucide="sliders" class="w-5 h-5 text-[#f2920b]"></i>
            <span>{d['s1_title']}</span>
          </h2>

          <!-- CONTROL 1: PISTAS -->
          <div class="space-y-2">
            <div class="flex justify-between items-center">
              <label class="text-xs sm:text-sm font-bold text-slate-200">{d['label_pistas']}</label>
              <span id="label-pistas" class="text-base sm:text-lg font-black text-[#f2920b] font-heading bg-slate-100 px-3 py-0.5 rounded-lg">4 {pistas_word}</span>
            </div>
            <input type="range" id="input-pistas" min="1" max="16" value="4" class="w-full h-2 bg-slate-800 rounded-lg cursor-pointer">
            <div class="flex justify-between text-[10px] text-slate-500 font-bold">
              <span>1 {pista_sing}</span>
              <span>4 {pistas_word}</span>
              <span>8 {pistas_word}</span>
              <span>16 {pistas_word}</span>
            </div>
          </div>

          <!-- CONTROL 2: PLAN -->
          <div class="space-y-2 pt-2">
            <label class="text-xs sm:text-sm font-bold text-slate-200">{d['label_plan']}</label>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
              <button type="button" id="btn-plan-b" onclick="selectPlan('B')" class="p-3.5 rounded-2xl border-2 border-sky-400 bg-sky-950/40 text-left transition flex flex-col justify-between cursor-pointer">
                <div class="flex items-center justify-between">
                  <span class="text-xs font-black uppercase text-sky-300">{d['plan_b_tag']}</span>
                  <i data-lucide="check-circle" class="w-4 h-4 text-sky-400"></i>
                </div>
                <div class="mt-2">
                  <span class="text-2xl font-black font-heading text-white">45 €</span>
                  <span class="text-xs text-slate-400">/ {pista_sing} / {mes_word}</span>
                </div>
                <p class="text-[11px] text-slate-300 mt-1">{d['plan_b_desc']}</p>
              </button>

              <button type="button" id="btn-plan-a" onclick="selectPlan('A')" class="p-3.5 rounded-2xl border border-slate-200 bg-slate-50 text-left hover:border-[#f2920b] text-slate-900 transition flex flex-col justify-between cursor-pointer">
                <div class="flex items-center justify-between">
                  <span class="text-xs font-black uppercase text-slate-300">{d['plan_a_tag']}</span>
                  <i data-lucide="circle" class="w-4 h-4 text-slate-500"></i>
                </div>
                <div class="mt-2">
                  <span class="text-2xl font-black font-heading text-white">136 €</span>
                  <span class="text-xs text-slate-400">/ {pista_sing} / {mes_word}</span>
                </div>
                <p class="text-[11px] text-slate-400 mt-1">{d['plan_a_desc']}</p>
              </button>
            </div>
          </div>

          <!-- CONTROL 3: PRECIO HORA -->
          <div class="space-y-2 pt-2">
            <div class="flex justify-between items-center">
              <label class="text-xs sm:text-sm font-bold text-slate-200">{d['label_precio']}</label>
              <span id="label-precio" class="text-base sm:text-lg font-black text-slate-950 font-heading bg-slate-100 px-3 py-0.5 rounded-lg">26 € / h</span>
            </div>
            <input type="range" id="input-precio" min="16" max="44" step="2" value="26" class="w-full h-2 bg-slate-800 rounded-lg cursor-pointer">
            <div class="flex justify-between text-[10px] text-slate-500 font-bold">
              <span>16 €</span>
              <span>26 €</span>
              <span>36 €</span>
              <span>44 €</span>
            </div>
          </div>

          <!-- CONTROL 4: HORAS VALLE -->
          <div class="space-y-2 pt-2">
            <div class="flex justify-between items-center">
              <label class="text-xs sm:text-sm font-bold text-slate-200">{d['label_horas_valle']}</label>
              <span id="label-horas-valle" class="text-base sm:text-lg font-black text-emerald-600 font-heading bg-slate-100 px-3 py-0.5 rounded-lg">+4 h / {mes_word}</span>
            </div>
            <input type="range" id="input-horas-valle" min="1" max="15" value="4" class="w-full h-2 bg-slate-800 rounded-lg cursor-pointer">
            <p class="text-[11px] text-slate-400">{d['horas_valle_desc']}</p>
          </div>

          <!-- CONTROL 5: SPONSOR -->
          <div class="space-y-2 pt-2">
            <div class="flex justify-between items-center">
              <label class="text-xs sm:text-sm font-bold text-slate-200">{d['label_sponsor']}</label>
              <span id="label-sponsor" class="text-base sm:text-lg font-black text-slate-950 font-heading bg-slate-100 px-3 py-0.5 rounded-lg">30 € / {mes_word} / {pista_sing}</span>
            </div>
            <input type="range" id="input-sponsor" min="0" max="100" step="10" value="30" class="w-full h-2 bg-slate-800 rounded-lg cursor-pointer">
            <p class="text-[11px] text-slate-400">{d['sponsor_desc']}</p>
          </div>
        </div>

        <!-- PANEL DERECHO -->
        <div class="lg:col-span-5 bg-gradient-to-br from-slate-800 to-slate-900 border-2 border-slate-700/80 rounded-3xl p-6 sm:p-8 space-y-6 flex flex-col justify-between">
          <div class="space-y-5">
            <div class="flex items-center justify-between border-b border-slate-700 pb-3">
              <span class="text-xs font-black uppercase tracking-wider text-slate-400">{d['s2_title']}</span>
              <span class="px-2.5 py-1 rounded-full bg-emerald-500/10 text-emerald-400 text-xs font-black border border-emerald-500/20">{d['roi_badge']}</span>
            </div>

            <div class="flex justify-between items-center text-xs sm:text-sm">
              <span class="text-slate-300">{d['out_hardware_label']}</span>
              <strong id="out-hardware" class="text-white font-black font-heading text-base sm:text-lg">720 €</strong>
            </div>

            <div class="flex justify-between items-center text-xs sm:text-sm">
              <span class="text-slate-300">{d['out_cuota_label']}</span>
              <strong id="out-cuota-mensual" class="text-sky-400 font-black font-heading text-base sm:text-lg">180 € / {mes_word}</strong>
            </div>

            <div class="flex justify-between items-center text-xs sm:text-sm">
              <span class="text-slate-300">{d['out_ingresos_label']}</span>
              <strong id="out-ingresos-extra" class="text-emerald-400 font-black font-heading text-base sm:text-lg">+536 € / {mes_word}</strong>
            </div>

            <div class="bg-emerald-50 border border-emerald-300 text-slate-900 rounded-2xl p-5 text-center space-y-1">
              <span class="text-xs uppercase font-extrabold text-slate-400 tracking-wider">{d['out_beneficio_badge']}</span>
              <div id="out-beneficio-neto" class="text-3xl sm:text-4xl font-black font-heading text-emerald-400">+356 € / {mes_word}</div>
              <p class="text-[11px] text-slate-400">{d['out_beneficio_desc']}</p>
            </div>

            <div class="bg-slate-50 rounded-xl p-3.5 border border-slate-200 text-slate-900 space-y-1 text-center">
              <span class="text-[11px] font-bold text-slate-400">{d['out_amortizar_q']}</span>
              <div class="text-sm font-black text-white font-heading">
                {d['out_amortizar_prefix']} <span id="out-horas-amortizar" class="text-[#f2920b]">1,7 {d['out_amortizar_suffix']}</span>
              </div>
            </div>
          </div>

          <div class="pt-4 border-t border-slate-700/80">
            <a id="btn-cta-wa" href="#" target="_blank" rel="noopener noreferrer" class="w-full inline-flex items-center justify-center gap-2 py-3.5 px-4 rounded-2xl bg-[#f2920b] hover:bg-[#76d3f6] text-slate-950 font-heading font-black text-xs sm:text-sm uppercase tracking-wider transition shadow-lg hover:scale-[1.02]">
              <i data-lucide="message-circle" class="w-4 h-4 fill-slate-950"></i>
              <span>{d['cta_btn']}</span>
            </a>
            <p class="text-[10px] text-slate-400 text-center mt-2">{d['cta_sub']}</p>
          </div>
        </div>

      </div>

      <!-- FAQ SECTION -->
      <section class="mt-16 border-t border-slate-800 pt-12 space-y-6">
        <h2 class="text-2xl font-black font-heading text-white">{d['faq_title']}</h2>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
{chr(10).join(faqs_cards_html)}
        </div>
      </section>

    </div>
  </main>

{get_tool_footer(lang)}

  <script>
    lucide.createIcons();

    let planSeleccionado = 'B';
    const cuotaPorPista = {{ 'B': 45, 'A': 136 }};
    const pistasWord = "{pistas_word}";
    const pistaSing = "{pista_sing}";
    const mesWord = "{mes_word}";
    const amortizeSuffix = "{d['out_amortizar_suffix']}";

    const inPistas = document.getElementById('input-pistas');
    const inPrecio = document.getElementById('input-precio');
    const inHorasValle = document.getElementById('input-horas-valle');
    const inSponsor = document.getElementById('input-sponsor');

    function selectPlan(plan) {{
      planSeleccionado = plan;
      const btnA = document.getElementById('btn-plan-a');
      const btnB = document.getElementById('btn-plan-b');

      if (plan === 'B') {{
        btnB.className = "p-3.5 rounded-2xl border-2 border-sky-400 bg-sky-950/40 text-left transition flex flex-col justify-between cursor-pointer";
        btnB.querySelector('i').setAttribute('data-lucide', 'check-circle');
        btnB.querySelector('i').className = "w-4 h-4 text-sky-400";
        
        btnA.className = "p-3.5 rounded-2xl border border-slate-200 bg-slate-50 text-left hover:border-[#f2920b] text-slate-900 transition flex flex-col justify-between cursor-pointer";
        btnA.querySelector('i').setAttribute('data-lucide', 'circle');
        btnA.querySelector('i').className = "w-4 h-4 text-slate-500";
      }} else {{
        btnA.className = "p-3.5 rounded-2xl border-2 border-orange-400 bg-orange-950/40 text-left transition flex flex-col justify-between cursor-pointer";
        btnA.querySelector('i').setAttribute('data-lucide', 'check-circle');
        btnA.querySelector('i').className = "w-4 h-4 text-orange-400";

        btnB.className = "p-3.5 rounded-2xl border border-slate-200 bg-slate-50 text-left hover:border-[#f2920b] text-slate-900 transition flex flex-col justify-between cursor-pointer";
        btnB.querySelector('i').setAttribute('data-lucide', 'circle');
        btnB.querySelector('i').className = "w-4 h-4 text-slate-500";
      }}
      lucide.createIcons();
      recalcular();
    }}

    function recalcular() {{
      const pistas = parseInt(inPistas.value, 10);
      const precio = parseFloat(inPrecio.value);
      const horasValle = parseInt(inHorasValle.value, 10);
      const sponsor = parseInt(inSponsor.value, 10);

      document.getElementById('label-pistas').textContent = pistas + ' ' + (pistas > 1 ? pistasWord : pistaSing);
      document.getElementById('label-precio').textContent = precio + ' € / h';
      document.getElementById('label-horas-valle').textContent = '+' + horasValle + ' h / ' + mesWord;
      document.getElementById('label-sponsor').textContent = sponsor + ' € / ' + mesWord + ' / ' + pistaSing;

      const costeHardware = pistas * 180;
      const cuotaSoftware = pistas * cuotaPorPista[planSeleccionado];
      const ingresosHorasValle = pistas * horasValle * precio;
      const ingresosSponsor = pistas * sponsor;
      const ingresosTotales = ingresosHorasValle + ingresosSponsor;
      const beneficioNeto = ingresosTotales - cuotaSoftware;

      const horasParaAmortizar = (cuotaPorPista[planSeleccionado] / precio).toFixed(1);

      document.getElementById('out-hardware').textContent = costeHardware.toLocaleString('es-ES') + ' €';
      document.getElementById('out-cuota-mensual').textContent = cuotaSoftware.toLocaleString('es-ES') + ' € / ' + mesWord;
      document.getElementById('out-ingresos-extra').textContent = '+' + ingresosTotales.toLocaleString('es-ES') + ' € / ' + mesWord;
      
      const elBeneficio = document.getElementById('out-beneficio-neto');
      if (beneficioNeto >= 0) {{
        elBeneficio.textContent = '+' + beneficioNeto.toLocaleString('es-ES') + ' € / ' + mesWord;
        elBeneficio.className = "text-3xl sm:text-4xl font-black font-heading text-emerald-400";
      }} else {{
        elBeneficio.textContent = beneficioNeto.toLocaleString('es-ES') + ' € / ' + mesWord;
        elBeneficio.className = "text-3xl sm:text-4xl font-black font-heading text-amber-400";
      }}

      document.getElementById('out-horas-amortizar').textContent = horasParaAmortizar.replace('.', ',') + ' ' + amortizeSuffix;

      const waMsg = encodeURIComponent(
        "Hola! ROI Save my Play: " + pistas + " " + pistasWord + ", " +
        (planSeleccionado === 'B' ? 'Plan B (45€)' : 'Plan A (136€)') + ", +" + beneficioNeto + " €/" + mesWord
      );
      document.getElementById('btn-cta-wa').href = "https://wa.me/34641695437?text=" + waMsg;
    }}

    [inPistas, inPrecio, inHorasValle, inSponsor].forEach(input => {{
      input.addEventListener('input', recalcular);
    }});

    recalcular();
  </script>
  <script src="/assets/js/cp-analytics.js" defer></script>
</body>
</html>
"""

def build_costes_page(lang):
    d = CALCULADORA_COSTES_DATA[lang]
    slug = "calculadora-coste-pistas-padel"
    is_es = (lang == "es")
    canonical = f"https://coolpadelstudios.com/herramientas/{slug}/" if is_es else f"https://coolpadelstudios.com/{lang}/herramientas/{slug}/"
    asset_prefix = "../../" if is_es else "../../../"
    og_locale = {"es": "es_ES", "en": "en_US", "fr": "fr_FR", "it": "it_IT"}[lang]
    bc_current = {"es": "Coste y Rentabilidad Pistas", "en": "Court Cost & ROI", "fr": "Coût et Rentabilité Pistes", "it": "Costo e Redditività Campi"}[lang]

    # FAQs
    faqs_schema_items = [f'''          {{
            "@type": "Question",
            "name": "{item['q']}",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "{item['a']}"
            }}
          }}''' for item in d["faqs"]]
    faqs_cards_html = [f'''          <div class="bg-white border border-slate-200/90 rounded-2xl p-5 space-y-2 text-slate-900 shadow-xs">
            <h3 class="text-sm font-bold text-slate-950">{item['q']}</h3>
            <p class="text-xs text-slate-600 leading-relaxed">{item['a']}</p>
          </div>''' for item in d["faqs"]]

    camaras_url = "../../save-my-play/" if is_es else f"../../../{lang}/save-my-play/"

    return f"""<!DOCTYPE html>
<html lang="{lang}" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{d['title']}</title>
  <meta name="description" content="{d['desc']}">
  <link rel="canonical" href="{canonical}">
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">

  <!-- SEO Multilingüe Hreflang -->
  <link rel="alternate" hreflang="es" href="https://coolpadelstudios.com/herramientas/{slug}/">
  <link rel="alternate" hreflang="en" href="https://coolpadelstudios.com/en/herramientas/{slug}/">
  <link rel="alternate" hreflang="fr" href="https://coolpadelstudios.com/fr/herramientas/{slug}/">
  <link rel="alternate" hreflang="it" href="https://coolpadelstudios.com/it/herramientas/{slug}/">
  <link rel="alternate" hreflang="x-default" href="https://coolpadelstudios.com/herramientas/{slug}/">
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
  <link rel="icon" type="image/png" href="{asset_prefix}assets/images/favicon_transparente.png?v=transp3">
  <link rel="apple-touch-icon" sizes="180x180" href="{asset_prefix}assets/images/favicon_transparente.png?v=transp3">
  <meta name="theme-color" content="#0b1626">

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
    input[type=range] {{ accent-color: #f2920b; }}
  </style>

  <!-- Schema.org WebApplication & FAQPage -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@graph": [
      {{
        "@type": "WebApplication",
        "@id": "{canonical}#app",
        "name": "{d['title']}",
        "applicationCategory": "BusinessApplication",
        "operatingSystem": "All",
        "description": "{d['desc']}",
        "offers": {{ "@type": "Offer", "price": "0", "priceCurrency": "EUR" }}
      }},
      {{
        "@type": "BreadcrumbList",
        "itemListElement": [
          {{ "@type": "ListItem", "position": 1, "name": "{'Inicio' if is_es else 'Home'}", "item": "https://coolpadelstudios.com{'' if is_es else '/' + lang + '/'}" }},
          {{ "@type": "ListItem", "position": 2, "name": "{'Herramientas' if is_es else 'Tools' if lang == 'en' else 'Outils' if lang == 'fr' else 'Strumenti'}", "item": "https://coolpadelstudios.com{'/herramientas/' if is_es else '/' + lang + '/herramientas/'}" }},
          {{ "@type": "ListItem", "position": 3, "name": "{bc_current}", "item": "{canonical}" }}
        ]
      }},
      {{
        "@type": "FAQPage",
        "mainEntity": [
{',\n'.join(faqs_schema_items)}
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

{get_tool_header(lang, slug, bc_current)}

  <main class="flex-1 py-6 sm:py-10">
    <div class="max-w-6xl mx-auto px-4 sm:px-6">

      <!-- HERO HEAD -->
      <div class="text-center space-y-3 mb-8 max-w-3xl mx-auto">
        <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-sky-950/80 border border-sky-800/80 text-xs font-bold text-[#76d3f6] uppercase tracking-wider">
          <i data-lucide="calculator" class="w-3.5 h-3.5"></i>
          <span>{d['badge']}</span>
        </div>
        <h1 class="text-3xl sm:text-5xl font-black font-heading text-white tracking-tight leading-tight">
          {d['h1']}
        </h1>
        <p class="text-xs sm:text-sm text-slate-300 leading-relaxed">
          {d['lead']}
        </p>
      </div>

      <!-- GRID CALCULADORA -->
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start mb-12">

        <!-- PARÁMETROS (7 COLS) -->
        <div class="lg:col-span-7 bg-white border border-slate-200/90 rounded-3xl p-6 sm:p-8 space-y-6 shadow-lg text-slate-900">
          <div class="flex items-center justify-between pb-3 border-b border-slate-800">
            <h2 class="font-heading font-black text-lg text-white">{d['s1_title']}</h2>
            <span class="text-xs text-[#f2920b] font-bold">{d['s1_badge']}</span>
          </div>

          <!-- PISTAS -->
          <div class="space-y-2">
            <div class="flex justify-between text-xs font-bold text-slate-300">
              <span>{d['label_pistas']}</span>
              <span id="label-num-pistas" class="text-white text-sm font-black">4</span>
            </div>
            <input type="range" id="input-pistas" min="1" max="16" value="4" oninput="actualizarCalculo()" class="w-full h-2 bg-slate-800 rounded-lg cursor-pointer">
          </div>

          <!-- TIPO DE PISTA -->
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 pt-2">
            <div>
              <label class="block text-xs font-bold text-slate-300 mb-1.5">{d['label_tipo_pista']}</label>
              <select id="select-tipo-pista" onchange="actualizarCalculo()" class="w-full bg-slate-50 border border-slate-300 text-slate-900 rounded-xl px-3 py-2 text-xs sm:text-sm text-white font-bold focus:border-[#f2920b] outline-none">
                <option value="panoramica" selected>{d['opt_panoramica']}</option>
                <option value="estandar">{d['opt_estandar']}</option>
                <option value="superpanoramica">{d['opt_superpanoramica']}</option>
              </select>
            </div>

            <div>
              <label class="block text-xs font-bold text-slate-300 mb-1.5">{d['label_solera']}</label>
              <select id="select-solera" onchange="actualizarCalculo()" class="w-full bg-slate-50 border border-slate-300 text-slate-900 rounded-xl px-3 py-2 text-xs sm:text-sm text-white font-bold focus:border-[#f2920b] outline-none">
                <option value="nueva" selected>{d['opt_solera_nueva']}</option>
                <option value="existente">{d['opt_solera_existente']}</option>
              </select>
            </div>
          </div>

          <!-- CESPED Y CAMARAS -->
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <div>
              <label class="block text-xs font-bold text-slate-300 mb-1.5">{d['label_cesped']}</label>
              <select id="select-cesped" onchange="actualizarCalculo()" class="w-full bg-slate-50 border border-slate-300 text-slate-900 rounded-xl px-3 py-2 text-xs sm:text-sm text-white font-bold focus:border-[#f2920b] outline-none">
                <option value="texturado" selected>{d['opt_cesped_texturado']}</option>
                <option value="monofilamento">{d['opt_cesped_monofilamento']}</option>
              </select>
            </div>

            <div>
              <label class="block text-xs font-bold text-slate-300 mb-1.5">{d['label_camaras']}</label>
              <select id="select-camaras" onchange="actualizarCalculo()" class="w-full bg-slate-50 border border-slate-300 text-slate-900 rounded-xl px-3 py-2 text-xs sm:text-sm text-white font-bold focus:border-[#76d3f6] outline-none">
                <option value="si" selected>{d['opt_camaras_si']}</option>
                <option value="no">{d['opt_camaras_no']}</option>
              </select>
            </div>
          </div>

          <div class="pt-4 border-t border-slate-800 flex items-center justify-between pb-2">
            <h2 class="font-heading font-black text-lg text-white">{d['s2_title']}</h2>
            <span class="text-xs text-emerald-400 font-bold">{d['s2_badge']}</span>
          </div>

          <!-- PRECIO HORA -->
          <div class="space-y-2">
            <div class="flex justify-between text-xs font-bold text-slate-300">
              <span>{d['label_precio_hora']}</span>
              <span id="label-precio-hora" class="text-white text-sm font-black">24 € / h</span>
            </div>
            <input type="range" id="input-precio-hora" min="12" max="48" value="24" oninput="actualizarCalculo()" class="w-full h-2 bg-slate-800 rounded-lg cursor-pointer">
          </div>

          <!-- HORAS DIA -->
          <div class="space-y-2">
            <div class="flex justify-between text-xs font-bold text-slate-300">
              <span>{d['label_horas_dia']}</span>
              <span id="label-horas-dia" class="text-white text-sm font-black">4.5 h</span>
            </div>
            <input type="range" id="input-horas-dia" min="2" max="10" step="0.5" value="4.5" oninput="actualizarCalculo()" class="w-full h-2 bg-slate-800 rounded-lg cursor-pointer">
          </div>

          <!-- GASTOS FIJOS -->
          <div class="space-y-2">
            <div class="flex justify-between text-xs font-bold text-slate-300">
              <span>{d['label_gastos_fijos']}</span>
              <span id="label-gastos-fijos" class="text-white text-sm font-black">2.500 €</span>
            </div>
            <input type="range" id="input-gastos-fijos" min="500" max="15000" step="250" value="2500" oninput="actualizarCalculo()" class="w-full h-2 bg-slate-800 rounded-lg cursor-pointer">
          </div>
        </div>

        <!-- RESULTADOS (5 COLS) -->
        <div class="lg:col-span-5 bg-gradient-to-br from-slate-800 to-slate-900 border-2 border-slate-700/80 rounded-3xl p-6 sm:p-8 space-y-6 shadow-2xl">
          <div class="border-b border-slate-700 pb-3 flex items-center justify-between">
            <h3 class="font-heading font-black text-base text-white uppercase tracking-wider">{d['s3_title']}</h3>
            <span class="px-2.5 py-0.5 rounded-full bg-emerald-500/10 text-emerald-400 text-xs font-bold border border-emerald-500/20">Proyección</span>
          </div>

          <div class="space-y-4">
            <div class="flex justify-between items-center text-xs sm:text-sm">
              <span class="text-slate-300">{d['out_inversion']}</span>
              <strong id="out-inversion" class="text-white font-black text-lg">150.000 €</strong>
            </div>

            <div class="flex justify-between items-center text-xs sm:text-sm">
              <span class="text-slate-300">{d['out_ingresos_brutos']}</span>
              <strong id="out-ingresos-brutos" class="text-emerald-400 font-black text-lg">12.960 € / mes</strong>
            </div>

            <div class="flex justify-between items-center text-xs sm:text-sm">
              <span class="text-slate-300">{d['out_gastos_operativos']}</span>
              <strong id="out-gastos-totales" class="text-slate-400 font-bold text-base">2.680 € / mes</strong>
            </div>

            <div class="bg-emerald-50 border border-emerald-300 text-slate-900 rounded-2xl p-5 text-center space-y-1">
              <span class="text-xs uppercase font-extrabold text-slate-400 tracking-wider">{d['out_beneficio_neto']}</span>
              <div id="out-beneficio-neto" class="text-3xl sm:text-4xl font-black font-heading text-emerald-400">+10.280 € / mes</div>
            </div>

            <div class="bg-slate-50 rounded-xl p-4 border border-slate-200 text-slate-900 space-y-1 text-center">
              <span class="text-xs font-bold text-slate-400">{d['out_payback_label']}</span>
              <div class="text-lg font-black text-[#f2920b] font-heading">
                <span id="out-meses-amortizacion">15</span> {d['out_payback_suffix']}
              </div>
            </div>
          </div>

          <!-- BANNER CAMARAS -->
          <div class="pt-4 border-t border-slate-700/80 space-y-2">
            <div class="p-4 rounded-2xl bg-sky-950/50 border border-sky-800/60 space-y-2">
              <span class="text-[10px] font-black uppercase tracking-wider text-[#76d3f6]">{d['banner_cam_badge']}</span>
              <h4 class="text-xs font-bold text-white">{d['banner_cam_title']}</h4>
              <p class="text-[11px] text-slate-300">{d['banner_cam_desc']}</p>
              <a href="{camaras_url}" class="inline-flex items-center gap-1.5 text-xs font-black text-[#76d3f6] hover:text-white transition pt-1">
                <span>{d['banner_cam_btn']}</span>
                <i data-lucide="arrow-right" class="w-3.5 h-3.5"></i>
              </a>
            </div>
          </div>
        </div>

      </div>

      <!-- FAQ SECTION -->
      <section class="border-t border-slate-800 pt-12 space-y-6">
        <h2 class="text-2xl font-black font-heading text-white">FAQ</h2>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
{chr(10).join(faqs_cards_html)}
        </div>
      </section>

    </div>
  </main>

{get_tool_footer(lang)}

  <script>
    lucide.createIcons();

    const COSTES_PISTA = {{
      panoramica: 23500,
      estandar: 18500,
      superpanoramica: 27000
    }};

    const COSTES_CESPED = {{
      texturado: 5500,
      monofilamento: 4200
    }};

    function actualizarCalculo() {{
      const numPistas = parseInt(document.getElementById('input-pistas').value);
      const tipoPista = document.getElementById('select-tipo-pista').value;
      const tieneSolera = document.getElementById('select-solera').value === 'nueva';
      const tipoCesped = document.getElementById('select-cesped').value;
      const tieneCamaras = document.getElementById('select-camaras').value === 'si';

      const precioHora = parseFloat(document.getElementById('input-precio-hora').value);
      const horasDia = parseFloat(document.getElementById('input-horas-dia').value);
      const gastosFijos = parseFloat(document.getElementById('input-gastos-fijos').value);

      document.getElementById('label-num-pistas').innerText = numPistas;
      document.getElementById('label-precio-hora').innerText = precioHora + ' € / h';
      document.getElementById('label-horas-dia').innerText = horasDia + ' h';
      document.getElementById('label-gastos-fijos').innerText = gastosFijos.toLocaleString('es-ES') + ' €';

      let costePista = COSTES_PISTA[tipoPista] + COSTES_CESPED[tipoCesped];
      if (tieneSolera) costePista += 8500;
      if (tieneCamaras) costePista += 180;

      const inversionTotal = costePista * numPistas;
      const facturacionMes = numPistas * horasDia * precioHora * 30;
      const cuotaCamarasMes = tieneCamaras ? (45 * numPistas) : 0;
      const gastosTotalesMes = gastosFijos + cuotaCamarasMes;
      const beneficioNetoMes = Math.max(0, facturacionMes - gastosTotalesMes);

      let mesesAmortizacion = beneficioNetoMes > 0 ? (inversionTotal / beneficioNetoMes).toFixed(1) : '99+';

      document.getElementById('out-inversion').innerText = inversionTotal.toLocaleString('es-ES') + ' €';
      document.getElementById('out-ingresos-brutos').innerText = facturacionMes.toLocaleString('es-ES') + ' € / mes';
      document.getElementById('out-gastos-totales').innerText = gastosTotalesMes.toLocaleString('es-ES') + ' € / mes';
      document.getElementById('out-beneficio-neto').innerText = '+' + beneficioNetoMes.toLocaleString('es-ES') + ' € / mes';
      document.getElementById('out-meses-amortizacion').innerText = mesesAmortizacion;
    }}

    actualizarCalculo();
  </script>
  <script src="/assets/js/cp-analytics.js" defer></script>
</body>
</html>
"""

def build_americana_page(lang):
    d = GENERADOR_AMERICANA_DATA[lang]
    slug = "generador-americana-padel"
    is_es = (lang == "es")
    canonical = f"https://coolpadelstudios.com/herramientas/{slug}/" if is_es else f"https://coolpadelstudios.com/{lang}/herramientas/{slug}/"
    asset_prefix = "../../" if is_es else "../../../"
    og_locale = {"es": "es_ES", "en": "en_US", "fr": "fr_FR", "it": "it_IT"}[lang]
    bc_current = {"es": "Generador Americana Pádel", "en": "Americano Generator", "fr": "Générateur Américana", "it": "Generatore Americana"}[lang]

    # Read base Spanish HTML to preserve the full tournament generator algorithms
    base_file = "coolpadel-web/herramientas/generador-americana-padel/index.html"
    with open(base_file, "r", encoding="utf-8") as f:
        base_html = f.read()

    # If Spanish, we only inject hreflang and language switcher in nav
    if is_es:
        html = base_html
        # Replace hreflang block
        hreflang_block = f"""  <!-- SEO Multilingüe Hreflang -->
  <link rel="alternate" hreflang="es" href="https://coolpadelstudios.com/herramientas/{slug}/">
  <link rel="alternate" hreflang="en" href="https://coolpadelstudios.com/en/herramientas/{slug}/">
  <link rel="alternate" hreflang="fr" href="https://coolpadelstudios.com/fr/herramientas/{slug}/">
  <link rel="alternate" hreflang="it" href="https://coolpadelstudios.com/it/herramientas/{slug}/">
  <link rel="alternate" hreflang="x-default" href="https://coolpadelstudios.com/herramientas/{slug}/">
  <meta name="language" content="es">"""
        if "<!-- SEO Multilingüe Hreflang -->" not in html:
            html = html.replace("<link rel=\"canonical\"", f"{hreflang_block}\n  <link rel=\"canonical\"")
        return html

    # For EN, FR, IT: translate metadata, header, hero, configuration labels, table headings, FAQs, and footer
    html = base_html
    html = html.replace('<html lang="es"', f'<html lang="{lang}"')
    html = html.replace('href="../../', f'href="{asset_prefix}')
    html = html.replace('src="../../', f'src="{asset_prefix}')
    html = html.replace('href="../"', f'href="{asset_prefix}{lang}/herramientas/"')
    html = html.replace('href="../calculadora-coste-pistas-padel/"', f'href="{asset_prefix}{lang}/herramientas/calculadora-coste-pistas-padel/"')

    # Replace Hreflang and Canonical
    hreflangs = f"""  <link rel="canonical" href="{canonical}">

  <!-- SEO Multilingüe Hreflang -->
  <link rel="alternate" hreflang="es" href="https://coolpadelstudios.com/herramientas/{slug}/">
  <link rel="alternate" hreflang="en" href="https://coolpadelstudios.com/en/herramientas/{slug}/">
  <link rel="alternate" hreflang="fr" href="https://coolpadelstudios.com/fr/herramientas/{slug}/">
  <link rel="alternate" hreflang="it" href="https://coolpadelstudios.com/it/herramientas/{slug}/">
  <link rel="alternate" hreflang="x-default" href="https://coolpadelstudios.com/herramientas/{slug}/">
  <meta name="language" content="{lang}">"""

    import re
    html = re.sub(r'<link rel="canonical"[^>]*>', hreflangs, html)
    html = re.sub(r'<title>.*?</title>', f'<title>{d["title"]}</title>', html)
    html = re.sub(r'<meta name="description" content=".*?">', f'<meta name="description" content="{d["desc"]}">', html)
    html = html.replace('content="es_ES"', f'content="{og_locale}"')

    # Header & Breadcrumbs
    header_block = get_tool_header(lang, slug, bc_current)
    html = re.sub(r'<!-- HEADER -->.*?<!-- BREADCRUMBS -->.*?</div>', header_block, html, flags=re.DOTALL)

    # Hero Badge, H1, Lead
    html = html.replace('Generador Oficial de Torneos y Pozos 2026', d['badge'])
    html = html.replace('Generador de <span class="text-[#f2920b]">Torneos de Americana</span> y Pozo de Pádel', d['h1'])
    html = html.replace('Crea cuadrantes y cruces equilibrados en 5 segundos. Todos juegan con todos y contra todos sin repetir compañeros. Listo para copiar y pegar en WhatsApp.', d['lead'])

    # Config Panel
    html = html.replace('1. Configuración de la Americana', d['s1_title'])
    html = html.replace('Número de Jugadores:', d['label_jugadores'])
    html = html.replace('Formato de Puntuación:', d['label_puntuacion'])
    html = html.replace('A 32 Puntos (Estándar recomendado)', d['opt_pts_32'])
    html = html.replace('A 24 Puntos (Rápido)', d['opt_pts_24'])
    html = html.replace('A 16 Puntos (Express)', d['opt_pts_16'])
    html = html.replace('Por Tiempo (15 min por ronda)', d['opt_pts_tiempo'])
    html = html.replace('Nombre del Torneo / Club:', d['label_nombre_torneo'])
    html = html.replace('Nombres de los Jugadores (separados por coma o salto de línea):', d['label_nombres_jugadores'])
    html = html.replace('Generar Cuadro de Americana', d['btn_generar'])

    # Buttons and live table
    html = html.replace('Copiar Formato para WhatsApp', d['btn_copiar_wa'])
    html = html.replace('Enviar Directo a WhatsApp', d['btn_enviar_wa'])
    html = html.replace('Clasificación General en Vivo', d['ranking_title'])
    html = html.replace('Puntos Favor', d['th_puntos'])
    html = html.replace('Diferencia', d['th_dif'])

    # Banner camaras
    html = html.replace('¿Organizas esta americana en tu club?', d['banner_cam_badge'])
    html = html.replace('Equipa tus pistas con cámaras Save my Play desde 45 €/mes', d['banner_cam_title'])
    html = html.replace('Graba automáticamente las finales y mejores jugadas de tus torneos. Los jugadores pulsarán el botón en la red y tendrán los highlights con tu logo para compartir en redes.', d['banner_cam_desc'])
    html = html.replace('Ver Cámaras para Clubes', d['banner_cam_btn'])

    # Footer
    footer_block = get_tool_footer(lang)
    html = re.sub(r'<!-- FOOTER INFERIOR.*?</footer>', footer_block, html, flags=re.DOTALL)

    return html

def build_cuadros_page(lang):
    d = GENERADOR_CUADROS_DATA[lang]
    slug = "generador-cuadros-torneo-padel"
    is_es = (lang == "es")
    canonical = f"https://coolpadelstudios.com/herramientas/{slug}/" if is_es else f"https://coolpadelstudios.com/{lang}/herramientas/{slug}/"
    asset_prefix = "../../" if is_es else "../../../"
    og_locale = {"es": "es_ES", "en": "en_US", "fr": "fr_FR", "it": "it_IT"}[lang]
    bc_current = {"es": "Generador Cuadros Torneo", "en": "Tournament Brackets", "fr": "Tableaux de Tournoi", "it": "Tabelloni Torneo"}[lang]

    base_file = "coolpadel-web/herramientas/generador-cuadros-torneo-padel/index.html"
    with open(base_file, "r", encoding="utf-8") as f:
        base_html = f.read()

    if is_es:
        html = base_html
        hreflang_block = f"""  <!-- SEO Multilingüe Hreflang -->
  <link rel="alternate" hreflang="es" href="https://coolpadelstudios.com/herramientas/{slug}/">
  <link rel="alternate" hreflang="en" href="https://coolpadelstudios.com/en/herramientas/{slug}/">
  <link rel="alternate" hreflang="fr" href="https://coolpadelstudios.com/fr/herramientas/{slug}/">
  <link rel="alternate" hreflang="it" href="https://coolpadelstudios.com/it/herramientas/{slug}/">
  <link rel="alternate" hreflang="x-default" href="https://coolpadelstudios.com/herramientas/{slug}/">
  <meta name="language" content="es">"""
        if "<!-- SEO Multilingüe Hreflang -->" not in html:
            html = html.replace("<link rel=\"canonical\"", f"{hreflang_block}\n  <link rel=\"canonical\"")
        return html

    html = base_html
    html = html.replace('<html lang="es"', f'<html lang="{lang}"')
    html = html.replace('href="../../', f'href="{asset_prefix}')
    html = html.replace('src="../../', f'src="{asset_prefix}')
    html = html.replace('href="../"', f'href="{asset_prefix}{lang}/herramientas/"')
    html = html.replace('href="../generador-americana-padel/"', f'href="{asset_prefix}{lang}/herramientas/generador-americana-padel/"')

    hreflangs = f"""  <link rel="canonical" href="{canonical}">

  <!-- SEO Multilingüe Hreflang -->
  <link rel="alternate" hreflang="es" href="https://coolpadelstudios.com/herramientas/{slug}/">
  <link rel="alternate" hreflang="en" href="https://coolpadelstudios.com/en/herramientas/{slug}/">
  <link rel="alternate" hreflang="fr" href="https://coolpadelstudios.com/fr/herramientas/{slug}/">
  <link rel="alternate" hreflang="it" href="https://coolpadelstudios.com/it/herramientas/{slug}/">
  <link rel="alternate" hreflang="x-default" href="https://coolpadelstudios.com/herramientas/{slug}/">
  <meta name="language" content="{lang}">"""

    import re
    html = re.sub(r'<link rel="canonical"[^>]*>', hreflangs, html)
    html = re.sub(r'<title>.*?</title>', f'<title>{d["title"]}</title>', html)
    html = re.sub(r'<meta name="description" content=".*?">', f'<meta name="description" content="{d["desc"]}">', html)
    html = html.replace('content="es_ES"', f'content="{og_locale}"')

    # Header & Breadcrumbs
    header_block = get_tool_header(lang, slug, bc_current)
    html = re.sub(r'<!-- HEADER -->.*?<!-- BREADCRUMBS -->.*?</div>', header_block, html, flags=re.DOTALL)

    # Hero Badge, H1, Lead
    html = html.replace('Generador Oficial de Cuadros de Eliminatoria 2026', d['badge'])
    html = html.replace('Generador de <span class="text-[#f2920b]">Cuadros de Torneo</span> de Pádel', d['h1'])
    html = html.replace('Diseña cuadros de competición por eliminatoria directa en segundos. Asigna cabezas de serie, cuadro de consolación, avance automático de ganadores e imprime en PDF.', d['lead'])

    # Config Panel
    html = html.replace('1. Configuración del Cuadro', d['s1_title'])
    html = html.replace('Tamaño del Cuadro:', d['label_tamano'])
    html = html.replace('8 Parejas (Cuartos de Final a Gran Final)', d['opt_8'])
    html = html.replace('16 Parejas (Octavos a Gran Final)', d['opt_16'])
    html = html.replace('32 Parejas (Dieciseisavos a Gran Final)', d['opt_32'])
    html = html.replace('Nombre del Torneo / Categoría:', d['label_nombre_torneo'])
    html = html.replace('Cuadro de Consolación:', d['label_consolacion'])
    html = html.replace('Sí, incluir cuadro de consolación para primeras derrotas', d['opt_consolacion_si'])
    html = html.replace('No, sólo cuadro principal', d['opt_consolacion_no'])
    html = html.replace('Nombres de las Parejas (1 por línea):', d['label_parejas'])
    html = html.replace('Generar Cuadro de Eliminatoria', d['btn_generar'])
    html = html.replace('Imprimir Cuadro (PDF / Póster)', d['btn_imprimir'])
    html = html.replace('Copiar Cuadro para WhatsApp', d['btn_copiar_wa'])
    html = html.replace('Enviar a WhatsApp', d['btn_enviar_wa'])

    # Titles in brackets
    html = html.replace('Cuadro Principal de Eliminatoria', d['bracket_main_title'])
    html = html.replace('Cuadro de Consolación', d['bracket_consolation_title'])
    html = html.replace('Campeón del Torneo', d['campeon_label'])

    # Banner
    html = html.replace('¿Quieres que los jugadores revivan las mejores jugadas de este torneo?', d['banner_cam_badge'])
    html = html.replace('Emite y graba torneos con las cámaras Save my Play', d['banner_cam_title'])
    html = html.replace('Permite que los participantes descarguen los vídeos de sus partidos de cuartos, semis y finales al instante con un simple botón en la red del poste.', d['banner_cam_desc'])
    html = html.replace('Solicitar Información Cámaras', d['banner_cam_btn'])

    # Footer
    footer_block = get_tool_footer(lang)
    html = re.sub(r'<!-- FOOTER INFERIOR.*?</footer>', footer_block, html, flags=re.DOTALL)

    return html

def build_all_tools():
    print(">> Compilando Suite Completa de Herramientas en 4 Idiomas (ES, EN, FR, IT)...")

    # 1. Hub
    for lang in ["es", "en", "fr", "it"]:
        html = build_hub(lang)
        out_path = "coolpadel-web/herramientas/index.html" if lang == "es" else f"coolpadel-web/{lang}/herramientas/index.html"
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"  [OK] Hub ({lang.upper()}): {out_path}")

    # 2. ROI Tool
    for lang in ["es", "en", "fr", "it"]:
        html = build_roi_page(lang)
        out_path = "coolpadel-web/herramientas/calculadora-roi-camaras-padel/index.html" if lang == "es" else f"coolpadel-web/{lang}/herramientas/calculadora-roi-camaras-padel/index.html"
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"  [OK] Calculadora ROI ({lang.upper()}): {out_path}")

    # 3. Costes Pistas Tool
    for lang in ["es", "en", "fr", "it"]:
        html = build_costes_page(lang)
        out_path = "coolpadel-web/herramientas/calculadora-coste-pistas-padel/index.html" if lang == "es" else f"coolpadel-web/{lang}/herramientas/calculadora-coste-pistas-padel/index.html"
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"  [OK] Calculadora Coste Pistas ({lang.upper()}): {out_path}")

    # 4. Americana Tool
    for lang in ["es", "en", "fr", "it"]:
        html = build_americana_page(lang)
        out_path = "coolpadel-web/herramientas/generador-americana-padel/index.html" if lang == "es" else f"coolpadel-web/{lang}/herramientas/generador-americana-padel/index.html"
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"  [OK] Generador Americana ({lang.upper()}): {out_path}")

    # 5. Cuadros Tool
    for lang in ["es", "en", "fr", "it"]:
        html = build_cuadros_page(lang)
        out_path = "coolpadel-web/herramientas/generador-cuadros-torneo-padel/index.html" if lang == "es" else f"coolpadel-web/{lang}/herramientas/generador-cuadros-torneo-padel/index.html"
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"  [OK] Generador Cuadros ({lang.upper()}): {out_path}")

    print(">> Suite de Herramientas 100% Cuatrilingue Completada Con Exito!")

if __name__ == "__main__":
    build_all_tools()
