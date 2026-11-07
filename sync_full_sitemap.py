# -*- coding: utf-8 -*-
"""
Sincroniza y reconstruye el sitemap.xml de coolpadelstudios.com
para incluir el 100% de las páginas generadas en disco (ciudades, nuevos artículos, países, etc.).
"""

import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SITEMAP_FILE = os.path.join(BASE_DIR, "sitemap.xml")

def update_full_sitemap():
    all_urls = set()
    
    for root, dirs, files in os.walk(BASE_DIR):
        # Excluir carpetas de sistema o assets
        rel_dir = os.path.relpath(root, BASE_DIR).replace('\\', '/')
        if any(rel_dir.startswith(p) for p in ['.git', 'assets', '__pycache__', 'scratch']):
            continue
            
        for f in files:
            if f.endswith('.html'):
                rel_path = os.path.relpath(os.path.join(root, f), BASE_DIR).replace('\\', '/')
                
                # Excluir páginas de error o plantillas
                if rel_path in ['404.html', 'template_clean.html', 'articulo_camaras_club.html']:
                    continue
                    
                if rel_path == 'index.html':
                    url = 'https://coolpadelstudios.com/'
                elif rel_path.endswith('/index.html'):
                    url = 'https://coolpadelstudios.com/' + rel_path[:-10]
                else:
                    url = 'https://coolpadelstudios.com/' + rel_path
                    
                if not url.endswith('.html') and not url.endswith('/'):
                    url += '/'
                    
                all_urls.add(url)

    today = datetime.now().strftime("%Y-%m-%d")
    sorted_urls = sorted(list(all_urls))
    
    entries = []
    for u in sorted_urls:
        # Prioridad SEO
        if u == 'https://coolpadelstudios.com/':
            priority = "1.0"
            changefreq = "daily"
        elif '/camaras/' in u and len(u.split('/')) <= 5:
            priority = "0.9"
            changefreq = "weekly"
        elif '/camaras/' in u:
            priority = "0.8"
            changefreq = "weekly"
        elif '/blog/' in u:
            priority = "0.8"
            changefreq = "weekly"
        elif '/herramientas/' in u:
            priority = "0.8"
            changefreq = "monthly"
        else:
            priority = "0.7"
            changefreq = "monthly"
            
        entry = f"""  <url>
    <loc>{u}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>{changefreq}</changefreq>
    <priority>{priority}</priority>
  </url>"""
        entries.append(entry)

    sitemap_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{chr(10).join(entries)}
</urlset>
"""

    with open(SITEMAP_FILE, "w", encoding="utf-8") as f:
        f.write(sitemap_content)

    print(f"Sitemap XML actualizado exitosamente con {len(sorted_urls)} URLs indexadas.")

if __name__ == '__main__':
    update_full_sitemap()
