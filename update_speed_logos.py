import os

clubs_dir = os.path.join(os.getcwd(), 'coolpadel-web', 'assets', 'images', 'Clubs')
logos = sorted([f for f in os.listdir(clubs_dir) if f.endswith('.png')])

def generate_faster_larger_logos(logo_list):
    items = []
    for l in logo_list:
        item = f'''        <div class="flex items-center justify-center shrink-0 px-4 sm:px-6 group">
          <img src="assets/images/Clubs/{l}" alt="Club Partner" class="h-16 sm:h-18 lg:h-22 w-auto max-w-[165px] sm:max-w-[215px] object-contain transition-all duration-300 hover:scale-110">
        </div>'''
        items.append(item)
    return '\n'.join(items)

logos_1 = generate_faster_larger_logos(logos)
logos_2 = generate_faster_larger_logos(logos)

new_marquee_section = f'''  <!-- 4. CARROUSEL PASARELA CLUBS (FONDO BLANCO AMPLIADO HASTA ABAJO DE PANTALLA) -->
  <section class="py-5 sm:py-7 lg:py-8 bg-white border-y border-slate-200 overflow-hidden shadow-sm">
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

# Update animation speed in tailwind config
html = html.replace("'ticker-trusted': 'tickerSlow 50s linear infinite'", "'ticker-trusted': 'tickerSlow 32s linear infinite'")

start_marker = '<!-- 4. CARROUSEL PASARELA'
end_marker = '<!-- 5. SECCIÓN DETALLADA: LLAVEROS PARA CLUBS -->'

start_idx = html.find(start_marker)
end_idx = html.find(end_marker)

if start_idx != -1 and end_idx != -1:
    html = html[:start_idx] + new_marquee_section + '\n\n  ' + html[end_idx:]
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print('Updated logos (+10% larger) and ticker speed (32s faster) successfully.')
else:
    print('Markers not found')
