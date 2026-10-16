import re
from pathlib import Path

target = Path("coolpadel-web/build_landing_pages.py")
content = target.read_text(encoding="utf-8")

# Let's inspect where render_landing starts and replace its variables and template
old_section = '''    # Dynamic Product / Service Schema per landing type
    if landing["slug"] == "camaras-grabacion-pistas-padel":'''

new_variables = '''    is_camaras = landing["slug"] == "camaras-grabacion-pistas-padel"
    breadcrumb_name = "Cámaras en Pista" if is_camaras else "Llaveros Personalizados"
    cta_hero_text = "Solicitar Demo / Presupuesto" if is_camaras else "Solicitar Muestra / Cotización"

    if is_camaras:
        hero_badges_html = """
              <span class="flex items-center gap-1.5"><i data-lucide="check-circle" class="w-4 h-4 text-[#f2920b]"></i> 0 obras · Montaje 5 min</span>
              <span class="flex items-center gap-1.5"><i data-lucide="check-circle" class="w-4 h-4 text-[#f2920b]"></i> 0 permanencia</span>
              <span class="flex items-center gap-1.5"><i data-lucide="check-circle" class="w-4 h-4 text-[#f2920b]"></i> Descarga instantánea QR</span>"""
        why_title = "¿Por qué elegir Save My Play para tu club?"
        why_sub = "La tecnología de grabación y analítica en pista más ágil, sin obras ni costes ocultos"
        precios_title = "Tarifas Oficiales Save My Play B2B"
        precios_sub = "Hardware en propiedad sin permanencia y cuota mensual de software por pista"
        table_html = f"""
          <div class="overflow-x-auto">
            <table class="w-full text-left text-sm sm:text-base">
              <thead>
                <tr class="border-b border-slate-200 text-xs uppercase tracking-wider text-slate-500">
                  <th class="py-3 px-3">Concepto / Plan</th>
                  <th class="py-3 px-3">Inversión / Cuota</th>
                  <th class="py-3 px-3">Modalidad</th>
                  <th class="py-3 px-3">Servicios Incluidos</th>
                </tr>
              </thead>
              <tbody class="divide-y divide-slate-100 font-bold">
                <tr>
                  <td class="py-4 px-3 text-slate-900">Inversión Hardware por Pista</td>
                  <td class="py-4 px-3 text-[#f2920b]">180 € / pista</td>
                  <td class="py-4 px-3 text-slate-700">Pago único (en propiedad)</td>
                  <td class="py-4 px-3 text-slate-600 text-xs font-medium">Cámara deportiva panorámica HD + fijación a poste + pulsador físico</td>
                </tr>
                <tr>
                  <td class="py-4 px-3 text-slate-900">Plan B · Highlights & Streaming (Recomendado)</td>
                  <td class="py-4 px-3 text-[#f2920b]">45 € / mes</td>
                  <td class="py-4 px-3 text-emerald-600">0 permanencia · Cancelación libre</td>
                  <td class="py-4 px-3 text-slate-600 text-xs font-medium">Grabación de partidos, repeticiones botón en poste, clips automáticos, streaming YouTube y descarga QR</td>
                </tr>
                <tr>
                  <td class="py-4 px-3 text-slate-900">Plan A · Analítica IA Avanzada</td>
                  <td class="py-4 px-3 text-[#f2920b]">136 € / mes</td>
                  <td class="py-4 px-3 text-emerald-600">0 permanencia · Cancelación libre</td>
                  <td class="py-4 px-3 text-slate-600 text-xs font-medium">Todo el Plan B + AI Analytics táctico, mapas de calor, recuento de golpes y métricas</td>
                </tr>
              </tbody>
            </table>
          </div>
          
          <div class="mt-6 pt-5 border-t border-slate-100 flex flex-col sm:flex-row items-center justify-between gap-4">
            <span class="text-xs text-slate-500">* Precios sin IVA. Sin contratos de permanencia ni penalizaciones. Instalación en 5 minutos sin obras civiles.</span>
            <a href="https://wa.me/34680317486?text={wa_encoded}" target="_blank" rel="noopener noreferrer" class="px-6 py-3 rounded-full bg-[#f2920b] hover:bg-[#76d3f6] text-slate-950 font-heading font-black text-xs uppercase tracking-wider transition">
              Pedir Presupuesto / Demo por WhatsApp
            </a>
          </div>"""
        pasos_html = """
        <div class="grid sm:grid-cols-3 gap-6 text-center">
          <div class="space-y-2">
            <div class="w-10 h-10 rounded-full bg-white/20 text-white font-heading font-black text-base flex items-center justify-center mx-auto">1</div>
            <h3 class="font-heading font-black text-lg">Demo Online (15 min)</h3>
            <p class="text-white/80 text-xs">Te mostramos en vivo cómo funciona la cámara, el pulsador y la descarga instantánea por QR.</p>
          </div>
          <div class="space-y-2">
            <div class="w-10 h-10 rounded-full bg-white/20 text-white font-heading font-black text-base flex items-center justify-center mx-auto">2</div>
            <h3 class="font-heading font-black text-lg">Instalación en 5 min</h3>
            <p class="text-white/80 text-xs">Se fija directamente al poste de la pista sin obras, sin zanjas y sin cortar horas de juego.</p>
          </div>
          <div class="space-y-2">
            <div class="w-10 h-10 rounded-full bg-white/20 text-white font-heading font-black text-base flex items-center justify-center mx-auto">3</div>
            <h3 class="font-heading font-black text-lg">Activación y Sin Permanencia</h3>
            <p class="text-white/80 text-xs">Tus jugadores disfrutan de sus mejores jugadas. Puedes darte de baja en cualquier momento.</p>
          </div>
        </div>"""
    else:
        hero_badges_html = """
              <span class="flex items-center gap-1.5"><i data-lucide="check-circle" class="w-4 h-4 text-[#f2920b]"></i> Muestra 15€ con envío</span>
              <span class="flex items-center gap-1.5"><i data-lucide="check-circle" class="w-4 h-4 text-[#f2920b]"></i> Pedido mín. 100 uds</span>
              <span class="flex items-center gap-1.5"><i data-lucide="check-circle" class="w-4 h-4 text-[#f2920b]"></i> Fabricación 7-10 días</span>"""
        why_title = "¿Por qué elegir CoolPadel Studios?"
        why_sub = "Acabado profesional de tienda oficial para elevar la imagen de tu club o evento"
        precios_title = "Tarifas Directas de Fabricación B2B"
        precios_sub = "Precios sin intermediarios adaptados al volumen de socios o jugadores"
        table_html = f"""
          <div class="overflow-x-auto">
            <table class="w-full text-left text-sm sm:text-base">
              <thead>
                <tr class="border-b border-slate-200 text-xs uppercase tracking-wider text-slate-500">
                  <th class="py-3 px-3">Tirada</th>
                  <th class="py-3 px-3">Precio Unitario</th>
                  <th class="py-3 px-3">Total Estimado</th>
                  <th class="py-3 px-3">Muestra Física Previa</th>
                </tr>
              </thead>
              <tbody class="divide-y divide-slate-100 font-bold">
                <tr>
                  <td class="py-4 px-3 text-slate-900">100 unidades (Mínimo)</td>
                  <td class="py-4 px-3 text-[#f2920b]">3,00 € / ud</td>
                  <td class="py-4 px-3 text-slate-700">300 € (+IVA)</td>
                  <td class="py-4 px-3 text-slate-500 text-xs">15 € (100% deducible)</td>
                </tr>
                <tr>
                  <td class="py-4 px-3 text-slate-900">250 unidades</td>
                  <td class="py-4 px-3 text-[#f2920b]">2,40 € / ud</td>
                  <td class="py-4 px-3 text-slate-700">600 € (+IVA)</td>
                  <td class="py-4 px-3 text-slate-500 text-xs">Incluida y deducible</td>
                </tr>
                <tr>
                  <td class="py-4 px-3 text-slate-900">500 unidades</td>
                  <td class="py-4 px-3 text-[#f2920b]">2,00 € / ud</td>
                  <td class="py-4 px-3 text-slate-700">1.000 € (+IVA)</td>
                  <td class="py-4 px-3 text-slate-500 text-xs">Incluida y deducible</td>
                </tr>
                <tr>
                  <td class="py-4 px-3 text-slate-900">1.500 unidades</td>
                  <td class="py-4 px-3 text-[#f2920b]">1,50 € / ud</td>
                  <td class="py-4 px-3 text-slate-700">2.250 € (+IVA)</td>
                  <td class="py-4 px-3 text-slate-500 text-xs">Tarifa directa gran volumen</td>
                </tr>
              </tbody>
            </table>
          </div>
          
          <div class="mt-6 pt-5 border-t border-slate-100 flex flex-col sm:flex-row items-center justify-between gap-4">
            <span class="text-xs text-slate-500">* Precios sin IVA. Envíos incluidos a toda España peninsular y Unión Europea.</span>
            <a href="https://wa.me/34680317486?text={wa_encoded}" target="_blank" rel="noopener noreferrer" class="px-6 py-3 rounded-full bg-[#f2920b] hover:bg-[#76d3f6] text-slate-950 font-heading font-black text-xs uppercase tracking-wider transition">
              Pedir Presupuesto por WhatsApp
            </a>
          </div>"""
        pasos_html = """
        <div class="grid sm:grid-cols-3 gap-6 text-center">
          <div class="space-y-2">
            <div class="w-10 h-10 rounded-full bg-white/20 text-white font-heading font-black text-base flex items-center justify-center mx-auto">1</div>
            <h3 class="font-heading font-black text-lg">Envías tu Logotipo</h3>
            <p class="text-white/80 text-xs">Preparamos el diseño digital 3D sin coste para validar proporciones y colores.</p>
          </div>
          <div class="space-y-2">
            <div class="w-10 h-10 rounded-full bg-white/20 text-white font-heading font-black text-base flex items-center justify-center mx-auto">2</div>
            <h3 class="font-heading font-black text-lg">Muestra Física (15€)</h3>
            <p class="text-white/80 text-xs">Fabricamos una muestra real enviada a tu dirección. Los 15€ se descuentan del pedido.</p>
          </div>
          <div class="space-y-2">
            <div class="w-10 h-10 rounded-full bg-white/20 text-white font-heading font-black text-base flex items-center justify-center mx-auto">3</div>
            <h3 class="font-heading font-black text-lg">Producción y Entrega</h3>
            <p class="text-white/80 text-xs">Fabricación final desde 100 uds y entrega en 7-10 días hábiles.</p>
          </div>
        </div>"""

    # Dynamic Product / Service Schema per landing type
    if landing["slug"] == "camaras-grabacion-pistas-padel":'''

