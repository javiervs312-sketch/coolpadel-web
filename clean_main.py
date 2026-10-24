import re

with open('coolpadel-web/camaras_main_es.html', 'r', encoding='utf-8') as f:
    main_es = f.read()

# Let's clean multiple empty lines to see the text clearly
clean_lines = []
for line in main_es.splitlines():
    l = line.strip()
    if l:
        clean_lines.append(l)

with open('coolpadel-web/camaras_es_clean.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(clean_lines))

print('Clean lines count:', len(clean_lines))
