"""Apply shared, static navigation and disclosure controls to generated pages."""

from collections import Counter
from dataclasses import dataclass, field
from html import escape, unescape
from html.parser import HTMLParser
from pathlib import Path
import re
import subprocess
from urllib.parse import quote, urlsplit


ROOT = Path(__file__).resolve().parent
HOME = {"index.html", "en/index.html", "fr/index.html", "it/index.html"}
EDITORIAL_LAYOUTS = {
    "barometro-camaras-padel-2026": "cp-editorial-report",
    "cuanto-cuesta-montar-pista-padel-presupuesto-rentabilidad": "cp-editorial-cost",
    "generador-americana-padel": "cp-tournament",
    "generador-cuadros-torneo-padel": "cp-tournament",
}
UI = {
    "es": ("Llaveros", "Cámaras", "Blog", "Cadenas de clubs", "Contactar", "Menú e idioma"),
    "en": ("Keyrings", "Cameras", "Blog", "Club chains", "Contact", "Menu and language"),
    "fr": ("Porte-clés", "Caméras", "Blog", "Réseaux de clubs", "Contact", "Menu et langue"),
    "it": ("Portachiavi", "Telecamere", "Blog", "Catene di club", "Contatti", "Menu e lingua"),
    "de": ("Schlüsselanhänger", "Kameras", "Blog", "Clubketten", "Kontakt", "Menü und Sprache"),
}
LANGUAGES = {"es": "Español", "en": "English", "fr": "Français", "it": "Italiano", "de": "Deutsch"}
HEADER = re.compile(r"<header\b[^>]*>[\s\S]*?</header>", re.I)
SPACER = re.compile(r'<div\b(?=[^>]*(?:cp-header-spacer|\bh-16\b))(?=[^>]*aria-hidden=["\']true)[^>]*>\s*</div>', re.I)
FAQ_TITLE = re.compile(
    r"^(?:\d+\.\s*)?(?:faq\b|preguntas frecuentes|frequently asked questions|"
    r"(?:foire aux|questions)\s+(?:questions|fréquentes)|domande frequenti|"
    r"häufig gestellte fragen|perguntas frequentes|veelgestelde vragen)", re.I
)
HEADING = {"h2", "h3", "h4", "h5"}
VOID = set("area base br col embed hr img input link meta param source track wbr".split())


@dataclass
class Element:
    tag: str
    attrs: dict
    start: int
    inner: int
    close: int = 0
    end: int = 0
    parent: object = None
    children: list = field(default_factory=list)

    @property
    def classes(self):
        return (self.attrs.get("class") or "").split()


class Markup(HTMLParser):
    def __init__(self, html):
        super().__init__(convert_charrefs=False)
        self.html = html
        self.lines = [0, *(m.end() for m in re.finditer("\n", html))]
        self.nodes = []
        self.stack = []
        self.feed(html)

    def source_offset(self):
        line, column = self.getpos()
        return self.lines[line - 1] + column

    def handle_starttag(self, tag, attrs):
        start = self.source_offset()
        parent = self.stack[-1] if self.stack else None
        inner = start + len(self.get_starttag_text())
        node = Element(tag, dict(attrs), start, inner, parent=parent)
        self.nodes.append(node)
        if parent:
            parent.children.append(node)
        if tag not in VOID:
            self.stack.append(node)
        else:
            node.close = node.end = inner

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in VOID:
            node = self.stack.pop()
            node.close = node.end = node.inner

    def handle_endtag(self, tag):
        for index in range(len(self.stack) - 1, -1, -1):
            if self.stack[index].tag == tag:
                node = self.stack[index]
                node.close = self.source_offset()
                node.end = self.html.index(">", node.close) + 1
                del self.stack[index:]
                break


def elements_replaced(html, edits):
    for start, end, replacement in sorted(edits, reverse=True):
        html = html[:start] + replacement + html[end:]
    return html