content = content.replace(old_section, new_variables)

# Replace breadcrumb
content = content.replace(
    '<span class="text-[#f2920b]">Llaveros Personalizados</span>',
    '<span class="text-[#f2920b]">{breadcrumb_name}</span>'
)

# Replace cta button text
content = content.replace(
    '<span>Solicitar Muestra / Cotización</span>',
    '<span>{cta_hero_text}</span>'
)

# Replace hero badges
old_hero_badges = '''            <div class="pt-3 flex items-center gap-4 text-xs font-bold text-slate-500">
              <span class="flex items-center gap-1.5"><i data-lucide="check-circle" class="w-4 h-4 text-[#f2920b]"></i> Muestra 15€ con envío</span>
              <span class="flex items-center gap-1.5"><i data-lucide="check-circle" class="w-4 h-4 text-[#f2920b]"></i> Pedido mín. 100 uds</span>
              <span class="flex items-center gap-1.5"><i data-lucide="check-circle" class="w-4 h-4 text-[#f2920b]"></i> Fabricación 7-10 días</span>
            </div>'''
new_hero_badges = '''            <div class="pt-3 flex items-center gap-4 text-xs font-bold text-slate-500">
              {hero_badges_html}
            </div>'''
content = content.replace(old_hero_badges, new_hero_badges)

