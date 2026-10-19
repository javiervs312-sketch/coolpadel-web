import glob
import re
import json

files = glob.glob('coolpadel-web/**/*.html', recursive=True)
print(f"Total HTML files scanned: {len(files)}")

over_titles = []
over_descs = []
schemas_valid = 0
schemas_with_rating = 0

for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    
    # Title check
    t_match = re.search(r'<title>(.*?)</title>', c, re.IGNORECASE | re.DOTALL)
    if t_match:
        t = t_match.group(1).strip()
        if len(t) > 60:
            over_titles.append((f, len(t), t))
            
    # Meta desc check
    d_match = re.search(r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']', c, re.IGNORECASE | re.DOTALL)
    if d_match:
        d = d_match.group(1).strip()
        if len(d) > 156:
            over_descs.append((f, len(d), d))
            
    # JSON-LD Schema
    for ld in re.findall(r'<script\s+type=["\']application/ld\+json["\']>(.*?)</script>', c, re.DOTALL):
        try:
            parsed = json.loads(ld)
            schemas_valid += 1
            if 'aggregateRating' in ld:
                schemas_with_rating += 1
        except Exception as err:
            print(f"JSON-LD error in {f}: {err}")

print(f"Titles > 60 characters: {len(over_titles)}")
for item in over_titles:
    print(f"  [TITLE > 60] {item[0]} ({item[1]} chars): {item[2]}")

print(f"Descriptions > 156 characters: {len(over_descs)}")
for item in over_descs:
    print(f"  [DESC > 156] {item[0]} ({item[1]} chars): {item[2]}")

print(f"Total JSON-LD schemas parsed without error: {schemas_valid}")
print(f"Total pages with AggregateRating (review stars): {schemas_with_rating}")
