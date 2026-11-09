# -*- coding: utf-8 -*-
"""
Generador Maestro y Determinista de las 50 Landings B2B de Países de Pádel.
Cumple rigurosamente todos los requerimientos de Javier:
1. Generación en el idioma nativo de cada uno de los 50 países.
2. Slug en el nombre del país en su idioma nativo (ej: /camaras/sverige/, /camaras/france/, /camaras/deutschland/, etc.)
   y compatibilidad con slug en español (/camaras/suecia/, /camaras/francia/).
3. Precios y planes en su moneda local y equivalencia en euros/dólares, con la tarifa unificada de 3 filas:
   - Fila 1: Inversión Hardware en Propiedad (180 €)
   - Fila 2: Grabación, Highlights & Streaming (45 €/mes)
   - Fila 3: Estadísticas con IA y Análisis Táctico (136 €/mes)
4. Orden estricto de las secciones:
   - 1) Hero (H1 en 3 líneas exactas con tipografía reducida y sin texto de IA)
   - 2) ¿Por qué elegir Save My Play para tu club? (exactamente las 3 razones sin duplicar IA)
   - 3) Tabla de Tarifas
   - 4) Demostración en Pista Real (4 vídeos)
   - 5) Preguntas Frecuentes desplegables (<details><summary>)
   - 6) Bloque de Contacto Directo con tarjetas WhatsApp (con QR) y Email
   - 7) Pie de página azul con textura (idéntico al de español con los 4 silos SEO de enlaces)
"""

import os
import re
import urllib.parse
from paises_data_50 import COUNTRIES_50
from country_i18n_native_all import NATIVE_TRANSLATIONS_21
from country_i18n_native_part2 import REMAINING_13_LANGS

ALL_LANGS_MASTER = dict(NATIVE_TRANSLATIONS_21)
ALL_LANGS_MASTER.update(REMAINING_13_LANGS)

OUTPUT_ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'camaras')
os.makedirs(OUTPUT_ROOT, exist_ok=True)

