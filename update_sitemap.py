#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Actualizador de sitemap.xml para coolpadelstudios.com.
Garantiza que todas las páginas principales, blog, barómetro 2026 y las 167 franquicias
estén perfectamente indexadas en el sitemap XML.
"""

import os
import sys
import xml.etree.ElementTree as ET

if sys.platform == "win32" and hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

from dataset_franquicias import FRANQUICIAS

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SITEMAP_FILE = os.path.join(BASE_DIR, "sitemap.xml")

with open(SITEMAP_FILE, "r", encoding="utf-8") as f:
    content = f.read()

# Verificar qué URLs faltan
urls_to_add = [
    "https://coolpadelstudios.com/save-my-play/",
    "https://coolpadelstudios.com/camaras-grabacion-pistas-padel/",
    "https://coolpadelstudios.com/camaras-padel-playtomic/",
    "https://coolpadelstudios.com/camaras-padel-matchi/",
    "https://coolpadelstudios.com/camaras-padel-resasports/",
    "https://coolpadelstudios.com/camaras-padel-madrid/",
    "https://coolpadelstudios.com/camaras-padel-barcelona/",
    "https://coolpadelstudios.com/llaveros-padel-personalizados/",
    "https://coolpadelstudios.com/llaveros-tenis-personalizados/",
    "https://coolpadelstudios.com/welcome-packs-torneos-padel/",
    "https://coolpadelstudios.com/llaveros-personalizados-clubs-padel/",
    "https://coolpadelstudios.com/blog/barometro-camaras-padel-2026/",
    "https://coolpadelstudios.com/blog/normativa-rgpd-camaras-pistas-padel/",
    "https://coolpadelstudios.com/blog/padmi-vs-save-my-play-camaras-padel/"
]

for f in FRANQUICIAS:
    urls_to_add.append(f"https://coolpadelstudios.com/franquicias-padel/{f['id']}/")

added_count = 0
closing_tag = "</urlset>"

if closing_tag in content:
    parts = content.split(closing_tag)
    base_part = parts[0].rstrip()
    
    new_xml_blocks = []
    for u in urls_to_add:
        if f"<loc>{u}</loc>" not in content:
            priority = "0.9" if "save-my-play" in u else ("0.85" if "barometro" in u or "padmi" in u else "0.75")
            block = f"""  <url>
    <loc>{u}</loc>
    <lastmod>2026-10-20</lastmod>
    <changefreq>weekly</changefreq>
    <priority>{priority}</priority>
  </url>"""
            new_xml_blocks.append(block)
            added_count += 1
            
    if new_xml_blocks:
        updated_content = base_part + "\n" + "\n".join(new_xml_blocks) + "\n</urlset>\n"
        with open(SITEMAP_FILE, "w", encoding="utf-8") as f:
            f.write(updated_content)
        print(f"Sitemap actualizado: {added_count} nuevas URLs añadidas (total actual: {content.count('<url>') + added_count})")
    else:
        print("Sitemap ya estaba al día con todas las URLs.")
else:
    print("Error: </urlset> no encontrado en sitemap.xml")
