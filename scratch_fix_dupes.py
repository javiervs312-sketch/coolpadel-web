# -*- coding: utf-8 -*-
"""
Fix SEO: Corrige canonicals y añade redirect JS en las 28 carpetas duplicadas (slug_es).
Para cada país donde slug != slug_local, la carpeta slug_es es la duplicada.
"""
import os, re, sys

sys.path.insert(0, os.path.dirname(__file__))
from paises_data_50 import COUNTRIES_50

CAMARAS_ROOT = os.path.join(os.path.dirname(__file__), "camaras")
BASE_URL = "https://coolpadelstudios.com"

# Los 28 duplicados: slug_es -> slug_local
DUPES = [(c["slug"], c["slug_local"], c["lang"])
         for c in COUNTRIES_50 if c["slug"] != c["slug_local"]]

REDIRECT_TEMPLATE = '<script>window.location.replace("{url}");</script>'
CANONICAL_RE = re.compile(r'<link\s+rel=["\']canonical["\']\s+href=["\']([^"\']+)["\']', re.IGNORECASE)
BODY_RE = re.compile(r'(<body[^>]*>)', re.IGNORECASE)
HEAD_CLOSE_RE = re.compile(r'(</head>)', re.IGNORECASE)

fixed_pages = []
already_ok = []
errors = []

def fix_html_file(filepath, canonical_url, redirect_url):
    """Asegura canonical correcto + redirect JS en el body."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        errors.append(f"ERROR leyendo {filepath}: {e}")
        return False

    changed = False

    # 1. Corregir/añadir canonical
    canon_match = CANONICAL_RE.search(content)
    if canon_match:
        current_canon = canon_match.group(1).rstrip("/") + "/"
        if current_canon != canonical_url:
            content = CANONICAL_RE.sub(
                f'<link rel="canonical" href="{canonical_url}"', content)
            changed = True
    else:
        # Insertar antes de </head>
        new_canon = f'<link rel="canonical" href="{canonical_url}">\n'
        content = HEAD_CLOSE_RE.sub(new_canon + r'\1', content, count=1)
        changed = True

    # 2. Añadir redirect JS si no existe ya
    redirect_script = REDIRECT_TEMPLATE.format(url=redirect_url)
    if redirect_script not in content:
        body_match = BODY_RE.search(content)
        if body_match:
            insert_pos = body_match.end()
            content = content[:insert_pos] + "\n" + redirect_script + "\n" + content[insert_pos:]
            changed = True
        else:
            errors.append(f"No se encontró <body> en {filepath}")

    if changed:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        return True
    return False

total_fixed = 0
total_ok = 0

for slug_es, slug_local, lang in DUPES:
    country_folder = os.path.join(CAMARAS_ROOT, slug_es)
    if not os.path.isdir(country_folder):
        print(f"  [SKIP] {slug_es}/ no existe en disco")
        continue

    canonical_country = f"{BASE_URL}/camaras/{slug_local}/"
    redirect_country = canonical_country

    # Procesar index.html de la carpeta país
    idx = os.path.join(country_folder, "index.html")
    if os.path.exists(idx):
        if fix_html_file(idx, canonical_country, redirect_country):
            fixed_pages.append(f"camaras/{slug_es}/index.html -> canonical={canonical_country}")
            total_fixed += 1
            print(f"  [FIX] camaras/{slug_es}/ -> {slug_local}")
        else:
            total_ok += 1
            print(f"  [OK]  camaras/{slug_es}/ ya correcto")

    # Procesar subcarpetas de ciudades
    for item in os.listdir(country_folder):
        city_folder = os.path.join(country_folder, item)
        city_idx = os.path.join(city_folder, "index.html")
        if os.path.isdir(city_folder) and os.path.exists(city_idx):
            canonical_city = f"{BASE_URL}/camaras/{slug_local}/{item}/"
            redirect_city = canonical_city
            if fix_html_file(city_idx, canonical_city, redirect_city):
                fixed_pages.append(f"camaras/{slug_es}/{item}/index.html -> canonical={canonical_city}")
                total_fixed += 1
            else:
                total_ok += 1

print(f"\n{'='*60}")
print(f"RESUMEN:")
print(f"  Páginas corregidas: {total_fixed}")
print(f"  Páginas ya OK: {total_ok}")
print(f"  Errores: {len(errors)}")
if errors:
    for e in errors:
        print(f"  ERROR: {e}")

# Guardar log
with open("../scratch_fix_log.txt", "w", encoding="utf-8") as f:
    f.write(f"PAGES FIXED ({total_fixed}):\n")
    for p in fixed_pages:
        f.write(f"  {p}\n")
    if errors:
        f.write(f"\nERRORS ({len(errors)}):\n")
        for e in errors:
            f.write(f"  {e}\n")

print(f"\nLog guardado en scratch_fix_log.txt")
