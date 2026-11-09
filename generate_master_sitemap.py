#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generador Maestro del Sitemap XML Multilingüe (ES, EN, FR, IT, DE) para coolpadelstudios.com.
Incluye únicamente URLs 100% originales y traducidas con hreflang simétrico válido,
eliminando URLs fantasma (404) y duplicados.
"""
import os
import sys
from datetime import datetime

cur_dir = os.path.dirname(os.path.abspath(__file__))
if cur_dir not in sys.path:
    sys.path.insert(0, cur_dir)

from dataset_franquicias import FRANQUICIAS
from translations_landings import LANDINGS_I18N
from translations_blog import FLAGSHIP_GUIDES_DATA
from extra_articles_i18n import EXTRA_ARTICLES_I18N

ALL_BLOG_SLUGS = set(FLAGSHIP_GUIDES_DATA.keys()).union(EXTRA_ARTICLES_I18N.keys())

# Las landings simétricas multilenguaje (llaveros, save-my-play, software genérico)
COMMON_LANDINGS = [
    "llaveros-padel-personalizados",
    "llaveros-tenis-personalizados",
    "welcome-packs-torneos-padel",
    "llaveros-personalizados-clubs-padel",
    "camaras-grabacion-pistas-padel",
    "camaras-padel-playtomic",
    "camaras-padel-matchi",
    "camaras-padel-resasports",
    "save-my-play"
]

# Landings locales nativas por mercado e idioma
GEO_LOCAL_LANDINGS = [
    # ES
    ("/camaras-padel-madrid/", "0.90"),
    ("/camaras-padel-barcelona/", "0.90"),
    ("/camaras-padel-valencia/", "0.90"),
    ("/camaras-padel-malaga/", "0.90"),
    # EN (UK & US)
    ("/en/padel-court-cameras-london/", "0.90"),
    ("/en/padel-court-cameras-miami/", "0.90"),
    # FR (France)
    ("/fr/cameras-padel-paris/", "0.90"),
    ("/fr/cameras-padel-lyon/", "0.90"),
    # IT (Italia)
    ("/it/telecamere-padel-roma/", "0.90"),
    ("/it/telecamere-padel-milano/", "0.90"),
]
DOMAIN = "https://coolpadelstudios.com"
TODAY = datetime.utcnow().strftime("%Y-%m-%d")

# 20 articulos de camaras
CAMARAS_SLUGS = [
    "por-donde-empezar-si-estoy-pensando-en-poner-camaras",
    "errores-clubs-se-arrepienten-de-poner-camaras",
    "camaras-de-padel-o-videovigilancia",
    "cuanto-cuesta-poner-camaras",
    "inversion-inicial-camaras-180-euros",
    "es-caro-save-my-play",
    "es-rentable-poner-camaras",
    "por-que-no-recomiendo-plan-analytics",
    "que-pasa-si-cancelo",
    "como-montar-camara-save-my-play",
    "problemas-con-las-camaras",
    "que-son-las-coaching-tools",
    "camaras-en-exterior-lluvia-nieve-viento",
    "como-ver-highlights-sin-app",
    "mejores-empresas-camaras-padel-espana",
    "por-que-no-conocia-save-my-play",
    "save-my-play-en-pocas-palabras",
    "por-que-coolpadel-colabora-con-save-my-play",
    "he-comprado-camaras-que-pasa-ahora",
    "por-que-no-me-interesa-venderte-una-camara",
]

# 13 articulos de llaveros
LLAVEROS_PADEL_SLUGS = [
    "pedido-minimo-plazos-entrega-llaveros-padel",
    "como-pedir-muestra-fisica-15-euros",
    "personalizar-reverso-patrocinador-redes",
    "precios-facturacion-iva-formas-pago",
    "tamano-peso-material-goma-3d-microinyectada",
    "vender-llaveros-tienda-recepcion-club",
    "ocasiones-usos-llaveros-padel-torneos-socios",
    "paises-envio-cobertura-internacional",
    "reutilizar-molde-pedidos-futuros-reposiciones",
]

LLAVEROS_TENIS_SLUGS = [
    "formatos-logotipo-escudo-para-llaveros-tenis",
    "vender-llaveros-tenis-pro-shop-escuelas-rentabilidad",
    "llaveros-tenis-regalos-torneos-welcome-packs",
    "llaveros-de-tenis-vs-padel-diferencias-materiales",
]


def get_cluster_xml(es_path, en_path, fr_path, it_path, priority="0.85", changefreq="weekly"):
    """
    Genera un bloque <url> para cada idioma con enlaces hreflang simétricos de 5 vías (4 idiomas + x-default).
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


