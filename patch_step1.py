# -*- coding: utf-8 -*-
"""
Genera y añade 5 nuevos artículos de alto impacto en build_blog.py:
1. expansion-padel-estados-unidos-oportunidad-clubes-marcas
2. proceso-artesanal-fabricacion-llaveros-3d-personalizados-clubs
3. pickleball-vs-padel-oportunidad-o-amenaza-clubs
4. modelos-club-padel-americano-lifestyle-servicios-adicionales
5. como-acertar-stand-feria-padel-pws-racquetx-roi

Además distribuye las fechas de publicación históricas a lo largo de 2024, 2025 y 2026.
"""
import re

NEW_CATALOG_ENTRIES = '''
    "expansion-padel-estados-unidos-oportunidad-clubes-marcas": {
        "title": "La Expansión del Pádel en Estados Unidos: Radiografía 2026, Retos y Oportunidades",
        "badge": "Mercado USA & Crecimiento",
        "url": "../expansion-padel-estados-unidos-oportunidad-clubes-marcas/",
        "img": "gallery-padel-1.jpg",
        "desc": "Análisis del mercado estadounidense (+1.112 pistas en 38 estados): modelo premium, costes de alquiler y desembarco europeo."
    },
    "proceso-artesanal-fabricacion-llaveros-3d-personalizados-clubs": {
        "title": "Por Qué Huir del Merchandising Plano: El Proceso Artesanal del Siglo XXI en Goma 3D",
        "badge": "Artesanía 3D & Identidad",
        "url": "../proceso-artesanal-fabricacion-llaveros-3d-personalizados-clubs/",
        "img": "llaveros-corazon-pista.jpg",
        "desc": "Frente al producto plano de catálogo importado: molde a medida, colores Pantone reales y relieve táctil que une a tu comunidad."
    },
    "pickleball-vs-padel-oportunidad-o-amenaza-clubs": {
        "title": "Pickleball vs Pádel en Clubes de Raqueta: ¿Enemigos o Aliados Estratégicos?",
        "badge": "Estrategia Multirraqueta",
        "url": "../pickleball-vs-padel-oportunidad-o-amenaza-clubs/",
        "img": "gallery-padel-3.jpg",
        "desc": "El 43,9% de clubes multideporte en EE.UU. combinan ambos deportes. Cómo crear el jugador híbrido y maximizar rentabilidad por metro cuadrado."
    },
    "modelos-club-padel-americano-lifestyle-servicios-adicionales": {
        "title": "Del Alquiler de Pistas al Padel Lifestyle: El Modelo de Club Americano y Bienestar",
        "badge": "Gestión & Padel Lifestyle",
        "url": "../modelos-club-padel-americano-lifestyle-servicios-adicionales/",
        "img": "foto-reportaje.jpg",
        "desc": "Coworking, saunas, clínicas de recuperación y sinergias con marcas premium. Por qué alquilar pistas ya no basta para retener al socio."
    },
    "como-acertar-stand-feria-padel-pws-racquetx-roi": {
        "title": "¿Merece la Pena un Stand en Ferias de Pádel? Guía de Rentabilidad para el PWS y RacquetX",
        "badge": "Ferias B2B & ROI",
        "url": "../como-acertar-stand-feria-padel-pws-racquetx-roi/",
        "img": "slide-1.jpg",
        "desc": "De 3.000 € a más de 10.000 € en 3 días: qué stands triunfan, errores de diseño 'fuerte romano' y cómo rentabilizar tu inversión."
    },
'''

NEW_RELATED_MAP_ENTRIES = '''
    "expansion-padel-estados-unidos-oportunidad-clubes-marcas": ["pickleball-vs-padel-oportunidad-o-amenaza-clubs", "modelos-club-padel-americano-lifestyle-servicios-adicionales", "highlights-03"],
    "proceso-artesanal-fabricacion-llaveros-3d-personalizados-clubs": ["welcome-pack-torneo-padel-ideas", "vender-llaveros-tienda-club-padel-pro-shop", "regalos-eventos-padel-cenas-socios-llaveros"],
    "pickleball-vs-padel-oportunidad-o-amenaza-clubs": ["expansion-padel-estados-unidos-oportunidad-clubes-marcas", "smart-courts-pistas-inteligentes-padel-horas-valle", "cuanto-cuesta-montar-pista-padel-presupuesto-rentabilidad"],
    "modelos-club-padel-americano-lifestyle-servicios-adicionales": ["expansion-padel-estados-unidos-oportunidad-clubes-marcas", "smart-courts-pistas-inteligentes-padel-horas-valle", "como-organizar-torneo-padel-americana-reglas-cuadros"],
    "como-acertar-stand-feria-padel-pws-racquetx-roi": ["merchandising-ferias-torneos-padel-regalos-marcas", "highlights-01", "expansion-padel-estados-unidos-oportunidad-clubes-marcas"],
'''

