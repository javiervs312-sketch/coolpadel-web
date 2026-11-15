# -*- coding: utf-8 -*-
import glob

html_files = glob.glob('coolpadel-web/**/*.html', recursive=True)
for fpath in html_files:
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
        c = f.read()
    if '<meta name="robots" content="noindex' not in c and 'rel="alternate" hreflang=' not in c:
        print(fpath)