def faq_disclosures(html):
    if not re.search(r"faq|frequently asked|preguntas frecuentes|domande frequenti|häufig gestellte", html, re.I):
        return html, 0
    nodes = Markup(html).nodes
    headings = [(node, re.sub(r"\s+", " ", unescape(re.sub(r"<[^>]+>", "", html[node.inner:node.close]))).strip())
                for node in nodes if node.tag in HEADING and node.end]
    scopes = []
    for index, (node, text) in enumerate(headings):
        if FAQ_TITLE.match(text):
            end = next((later.start for later, _ in headings[index + 1:] if later.tag <= node.tag), len(html))
            section = node.parent
            while section and section.tag not in {"section", "article", "main"}:
                section = section.parent
            scopes.append((node.end, min(end, section.close if section and section.close else end)))
    edits = []
    for card in nodes:
        if card.tag != "div" or not card.end or len(card.children) < 2:
            continue
        q, answer = card.children[:2]
        if not q.end or not answer.end:
            continue
        custom = "faq-item" in card.classes and q.tag == "button" and "faq-answer" in answer.classes
        explicit = "faq-card" in card.classes and "faq-q" in q.classes
        scoped = q.tag in HEADING and answer.tag in {"p", "div"} and any(a <= card.start and card.end <= b for a, b in scopes)
        if not (custom or explicit or scoped):
            continue
        ancestor = card.parent
        inside_details = False
        while ancestor:
            if ancestor.tag == "details":
                inside_details = True
                break
            ancestor = ancestor.parent
        if inside_details:
            continue
        classes = " ".join([*card.classes, "cp-faq"])
        attrs = f' name="home-faq"' if custom else ""
        summary = escape(" ".join(q.classes), quote=True)
        body = html[q.end:card.close]
        if custom:
            body = body.replace('class="faq-answer hidden ', 'class="faq-answer ', 1)
        edits.append((card.start, card.end, f'<details class="{escape(classes, quote=True)}"{attrs}>'
                      f'{html[card.inner:q.start]}<summary class="{summary}">{html[q.inner:q.close]}</summary>'
                      f'{body}</details>'))
    return elements_replaced(html, edits), len(edits)


def local_route(href, paths):
    url = urlsplit(href)
    if url.netloc and url.netloc != "coolpadelstudios.com":
        return None
    if not url.path.startswith("/"):
        return None
    return url.path if url.path in paths else None


def site_header(html, route, paths, is_home):
    code = re.search(r'<html\b[^>]*\blang=["\']([a-z]{2})', html, re.I)
    lang = code[1].lower() if code else "es"
    shell = lang if lang in {"es", "en", "fr", "it"} else "en"
    prefix = "/" if shell == "es" else f"/{shell}/"
    ui = UI.get(lang, UI["en"])
    sections = ("llaveros-padel-personalizados/", "camaras/", "blog/", "franquicias-padel/")
    links = "".join(f'<a href="{prefix}{slug}">{label}</a>' for slug, label in zip(sections, ui))
    alternatives = {}
    for entry in re.findall(r'<link\b[^>]*hreflang=["\'][^>]+>', html, re.I):
        lang_match = re.search(r'hreflang=["\']([a-z]{2})["\']', entry, re.I)
        href_match = re.search(r'\bhref=["\']([^"\']+)', entry, re.I)
        if lang_match and href_match:
            target = local_route(href_match[1], paths)
            if target:
                alternatives[lang_match[1].lower()] = target
    language_links = []
    for key, label in LANGUAGES.items():
        home = "/" if key == "es" else f"/{key}/"
        fallback = home if home in paths else None
        if key == "de" and (route.startswith("/camaras/") or "/camaras/" in route):
            fallback = "/de/camaras/" if "/de/camaras/" in paths else None
        target = route if key == lang else alternatives.get(key, fallback)
        if target:
            current = ' aria-current="page"' if key == lang else ''
            language_links.append(f'<a href="{escape(target, quote=True)}" lang="{key}"{current}>{label}</a>')
    contact = "#contacto" if is_home else prefix + "#contacto"
    return f'''<header class="cp-site-header">
  <div class="cp-header-inner">
    <a class="cp-header-brand" href="{prefix}" aria-label="CoolPadel">
      <img src="/assets/images/coolpadel-mascot-hd.png" alt="" width="44" height="44">
      <img src="/assets/images/coolpadel-typography-hd.png" alt="CoolPadel" width="140" height="28">
    </a>
    <nav class="cp-header-links" aria-label="{ui[5]}">{links}</nav>
    <div class="cp-header-actions">
      <details class="cp-header-menu">
        <summary aria-label="{ui[5]}"><span id="current-lang-code">{lang.upper()}</span></summary>
        <div class="cp-header-panel"><div class="cp-header-mobile-links">{links}<hr></div>{''.join(language_links)}</div>
      </details>
      <a class="cp-header-contact" id="nav-contact-btn" href="{contact}">{ui[4]}</a>
      <a class="cp-header-eyes" href="{prefix}" aria-label="CoolPadel Eyes">
        <img src="/assets/images/eyes-thumb.png?v=fixed_eyes" alt="" width="28" height="28">
      </a>
    </div>
  </div>
</header>
<div class="cp-header-spacer" aria-hidden="true"></div>'''


