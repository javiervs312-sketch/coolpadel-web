# -*- coding: utf-8 -*-
with open('coolpadel-web/generate_master_sitemap.py', 'r', encoding='utf-8') as f:
    code = f.read()

old_block = """    # 4c. 50 Landings de Países de Cámaras Save My Play
    try:
        from paises_data import COUNTRIES
        for c in COUNTRIES:
            all_blocks.append(get_single_xml(f"/camaras/{c['slug']}/", priority="0.95", changefreq="weekly"))
    except Exception as e:
        print(f"Error adding country landings to sitemap: {e}")"""

new_block = """    # 4c. 50 Landings de Países de Cámaras Save My Play (78 slugs únicos)
    try:
        from paises_data_50 import COUNTRIES_50
        seen_slugs = set()
        for item in COUNTRIES_50:
            for s in [item.get('slug'), item.get('slug_local')]:
                if s and s not in seen_slugs:
                    seen_slugs.add(s)
                    all_blocks.append(get_single_xml(f"/camaras/{s}/", priority="0.95", changefreq="weekly"))
        print(f"Added {len(seen_slugs)} country slugs to sitemap.")
    except Exception as e:
        print(f"Error adding country landings to sitemap: {e}")"""

code_norm = code.replace('\r\n', '\n')
old_norm = old_block.replace('\r\n', '\n')
if old_norm in code_norm:
    code_norm = code_norm.replace(old_norm, new_block, 1)
    with open('coolpadel-web/generate_master_sitemap.py', 'w', encoding='utf-8') as f:
        f.write(code_norm)
    print("SUCCESSFULLY UPDATED generate_master_sitemap.py")
else:
    print("old_norm NOT FOUND")