# Replace why section
old_why = '''          <h2 class="font-heading font-black text-2xl sm:text-4xl text-slate-950 uppercase tracking-tight">
            ¿Por qué elegir CoolPadel Studios?
          </h2>
          <p class="text-sm sm:text-base text-slate-600 font-medium">
            Acabado profesional de tienda oficial para elevar la imagen de tu club o evento
          </p>'''
new_why = '''          <h2 class="font-heading font-black text-2xl sm:text-4xl text-slate-950 uppercase tracking-tight">
            {why_title}
          </h2>
          <p class="text-sm sm:text-base text-slate-600 font-medium">
            {why_sub}
          </p>'''
content = content.replace(old_why, new_why)

# Replace pricing header
old_precios_head = '''          <h2 class="font-heading font-black text-2xl sm:text-4xl uppercase tracking-tight">
            Tarifas Directas de Fabricación B2B
          </h2>
          <p class="text-white/80 text-sm sm:text-base">
            Precios sin intermediarios adaptados al volumen de socios o jugadores
          </p>'''
new_precios_head = '''          <h2 class="font-heading font-black text-2xl sm:text-4xl uppercase tracking-tight">
            {precios_title}
          </h2>
          <p class="text-white/80 text-sm sm:text-base">
            {precios_sub}
          </p>'''
content = content.replace(old_precios_head, new_precios_head)

