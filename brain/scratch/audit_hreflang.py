#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Auditoría hreflang y canonicals de coolpadel-web."""
import os
import re
import sys

base = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
web_dir = os.path.join(base, 'coolpadel-web')

html_files = []
for root, dirs, files in os.walk(web_dir):
    dirs[:] = [d for d in dirs if d not in ['node_modules', '__pycache__', '.git', 'assets']]
    for f in files:
        if f.endswith('.html'):
            html_files.append(os.path.join(root, f))

print(f'Total HTML files: {len(html_files)}')

with_hreflang = 0
without_hreflang = 0
with_canonical = 0
pages_no_hreflang = []

for filepath in html_files:
    try:
        with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
            content = f.read(8000)
        has_hreflang = 'hreflang' in content.lower()
        has_canonical = 'canonical' in content.lower()
        if has_hreflang:
            with_hreflang += 1
        else:
            without_hreflang += 1
            rel_path = filepath.replace(web_dir + os.sep, '').replace(web_dir + '/', '')
            pages_no_hreflang.append(rel_path)
        if has_canonical:
            with_canonical += 1
    except Exception as e:
        pass

print(f'Con hreflang: {with_hreflang}')
print(f'Sin hreflang: {without_hreflang}')
print(f'Con canonical: {with_canonical}')
print('Muestra sin hreflang (primeras 30):')
for p in sorted(pages_no_hreflang)[:30]:
    print(f'  {p}')

# Check canonical en country pages
print('\n--- Canonicals de paginas de paises (camaras/) ---')
camaras_dir = os.path.join(web_dir, 'camaras')
test_paises = ['espana', 'france', 'italia', 'deutschland', 'nederland', 'argentina', 'alemania', 'francia']
for p in test_paises:
    idx = os.path.join(camaras_dir, p, 'index.html')
    if os.path.exists(idx):
        try:
            with open(idx, 'r', encoding='utf-8', errors='replace') as f:
                content = f.read(5000)
            m = re.search(r'<link[^>]+rel=["\']canonical["\'][^>]*href=["\']([^"\']+)["\']', content, re.IGNORECASE)
            if not m:
                m = re.search(r'<link[^>]+href=["\']([^"\']+)["\'][^>]*rel=["\']canonical["\']', content, re.IGNORECASE)
            canon = m.group(1) if m else 'NO CANONICAL'
            print(f'  {p:<25} canonical={canon}')
        except Exception as e:
            print(f'  {p:<25} ERROR: {e}')
    else:
        print(f'  {p:<25} NO EXISTS')

# Verificar hreflang del sitemap vs HTML
print('\n--- Verificando sitemap (primeras lineas) ---')
sitemap_path = os.path.join(web_dir, 'sitemap.xml')
if os.path.exists(sitemap_path):
    with open(sitemap_path, 'r', encoding='utf-8') as f:
        sitemap_content = f.read()
    urls = re.findall(r'<loc>([^<]+)</loc>', sitemap_content)
    print(f'URLs en sitemap: {len(urls)}')
    # Contar por sección
    camaras_urls = [u for u in urls if '/camaras/' in u]
    blog_urls = [u for u in urls if '/blog/' in u]
    lang_urls = [u for u in urls if '/en/' in u or '/fr/' in u or '/it/' in u or '/de/' in u]
    print(f'  URLs /camaras/: {len(camaras_urls)}')
    print(f'  URLs /blog/: {len(blog_urls)}')
    print(f'  URLs lang (en/fr/it/de): {len(lang_urls)}')
    print('  Muestra URLs camaras:')
    for u in camaras_urls[:15]:
        print(f'    {u}')
