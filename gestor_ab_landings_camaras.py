# -*- coding: utf-8 -*-
"""
Gestor Maestro y Automatizado de Test A/B para las 300 Landings B2B de Cámaras (50 Países y 250 Ciudades).

Variante A: Control clásico (Hero estándar con tarjeta 2x2 en columna derecha, sin rectángulos ni artículos en cabecera).
Variante B: Variante Asunción (Foto limpia con badge oficial + 4 Rectángulos azules de estadísticas + 3 Artículos destacados 16:9 + Moneda local en envío + CTAs WhatsApp "Solicitar Demo 15 min").
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
from camaras_i18n_ab import (
    SHIPPING_MAP, STAT_CARDS_I18N, AWARD_BADGE_I18N, ARTICLES_I18N,
    DEMO_BTN_TEXT, ASUNCION_CSS_BLOCK
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
                if len(data.get("pages", {})) == len(pages):
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

    return {
        "stats_html": stats_html,
        "articles_html": articles_html,
        "hero_right_col": hero_right_col,
        "shipping_str": shipping_str,
        "demo_btn_str": demo_btn_str
    }

def apply_variant_b_to_html(html, p):
    """Inyecta los bloques de la Variante Asunción adaptados a la página respetando estructura e idempotencia."""
    b_data = build_variant_b_sections(p)
    body_idx = html.find("<body")
    if body_idx == -1:
        body_idx = 0

    # 1. Inyectar CSS en <style> si no existe
    if "/* --- REGLAS ASUNCIÓN (VARIANTE B) --- */" not in html:
        style_idx = html.find("</style>")
        if style_idx != -1:
            html = html[:style_idx] + ASUNCION_CSS_BLOCK + "\n  " + html[style_idx:]

    # 2. Reemplazar la columna derecha del hero por la estructura limpia (foto + ribbon badge)
    # Detectamos <div class="lg:col-span-5">... y reemplazamos hasta el cierre de esa columna
    if "grid grid-cols-2 gap-3 text-left" in html:
        # Columna clásica con caja de 4 precios duplicada
        pattern = r'(<div class="lg:col-span-5">[\s\S]*?</div>\s*</div>\s*</div>)'
        # Reemplazamos la columna completa
        col_match = re.search(r'<div class="lg:col-span-5">[\s\S]*?</div>\s*</div>\s*</div>\s*</div>', html)
        if col_match:
            html = html[:col_match.start()] + b_data["hero_right_col"] + html[col_match.end():]
        else:
            # Búsqueda más flexible del bloque lg:col-span-5
            col_match_flex = re.search(r'<div class="lg:col-span-5">[\s\S]*?</div>\s*</div>\s*</div>', html)
            if col_match_flex:
                html = html[:col_match_flex.start()] + b_data["hero_right_col"] + html[col_match_flex.end():]

    # Asegurar que el hero-award-badge tiene el margen superior de 28px si ya estuviera
    if "hero-award-badge" in html:
        html = re.sub(
            r'class="hero-award-badge[^"]*"(?:\s*style="[^"]*")?',
            'class="hero-award-badge flex flex-row items-center justify-center gap-1.5 sm:gap-2 text-[#f2920b] font-heading font-black text-xs sm:text-sm uppercase tracking-wider text-center flex-nowrap whitespace-nowrap" style="margin-top: 28px !important;"',
            html
        )

    # 3. Inyectar los 4 rectángulos y los 3 artículos entre Hero y Sección 2 (inspeccionando dentro de <body>)
    body_content = html[body_idx:]
    if 'class="hero-stat-card' not in body_content:
        sec2_match = re.search(r'(</section>\s*)(<!--\s*2\.)', html)
        if sec2_match:
            insert_content = f"\n\n{b_data['stats_html']}\n\n{b_data['articles_html']}\n\n    "
            html = html[:sec2_match.start(1)] + "</section>" + insert_content + html[sec2_match.start(2):]

    # 4. Sustituir el envío internacional genérico en euros por la divisa local exacta
    html = re.sub(
        r'\(\+[^)]*?(?:envío|shipping|livr|sped|versand|livrare|dostawa|frakt|fragt|toimitus|verzending|envio|kargo|pos|送料)[^)]*?\)',
        f"({b_data['shipping_str']})",
        html,
        flags=re.IGNORECASE
    )

    # 5. Botón de demostración bajo tabla de precios ("pricing") y en cabecera si procede
    html = re.sub(
        r'(data-button-position="pricing"[^>]*>[\s\S]*?<span>).*?(</span>)',
        rf'\g<1>{b_data["demo_btn_str"]}\g<2>',
        html
    )

    return html

def remove_variant_b_from_html(html):
    """Restaura la estructura limpia de Variante A (Control)."""
    # Eliminar bloque de 4 rectangulitos
    html = re.sub(r'<!-- Resumen Clave[\s\S]*?hero-stats-section[\s\S]*?</section>\s*', '', html)
    # Eliminar bloque de 3 artículos
    html = re.sub(r'<!-- 3 Artículos Destacados[\s\S]*?hero-featured-articles[\s\S]*?</section>\s*', '', html)
    return html

def apply_all_variants():
    pages = scan_all_market_pages()
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
            # Asunción es el modelo canónico de referencia
            if rel == "paraguay/asuncion/index.html":
                continue
            updated = apply_variant_b_to_html(original, p)
            if updated != original:
                with open(full_path, 'w', encoding='utf-8') as f:
                    f.write(updated)
                modified_b += 1
        else:
            # Variante A: asegurar que no tiene bloques residuales de B
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

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Gestor de Test A/B de Landings de Cámaras")
    parser.add_argument("--status", action="store_true", help="Mostrar distribución actual")
    parser.add_argument("--apply", action="store_true", help="Aplicar división A/B a todas las landings")
    args = parser.parse_args()
    
    pages = scan_all_market_pages()
    split = generate_or_load_ab_split(pages)
    
    if args.status:
        print(f"Total páginas: {len(pages)}")
        print(f"Variante A (Control): {split['count_a']}")
        print(f"Variante B (Asunción): {split['count_b']}")
        sample_b = [k for k, v in split["pages"].items() if v == "B"][:10]
        print("Muestra Variante B:", sample_b)
    elif args.apply or len(sys.argv) == 1:
        apply_all_variants()
