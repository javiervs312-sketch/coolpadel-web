# -*- coding: utf-8 -*-
"""
Traductor determinista por bloques completos para generar camaras_i18n_data.py
Traduce bloques enteros (no línea a línea), preservando etiquetas HTML y saltos de línea.
Total llamadas por idioma: ~75 (muy rápido, ~20-30 segundos por idioma).
"""

import html
import json
import re
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.append(str(ROOT))

from build_camera_articles import load_articles
from camaras_fr_data import FR_ARTICLES_DATA, FR_VIDEOS

I18N_OUTPUT_FILE = ROOT / "camaras_i18n_data.py"

def translate_block_fast(text: str, target_lang: str, source_lang: str = "es") -> str:
    """Traduce un bloque protegiendo tags HTML."""
    if not text.strip():
        return text

    tag_map = {}
    tag_cnt = 0
    def replace_html_tag(match):
        nonlocal tag_cnt
        token = f"[H{tag_cnt}]"
        tag_map[token] = match.group(0)
        tag_cnt += 1
        return token

    masked = re.sub(r'</?[a-zA-Z0-9]+[^>]*>', replace_html_tag, text)

    translated = masked
    for attempt in range(4):
        try:
            url = f"https://clients5.google.com/translate_a/t?client=dict-chrome-ex&sl={source_lang}&tl={target_lang}&q={urllib.parse.quote(masked)}"
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
            with urllib.request.urlopen(req, timeout=10) as resp:
                res = resp.read().decode("utf-8")
                parsed = json.loads(res)
                if isinstance(parsed, list) and len(parsed) > 0:
                    translated = parsed[0]
                else:
                    translated = str(parsed)
                break
        except Exception as e:
            if attempt == 3:
                print(f"      [WARN] Fallo traduciendo bloque ({e}), usando original.")
                translated = masked
            time.sleep(1.0 * (attempt + 1))

    # Restaurar tags
    for token, original_tag in tag_map.items():
        pattern = re.escape(token).replace(r'\[', r'\[\s*').replace(r'\]', r'\s*\]')
        translated = re.sub(pattern, original_tag, translated)
        translated = translated.replace(r'[\/' + token[1:], original_tag)

    translated = translated.replace(r'\/', '/')
    return translated