def generate_country_page(item, slug_to_use, canonical_slug=None):
    lang = item["lang"]
    t = ALL_LANGS_MASTER.get(lang, ALL_LANGS_MASTER["en"])
    country_display = item["country_local"]
    
    hw = item["hw"]
    rec = item["rec"]
    ai = item["ai"]

    title = t["title"].format(country=country_display, hw=hw, rec=rec, ai=ai)
    meta_desc = t["meta_desc"].format(country=country_display, hw=hw, rec=rec, ai=ai)
    h1 = t["h1"]
    sub = t["sub"].format(country=country_display, hw=hw, rec=rec, ai=ai)
    
    wa_msg = t["wa_msg"].format(country=country_display)
    encoded_wa = urllib.parse.quote(wa_msg)
    wa_url = f"https://api.whatsapp.com/send?phone=34680317486&text={encoded_wa}"
    target_slug = canonical_slug if canonical_slug else slug_to_use
    canonical_url = f"https://coolpadelstudios.com/camaras/{target_slug}/"
    
    is_es = (lang == "es")
    nav_prefix = "/" if is_es else "/en/"
    
    # HTML dir for Arabic
    dir_attr = ' dir="rtl"' if lang == "ar" else ''
    
    html = f"""<!DOCTYPE html>
<html lang="{lang}"{dir_attr} class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{meta_desc}">
  <link rel="canonical" href="{canonical_url}">
  <meta name="robots" content="index, follow">

  <!-- Open Graph / Social -->
  <meta property="og:type" content="product">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{meta_desc}">
  <meta property="og:url" content="{canonical_url}">
  <meta property="og:site_name" content="CoolPadel Studios • Save My Play">
  <meta property="og:image" content="https://coolpadelstudios.com/assets/images/savemyplay-1.jpg">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{meta_desc}">
  <meta name="twitter:image" content="https://coolpadelstudios.com/assets/images/savemyplay-1.jpg">

  <link rel="icon" type="image/png" href="../../assets/images/favicon_transparente.png?v=transp3">
  <link rel="apple-touch-icon" sizes="180x180" href="../../assets/images/favicon_transparente.png?v=transp3">
  <meta name="theme-color" content="#0b1626">

  <!-- Fonts & Tailwind -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800;900&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {{
      theme: {{
        extend: {{
          fontFamily: {{
            heading: ['Outfit', 'sans-serif'],
            body: ['Plus Jakarta Sans', 'sans-serif'],
          }}
        }}
      }}
    }}
  </script>
  <script src="https://unpkg.com/lucide@latest"></script>

  <!-- Schema.org Microdata -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org/",
    "@type": ["Product", "Service"],
    "name": "Save My Play - {country_display}",
    "description": "{meta_desc}",
    "image": ["https://coolpadelstudios.com/assets/images/savemyplay-1.jpg"],
    "brand": {{
      "@type": "Brand",
      "name": "Save My Play"
    }},
    "offers": {{
      "@type": "AggregateOffer",
      "priceCurrency": "{item.get('curr_code', 'EUR')}",
      "lowPrice": "45",
      "highPrice": "180",
      "offerCount": "2",
      "availability": "https://schema.org/InStock"
    }}
  }}
  </script>
  <style>
    .bg-textured-blue {{
      background-color: #3478a6;
      background-image: radial-gradient(rgba(255, 255, 255, 0.08) 1px, transparent 0);
      background-size: 20px 20px;
    }}
  </style>
</head>
<body class="bg-white text-slate-800 font-body antialiased flex flex-col min-h-screen">

  <!-- HEADER -->
  <header class="fixed top-0 left-0 w-full z-50 bg-white/95 backdrop-blur-md border-b border-slate-200/80 shadow-xs">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 sm:h-20 flex items-center justify-between">
      <a href="{nav_prefix}" class="flex items-center gap-2 group">
        <img src="../../assets/images/coolpadel-mascot-hd.png" alt="CoolPadel Mascot" width="44" height="44" class="h-8 sm:h-11 w-auto object-contain">
        <img src="../../assets/images/coolpadel-typography-hd.png" alt="CoolPadel" width="140" height="28" class="h-5 sm:h-7 w-auto object-contain">
      </a>
      
      <div class="flex items-center gap-2 sm:gap-4 lg:gap-6">
        <a href="{nav_prefix}llaveros-padel-personalizados/" class="hidden sm:inline-block font-heading font-black text-xs uppercase tracking-wider text-slate-700 hover:text-[#f2920b] transition">{t["nav_llaveros"]}</a>
        <a href="{nav_prefix}camaras/" class="hidden sm:inline-block font-heading font-black text-xs uppercase tracking-wider text-slate-700 hover:text-[#f2920b] transition whitespace-nowrap">{t["nav_camaras"]}</a>
        <a href="{nav_prefix}blog/" class="hidden sm:inline-block font-heading font-black text-xs uppercase tracking-wider text-slate-700 hover:text-[#f2920b] transition">{t["nav_blog"]}</a>
        <a href="{nav_prefix}franquicias-padel/" class="hidden sm:inline-block font-heading font-black text-xs uppercase tracking-wider text-slate-700 hover:text-[#f2920b] transition">{t.get("nav_franquicias", "Cadenas de clubs")}</a>

        <a href="{wa_url}" target="_blank" rel="noopener" class="inline-flex items-center gap-2 px-4 py-2 sm:px-5 sm:py-2.5 rounded-full bg-[#f2920b] hover:bg-[#76d3f6] text-slate-950 font-heading font-black text-xs sm:text-sm uppercase tracking-wider transition shadow-sm hover:scale-105 active:scale-95">
          <i data-lucide="message-circle" class="w-4 h-4 text-slate-950"></i>
          <span>WhatsApp Demo</span>
        </a>

        <!-- OJOS DEL LOGO A LA DERECHA DEL TODO -->
        <a href="{nav_prefix}" class="group py-1 inline-flex items-center shrink-0 pl-1" aria-label="CoolPadel Eyes">
          <img src="../../assets/images/eyes-thumb.png?v=fixed_eyes" alt="CoolPadel Eyes" width="28" height="28" style="height: 26px; max-height: 26px; width: auto;" class="object-contain group-hover:scale-110 transition duration-300">
        </a>
      </div>
    </div>
  </header>

  <main class="flex-1 pt-20">

    <!-- 1. HERO SECTION -->
    <section class="py-12 sm:py-20 bg-gradient-to-b from-white via-slate-50 to-[#f8fafc] border-b border-slate-200">
      <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
        
        <!-- Breadcrumbs Navigation -->
        <nav aria-label="Breadcrumb" class="flex items-center gap-2 text-xs font-bold text-slate-500 mb-6 uppercase tracking-wider">
          <a href="{nav_prefix}" class="hover:text-slate-900 transition">{t["nav_home"]}</a>
          <span>/</span>
          <span class="hover:text-slate-900 transition">{t["nav_camaras"]}</span>
          <span>/</span>
          <span class="text-[#f2920b] font-black">{country_display} ({item['courts']} {t.get('nav_courts', 'Courts') if lang != 'es' else 'Pistas'})</span>
        </nav>

        <div class="grid lg:grid-cols-12 gap-8 sm:gap-12 items-center">
          
          <div class="lg:col-span-7 space-y-6">
            <div class="inline-flex items-center gap-2 text-[#f2920b] font-heading font-black text-xs uppercase tracking-wider">
              <i data-lucide="award" class="w-4 h-4"></i>
              <span>{t["badge"]}</span>
            </div>

            <!-- H1 FORMATTED IN 3 LINES -->
            <h1 class="font-heading font-black text-2xl sm:text-3xl lg:text-4xl text-slate-950 uppercase tracking-tight leading-[1.18]">
              {h1}
            </h1>

            <p class="text-base sm:text-lg text-slate-600 leading-relaxed font-normal">
              {sub}
            </p>

            <div class="pt-4 flex flex-col sm:flex-row items-stretch sm:items-center gap-3 sm:gap-4">
              <a href="{wa_url}" target="_blank" rel="noopener" class="inline-flex items-center justify-center gap-2.5 px-7 py-4 rounded-full bg-[#f2920b] hover:bg-[#76d3f6] text-slate-950 font-heading font-black text-sm uppercase tracking-wider transition shadow-md hover:scale-105 active:scale-95 group">
                <i data-lucide="message-circle" class="w-5 h-5 text-slate-950"></i>
                <span>{t["demo_btn"]}</span>
              </a>

              <a href="#precios" class="inline-flex items-center justify-center gap-2 px-6 py-4 rounded-full bg-white hover:bg-slate-100 text-slate-900 border border-slate-200 font-heading font-black text-sm uppercase tracking-wider transition">
                <span>{t["rates_btn"]}</span>
                <i data-lucide="arrow-down" class="w-4 h-4 text-slate-500"></i>
              </a>
            </div>
          </div>

          <div class="lg:col-span-5">
            <div class="relative mx-auto max-w-md lg:max-w-none">
              <div class="absolute -inset-1 bg-gradient-to-r from-[#f2920b] to-[#76d3f6] rounded-3xl blur-xl opacity-30"></div>
              <div class="relative bg-white p-3 sm:p-4 rounded-3xl border border-slate-200/90 shadow-xl overflow-hidden group">
                <img src="../../assets/images/savemyplay-1.jpg" alt="Save My Play {country_display}" width="800" height="800" class="w-full h-auto rounded-2xl object-cover group-hover:scale-105 transition duration-500" loading="eager" decoding="async">
                
                <div class="mt-4 p-4 rounded-2xl bg-slate-50 border border-slate-200/80">
                  <div class="grid grid-cols-2 gap-3 text-left">
                    <div>
                      <span class="text-[10px] font-heading font-black uppercase text-slate-400 tracking-wider block">{t["p1_label"]}</span>
                      <span class="text-xs sm:text-sm font-bold text-slate-900">{t["p1_val"].format(hw=hw, rec=rec, ai=ai)}</span>
                    </div>
                    <div>
                      <span class="text-[10px] font-heading font-black uppercase text-slate-400 tracking-wider block">{t["p2_label"]}</span>
                      <span class="text-xs sm:text-sm font-bold text-slate-900">{t["p2_val"].format(hw=hw, rec=rec, ai=ai)}</span>
                    </div>
                    <div>
                      <span class="text-[10px] font-heading font-black uppercase text-slate-400 tracking-wider block">{t["p3_label"]}</span>
                      <span class="text-xs sm:text-sm font-bold text-[#f2920b]">{t["p3_val"].format(hw=hw, rec=rec, ai=ai)}</span>
                    </div>
                    <div>
                      <span class="text-[10px] font-heading font-black uppercase text-slate-400 tracking-wider block">{t["p4_label"]}</span>
                      <span class="text-xs sm:text-sm font-bold text-emerald-700">{t["p4_val"].format(hw=hw, rec=rec, ai=ai)}</span>
                    </div>
                  </div>
                  <p class="mt-3 text-xs text-slate-500 border-t border-slate-200/60 pt-2 font-medium">
                    {t["quick_p"]}
                  </p>
                </div>
              </div>
            </div>
          </div>

        </div>

      </div>
    </section>

    <!-- 2. POR QUÉ ELEGIR SAVE MY PLAY (EXACTAMENTE 3 RAZONES) -->
    <section class="py-14 sm:py-20 bg-white border-b border-slate-200">
      <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center max-w-2xl mx-auto mb-10 sm:mb-14 space-y-2">
          <h2 class="font-heading font-black text-2xl sm:text-4xl text-slate-950 uppercase tracking-tight">
            {t["why_title"]}
          </h2>
          <p class="text-sm sm:text-base text-slate-600 font-medium">
            {t["why_sub"]}
          </p>
        </div>

        <div class="grid md:grid-cols-3 gap-6 sm:gap-8">
          
          <div class="bg-white rounded-3xl p-6 sm:p-8 border border-slate-200/90 shadow-sm hover:shadow-md transition">
            <div class="text-[#f2920b] flex items-center justify-start mb-4 font-black text-2xl">
              ✓
            </div>
            <h3 class="font-heading font-black text-xl sm:text-2xl text-slate-950 mb-2">{t["f1_title"]}</h3>
            <p class="text-slate-600 text-sm sm:text-base leading-relaxed">{t["f1_desc"]}</p>
          </div>

          <div class="bg-white rounded-3xl p-6 sm:p-8 border border-slate-200/90 shadow-sm hover:shadow-md transition">
            <div class="text-[#f2920b] flex items-center justify-start mb-4 font-black text-2xl">
              ✓
            </div>
            <h3 class="font-heading font-black text-xl sm:text-2xl text-slate-950 mb-2">{t["f2_title"]}</h3>
            <p class="text-slate-600 text-sm sm:text-base leading-relaxed">{t["f2_desc"].format(hw=hw, rec=rec, ai=ai)}</p>
          </div>

          <div class="bg-white rounded-3xl p-6 sm:p-8 border border-slate-200/90 shadow-sm hover:shadow-md transition">
            <div class="text-[#f2920b] flex items-center justify-start mb-4 font-black text-2xl">
              ✓
            </div>
            <h3 class="font-heading font-black text-xl sm:text-2xl text-slate-950 mb-2">{t["f3_title"]}</h3>
            <p class="text-slate-600 text-sm sm:text-base leading-relaxed">{t["f3_desc"].format(hw=hw, rec=rec, ai=ai)}</p>
          </div>

        </div>
      </div>
    </section>

    <!-- 3. TABLA DE PRECIOS EXACTA EN 3 FILAS (PUESTA INMEDIATAMENTE DESPUÉS DE POR QUÉ ELEGIR) -->
    <section id="precios" class="py-14 sm:py-20 bg-slate-50 border-b border-slate-200 scroll-mt-20">
      <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8">
        
        <div class="overflow-x-auto">
          <table class="w-full text-left text-sm sm:text-base">
            <thead>
              <tr class="border-b border-slate-200 text-xs uppercase tracking-wider text-slate-500">
                <th class="py-3 px-3">{t["pricing_th_plan"]}</th>
                <th class="py-3 px-3">{t["pricing_th_invest"]}</th>
                <th class="py-3 px-3">{t["pricing_th_mod"]}</th>
                <th class="py-3 px-3">{t["pricing_th_serv"]}</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-slate-100 font-bold">
              <tr>
                <td class="py-4 px-3 text-slate-900">{t["tbl_hw_title"]}</td>
                <td class="py-4 px-3 text-[#f2920b]">{hw}</td>
                <td class="py-4 px-3 text-slate-700">{t["tbl_hw_mod"]}</td>
                <td class="py-4 px-3 text-slate-600 text-xs font-medium">{t["tbl_hw_desc"]}</td>
              </tr>
              <tr>
                <td class="py-4 px-3 text-slate-900">{t["tbl_rec_title"]}</td>
                <td class="py-4 px-3 text-[#f2920b]">{rec}</td>
                <td class="py-4 px-3 text-emerald-600">{t["tbl_rec_mod"]}</td>
                <td class="py-4 px-3 text-slate-600 text-xs font-medium">{t["tbl_rec_desc"]}</td>
              </tr>
              <tr class="bg-amber-50/50">
                <td class="py-4 px-3 text-slate-900">{t["tbl_ai_title"]}</td>
                <td class="py-4 px-3 text-[#f2920b]">{ai}</td>
                <td class="py-4 px-3 text-slate-700">{t["tbl_ai_mod"]}</td>
                <td class="py-4 px-3 text-slate-600 text-xs font-medium">{t["tbl_ai_desc"]}</td>
              </tr>
            </tbody>
          </table>
        </div>

        <div class="mt-6 pt-5 border-t border-slate-100 flex flex-col sm:flex-row items-center justify-between gap-4">
          <span class="text-xs text-slate-500">{t["pricing_footnote"]}</span>
          <a href="{wa_url}" target="_blank" rel="noopener" class="px-6 py-3 rounded-full bg-[#f2920b] hover:bg-[#76d3f6] text-slate-950 font-heading font-black text-xs uppercase tracking-wider transition">
            {t["demo_btn"]}
          </a>
        </div>

      </div>
    </section>

    <!-- 4. DEMOSTRACIÓN EN PISTA REAL (4 VÍDEOS) -->
    <section class="py-14 sm:py-20 bg-slate-50 border-b border-slate-200">
      <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center max-w-2xl mx-auto mb-10 sm:mb-14 space-y-2">
          <span class="inline-block text-[#f2920b] font-heading font-black text-xs uppercase tracking-wider">
            {t["vid_badge"]}
          </span>
          <h2 class="font-heading font-black text-2xl sm:text-4xl text-slate-950 uppercase tracking-tight">
            {t["vid_title"]}
          </h2>
          <p class="text-sm sm:text-base text-slate-600 font-medium">
            {t["vid_sub"]}
          </p>
        </div>

        <div class="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
          <div class="bg-white rounded-2xl border border-slate-200 overflow-hidden shadow-xs hover:shadow-md transition flex flex-col">
            <div class="aspect-video bg-slate-900 relative">
              <iframe class="w-full h-full" src="https://www.youtube-nocookie.com/embed/4xwrrveDZxg?start=5623" title="{t['vid1_title']}" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy"></iframe>
            </div>
            <div class="p-4 flex-1 flex flex-col justify-between">
              <div>
                <span class="inline-block px-2 py-0.5 mb-2 rounded bg-amber-50 text-[#f2920b] font-black text-[10px] uppercase tracking-wider">{t.get("vid1_badge", "Live")}</span>
                <h3 class="font-heading font-bold text-slate-900 text-sm leading-snug">{t["vid1_title"]}</h3>
                <p class="text-xs text-slate-600 mt-1">{t["vid1_desc"]}</p>
              </div>
              <a href="https://www.youtube.com/live/4xwrrveDZxg?t=5623" target="_blank" rel="noopener" class="mt-3 inline-flex items-center gap-1.5 text-xs font-bold text-[#3478a6] hover:text-[#f2920b] transition">
                <i data-lucide="play-circle" class="w-4 h-4"></i>
                <span>{t.get("vid_btn", "YouTube")}</span>
              </a>
            </div>
          </div>

          <div class="bg-white rounded-2xl border border-slate-200 overflow-hidden shadow-xs hover:shadow-md transition flex flex-col">
            <div class="aspect-video bg-slate-900 relative">
              <iframe class="w-full h-full" src="https://www.youtube-nocookie.com/embed/LuzDvB5Umfs" title="{t['vid2_title']}" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy"></iframe>
            </div>
            <div class="p-4 flex-1 flex flex-col justify-between">
              <div>
                <span class="inline-block px-2 py-0.5 mb-2 rounded bg-amber-50 text-[#f2920b] font-black text-[10px] uppercase tracking-wider">{t.get("vid2_badge", "Demo")}</span>
                <h3 class="font-heading font-bold text-slate-900 text-sm leading-snug">{t["vid2_title"]}</h3>
                <p class="text-xs text-slate-600 mt-1">{t["vid2_desc"]}</p>
              </div>
              <a href="https://www.youtube.com/watch?v=LuzDvB5Umfs" target="_blank" rel="noopener" class="mt-3 inline-flex items-center gap-1.5 text-xs font-bold text-[#3478a6] hover:text-[#f2920b] transition">
                <i data-lucide="play-circle" class="w-4 h-4"></i>
                <span>{t.get("vid_btn", "YouTube")}</span>
              </a>
            </div>
          </div>

          <div class="bg-white rounded-2xl border border-slate-200 overflow-hidden shadow-xs hover:shadow-md transition flex flex-col">
            <div class="aspect-video bg-slate-900 relative">
              <iframe class="w-full h-full" src="https://www.youtube-nocookie.com/embed/Z0vnvyrUbPQ" title="{t['vid3_title']}" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy"></iframe>
            </div>
            <div class="p-4 flex-1 flex flex-col justify-between">
              <div>
                <span class="inline-block px-2 py-0.5 mb-2 rounded bg-amber-50 text-[#f2920b] font-black text-[10px] uppercase tracking-wider">{t.get("vid3_badge", "Clip")}</span>
                <h3 class="font-heading font-bold text-slate-900 text-sm leading-snug">{t["vid3_title"]}</h3>
                <p class="text-xs text-slate-600 mt-1">{t["vid3_desc"]}</p>
              </div>
              <a href="https://youtu.be/Z0vnvyrUbPQ" target="_blank" rel="noopener" class="mt-3 inline-flex items-center gap-1.5 text-xs font-bold text-[#3478a6] hover:text-[#f2920b] transition">
                <i data-lucide="play-circle" class="w-4 h-4"></i>
                <span>{t.get("vid_btn", "YouTube")}</span>
              </a>
            </div>
          </div>

          <div class="bg-white rounded-2xl border border-slate-200 overflow-hidden shadow-xs hover:shadow-md transition flex flex-col">
            <div class="aspect-video bg-slate-900 relative">
              <iframe class="w-full h-full" src="https://www.youtube-nocookie.com/embed/FcnCWaYahP8" title="{t['vid4_title']}" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy"></iframe>
            </div>
            <div class="p-4 flex-1 flex flex-col justify-between">
              <div>
                <span class="inline-block px-2 py-0.5 mb-2 rounded bg-amber-50 text-[#f2920b] font-black text-[10px] uppercase tracking-wider">{t.get("vid4_badge", "Coach")}</span>
                <h3 class="font-heading font-bold text-slate-900 text-sm leading-snug">{t["vid4_title"]}</h3>
                <p class="text-xs text-slate-600 mt-1">{t["vid4_desc"]}</p>
              </div>
              <a href="https://www.youtube.com/watch?v=FcnCWaYahP8" target="_blank" rel="noopener" class="mt-3 inline-flex items-center gap-1.5 text-xs font-bold text-[#3478a6] hover:text-[#f2920b] transition">
                <i data-lucide="play-circle" class="w-4 h-4"></i>
                <span>{t.get("vid_btn", "YouTube")}</span>
              </a>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 5. PREGUNTAS FRECUENTES DESPLEGABLES (<details><summary>) -->
    <section class="py-14 sm:py-20 bg-white border-b border-slate-200">
      <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center max-w-2xl mx-auto mb-10 space-y-2">
          <h2 class="font-heading font-black text-2xl sm:text-4xl text-slate-950 uppercase tracking-tight">
            {t["faq_title"]}
          </h2>
          <p class="text-sm sm:text-base text-slate-600 font-medium">
            {t["faq_sub"]}
          </p>
        </div>

        <div class="space-y-4">
          <details class="group bg-white rounded-2xl p-4 sm:p-5 border border-slate-200/90 shadow-2xs transition hover:border-[#f2920b]">
            <summary class="flex items-center justify-between font-heading font-black text-sm sm:text-base text-slate-950 cursor-pointer list-none select-none">
              <span>{t["faq1_q"]}</span>
              <span class="w-6 h-6 rounded-full bg-slate-100 text-slate-700 group-open:rotate-180 group-open:bg-[#f2920b] group-open:text-slate-950 flex items-center justify-center transition-transform text-xs shrink-0 ml-3">▼</span>
            </summary>
            <p class="mt-3 text-xs sm:text-sm text-slate-600 leading-relaxed font-normal">{t["faq1_a"]}</p>
          </details>

          <details class="group bg-white rounded-2xl p-4 sm:p-5 border border-slate-200/90 shadow-2xs transition hover:border-[#f2920b]">
            <summary class="flex items-center justify-between font-heading font-black text-sm sm:text-base text-slate-950 cursor-pointer list-none select-none">
              <span>{t["faq2_q"]}</span>
              <span class="w-6 h-6 rounded-full bg-slate-100 text-slate-700 group-open:rotate-180 group-open:bg-[#f2920b] group-open:text-slate-950 flex items-center justify-center transition-transform text-xs shrink-0 ml-3">▼</span>
            </summary>
            <p class="mt-3 text-xs sm:text-sm text-slate-600 leading-relaxed font-normal">{t["faq2_a"].format(hw=hw, rec=rec, ai=ai)}</p>
          </details>

          <details class="group bg-white rounded-2xl p-4 sm:p-5 border border-slate-200/90 shadow-2xs transition hover:border-[#f2920b]">
            <summary class="flex items-center justify-between font-heading font-black text-sm sm:text-base text-slate-950 cursor-pointer list-none select-none">
              <span>{t["faq3_q"]}</span>
              <span class="w-6 h-6 rounded-full bg-slate-100 text-slate-700 group-open:rotate-180 group-open:bg-[#f2920b] group-open:text-slate-950 flex items-center justify-center transition-transform text-xs shrink-0 ml-3">▼</span>
            </summary>
            <p class="mt-3 text-xs sm:text-sm text-slate-600 leading-relaxed font-normal">{t["faq3_a"]}</p>
          </details>

          <details class="group bg-white rounded-2xl p-4 sm:p-5 border border-slate-200/90 shadow-2xs transition hover:border-[#f2920b]">
            <summary class="flex items-center justify-between font-heading font-black text-sm sm:text-base text-slate-950 cursor-pointer list-none select-none">
              <span>{t["faq4_q"]}</span>
              <span class="w-6 h-6 rounded-full bg-slate-100 text-slate-700 group-open:rotate-180 group-open:bg-[#f2920b] group-open:text-slate-950 flex items-center justify-center transition-transform text-xs shrink-0 ml-3">▼</span>
            </summary>
            <p class="mt-3 text-xs sm:text-sm text-slate-600 leading-relaxed font-normal">{t["faq4_a"]}</p>
          </details>
        </div>
      </div>
    </section>

    <!-- 6. CONTACTO DIRECTO (WHATSAPP CON QR + EMAIL) -->
    <section id="contacto" class="py-10 sm:py-14 bg-slate-50 relative border-t border-slate-200 text-slate-900 overflow-hidden">
      <div class="max-w-4xl mx-auto px-4 sm:px-6 relative z-10 text-center">
        
        <div class="max-w-2xl mx-auto text-center mb-6">
          <span class="inline-block text-[#f2920b] text-xs font-bold uppercase tracking-wider mb-2">
            {t["contact_badge"]}
          </span>
          <h2 class="text-2xl sm:text-4xl font-black font-heading text-slate-950 uppercase tracking-tight leading-tight">
            {t["contact_title"]}
          </h2>
          <p class="text-slate-600 text-xs sm:text-sm mt-2">
            {t["contact_sub"]}
          </p>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 sm:gap-6 max-w-2xl mx-auto text-left">
          <!-- WhatsApp Card -->
          <a id="landing-contact-wa" href="{wa_url}" target="_blank" rel="noopener noreferrer"
             class="bg-white border border-slate-200 hover:border-[#25D366] rounded-2xl p-5 shadow-xs hover:shadow-lg transition-all duration-300 flex flex-col justify-between items-center text-center group cursor-pointer block no-underline text-inherit">
            <div class="flex flex-col items-center space-y-2 w-full">
              <div class="w-11 h-11 rounded-xl bg-emerald-50 text-[#25D366] flex items-center justify-center shadow-inner group-hover:scale-105 group-hover:bg-[#25D366] group-hover:text-white transition-all duration-300">
                <i data-lucide="message-circle" class="w-6 h-6 stroke-[2.2]"></i>
              </div>
              <h3 class="font-heading font-black text-base sm:text-lg text-slate-950">{t.get("contact_wa_title", "WhatsApp Directo")}</h3>
              <p class="font-mono font-bold text-xs sm:text-sm text-emerald-600 tracking-wide">+34 680 31 74 86</p>
              <div class="pt-1">
                <div class="p-1.5 bg-white border border-slate-200 rounded-xl shadow-2xs inline-block group-hover:border-emerald-300 transition">
                  <img src="../../assets/images/qr_whatsapp_coolpadel.png" alt="WhatsApp CoolPadel" width="80" height="80" class="w-16 h-16 sm:w-20 sm:h-20 object-contain" loading="lazy">
                </div>
              </div>
            </div>
            <div class="w-full pt-3 border-t border-slate-100 mt-3">
              <div class="w-full inline-flex items-center justify-center px-4 py-2 sm:py-2.5 rounded-full bg-[#25D366] group-hover:bg-[#20ba59] text-white font-sans font-black text-xs uppercase tracking-wider shadow-sm transition">
                <span>{t["contact_wa_btn"]}</span>
              </div>
            </div>
          </a>

          <!-- Email Card -->
          <a id="landing-contact-mail" href="mailto:javier@coolpadelstudios.com?subject=Consulta%20CoolPadel%20/%20Save%20my%20Play"
             class="bg-white border border-slate-200 hover:border-[#3478a6] rounded-2xl p-5 shadow-xs hover:shadow-lg transition-all duration-300 flex flex-col justify-between items-center text-center group cursor-pointer block no-underline text-inherit">
            <div class="flex flex-col items-center space-y-2 w-full">
              <div class="w-11 h-11 rounded-xl bg-sky-50 text-[#3478a6] flex items-center justify-center shadow-inner group-hover:scale-105 group-hover:bg-[#3478a6] group-hover:text-white transition-all duration-300">
                <i data-lucide="mail" class="w-6 h-6 stroke-[2.2]"></i>
              </div>
              <h3 class="font-heading font-black text-base sm:text-lg text-slate-950">{t.get("contact_mail_title", "Correo Electrónico")}</h3>
              <p class="font-sans font-bold text-xs sm:text-sm text-sky-800 tracking-normal break-all">javier@coolpadelstudios.com</p>
              <div class="pt-1">
                <div class="p-1.5 bg-white border border-slate-200 rounded-xl shadow-2xs inline-block group-hover:border-sky-300 transition">
                  <img src="../../assets/images/qr_email_coolpadel.png" alt="Email CoolPadel" width="80" height="80" class="w-16 h-16 sm:w-20 sm:h-20 object-contain" loading="lazy">
                </div>
              </div>
            </div>
            <div class="w-full pt-3 border-t border-slate-100 mt-3">
              <div class="w-full inline-flex items-center justify-center px-4 py-2 sm:py-2.5 rounded-full bg-[#3478a6] group-hover:bg-[#2c668d] text-white font-sans font-black text-xs uppercase tracking-wider shadow-sm transition">
                <span>{t["contact_mail_btn"]}</span>
              </div>
            </div>
          </a>
        </div>

      </div>
    </section>

  </main>

  <!-- 7. FOOTER TEXTURIZADO AZUL IDÉNTICO EN TODOS LOS IDIOMAS CON 4 SILOS SEO -->
  <footer class="relative z-20 bg-[#3478a6] bg-textured-blue text-white pt-14 pb-10 border-t border-sky-700/40 text-xs">
    <div class="max-w-[1700px] mx-auto px-4 sm:px-8 space-y-10">
      <div class="flex flex-col sm:flex-row items-center justify-between gap-4 pb-8 border-b border-white/20">
        <div class="flex items-center gap-3.5">
          <img src="../../assets/images/coolpadel-mascot-hd.png" alt="CoolPadel Mascota" width="60" height="60" class="h-10 sm:h-12 w-auto object-contain drop-shadow-sm" loading="lazy">
          <img src="../../assets/images/coolpadel-typography-hd.png" alt="CoolPadel" width="160" height="32" class="h-5 sm:h-6 w-auto object-contain drop-shadow-sm" loading="lazy">
        </div>
      </div>

      <nav aria-label="Estructura y Silos SEO de CoolPadel" class="grid grid-cols-2 lg:grid-cols-4 gap-8 text-left">
        <div class="space-y-3">
          <div class="font-heading font-black text-sm uppercase tracking-wider text-white">{t["footer_b2b"]}</div>
          <ul class="space-y-2 text-white/80 font-normal">
            <li><a href="{nav_prefix}llaveros-padel-personalizados/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">Llaveros de Pádel 3D</a></li>
            <li><a href="{nav_prefix}llaveros-tenis-personalizados/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">Llaveros de Tenis</a></li>
            <li><a href="{nav_prefix}welcome-packs-torneos-padel/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">Welcome Packs Torneos</a></li>
            <li><a href="{nav_prefix}llaveros-personalizados-clubs-padel/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">Merchandising Clubes</a></li>
          </ul>
        </div>

        <div class="space-y-3">
          <div class="font-heading font-black text-sm uppercase tracking-wider text-white">{t["footer_tech"]}</div>
          <ul class="space-y-2 text-white/80 font-normal">
            <li><a href="/camaras-grabacion-pistas-padel/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">Cámaras Inteligentes Pádel</a></li>
            <li><a href="{nav_prefix}save-my-play/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">Save My Play Clubes</a></li>
            <li><a href="{nav_prefix}camaras-padel-playtomic/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">Integración Playtomic</a></li>
            <li><a href="{nav_prefix}camaras-padel-matchi/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">Integración MATCHi</a></li>
          </ul>
        </div>

        <div class="space-y-3">
          <div class="font-heading font-black text-sm uppercase tracking-wider text-white">{t["footer_tools"]}</div>
          <ul class="space-y-2 text-white/80 font-normal">
            <li><a href="{nav_prefix}herramientas/calculadora-roi-camaras-padel/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">Calculadora ROI Cámaras</a></li>
            <li><a href="{nav_prefix}herramientas/calculadora-coste-pistas-padel/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">Calculadora Coste Pistas</a></li>
            <li><a href="{nav_prefix}herramientas/generador-americana-padel/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">Generador Americana</a></li>
            <li><a href="{nav_prefix}herramientas/generador-cuadros-torneo-padel/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">Generador Cuadros Torneo</a></li>
          </ul>
        </div>

        <div class="space-y-3">
          <div class="font-heading font-black text-sm uppercase tracking-wider text-white">{t["footer_corp"]}</div>
          <ul class="space-y-2 text-white/80 font-normal">
            <li><a href="{nav_prefix}blog/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">Blog & Tendencias</a></li>
            <li><a href="{nav_prefix}franquicias-padel/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">Directorio Franquicias</a></li>
            <li><a href="{nav_prefix}privacidad.html" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">Política de Privacidad</a></li>
            <li><a href="{nav_prefix}aviso-legal.html" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">Aviso Legal</a></li>
          </ul>
        </div>
      </nav>

      <div class="pt-8 border-t border-white/20 text-center space-y-2">
        <p class="text-white/70">
          © 2026 CoolPadel Studios • Save My Play — {country_display}. Todos los derechos reservados.
        </p>
      </div>
    </div>
  </footer>

  <script>
    if (typeof lucide !== 'undefined') {{
      lucide.createIcons();
    }}
  </script>
</body>
</html>
"""
    return html

