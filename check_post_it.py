with open('coolpadel-web/it/camaras/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

post = text[text.find('</main>') + 7:]

with open('coolpadel-web/post_it_clean.html', 'w', encoding='utf-8') as f:
    f.write(post)

print('IT Post length:', len(post))
