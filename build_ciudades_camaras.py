# -*- coding: utf-8 -*-
"""
Generador Maestro y Determinista de las 250 Landings B2B de Ciudades Mundiales de Pádel (Top 5 por País).
Estructura canónica: /camaras/{pais-slug}/{ciudad-slug}/
En el idioma nativo de cada país, con moneda local, estructura aprobada por Javier y cero coste de tokens.
"""

import os
import re
import json
import urllib.parse
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from paises_data_50 import COUNTRIES_50
from country_i18n_master import ALL_LANGS_MASTER
from ciudades_data_250 import CITIES_50
from country_i18n_extras import ISO_MAP, COURTS_TERM, NAV_PREFIX_MAP, FOOTER_I18N, CITY_TEMPLATES, BADGE_RECOMMENDED_22
from ciudades_faqs_i18n import EXTRA_FAQS_22

OUTPUT_ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'camaras')

def extract_numeric_price(price_str, fallback="45"):
    s = price_str
    if "jt" in s:
        m = re.search(r"(\d+(?:\.\d+)?)\s*jt", s)
        if m:
            return str(int(float(m.group(1)) * 1000000))
    if "rb" in s:
        m = re.search(r"(\d+(?:\.\d+)?)\s*rb", s)
        if m:
            return str(int(float(m.group(1)) * 1000))
    m_dec = re.search(r"(\d+\.\d+)\s*(?:BHD|OMR|KWD)", s)
    if m_dec:
        return m_dec.group(1)
    digits = re.sub(r"[^\d]", "", s)
    return digits if digits else fallback

