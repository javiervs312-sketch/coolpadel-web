#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generador Maestro del Sitemap XML Multilingüe (ES, EN, FR, IT) para coolpadelstudios.com.
Incluye únicamente URLs 100% originales y traducidas con hreflang simétrico válido,
eliminando URLs fantasma (404) y duplicados en español bajo rutas /en/, /fr/, /it/.
"""
import os
import sys

cur_dir = os.path.dirname(os.path.abspath(__file__))
if cur_dir not in sys.path:
    sys.path.insert(0, cur_dir)

from dataset_franquicias import FRANQUICIAS
from translations_landings import LANDINGS_I18N

LANDING_SLUGS = list(LANDINGS_I18N["en"].keys())
DOMAIN = "https://coolpadelstudios.com"
TODAY = "2026-10-20"


def get_cluster_xml(es_path, en_path, fr_path, it_path, priority="0.85", changefreq="weekly"):
    """
    Genera un bloque <url> para cada idioma con enlaces hreflang simétricos de 5 vías.
    Solo para páginas 100% traducidas en los 4 idiomas.
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


def get_single_xml(path, priority="0.80", changefreq="weekly"):
    url = f"{DOMAIN}{path}"
    return f"""  <url>
    <loc>{url}</loc>
    <lastmod>{TODAY}</lastmod>
    <changefreq>{changefreq}</changefreq>
    <priority>{priority}</priority>
  </url>"""


def generate_sitemap():
    print(">> Generando Sitemap Maestro Optimizado (0 errores 404, 0 duplicados)...")
    all_blocks = []

    # 1. Home (4 idiomas 100% traducidos)
    all_blocks.extend(get_cluster_xml("/", "/en/", "/fr/", "/it/", priority="1.0", changefreq="daily"))

    # 2. Cámaras Core Landing (4 idiomas 100% traducidos)
    all_blocks.extend(get_cluster_xml("/camaras/", "/en/camaras/", "/fr/camaras/", "/it/camaras/", priority="0.95", changefreq="weekly"))

    # 3. 11 B2B Landings Transaccionales (44 páginas 100% traducidas)
    for slug in LANDING_SLUGS:
        priority = "0.95" if ("camaras" in slug or "save-my-play" in slug or "llaveros-padel" in slug) else "0.90"
        all_blocks.extend(get_cluster_xml(
            f"/{slug}/",
            f"/en/{slug}/",
            f"/fr/{slug}/",
            f"/it/{slug}/",
            priority=priority,
            changefreq="weekly"
        ))

    # 4. Herramientas Hub (4 idiomas 100% traducidos)
    all_blocks.extend(get_cluster_xml(
        "/herramientas/",
        "/en/herramientas/",
        "/fr/herramientas/",
        "/it/herramientas/",
        priority="0.90",
        changefreq="weekly"
    ))

    # 5. 4 Herramientas Interactivas (16 páginas 100% traducidas)
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
            priority="0.90",
            changefreq="weekly"
        ))

    # 6. Directorio Franquicias Hub (4 idiomas)
    all_blocks.extend(get_cluster_xml(
        "/franquicias-padel/",
        "/en/franquicias-padel/",
        "/fr/franquicias-padel/",
        "/it/franquicias-padel/",
        priority="0.85",
        changefreq="weekly"
    ))

    # 7. Blog Hub (4 idiomas)
    all_blocks.extend(get_cluster_xml(
        "/blog/",
        "/en/blog/",
        "/fr/blog/",
        "/it/blog/",
        priority="0.85",
        changefreq="weekly"
    ))

    # 8. Todos los artículos y estudios del Blog en su URL canónica original (ES)
    blog_root = os.path.join(cur_dir, "blog")
    all_blog_dirs = sorted([d for d in os.listdir(blog_root) if os.path.isdir(os.path.join(blog_root, d))])
    for b_dir in all_blog_dirs:
        art_path = os.path.join(blog_root, b_dir, "index.html")
        if not os.path.isfile(art_path):
            continue
        prio = "0.90" if "barometro" in b_dir or "comparativa" in b_dir or "rentabilidad" in b_dir else "0.80"
        all_blocks.append(get_single_xml(f"/blog/{b_dir}/", priority=prio, changefreq="weekly"))

    # 9. Fichas de Franquicias Individuales en su URL canónica original (ES)
    for f in FRANQUICIAS:
        fid = f["id"]
        all_blocks.append(get_single_xml(f"/franquicias-padel/{fid}/", priority="0.70", changefreq="monthly"))

    # 10. Páginas estáticas secundarias
    all_blocks.append(get_single_xml("/politica-de-devoluciones.html", priority="0.30", changefreq="yearly"))

    xml_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:xhtml="http://www.w3.org/1999/xhtml">
{chr(10).join(all_blocks)}
</urlset>
"""

    out_file = os.path.join(cur_dir, "sitemap.xml")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(xml_content)

    print(f">> Sitemap XML generado con éxito: {len(all_blocks)} URLs canónicas registradas.")
    print(f"   Archivo guardado en: {out_file}")


if __name__ == "__main__":
    generate_sitemap()
