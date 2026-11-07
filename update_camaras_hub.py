# -*- coding: utf-8 -*-
"""
Actualiza el hub principal de cámaras (/camaras/index.html) añadiendo
los 8 nuevos artículos estratégicos en una nueva sección destacada de
'Comparativas, Rentabilidad e Instalación'.
"""

import os
import re

HUB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'camaras', 'index.html')

with open(HUB_PATH, 'r', encoding='utf-8') as f:
    html = f.read()

# Definición de las nuevas tarjetas
new_cards = [
    {
        "url": "/camaras/save-my-play-vs-camaras-vigilancia/",
        "img": "/assets/images/camaras/camera-05.jpg",
        "title": "Cámaras para Pistas de Pádel vs Cámaras de Seguridad (CCTV)",
    },
    {
        "url": "/camaras/save-my-play-vs-sistemas-con-obras/",
        "img": "/assets/images/camaras/camara-instalada-reja-4m-crop.jpg",
        "title": "Sistemas de Grabación Sin Obras vs Instalaciones con Cableado",
    },
    {
        "url": "/camaras/cuanto-cuesta-poner-camaras-pistas-padel/",
        "img": "/assets/images/camaras/pista-moqueta-negra-indoor.png",
        "title": "¿Cuánto Cuesta Poner Cámaras de Pádel y Qué ROI Tiene?",
    },
    {
        "url": "/camaras/camaras-padel-playtomic-matchi-padelmates/",
        "img": "/assets/images/camaras/camera-03.jpg",
        "title": "Cámaras Integradas con Playtomic, Matchi y Padel Mates",
    },
    {
        "url": "/camaras/camaras-para-clubes-indoor-padel/",
        "img": "/assets/images/camaras/pista-indoor-blue-zone-clean.png",
        "title": "Cámaras de Grabación para Clubes de Pádel Indoor",
    },
    {
        "url": "/camaras/camaras-para-pistas-outdoor-padel/",
        "img": "/assets/images/camaras/pista-outdoor-world-sports.png",
        "title": "Cámaras para Pistas de Pádel Outdoor (Exteriores)",
    },
    {
        "url": "/camaras/camaras-padel-urbanizaciones-comunidades/",
        "img": "/assets/images/camaras/retransmision-directo-marcador-youtube.png",
        "title": "Cámaras para Urbanizaciones y Comunidades de Vecinos",
    },
    {
        "url": "/camaras/camaras-retransmision-torneos-padel/",
        "img": "/assets/images/camaras/partido-directo-patrocinador-harbor.png",
        "title": "Cómo Retransmitir Torneos y Ligas de Pádel en Streaming",
    },
]

def make_card(item):
    return f"""      <a href="{item['url']}" class="article-card bg-white border-2 border-slate-200/90 hover:border-[#f2920b] rounded-2xl p-4 sm:p-5 shadow-2xs hover:shadow-lg transition-all duration-300 flex flex-col justify-between group hover:-translate-y-0.5 cursor-pointer block">
  <div class="space-y-3">
    <div class="aspect-[16/9] rounded-xl overflow-hidden bg-slate-900 border border-slate-200/90 shadow-sm relative">
      <img src="{item['img']}" alt="{item['title']}" width="800" height="450" class="w-full h-full object-cover group-hover:scale-105 transition duration-500" loading="lazy" decoding="async">
    </div>
    <div>
      <h2 class="font-sans font-extrabold text-sm sm:text-base lg:text-lg text-slate-900 leading-snug tracking-tight transition-colors m-0">{item['title']}</h2>
    </div>
  </div>
  <div class="pt-3.5 border-t border-slate-100 mt-4">
    <div class="card-action group relative w-full inline-flex items-center justify-center gap-2 px-4 py-2.5 rounded-full bg-[#f2920b] group-hover:bg-[#76d3f6] text-slate-950 font-heading font-black text-xs uppercase tracking-wider transition-all duration-300 shadow-xs group-hover:shadow-md group-hover:scale-[1.01] overflow-hidden active:scale-[.98]">
      <span class="font-black">Leer artículo</span>
      <div class="w-4 h-4 rounded-full bg-slate-950/10 group-hover:bg-slate-950 group-hover:text-white flex items-center justify-center transition-all duration-300">
        <i data-lucide="arrow-right" class="w-3 h-3 stroke-[3] group-hover:translate-x-0.5 transition-transform duration-300"></i>
      </div>
    </div>
  </div>
</a>"""

# Crear bloques de 3 tarjetas por sección
cards_html_chunks = []
current_chunk = []
for c in new_cards:
    current_chunk.append(make_card(c))
    if len(current_chunk) == 3:
        cards_html_chunks.append("\n".join(current_chunk))
        current_chunk = []
if current_chunk:
    cards_html_chunks.append("\n".join(current_chunk))

new_sections_html = ""
for chunk in cards_html_chunks:
    new_sections_html += f"""
  <section>
    <div class="article-grid">
{chunk}
    </div>
  </section>
"""

# Insertar antes de <section class="next-step">
insert_marker = '<section class="next-step">'
if insert_marker in html and '/camaras/save-my-play-vs-camaras-vigilancia/' not in html:
    html = html.replace(insert_marker, f"{new_sections_html}\n  {insert_marker}")
    with open(HUB_PATH, 'w', encoding='utf-8') as f:
        f.write(html)
    print("Hub de cámaras actualizado con los 8 nuevos artículos estratégicos.")
else:
    print("Los artículos ya estaban en el hub o no se encontró el marcador.")