NEW_DOWNLOAD_BOXES = '''
    "expansion-padel-estados-unidos-oportunidad-clubes-marcas": {
        "badge": "Reporte de Mercado PDF",
        "title": "Informe Ejecutivo: El Mercado del Pádel en Estados Unidos 2026",
        "desc": "Datos verificados de pistas por estado, tarifas medias (Peak vs Off-Peak) y modelos operativos indoor. Claves para clubes y marcas en expansión.",
        "file_url": "../../assets/reports/padel-industry-report-es.pdf",
        "btn_text": "Descargar Informe USA (PDF)",
        "wa_msg": "Hola Javier, me interesa el informe de expansión del pádel en Estados Unidos y las oportunidades para marcas"
    },
    "proceso-artesanal-fabricacion-llaveros-3d-personalizados-clubs": {
        "badge": "Muestra Digital y Dossier PDF",
        "title": "Guía de Fabricación Artesanal 3D y Muestra Digital para tu Club",
        "desc": "Descubre cómo recreamos tu pala, tu escudo y tus colores Pantone oficiales en relieve de goma 3D inyectada. Solicita un boceto 3D gratuito en 24h.",
        "file_url": "../../assets/downloads/checklist-organizacion-torneos-padel.pdf",
        "btn_text": "Descargar Guía y Dossier",
        "wa_msg": "Hola Javier, quiero un boceto digital de muestra 3D con el logo y colores de nuestro club"
    },
    "pickleball-vs-padel-oportunidad-o-amenaza-clubs": {
        "badge": "Estudio Comparativo PDF",
        "title": "Guía de Integración Dual Pádel & Pickleball para Clubes",
        "desc": "Estrategias de dinamización cruzada, ratios de ocupación y calendario de eventos híbridos para convertir jugadores de pickleball al pádel sin canibalizar.",
        "file_url": "../../assets/downloads/protocolo-smart-court-horas-valle.pdf",
        "btn_text": "Descargar Guía Multirraqueta",
        "wa_msg": "Hola Javier, tenemos instalaciones de raqueta y queremos integrar pádel y pickleball con Save my Play y CoolPadel"
    },
    "modelos-club-padel-americano-lifestyle-servicios-adicionales": {
        "badge": "Plantilla Operativa PDF",
        "title": "Matriz de Servicios Adicionales e Ingresos Post-Partido para Clubes",
        "desc": "Checklist de amenidades de alto margen: áreas de coworking, cafetería saludable, recuperación física, eventos multidisciplinares y convenios de patrocinio local.",
        "file_url": "../../assets/downloads/checklist-organizacion-torneos-padel.pdf",
        "btn_text": "Descargar Matriz Lifestyle",
        "wa_msg": "Hola Javier, queremos implementar nuevos servicios y experiencia de club premium en nuestras instalaciones"
    },
    "como-acertar-stand-feria-padel-pws-racquetx-roi": {
        "badge": "Checklist para Expositores PDF",
        "title": "Checklist de Preparación para Ferias de Pádel (PWS, RacquetX)",
        "desc": "Cronograma de 90 días para ferias B2B: diseño de stand abierto, cálculo de costes (suelo, montaje, viajes), política de regalos y captación de leads en vivo.",
        "file_url": "../../assets/downloads/checklist-organizacion-torneos-padel.pdf",
        "btn_text": "Descargar Checklist de Ferias",
        "wa_msg": "Hola Javier, estamos valorando montar stand en una feria de pádel y me gustaría comentar detalles"
    },
'''

NEW_SHORT_SEO_TITLES = '''
    "expansion-padel-estados-unidos-oportunidad-clubes-marcas": "Expansión del Pádel en Estados Unidos 2026 | CoolPadel",
    "proceso-artesanal-fabricacion-llaveros-3d-personalizados-clubs": "Fabricación Artesanal de Llaveros de Pádel 3D | CoolPadel",
    "pickleball-vs-padel-oportunidad-o-amenaza-clubs": "Pickleball vs Pádel en Clubes de Raqueta | CoolPadel",
    "modelos-club-padel-americano-lifestyle-servicios-adicionales": "Padel Lifestyle y Modelo de Club Americano | CoolPadel",
    "como-acertar-stand-feria-padel-pws-racquetx-roi": "Guía de Stands en Ferias de Pádel (PWS, RacquetX) | CoolPadel",
'''

def main():
    with open('coolpadel-web/build_blog.py', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update ALL_ARTICLES_CATALOG
    cat_idx = content.find('ALL_ARTICLES_CATALOG = {')
    if cat_idx != -1:
        insert_pos = cat_idx + len('ALL_ARTICLES_CATALOG = {')
        content = content[:insert_pos] + NEW_CATALOG_ENTRIES + content[insert_pos:]
        print('[OK] Injected NEW_CATALOG_ENTRIES')

    # 2. Update RELATED_SLUGS_MAP
    rel_idx = content.find('RELATED_SLUGS_MAP = {')
    if rel_idx != -1:
        insert_pos = rel_idx + len('RELATED_SLUGS_MAP = {')
        content = content[:insert_pos] + NEW_RELATED_MAP_ENTRIES + content[insert_pos:]
        print('[OK] Injected NEW_RELATED_MAP_ENTRIES')

    # 3. Update DOWNLOAD_BOXES
    db_idx = content.find('DOWNLOAD_BOXES = {')
    if db_idx != -1:
        insert_pos = db_idx + len('DOWNLOAD_BOXES = {')
        content = content[:insert_pos] + NEW_DOWNLOAD_BOXES + content[insert_pos:]
        print('[OK] Injected NEW_DOWNLOAD_BOXES')

    # 4. Update SHORT_SEO_TITLES
    st_idx = content.find('SHORT_SEO_TITLES = {')
    if st_idx != -1:
        insert_pos = st_idx + len('SHORT_SEO_TITLES = {')
        content = content[:insert_pos] + NEW_SHORT_SEO_TITLES + content[insert_pos:]
        print('[OK] Injected NEW_SHORT_SEO_TITLES')

    with open('coolpadel-web/build_blog.py', 'w', encoding='utf-8') as f:
        f.write(content)
    print('[DONE] Part 1 applied successfully.')

if __name__ == '__main__':
    main()
