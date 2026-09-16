import os

clubs_dir = os.path.join(os.getcwd(), 'coolpadel-web', 'assets', 'images', 'Clubs')
logos = sorted([f for f in os.listdir(clubs_dir) if f.endswith('.png')])

def generate_compact_logos(logo_list):
    items = []
    for l in logo_list:
        item = f'''        <div class="flex items-center justify-center shrink-0 px-4 sm:px-6 group">
          <img src="assets/images/Clubs/{l}" alt="Club Partner" class="h-14 sm:h-16 lg:h-20 w-auto max-w-[150px] sm:max-w-[195px] object-contain transition-all duration-300 hover:scale-110">
        </div>'''
        items.append(item)
    return '\n'.join(items)

logos_1 = generate_compact_logos(logos)
logos_2 = generate_compact_logos(logos)

previous_text_and_marquee = f'''      <!-- TEXTO EN ZONA AZUL DEBAJO DE LAS FOTOS -->
      <div class="mt-6 sm:mt-8 text-center px-4">
        <p class="text-sm sm:text-base lg:text-lg font-heading font-extrabold uppercase tracking-widest text-white/95">
          Trabajamos con clubs, marcas y federaciones de tenis y padel de todo el mundo
        </p>
      </div>

    </div>
  </section>

  <!-- 4. CARROUSEL PASARELA CLUBS (FONDO BLANCO ULTRA-ESTRECHO SOLO LOGOS) -->
  <section class="py-3 sm:py-4 bg-white border-y border-slate-200 overflow-hidden shadow-sm">
    <div class="ticker-wrap py-1">
      <div class="ticker-content animate-ticker-trusted flex items-center gap-8 sm:gap-12 lg:gap-14">
{logos_1}
        <!-- DUPLICATE FOR INFINITE LOOP -->
{logos_2}
      </div>
    </div>
  </section>'''

index_path = os.path.join(os.getcwd(), 'coolpadel-web', 'index.html')
with open(index_path, 'r', encoding='utf-8') as f:
    html = f.read()

start_marker = '<!-- TEXTO EN ZONA AZUL DEBAJO DE LAS FOTOS'
end_marker = '<!-- 5. SECCIÓN DETALLADA: LLAVEROS PARA CLUBS -->'

start_idx = html.find(start_marker)
end_idx = html.find(end_marker)

if start_idx != -1 and end_idx != -1:
    html = html[:start_idx] + previous_text_and_marquee + '\n\n  ' + html[end_idx:]
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print('Restored previous version successfully.')
else:
    print('Markers not found')
