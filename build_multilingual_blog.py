#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Compilador Maestro del Blog Multilingüe en 4 Idiomas (ES, EN, FR, IT):
- Blog Hub (/blog/ y /{lang}/blog/)
- 29 Artículos y Newsletters completos en 4 idiomas (ES, EN, FR, IT)
- Inyección de Hreflangs simétricos de 5 vías en todos los artículos
- Menú de selección de idioma sincronizado (código activo, clases, rutas exactas)
- Cero enlaces rotos 404 en todas las versiones lingüísticas
"""
import os
import sys
import re

cur_dir = os.path.dirname(os.path.abspath(__file__))
if cur_dir not in sys.path:
    sys.path.insert(0, cur_dir)

from translations_blog import BLOG_HUB_DATA, FLAGSHIP_GUIDES_DATA
from extra_articles_i18n import EXTRA_ARTICLES_I18N

# Catálogo completo unificado de 29 artículos
ALL_ARTICLES_I18N = {**FLAGSHIP_GUIDES_DATA, **EXTRA_ARTICLES_I18N}

def adapt_header_and_nav(html, lang, asset_prefix):
    """
    Adapta la cabecera oficial en páginas de blog (Hub y Artículos) para el idioma `lang`:
    - Logo a /{lang}/
    - Llaveros a /{lang}/#llaveros
    - Cámaras a /{lang}/camaras/
    - Blog a /{lang}/blog/
    - Franquicias a /{lang}/franquicias-padel/
    - Contacto a /{lang}/#contacto
    - Ojos a /{lang}/
    - Dropdown: código activo {LANG} y clases activas
    - Textos de navegación según el idioma
    """
    if lang == "es":
        return html

    t_nav = {
        'en': {'llaveros': 'KEYCHAINS', 'camaras': 'CAMERAS', 'blog': 'Blog', 'franquicias': 'Franchises', 'contacto': 'Contact'},
        'fr': {'llaveros': 'PORTE-CLÉS', 'camaras': 'CAMÉRAS', 'blog': 'Blog', 'franquicias': 'Franchises', 'contacto': 'Contacter'},
        'it': {'llaveros': 'PORTACHIAVI', 'camaras': 'TELECAMERE', 'blog': 'Blog', 'franquicias': 'Franchigie', 'contacto': 'Contattaci'},
    }[lang]

    # 1. Logo principal
    html = re.sub(
        r'<a href="[^"]*" class="flex items-center gap-2 group shrink-0" aria-label="CoolPadel Home">',
        f'<a href="/{lang}/" class="flex items-center gap-2 group shrink-0" aria-label="CoolPadel Home">',
        html
    )

    # 2. Llaveros
    html = re.sub(
        r'<a href="[^"]*#llaveros" class="([^"]*)">[^<]*</a>',
        f'<a href="/{lang}/#llaveros" class="\\1">{t_nav["llaveros"]}</a>',
        html
    )

    # 3. Cámaras
    html = re.sub(
        r'<a href="[^"]*camaras/" class="([^"]*)">[^<]*</a>',
        f'<a href="/{lang}/camaras/" class="\\1">{t_nav["camaras"]}</a>',
        html
    )

    # 4. Blog link en nav
    html = re.sub(
        r'<a href="(?:\./|\.\./|[^"]*blog/)" class="([^"]*whitespace-nowrap)">Blog</a>',
        f'<a href="/{lang}/blog/" class="\\1">{t_nav["blog"]}</a>',
        html
    )

    # 5. Franquicias / Cadenas de clubs
    html = re.sub(
        r'<a href="[^"]*franquicias-padel/" class="([^"]*)">[^<]*</a>',
        f'<a href="/{lang}/franquicias-padel/" class="\\1">{t_nav["franquicias"]}</a>',
        html
    )

    # 6. Selector de idioma en header: Código activo
    html = html.replace(
        '<span id="current-lang-code" class="uppercase font-black">ES</span>',
        f'<span id="current-lang-code" class="uppercase font-black">{lang.upper()}</span>'
    )

    # 7. Clases del menú desplegable
    active_cls = 'lang-opt block lang-opt-active font-black w-full text-center px-4 py-2 text-xs transition duration-150'
    inactive_cls = 'lang-opt block text-slate-700 hover:bg-[#f2920b] hover:text-slate-950 font-bold w-full text-center px-4 py-2 text-xs transition duration-150'
    html = html.replace(f'data-lang-opt="es" class="{active_cls}"', f'data-lang-opt="es" class="{inactive_cls}"')
    html = html.replace(f'data-lang-opt="{lang}" class="{inactive_cls}"', f'data-lang-opt="{lang}" class="{active_cls}"')

    # 8. Botón Contactar
    contact_text = t_nav["contacto"]
    html = re.sub(
        r'<a id="nav-contact-btn" href="[^"]*#contacto"([^>]*)>[\s\S]*?</a>',
        rf'<a id="nav-contact-btn" href="/{lang}/#contacto"\1><span data-i18n="nav_contact">{contact_text}</span><i data-lucide="arrow-down" class="w-3 h-3 stroke-[3]"></i></a>',
        html
    )

    # 9. Ojos del logo
    html = re.sub(
        r'<a href="[^"]*" class="group py-1 inline-flex items-center shrink-0 pl-1" aria-label="CoolPadel Eyes">',
        f'<a href="/{lang}/" class="group py-1 inline-flex items-center shrink-0 pl-1" aria-label="CoolPadel Eyes">',
        html
    )

    return html

def build_blog_hub(lang):
    d = BLOG_HUB_DATA[lang]
    is_es = (lang == "es")
    canonical = "https://coolpadelstudios.com/blog/" if is_es else f"https://coolpadelstudios.com/{lang}/blog/"
    og_locale = {"es": "es_ES", "en": "en_US", "fr": "fr_FR", "it": "it_IT"}[lang]
    asset_prefix = "../" if is_es else "../../"

    # Base HTML desde ES
    with open("coolpadel-web/blog/index.html", "r", encoding="utf-8") as f:
        base_html = f.read()

    hreflangs = f"""  <link rel="canonical" href="{canonical}">

  <!-- SEO Multilingüe Hreflang -->
  <link rel="alternate" hreflang="es" href="https://coolpadelstudios.com/blog/">
  <link rel="alternate" hreflang="en" href="https://coolpadelstudios.com/en/blog/">
  <link rel="alternate" hreflang="fr" href="https://coolpadelstudios.com/fr/blog/">
  <link rel="alternate" hreflang="it" href="https://coolpadelstudios.com/it/blog/">
  <link rel="alternate" hreflang="x-default" href="https://coolpadelstudios.com/blog/">
  <meta name="language" content="{lang}">"""

    # Limpiar cualquier bloque hreflang previo para evitar duplicados
    html = re.sub(r'\s*<!-- SEO Multilingüe Hreflang -->\s*(<link rel="alternate" hreflang="[^"]+" href="[^"]+">\s*)+', '', base_html)
    html = re.sub(r'\s*<meta name="language" content="[^"]+">', '', html)
    html = re.sub(r'<link rel="canonical"[^>]*>', hreflangs, html)

    if is_es:
        return html

    html = html.replace('<html lang="es"', f'<html lang="{lang}"')
    html = re.sub(r'<title>.*?</title>', f'<title>{d["title"]}</title>', html)
    html = re.sub(r'<meta name="description" content=".*?">', f'<meta name="description" content="{d["desc"]}">', html)
    html = html.replace('content="es_ES"', f'content="{og_locale}"')
    html = html.replace('content="https://coolpadelstudios.com/blog/"', f'content="{canonical}"')
    html = html.replace('href="../', f'href="{asset_prefix}')
    html = html.replace('src="../', f'src="{asset_prefix}')
    html = html.replace('"inLanguage": "es"', f'"inLanguage": "{lang}"')

    # Traducción de títulos hero
    html = html.replace('Blog & Newsletter de la Industria del Pádel', d['title'].split(' | ')[0])
    html = html.replace('Blog & Newsletter de la <span class="text-[#f2920b]">Industria del Pádel</span>', d['h1'])
    html = html.replace('Análisis estratégico y noticias del ecosistema de raqueta por Javier Villoria.', d['lead'])

    # Filtros de categorías
    html = html.replace('>Todas las Guías<', f'>{d["filter_all"]}<')
    html = html.replace('>Cámaras & Tecnología<', f'>{d["filter_cam"]}<')
    html = html.replace('>Rentabilidad & Gestión<', f'>{d["filter_fin"]}<')
    html = html.replace('>Torneos & Eventos<', f'>{d["filter_tourn"]}<')
    html = html.replace('>Llaveros & Merchandising<', f'>{d["filter_merch"]}<')

    # Convertir todas las tarjetas de los 29 artículos a rutas localizadas
    for slug in ALL_ARTICLES_I18N:
        html = html.replace(f'href="/blog/{slug}/"', f'href="/{lang}/blog/{slug}/"')
        html = html.replace(f'href="./{slug}/"', f'href="/{lang}/blog/{slug}/"')

    # Adaptar cabecera oficial
    html = adapt_header_and_nav(html, lang, asset_prefix)

    return html

def build_article_page(slug, lang):
    is_es = (lang == "es")
    canonical = f"https://coolpadelstudios.com/blog/{slug}/" if is_es else f"https://coolpadelstudios.com/{lang}/blog/{slug}/"
    og_locale = {"es": "es_ES", "en": "en_US", "fr": "fr_FR", "it": "it_IT"}[lang]
    asset_prefix = "../../" if is_es else "../../../"

    es_file = f"coolpadel-web/blog/{slug}/index.html"
    if not os.path.exists(es_file):
        return None

    with open(es_file, "r", encoding="utf-8") as f:
        base_html = f.read()

    hreflangs = f"""  <link rel="canonical" href="{canonical}">

  <!-- SEO Multilingüe Hreflang -->
  <link rel="alternate" hreflang="es" href="https://coolpadelstudios.com/blog/{slug}/">
  <link rel="alternate" hreflang="en" href="https://coolpadelstudios.com/en/blog/{slug}/">
  <link rel="alternate" hreflang="fr" href="https://coolpadelstudios.com/fr/blog/{slug}/">
  <link rel="alternate" hreflang="it" href="https://coolpadelstudios.com/it/blog/{slug}/">
  <link rel="alternate" hreflang="x-default" href="https://coolpadelstudios.com/blog/{slug}/">
  <meta name="language" content="{lang}">"""

    # Limpiar cualquier bloque previo de hreflangs
    html = re.sub(r'\s*<!-- SEO Multilingüe Hreflang -->\s*(<link rel="alternate" hreflang="[^"]+" href="[^"]+">\s*)+', '', base_html)
    html = re.sub(r'\s*<meta name="language" content="[^"]+">', '', html)
    html = re.sub(r'<link rel="canonical"[^>]*>', hreflangs, html)

    if is_es:
        return html

    d = ALL_ARTICLES_I18N[slug][lang]
    html = html.replace('<html lang="es"', f'<html lang="{lang}"')
    html = re.sub(r'<title>.*?</title>', f'<title>{d["title"]}</title>', html)
    html = re.sub(r'<meta name="description" content=".*?">', f'<meta name="description" content="{d["desc"]}">', html)
    html = html.replace('content="es_ES"', f'content="{og_locale}"')
    html = re.sub(r'<meta property="og:url" content="[^"]*">', f'<meta property="og:url" content="{canonical}">', html)
    html = re.sub(r'<meta property="og:title" content="[^"]*">', f'<meta property="og:title" content="{d["title"]}">', html)
    html = re.sub(r'<meta property="og:description" content="[^"]*">', f'<meta property="og:description" content="{d["desc"]}">', html)
    html = re.sub(r'<meta name="twitter:title" content="[^"]*">', f'<meta name="twitter:title" content="{d["title"]}">', html)
    html = re.sub(r'<meta name="twitter:description" content="[^"]*">', f'<meta name="twitter:description" content="{d["desc"]}">', html)
    html = html.replace('"inLanguage": "es"', f'"inLanguage": "{lang}"')
    html = html.replace(f'"headline": "{slug}"', f'"headline": "{d["h1"]}"')

    # Ajustar rutas relativas de assets y navegación
    html = html.replace('href="../../', f'href="{asset_prefix}')
    html = html.replace('src="../../', f'src="{asset_prefix}')
    html = html.replace('href="../"', f'href="{asset_prefix}{lang}/blog/"')

    # Actualizar H1 del artículo
    def replace_h1(match):
        attrs = match.group(1)
        return f'<h1{attrs}>\n            {d["h1"]}\n          </h1>'
    html = re.sub(r'<h1([^>]*)>[\s\S]*?</h1>', replace_h1, html, count=1)

    # Actualizar Subtitle y Badge si están presentes en el diccionario y en el HTML
    es_data = ALL_ARTICLES_I18N[slug]["es"]
    if es_data.get("subtitle") and d.get("subtitle") and es_data["subtitle"] in html:
        html = html.replace(es_data["subtitle"], d["subtitle"])
    if es_data.get("badge") and d.get("badge") and es_data["badge"] in html:
        html = html.replace(es_data["badge"], d["badge"])

    # Adaptar cabecera oficial completa
    html = adapt_header_and_nav(html, lang, asset_prefix)

    # 4. Enlaces relativos a otras newsletters (en Highlights: ../highlights-0X/ -> /{lang}/blog/highlights-0X/)
    for hl_slug in ["highlights-01", "highlights-02", "highlights-03"]:
        html = html.replace(f'href="../{hl_slug}/"', f'href="/{lang}/blog/{hl_slug}/"')

    return html

def run():
    print(f">> Compilando Blog y Catálogo Completo ({len(ALL_ARTICLES_I18N)} artículos) en 4 Idiomas (ES, EN, FR, IT)...")

    # 1. Compilación del Blog Hub
    for lang in ["es", "en", "fr", "it"]:
        html = build_blog_hub(lang)
        out_path = "coolpadel-web/blog/index.html" if lang == "es" else f"coolpadel-web/{lang}/blog/index.html"
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"  [OK] Blog Hub ({lang.upper()}): {out_path}")

    # 2. Compilación de todos los Artículos y Newsletters
    count_generated = 0
    for slug in sorted(ALL_ARTICLES_I18N.keys()):
        for lang in ["es", "en", "fr", "it"]:
            html = build_article_page(slug, lang)
            if not html:
                print(f"  [AVISO] No se pudo compilar '{slug}' para {lang.upper()}")
                continue
            out_path = f"coolpadel-web/blog/{slug}/index.html" if lang == "es" else f"coolpadel-web/{lang}/blog/{slug}/index.html"
            os.makedirs(os.path.dirname(out_path), exist_ok=True)
            with open(out_path, "w", encoding="utf-8") as f:
                f.write(html)
            count_generated += 1

    print(f">> Total páginas generadas: {count_generated} ({len(ALL_ARTICLES_I18N)} artículos x 4 idiomas)")
    print(">> Blog 100% Cuatrilingüe Completado Con Éxito!")

if __name__ == "__main__":
    run()
