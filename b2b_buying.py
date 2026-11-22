"""Shared content for the two CoolPadel purchase paths."""
from html import escape
from urllib.parse import quote

TARIFFS_URL = "/camaras/cuanto-cuesta-poner-camaras-pistas-padel/"
INSTALL_URL = "/camaras-grabacion-pistas-padel/"
BUTTON_CLASSES = (
    "inline-flex items-center justify-center gap-2 rounded-full bg-[#f2920b] "
    "px-5 py-3 font-heading font-black text-sm text-slate-950 hover:bg-[#76d3f6] transition"
)
BOX_CLASSES = "my-6 rounded-2xl border border-slate-200 bg-slate-50 p-4 sm:p-6 text-slate-900"


def euros(value):
    return f"{value:,}".replace(",", ".") + " €"


def quote_button(product, intent, label, message, position, market="ES"):
    href = "https://wa.me/34680317486?text=" + quote(message)
    return (
        f'<a class="{BUTTON_CLASSES}" href="{escape(href, quote=True)}" '
        f'data-product="{product}" data-lead-intent="{intent}" '
        f'data-button-position="{position}" data-delivery-market="{market}" '
        f'target="_blank" rel="noopener noreferrer">{escape(label)}</a>'
    )


def camera_quote(courts=None, position="content", market="ES"):
    quantity = str(courts) if courts else "__"
    label = f"Pedir presupuesto para {courts} pistas" if courts else "Pedir presupuesto para mi club"
    return quote_button(
        "camaras", "presupuesto", label,
        f"Hola Javier, quiero presupuesto para poner cámaras Save my Play en mi club. "
        f"Pistas: {quantity}. Ciudad: __. [CP-WEB-CAM]", position, market,
    )


def camera_decision():
    return f'''<aside class="{BOX_CLASSES}" aria-label="Resumen para pedir presupuesto">
      <p><strong>Hardware:</strong> 180 € por pista, en propiedad.</p>
      <p><strong>Cuota:</strong> 45 €/mes por pista en clubes de menos de 5 pistas. Incluye grabación, pulsador, highlights y streaming, sin permanencia. La analítica avanzada con IA tiene su propia tarifa.</p>
      <p><strong>Montaje:</strong> unos 5 minutos para fijar el soporte al poste sin obra, con corriente y conexión preparadas.</p>
      {camera_quote(position="hero")}
    </aside>'''


def camera_examples():
    return [(n, n * 180, n * (45 if n < 5 else 41)) for n in (4, 8, 12)]


def camera_cost_faq():
    return [
        {
            "q": f"¿Cuánto cuesta poner cámaras en {n} pistas de pádel en España?",
            "a": f"El hardware cuesta {euros(hardware)} en un pago único y el plan de grabación y streaming cuesta {euros(monthly)} al mes para las {n} pistas. El ejemplo excluye IVA, envío y extras.",
        }
        for n, hardware, monthly in camera_examples()
    ]


def camera_cost_table():
    rows = "".join(
        f'<tr><th scope="row" class="p-2">{n}</th><td class="p-2">{euros(hw)}</td>'
        f'<td class="p-2">{euros(rec)}/mes</td></tr>'
        for n, hw, rec in camera_examples()
    )
    return f'''<section id="presupuesto-por-pistas" class="{BOX_CLASSES}">
      <h2 class="font-heading text-xl font-black">Presupuesto de cámaras para 4, 8 y 12 pistas en España</h2>
      <div class="overflow-x-auto"><table class="w-full text-left text-sm">
        <thead><tr><th scope="col" class="p-2">Pistas</th><th scope="col" class="p-2">Hardware en propiedad</th><th scope="col" class="p-2">Grabación y streaming</th></tr></thead>
        <tbody>{rows}</tbody>
      </table></div>
      <p>Importes sin IVA, envío ni extras. El tramo base es de 45 €/mes por pista. De 5 a 14 pistas se aplican 41 €/mes por pista.</p>
    </section>'''


def camera_cost_questions():
    return "".join(f'<details class="my-3"><summary>{row["q"]}</summary><p>{row["a"]}</p></details>' for row in camera_cost_faq())


def camera_demo_link():
    return """<details class="my-3">
      <summary class="cursor-pointer font-bold underline">Ver cómo se graba y descarga una jugada por QR</summary>
      <div class="my-2 aspect-video max-w-xl">
        <iframe class="h-full w-full" src="https://www.youtube-nocookie.com/embed/LuzDvB5Umfs"
          title="Save my Play: demostración de uso" loading="lazy" allowfullscreen></iframe>
      </div>
      <a href="https://www.youtube.com/watch?v=LuzDvB5Umfs" target="_blank" rel="noopener noreferrer">Abrir en YouTube</a>
    </details>"""


def keyring_decision():
    sample = quote_button(
        "llaveros", "muestra_llaveros", "Solicitar muestra física con mi logo",
        "Hola Javier, quiero solicitar la muestra física de 15 € con el logo de mi club. País de entrega: __. Fecha del evento: __. [CP-WEB-LLA]", "hero",
    )
    return f'''<div class="{BOX_CLASSES}" id="pedido-clubes">
      <h2 class="font-heading text-xl font-black">Llaveros personalizados con el logo de tu club</h2>
      <p>Goma 3D microinyectada en relieve, con el logo que nos envíes.</p>
      <h2 class="font-heading text-lg font-black">Pedido mínimo al por mayor desde 100 unidades</h2>
      <p>100 unidades por 300 € sin IVA (3,00 €/ud). La muestra física cuesta 15 € y se descuenta del pedido final.</p>
      <div class="flex flex-wrap items-center justify-center gap-3">
        <a href="#precios" class="{BUTTON_CLASSES}" data-product="llaveros" data-lead-intent="calculo_llaveros" data-button-position="hero">Calcular pedido</a>
        {sample}
      </div>
    </div>'''


def keyring_process():
    return f'''<section class="{BOX_CLASSES}" aria-labelledby="welcome-packs-llaveros">
      <h2 id="welcome-packs-llaveros" class="font-heading text-xl font-black">Llaveros para welcome packs de torneos</h2>
      <ol class="list-decimal pl-5">
        <li>Envíanos el vector o una imagen del logo de tu club.</li>
        <li>Revisa el diseño y solicita la muestra física de 15 €.</li>
        <li>Confirma la tirada, el país de entrega y la fecha del torneo.</li>
      </ol>
      <figure class="my-4"><img src="/assets/images/llaveros-padel-personalizados-clubs.webp" alt="Ejemplos de llaveros en relieve con logos de clubes" loading="lazy" class="w-full rounded-2xl"><figcaption>Ejemplos de acabados 3D de CoolPadel.</figcaption></figure>
      <a href="/welcome-packs-torneos-padel/#precios" class="underline" data-product="llaveros" data-lead-intent="calculo_llaveros" data-button-position="content">Calcular llaveros para un torneo</a>
    </section>'''
