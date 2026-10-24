import re
import os

with open('coolpadel-web/camaras/index.html', 'r', encoding='utf-8') as f:
    text_es = f.read()

with open('coolpadel-web/it/camaras/index.html', 'r', encoding='utf-8') as f:
    text_it = f.read()

# Let's inspect differences in <head> and scripts
head_es = text_es[:text_es.find('<main>')]
head_it = text_it[:text_it.find('<main>')]
post_es = text_es[text_es.find('</main>') + 7:]
post_it = text_it[text_it.find('</main>') + 7:]

print('ES head len:', len(head_es))
print('IT head len:', len(head_it))
print('ES post len:', len(post_es))
print('IT post len:', len(post_it))

with open('coolpadel-web/head_es.html', 'w', encoding='utf-8') as f:
    f.write(head_es)
with open('coolpadel-web/head_it.html', 'w', encoding='utf-8') as f:
    f.write(head_it)
with open('coolpadel-web/post_es.html', 'w', encoding='utf-8') as f:
    f.write(post_es)
with open('coolpadel-web/post_it.html', 'w', encoding='utf-8') as f:
    f.write(post_it)
