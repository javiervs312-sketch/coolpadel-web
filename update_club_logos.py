import os

clubs_dir = os.path.join(os.getcwd(), 'coolpadel-web', 'assets', 'images', 'Clubs')
logos = sorted([f for f in os.listdir(clubs_dir) if f.endswith('.png')])

def generate_cards(logo_list):
    cards = []
    for l in logo_list:
        card = f'''        <div class="flex items-center justify-center h-16 w-28 sm:w-36 px-4 py-2.5 rounded-xl bg-neutral-900/90 border border-neutral-800 shrink-0 hover:border-neutral-700 transition hover:scale-105 duration-200">
          <img src="assets/images/Clubs/{l}" alt="Club Partner" class="max-h-11 max-w-[90%] object-contain filter brightness-110">
        </div>'''
        cards.append(card)
    return '\n'.join(cards)

logo_cards_1 = generate_cards(logos)
logo_cards_2 = generate_cards(logos)

new_marquee = f'''      <div class="ticker-content animate-ticker-trusted flex items-center gap-6 sm:gap-8">
{logo_cards_1}
        <!-- DUPLICATE FOR INFINITE LOOP -->
{logo_cards_2}
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
    html = html.replace("'ticker-trusted': 'tickerSlow 25s linear infinite'", "'ticker-trusted': 'tickerSlow 50s linear infinite'")
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'Updated index.html with {len(logos)} club logos successfully!')
else:
    print('Markers not found')
