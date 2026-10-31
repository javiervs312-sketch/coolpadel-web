import glob

for s in glob.glob('coolpadel-web/*.py'):
    with open(s, 'r', encoding='utf-8', errors='ignore') as f:
        c = f.read()
    has_click = 'toggleLangDropdown(' in c
    has_def = 'function toggleLangDropdown' in c
    if has_click or has_def:
        print(f"{s}: has_click={has_click}, has_def={has_def}")
