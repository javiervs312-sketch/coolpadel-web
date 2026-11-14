# -*- coding: utf-8 -*-
"""
SEO Fixer Script
TAREA 2: Fix canonical + add JS redirect in dupe pages
TAREA 3: Add hreflang in canonical pages
"""
import os, re, sys

BASE = os.path.dirname(os.path.abspath(__file__))
CAMARAS = os.path.join(BASE, 'camaras')

DUPES = [
    # (slug_es, slug_local, lang)
    ('suecia','sverige','sv'),
    ('francia','france','fr'),
    ('paises-bajos','nederland','nl'),
    ('belgica','belgique','fr'),
    ('dinamarca','danmark','da'),
    ('egipto','egypt','ar'),
    ('sudafrica','south-africa','en'),
    ('arabia-saudi','saudi-arabia','ar'),
    ('finlandia','suomi','fi'),
    ('gran-bretana','united-kingdom','en'),
    ('emiratos-arabes-unidos','uae','ar'),
    ('alemania','deutschland','de'),
    ('estados-unidos','united-states','en'),
    ('noruega','norge','no'),
    ('austria','oesterreich','de'),
    ('suiza','schweiz','de'),
    ('polonia','polska','pl'),
    ('grecia','ellada','el'),
    ('croacia','hrvatska','hr'),
    ('marruecos','maroc','fr'),
    ('irlanda','ireland','en'),
    ('turquia','turkiye','tr'),
    ('tunez','tunisie','fr'),
    ('japon','japan','ja'),
    ('libano','lebanon','ar'),
    ('bahrein','bahrain','ar'),
    ('republica-checa','ceska-republika','cs'),
    ('rumania','romania','ro'),
]

changes = []

# ── TAREA 2: Fix dupe pages ──────────────────────────────────────────────────
print("=== TAREA 2: Fixing duplicate pages ===")
for slug, local, lang in DUPES:
    idx_path = os.path.join(CAMARAS, slug, 'index.html')
    if not os.path.isfile(idx_path):
        print(f"  SKIP (no file): {slug}")
        continue

    with open(idx_path, 'r', encoding='utf-8') as f:
        content = f.read()

    correct_canon = f"https://coolpadelstudios.com/camaras/{local}/"
    js_redirect = f'<script>window.location.replace("{correct_canon}");</script>'

    # Check current canonical
    canon_match = re.search(r'<link rel="canonical" href="([^"]+)"', content)
    current_canon = canon_match.group(1) if canon_match else None

    modified = False

    # Fix canonical if wrong
    if current_canon != correct_canon:
        if current_canon:
            content = content.replace(
                f'<link rel="canonical" href="{current_canon}">',
                f'<link rel="canonical" href="{correct_canon}">'
            )
        else:
            # Insert before </head>
            content = content.replace('</head>', f'  <link rel="canonical" href="{correct_canon}">\n</head>')
        changes.append(f'[DUPE] Fixed canonical: {slug} -> {correct_canon}')
        modified = True
        print(f"  FIXED canonical: {slug} ({current_canon} -> {correct_canon})")
    else:
        print(f"  OK canonical: {slug}")

    # Add JS redirect if missing
    if 'window.location.replace' not in content:
        # Insert at start of body
        content = content.replace('<body', f'{js_redirect}\n<body', 1)
        changes.append(f'[DUPE] Added JS redirect: {slug} -> {correct_canon}')
        modified = True
        print(f"  ADDED jsredir: {slug}")
    else:
        print(f"  OK jsredir: {slug}")

    # Also fix meta robots - duplicate pages should still be indexable but canonical tells Google
    # Also fix robots content attribute to noindex for duplicate page
    robots_match = re.search(r'<meta name="robots" content="([^"]+)"', content)
    if robots_match and 'noindex' not in robots_match.group(1):
        content = content.replace(
            f'<meta name="robots" content="{robots_match.group(1)}">',
            '<meta name="robots" content="noindex, follow">'
        )
        changes.append(f'[DUPE] Set noindex: {slug}')
        modified = True
        print(f"  SET noindex: {slug}")

    if modified:
        with open(idx_path, 'w', encoding='utf-8') as f:
            f.write(content)

print()

# ── TAREA 3: Verify/fix hreflang in canonical pages ─────────────────────────
print("=== TAREA 3: Fixing hreflang in canonical pages ===")
for slug, local, lang in DUPES:
    idx_path = os.path.join(CAMARAS, local, 'index.html')
    if not os.path.isfile(idx_path):
        print(f"  SKIP (no file): {local}")
        continue

    with open(idx_path, 'r', encoding='utf-8') as f:
        content = f.read()

    canon_url = f"https://coolpadelstudios.com/camaras/{local}/"
    hreflang_lang = f'<link rel="alternate" hreflang="{lang}" href="{canon_url}"/>'
    hreflang_xdef = f'<link rel="alternate" hreflang="x-default" href="{canon_url}"/>'

    has_hreflang = 'hreflang=' in content
    modified = False

    if not has_hreflang:
        # Insert before </head>
        insert_block = f'  {hreflang_lang}\n  {hreflang_xdef}\n'
        content = content.replace('</head>', insert_block + '</head>')
        changes.append(f'[CANON] Added hreflang: {local} (lang={lang})')
        modified = True
        print(f"  ADDED hreflang: {local}")
    else:
        # Check if correct lang is present
        if f'hreflang="{lang}"' not in content:
            content = content.replace('</head>', f'  {hreflang_lang}\n</head>')
            changes.append(f'[CANON] Added hreflang lang tag: {local} (lang={lang})')
            modified = True
            print(f"  ADDED missing lang hreflang: {local}")
        if 'hreflang="x-default"' not in content:
            content = content.replace('</head>', f'  {hreflang_xdef}\n</head>')
            changes.append(f'[CANON] Added hreflang x-default: {local}')
            modified = True
            print(f"  ADDED missing x-default hreflang: {local}")
        if not modified:
            print(f"  OK hreflang: {local}")

    if modified:
        with open(idx_path, 'w', encoding='utf-8') as f:
            f.write(content)

print()
print(f"=== TOTAL CHANGES: {len(changes)} ===")
for c in changes:
    print(f"  {c}")

# Save changes list for report
with open(os.path.join(BASE, '_seo_changes.txt'), 'w', encoding='utf-8') as f:
    f.write('\n'.join(changes))

print("\nDone. Changes saved to _seo_changes.txt")
