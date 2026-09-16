import os

clubs_dir = os.path.join(os.getcwd(), 'coolpadel-web', 'assets', 'images', 'Clubs')
logos = sorted([f for f in os.listdir(clubs_dir) if f.endswith('.png')])

def generate_free_logos(logo_list):
    items = []
    for l in logo_list:
        item = f'''        <div class="flex items-center justify-center shrink-0 px-3 sm:px-5 group">
          <img src="assets/images/Clubs/{l}" alt="Club Partner" class="h-12 sm:h-14 lg:h-16 w-auto max-w-[130px] sm:max-w-[170px] object-contain opacity-85 hover:opacity-100 transition-all duration-300 hover:scale-105 filter brightness-105">
        </div>'''
        items.append(item)
    return '\n'.join(items)

free_logos_1 = generate_free_logos(logos)
free_logos_2 = generate_free_logos(logos)

new_marquee = f'''      <div class="ticker-content animate-ticker-trusted flex items-center gap-8 sm:gap-12 lg:gap-14 py-2">
{free_logos_1}
        <!-- DUPLICATE FOR INFINITE LOOP -->
{free_logos_2}
      </div>'''

index_path = os.path.join(os.getcwd(), 'coolpadel-web', 'index.html')
with open(index_path, 'r', encoding='utf-8') as f:
    html = f.read()

start_str = '<div class="ticker-content animate-ticker-trusted'
end_str = '<!-- 5. SECCIÓN DETALLADA: LLAVEROS PARA CLUBS -->'

start_idx = html.find(start_str)
end_idx = html.find(end_str)

if start_idx != -1 and end_idx != -1:
    section_end_str = '</section>'
    actual_end_idx = html.rfind(section_end_str, start_idx, end_idx) + len(section_end_str)
    replacement = f'''{new_marquee}
    </div>
  </section>'''
    html = html[:start_idx] + replacement + '\n\n  ' + html[end_idx:]
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'Updated index.html: logos are now free (no boxes) and larger!')
else:
    print('Markers not found')
