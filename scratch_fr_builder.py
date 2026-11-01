import sys
from pathlib import Path

ROOT = Path("coolpadel-web")
sys.path.append(str(ROOT))
import build_camera_articles as b

articles = b.load_articles()
print(f"Total articles loaded: {len(articles)}")

# We will define the full French localization data:
# 1. Hub metadata and texts (Hero eyebrow, title, intro text, cards CTA, Next Step)
# 2. Titles of the 20 articles in French
# 3. Blocks / content of the 20 articles in French (preserving personal, direct Javier tone, bolds, structure)
# 4. Videos captions and CTA in French

FR_HUB = {
    "lang": "fr",
    "meta_title": "Caméras pour clubs de padel | CoolPadel",
    "meta_desc": "Tout ce que vous devez savoir avant d'installer des caméras dans votre club de padel.",
    "eyebrow": "Tout ce que vous devez savoir avant d'installer des caméras",
    "title": "Caméras pour clubs de padel",
    "intro": """<p>Nous savons que vous voulez prendre la meilleure décision concernant les caméras<br>L'expérience nous montre que les clubs apprécient d'avoir des informations utiles à leur disposition<br>Et que si vous n'avez pas d'intérêt à vous informer, cela ne vaut pas la peine de faire la démo en ligne</p><p>C'est pourquoi nous avons essayé d'être le plus sincères et transparents possible</p><p>En cours de route, vous vous rendrez compte si installer des caméras est une bonne idée ou non<br>Et si vous souhaitez installer celles de Save My Play ou d'une autre entreprise<br>Quelle que soit votre décision, ce sera le mieux pour vous comme pour nous</p><p>Ainsi, si nous faisons la démo, vous aurez de meilleures questions et nous rentabiliserons mieux notre temps</p>""",
    "card_cta": "Lire l'article",
    "next_step_title": "Étape suivante",
    "next_step_p1": "Si vous n'êtes pas encore totalement fixé, je vous laisse ci-dessus d'autres articles sur les caméras qui vous aideront.",
    "next_step_p2": "Si vous avez des questions et souhaitez que je vous montre en détail comment tout fonctionne, réservez votre créneau pour la démo.",
    "related_title": "Plus d'articles sur les caméras",
    "calendly_url": "https://calendly.com/javier-vs-312/demo-save-my-play?locale=fr",
}

print("French config draft ready")
