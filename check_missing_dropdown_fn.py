import os
import re

files_with_btn = []
files_missing_toggle = []
files_missing_click_listener = []

for root, dirs, files in os.walk('coolpadel-web'):
    if '.git' in root or 'node_modules' in root:
        continue
    for f in files:
        if f.endswith('.html'):
            p = os.path.join(root, f)
            with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
                c = fp.read()
            if 'lang-dropdown-btn' in c or 'lang-dropdown-container' in c:
                files_with_btn.append(p)
                if 'toggleLangDropdown' not in c:
                    files_missing_toggle.append(p)

print(f"Total files with dropdown button: {len(files_with_btn)}")
print(f"Total files missing toggleLangDropdown: {len(files_missing_toggle)}")
if files_missing_toggle:
    print("Sample missing:", [p.replace('coolpadel-web\\', '') for p in files_missing_toggle[:20]])
