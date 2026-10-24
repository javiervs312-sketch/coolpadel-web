import re

with open('coolpadel-web/head_es.html', 'r', encoding='utf-8') as f:
    h_es = f.read()
with open('coolpadel-web/head_it.html', 'r', encoding='utf-8') as f:
    h_it = f.read()

# Compare styles
style_es = re.search(r'<style>(.*?)</style>', h_es, re.DOTALL).group(1)
style_it = re.search(r'<style>(.*?)</style>', h_it, re.DOTALL).group(1)

with open('coolpadel-web/style_es.css', 'w', encoding='utf-8') as f:
    f.write(style_es)
with open('coolpadel-web/style_it.css', 'w', encoding='utf-8') as f:
    f.write(style_it)

# Check what classes exist in ES that don't exist in IT
es_classes = set(re.findall(r'\.([a-zA-Z0-9_-]+)\s*\{', style_es))
it_classes = set(re.findall(r'\.([a-zA-Z0-9_-]+)\s*\{', style_it))

print('Classes in ES but not in IT:', es_classes - it_classes)

with open('coolpadel-web/post_es.html', 'r', encoding='utf-8') as f:
    p_es = f.read()
with open('coolpadel-web/post_it.html', 'r', encoding='utf-8') as f:
    p_it = f.read()

print('Scripts in ES:', re.findall(r'<script.*?</script>', p_es, re.DOTALL))