def get_camaras_cluster_xml(slug=None, priority="0.90", changefreq="weekly"):
    """
    Genera un bloque <url> para los 5 idiomas de cámaras (ES, EN, FR, IT, DE + x-default).
    """
    if slug:
        es_path = f"/camaras/articulos/{slug}/"
        en_path = f"/en/camaras/articulos/{slug}/"
        fr_path = f"/fr/camaras/articulos/{slug}/"
        it_path = f"/it/camaras/articulos/{slug}/"
        de_path = f"/de/camaras/articulos/{slug}/"
    else:
        es_path = "/camaras/"
        en_path = "/en/camaras/"
        fr_path = "/fr/camaras/"
        it_path = "/it/camaras/"
        de_path = "/de/camaras/"

    es_url = f"{DOMAIN}{es_path}"
    en_url = f"{DOMAIN}{en_path}"
    fr_url = f"{DOMAIN}{fr_path}"
    it_url = f"{DOMAIN}{it_path}"
    de_url = f"{DOMAIN}{de_path}"
    x_default_url = es_url

    hreflang_links = f"""    <xhtml:link rel="alternate" hreflang="es" href="{es_url}"/>
    <xhtml:link rel="alternate" hreflang="en" href="{en_url}"/>
    <xhtml:link rel="alternate" hreflang="fr" href="{fr_url}"/>
    <xhtml:link rel="alternate" hreflang="it" href="{it_url}"/>
    <xhtml:link rel="alternate" hreflang="de" href="{de_url}"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="{x_default_url}"/>"""

    blocks = []
    variants = [
        (es_url, priority),
        (en_url, priority),
        (fr_url, priority),
        (it_url, priority),
        (de_url, priority),
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
    print(f">> Generando Sitemap Maestro Optimizado (fecha: {TODAY})...")
    all_blocks = []

    # 1. Home (4 idiomas 100% traducidos)
    all_blocks.extend(get_cluster_xml("/", "/en/", "/fr/", "/it/", priority="1.0", changefreq="daily"))

    # 2. Cámaras Core Landing (5 idiomas 100% traducidos)
    all_blocks.extend(get_camaras_cluster_xml(slug=None, priority="0.95", changefreq="weekly"))

    # 3. 20 Artículos de Cámaras (100 URLs: 20 x 5 idiomas)
    for c_slug in CAMARAS_SLUGS:
        all_blocks.extend(get_camaras_cluster_xml(slug=c_slug, priority="0.88", changefreq="weekly"))

    # 4. B2B Landings Transaccionales Multilingües Simétricas (36 URLs: 9 x 4 idiomas)
    for slug in COMMON_LANDINGS:
        priority = "0.95" if ("camaras" in slug or "save-my-play" in slug or "llaveros-padel" in slug) else "0.90"
        all_blocks.extend(get_cluster_xml(
            f"/{slug}/",
            f"/en/{slug}/",
            f"/fr/{slug}/",
            f"/it/{slug}/",
            priority=priority,
            changefreq="weekly"
        ))

    # 4b. Landings Geo-Locales Nativas por Idioma y Ciudad (10 URLs)
    # 4c. 50 Landings Canónicas de Países de Cámaras Save My Play (50 URLs oficiales nativas, sin duplicados)
    try:
        from paises_data_50 import COUNTRIES_50
        seen_slugs = set()
        for item in COUNTRIES_50:
            # La versión canónica oficial es siempre el slug local nativo
            s = item.get('slug_local') or item.get('slug')
            if s and s not in seen_slugs:
                seen_slugs.add(s)
                all_blocks.append(get_single_xml(f"/camaras/{s}/", priority="0.95", changefreq="weekly"))
        print(f"Added {len(seen_slugs)} canonical country slugs to sitemap (0 duplicate alternates).")
    except Exception as e:
        print(f"Error adding country landings to sitemap: {e}")

    for path, prio in GEO_LOCAL_LANDINGS:
        all_blocks.append(get_single_xml(path, priority=prio, changefreq="weekly"))

    # 5. Artículos de Llaveros Pádel y Tenis en Español
    for lp in LLAVEROS_PADEL_SLUGS:
        all_blocks.append(get_single_xml(f"/llaveros-padel-personalizados/articulos/{lp}/", priority="0.85", changefreq="weekly"))
    for lt in LLAVEROS_TENIS_SLUGS:
        all_blocks.append(get_single_xml(f"/llaveros-tenis-personalizados/articulos/{lt}/", priority="0.85", changefreq="weekly"))

    # 6. Herramientas Hub (4 idiomas 100% traducidos)
    all_blocks.extend(get_cluster_xml(
        "/herramientas/",
        "/en/herramientas/",
        "/fr/herramientas/",
        "/it/herramientas/",
        priority="0.90",
        changefreq="weekly"
    ))

    # 7. 4 Herramientas Interactivas (16 páginas 100% traducidas)
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

    # 8. Directorio Franquicias Hub (4 idiomas)
    all_blocks.extend(get_cluster_xml(
        "/franquicias-padel/",
        "/en/franquicias-padel/",
        "/fr/franquicias-padel/",
        "/it/franquicias-padel/",
        priority="0.85",
        changefreq="weekly"
    ))

    # 9. Blog Hub (4 idiomas)
    all_blocks.extend(get_cluster_xml(
        "/blog/",
        "/en/blog/",
        "/fr/blog/",
        "/it/blog/",
        priority="0.85",
        changefreq="weekly"
    ))

    # 10. Artículos del Blog: Catálogo Completo (29 artículos en 4 idiomas con clúster simétrico)
    blog_root = os.path.join(cur_dir, "blog")
    all_blog_dirs = sorted([d for d in os.listdir(blog_root) if os.path.isdir(os.path.join(blog_root, d)) and not d.startswith(".")])
    for b_dir in all_blog_dirs:
        art_path = os.path.join(blog_root, b_dir, "index.html")
        if not os.path.isfile(art_path):
            continue
        if b_dir in ALL_BLOG_SLUGS:
            prio = "0.90" if "barometro" in b_dir or "comparativa" in b_dir or "rentabilidad" in b_dir else "0.85"
            all_blocks.extend(get_cluster_xml(
                f"/blog/{b_dir}/",
                f"/en/blog/{b_dir}/",
                f"/fr/blog/{b_dir}/",
                f"/it/blog/{b_dir}/",
                priority=prio,
                changefreq="weekly"
            ))
        else:
            all_blocks.append(get_single_xml(f"/blog/{b_dir}/", priority="0.80", changefreq="weekly"))

    # 11. Fichas de Franquicias Individuales (100% traducidas en 4 idiomas con clúster simétrico)
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

    # 12. Páginas estáticas secundarias
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
