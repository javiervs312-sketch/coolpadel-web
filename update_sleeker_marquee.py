import os

clubs_dir = os.path.join(os.getcwd(), 'coolpadel-web', 'assets', 'images', 'Clubs')
logos = sorted([f for f in os.listdir(clubs_dir) if f.endswith('.png')])

def generate_sleek_logos(logo_list):
    items = []
    for l in logo_list:
        item = f'''        <div class="flex items-center justify-center shrink-0 px-4 sm:px-6 group">
          <img src="assets/images/Clubs/{l}" alt="Club Partner" class="h-13 sm:h-15 lg:h-18 w-auto max-w-[140px] sm:max-w-[190px] object-contain transition-all duration-300 hover:scale-110">
        </div>'''
        items.append(item)
    return '\n'.join(items)

sleek_logos_1 = generate_sleek_logos(logos)
sleek_logos_2 = generate_sleek_logos(logos)

new_text_and_marquee = f'''      <!-- TEXTO EN ZONA AZUL DEBAJO DE LAS FOTOS (SUBIDO Y PEGADO AL CAROUSEL) -->
      <div class="mt-2 sm:mt-3 mb-1 text-center px-4">
        <p class="text-base sm:text-lg lg:text-xl font-heading font-black uppercase tracking-widest text-white">
          Trabajamos con clubs, marcas y federaciones de tenis y padel de todo el mundo
        </p>
      </div>

    </div>
  </section>

  <!-- 4. CARROUSEL PASARELA CLUBS (FONDO BLANCO ESTRECHO Y ELEGANTE) -->
  <section class="py-4 sm:py-5 lg:py-6 bg-white border-y border-slate-200 overflow-hidden shadow-sm">
    <div class="ticker-wrap py-1">
      <div class="ticker-content animate-ticker-trusted flex items-center gap-8 sm:gap-12 lg:gap-14">
{sleek_logos_1}
        <!-- DUPLICATE FOR INFINITE LOOP -->
{sleek_logos_2}
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
    html = html[:start_idx] + new_text_and_marquee + '\n\n  ' + html[end_idx:]
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print('Updated: letters moved up, pasarela made narrower!')
else:
    print('Markers not found')
