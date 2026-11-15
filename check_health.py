# -*- coding: utf-8 -*-
import glob

html_files = glob.glob('coolpadel-web/**/*.html', recursive=True)
print(f'Total HTML files: {len(html_files)}')

dup_ga4 = 0
dup_clarity = 0
no_hreflang = 0

for fpath in html_files:
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
        c = f.read()
    if 'G-TR5418F4F2' in c and c.count('G-TR5418F4F2') > 2:
        dup_ga4 += 1
    if 'rcto45p2i6' in c and c.count('rcto45p2i6') > 1:
        dup_clarity += 1
    if '<meta name="robots" content="noindex' not in c:
        if 'rel="alternate" hreflang=' not in c:
            no_hreflang += 1

print(f'Duplicates GA4: {dup_ga4}')
print(f'Duplicates Clarity: {dup_clarity}')
print(f'Indexable pages without hreflang: {no_hreflang}')
