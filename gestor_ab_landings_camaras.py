# -*- coding: utf-8 -*-
"""
Gestor Maestro y Automatizado de Test A/B para las 300 Landings B2B de Cámaras (50 Países y 250 Ciudades).

Variante A: Control clásico (Hero estándar blanco/gris con tarjeta 2x2 en columna derecha, sin rectángulos ni artículos en cabecera).
Variante B: Variante Asunción (Hero con textura azul y texto blanco + Subtítulo Cámara Nº1 USA + Botón WhatsApp Demo + Pills estilizadas + Foto limpia con ribbon badge oficial + 4 Rectángulos azules de estadísticas + 3 Artículos destacados 16:9 + Moneda local en envío + CTAs WhatsApp "Solicitar Demo 15 min").
"""

import os
import re
import json
import random
import argparse
import sys
from pathlib import Path

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_ROOT = os.path.join(BASE_DIR, 'camaras')
MAP_FILE = os.path.join(BASE_DIR, 'camaras_ab_variant_map.json')

sys.path.append(BASE_DIR)
from paises_data_50 import COUNTRIES_50
from ciudades_data_250 import CITIES_50
from country_i18n_extras import ISO_MAP
from country_i18n_dict_full import ALL_LANGS_I18N
from camaras_i18n_ab import (
    SHIPPING_MAP, STAT_CARDS_I18N, AWARD_BADGE_I18N, ARTICLES_I18N,
    DEMO_BTN_TEXT, TARIFS_BTN_TEXT, SUBTITLE_I18N, H1_TEMPLATES_I18N,
    PRICING_SUBTITLE_I18N, ASUNCION_CSS_BLOCK
)

def get_country_lookup():
    by_slug = {}
    for c in COUNTRIES_50:
        by_slug[c["slug"]] = c
        by_slug[c["slug_local"]] = c
    return by_slug

def scan_all_market_pages():
    """Escanea y clasifica todas las 300 páginas de países y ciudades."""
    country_map = get_country_lookup()
    pages = []
    
    # 50 Países
    for c in COUNTRIES_50:
        slug = c["slug_local"]
        html_path = os.path.join(OUTPUT_ROOT, slug, 'index.html')
        if os.path.exists(html_path):
            pages.append({
                "type": "country",
                "rel_path": f"{slug}/index.html",
                "country_slug": slug,
                "city_slug": None,
                "country_data": c,
                "target_name": c.get("country_local", c.get("country_es")),
                "lang": c.get("lang", "es"),
                "iso": ISO_MAP.get(slug, "ES")
            })
            
    # 250 Ciudades
    for country_slug, cities in CITIES_50.items():
        c = country_map.get(country_slug)
        if not c:
            continue
        slug_local = c["slug_local"]
        for city in cities:
            city_slug = city["slug"]
            html_path = os.path.join(OUTPUT_ROOT, slug_local, city_slug, 'index.html')
            if os.path.exists(html_path):
                pages.append({
                    "type": "city",
                    "rel_path": f"{slug_local}/{city_slug}/index.html",
                    "country_slug": slug_local,
                    "city_slug": city_slug,
                    "country_data": c,
                    "target_name": city["name"],
                    "lang": c.get("lang", "es"),
                    "iso": ISO_MAP.get(slug_local, "ES")
                })
                
    return pages

