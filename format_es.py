import re

with open('coolpadel-web/camaras/index.html', 'r', encoding='utf-8') as f:
    text_es = f.read()

clean_es = re.sub(r'\n\s*\n\s*\n+', '\n\n', text_es)
with open('coolpadel-web/camaras/index.html', 'w', encoding='utf-8') as f:
    f.write(clean_es)

print('Cleaned ES! Lines:', len(clean_es.splitlines()))
