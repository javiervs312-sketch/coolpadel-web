import os
import re
from collections import Counter

headers_patterns = Counter()
files_with_header = []
files_without_header = []
files_by_lang = Counter()

for root, dirs, files in os.walk('coolpadel-web'):
    if '.git' in root:
        continue
    for f in files:
        if f.endswith('.html'):
            p = os.path.join(root, f).replace('\\', '/')
            with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
                c = fp.read()
            m = re.search(r'<header.*?</header>', c, re.DOTALL | re.IGNORECASE)
            if m:
                files_with_header.append(p)
                header_html = m.group(0)
                # find any link having llavero in text
                matches = re.findall(r'<a[^>]+href=["\']([^"\']+)["\'][^>]*>(?:(?!</a>).)*llavero(?:(?!</a>).)*</a>', header_html, re.IGNORECASE | re.DOTALL)
                headers_patterns[str(matches)] += 1
                
                # Check lang dropdown presence
                has_dropdown = 'id="lang-dropdown-container"' in header_html or 'lang-dropdown-menu' in header_html
                if not has_dropdown:
                    print(f"NO DROPDOWN: {p}")
            else:
                files_without_header.append(p)

print('Files with header:', len(files_with_header))
print('Files without header:', len(files_without_header), files_without_header)
print('Llaveros href patterns in header:')
for k, v in headers_patterns.items():
    print(f"  {k}: {v}")
