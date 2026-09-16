import os

clubs_dir = os.path.join(os.getcwd(), 'coolpadel-web', 'assets', 'images', 'Clubs')
logos = sorted([f for f in os.listdir(clubs_dir) if f.endswith('.png')])

def generate_grand_logos(logo_list):
    items = []
    for l in logo_list:
        item = f'''        <div class="flex items-center justify-center shrink-0 px-4 sm:px-6 group">
          <img src="assets/images/Clubs/{l}" alt="Club Partner" class="h-16 sm:h-20 lg:h-24 w-auto max-w-[160px] sm:max-w-[220px] object-contain transition-all duration-300 hover:scale-110">
        </div>'''
        items.append(item)
    return '\n'.join(items)

grand_logos_1 = generate_grand_logos(logos)
grand_logos_2 = generate_grand_logos(logos)

new_text_and_marquee = f'''      <!-- TEXTO EN ZONA AZUL DEBAJO DE LAS FOTOS (MÁS GRANDE Y ELEVADO) -->
      <div class="mt-8 sm:mt-10 mb-2 text-center px-4">
        <p class="text-base sm:text-lg lg:text-xl font-heading font-black uppercase tracking-widest text-white">
          Trabajamos con clubs, marcas y federaciones de tenis y padel de todo el mundo
        </p>
      </div>

    </div>
  </section>

  <!-- 4. CARROUSEL PASARELA CLUBS (FONDO BLANCO AMPLIADO HASTA ABAJO DE PANTALLA) -->
  <section class="py-7 sm:py-9 lg:py-12 bg-white border-y border-slate-200 overflow-hidden shadow-sm">
    <div class="ticker-wrap py-2">
      <div class="ticker-content animate-ticker-trusted flex items-center gap-10 sm:gap-14 lg:gap-16">
{grand_logos_1}
        <!-- DUPLICATE FOR INFINITE LOOP -->
{grand_logos_2}
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
    print('Updated: text is larger & higher, white strip is wider and fills viewport!')
else:
    print('Markers not found')
