#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generador Maestro del Sitemap XML Multilingüe (ES, EN, FR, IT) para coolpadelstudios.com.
Genera todas las entradas con etiquetas xhtml:link rel="alternate" hreflang para máxima indexación SEO y GEO.
"""
import os
import sys

cur_dir = os.path.dirname(os.path.abspath(__file__))
if cur_dir not in sys.path:
    sys.path.insert(0, cur_dir)

from dataset_franquicias import FRANQUICIAS
from translations_landings import LANDINGS_I18N as LANDING_PAGES
from translations_blog import FLAGSHIP_GUIDES_DATA

DOMAIN = "https://coolpadelstudios.com"
TODAY = "2026-10-20"

def get_cluster_xml(es_path, en_path, fr_path, it_path, priority="0.8", changefreq="weekly"):
    """
    Genera un bloque <url> para cada idioma con enlaces hreflang simétricos de 5 vías.
    """
    es_url = f"{DOMAIN}{es_path}"
    en_url = f"{DOMAIN}{en_path}"
    fr_url = f"{DOMAIN}{fr_path}"
    it_url = f"{DOMAIN}{it_path}"
    x_default_url = es_url

    hreflang_links = f"""    <xhtml:link rel="alternate" hreflang="es" href="{es_url}"/>
    <xhtml:link rel="alternate" hreflang="en" href="{en_url}"/>
    <xhtml:link rel="alternate" hreflang="fr" href="{fr_url}"/>
    <xhtml:link rel="alternate" hreflang="it" href="{it_url}"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="{x_default_url}"/>"""

    blocks = []
    variants = [
        (es_url, priority),
        (en_url, priority),
        (fr_url, priority),
        (it_url, priority),
    ]

    for url, prio in variants:
        block = f"""  <url>
    <loc>{url}</loc>
    <lastmod>{TODAY}</lastmod>
    <changefreq>{changefreq}</changefreq>
    <priority>{prio}</priority>
{hreflang_links}
  </url>"""
        blocks.append(block)

    return blocks

def generate_sitemap():
    print(">> Generando Sitemap Maestro Cuatrilingüe (ES, EN, FR, IT)...")
    all_blocks = []

    # 1. Home
    all_blocks.extend(get_cluster_xml("/", "/en/", "/fr/", "/it/", priority="1.0", changefreq="daily"))

    # 2. Cámaras Core Landing
    all_blocks.extend(get_cluster_xml("/camaras/", "/en/camaras/", "/fr/camaras/", "/it/camaras/", priority="0.95", changefreq="weekly"))

    # 3. 11 B2B Landings
    for slug in LANDING_PAGES:
        priority = "0.9" if "camaras" in slug or "save-my-play" in slug else "0.85"
        all_blocks.extend(get_cluster_xml(
            f"/{slug}/",
            f"/en/{slug}/",
            f"/fr/{slug}/",
            f"/it/{slug}/",
            priority=priority,
            changefreq="weekly"
        ))

    # 4. Herramientas Hub
    all_blocks.extend(get_cluster_xml(
        "/herramientas/",
        "/en/herramientas/",
        "/fr/herramientas/",
        "/it/herramientas/",
        priority="0.9",
        changefreq="weekly"
    ))

    # 5. 4 Herramientas Interactivas
    tools_slugs = [
        "calculadora-roi-camaras-padel",
        "calculadora-coste-pistas-padel",
        "generador-americana-padel",
        "generador-cuadros-torneo-padel"
    ]
    for ts in tools_slugs:
        all_blocks.extend(get_cluster_xml(
            f"/herramientas/{ts}/",
            f"/en/herramientas/{ts}/",
            f"/fr/herramientas/{ts}/",
            f"/it/herramientas/{ts}/",
            priority="0.85",
            changefreq="weekly"
        ))

    # 6. Directorio Franquicias Hub
    all_blocks.extend(get_cluster_xml(
        "/franquicias-padel/",
        "/en/franquicias-padel/",
        "/fr/franquicias-padel/",
        "/it/franquicias-padel/",
        priority="0.85",
        changefreq="weekly"
    ))

    # 7. 167 Fichas de Franquicias Individuales
    for f in FRANQUICIAS:
        fid = f["id"]
        all_blocks.extend(get_cluster_xml(
            f"/franquicias-padel/{fid}/",
            f"/en/franquicias-padel/{fid}/",
            f"/fr/franquicias-padel/{fid}/",
            f"/it/franquicias-padel/{fid}/",
            priority="0.75",
            changefreq="monthly"
        ))

    # 8. Blog Hub
    all_blocks.extend(get_cluster_xml(
        "/blog/",
        "/en/blog/",
        "/fr/blog/",
        "/it/blog/",
        priority="0.85",
        changefreq="weekly"
    ))

    # 9. 7 Guías Flagship
    for slug in FLAGSHIP_GUIDES_DATA:
        priority = "0.9" if "barometro" in slug else "0.8"
        all_blocks.extend(get_cluster_xml(
            f"/blog/{slug}/",
            f"/en/blog/{slug}/",
            f"/fr/blog/{slug}/",
            f"/it/blog/{slug}/",
            priority=priority,
            changefreq="weekly"
        ))

    # 10. Resto de artículos y newsletters del blog (solo ES con fallback)
    all_blog_dirs = [d for d in os.listdir("coolpadel-web/blog") if os.path.isdir(f"coolpadel-web/blog/{d}")]
    for b_dir in all_blog_dirs:
        if b_dir in FLAGSHIP_GUIDES_DATA:
            continue
        art_path = f"coolpadel-web/blog/{b_dir}/index.html"
        if not os.path.isfile(art_path):
            continue
        art_url = f"{DOMAIN}/blog/{b_dir}/"
        block = f"""  <url>
    <loc>{art_url}</loc>
    <lastmod>{TODAY}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
    <xhtml:link rel="alternate" hreflang="es" href="{art_url}"/>
    <xhtml:link rel="alternate" hreflang="en" href="{DOMAIN}/en/blog/"/>
    <xhtml:link rel="alternate" hreflang="fr" href="{DOMAIN}/fr/blog/"/>
    <xhtml:link rel="alternate" hreflang="it" href="{DOMAIN}/it/blog/"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="{art_url}"/>
  </url>"""
        all_blocks.append(block)

    # 11. Páginas estáticas secundarias
    all_blocks.append(f"""  <url>
    <loc>{DOMAIN}/politica-de-devoluciones.html</loc>
    <lastmod>{TODAY}</lastmod>
    <changefreq>yearly</changefreq>
    <priority>0.3</priority>
  </url>""")

    # XML output
    xml_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:xhtml="http://www.w3.org/1999/xhtml">
{chr(10).join(all_blocks)}
</urlset>
"""

    out_file = os.path.join(cur_dir, "sitemap.xml")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(xml_content)

    print(f">> Sitemap XML generado con éxito: {len(all_blocks)} URLs registradas.")
    print(f"   Archivo guardado en: {out_file}")

if __name__ == "__main__":
    generate_sitemap()
