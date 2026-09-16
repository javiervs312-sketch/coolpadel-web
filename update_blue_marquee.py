import os

clubs_dir = os.path.join(os.getcwd(), 'coolpadel-web', 'assets', 'images', 'Clubs')
logos = sorted([f for f in os.listdir(clubs_dir) if f.endswith('.png')])

def generate_free_logos(logo_list):
    items = []
    for l in logo_list:
        item = f'''        <div class="flex items-center justify-center shrink-0 px-4 sm:px-6 group">
          <img src="assets/images/Clubs/{l}" alt="Club Partner" class="h-12 sm:h-14 lg:h-16 w-auto max-w-[130px] sm:max-w-[170px] object-contain transition-all duration-300 hover:scale-110">
        </div>'''
        items.append(item)
    return '\n'.join(items)

free_logos_1 = generate_free_logos(logos)
free_logos_2 = generate_free_logos(logos)

new_section = f'''  <!-- 4. CARROUSEL PASARELA "TRUSTED BY" (FONDO AZUL CLARITO #76D3F6) -->
  <section class="py-8 sm:py-10 bg-[#76d3f6] border-y border-[#5ec5ed] overflow-hidden text-slate-950">
    <div class="max-w-7xl mx-auto px-4 mb-3 text-center">
      <p class="text-[11px] sm:text-xs uppercase tracking-widest font-black text-slate-950/80">
        TRUSTED BY · MÁS DE 30 CLUBS, MARCAS Y FEDERACIONES
      </p>
    </div>

    <div class="ticker-wrap py-2">
      <div class="ticker-content animate-ticker-trusted flex items-center gap-8 sm:gap-12 lg:gap-14 py-2">
{free_logos_1}
        <!-- DUPLICATE FOR INFINITE LOOP -->
{free_logos_2}
      </div>
    </div>
  </section>'''

index_path = os.path.join(os.getcwd(), 'coolpadel-web', 'index.html')
with open(index_path, 'r', encoding='utf-8') as f:
    html = f.read()

start_marker = '<!-- 4. CARROUSEL PASARELA "TRUSTED BY"'
end_marker = '<!-- 5. SECCIÓN DETALLADA: LLAVEROS PARA CLUBS -->'

start_idx = html.find(start_marker)
end_idx = html.find(end_marker)

if start_idx != -1 and end_idx != -1:
    html = html[:start_idx] + new_section + '\n\n  ' + html[end_idx:]
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print('Updated TRUSTED BY section with exact light blue background #76d3f6!')
else:
    print('Markers not found')
