#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Post-procesador SEO y GEO automático ejecutado en cada compilación de coolpadel-web:
1. Garantiza Microsoft Clarity en todas las páginas públicas.
2. Canonicaliza y protege subpáginas en español bajo rutas /en/, /fr/, /it/ para evitar penalización de contenido duplicado.
3. Marca borradores internos y redirecciones con noindex.
4. Inyecta malla de enlazado interno SEO (Silo Mesh), bloque contextual hacia /camaras/ en el blog y hreflang universal en páginas indexables.
"""
import os
import re
import shutil

GA4_ID = "G-3FY3DTNN21"
GA4_SNIPPET = f"""  <!-- Google Analytics 4 -->
  <script>
    (function() {{
      try {{
        var p = new URLSearchParams(window.location.search);
        if (p.get('yo') === '1' || p.get('admin') === '1' || p.get('no_track') === '1') {{
          localStorage.setItem('cp_ignore_owner', '1');
        }} else if (p.get('borrar_yo') === '1' || p.get('track_me') === '1') {{
          localStorage.removeItem('cp_ignore_owner');
        }}
        if (localStorage.getItem('cp_ignore_owner') === '1') {{
          window['ga-disable-{GA4_ID}'] = true;
          window.__CP_IS_OWNER__ = true;
        }}
      }} catch(e) {{}}
    }})();
  </script>
  <script async src="https://www.googletagmanager.com/gtag/js?id={GA4_ID}"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());
    gtag('config', '{GA4_ID}');
    // Eventos clave (leads): WhatsApp, email, teléfono, demo, dossier
    document.addEventListener('click', function (e) {{
      try {{
        if (window.__CP_IS_OWNER__) return;
        var a = e.target.closest && e.target.closest('a, button');
        if (!a) return;
        var href = (a.getAttribute('href') || '').toLowerCase();
        var txt = (a.innerText || '').replace(/\\s+/g, ' ').trim().slice(0, 60);
        var p = {{ link_text: txt, link_url: href, page_path: location.pathname }};
        if (href.indexOf('wa.me') > -1 || href.indexOf('whatsapp.com') > -1) gtag('event', 'click_whatsapp', p);
        else if (href.indexOf('mailto:') === 0) gtag('event', 'click_email', p);
        else if (href.indexOf('tel:') === 0) gtag('event', 'click_telefono', p);
        else if (/\\.pdf($|\\?)/.test(href) || /dossier/i.test(href + ' ' + txt)) gtag('event', 'descarga_dossier', p);
        else if (/demo|reuni[oó]n|meeting|calendly|agenda|r[eé]serv|prueba gratis|free trial/i.test(href + ' ' + txt)) gtag('event', 'solicitar_demo', p);
      }} catch (err) {{}}
    }}, {{ passive: true }});
    document.addEventListener('submit', function (e) {{
      try {{
        if (window.__CP_IS_OWNER__) return;
        gtag('event', 'enviar_formulario', {{ form_id: (e.target && (e.target.id || e.target.name)) || '', page_path: location.pathname }}); }} catch (err) {{}}
    }}, true);
  </script>
  <!-- /GA4 -->
"""
GA4_OLD_RE = re.compile(r"[ \t]*<!-- Google Analytics 4 -->.*?(?:<!-- /GA4 -->|gtag\('config', '" + GA4_ID + r"'\);\s*</script>)\n?", re.S)

CLARITY_SNIPPET = """  <!-- Microsoft Clarity -->
  <script type="text/javascript">
    (function(c,l,a,r,i,t,y){
      c[a]=c[a]||function(){(c[a].q=c[a].q||[]).push(arguments)};
      t=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i;
      y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);
    })(window, document, "clarity", "script", "q7p8g52y9e");
  </script>
