import os

with open('coolpadel-web/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

template = f"""import os

def build_larger_coverflow_site():
    html = {repr(content)}
    out_file = os.path.join(os.getcwd(), "coolpadel-web", "index.html")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(html)
    print("Site generated successfully.")

if __name__ == "__main__":
    build_larger_coverflow_site()
"""

with open('coolpadel-web/build_larger_coverflow.py', 'w', encoding='utf-8') as f:
    f.write(template)

print('Build script synced with 100% fidelity.')