def build_all():
    built = 0
    all_generated_urls = []
    
    for item in COUNTRIES_50:
        slug_local = item["slug_local"]
        slug_es = item["slug"]
        
        # 1. Generate in native local slug (e.g. /camaras/sverige/, /camaras/france/)
        dir_local = os.path.join(OUTPUT_ROOT, slug_local)
        os.makedirs(dir_local, exist_ok=True)
        html_local = generate_country_page(item, slug_local)
        with open(os.path.join(dir_local, 'index.html'), 'w', encoding='utf-8') as f:
            f.write(html_local)
        built += 1
        all_generated_urls.append(f"https://coolpadelstudios.com/camaras/{slug_local}/")
        
        # 2. If slug_es differs from slug_local (e.g. suecia vs sverige), generate Spanish slug pointing canonical to native local slug!
        if slug_es != slug_local:
            dir_es = os.path.join(OUTPUT_ROOT, slug_es)
            os.makedirs(dir_es, exist_ok=True)
            html_es = generate_country_page(item, slug_es, canonical_slug=slug_local)
            with open(os.path.join(dir_es, 'index.html'), 'w', encoding='utf-8') as f:
                f.write(html_es)
            built += 1
            all_generated_urls.append(f"https://coolpadelstudios.com/camaras/{slug_es}/")
            
        print(f"[{item['rank']}/50] OK slug: {slug_local} (lang: {item['lang']})")
        
    print(f"\nGeneradas {built} páginas de países en sus idiomas y monedas locales.")
    return all_generated_urls

if __name__ == '__main__':
    build_all()