def logo_carousel(html):
    match = re.search(r'<div class="ticker-wrap[^"]*">[\s\S]*?</div>\s*</div>\s*</section>', html)
    if not match:
        return html
    # Find the ticker's original 26 images before its repeated copy.
    logos = re.findall(r'<img\b[^>]*\bclient-\d+\.webp"[^>]*>', match[0])[:26]
    if len(logos) != 26:
        raise ValueError("Unexpected club logo count")
    primary = []
    for logo in logos:
        src = re.search(r'src="([^"]+)"', logo)[1]
        alt = re.search(r'alt="([^"]*)"', logo)[1]
        if not (ROOT / src.replace("../", "")).is_file():
            raise ValueError(f"Missing club logo: {src}")
        primary.append(f'<img src="{src}" alt="{alt}" width="148" height="64" loading="eager" decoding="async">')
    duplicate = [re.sub(r'alt="[^"]*"', 'alt=""', logo) for logo in primary]
    ticker = ('<div class="cp-logo-window"><div class="cp-logo-track">'
              f'<div class="cp-logo-group">{"".join(primary)}</div>'
              f'<div class="cp-logo-group" aria-hidden="true">{"".join(duplicate)}</div>'
              '</div></div></div>\n    </section>')
    return html[:match.start()] + ticker + html[match.end():]


def add_body_class(tag, name):
    classes = re.search(r'\bclass="([^"]*)"', tag)
    if not classes:
        return tag[:-1] + f' class="{name}">'
    if name in classes[1].split():
        return tag
    return tag[:classes.end(1)] + " " + name + tag[classes.end(1):]


def spain_camera_pilot(html):
    if 'class="cp-spain-hero"' in html:
        return html
    message = "Hola Javier, me gustaría pedir una demo de 15 minutos de Save my Play para mi club en España."
    demo_url = "https://wa.me/34680317486?text=" + quote(message)
    label = "Pedir demo de 15 min por WhatsApp"
    demo = f'<a href="{demo_url}" target="_blank" rel="noopener noreferrer" data-product="camaras" data-lead-intent="demo"'
    hero = f'''<nav class="cp-spain-breadcrumb" aria-label="Ruta de navegación">
      <div class="cp-spain-wrap"><a href="/">Inicio</a> / <a href="/camaras/">Cámaras</a> / España</div>
    </nav>
    <section class="cp-spain-hero">
      <div class="cp-spain-wrap cp-spain-hero-grid">
        <div>
          <p class="cp-spain-kicker">La cámara n.º 1 de tenis, pádel y pickleball en Estados Unidos</p>
          <h1>Cámaras para clubs de Pádel en España</h1>
          <p class="cp-spain-subtitle">Retransmite Partidos, Comparte Highlights y Estadísticas con IA</p>
          <p class="cp-spain-description">Save my Play es la cámara oficial de USA Padel y USTA. Graba partidos, recupera tus mejores puntos por QR y monta la cámara en el poste sin obras.</p>
          <div class="cp-spain-actions">
            {demo} id="spain-demo" data-button-position="hero" class="cp-spain-button">{label}</a>
            <a class="cp-spain-button cp-spain-price-link" href="#precios">Ver precios ↓</a>
          </div>
        </div>
        <img class="cp-spain-photo" src="/assets/images/savemyplay-1.jpg" width="800" height="450"
             alt="Vista de una pista de pádel desde una cámara Save my Play" fetchpriority="high">
      </div>
    </section>
    <section class="cp-spain-facts" aria-label="Equipamiento y servicio">
      <div class="cp-spain-wrap">
        <dl>
          <div><dt>Cámara en propiedad</dt><dd>180 € por pista</dd></div>
          <div><dt>Plan de grabación</dt><dd>Desde 45 €/mes por pista</dd></div>
          <div><dt>Modalidad del plan</dt><dd>Suscripción mensual</dd></div>
          <div><dt>Instalación</dt><dd>Montaje en el poste sin obras</dd></div>
        </dl>
        <nav class="cp-spain-city-links" aria-label="Cámaras por ciudad">
          <a href="/camaras-padel-madrid/">Madrid</a>
          <a href="/camaras-padel-barcelona/">Barcelona</a>
          <a href="/camaras-padel-valencia/">Valencia</a>
          <a href="/camaras/espana/sevilla/">Sevilla</a>
          <a href="/camaras-padel-malaga/">Málaga</a>
        </nav>
      </div>
    </section>

    '''
    start, benefits_start, prices_start, video_start = (
        html.index(f"<!-- {number}. ") for number in range(1, 5)
    )
    benefits = html[benefits_start:prices_start].replace('<section class="', '<section class="cp-spain-benefits ', 1)
    benefits = re.sub(r"(?m)^[ \t]+(?=\r?$)", "", benefits)
    html = html[:start] + hero + html[prices_start:video_start] + benefits + html[video_start:]
    html = html.replace("0 permanencia • Cancelación libre", "Cuota mensual sin permanencia")
    html = html.replace("Ninguna permanencia. Cancelación libre mes a mes sin penalizaciones.",
                        "El plan se contrata mes a mes, sin compromiso de permanencia.")
    html = re.sub(r'(?s)    // Mantener el MISMO boton.*?(?=  </script>)', '', html, count=1)
    html = re.sub(r'<body\b[^>]*>', lambda m: add_body_class(m[0], "cp-spain-pilot"), html, count=1)
    html = html.replace("</head>", '  <link rel="stylesheet" href="/assets/css/camera-spain-pilot.css">\n</head>', 1)
    floating = f'''{demo} id="spain-demo-floating" data-button-position="floating"
   class="cp-spain-button cp-spain-floating">{label}</a>
<script>
  if ('IntersectionObserver' in window) {{
    const heroDemo = document.getElementById('spain-demo');
    const floatingDemo = document.getElementById('spain-demo-floating');
    new IntersectionObserver(([entry]) => {{
      floatingDemo.hidden = entry.isIntersecting;
    }}).observe(heroDemo);
  }}
</script>
'''
    return html.replace("</body>", floating + "</body>", 1)