def run():
    print("Iniciando traduccion rapida por bloques de los 20 articulos de camaras...")
    articles_es = load_articles()
    print(f"Total articulos base: {len(articles_es)}")

    hub_intro_es = [
        "Sabemos que queréis tomar la mejor decisión sobre las cámaras<br>La experiencia nos dice que los clubs agradecen tener información útil a su disposición<br>Y que si no tenéis interés en informaros, no merece la pena hacer la demo online",
        "Por eso, hemos tratado de ser lo más sinceros y transparentes posible",
        "Por el camino os iréis dando cuenta de si es buena idea poner cámaras o no<br>Y si queréis ponerlas de Save My Play o de otra empresa<br>Sea cual sea la decisión, será mejor para vosotros y para nosotros",
        "Así si hacemos la demo, tenéis mejores preguntas y aprovechamos mejor el tiempo"
    ]

    hub_videos_es = {
        "como-ver-highlights-sin-app": (
            "Cómo guardar los highlights en pista",
            "Levanta los brazos mirando a la cámara o pulsa el botón verde para guardar tu mejor punto al instante.",
            "https://www.youtube-nocookie.com/embed/Z0vnvyrUbPQ",
        ),
        "como-montar-camara-save-my-play": (
            "Lo fácil que es de usar",
            "En apenas 10 minutos y con solo dos botones tienes la cámara grabando partidos, highlights y directos sin complicaciones.",
            "https://www.youtube-nocookie.com/embed/LuzDvB5Umfs",
        ),
        "save-my-play-en-pocas-palabras": (
            "Retransmisión en directo del torneo FIP de Miami",
            "Así se ve una retransmisión en directo oficial con las cámaras de Save My Play en torneos internacionales FIP.",
            "https://www.youtube-nocookie.com/embed/4xwrrveDZxg?start=5623",
        ),
        "que-son-las-coaching-tools": (
            "Herramientas de entrenamiento en pista",
            "Con las coaching tools puedes pausar la jugada en la tablet, dibujar trayectorias y grabar notas de voz para tus alumnos.",
            "https://www.youtube-nocookie.com/embed/FcnCWaYahP8",
        ),
    }

    result = {
        "fr": {
            "articles": FR_ARTICLES_DATA,
            "videos": FR_VIDEOS,
            "hub_eyebrow": "Tout ce que vous devez savoir avant d'installer des caméras",
            "hub_title": "Caméras pour clubs de padel",
            "hub_intro": [
                "Nous savons que vous voulez prendre la meilleure décision concernant les caméras<br>L'expérience nous montre que les clubs apprécient d'avoir des informations utiles et transparentes à disposition<br>Et que si vous n'avez aucun intérêt à vous informer, cela ne vaut pas la peine de faire une démo en ligne",
                "C'est pourquoi nous avons voulu être les plus sincères et transparents possible",
                "Au fil de vos lectures, vous vous rendrez compte par vous-même si c'est une bonne idée d'installer des caméras ou non<br>Et si vous souhaitez les prendre chez Save My Play ou chez un confrère<br>Quelle que soit votre décision, ce sera la meilleure pour vous comme pour nous",
                "Ainsi, si nous faisons la démo, vous aurez de bien meilleures questions et nous rentabiliserons au mieux notre temps d'échange"
            ],
            "next_step_title": "Étape suivante",
            "next_step_p1": "Si vous hésitez encore, découvrez ci-dessus nos guides détaillés sur les caméras de padel.",
            "next_step_p2": "Si vous avez des questions précises et souhaitez voir concrètement le système en direct, réservez votre créneau pour la démo.",
            "read_article": "Lire l'article",
            "related_title": "Articles recommandés",
            "nav_camaras": "CAMÉRAS"
        }
    }

    languages = [
        ("en", "Everything you need to know before installing cameras", "Cameras for padel clubs", "Next step", "If you're still not sure, check out our guides above on padel court cameras.", "If you have questions and want to see how it all works live, book a demo call.", "Read article", "Recommended articles", "CAMERAS"),
        ("it", "Tutto quello che devi sapere prima di installare le telecamere", "Telecamere per club di padel", "Passo successivo", "Se hai ancora dubbi, consulta gli articoli qui sopra che ti aiuteranno a decidere.", "Se hai domande e vuoi vedere come funziona tutto dal vivo, prenota il tuo spazio per la demo.", "Leggi l'articolo", "Articoli correlati", "TELECAMERE"),
        ("de", "Alles, was Sie vor der Installation von Kameras wissen müssen", "Kameras für Padel-Clubs", "Nächster Schritt", "Wenn Sie noch unsicher sind, finden Sie oben weitere hilfreiche Artikel.", "Wenn Sie Fragen haben und das System live im Einsatz sehen möchten, buchen Sie eine Demo.", "Artikel lesen", "Empfohlene Artikel", "KAMERAS")
    ]

    for lang_code, eyebrow, title, next_title, next_p1, next_p2, read_btn, rel_title, nav_label in languages:
        print(f"\n================ Procesando idioma: {lang_code.upper()} ================")
        
        # 1. Intro Hub
        print("  -> Traduciendo intro del hub...")
        trans_intro = []
        for p in hub_intro_es:
            t_p = translate_block_fast(p, lang_code, "es")
            trans_intro.append(t_p)
            time.sleep(0.15)

        # 2. Videos
        print("  -> Traduciendo videos...")
        lang_videos = {}
        for v_slug, (v_title, v_desc, v_url) in hub_videos_es.items():
            t_title = translate_block_fast(v_title, lang_code, "es")
            t_desc = translate_block_fast(v_desc, lang_code, "es")
            lang_videos[v_slug] = (t_title, t_desc, v_url)
            time.sleep(0.15)

        # 3. 20 Artículos por bloques
        print("  -> Traduciendo 20 articulos por bloques...")
        lang_articles = {}
        for idx, art in enumerate(articles_es, 1):
            slug = art["slug"]
            orig_title = art["title"]
            trans_title = translate_block_fast(orig_title, lang_code, "es")
            time.sleep(0.1)

            trans_blocks = []
            for b_text in art["blocks"]:
                # Traducir bloque completo respetando \n
                t_block = translate_block_fast(b_text, lang_code, "es")
                # Dividir por líneas no vacías para estructura de párrafos
                paras = [p.strip() for p in t_block.split("\n") if p.strip()]
                trans_blocks.append(paras)
                time.sleep(0.15)

            lang_articles[slug] = {
                "title": trans_title,
                "blocks": trans_blocks
            }
            print(f"    [{idx}/20] {slug} OK")

        result[lang_code] = {
            "articles": lang_articles,
            "videos": lang_videos,
            "hub_eyebrow": eyebrow,
            "hub_title": title,
            "hub_intro": trans_intro,
            "next_step_title": next_title,
            "next_step_p1": next_p1,
            "next_step_p2": next_p2,
            "read_article": read_btn,
            "related_title": rel_title,
            "nav_camaras": nav_label
        }

    print(f"\nGuardando datos en {I18N_OUTPUT_FILE}...")
    with open(I18N_OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("# -*- coding: utf-8 -*-\n")
        f.write('"""\nDiccionario completo y determinista de Camaras para FR, EN, IT, DE.\n')
        f.write('Generado automaticamente sin coste de tokens de LLM.\n"""\n\n')
        f.write("CAMARAS_I18N = " + repr(result) + "\n")

    print("[EXITO] Generacion de diccionarios i18n finalizada.")

if __name__ == "__main__":
    run()