def generate_or_load_ab_split(pages, seed=42):
    """Carga o genera una partición determinista exactamente al 50/50 (Variante A vs Variante B)."""
    if os.path.exists(MAP_FILE):
        try:
            with open(MAP_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)
                assignments = data.get("pages", {})
                if (assignments.keys() == {p["rel_path"] for p in pages}
                        and list(assignments.values()).count("A") == 150
                        and list(assignments.values()).count("B") == 150
                        and assignments.get("paraguay/asuncion/index.html") == "B"):
                    return data
        except Exception:
            pass

    rng = random.Random(seed)
    
    countries = [p for p in pages if p["type"] == "country"]
    cities = [p for p in pages if p["type"] == "city"]
    
    # Asunción debe estar siempre en Variante B
    asuncion_page = next((p for p in cities if p["rel_path"] == "paraguay/asuncion/index.html"), None)
    other_cities = [p for p in cities if p["rel_path"] != "paraguay/asuncion/index.html"]
    
    rng.shuffle(countries)
    rng.shuffle(other_cities)
    
    half_country = len(countries) // 2
    total_cities_b = len(cities) // 2
    
    variant_map = {}
    
    # Países: 25 A y 25 B
    for i, p in enumerate(countries):
        variant = "B" if i < half_country else "A"
        variant_map[p["rel_path"]] = variant
        
    # Asunción en B
    if asuncion_page:
        variant_map[asuncion_page["rel_path"]] = "B"
        
    # Resto de ciudades: asignar hasta completar total_cities_b en B
    b_count_cities = 1 if asuncion_page else 0
    for p in other_cities:
        if b_count_cities < total_cities_b:
            variant_map[p["rel_path"]] = "B"
            b_count_cities += 1
        else:
            variant_map[p["rel_path"]] = "A"

    result = {
        "seed": seed,
        "total_pages": len(pages),
        "count_a": sum(1 for v in variant_map.values() if v == "A"),
        "count_b": sum(1 for v in variant_map.values() if v == "B"),
        "pages": variant_map
    }
    
    with open(MAP_FILE, 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
        
    return result

def build_variant_b_sections(p):
    """Construye los bloques HTML específicos de la Variante Asunción adaptados al país, idioma y moneda."""
    lang = p["lang"]
    c = p["country_data"]
    iso = p["iso"]
    target_name = p["target_name"]
    
    hw = c["hw"]
    rec = c["rec"]
    ai = c["ai"]
    
    stat_t = STAT_CARDS_I18N.get(lang, STAT_CARDS_I18N["en"])
    art_t = ARTICLES_I18N.get(lang, ARTICLES_I18N["en"])
    award_text = AWARD_BADGE_I18N.get(lang, AWARD_BADGE_I18N["en"])
    
    c1_val = stat_t["c1_val"].format(rec=rec)
    c2_val = stat_t["c2_val"].format(hw=hw)
    c3_val = stat_t["c3_val"]
    c4_val = stat_t["c4_val"]
    
    # 1. Las 4 tarjetas de estadísticas con textura azul
    stats_html = f"""    <!-- Resumen Clave (4 Tarjetas con textura azul sobre fondo blanco sin reborde naranja - Variante Asunción) -->
    <section class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 hero-stats-section relative z-20">
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 sm:gap-6">
        <div class="hero-stat-card rounded-2xl p-3.5 sm:p-4 shadow-xl flex flex-col justify-center h-[88px] overflow-hidden">
          <span class="text-[10px] sm:text-[11px] font-bold text-slate-100/90 uppercase tracking-wider block leading-tight">{stat_t['c1_lbl']}</span>
          <span class="text-xs sm:text-sm font-black font-heading text-white mt-1 block leading-tight">{c1_val}</span>
        </div>
        <div class="hero-stat-card rounded-2xl p-3.5 sm:p-4 shadow-xl flex flex-col justify-center h-[88px] overflow-hidden">
          <span class="text-[10px] sm:text-[11px] font-bold text-slate-100/90 uppercase tracking-wider block leading-tight">{stat_t['c2_lbl']}</span>
          <span class="text-xs sm:text-sm font-black font-heading text-white mt-1 block leading-tight">{c2_val}</span>
        </div>
        <div class="hero-stat-card rounded-2xl p-3.5 sm:p-4 shadow-xl flex flex-col justify-center h-[88px] overflow-hidden">
          <span class="text-[10px] sm:text-[11px] font-bold text-slate-100/90 uppercase tracking-wider block leading-tight">{stat_t['c3_lbl']}</span>
          <span class="text-xs sm:text-sm font-black font-heading text-white mt-1 block leading-tight">{c3_val}</span>
        </div>
        <div class="hero-stat-card rounded-2xl p-3.5 sm:p-4 shadow-xl flex flex-col justify-center h-[88px] overflow-hidden">
          <span class="text-[10px] sm:text-[11px] font-bold text-slate-100/90 uppercase tracking-wider block leading-tight">{stat_t['c4_lbl']}</span>
          <span class="text-xs sm:text-sm font-black font-heading text-white mt-1 block leading-tight">{c4_val}</span>
        </div>
      </div>
    </section>"""

    # 2. Los 3 artículos destacados 16:9
    articles_html = f"""    <!-- 3 Artículos Destacados de Cámaras para Clubs (Variante Asunción) -->
    <section class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 mb-12 sm:mb-16">
      <div class="hero-featured-articles">
        
        <!-- Artículo 1 -->
        <a href="/camaras/articulos/por-donde-empezar-si-estoy-pensando-en-poner-camaras/" class="article-card group">
          <div>
            <div class="article-thumb-wrap">
              <img src="/assets/images/camaras/camera-01.jpg" alt="{art_t['art1_title']}" width="800" height="450" loading="lazy" decoding="async">
            </div>
            <h3 class="article-card-title">
              {art_t['art1_title']}
            </h3>
          </div>
          <div class="article-card-footer">
            <div class="card-action">
              <span>{art_t['read_btn']}</span>
              <div class="action-icon">
                <i data-lucide="arrow-right"></i>
              </div>
            </div>
          </div>
        </a>

        <!-- Artículo 2 -->
        <a href="/camaras/articulos/errores-clubs-se-arrepienten-de-poner-camaras/" class="article-card group">
          <div>
            <div class="article-thumb-wrap">
              <img src="/assets/images/camaras/retransmision-directo-marcador-youtube.png" alt="{art_t['art2_title']}" width="800" height="450" loading="lazy" decoding="async">
            </div>
            <h3 class="article-card-title">
              {art_t['art2_title']}
            </h3>
          </div>
          <div class="article-card-footer">
            <div class="card-action">
              <span>{art_t['read_btn']}</span>
              <div class="action-icon">
                <i data-lucide="arrow-right"></i>
              </div>
            </div>
          </div>
        </a>

        <!-- Artículo 3 -->
        <a href="/camaras/articulos/por-que-no-recomiendo-plan-analytics/" class="article-card group">
          <div>
            <div class="article-thumb-wrap">
              <img src="/assets/images/camaras/portada-mapa-calor-analytics.png" alt="{art_t['art3_title']}" width="800" height="450" loading="lazy" decoding="async">
            </div>
            <h3 class="article-card-title">
              {art_t['art3_title']}
            </h3>
          </div>
          <div class="article-card-footer">
            <div class="card-action">
              <span>{art_t['read_btn']}</span>
              <div class="action-icon">
                <i data-lucide="arrow-right"></i>
              </div>
            </div>
          </div>
        </a>

      </div>
    </section>"""

    # 3. Columna derecha limpia (foto + ribbon badge oficial con 28px de holgura)
    hero_right_col = f"""          <div class="lg:col-span-5">
            <div class="relative rounded-3xl overflow-hidden border border-white/20 shadow-2xl bg-slate-900/40 group max-w-md mx-auto lg:max-w-none">
              <picture>
                <source srcset="/assets/images/savemyplay_photos/1.webp" type="image/webp">
                <img src="/assets/images/savemyplay_photos/1.jpg" alt="Save My Play {target_name}" width="1920" height="1080" class="w-full h-auto object-cover group-hover:scale-105 transition-transform duration-500 shadow-inner" loading="eager" decoding="async">
              </picture>
            </div>
            <div class="hero-award-badge flex flex-row items-center justify-center gap-1.5 sm:gap-2 text-[#f2920b] font-heading font-black text-xs sm:text-sm uppercase tracking-wider text-center flex-nowrap whitespace-nowrap" style="margin-top: 28px !important;">
              <i data-lucide="award" class="w-4 h-4 text-[#f2920b] shrink-0"></i>
              <span class="whitespace-nowrap">{award_text}</span>
            </div>
          </div>"""

    shipping_str = SHIPPING_MAP.get(iso, "+20 € envío int.")
    demo_btn_str = DEMO_BTN_TEXT.get(lang, DEMO_BTN_TEXT["en"])
    tarifs_btn_str = TARIFS_BTN_TEXT.get(lang, TARIFS_BTN_TEXT["en"])
    sub_data = SUBTITLE_I18N.get(lang, SUBTITLE_I18N["en"])
    h1_template = H1_TEMPLATES_I18N.get(lang, H1_TEMPLATES_I18N["en"])
    h1_formatted = h1_template.format(target=target_name)
    pricing_sub_str = PRICING_SUBTITLE_I18N.get(lang, PRICING_SUBTITLE_I18N["en"])

    # 4. Sección 2: ¿Por qué elegir Save My Play? (3 tarjetas blancas con ✓ naranja, adaptado a idioma y moneda)
    lang_data = ALL_LANGS_I18N.get(lang)
    if not lang_data and lang == "pt-br":
        lang_data = ALL_LANGS_I18N.get("pt")
    if not lang_data:
        lang_data = ALL_LANGS_I18N.get("en", ALL_LANGS_I18N["es"])

    why_title = lang_data.get("why_title", "¿Por qué elegir Save My Play para tu club?")
    why_sub = lang_data.get("why_sub", "La tecnología de grabación y analítica en pista más ágil, sin obras ni costes ocultos")
    f1_title = lang_data.get("f1_title", "No son cámaras de vigilancia: máxima calidad de imagen")
    f1_desc = lang_data.get("f1_desc", "Diseñadas exclusivamente para pádel y tenis. Grabación nítida deportiva, gran angular sin deformar la pista y retransmisión directa sin cortes.")
    f2_title = lang_data.get("f2_title", "Planes mensuales por pista")
    f2_desc = lang_data.get("f2_desc", "Grabación de partidos, highlights y directos por {rec}. Estadísticas con IA por {ai} que incluyen análisis completo de tu juego.")
    f2_desc = f2_desc.replace("{rec}", rec).replace("{ai}", ai)
    f3_title = lang_data.get("f3_title", "Fácil de usar y sin obras")
    f3_desc = lang_data.get("f3_desc", "Inversión hardware de {hw} en propiedad. Se instala en 5 minutos en el poste de la red o iluminación, y sin permanencias.")
    f3_desc = f3_desc.replace("{hw}", hw)

    sec2_html = f"""    <!-- 2. POR QUÉ ELEGIR SAVE MY PLAY (EXACTAMENTE 3 RAZONES) -->
    <section class="pt-8 pb-14 sm:pt-10 sm:pb-20 bg-white border-b border-slate-200">
      <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center max-w-2xl mx-auto mb-10 sm:mb-14 space-y-2">
          <h2 class="font-heading font-black text-2xl sm:text-4xl text-slate-950 uppercase tracking-tight">
            {why_title}
          </h2>
          <p class="text-sm sm:text-base text-slate-600 font-medium">
            {why_sub}
          </p>
        </div>

        <div class="grid md:grid-cols-3 gap-6 sm:gap-8">
          
          <div class="bg-white rounded-3xl p-6 sm:p-8 border border-slate-200/90 shadow-sm hover:shadow-md transition">
            <div class="text-[#f2920b] flex items-center justify-start mb-4 font-black text-2xl">
              ✓
            </div>
            <h3 class="font-heading font-black text-xl sm:text-2xl text-slate-950 mb-2">{f1_title}</h3>
            <p class="text-slate-600 text-sm sm:text-base leading-relaxed">{f1_desc}</p>
          </div>

          <div class="bg-white rounded-3xl p-6 sm:p-8 border border-slate-200/90 shadow-sm hover:shadow-md transition">
            <div class="text-[#f2920b] flex items-center justify-start mb-4 font-black text-2xl">
              ✓
            </div>
            <h3 class="font-heading font-black text-xl sm:text-2xl text-slate-950 mb-2">{f2_title}</h3>
            <p class="text-slate-600 text-sm sm:text-base leading-relaxed">{f2_desc}</p>
          </div>

          <div class="bg-white rounded-3xl p-6 sm:p-8 border border-slate-200/90 shadow-sm hover:shadow-md transition">
            <div class="text-[#f2920b] flex items-center justify-start mb-4 font-black text-2xl">
              ✓
            </div>
            <h3 class="font-heading font-black text-xl sm:text-2xl text-slate-950 mb-2">{f3_title}</h3>
            <p class="text-slate-600 text-sm sm:text-base leading-relaxed">{f3_desc}</p>
          </div>

        </div>
      </div>
    </section>"""

    return {
        "stats_html": stats_html,
        "articles_html": articles_html,
        "hero_right_col": hero_right_col,
        "sec2_html": sec2_html,
        "shipping_str": shipping_str,
        "demo_btn_str": demo_btn_str,
        "tarifs_btn_str": tarifs_btn_str,
        "sub_data": sub_data,
        "h1_formatted": h1_formatted,
        "pricing_sub_str": pricing_sub_str
    }

def apply_variant_b_to_html(html, p):
    """Inyecta todos los componentes visuales y textuales de la Variante Asunción adaptados al mercado."""
    b_data = build_variant_b_sections(p)
    body_idx = html.find("<body")
    if body_idx == -1:
        body_idx = 0

    # 0. Header Container max-w-6xl (idéntico a Asunción)
    html = re.sub(
        r'(<header[^>]*>\s*<div class=")[^"]*max-w-7xl([^"]*")',
        r'\g<1>max-w-6xl\g<2>',
        html
    )

    # 1. Inyectar / actualizar CSS en <style>
    if "/* --- REGLAS ASUNCIÓN (VARIANTE B) --- */" not in html:
        style_idx = html.find("</style>")
        if style_idx != -1:
            html = html[:style_idx] + ASUNCION_CSS_BLOCK + "\n  " + html[style_idx:]
    else:
        if ".camera-local-hero" not in html:
            html = re.sub(r'/\* --- REGLAS ASUNCIÓN \(VARIANTE B\) --- \*/[\s\S]*?(?=</style>)', ASUNCION_CSS_BLOCK.strip(), html)

    # 2. Hero Section tag (fondo azul texturado)
    html = re.sub(
        r'<section class="pt-5 pb-12 sm:pt-6 sm:pb-16 bg-gradient-to-b from-white via-slate-50 to-\[#f8fafc\] border-b border-slate-200">',
        '<section class="camera-local-hero relative text-white pt-6 pb-10 sm:pt-8 sm:pb-12 lg:pt-8 lg:pb-14">',
        html
    )

    # 3. Breadcrumb navigation
    html = re.sub(
        r'<nav aria-label="Breadcrumb" class="[^"]*">',
        '<nav aria-label="Breadcrumb" class="hero-breadcrumb flex items-center gap-2 text-xs font-bold text-white/70 mb-8 sm:mb-12 lg:mb-14 uppercase tracking-wider flex-wrap">',
        html
    )
    breadcrumb_m = re.search(r'<nav aria-label="Breadcrumb"[\s\S]*?</nav>', html)
    if breadcrumb_m:
        bc_old = breadcrumb_m.group(0)
        bc_new = bc_old.replace('hover:text-slate-900', 'hover:text-white').replace('text-slate-500', 'text-white/70')
        html = html[:breadcrumb_m.start()] + bc_new + html[breadcrumb_m.end():]

    # 4. H1 Formatted en 4 líneas
    h1_new = f'<h1 class="hero-main-title font-heading font-black text-xl sm:text-2xl lg:text-3xl text-white uppercase tracking-tight leading-snug">\n              {b_data["h1_formatted"]}\n            </h1>'
    html = re.sub(r'<h1 class="[^"]*">[\s\S]*?</h1>', h1_new, html, count=1)

    # 5. Subtítulo en 3 líneas (Cámara Nº1 USA)
    sub = b_data["sub_data"]
    sub_new = f'<p class="hero-main-subtitle text-slate-100/95 leading-relaxed font-normal max-w-2xl">\n              {sub["l1"]}<br class="hidden sm:inline">\n              {sub["l2"]}<br class="hidden sm:inline">\n              {sub["l3"]}\n            </p>'
    html = re.sub(r'(</h1>\s*)<p class="[^"]*leading-relaxed[^"]*">[\s\S]*?</p>', rf'\g<1>{sub_new}', html, count=1)

    # 6. Botones de cabecera (Solicitar Demo WhatsApp + Ver Tarifas)
    hero_btn_m = re.search(r'<div class="pt-4 flex flex-col sm:flex-row[^"]*" style="min-height: 58px;">[\s\S]*?</a>\s*</div>', html)
    if hero_btn_m:
        demo_btn_str = b_data["demo_btn_str"]
        tarifs_btn_str = b_data["tarifs_btn_str"]
        wa_href_m = re.search(r'href="(https://api\.whatsapp\.com/send\?[^"]*)"', hero_btn_m.group(0))
        wa_href = wa_href_m.group(1) if wa_href_m else "https://api.whatsapp.com/send?phone=34680317486"
        btn_new = f'''<div class="flex flex-row items-center gap-3 sm:gap-4 hero-btn-row relative" style="min-height: 54px;">
              <div id="hero-btn-placeholder" style="display: none; height: 50px;" class="w-full sm:w-[320px]"></div>
              <a id="hero-wa-btn" data-product="camaras" data-lead-intent="demo" data-button-position="hero" href="{wa_href}" target="_blank" rel="noopener" class="inline-flex items-center justify-center gap-2.5 px-6 py-3.5 sm:px-7 sm:py-3.5 rounded-full bg-[#f2920b] hover:bg-[#e08508] text-slate-950 font-heading font-black text-xs sm:text-sm uppercase tracking-wider transition-all duration-200 shadow-xl hover:scale-105 active:scale-95 group z-40">
                <i data-lucide="message-circle" class="w-4 h-4 sm:w-5 sm:h-5 text-slate-950"></i>
                <span>{demo_btn_str}</span>
              </a>

              <a href="#precios" class="inline-flex items-center justify-center gap-2 px-5 py-3.5 sm:px-6 sm:py-3.5 rounded-full bg-white hover:bg-slate-100 text-slate-900 border border-slate-200 font-heading font-black text-xs sm:text-sm uppercase tracking-wider transition shadow-md hover:scale-105">
                <span>{tarifs_btn_str}</span>
                <i data-lucide="arrow-down" class="w-4 h-4 text-slate-600"></i>
              </a>
            </div>'''
        html = html[:hero_btn_m.start()] + btn_new + html[hero_btn_m.end():]
    else:
        # Asegurar textos y atributos si ya fue transformado
        html = re.sub(
            r'(<a id="hero-wa-btn"[^>]*>[\s\S]*?<span>).*?(</span>)',
            rf'\g<1>{b_data["demo_btn_str"]}\g<2>',
            html
        )

    # 7. Pills de ciudades
    html = re.sub(
        r'<div class="pt-2 flex flex-wrap items-center gap-1.5">',
        '<div class="flex flex-row items-center gap-1.5 sm:gap-2 flex-nowrap hero-cities-row">',
        html
    )
    pills_m = re.search(r'<div class="[^"]*hero-cities-row">[\s\S]*?</div>', html)
    if pills_m:
        pills_old = pills_m.group(0)
        pills_new = re.sub(
            r'class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full[^"]*"',
            'class="hero-city-pill inline-flex items-center gap-1 px-2.5 py-1.5 rounded-full bg-white/95 hover:bg-[#f2920b] text-slate-800 hover:text-slate-950 border border-white/80 font-heading font-bold text-[10px] sm:text-[11px] uppercase tracking-wider transition shadow-sm shrink-0 whitespace-nowrap"',
            pills_old
        )
        html = html[:pills_m.start()] + pills_new + html[pills_m.end():]

    # 8. Columna derecha limpia (foto + ribbon badge con 28px de holgura)
    if "grid grid-cols-2 gap-3 text-left" in html:
        col_match = re.search(r'<div class="lg:col-span-5">[\s\S]*?</div>\s*</div>\s*</div>\s*</div>', html)
        if col_match:
            html = html[:col_match.start()] + b_data["hero_right_col"] + html[col_match.end():]
        else:
            col_match_flex = re.search(r'<div class="lg:col-span-5">[\s\S]*?</div>\s*</div>\s*</div>', html)
            if col_match_flex:
                html = html[:col_match_flex.start()] + b_data["hero_right_col"] + html[col_match_flex.end():]

    if "hero-award-badge" in html:
        html = re.sub(
            r'class="hero-award-badge[^"]*"(?:\s*style="[^"]*")?',
            'class="hero-award-badge flex flex-row items-center justify-center gap-1.5 sm:gap-2 text-[#f2920b] font-heading font-black text-xs sm:text-sm uppercase tracking-wider text-center flex-nowrap whitespace-nowrap" style="margin-top: 28px !important;"',
            html
        )

    # 9. Inyectar los 4 rectángulos y los 3 artículos entre Hero y Sección 2
    body_content = html[body_idx:]
    if 'class="hero-stat-card' not in body_content:
        sec2_match = re.search(r'(</section>\s*)(<!--\s*2\.)', html)
        if sec2_match:
            insert_content = f"\n\n{b_data['stats_html']}\n\n{b_data['articles_html']}\n\n    "
            html = html[:sec2_match.start(1)] + "</section>" + insert_content + html[sec2_match.start(2):]

    # 10. Reemplazar Sección 2 antigua por la de Asunción (3 tarjetas blancas con ✓ naranja)
    sec2_regex = r'[ \t]*<!--\s*2\.[^>]*?-->\s*<section[^>]*>[\s\S]*?</section>\s*(?=<!--\s*3\.\s*TABLA DE PRECIOS)'
    html = re.sub(sec2_regex, f'{b_data["sec2_html"]}\n\n    ', html)

    # 11. Sección 3 (Precios): scroll-mt-20, subtítulo limpio, divisa de envío y botón Demo
    html = re.sub(
        r'<section id="precios" class="py-14 sm:py-20 bg-slate-50 border-b border-slate-200(?:\s+scroll-mt-20)?"',
        '<section id="precios" class="py-14 sm:py-20 bg-slate-50 border-b border-slate-200 scroll-mt-20"',
        html
    )
    html = re.sub(
        r'(<section id="precios"[\s\S]*?<h2[^>]*>[\s\S]*?</h2>\s*)<p class="text-sm[^"]*">[\s\S]*?</p>',
        rf'\g<1><p class="text-sm sm:text-base text-slate-600 font-medium">\n            {b_data["pricing_sub_str"]}\n          </p>',
        html,
        count=1
    )

    # Envío internacional en divisa local
    html = re.sub(
        r'\(\+[^)]*?(?:envío|shipping|livr|sped|versand|livrare|dostawa|frakt|fragt|toimitus|verzending|envio|kargo|pos|送料)[^)]*?\)',
        f"({b_data['shipping_str']})",
        html,
        flags=re.IGNORECASE
    )

    # Botón demo en pricing bajo la tabla
    btn_m = re.search(r'(<section id="precios"[\s\S]*?<div class="mt-8 text-center">\s*)<a [^>]*href="([^"]+)"[^>]*>[\s\S]*?</a>(\s*</div>)', html)
    if btn_m:
        wa_price_url = btn_m.group(2)
        btn_replacement = f'''{btn_m.group(1)}<a data-product="camaras" data-lead-intent="demo" data-button-position="pricing" href="{wa_price_url}" target="_blank" rel="noopener" class="inline-flex items-center gap-2 px-8 py-4 rounded-full bg-[#f2920b] hover:bg-[#76d3f6] text-slate-950 font-heading font-black text-sm uppercase tracking-wider transition shadow-md hover:scale-105 active:scale-95">
            <i data-lucide="message-circle" class="w-4 h-4 text-slate-950"></i>
            <span>{b_data["demo_btn_str"]}</span>
          </a>{btn_m.group(3)}'''
        html = html[:btn_m.start()] + btn_replacement + html[btn_m.end():]

    # 12. Sección 5 (FAQs): fondo blanco bg-white idéntico a Asunción
    html = re.sub(
        r'(<!--\s*5\.\s*PREGUNTAS FRECUENTES[^\n]*\s*)<section class="py-14 sm:py-20 bg-slate-50 border-b border-slate-200">',
        r'\g<1><section class="py-14 sm:py-20 bg-white border-b border-slate-200">',
        html
    )

    return html

def remove_variant_b_from_html(html):
    """Restaura la estructura limpia de Variante A (Control)."""
    html = re.sub(r'<!-- Resumen Clave[\s\S]*?hero-stats-section[\s\S]*?</section>\s*', '', html)
    html = re.sub(r'<!-- 3 Artículos Destacados[\s\S]*?hero-featured-articles[\s\S]*?</section>\s*', '', html)
    return html

def apply_all_variants():
    pages = scan_all_market_pages()
    if len(pages) != 300:
        raise ValueError(f"Se esperaban 300 landings de cámaras, hay {len(pages)}.")
    split = generate_or_load_ab_split(pages)
    variant_map = split["pages"]
    
    modified_b = 0
    checked_a = 0
    
    for p in pages:
        rel = p["rel_path"]
        variant = variant_map.get(rel, "A")
        full_path = os.path.join(OUTPUT_ROOT, rel)
        
        with open(full_path, 'r', encoding='utf-8') as f:
            original = f.read()
            
        if variant == "B":
            if rel == "paraguay/asuncion/index.html":
                continue
            updated = apply_variant_b_to_html(original, p)
            if updated != original:
                with open(full_path, 'w', encoding='utf-8') as f:
                    f.write(updated)
                modified_b += 1
        else:
            body_idx = original.find("<body")
            body_content = original[body_idx:] if body_idx != -1 else original
            if "hero-stats-section" in body_content or "hero-featured-articles" in body_content:
                updated = remove_variant_b_from_html(original)
                with open(full_path, 'w', encoding='utf-8') as f:
                    f.write(updated)
            checked_a += 1

    print(f"\n[A/B Manager] Éxito:")
    print(f" - Total Páginas analizadas: {len(pages)}")
    print(f" - Variante A (Control Clásico): {split['count_a']} páginas")
    print(f" - Variante B (Asunción Nueva): {split['count_b']} páginas ({modified_b} actualizadas/verificadas)")
    return split

def audit_all_pages():
    """Ejecuta una auditoría estructural y técnica exhaustiva sobre las 300 páginas (Variante A y B)."""
    pages = scan_all_market_pages()
    if len(pages) != 300:
        print(f"Se esperaban 300 landings de cámaras, hay {len(pages)}.")
        return False
    split = generate_or_load_ab_split(pages)
    variant_map = split["pages"]

    errors_by_page = {}
    count_b = 0
    count_a = 0

    for p in pages:
        rel = p["rel_path"]
        variant = variant_map.get(rel, "A")
        if variant == "B":
            count_b += 1
        else:
            count_a += 1

        fpath = os.path.join(OUTPUT_ROOT, rel)
        with open(fpath, "r", encoding="utf-8") as f:
            html = f.read()

        errs = []

        # 1. Chequeos transversales
        if '<meta http-equiv="refresh" content="0;' in html:
            errs.append("La landing redirige y no muestra su variante")
        if "G-3FY3DTNN21" not in html:
            errs.append("Falta GA4")
        if "q7p8g52y9e" not in html:
            errs.append("Falta Clarity")
        if "application/ld+json" not in html:
            errs.append("Falta Schema.org JSON-LD")
        if "phone=34680317486" not in html:
            errs.append("Falta o teléfono erróneo en WhatsApp (+34 680 31 74 86)")

        if variant == "B":
            # 2. Header
            if "max-w-7xl" in html[:html.find("</header>")]:
                errs.append("Header tiene max-w-7xl en lugar de max-w-6xl")
            if "max-w-6xl" not in html[:html.find("</header>")]:
                errs.append("Header no tiene max-w-6xl")

            # 3. Hero
            if "camera-local-hero" not in html:
                errs.append("Hero sin textura azul .camera-local-hero")
            if "hero-breadcrumb" not in html:
                errs.append("Hero sin hero-breadcrumb")
            if "hero-main-title" not in html:
                errs.append("Hero sin hero-main-title")
            if "hero-main-subtitle" not in html:
                errs.append("Hero sin hero-main-subtitle")
            if "hero-btn-row" not in html:
                errs.append("Hero sin hero-btn-row")
            if "hero-city-pill" not in html:
                errs.append("Hero sin hero-city-pill")
            if "hero-award-badge" not in html:
                errs.append("Hero sin hero-award-badge")
            if "margin-top: 28px !important;" not in html:
                errs.append("hero-award-badge sin margen 28px")

            # 4. Rectángulos de estadísticas
            if "hero-stats-section" not in html:
                errs.append("Falta sección hero-stats-section")
            if html.count("hero-stat-card") < 4:
                errs.append(f"Se esperaban 4 hero-stat-card, hay {html.count('hero-stat-card')}")

            # 5. Artículos destacados
            if "hero-featured-articles" not in html:
                errs.append("Falta sección hero-featured-articles")
            if html.count('class="article-card') < 3:
                errs.append(f"Se esperaban 3 article-card, hay {html.count('class=\"article-card')}")

            # 6. Sección 2: 3 tarjetas blancas con ✓ naranja
            if "pt-8 pb-14 sm:pt-10 sm:pb-20 bg-white border-b border-slate-200" not in html:
                errs.append("Sección 2 sin padding canónico pt-8 pb-14...")
            sec2_m = re.search(r'<!--\s*2\.[^>]*?-->\s*<section[^>]*>([\s\S]*?)</section>', html)
            if sec2_m:
                sec2_content = sec2_m.group(1)
                for bad_icon in ['data-lucide="zap"', 'data-lucide="smartphone"', 'data-lucide="shield-check"']:
                    if bad_icon in sec2_content:
                        errs.append(f"Sección 2 contiene icono obsoleto {bad_icon}")
                if "bg-slate-50" in sec2_content:
                    errs.append("Sección 2 contiene tarjetas grises bg-slate-50")
            if html.count("text-[#f2920b] flex items-center justify-start mb-4 font-black text-2xl") < 3:
                errs.append("Sección 2 sin los 3 checks naranjas ✓")

            # 7. Sección 3 (Precios)
            precios_m = re.search(r'<section id="precios"[^>]*>([\s\S]*?)</section>', html)
            if not precios_m:
                errs.append("Falta sección precios")
            else:
                p_content = precios_m.group(0)
                if "scroll-mt-20" not in p_content:
                    errs.append("Precios sin scroll-mt-20")
                if "* Precios sin IVA" in p_content:
                    errs.append("Precios contiene texto antiguo '* Precios sin IVA'")
                if 'data-button-position="pricing"' not in p_content:
                    errs.append("Botón precios sin data-button-position='pricing'")
                if "Pedir presupuesto" in p_content:
                    errs.append("Botón precios con texto antiguo 'Pedir presupuesto'")

            # 8. Sección 5 (FAQs)
            faq_m = re.search(r'<!--\s*5\.\s*PREGUNTAS FRECUENTES[^\n]*\s*<section class="([^"]*)"', html)
            if faq_m:
                faq_class = faq_m.group(1)
                if "bg-slate-50" in faq_class:
                    errs.append(f"FAQs con fondo gris bg-slate-50 en vez de bg-white")

            # 9. Placeholders sin resolver
            if "{rec}" in html or "{hw}" in html or "{ai}" in html:
                errs.append("Variables sin formatear {rec}, {hw} o {ai}")

        else: # Variante A (Control)
            if "hero-stats-section" in html:
                errs.append("Variante A contiene hero-stats-section")
            if "hero-featured-articles" in html:
                errs.append("Variante A contiene hero-featured-articles")
            if "camera-local-hero" in html:
                errs.append("Variante A contiene camera-local-hero")

        if errs:
            errors_by_page[rel] = errs

    print(f"\n==========================================")
    print(f"       AUDITORÍA MAESTRA A/B LANDINGS      ")
    print(f"==========================================")
    print(f"Total páginas auditadas: {len(pages)}")
    print(f" - Variante B (Asunción): {count_b}")
    print(f" - Variante A (Control):  {count_a}")
    print(f"Páginas con discrepancias: {len(errors_by_page)}")
    
    if errors_by_page:
        print("\n[FALLO] Discrepancias encontradas:")
        for rel, errs in list(errors_by_page.items())[:15]:
            print(f"  ❌ {rel}: {errs}")
        return False
    else:
        print("\n✅ [ÉXITO TOTAL] Las 300 páginas cumplen al 100% el contrato estructural y técnico.")
        return True

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Gestor de Test A/B de Landings de Cámaras")
    parser.add_argument("--status", action="store_true", help="Mostrar distribución actual")
    parser.add_argument("--apply", action="store_true", help="Aplicar división A/B a todas las landings")
    parser.add_argument("--audit", action="store_true", help="Auditar al 100% todas las 300 landings contra el contrato")
    args = parser.parse_args()
    
    pages = scan_all_market_pages()
    split = generate_or_load_ab_split(pages)
    
    if args.status:
        print(f"Total páginas: {len(pages)}")
        print(f"Variante A (Control): {split['count_a']}")
        print(f"Variante B (Asunción): {split['count_b']}")
        sample_b = [k for k, v in split["pages"].items() if v == "B"][:10]
        print("Muestra Variante B:", sample_b)
    elif args.audit:
        success = audit_all_pages()
        sys.exit(0 if success else 1)
    elif args.apply or len(sys.argv) == 1:
        apply_all_variants()