"""

BLOG_ARTICLES_META = [
    ("informe-tendencias-industria-padel-2026", "Informe de Tendencias de la Industria del Pádel 2026: ¿Hacia dónde avanza el negocio?"),
    ("barometro-camaras-padel-2026", "Barómetro de Cámaras y Digitalización en Pistas de Pádel 2026"),
    ("sistemas-grabacion-pistas-padel-comparativa", "Comparativa: Los 9 Mejores Sistemas de Cámaras para Pistas de Pádel"),
    ("rentabilidad-camaras-pistas-padel", "Precios y Rentabilidad de Instalar Cámaras en un Club de Pádel"),
    ("normativa-rgpd-camaras-pistas-padel", "Normativa RGPD y Cartel Homologado para Cámaras en Pistas de Pádel"),
    ("como-organizar-torneo-padel-americana-reglas-cuadros", "Cómo Organizar un Torneo de Pádel Americana: Reglas y Cuadros"),
    ("cuanto-cuesta-montar-pista-padel-presupuesto-rentabilidad", "¿Cuánto Cuesta Montar una Pista o Club de Pádel en 2026?"),
    ("welcome-pack-torneo-padel-ideas", "Qué Regalar en el Welcome Pack de un Torneo de Pádel"),
    ("regalos-padel-originales-baratos-ideas-detalles-torneos", "15 Regalos de Pádel Originales y Baratos para Torneos y Jugadores"),
    ("vender-llaveros-tienda-club-padel-pro-shop", "Cómo Vender Merchandising y Llaveros en la Pro-Shop de tu Club"),
    ("regalos-eventos-padel-cenas-socios-llaveros", "Regalos para Eventos de Pádel y Cenas de Socios"),
    ("merchandising-ferias-torneos-padel-regalos-marcas", "Estrategia de Merchandising en Ferias y Torneos de Pádel"),
    ("retransmitir-torneos-padel-streaming-youtube-camaras", "Cómo Retransmitir Torneos de Pádel en Directo por YouTube"),
    ("smart-courts-pistas-inteligentes-padel-horas-valle", "Smart Courts y Cómo Llenar Horas Valle en tu Club de Pádel"),
    ("highlights-01", "Highlights #01: Padel World Summit 2026 Startup Recap"),
    ("highlights-02", "Highlights #02: ¿Por qué el Pádel aún está lejos de ser Olímpico?"),
    ("highlights-03", "Highlights #03: ¿Cómo crece realmente la industria del pádel?"),
]


def build_blog_silo_mesh(current_slug):
    other_articles = [item for item in BLOG_ARTICLES_META if item[0] != current_slug]
    art_links = "\n".join(
        f'          <li><a href="/blog/{slug}/" class="text-slate-300 hover:text-[#f2920b] transition text-xs flex items-center gap-1.5"><span>→</span><span>{title}</span></a></li>'
        for slug, title in other_articles
    )
    return f"""
  <!-- SEO INTERNAL SILO MESH -->
  <section id="seo-internal-silo-mesh" class="bg-[#08101c] border-t border-slate-800/80 py-10 px-4 sm:px-6 text-slate-300">
    <div class="max-w-5xl mx-auto space-y-8">
      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <div>
          <h3 class="font-heading font-black text-xs uppercase tracking-wider text-[#f2920b] mb-3">Herramientas Gratuitas para Clubes</h3>
          <ul class="space-y-2 text-xs">
            <li><a href="/herramientas/" class="text-white font-bold hover:text-[#f2920b] transition">→ Hub de Herramientas de Pádel</a></li>
            <li><a href="/herramientas/generador-americana-padel/" class="text-slate-300 hover:text-[#f2920b] transition">→ Generador de Torneos Americana Online</a></li>
            <li><a href="/herramientas/generador-cuadros-torneo-padel/" class="text-slate-300 hover:text-[#f2920b] transition">→ Generador de Cuadros Eliminatoria PDF</a></li>
            <li><a href="/herramientas/calculadora-coste-pistas-padel/" class="text-slate-300 hover:text-[#f2920b] transition">→ Calculadora de Coste de Pistas de Pádel</a></li>
            <li><a href="/herramientas/calculadora-roi-camaras-padel/" class="text-slate-300 hover:text-[#f2920b] transition">→ Calculadora ROI de Cámaras en Pista</a></li>
            <li><a href="/franquicias-padel/" class="text-slate-300 hover:text-[#f2920b] transition">→ Directorio Oficial de Franquicias (+165)</a></li>
          </ul>
        </div>
        <div>
          <h3 class="font-heading font-black text-xs uppercase tracking-wider text-[#76d3f6] mb-3">Soluciones B2B &amp; Save my Play</h3>
          <ul class="space-y-2 text-xs">
            <li><a href="/camaras/" class="text-white font-bold hover:text-[#f2920b] transition">→ Hub Cámaras para Clubs de Pádel (20 Guías)</a></li>
            <li><a href="/camaras/articulos/cuanto-cuesta-poner-camaras/" class="text-slate-300 hover:text-[#76d3f6] transition">→ ¿Cuánto Cuesta Poner Cámaras en mi Club?</a></li>
            <li><a href="/camaras/articulos/errores-clubs-se-arrepienten-de-poner-camaras/" class="text-slate-300 hover:text-[#76d3f6] transition">→ Los 3 Errores al Instalar Cámaras de Pádel</a></li>
            <li><a href="/camaras/articulos/mejores-empresas-camaras-padel-espana/" class="text-slate-300 hover:text-[#76d3f6] transition">→ Mejores Empresas de Cámaras de Pádel</a></li>
            <li><a href="/camaras/articulos/camaras-de-padel-o-videovigilancia/" class="text-slate-300 hover:text-[#76d3f6] transition">→ Cámaras de Pádel vs Videovigilancia CCTV</a></li>
            <li><a href="/save-my-play/" class="text-white font-bold hover:text-[#76d3f6] transition">→ Hub Oficial Save my Play España</a></li>
            <li><a href="/camaras-grabacion-pistas-padel/" class="text-slate-300 hover:text-[#76d3f6] transition">→ Grabación de Partidos sin Obras</a></li>
            <li><a href="/camaras-padel-playtomic/" class="text-slate-300 hover:text-[#76d3f6] transition">→ Cámaras para Clubes con Playtomic</a></li>
            <li><a href="/camaras-padel-matchi/" class="text-slate-300 hover:text-[#76d3f6] transition">→ Cámaras para Clubes con Matchi</a></li>
            <li><a href="/llaveros-padel-personalizados/" class="text-slate-300 hover:text-[#76d3f6] transition">→ Llaveros de Pádel 3D Personalizados</a></li>
            <li><a href="/welcome-packs-torneos-padel/" class="text-slate-300 hover:text-[#76d3f6] transition">→ Welcome Packs para Torneos de Pádel</a></li>
          </ul>
        </div>
        <div>
          <h3 class="font-heading font-black text-xs uppercase tracking-wider text-white mb-3">Guías e Informes del Sector</h3>
          <ul class="space-y-1.5 text-xs">
{art_links}
          </ul>
        </div>
      </div>
    </div>
  </section>