# Replace table block
old_table_block = '''        <!-- Tabla de Tarifas -->
        <div class="bg-white rounded-3xl p-6 sm:p-8 text-slate-950 shadow-2xl mb-12">
          <div class="overflow-x-auto">
            <table class="w-full text-left text-sm sm:text-base">
              <thead>
                <tr class="border-b border-slate-200 text-xs uppercase tracking-wider text-slate-500">
                  <th class="py-3 px-3">Tirada</th>
                  <th class="py-3 px-3">Precio Unitario</th>
                  <th class="py-3 px-3">Total Estimado</th>
                  <th class="py-3 px-3">Muestra Física Previa</th>
                </tr>
              </thead>
              <tbody class="divide-y divide-slate-100 font-bold">
                <tr>
                  <td class="py-4 px-3 text-slate-900">100 unidades (Mínimo)</td>
                  <td class="py-4 px-3 text-[#f2920b]">3,00 € / ud</td>
                  <td class="py-4 px-3 text-slate-700">300 € (+IVA)</td>
                  <td class="py-4 px-3 text-slate-500 text-xs">15 € (100% deducible)</td>
                </tr>
                <tr>
                  <td class="py-4 px-3 text-slate-900">250 unidades</td>
                  <td class="py-4 px-3 text-[#f2920b]">2,40 € / ud</td>
                  <td class="py-4 px-3 text-slate-700">600 € (+IVA)</td>
                  <td class="py-4 px-3 text-slate-500 text-xs">Incluida y deducible</td>
                </tr>
                <tr>
                  <td class="py-4 px-3 text-slate-900">500 unidades</td>
                  <td class="py-4 px-3 text-[#f2920b]">2,00 € / ud</td>
                  <td class="py-4 px-3 text-slate-700">1.000 € (+IVA)</td>
                  <td class="py-4 px-3 text-slate-500 text-xs">Incluida y deducible</td>
                </tr>
                <tr>
                  <td class="py-4 px-3 text-slate-900">1.500 unidades</td>
                  <td class="py-4 px-3 text-[#f2920b]">1,50 € / ud</td>
                  <td class="py-4 px-3 text-slate-700">2.250 € (+IVA)</td>
                  <td class="py-4 px-3 text-slate-500 text-xs">Tarifa directa gran volumen</td>
                </tr>
              </tbody>
            </table>
          </div>
          
          <div class="mt-6 pt-5 border-t border-slate-100 flex flex-col sm:flex-row items-center justify-between gap-4">
            <span class="text-xs text-slate-500">* Precios sin IVA. Envíos incluidos a toda España peninsular y Unión Europea.</span>
            <a href="https://wa.me/34680317486?text={wa_encoded}" target="_blank" rel="noopener noreferrer" class="px-6 py-3 rounded-full bg-[#f2920b] hover:bg-[#76d3f6] text-slate-950 font-heading font-black text-xs uppercase tracking-wider transition">
              Pedir Presupuesto por WhatsApp
            </a>
          </div>
        </div>'''
new_table_block = '''        <!-- Tabla de Tarifas -->
        <div class="bg-white rounded-3xl p-6 sm:p-8 text-slate-950 shadow-2xl mb-12">
          {table_html}
        </div>'''
content = content.replace(old_table_block, new_table_block)

# Replace 3 steps
old_steps = '''        <!-- Proceso en 3 pasos -->
        <div class="grid sm:grid-cols-3 gap-6 text-center">
          <div class="space-y-2">
            <div class="w-10 h-10 rounded-full bg-white/20 text-white font-heading font-black text-base flex items-center justify-center mx-auto">1</div>
            <h3 class="font-heading font-black text-lg">Envías tu Logotipo</h3>
            <p class="text-white/80 text-xs">Preparamos el diseño digital 3D sin coste para validar proporciones y colores.</p>
          </div>
          <div class="space-y-2">
            <div class="w-10 h-10 rounded-full bg-white/20 text-white font-heading font-black text-base flex items-center justify-center mx-auto">2</div>
            <h3 class="font-heading font-black text-lg">Muestra Física (15€)</h3>
            <p class="text-white/80 text-xs">Fabricamos una muestra real enviada a tu dirección. Los 15€ se descuentan del pedido.</p>
          </div>
          <div class="space-y-2">
            <div class="w-10 h-10 rounded-full bg-white/20 text-white font-heading font-black text-base flex items-center justify-center mx-auto">3</div>
            <h3 class="font-heading font-black text-lg">Producción y Entrega</h3>
            <p class="text-white/80 text-xs">Fabricación final desde 100 uds y entrega en 7-10 días hábiles.</p>
          </div>
        </div>'''
new_steps = '''        <!-- Proceso en 3 pasos -->
        {pasos_html}'''
content = content.replace(old_steps, new_steps)

target.write_text(content, encoding="utf-8")
print("Successfully updated build_landing_pages.py with dynamic camera pricing and steps!")
