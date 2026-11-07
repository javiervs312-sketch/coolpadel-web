# -*- coding: utf-8 -*-
"""
Generador Maestro y Determinista de las 50 Landings B2B de Países de Pádel.
Cumple rigurosamente todos los requerimientos de Javier:
1. Generación en el idioma nativo de cada uno de los 50 países.
2. Slug en el nombre del país en su idioma nativo (ej: /camaras/sverige/, /camaras/france/, /camaras/deutschland/, etc.)
   y compatibilidad con slug en español.
3. Precios y planes en su moneda local y equivalencia en euros/dólares.
4. Sección '¿Por qué elegir Save My Play para tu club?' con exactamente las 3 razones:
   - 1) No son cámaras de vigilancia: máxima calidad de imagen deportiva
   - 2) Planes mensuales claros por pista (grabación 45 €/mes, estadísticas IA 136 €/mes)
   - 3) Fácil de usar y sin obras (180 € hardware en propiedad, 5 min montaje)
5. H1 exacto en 3 líneas limpias.
6. Cero menciones a 'pulsador' ni 'zanjas'.
7. Enlaces de navegación con fallback a /en/ si no es ES.
"""

import os
import re
import urllib.parse
from paises_data_50 import COUNTRIES_50
from country_i18n_dict_full import ALL_LANGS_I18N

OUTPUT_ROOT = 'coolpadel-web/camaras'
os.makedirs(OUTPUT_ROOT, exist_ok=True)

def generate_country_page(item, slug_to_use):
    lang = item["lang"]
    t = ALL_LANGS_I18N.get(lang, ALL_LANGS_I18N["en"])
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
    canonical_url = f"https://coolpadelstudios.com/camaras/{slug_to_use}/"
    
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
      "priceCurrency": "{item.get('curr_symbol', 'EUR')}",
      "lowPrice": "45",
      "highPrice": "180",
      "offerCount": "2",
      "availability": "https://schema.org/InStock"
    }}
  }}
  </script>
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
        <a href="{nav_prefix}herramientas/" class="hidden sm:inline-block font-heading font-black text-xs uppercase tracking-wider text-slate-700 hover:text-[#f2920b] transition">{t["nav_calc"]}</a>
        <a href="{nav_prefix}blog/" class="hidden sm:inline-block font-heading font-black text-xs uppercase tracking-wider text-slate-700 hover:text-[#f2920b] transition">{t["nav_blog"]}</a>

        <a href="{wa_url}" target="_blank" rel="noopener" class="inline-flex items-center gap-2 px-4 py-2 sm:px-5 sm:py-2.5 rounded-full bg-[#f2920b] hover:bg-[#76d3f6] text-slate-950 font-heading font-black text-xs sm:text-sm uppercase tracking-wider transition shadow-sm hover:scale-105 active:scale-95">
          <i data-lucide="message-circle" class="w-4 h-4 text-slate-950"></i>
          <span>WhatsApp Demo</span>
        </a>
      </div>
    </div>
  </header>

  <main class="flex-1 pt-20">

    <!-- HERO SECTION -->
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

    <!-- 3 RAZONES / POR QUÉ ELEGIR SAVE MY PLAY -->
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

    <!-- TABLA DE PRECIOS TRANSPARENTES -->
    <section id="precios" class="py-14 sm:py-20 bg-slate-50 border-b border-slate-200 scroll-mt-20">
      <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="overflow-x-auto">
          <table class="w-full text-left text-sm sm:text-base">
            <thead>
              <tr class="border-b border-slate-200 text-xs uppercase tracking-wider text-slate-500">
                <th class="py-3 px-3">{t["pricing_h2"]}</th>
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
              <tr>
                <td class="py-4 px-3 text-slate-900">{t["tbl_ai_title"]}</td>
                <td class="py-4 px-3 text-[#f2920b]">{ai}</td>
                <td class="py-4 px-3 text-slate-700">{t["tbl_ai_mod"]}</td>
                <td class="py-4 px-3 text-slate-600 text-xs font-medium">{t["tbl_ai_desc"]}</td>
              </tr>
            </tbody>
          </table>
        </div>

        <div class="mt-8 text-center">
          <a href="{wa_url}" target="_blank" rel="noopener" class="inline-flex items-center justify-center gap-2.5 px-8 py-4 rounded-full bg-[#f2920b] hover:bg-[#76d3f6] text-slate-950 font-heading font-black text-sm uppercase tracking-wider transition shadow-md hover:scale-105 active:scale-95">
            <i data-lucide="message-circle" class="w-5 h-5 text-slate-950"></i>
            <span>{t["demo_btn"]}</span>
          </a>
        </div>
      </div>
    </section>

    <!-- PREGUNTAS FRECUENTES -->
    <section class="py-14 sm:py-20 bg-white border-b border-slate-200">
      <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center max-w-2xl mx-auto mb-10 space-y-2">
          <h2 class="font-heading font-black text-2xl sm:text-4xl text-slate-950 uppercase tracking-tight">
            {t["faq_h2"]}
          </h2>
        </div>

        <div class="space-y-4">
          <div class="bg-slate-50 rounded-2xl p-6 border border-slate-200">
            <h3 class="font-heading font-black text-base sm:text-lg text-slate-950 mb-2">{t["faq1_q"]}</h3>
            <p class="text-slate-600 text-sm leading-relaxed">{t["faq1_a"]}</p>
          </div>

          <div class="bg-slate-50 rounded-2xl p-6 border border-slate-200">
            <h3 class="font-heading font-black text-base sm:text-lg text-slate-950 mb-2">{t["faq2_q"]}</h3>
            <p class="text-slate-600 text-sm leading-relaxed">{t["faq2_a"].format(hw=hw, rec=rec, ai=ai)}</p>
          </div>

          <div class="bg-slate-50 rounded-2xl p-6 border border-slate-200">
            <h3 class="font-heading font-black text-base sm:text-lg text-slate-950 mb-2">{t["faq3_q"]}</h3>
            <p class="text-slate-600 text-sm leading-relaxed">{t["faq3_a"]}</p>
          </div>
        </div>
      </div>
    </section>

  </main>

  <!-- FOOTER -->
  <footer class="bg-slate-950 text-white py-12 border-t border-slate-800">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center space-y-4">
      <p class="text-xs text-slate-500">
        © 2026 CoolPadel Studios • Save My Play — {country_display}. All rights reserved.
      </p>
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
        
        # 2. If slug_es differs from slug_local (e.g. suecia vs sverige), generate both so both URLs work!
        if slug_es != slug_local:
            dir_es = os.path.join(OUTPUT_ROOT, slug_es)
            os.makedirs(dir_es, exist_ok=True)
            html_es = generate_country_page(item, slug_es)
            with open(os.path.join(dir_es, 'index.html'), 'w', encoding='utf-8') as f:
                f.write(html_es)
            built += 1
            all_generated_urls.append(f"https://coolpadelstudios.com/camaras/{slug_es}/")
            
        print(f"[{item['rank']}/50] OK slug: {slug_local} (lang: {item['lang']})")
        
    print(f"\nGeneradas {built} páginas de países en sus idiomas y monedas locales.")
    return all_generated_urls

if __name__ == '__main__':
    build_all()
