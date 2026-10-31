import os, time
from collections import Counter

t0 = time.time()
html_files = []
for root, dirs, files in os.walk('coolpadel-web'):
    if '.git' in root or 'node_modules' in root:
        continue
    for f in files:
        if f.endswith('.html'):
            html_files.append(os.path.join(root, f))

llaveros_hrefs = Counter()
has_header = 0
no_header = []
dropdown_counts = Counter()

for p in html_files:
    try:
        with open(p, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
    except Exception as e:
        continue
    
    # Extract header
    h_idx = content.find('<header')
    if h_idx != -1:
        h_end = content.find('</header>', h_idx)
        if h_end != -1:
            header = content[h_idx:h_end+9]
            has_header += 1
            
            # Check llaveros link
            lower_h = header.lower()
            ll_pos = lower_h.find('llavero')
            if ll_pos != -1:
                a_pos = lower_h.rfind('<a', 0, ll_pos)
                if a_pos != -1:
                    href_start = lower_h.find('href=', a_pos)
                    if href_start != -1 and href_start < ll_pos:
                        quote = header[href_start+5]
                        if quote in ('"', "'"):
                            quote_end = header.find(quote, href_start+6)
                            href = header[href_start+6:quote_end]
                        else:
                            href = header[href_start+5:].split()[0].replace('>', '')
                        llaveros_hrefs[href] += 1
            else:
                llaveros_hrefs['NONE'] += 1
                
            # Check dropdown
            if 'id="lang-dropdown-btn"' in header or 'id="lang-dropdown-container"' in header:
                dropdown_counts['has_dropdown'] += 1
            else:
                dropdown_counts['no_dropdown'] += 1
        else:
            no_header.append(p)
    else:
        no_header.append(p)

print(f"Done in {time.time()-t0:.2f}s")
print(f"Total HTML: {len(html_files)}")
print(f"Has header: {has_header}, No header: {len(no_header)}")
print("No header files:", [p.replace('coolpadel-web\\', '') for p in no_header])
print("\nLlaveros href counts:")
for k, v in llaveros_hrefs.most_common():
    print(f"  {k}: {v}")
print("\nDropdown counts:")
for k, v in dropdown_counts.items():
    print(f"  {k}: {v}")
