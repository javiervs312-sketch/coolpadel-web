with open('coolpadel-web/camaras/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

post = text[text.find('</main>') + 7:]

with open('coolpadel-web/post_es_clean.html', 'w', encoding='utf-8') as f:
    f.write(post)

print('Post length:', len(post))