def normalize(only=None):
    names = subprocess.check_output(
        ["git", "ls-files", "-z", "--cached", "--others", "--exclude-standard", "--", "*.html"],
        cwd=ROOT
    ).decode().split("\0")
    routes = {name: "/" + re.sub(r"(^|/)index\.html$", r"\1", name) for name in set(names) if name}
    paths = set(routes.values())
    counts = Counter()
    for name, route in sorted(routes.items()):
        if only is not None and name not in only:
            continue
        file = ROOT / name
        if not file.is_file() or name in {"admin/index.html", "yo/index.html", "manual-marca.html"}:
            continue
        raw = file.read_bytes()
        html = raw.decode("utf-8")
        body = re.search(r"<body\b[^>]*>", html, re.I)
        if not body or re.search(r'<meta\b[^>]*http-equiv=["\']refresh', html, re.I):
            continue
        old = HEADER.search(html, body.end())
        if not old and name != "404.html":
            continue
        start, end = old.span() if old else (body.end(), body.end())
        previous = html[start:end]
        spacer = SPACER.search(html, end, min(end + 540, len(html)))
        if spacer and not re.search(r"<(?:main|section|nav|header)\b", html[end:spacer.start()]):
            end = spacer.end()
        elif old and "top-0" in previous:
            html = html[:end] + re.sub(
                r'(<main\b[^>]*?\bclass="[^"]*?)\bpt-16 sm:pt-20\b',
                r"\1", html[end:], count=1
            )
        header = site_header(html, route, paths, name in HOME)
        content_heading = re.search(r"<h1\b", previous, re.I)
        if content_heading:
            heading = previous[previous.index(">") + 1:previous.lower().rindex("</header>")]
            header += '\n<div class="cp-content-heading">' + heading.replace("\r\n", "\n") + "</div>"
        revised = html[:start] + header.replace("\n", "\r\n" if b"\r\n" in raw else "\n") + html[end:]
        if content_heading:
            revised = re.sub(r"(?m)^(\s*)header(\s*\{)", r"\1.cp-content-heading\2", revised)
        if 'href="/assets/css/site-layout.css"' not in revised:
            revised = revised.replace("</head>", '  <link rel="stylesheet" href="/assets/css/site-layout.css">\n</head>', 1)
        layout = EDITORIAL_LAYOUTS.get(Path(name).parent.name)
        if layout:
            revised = re.sub(r'<body\b[^>]*>', lambda m: add_body_class(m[0], layout), revised, count=1)
        if name == "camaras/espana/index.html":
            revised = spain_camera_pilot(revised)
        if name in HOME:
            revised = logo_carousel(revised)
            if "cp-home-faq-tracking" not in revised:
                revised = revised.replace("</body>", """<script id="cp-home-faq-tracking">
document.addEventListener('toggle', function (event) {
  const faq = event.target;
  if (!faq.matches?.('#faq-accordion details[open]') || typeof trackEvent !== 'function') return;
  if (typeof hasOpenedFaq === 'boolean') hasOpenedFaq = true;
  const question = faq.querySelector('summary').textContent.trim();
  trackEvent('faq_abierto', { faq_pregunta: question, evento_desc: 'Abrió FAQ: ' + question.slice(0, 45) });
}, true);
</script>
</body>""", 1)
        revised, converted = faq_disclosures(revised)
        if revised.encode("utf-8") != raw:
            file.write_bytes(revised.encode("utf-8"))
        counts["headers"] += 1
        counts["faq"] += converted
    print(dict(counts), flush=True)


if __name__ == "__main__":
    normalize()
