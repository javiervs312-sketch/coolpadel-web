import os

clubs_dir = os.path.join(os.getcwd(), 'coolpadel-web', 'assets', 'images', 'Clubs')
logos = sorted([f for f in os.listdir(clubs_dir) if f.endswith('.png')])

def generate_larger_free_logos(logo_list):
    items = []
    for l in logo_list:
        item = f'''        <div class="flex items-center justify-center shrink-0 px-4 sm:px-6 group">
          <img src="assets/images/Clubs/{l}" alt="Club Partner" class="h-14 sm:h-16 lg:h-20 w-auto max-w-[150px] sm:max-w-[195px] object-contain transition-all duration-300 hover:scale-110">
        </div>'''
        items.append(item)
    return '\n'.join(items)

free_logos_1 = generate_larger_free_logos(logos)
free_logos_2 = generate_larger_free_logos(logos)

new_section = f'''  <!-- 4. CARROUSEL PASARELA CLUBS (FONDO BLANCO ESTRECHO) -->
  <section class="py-4 sm:py-5 bg-white border-y border-slate-200 overflow-hidden text-slate-900 shadow-sm">
    <div class="max-w-7xl mx-auto px-4 mb-2 text-center">
      <p class="text-xs sm:text-sm font-heading font-extrabold uppercase tracking-widest text-slate-800">
        Clubs, marcas y federaciones de tenis y pádel de todo el mundo
      </p>
    </div>

    <div class="ticker-wrap py-1">
      <div class="ticker-content animate-ticker-trusted flex items-center gap-8 sm:gap-12 lg:gap-14">
{free_logos_1}
        <!-- DUPLICATE FOR INFINITE LOOP -->
{free_logos_2}
      </div>
    </div>
  </section>'''

index_path = os.path.join(os.getcwd(), 'coolpadel-web', 'index.html')
with open(index_path, 'r', encoding='utf-8') as f:
    html = f.read()

start_marker = '<!-- 4. CARROUSEL PASARELA'
end_marker = '<!-- 5. SECCIÓN DETALLADA: LLAVEROS PARA CLUBS -->'

start_idx = html.find(start_marker)
end_idx = html.find(end_marker)

if start_idx != -1 and end_idx != -1:
    html = html[:start_idx] + new_section + '\n\n  ' + html[end_idx:]
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print('Updated pasarela with white background, narrower strip, 15% larger logos, and larger header text!')
else:
    print('Markers not found')
