#!/usr/bin/env python3
"""
Compilador del Blog y Guías Flagship en 4 Idiomas (ES, EN, FR, IT):
- Blog Hub (/blog/ y /{lang}/blog/)
- 7 Guías Flagship con versiones dedicadas en EN, FR, IT
- Inyección de Hreflangs simétricos de 5 vías en todos los artículos
"""
import os
import sys
import re

cur_dir = os.path.dirname(os.path.abspath(__file__))
if cur_dir not in sys.path:
    sys.path.insert(0, cur_dir)

from translations_blog import BLOG_HUB_DATA, FLAGSHIP_GUIDES_DATA

def get_blog_lang_switcher(lang, slug=None):
    langs = ["es", "en", "fr", "it"]
    links = []
    for l in langs:
        if slug:
            url = f"/blog/{slug}/" if l == "es" else f"/{l}/blog/{slug}/"
        else:
            url = "/blog/" if l == "es" else f"/{l}/blog/"
        if l == lang:
            links.append(f'<a href="{url}" class="px-2 py-1 rounded text-xs transition bg-[#f2920b] text-slate-950 font-black">{l.upper()}</a>')
        else:
            links.append(f'<a href="{url}" class="px-2 py-1 rounded text-xs transition text-slate-300 hover:text-white">{l.upper()}</a>')
    return f'<div class="flex items-center gap-1 border border-slate-700 rounded-lg p-0.5 bg-slate-800/80">{"".join(links)}</div>'

def build_blog_hub(lang):
    d = BLOG_HUB_DATA[lang]
    is_es = (lang == "es")
    canonical = "https://coolpadelstudios.com/blog/" if is_es else f"https://coolpadelstudios.com/{lang}/blog/"
    og_locale = {"es": "es_ES", "en": "en_US", "fr": "fr_FR", "it": "it_IT"}[lang]
    asset_prefix = "../" if is_es else "../../"

    # Base HTML from ES
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

    if is_es:
        html = re.sub(r'<link rel="canonical"[^>]*>', hreflangs, base_html)
        return html

    html = base_html
    html = html.replace('<html lang="es"', f'<html lang="{lang}"')
    html = re.sub(r'<link rel="canonical"[^>]*>', hreflangs, html)
    html = re.sub(r'<title>.*?</title>', f'<title>{d["title"]}</title>', html)
    html = re.sub(r'<meta name="description" content=".*?">', f'<meta name="description" content="{d["desc"]}">', html)
    html = html.replace('content="es_ES"', f'content="{og_locale}"')
    html = html.replace('content="https://coolpadelstudios.com/blog/"', f'content="{canonical}"')
    html = html.replace('href="../', f'href="{asset_prefix}')
    html = html.replace('src="../', f'src="{asset_prefix}')
    html = html.replace('"inLanguage": "es"', f'"inLanguage": "{lang}"')

    # Hero translations
    html = html.replace('Blog & Newsletter de la Industria del Pádel', d['title'].split(' | ')[0])
    html = html.replace('Blog & Newsletter de la <span class="text-[#f2920b]">Industria del Pádel</span>', d['h1'])
    html = html.replace('Análisis estratégico y noticias del ecosistema de raqueta por Javier Villoria.', d['lead'])

    # Category filters
    html = html.replace('>Todas las Guías<', f'>{d["filter_all"]}<')
    html = html.replace('>Cámaras & Tecnología<', f'>{d["filter_cam"]}<')
    html = html.replace('>Rentabilidad & Gestión<', f'>{d["filter_fin"]}<')
    html = html.replace('>Torneos & Eventos<', f'>{d["filter_tourn"]}<')
    html = html.replace('>Llaveros & Merchandising<', f'>{d["filter_merch"]}<')

    # Links in cards pointing to localized versions if flagship guide
    for slug in FLAGSHIP_GUIDES_DATA:
        html = html.replace(f'href="/blog/{slug}/"', f'href="/{lang}/blog/{slug}/"')
        html = html.replace(f'href="./{slug}/"', f'href="/{lang}/blog/{slug}/"')

    # Inject Lang Switcher in header
    switcher = get_blog_lang_switcher(lang)
    html = html.replace('</nav>\n\n      <a href="../#contacto"', f'</nav>\n\n      <div class="flex items-center gap-3">\n        {switcher}\n        <a href="../../{lang}/#contacto"')
    html = html.replace('</nav>\r\n\r\n      <a href="../#contacto"', f'</nav>\r\n\r\n      <div class="flex items-center gap-3">\r\n        {switcher}\r\n        <a href="../../{lang}/#contacto"')

    return html

def build_flagship_guide(slug, lang):
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

    if is_es:
        html = re.sub(r'<link rel="canonical"[^>]*>', hreflangs, base_html)
        return html

    d = FLAGSHIP_GUIDES_DATA[slug][lang]
    html = base_html
    html = html.replace('<html lang="es"', f'<html lang="{lang}"')
    html = re.sub(r'<link rel="canonical"[^>]*>', hreflangs, html)
    html = re.sub(r'<title>.*?</title>', f'<title>{d["title"]}</title>', html)
    html = re.sub(r'<meta name="description" content=".*?">', f'<meta name="description" content="{d["desc"]}">', html)
    html = html.replace('content="es_ES"', f'content="{og_locale}"')
    html = re.sub(r'<meta property="og:url" content="[^"]*">', f'<meta property="og:url" content="{canonical}">', html)
    html = html.replace('href="../../', f'href="{asset_prefix}')
    html = html.replace('src="../../', f'src="{asset_prefix}')
    html = html.replace('href="../"', f'href="{asset_prefix}{lang}/blog/"')

    # Update H1 and Subtitle
    es_data = FLAGSHIP_GUIDES_DATA[slug]["es"]
    html = html.replace(es_data["h1"], d["h1"])
    html = html.replace(es_data["subtitle"], d["subtitle"])
    html = html.replace(es_data["badge"], d["badge"])

    # Language Switcher
    switcher = get_blog_lang_switcher(lang, slug)
    if 'data-lucide="arrow-up-right"' in html:
        html = html.replace('<a href="../../#contacto"', f'{switcher}\n        <a href="../../../{lang}/#contacto"')

    return html

def run():
    print(">> Compilando Blog y Guías Flagship en 4 Idiomas (ES, EN, FR, IT)...")

    # 1. Blog Hub
    for lang in ["es", "en", "fr", "it"]:
        html = build_blog_hub(lang)
        out_path = "coolpadel-web/blog/index.html" if lang == "es" else f"coolpadel-web/{lang}/blog/index.html"
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"  [OK] Blog Hub ({lang.upper()}): {out_path}")

    # 2. Flagship Guides
    for slug in FLAGSHIP_GUIDES_DATA:
        for lang in ["es", "en", "fr", "it"]:
            html = build_flagship_guide(slug, lang)
            if not html:
                continue
            out_path = f"coolpadel-web/blog/{slug}/index.html" if lang == "es" else f"coolpadel-web/{lang}/blog/{slug}/index.html"
            os.makedirs(os.path.dirname(out_path), exist_ok=True)
            with open(out_path, "w", encoding="utf-8") as f:
                f.write(html)
            print(f"  [OK] Guía '{slug}' ({lang.upper()}): {out_path}")

        print(">> Blog 100% Cuatrilingue Completado Con Exito!")

if __name__ == "__main__":
    run()