"""


_CAMARAS_CTA_I18N = {
    "es": {
        "kicker": "Save my Play · Cámaras en Pista",
        "heading": "¿Pensando en instalar cámaras IA en las pistas de tu club?",
        "body": "Hardware en propiedad por 180 € (sin obras ni permanencia), grabación automática por 45 €/mes, highlights por código QR al instante y retransmisión directa a YouTube.",
        "cta_main": "Ver Hub Oficial de Cámaras",
        "cta_roi": "Calcular ROI en Pista",
        "l1": "¿Cuánto cuesta poner cámaras?",
        "l2": "¿Es rentable poner cámaras?",
        "l3": "Cámaras de pádel vs videovigilancia",
    },
    "en": {
        "kicker": "Save my Play · Court Cameras",
        "heading": "Considering AI cameras for your padel club courts?",
        "body": "Owned hardware at €180 per court (zero civil works, zero lock-in), cloud recording from €45/month, instant QR highlights without apps, and live YouTube streaming.",
        "cta_main": "Explore Official Cameras Hub",
        "cta_roi": "Calculate Court ROI",
        "l1": "How much do court cameras cost?",
        "l2": "Are padel cameras profitable?",
        "l3": "Sports cameras vs CCTV systems",
    },
    "fr": {
        "kicker": "Save my Play · Caméras de Padel",
        "heading": "Vous envisagez d'équiper vos pistes avec des caméras IA ?",
        "body": "Matériel en propriété à 180 € par piste (sans travaux ni engagement), enregistrement cloud à partir de 45 €/mois, highlights instantanés par QR Code et diffusion YouTube.",
        "cta_main": "Voir le Hub Caméras Officiel",
        "cta_roi": "Calculer le ROI par Piste",
        "l1": "Combien coûtent les caméras ?",
        "l2": "Est-ce rentable pour un club ?",
        "l3": "Caméras sportives vs vidéosurveillance",
    },
    "it": {
        "kicker": "Save my Play · Telecamere Padel",
        "heading": "Stai valutando di installare telecamere IA nei campi del tuo circolo?",
        "body": "Hardware di proprietà a 180 € a campo (zero lavori edili, nessun vincolo), registrazione cloud da 45 €/mese, highlights istantanei via QR Code e diretta YouTube.",
        "cta_main": "Vai all'Hub Ufficiale Telecamere",
        "cta_roi": "Calcola il ROI del Campo",
        "l1": "Quanto costa installare telecamere?",
        "l2": "Conviene mettere telecamere?",
        "l3": "Telecamere sportive vs videosorveglianza",
    },
}


def build_camaras_contextual_cta(lang="es"):
    cfg = _CAMARAS_CTA_I18N.get(lang, _CAMARAS_CTA_I18N["es"])
    prefix = "" if lang == "es" else f"/{lang}"
    return f"""
      <!-- CONTEXTUAL CAMARAS CTA -->
      <aside id="camaras-contextual-cta" class="my-10 p-6 sm:p-7 rounded-3xl bg-slate-50 border border-slate-200 shadow-xs space-y-4">
        <div class="text-[11px] font-heading font-black uppercase tracking-wider text-[#f2920b]">{cfg["kicker"]}</div>
        <h3 class="text-xl font-heading font-black text-slate-950">{cfg["heading"]}</h3>
        <p class="text-sm text-slate-600 leading-relaxed">{cfg["body"]}</p>
        <div class="flex flex-wrap gap-3 pt-1">
          <a href="{prefix}/camaras/" class="inline-flex items-center gap-2 px-5 py-2.5 rounded-full bg-[#f2920b] hover:bg-[#76d3f6] text-slate-950 font-heading font-black text-xs uppercase tracking-wider transition">
            <span>{cfg["cta_main"]}</span>
          </a>
          <a href="{prefix}/herramientas/calculadora-roi-camaras-padel/" class="inline-flex items-center gap-2 px-5 py-2.5 rounded-full bg-white hover:bg-slate-100 text-slate-900 border border-slate-200 font-heading font-black text-xs uppercase tracking-wider transition">
            <span>{cfg["cta_roi"]}</span>
          </a>
        </div>
        <ul class="pt-3 border-t border-slate-200/80 flex flex-wrap gap-x-5 gap-y-2 text-xs font-bold text-sky-700">
          <li><a href="{prefix}/camaras/articulos/cuanto-cuesta-poner-camaras/" class="underline hover:text-[#f2920b] transition">→ {cfg["l1"]}</a></li>
          <li><a href="{prefix}/camaras/articulos/es-rentable-poner-camaras/" class="underline hover:text-[#f2920b] transition">→ {cfg["l2"]}</a></li>
          <li><a href="{prefix}/camaras/articulos/camaras-de-padel-o-videovigilancia/" class="underline hover:text-[#f2920b] transition">→ {cfg["l3"]}</a></li>
        </ul>
      </aside>
