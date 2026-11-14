#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
fix_seo_duplicates.py
Corrige canonicals y añade redirect JS en todas las páginas duplicadas (slug_es != slug_local).
También verifica hreflang en páginas canónicas.
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from paises_data_50 import COUNTRIES_50

CAMARAS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "camaras")
BASE_URL = "https://coolpadelstudios.com"

# Duplicados: países donde slug != slug_local
DUPLICATES = [(c['slug'], c['slug_local'], c['lang']) for c in COUNTRIES_50 if c['slug'] != c['slug_local']]

stats = {
    "canonical_already_ok": 0,
    "canonical_fixed": 0,
    "redirect_added": 0,
    "redirect_already_ok": 0,
    "hreflang_added": 0,
    "hreflang_already_ok": 0,
    "files_processed": 0,
}

def fix_duplicate_page(html_path, canonical_url, redirect_url):
    """Corrige canonical y añade redirect JS en página duplicada."""
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    changed = False

    # 1. Canonical
    canon_pattern = re.compile(r'<link\s+rel=["\']canonical["\']\s+href=["\']([^"\']+)["\'][^>]*/?\s*>', re.IGNORECASE)
    match = canon_pattern.search(content)
    if match:
        current_canonical = match.group(1)
        if current_canonical != canonical_url:
            content = canon_pattern.sub(f'<link rel="canonical" href="{canonical_url}">', content)
            stats["canonical_fixed"] += 1
            changed = True
            print(f"  [CANON FIX] {html_path}")
            print(f"    {current_canonical} → {canonical_url}")
        else:
            stats["canonical_already_ok"] += 1
    else:
        # No hay canonical, añadir después de <head>
        content = re.sub(r'(<head[^>]*>)', rf'\1\n  <link rel="canonical" href="{canonical_url}">', content, count=1, flags=re.IGNORECASE)
        stats["canonical_fixed"] += 1
        changed = True
        print(f"  [CANON ADD] {html_path}")

    # 2. Redirect JS: buscar si ya existe el redirect
    redirect_js = f'<script>window.location.replace("{redirect_url}");</script>'
    redirect_pattern = re.compile(r'<script>window\.location\.replace\(["\'][^"\']+["\']\);<\/script>', re.IGNORECASE)
    
    if redirect_pattern.search(content):
        # Verificar que apunta a la URL correcta
        existing = redirect_pattern.search(content)
        if redirect_url not in existing.group(0):
            content = redirect_pattern.sub(redirect_js, content)
            stats["redirect_added"] += 1
            changed = True
            print(f"  [REDIRECT FIX] {html_path}")
        else:
            stats["redirect_already_ok"] += 1
    else:
        # Añadir después de <body ...>
        body_pattern = re.compile(r'(<body[^>]*>)', re.IGNORECASE)
        if body_pattern.search(content):
            content = body_pattern.sub(rf'\1\n{redirect_js}', content, count=1)
            stats["redirect_added"] += 1
            changed = True
            print(f"  [REDIRECT ADD] {html_path}")

    if changed:
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(content)
    
    stats["files_processed"] += 1
    return changed


def fix_canonical_pages(hreflang_checks):
    """Verifica hreflang en páginas canónicas."""
    for c in COUNTRIES_50:
        slug_local = c['slug_local']
        lang = c['lang']
        canon_url = f"{BASE_URL}/camaras/{slug_local}/"
        
        index_path = os.path.join(CAMARAS_DIR, slug_local, "index.html")
        if not os.path.exists(index_path):
            continue
        
        with open(index_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        changed = False
        
        # Verificar hreflang lang
        lang_hreflang = f'<link rel="alternate" hreflang="{lang}" href="{canon_url}"/>'
        xdefault_hreflang = f'<link rel="alternate" hreflang="x-default" href="{canon_url}"/>'
        
        head_close = re.search(r'</head>', content, re.IGNORECASE)
        if not head_close:
            continue

        has_lang = bool(re.search(rf'hreflang=["\'{lang}["\']', content, re.IGNORECASE))
        has_xdefault = bool(re.search(r'hreflang=["\']x-default["\']', content, re.IGNORECASE))
        
        if not has_lang or not has_xdefault:
            inject = ""
            if not has_lang:
                inject += f'\n  {lang_hreflang}'
            if not has_xdefault:
                inject += f'\n  {xdefault_hreflang}'
            
            content = re.sub(r'(</head>)', rf'{inject}\1', content, count=1, flags=re.IGNORECASE)
            changed = True
            stats["hreflang_added"] += 1
            hreflang_checks.append({"slug_local": slug_local, "added": inject.strip()})
            print(f"  [HREFLANG ADD] {index_path}")
        else:
            stats["hreflang_already_ok"] += 1
        
        if changed:
            with open(index_path, 'w', encoding='utf-8') as f:
                f.write(content)


def main():
    print("=" * 70)
    print("FIX SEO DUPLICATES - CoolPadel Studios")
    print(f"Duplicados a procesar: {len(DUPLICATES)}")
    print("=" * 70)
    
    all_fixed = []
    
    for slug_es, slug_local, lang in DUPLICATES:
        slug_dir = os.path.join(CAMARAS_DIR, slug_es)
        if not os.path.isdir(slug_dir):
            print(f"[SKIP] Carpeta no existe: {slug_dir}")
            continue

        canonical_url = f"{BASE_URL}/camaras/{slug_local}/"
        redirect_url = canonical_url

        print(f"\n→ {slug_es}/ → canonical: {slug_local}/")

        # Página principal
        main_index = os.path.join(slug_dir, "index.html")
        if os.path.exists(main_index):
            changed = fix_duplicate_page(main_index, canonical_url, redirect_url)
            if changed:
                all_fixed.append(main_index)

        # Ciudades dentro del slug_es
        for city in os.listdir(slug_dir):
            city_dir = os.path.join(slug_dir, city)
            if os.path.isdir(city_dir):
                city_index = os.path.join(city_dir, "index.html")
                if os.path.exists(city_index):
                    # Canonical de ciudad → slug_local/{city}/
                    city_canonical = f"{BASE_URL}/camaras/{slug_local}/{city}/"
                    city_redirect = city_canonical
                    changed = fix_duplicate_page(city_index, city_canonical, city_redirect)
                    if changed:
                        all_fixed.append(city_index)

    print("\n" + "=" * 70)
    print("TAREA 3 — Verificar hreflang en páginas CANÓNICAS")
    print("=" * 70)
    hreflang_checks = []
    fix_canonical_pages(hreflang_checks)

    print("\n" + "=" * 70)
    print("RESUMEN FINAL")
    print("=" * 70)
    for k, v in stats.items():
        print(f"  {k}: {v}")
    print(f"\nArchivos modificados totales: {len(all_fixed)}")
    print(f"Hreflang issues corregidos: {len(hreflang_checks)}")
    
    return stats, all_fixed, hreflang_checks


if __name__ == "__main__":
    main()
