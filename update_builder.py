# -*- coding: utf-8 -*-
"""
Updater for build_paises_camaras_v2.py
"""

def main():
    path = 'coolpadel-web/build_paises_camaras_v2.py'
    with open(path, 'r', encoding='utf-8') as f:
        code = f.read()

    # 1. Update imports
    old_imp = "from country_i18n_master import ALL_LANGS_MASTER"
    new_imp = """from country_i18n_native_all import NATIVE_TRANSLATIONS_21
from country_i18n_native_part2 import REMAINING_13_LANGS

ALL_LANGS_MASTER = dict(NATIVE_TRANSLATIONS_21)
ALL_LANGS_MASTER.update(REMAINING_13_LANGS)"""

    if old_imp in code:
        code = code.replace(old_imp, new_imp, 1)
        print("Updated imports.")
    else:
        print("old_imp already replaced or not found.")

    # 2. Update Video Section to use working YouTube IDs and native badges/titles/descriptions/buttons
    # Look for the start of video section
    vid_section_start = '<!-- 4. DEMOSTRACIÓN EN PISTA REAL (4 VÍDEOS) -->'
    vid_section_end = '<!-- 5. PREGUNTAS FRECUENTES DESPLEGABLES (<details><summary>) -->'

    start_idx = code.find(vid_section_start)
    end_idx = code.find(vid_section_end)

    if start_idx != -1 and end_idx != -1:
        new_video_section = """<!-- 4. DEMOSTRACIÓN EN PISTA REAL (4 VÍDEOS) -->
    <section class="py-14 sm:py-20 bg-slate-50 border-b border-slate-200">
      <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center max-w-2xl mx-auto mb-10 sm:mb-14 space-y-2">
          <span class="inline-block text-[#f2920b] font-heading font-black text-xs uppercase tracking-wider">
            {t["vid_badge"]}
          </span>
          <h2 class="font-heading font-black text-2xl sm:text-4xl text-slate-950 uppercase tracking-tight">
            {t["vid_title"]}
          </h2>
          <p class="text-sm sm:text-base text-slate-600 font-medium">
            {t["vid_sub"]}
          </p>
        </div>

        <div class="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
          <div class="bg-white rounded-2xl border border-slate-200 overflow-hidden shadow-xs hover:shadow-md transition flex flex-col">
            <div class="aspect-video bg-slate-900 relative">
              <iframe class="w-full h-full" src="https://www.youtube-nocookie.com/embed/4xwrrveDZxg?start=5623" title="{t['vid1_title']}" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy"></iframe>
            </div>
            <div class="p-4 flex-1 flex flex-col justify-between">
              <div>
                <span class="inline-block px-2 py-0.5 mb-2 rounded bg-amber-50 text-[#f2920b] font-black text-[10px] uppercase tracking-wider">{t.get("vid1_badge", "Live")}</span>
                <h3 class="font-heading font-bold text-slate-900 text-sm leading-snug">{t["vid1_title"]}</h3>
                <p class="text-xs text-slate-600 mt-1">{t["vid1_desc"]}</p>
              </div>
              <a href="https://www.youtube.com/live/4xwrrveDZxg?t=5623" target="_blank" rel="noopener" class="mt-3 inline-flex items-center gap-1.5 text-xs font-bold text-[#3478a6] hover:text-[#f2920b] transition">
                <i data-lucide="play-circle" class="w-4 h-4"></i>
                <span>{t.get("vid_btn", "YouTube")}</span>
              </a>
            </div>
          </div>

          <div class="bg-white rounded-2xl border border-slate-200 overflow-hidden shadow-xs hover:shadow-md transition flex flex-col">
            <div class="aspect-video bg-slate-900 relative">
              <iframe class="w-full h-full" src="https://www.youtube-nocookie.com/embed/LuzDvB5Umfs" title="{t['vid2_title']}" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy"></iframe>
            </div>
            <div class="p-4 flex-1 flex flex-col justify-between">
              <div>
                <span class="inline-block px-2 py-0.5 mb-2 rounded bg-amber-50 text-[#f2920b] font-black text-[10px] uppercase tracking-wider">{t.get("vid2_badge", "Demo")}</span>
                <h3 class="font-heading font-bold text-slate-900 text-sm leading-snug">{t["vid2_title"]}</h3>
                <p class="text-xs text-slate-600 mt-1">{t["vid2_desc"]}</p>
              </div>
              <a href="https://www.youtube.com/watch?v=LuzDvB5Umfs" target="_blank" rel="noopener" class="mt-3 inline-flex items-center gap-1.5 text-xs font-bold text-[#3478a6] hover:text-[#f2920b] transition">
                <i data-lucide="play-circle" class="w-4 h-4"></i>
                <span>{t.get("vid_btn", "YouTube")}</span>
              </a>
            </div>
          </div>

          <div class="bg-white rounded-2xl border border-slate-200 overflow-hidden shadow-xs hover:shadow-md transition flex flex-col">
            <div class="aspect-video bg-slate-900 relative">
              <iframe class="w-full h-full" src="https://www.youtube-nocookie.com/embed/Z0vnvyrUbPQ" title="{t['vid3_title']}" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy"></iframe>
            </div>
            <div class="p-4 flex-1 flex flex-col justify-between">
              <div>
                <span class="inline-block px-2 py-0.5 mb-2 rounded bg-amber-50 text-[#f2920b] font-black text-[10px] uppercase tracking-wider">{t.get("vid3_badge", "Clip")}</span>
                <h3 class="font-heading font-bold text-slate-900 text-sm leading-snug">{t["vid3_title"]}</h3>
                <p class="text-xs text-slate-600 mt-1">{t["vid3_desc"]}</p>
              </div>
              <a href="https://youtu.be/Z0vnvyrUbPQ" target="_blank" rel="noopener" class="mt-3 inline-flex items-center gap-1.5 text-xs font-bold text-[#3478a6] hover:text-[#f2920b] transition">
                <i data-lucide="play-circle" class="w-4 h-4"></i>
                <span>{t.get("vid_btn", "YouTube")}</span>
              </a>
            </div>
          </div>

          <div class="bg-white rounded-2xl border border-slate-200 overflow-hidden shadow-xs hover:shadow-md transition flex flex-col">
            <div class="aspect-video bg-slate-900 relative">
              <iframe class="w-full h-full" src="https://www.youtube-nocookie.com/embed/FcnCWaYahP8" title="{t['vid4_title']}" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy"></iframe>
            </div>
            <div class="p-4 flex-1 flex flex-col justify-between">
              <div>
                <span class="inline-block px-2 py-0.5 mb-2 rounded bg-amber-50 text-[#f2920b] font-black text-[10px] uppercase tracking-wider">{t.get("vid4_badge", "Coach")}</span>
                <h3 class="font-heading font-bold text-slate-900 text-sm leading-snug">{t["vid4_title"]}</h3>
                <p class="text-xs text-slate-600 mt-1">{t["vid4_desc"]}</p>
              </div>
              <a href="https://www.youtube.com/watch?v=FcnCWaYahP8" target="_blank" rel="noopener" class="mt-3 inline-flex items-center gap-1.5 text-xs font-bold text-[#3478a6] hover:text-[#f2920b] transition">
                <i data-lucide="play-circle" class="w-4 h-4"></i>
                <span>{t.get("vid_btn", "YouTube")}</span>
              </a>
            </div>
          </div>
        </div>
      </div>
    </section>

    """
        code = code[:start_idx] + new_video_section + code[end_idx:]
        print("Updated video section with 4 real working YouTube IDs and native texts.")
    else:
        print("Video section markers not found!")

    # 3. Update WhatsApp and Email titles to be dynamic
    old_wa_card = '<h3 class="font-heading font-black text-base sm:text-lg text-slate-950">WhatsApp Directo</h3>'
    new_wa_card = '<h3 class="font-heading font-black text-base sm:text-lg text-slate-950">{t.get("contact_wa_title", "WhatsApp Directo")}</h3>'
    if old_wa_card in code:
        code = code.replace(old_wa_card, new_wa_card, 1)
        print("Updated WhatsApp card title.")

    old_mail_card = '<h3 class="font-heading font-black text-base sm:text-lg text-slate-950">Correo Electrónico</h3>'
    new_mail_card = '<h3 class="font-heading font-black text-base sm:text-lg text-slate-950">{t.get("contact_mail_title", "Correo Electrónico")}</h3>'
    if old_mail_card in code:
        code = code.replace(old_mail_card, new_mail_card, 1)
        print("Updated Email card title.")

    with open(path, 'w', encoding='utf-8') as f:
        f.write(code)
    print("Done writing build_paises_camaras_v2.py")

if __name__ == '__main__':
    main()