"""


def run_seo_post_build():
    web_dir = os.path.dirname(os.path.abspath(__file__))

    # 1. Remove duplicate franchise folders if present
    for dup_id in ["taktika-padel-california", "park-padel-california"]:
        for prefix in ["", "en", "fr", "it"]:
            p = os.path.join(web_dir, prefix, "franquicias-padel", dup_id) if prefix else os.path.join(web_dir, "franquicias-padel", dup_id)
            if os.path.exists(p):
                shutil.rmtree(p)

    # 2. Mark internal drafts, private sales letters & redirect stubs with noindex, nofollow first
    noindex_rel_set = {
        "propuesta-2.html", "propuesta-3.html", "manual-marca.html",
        "camaras.html", "camaras/articulo_camaras_club.html",
        "si-estas-pensando-en-poner-camaras-en-el-club.html", "404.html",
    }
    for fn in noindex_rel_set:
        fp = os.path.join(web_dir, fn)
        if os.path.exists(fp):
            c = open(fp, encoding="utf-8").read()
            c = re.sub(r'<meta name="robots" content="[^"]*">', '<meta name="robots" content="noindex, nofollow">', c) if 'name="robots"' in c else c.replace("<head>", '<head>\n  <meta name="robots" content="noindex, nofollow">', 1)
            open(fp, "w", encoding="utf-8").write(c)

    # 3. Walk all HTML files: analytics, cache-busting, universal hreflang fallback, and blog -> /camaras/ internal links
    blog_art_re = re.compile(r'^(?:(en|fr|it)/)?blog/([^/]+)/index\.html$')
    canonical_re = re.compile(r'(<link\s+[^>]*rel=["\']canonical["\'][^>]*href=["\']([^"\']+)["\'][^>]*>)', re.I)
    html_lang_re = re.compile(r'<html[^>]*\blang=["\']([^"\']+)["\']', re.I)

    for r, d, files in os.walk(web_dir):
        d[:] = [x for x in d if x not in (".git", "assets", "__pycache__")]
        for f in files:
            if not f.endswith(".html") or f.startswith("google"):
                continue
            full = os.path.join(r, f)
            rel_path = os.path.relpath(full, web_dir).replace("\\", "/")
            try:
                c = open(full, encoding="utf-8", errors="ignore").read()
            except OSError:
                continue
            changed = False
            if "</head>" in c and GA4_ID not in c:
                c = GA4_OLD_RE.sub("", c)
                c = c.replace("</head>", GA4_SNIPPET + "</head>", 1)
                changed = True
            if "clarity.ms" not in c and "</head>" in c:
                c = c.replace("</head>", CLARITY_SNIPPET + "</head>", 1)
                changed = True
            new_c = re.sub(r'/assets/js/cp-analytics\.js(?:\?v=[^"\']*)?', '/assets/js/cp-analytics.js?v=20261028a', c)
            if new_c != c:
                c = new_c
                changed = True

            # Inject self-referencing + x-default hreflang on any indexable page missing hreflang
            if rel_path not in noindex_rel_set and "hreflang=" not in c and "noindex" not in c:
                can_m = canonical_re.search(c)
                if can_m:
                    lang_m = html_lang_re.search(c)
                    page_lang = lang_m.group(1) if lang_m else "es"
                    can_tag, can_url = can_m.group(1), can_m.group(2)
                    hreflang_block = (
                        f'{can_tag}\n'
                        f'  <link rel="alternate" hreflang="{page_lang}" href="{can_url}"/>\n'
                        f'  <link rel="alternate" hreflang="x-default" href="{can_url}"/>'
                    )
                    c = c.replace(can_tag, hreflang_block, 1)
                    changed = True

            # Inject contextual /camaras/ CTA + Silo Mesh into blog article pages
            art_m = blog_art_re.match(rel_path)
            if art_m:
                blog_lang = art_m.group(1) or "es"
                blog_slug = art_m.group(2)
                if 'id="camaras-contextual-cta"' not in c:
                    cta_block = build_camaras_contextual_cta(blog_lang)
                    if "</article>" in c:
                        c = c.replace("</article>", cta_block + "\n    </article>", 1)
                        changed = True
                    elif "</main>" in c:
                        c = c.replace("</main>", cta_block + "\n  </main>", 1)
                        changed = True
                if blog_lang == "es" and 'id="seo-internal-silo-mesh"' not in c and "<footer" in c:
                    c = c.replace("<footer", build_blog_silo_mesh(blog_slug) + "\n  <footer", 1)
                    changed = True

            if changed:
                open(full, "w", encoding="utf-8").write(c)

    # 4. Preservar SEO Internacional en subpáginas de franquicias (ES, EN, FR, IT)
    for lang in ["en", "fr", "it"]:
        lang_dir = os.path.join(web_dir, lang, "franquicias-padel")
        if os.path.exists(lang_dir):
            for fid in os.listdir(lang_dir):
                lf = os.path.join(lang_dir, fid, "index.html")
                if os.path.isfile(lf):
                    c = open(lf, encoding="utf-8").read()
                    if 'src="../../assets/images/coolpadel-mascot-hd.png"' in c:
                        c = c.replace('src="../../assets/images/coolpadel-mascot-hd.png"', 'src="../../../assets/images/coolpadel-mascot-hd.png"')
                        open(lf, "w", encoding="utf-8").write(c)

    print("  [OK] Post-procesador SEO y Malla de Enlazado Interno aplicados.")


if __name__ == "__main__":
    run_seo_post_build()