def generate_city_page(country_item, city, slug_country_used, canonical_country_slug=None):
    lang = country_item["lang"]
    t = ALL_LANGS_MASTER.get(lang, ALL_LANGS_MASTER["en"])
    country_display = country_item["country_local"]
    city_name = city["name"]
    city_slug = city["slug"]
    city_courts = city.get("courts", 200)
    
    hw = country_item["hw"]
    rec = country_item["rec"]
    ai = country_item["ai"]

    badge_plan_rec = BADGE_RECOMMENDED_22.get(lang, "Recommended")

    # Localized City Title, Meta, H1, Sub & WA Message para los 22 idiomas
    c_tmpl = CITY_TEMPLATES.get(lang, CITY_TEMPLATES["en"])
    title = c_tmpl["title"].format(city=city_name, country=country_display)
    meta_desc = c_tmpl["meta_desc"].format(city=city_name, country=country_display, hw=hw, rec=rec, ai=ai)
    h1 = c_tmpl["h1"].format(city=city_name)
    sub = c_tmpl["sub"].format(city=city_name, country=country_display, courts=city_courts, hw=hw, rec=rec, ai=ai)
    wa_msg = c_tmpl["wa_msg"].format(city=city_name, country=country_display)

    if lang in ("pt", "pt-br") and country_display == "Brasil":
        title = title.replace("em Brasil", "no Brasil")
        meta_desc = meta_desc.replace("em Brasil", "no Brasil")
        sub = sub.replace("em Brasil", "no Brasil")
        wa_msg = wa_msg.replace("em Brasil", "no Brasil")

    encoded_wa = urllib.parse.quote(wa_msg)
    wa_url = f"https://api.whatsapp.com/send?phone=34680317486&text={encoded_wa}"
    target_country = canonical_country_slug if canonical_country_slug else slug_country_used
    # Mapeo canónico a Landings Hub locales dedicadas en España para evitar canibalización
    SPAIN_DEDICATED_LANDINGS = {
        "madrid": "https://coolpadelstudios.com/camaras-padel-madrid/",
        "barcelona": "https://coolpadelstudios.com/camaras-padel-barcelona/",
        "valencia": "https://coolpadelstudios.com/camaras-padel-valencia/",
        "malaga": "https://coolpadelstudios.com/camaras-padel-malaga/",
    }
    if target_country == "espana" and city_slug in SPAIN_DEDICATED_LANDINGS:
        canonical_url = SPAIN_DEDICATED_LANDINGS[city_slug]
        robots_content = "noindex, follow"
    else:
        canonical_url = f"https://coolpadelstudios.com/camaras/{target_country}/{city_slug}/"
        robots_content = "index, follow"
    country_url = f"/camaras/{target_country}/"

    redirect_js = ""

    # ISO y Hreflang Regional de la Ciudad
    iso_code = ISO_MAP.get(target_country, ISO_MAP.get(country_item["slug"], "ES"))
    regional_hreflang = f"{lang}-{iso_code}" if lang != "pt-br" else "pt-BR"

    hreflang_tags = (
        f'  <link rel="alternate" hreflang="{lang}" href="{canonical_url}"/>\n'
        f'  <link rel="alternate" hreflang="{regional_hreflang}" href="{canonical_url}"/>\n'
        f'  <link rel="alternate" hreflang="x-default" href="{canonical_url}"/>\n'
    )

    # Prefijo de navegación según hub nativo
    nav_prefix = NAV_PREFIX_MAP.get(lang, "/en/")
    dir_attr = ' dir="rtl"' if lang == "ar" else ''

    # Diccionario de footer y término de pistas localizado
    f_i18n = FOOTER_I18N.get(lang, FOOTER_I18N["en"])
    courts_word = COURTS_TERM.get(lang, "Courts")

    # Detección determinista de divisa y precios numéricos reales en la moneda declarada
    schema_curr = country_item.get("curr_code", "EUR")
    if "USD" in hw:
        schema_curr = "USD"
    elif "€" in hw:
        schema_curr = "EUR"
    elif "£" in hw:
        schema_curr = "GBP"
    schema_low_price = extract_numeric_price(rec, "45")
    schema_high_price = extract_numeric_price(hw, "180")

    faq2_a_fmt = t["faq2_a"].format(hw=hw, rec=rec, ai=ai)
    
    # FAQs adicionales de logística y propiedad con cero alucinaciones (4 semanas de entrega oficial)
    lang_extra_faq = EXTRA_FAQS_22.get(lang, EXTRA_FAQS_22["en"])
    faq5_q_fmt = lang_extra_faq["faq5_q"].format(city=city_name)
    faq5_a_fmt = lang_extra_faq["faq5_a"].format(city=city_name, hw=hw, rec=rec, ai=ai)
    faq6_q_fmt = lang_extra_faq["faq6_q"].format(city=city_name)
    faq6_a_fmt = lang_extra_faq["faq6_a"].format(city=city_name, hw=hw, rec=rec, ai=ai)

    faq_pairs = [
        (t["faq1_q"], t["faq1_a"].format(hw=hw, rec=rec, ai=ai)),
        (t["faq2_q"], faq2_a_fmt),
        (t["faq3_q"], t["faq3_a"].format(hw=hw, rec=rec, ai=ai)),
        (t["faq4_q"], t["faq4_a"].format(hw=hw, rec=rec, ai=ai)),
        (faq5_q_fmt, faq5_a_fmt),
        (faq6_q_fmt, faq6_a_fmt),
    ]
    schema_obj = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": ["Product", "Service"],
                "name": f"Save My Play - {city_name} ({country_display})",
                "inLanguage": lang,
                "description": meta_desc,
                "image": ["https://coolpadelstudios.com/assets/images/savemyplay-1.jpg"],
                "brand": {"@type": "Brand", "name": "Save My Play"},
                "areaServed": {
                    "@type": "City",
                    "name": city_name,
                    "containedInPlace": {
                        "@type": "Country",
                        "name": country_display,
                        "identifier": iso_code
                    }
                },
                "offers": {
                    "@type": "AggregateOffer",
                    "priceCurrency": schema_curr,
                    "lowPrice": schema_low_price,
                    "highPrice": schema_high_price,
                    "offerCount": "2",
                    "availability": "https://schema.org/InStock",
                },
            },
            {
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": t["nav_home"], "item": f"https://coolpadelstudios.com{nav_prefix}"},
                    {"@type": "ListItem", "position": 2, "name": t["nav_camaras"], "item": f"https://coolpadelstudios.com{nav_prefix}camaras/"},
                    {"@type": "ListItem", "position": 3, "name": country_display, "item": f"https://coolpadelstudios.com{country_url}"},
                    {"@type": "ListItem", "position": 4, "name": city_name, "item": canonical_url},
                ],
            },
            {
                "@type": "VideoObject",
                "name": f"{t['vid_badge']} - Save My Play {city_name} ({country_display})",
                "description": f"{t['vid_title']} - {t['vid_sub']}",
                "thumbnailUrl": "https://img.youtube.com/vi/4xwrrveDZxg/hqdefault.jpg",
                "uploadDate": "2026-01-15T12:00:00+01:00",
                "contentUrl": "https://www.youtube.com/watch?v=4xwrrveDZxg",
                "embedUrl": "https://www.youtube-nocookie.com/embed/4xwrrveDZxg",
                "inLanguage": lang
            },
            {
                "@type": "FAQPage",
                "@id": f"{canonical_url}#faq",
                "mainEntity": [
                    {
                        "@type": "Question",
                        "name": fq,
                        "acceptedAnswer": {"@type": "Answer", "text": fa},
                    }
                    for fq, fa in faq_pairs
                ],
            },
        ],
    }
    schema_json_str = json.dumps(schema_obj, ensure_ascii=False, indent=2)

    sibling_cities = [c for c in CITIES_50.get(country_item["slug"], []) if c["slug"] != city_slug]
    sibling_pills_html = ""
    if sibling_cities:
        pills = [
            f'<a href="{country_url}" class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full bg-slate-100 hover:bg-[#f2920b] text-slate-800 hover:text-slate-950 border border-slate-200 font-heading font-bold text-[11px] uppercase tracking-wider transition">'
            f'<span>{country_display}</span>'
            f'</a>'
        ]
        for s_city in sibling_cities:
            if target_country == "espana" and s_city['slug'] in SPAIN_DEDICATED_LANDINGS:
                s_url = f"/camaras-padel-{s_city['slug']}/"
            else:
                s_url = f"/camaras/{target_country}/{s_city['slug']}/"
            pills.append(
                f'<a href="{s_url}" class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full bg-white hover:bg-[#f2920b] text-slate-700 hover:text-slate-950 border border-slate-200 hover:border-[#f2920b] font-heading font-bold text-[11px] uppercase tracking-wider transition shadow-2xs">'
                f'<i data-lucide="map-pin" class="w-3 h-3 text-[#f2920b]"></i>'
                f'<span>{s_city["name"]}</span>'
                f'</a>'
            )
        sibling_pills_html = f'<div class="pt-2 flex flex-wrap items-center gap-1.5">{"".join(pills)}</div>'

    sibling_footer_links = "\n".join(
        f'            <li><a href="{"/camaras-padel-" + s_city["slug"] + "/" if (target_country == "espana" and s_city["slug"] in SPAIN_DEDICATED_LANDINGS) else "/camaras/" + target_country + "/" + s_city["slug"] + "/"}" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">Save My Play {s_city["name"]}</a></li>'
        for s_city in sibling_cities[:4]
    )

    html = f"""<!DOCTYPE html>
<html lang="{lang}"{dir_attr} class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{meta_desc}">
  <link rel="canonical" href="{canonical_url}">
{hreflang_tags}  <meta name="robots" content="{robots_content}">
  <link rel="alternate" type="text/markdown" href="https://coolpadelstudios.com/llms.txt" title="LLMs.txt">
  <link rel="alternate" type="text/plain" href="https://coolpadelstudios.com/llms-full.txt" title="LLMs Full Context">

  <!-- Open Graph / Social -->
  <meta property="og:type" content="product">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{meta_desc}">
  <meta property="og:url" content="{canonical_url}">
  <meta property="og:site_name" content="CoolPadel Studios · Save My Play">
  <meta property="og:image" content="https://coolpadelstudios.com/assets/images/savemyplay-1.jpg">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{meta_desc}">
  <meta name="twitter:image" content="https://coolpadelstudios.com/assets/images/savemyplay-1.jpg">

  <link rel="icon" type="image/png" href="../../../assets/images/favicon_transparente.png?v=transp3">
  <link rel="apple-touch-icon" sizes="180x180" href="../../../assets/images/favicon_transparente.png?v=transp3">
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
  {schema_json_str}
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
{redirect_js}

  <!-- HEADER -->
  <header class="fixed top-0 left-0 w-full z-50 bg-white/95 backdrop-blur-md border-b border-slate-200/80 shadow-xs">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 sm:h-20 flex items-center justify-between">
      <a href="{nav_prefix}" class="flex items-center gap-2 group">
        <img src="../../../assets/images/coolpadel-mascot-hd.png" alt="CoolPadel Mascot" width="44" height="44" class="h-8 sm:h-11 w-auto object-contain">
        <img src="../../../assets/images/coolpadel-typography-hd.png" alt="CoolPadel" width="140" height="28" class="h-5 sm:h-7 w-auto object-contain">
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
          <img src="../../../assets/images/eyes-thumb.png?v=fixed_eyes" alt="CoolPadel Eyes" width="28" height="28" style="height: 26px; max-height: 26px; width: auto;" class="object-contain group-hover:scale-110 transition duration-300">
        </a>
      </div>
    </div>
  </header>

  <main class="flex-1 pt-16 sm:pt-20">

    <!-- 1. HERO SECTION -->
    <section class="pt-5 pb-12 sm:pt-6 sm:pb-16 bg-gradient-to-b from-white via-slate-50 to-[#f8fafc] border-b border-slate-200">
      <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
        
        <!-- Breadcrumbs Navigation -->
        <nav aria-label="Breadcrumb" class="flex items-center gap-2 text-xs font-bold text-slate-500 mb-3 sm:mb-4 uppercase tracking-wider flex-wrap">
          <a href="{nav_prefix}" class="hover:text-slate-900 transition">{t["nav_home"]}</a>
          <span>/</span>
          <a href="{nav_prefix}camaras/" class="hover:text-slate-900 transition">{t["nav_camaras"]}</a>
          <span>/</span>
          <a href="{country_url}" class="hover:text-slate-900 transition">{country_display}</a>
          <span>/</span>
          <span class="text-[#f2920b] font-black">{city_name}</span>
        </nav>

        <div class="grid lg:grid-cols-12 gap-6 sm:gap-10 items-center">
          
          <div class="lg:col-span-7 space-y-3.5">
            <div class="inline-flex items-center gap-2 text-[#f2920b] font-heading font-black text-xs uppercase tracking-wider">
              <i data-lucide="award" class="w-4 h-4"></i>
              <span>{city_name} · {t["badge"]}</span>
            </div>

            <!-- H1 FORMATTED IN 3 LINES -->
            <h1 class="font-heading font-black text-2xl sm:text-3xl lg:text-[2rem] text-slate-950 uppercase tracking-tight leading-[1.15]">
              {h1}
            </h1>

            <p class="text-base sm:text-lg text-slate-600 leading-relaxed font-normal">
              {sub}
            </p>

            <div class="pt-4 flex flex-col sm:flex-row items-stretch sm:items-center gap-3 sm:gap-4 relative" style="min-height: 58px;">
              <div id="hero-btn-placeholder" style="display: none; height: 54px;" class="w-full sm:w-[350px]"></div>
              <a id="hero-wa-btn" href="{wa_url}" target="_blank" rel="noopener" class="inline-flex items-center justify-center gap-2.5 px-7 py-4 rounded-full bg-[#f2920b] hover:bg-[#76d3f6] text-slate-950 font-heading font-black text-sm uppercase tracking-wider transition-all duration-200 shadow-md hover:scale-105 active:scale-95 group z-40">
                <i data-lucide="message-circle" class="w-5 h-5 text-slate-950"></i>
                <span>{t["demo_btn"]}</span>
              </a>

              <a href="#precios" class="inline-flex items-center justify-center gap-2 px-6 py-4 rounded-full bg-white hover:bg-slate-100 text-slate-900 border border-slate-200 font-heading font-black text-sm uppercase tracking-wider transition">
                <span>{t["rates_btn"]}</span>
                <i data-lucide="arrow-down" class="w-4 h-4 text-slate-500"></i>
              </a>
            </div>
            {sibling_pills_html}
          </div>

          <div class="lg:col-span-5">
            <div class="relative mx-auto max-w-md lg:max-w-none">
              <div class="absolute -inset-1 bg-gradient-to-r from-[#f2920b] to-[#76d3f6] rounded-3xl blur-xl opacity-30"></div>
              <div class="relative bg-white p-3 sm:p-4 rounded-3xl border border-slate-200/90 shadow-xl overflow-hidden group">
                <img src="../../../assets/images/savemyplay-1.jpg" alt="Save My Play {city_name} {country_display}" width="800" height="800" class="w-full h-auto rounded-2xl object-cover group-hover:scale-105 transition duration-500" loading="eager" decoding="async">
                
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
                  <p class="mt-3 text-xs text-slate-500 border-t border-slate-200/60 pt-2.5 font-medium">
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
        <div class="text-center max-w-2xl mx-auto mb-12 sm:mb-16 space-y-2">
          <h2 class="font-heading font-black text-2xl sm:text-4xl text-slate-950 uppercase tracking-tight">
            {t["why_title"]}
          </h2>
          <p class="text-sm sm:text-base text-slate-600 font-medium">
            {t["why_sub"]}
          </p>
        </div>

        <div class="grid md:grid-cols-3 gap-6 sm:gap-8">
          <div class="p-6 sm:p-8 rounded-3xl bg-slate-50 border border-slate-200/80 shadow-xs hover:border-[#f2920b]/60 transition group flex flex-col justify-between">
            <div class="space-y-4">
              <div class="w-12 h-12 rounded-2xl bg-amber-500/10 text-[#f2920b] flex items-center justify-center font-heading font-black text-lg group-hover:scale-110 transition">
                <i data-lucide="zap" class="w-6 h-6"></i>
              </div>
              <h3 class="font-heading font-black text-lg text-slate-950 uppercase tracking-tight">
                {t["f1_title"]}
              </h3>
              <p class="text-sm text-slate-600 leading-relaxed font-normal">
                {t["f1_desc"]}
              </p>
            </div>
          </div>

          <div class="p-6 sm:p-8 rounded-3xl bg-slate-50 border border-slate-200/80 shadow-xs hover:border-[#f2920b]/60 transition group flex flex-col justify-between">
            <div class="space-y-4">
              <div class="w-12 h-12 rounded-2xl bg-sky-500/10 text-sky-600 flex items-center justify-center font-heading font-black text-lg group-hover:scale-110 transition">
                <i data-lucide="smartphone" class="w-6 h-6"></i>
              </div>
              <h3 class="font-heading font-black text-lg text-slate-950 uppercase tracking-tight">
                {t["f2_title"]}
              </h3>
              <p class="text-sm text-slate-600 leading-relaxed font-normal">
                {t["f2_desc"].format(hw=hw, rec=rec, ai=ai)}
              </p>
            </div>
          </div>

          <div class="p-6 sm:p-8 rounded-3xl bg-slate-50 border border-slate-200/80 shadow-xs hover:border-[#f2920b]/60 transition group flex flex-col justify-between">
            <div class="space-y-4">
              <div class="w-12 h-12 rounded-2xl bg-emerald-500/10 text-emerald-600 flex items-center justify-center font-heading font-black text-lg group-hover:scale-110 transition">
                <i data-lucide="shield-check" class="w-6 h-6"></i>
              </div>
              <h3 class="font-heading font-black text-lg text-slate-950 uppercase tracking-tight">
                {t["f3_title"]}
              </h3>
              <p class="text-sm text-slate-600 leading-relaxed font-normal">
                {t["f3_desc"].format(hw=hw, rec=rec, ai=ai)}
              </p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 3. TABLA DE PRECIOS EXACTA EN 3 FILAS -->
    <section id="precios" class="py-14 sm:py-20 bg-slate-50 border-b border-slate-200">
      <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center max-w-2xl mx-auto mb-10 sm:mb-14 space-y-2">
          <h2 class="font-heading font-black text-2xl sm:text-4xl text-slate-950 uppercase tracking-tight">
            {t["pricing_h2"]}
          </h2>
          <p class="text-sm sm:text-base text-slate-600 font-medium">
            {t["pricing_footnote"]}
          </p>
        </div>

        <div class="bg-white rounded-3xl border border-slate-200/90 shadow-sm overflow-hidden">
          <div class="overflow-x-auto">
            <table class="w-full text-left border-collapse">
              <thead>
                <tr class="bg-slate-100/80 border-b border-slate-200 text-[11px] sm:text-xs font-heading font-black uppercase text-slate-600 tracking-wider">
                  <th class="p-4 sm:p-5">{t["pricing_th_plan"]}</th>
                  <th class="p-4 sm:p-5">{t["pricing_th_invest"]}</th>
                  <th class="p-4 sm:p-5">{t["pricing_th_mod"]}</th>
                  <th class="p-4 sm:p-5">{t["pricing_th_serv"]}</th>
                </tr>
              </thead>
              <tbody class="divide-y divide-slate-100 text-xs sm:text-sm">
                <!-- Fila 1: Hardware en Propiedad -->
                <tr class="hover:bg-slate-50/60 transition">
                  <td class="p-4 sm:p-5 font-bold text-slate-900">
                    <div class="flex items-center gap-2">
                      <i data-lucide="hard-drive" class="w-4 h-4 text-[#f2920b]"></i>
                      <span>{t["tbl_hw_title"]}</span>
                    </div>
                  </td>
                  <td class="p-4 sm:p-5 font-heading font-black text-base text-slate-950">{hw}</td>
                  <td class="p-4 sm:p-5 text-slate-600">{t["tbl_hw_mod"]}</td>
                  <td class="p-4 sm:p-5 text-slate-600">{t["tbl_hw_desc"]}</td>
                </tr>

                <!-- Fila 2: Grabación y Highlights -->
                <tr class="bg-amber-500/5 hover:bg-amber-500/10 transition border-y-2 border-[#f2920b]/30">
                  <td class="p-4 sm:p-5 font-bold text-slate-900">
                    <div class="flex items-center gap-2">
                      <i data-lucide="video" class="w-4 h-4 text-[#f2920b]"></i>
                      <span>{t["tbl_rec_title"]}</span>
                    </div>
                    <span class="inline-block mt-1 px-2 py-0.5 rounded text-[10px] font-heading font-black uppercase bg-[#f2920b] text-slate-950">{badge_plan_rec}</span>
                  </td>
                  <td class="p-4 sm:p-5 font-heading font-black text-base text-[#f2920b]">{rec}</td>
                  <td class="p-4 sm:p-5 text-slate-600">{t["tbl_rec_mod"]}</td>
                  <td class="p-4 sm:p-5 text-slate-600">{t["tbl_rec_desc"]}</td>
                </tr>

                <!-- Fila 3: Estadísticas con IA -->
                <tr class="hover:bg-slate-50/60 transition">
                  <td class="p-4 sm:p-5 font-bold text-slate-900">
                    <div class="flex items-center gap-2">
                      <i data-lucide="sparkles" class="w-4 h-4 text-sky-600"></i>
                      <span>{t["tbl_ai_title"]}</span>
                    </div>
                  </td>
                  <td class="p-4 sm:p-5 font-heading font-black text-base text-slate-950">{ai}</td>
                  <td class="p-4 sm:p-5 text-slate-600">{t["tbl_ai_mod"]}</td>
                  <td class="p-4 sm:p-5 text-slate-600">{t["tbl_ai_desc"]}</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>

        <div class="mt-8 text-center">
          <a href="{wa_url}" target="_blank" rel="noopener" class="inline-flex items-center gap-2 px-8 py-4 rounded-full bg-[#f2920b] hover:bg-[#76d3f6] text-slate-950 font-heading font-black text-sm uppercase tracking-wider transition shadow-md hover:scale-105 active:scale-95">
            <i data-lucide="message-circle" class="w-4 h-4 text-slate-950"></i>
            <span>{f_i18n["quote_city_btn"].format(city=city_name)}</span>
          </a>
        </div>
      </div>
    </section>

    <!-- 4. DEMOSTRACIÓN EN PISTA REAL (4 VÍDEOS) -->
    <section class="py-14 sm:py-20 bg-white border-b border-slate-200">
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
              <iframe class="w-full h-full" src="https://www.youtube-nocookie.com/embed/4xwrrveDZxg?start=5623" title="{t['vid1_t']}" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy"></iframe>
            </div>
            <div class="p-4 flex-1 flex flex-col justify-between">
              <div>
                <h3 class="font-heading font-bold text-sm text-slate-900">{t["vid1_t"]}</h3>
                <p class="text-xs text-slate-500 mt-1">{t["vid1_d"]}</p>
              </div>
            </div>
          </div>

          <div class="bg-white rounded-2xl border border-slate-200 overflow-hidden shadow-xs hover:shadow-md transition flex flex-col">
            <div class="aspect-video bg-slate-900 relative">
              <iframe class="w-full h-full" src="https://www.youtube-nocookie.com/embed/LuzDvB5Umfs" title="{t['vid2_t']}" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy"></iframe>
            </div>
            <div class="p-4 flex-1 flex flex-col justify-between">
              <div>
                <h3 class="font-heading font-bold text-sm text-slate-900">{t["vid2_t"]}</h3>
                <p class="text-xs text-slate-500 mt-1">{t["vid2_d"]}</p>
              </div>
            </div>
          </div>

          <div class="bg-white rounded-2xl border border-slate-200 overflow-hidden shadow-xs hover:shadow-md transition flex flex-col">
            <div class="aspect-video bg-slate-900 relative">
              <iframe class="w-full h-full" src="https://www.youtube-nocookie.com/embed/Z0vnvyrUbPQ" title="{t['vid3_t']}" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy"></iframe>
            </div>
            <div class="p-4 flex-1 flex flex-col justify-between">
              <div>
                <h3 class="font-heading font-bold text-sm text-slate-900">{t["vid3_t"]}</h3>
                <p class="text-xs text-slate-500 mt-1">{t["vid3_d"]}</p>
              </div>
            </div>
          </div>

          <div class="bg-white rounded-2xl border border-slate-200 overflow-hidden shadow-xs hover:shadow-md transition flex flex-col">
            <div class="aspect-video bg-slate-900 relative">
              <iframe class="w-full h-full" src="https://www.youtube-nocookie.com/embed/FcnCWaYahP8" title="{t['vid4_t']}" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy"></iframe>
            </div>
            <div class="p-4 flex-1 flex flex-col justify-between">
              <div>
                <h3 class="font-heading font-bold text-sm text-slate-900">{t["vid4_t"]}</h3>
                <p class="text-xs text-slate-500 mt-1">{t["vid4_d"]}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 5. PREGUNTAS FRECUENTES DESPLEGABLES -->
    <section class="py-14 sm:py-20 bg-slate-50 border-b border-slate-200">
      <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center max-w-2xl mx-auto mb-10 sm:mb-14 space-y-2">
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
            <p class="mt-3 text-xs sm:text-sm text-slate-600 leading-relaxed font-normal">{faq2_a_fmt}</p>
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

          <details class="group bg-white rounded-2xl p-4 sm:p-5 border border-slate-200/90 shadow-2xs transition hover:border-[#f2920b]">
            <summary class="flex items-center justify-between font-heading font-black text-sm sm:text-base text-slate-950 cursor-pointer list-none select-none">
              <span>{faq5_q_fmt}</span>
              <span class="w-6 h-6 rounded-full bg-slate-100 text-slate-700 group-open:rotate-180 group-open:bg-[#f2920b] group-open:text-slate-950 flex items-center justify-center transition-transform text-xs shrink-0 ml-3">▼</span>
            </summary>
            <p class="mt-3 text-xs sm:text-sm text-slate-600 leading-relaxed font-normal">{faq5_a_fmt}</p>
          </details>

          <details class="group bg-white rounded-2xl p-4 sm:p-5 border border-slate-200/90 shadow-2xs transition hover:border-[#f2920b]">
            <summary class="flex items-center justify-between font-heading font-black text-sm sm:text-base text-slate-950 cursor-pointer list-none select-none">
              <span>{faq6_q_fmt}</span>
              <span class="w-6 h-6 rounded-full bg-slate-100 text-slate-700 group-open:rotate-180 group-open:bg-[#f2920b] group-open:text-slate-950 flex items-center justify-center transition-transform text-xs shrink-0 ml-3">▼</span>
            </summary>
            <p class="mt-3 text-xs sm:text-sm text-slate-600 leading-relaxed font-normal">{faq6_a_fmt}</p>
          </details>
        </div>
      </div>
    </section>

    <!-- 6. CONTACTO DIRECTO (WHATSAPP CON QR + EMAIL) -->
    <section id="contacto" class="py-10 sm:py-14 bg-white relative border-t border-slate-200 text-slate-900 overflow-hidden">
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
             class="bg-white border border-slate-200 hover:border-[#25D366] rounded-2xl p-5 shadow-xs hover:shadow-lg transition-all duration-300 flex flex-col justify-between items-center text-center group cursor-pointer">
            <div class="flex flex-col items-center">
              <div class="w-12 h-12 rounded-xl bg-emerald-50 text-[#25D366] flex items-center justify-center mb-3 group-hover:scale-110 transition-transform">
                <i data-lucide="message-circle" class="w-6 h-6"></i>
              </div>
              <h3 class="font-heading font-black text-slate-950 text-base mb-1">{f_i18n["wa_direct_title"]}</h3>
              <p class="text-slate-500 text-xs mb-3">{f_i18n["wa_direct_sub"]}</p>
            </div>
            <span class="inline-flex items-center justify-center gap-1.5 w-full py-2.5 px-4 rounded-xl bg-[#25D366] text-white font-heading font-bold text-xs uppercase tracking-wider group-hover:bg-[#1ebd59] transition-colors shadow-xs">
              <i data-lucide="message-circle" class="w-3.5 h-3.5"></i>
              <span>{t["contact_wa_btn"]}</span>
            </span>
          </a>

          <!-- Email Card -->
          <a id="landing-contact-email" href="mailto:javier@coolpadelstudios.com?subject=Save%20My%20Play%20Club%20{city_name}"
             class="bg-white border border-slate-200 hover:border-sky-500 rounded-2xl p-5 shadow-xs hover:shadow-lg transition-all duration-300 flex flex-col justify-between items-center text-center group cursor-pointer">
            <div class="flex flex-col items-center">
              <div class="w-12 h-12 rounded-xl bg-sky-50 text-sky-600 flex items-center justify-center mb-3 group-hover:scale-110 transition-transform">
                <i data-lucide="mail" class="w-6 h-6"></i>
              </div>
              <h3 class="font-heading font-black text-slate-950 text-base mb-1">{f_i18n["email_dossier_title"]}</h3>
              <p class="text-slate-500 text-xs mb-3">javier@coolpadelstudios.com</p>
            </div>
            <span class="inline-flex items-center justify-center gap-1.5 w-full py-2.5 px-4 rounded-xl bg-sky-600 text-white font-heading font-bold text-xs uppercase tracking-wider group-hover:bg-sky-500 transition-colors shadow-xs">
              <i data-lucide="send" class="w-3.5 h-3.5"></i>
              <span>{t["contact_mail_btn"]}</span>
            </span>
          </a>
        </div>
      </div>
    </section>

  </main>

  <!-- 7. FOOTER TEXTURIZADO AZUL IDÉNTICO -->
  <footer class="relative z-20 bg-[#3478a6] bg-textured-blue text-white pt-14 pb-10 border-t border-sky-700/40 text-xs">
    <div class="max-w-[1700px] mx-auto px-4 sm:px-8 space-y-10">
      <div class="flex flex-col sm:flex-row items-center justify-between gap-4 pb-8 border-b border-white/20">
        <div class="flex items-center gap-3.5">
          <img src="../../../assets/images/coolpadel-mascot-hd.png" alt="CoolPadel Mascota" width="60" height="60" class="h-10 sm:h-12 w-auto object-contain drop-shadow-sm" loading="lazy">
          <img src="../../../assets/images/coolpadel-typography-hd.png" alt="CoolPadel" width="160" height="32" class="h-5 sm:h-6 w-auto object-contain drop-shadow-sm" loading="lazy">
        </div>
      </div>

      <nav aria-label="CoolPadel Navigation" class="grid grid-cols-2 lg:grid-cols-4 gap-8 text-left">
        <div class="space-y-3">
          <div class="font-heading font-black text-sm uppercase tracking-wider text-white">{t["footer_b2b"]}</div>
          <ul class="space-y-2 text-white/80 font-normal">
            <li><a href="{nav_prefix}llaveros-padel-personalizados/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">{f_i18n["llaveros_3d"]}</a></li>
            <li><a href="{nav_prefix}llaveros-tenis-personalizados/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">{f_i18n["llaveros_tenis"]}</a></li>
            <li><a href="{nav_prefix}welcome-packs-torneos-padel/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">{f_i18n["welcome_packs"]}</a></li>
            <li><a href="{nav_prefix}llaveros-personalizados-clubs-padel/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">{f_i18n["merch_clubs"]}</a></li>
          </ul>
        </div>

        <div class="space-y-3">
          <div class="font-heading font-black text-sm uppercase tracking-wider text-white">{t["footer_tech"]}</div>
          <ul class="space-y-2 text-white/80 font-normal">
            <li><a href="{nav_prefix}camaras/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">{f_i18n["camaras_hub"]}</a></li>
            <li><a href="{country_url}" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">{f_i18n["camaras_country"].format(country=country_display)}</a></li>
            <li><a href="{nav_prefix}camaras-grabacion-pistas-padel/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">{f_i18n["grabacion_streaming"]}</a></li>
            <li><a href="{nav_prefix}camaras/articulos/cuanto-cuesta-poner-camaras/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">{f_i18n["tarifas_precios"]}</a></li>
          </ul>
        </div>

        <div class="space-y-3">
          <div class="font-heading font-black text-sm uppercase tracking-wider text-white">{t["footer_tools"]}</div>
          <ul class="space-y-2 text-white/80 font-normal">
            <li><a href="{nav_prefix}herramientas/calculadora-coste-pistas-padel/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">{f_i18n["calc_cost"]}</a></li>
            <li><a href="{nav_prefix}herramientas/calculadora-roi-camaras-padel/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">{f_i18n["calc_roi"]}</a></li>
            <li><a href="{nav_prefix}herramientas/generador-cuadros-torneo-padel/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">{f_i18n["gen_cuadros"]}</a></li>
            <li><a href="{nav_prefix}franquicias-padel/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">{f_i18n["cadenas_clubs"]}</a></li>
          </ul>
        </div>

        <div class="space-y-3">
          <div class="font-heading font-black text-sm uppercase tracking-wider text-white">{country_display} &amp; {t["footer_corp"]}</div>
          <ul class="space-y-2 text-white/80 font-normal">
{sibling_footer_links}
            <li><a href="{nav_prefix}blog/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">{f_i18n["blog_oficial"]}</a></li>
            <li><a href="/politica-de-devoluciones.html" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">{f_i18n["politica_dev"]}</a></li>
          </ul>
        </div>
      </nav>

      <div class="pt-8 border-t border-white/20 flex flex-col sm:flex-row items-center justify-between gap-4 text-white/70">
        <p>© 2026 CoolPadel Studios · {f_i18n["distribuidor_oficial"].format(city=city_name, country=country_display)}</p>
        <p class="text-right">{f_i18n["propiedad_tagline"]}</p>
      </div>
    </div>
  </footer>

  <script>
    if (window.lucide) {{
      lucide.createIcons();
    }}

    // Mantener el MISMO boton en la misma posicion de la pantalla al hacer scroll
    (function() {{
      var heroBtn = document.getElementById('hero-wa-btn');
      var placeholder = document.getElementById('hero-btn-placeholder');
      if (!heroBtn || !placeholder) return;

      var initialLeft = null;
      var initialTop = null;
      var initialWidth = null;
      var initialHeight = null;
      var isFixed = false;
      var ticking = false;

      function updateInitialMetrics() {{
        if (!isFixed) {{
          var rect = heroBtn.getBoundingClientRect();
          initialLeft = rect.left;
          initialTop = rect.top;
          initialWidth = rect.width;
          initialHeight = rect.height;
        }}
      }}

      window.addEventListener('resize', function() {{
        if (isFixed) {{
          heroBtn.style.position = '';
          heroBtn.style.top = '';
          heroBtn.style.left = '';
          heroBtn.style.width = '';
          heroBtn.style.maxWidth = '';
          placeholder.style.display = 'none';
          isFixed = false;
        }}
        updateInitialMetrics();
        onScroll();
      }});

      function onScroll() {{
        if (initialTop === null) {{
          updateInitialMetrics();
        }}

        var anchor = isFixed ? placeholder : heroBtn;
        var anchorRect = anchor.getBoundingClientRect();

        if (anchorRect.top <= initialTop) {{
          if (!isFixed) {{
            isFixed = true;
            placeholder.style.width = initialWidth + 'px';
            placeholder.style.height = initialHeight + 'px';
            placeholder.style.display = 'block';

            heroBtn.style.position = 'fixed';
            heroBtn.style.top = initialTop + 'px';
            heroBtn.style.left = initialLeft + 'px';
            heroBtn.style.width = initialWidth + 'px';
            heroBtn.style.margin = '0';
            heroBtn.classList.add('shadow-xl');
          }}
        }} else {{
          if (isFixed) {{
            isFixed = false;
            heroBtn.style.position = '';
            heroBtn.style.top = '';
            heroBtn.style.left = '';
            heroBtn.style.width = '';
            heroBtn.style.margin = '';
            heroBtn.classList.remove('shadow-xl');
            placeholder.style.display = 'none';
          }}
        }}
        ticking = false;
      }}

      window.addEventListener('scroll', function() {{
        if (!ticking) {{
          window.requestAnimationFrame(onScroll);
          ticking = true;
        }}
      }}, {{ passive: true }});

      setTimeout(function() {{
        updateInitialMetrics();
        onScroll();
      }}, 100);
    }})();
  </script>
  <script src="/assets/js/cp-analytics.js?v=20261114b" defer></script>
</body>
</html>
"""
    return html

def build_all_cities():
    built = 0
    generated_city_urls = []
    
    country_map = {c['slug']: c for c in COUNTRIES_50}
    
    for country_slug, cities in CITIES_50.items():
        country_item = country_map.get(country_slug)
        if not country_item:
            continue
            
        slug_local = country_item["slug_local"]
        slug_es = country_item["slug"]
        
        for city in cities:
            # Generar EXCLUSIVAMENTE en el slug local nativo del país: /camaras/{slug_local}/{city_slug}/
            dir_city_local = os.path.join(OUTPUT_ROOT, slug_local, city["slug"])
            os.makedirs(dir_city_local, exist_ok=True)
            html_city = generate_city_page(country_item, city, slug_local)
            with open(os.path.join(dir_city_local, 'index.html'), 'w', encoding='utf-8') as f:
                f.write(html_city)
            built += 1
            generated_city_urls.append(f"https://coolpadelstudios.com/camaras/{slug_local}/{city['slug']}/")

        print(f"OK [5 Ciudades] -> {country_slug} ({slug_local})")

    print(f"\n¡Éxito! Generadas {built} páginas de ciudades B2B para los 50 países.")
    return generated_city_urls

if __name__ == '__main__':
    build_all_cities()
