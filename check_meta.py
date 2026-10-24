import re

with open('coolpadel-web/camaras/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

head = text[:text.find('<main>')]

# Title & Meta
title = re.search(r'<title>(.*?)</title>', head, re.DOTALL)
desc = re.search(r'<meta name="description" content="(.*?)">', head, re.DOTALL)
og_title = re.search(r'<meta property="og:title" content="(.*?)">', head, re.DOTALL)
og_desc = re.search(r'<meta property="og:description" content="(.*?)">', head, re.DOTALL)

print('Title:', title.group(1) if title else '')
print('Desc:', desc.group(1) if desc else '')
print('OG Title:', og_title.group(1) if og_title else '')
print('OG Desc:', og_desc.group(1) if og_desc else '')
