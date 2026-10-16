import os
import json
import urllib.parse
from translations_data import TRANSLATIONS

CLUB_NAMES_MAP = {
    2: 'Club de Tenis Cambados',
    3: 'Pinondo Padel Zaleak',
    4: 'Tenis Club El Soto (Zaragoza)',
    5: 'Fiorfiore Padel (Italia)',
    6: 'Tennis Life Canzo (Italia)',
    7: 'Club Deportivo Pádel Higueruela',
    8: 'Vitasports Escuela de Tenis y Pádel',
    9: 'Club de Pádel Ortigueira',
    10: "Tennis Club Sant'Agostino (Italia)",
    11: 'Club Tennis Reus Monterols',
    12: 'Club Pádel Vilamalla',
    13: "Padel Club Cabrera d'Anoia",
    14: 'ALM Évreux Tennis Padel (Francia)',
    15: 'Club Green Park (Italia)',
    16: 'Royal Excelsior Tennis Club (Bélgica)',
    17: 'Le Garden Rennes (Francia)',
    18: 'Austrian Padel Union (Austria)',
    19: 'Padel Alba (Alicante)',
    20: 'Padeleiros Vigo',
    21: 'A.T.M. Amigos del Tenis de Málaga',
    22: 'CBS Padel (Dinamarca)',
    23: 'USP Tennis 17 (París)',
    24: 'Padel Kiosk (Bélgica)',
    25: 'Padel Addict',
    26: 'Backspin Academy (Madrid)',
    27: 'Espacio Herrería (Madrid)',
}

def get_base_html(active_lang="es", is_subfolder=False):
    t = TRANSLATIONS[active_lang]
    # Diccionario limpio de etiquetas HTML para Schema JSON-LD
    t_clean = {k: v.replace('<br>', ' ') if isinstance(v, str) else v for k, v in t.items()}
    asset_prefix = "../" if is_subfolder else ""
    
    ticker_items = []
    for idx, i in enumerate(list(range(2, 28)) * 2):
        c_name = CLUB_NAMES_MAP.get(i, f"Club #{i}")
        is_duplicate = idx >= 26
        aria_attr = ' aria-hidden="true"' if is_duplicate else ''
        alt_text = "" if is_duplicate else f"Logo de {c_name}, club cliente de CoolPadel Studios"
        ticker_items.append(
            f'<div class="flex items-center justify-center shrink-0 px-2.5 sm:px-5 group"{aria_attr}>'
            f'<img src="{asset_prefix}assets/images/Clubs/client-{str(i).zfill(2)}.png" '
            f'alt="{alt_text}" '
            f'width="140" height="56" '
            f'class="h-10 sm:h-14 lg:h-16 w-auto max-w-[110px] sm:max-w-[180px] object-contain transition-all duration-300 hover:scale-110" '
            f'loading="lazy" decoding="async"></div>'
        )
    ticker_html = "".join(ticker_items)

    club_list_items = [f"<li>{cname}</li>" for cid, cname in sorted(CLUB_NAMES_MAP.items())]
    club_list_html = "".join(club_list_items)
    wa_prefilled_encoded = urllib.parse.quote(t.get('wa_prefilled_msg', 'Hola Javier'))

    # Pre-calcular JSON de traducciones para inyectar en JS
    translations_json = json.dumps(TRANSLATIONS, ensure_ascii=False)

    og_locales = {"es": "es_ES", "en": "en_US", "fr": "fr_FR", "it": "it_IT"}
    og_locale = og_locales.get(active_lang, "es_ES")
    page_url = f"https://coolpadelstudios.com/{active_lang + '/' if is_subfolder else ''}"

    seo_i18n = {
        "es": {
            "og_img_alt": "Llaveros de pádel personalizados en relieve 3D CoolPadel Studios",
            "org_desc": "Fabricante y distribuidor directo de llaveros de pádel personalizados de goma 3D para clubes deportivos y marcas, y partner oficial de cámaras en pista Save my Play.",
            "bc_home": "Inicio",
            "bc_llaveros": "Llaveros de Pádel",
            "prod_name": "Llaveros de Pádel Personalizados 3D - CoolPadel Studios",
            "prod_desc": "Llaveros de pádel personalizados de goma 3D de alta densidad con el logotipo oficial del club o comunidad. Muestra física real por 15€ (~15 días laborables, 100% deducible) y pedidos desde 100 unidades con entrega en torno a un mes y envíos incluidos.",
            "prod_material": "Goma y Silicona PVC 3D de alta densidad con anilla metálica reforzada",
            "howto_name": "Cómo encargar llaveros de pádel personalizados para tu club",
            "howto_desc": "Proceso oficial en 3 pasos para diseñar y fabricar llaveros de pádel en relieve 3D con muestra física real previa.",
            "step1_name": "Envío de logotipo y diseño 3D",
            "step1_text": "Envíanos el logo de tu club en cualquier formato para preparar el render digital 3D a ordenador sin coste.",
            "step2_name": "Muestra física real por 15€",
            "step2_text": "Fabricamos y enviamos una muestra física real con el logo de tu club en ~15 días laborables (15€ descontables al 100% del pedido final).",
            "step3_name": "Confirmación y fabricación del pedido",
            "step3_text": "Producción en serie desde 100 unidades (1,50€ a 3,00€/ud) y entrega en torno a un mes según volumen con envíos incluidos.",
            "sr_h2": "Llaveros de Pádel Personalizados 3D CoolPadel Studios",
            "sr_p": "Fabricante B2B especializado en llaveros de pádel y tenis personalizados en relieve 3D de goma microinyectada de alta densidad para clubes, torneos y federaciones. Pedidos al por mayor desde 100 unidades con tarifa directa de fábrica de 1,50€ a 3,00€ por unidad (100 uds: 300€ | 250 uds: 625€ | 500 uds: 1.000€ | 1.500 uds: 2.250€). Muestra física real personalizada previa por 15€ en ~15 días laborables (100% reembolsable con el pedido final). Entrega del pedido en torno a un mes según volumen en España, Europa y EE. UU.",
            "sr_caption": "Tarifas oficiales de fabricación al por mayor de llaveros de pádel personalizados 3D CoolPadel Studios",
            "sr_th_tier": "Tramo de volumen",
            "sr_th_unit": "Precio unitario",
            "sr_th_total": "Importe estimado",
            "sr_th_cond": "Condiciones y Plazos",
            "sr_r1_c1": "100 unidades (Pedido mínimo)",
            "sr_r1_c4": "Muestra física real en ~15 días laborables: 15€ (100% descontable del pedido final)",
            "sr_r2_c1": "250 unidades",
            "sr_r2_c4": "Muestra física descontable · Entrega del pedido en ~1 mes",
            "sr_r3_c1": "500 unidades",
            "sr_r3_c4": "Muestra física descontable y envíos incluidos · Entrega en ~1 mes",
            "sr_r4_c1": "1.500 unidades",
            "sr_r4_c4": "Tarifa directa de fábrica gran volumen · Envíos incluidos",
            "map_h3": "Clubs y Marcas con Llaveros CoolPadel",
            "map_p": "Selecciona una zona o haz clic en cualquier marcador para explorar nuestros clubs oficiales",
            "sr_clubs_h4": "Clubes, academias y federaciones clientes oficiales de CoolPadel Studios:"
        },
        "en": {
            "og_img_alt": "Custom 3D rubber padel keychains for clubs by CoolPadel Studios",
            "org_desc": "Direct B2B manufacturer of custom 3D rubber padel and tennis keychains for sports clubs, tournaments and brands, and official partner of Save my Play court cameras.",
            "bc_home": "Home",
            "bc_llaveros": "Custom Padel Keychains",
            "prod_name": "Custom 3D Padel Keychains - CoolPadel Studios",
            "prod_desc": "High-density custom 3D rubber padel keychains featuring your official club or tournament logo. Real physical sample for 15€ (~15 business days, 100% deducted from final order), minimum order from 100 units, delivery in ~1 month with shipping included.",
            "prod_material": "High-density 3D micro-injected PVC & silicone rubber with reinforced metal keyring",
            "howto_name": "How to order custom padel keychains for your club",
            "howto_desc": "Official 3-step guided process to design and manufacture custom 3D padel keychains with a real physical sample.",
            "step1_name": "Send your logo & free 3D digital mockup",
            "step1_text": "Send us your club logo in any format to prepare a 3D digital computer mockup at no cost.",
            "step2_name": "Real physical sample for 15€",
            "step2_text": "We manufacture and ship a real physical sample with your club logo in ~15 business days (15€ is 100% deducted from the final order).",
            "step3_name": "Order confirmation & mass manufacturing",
            "step3_text": "Series production from 100 units (1.50€ to 3.00€/unit) with delivery in about one month depending on volume and shipping included.",
            "sr_h2": "Custom 3D Padel Keychains CoolPadel Studios",
            "sr_p": "B2B manufacturer specializing in custom 3D micro-injected rubber padel and tennis keychains for clubs, tournaments and federations. Wholesale orders from 100 units at direct factory pricing from 1.50€ to 3.00€ per unit (100 units: 300€ | 250 units: 625€ | 500 units: 1,000€ | 1,500 units: 2,250€). Real custom physical sample for 15€ delivered in ~15 business days (100% deducted from the final order). Full order delivery in about one month across Spain, Europe and the USA.",
            "sr_caption": "Official wholesale manufacturing prices for custom 3D padel keychains by CoolPadel Studios",
            "sr_th_tier": "Volume tier",
            "sr_th_unit": "Unit price",
            "sr_th_total": "Estimated total",
            "sr_th_cond": "Terms & Lead Time",
            "sr_r1_c1": "100 units (Minimum order)",
            "sr_r1_c4": "Real physical sample in ~15 business days: 15€ (100% deducted from final order)",
            "sr_r2_c1": "250 units",
            "sr_r2_c4": "Deductible physical sample · Full order delivery in ~1 month",
            "sr_r3_c1": "500 units",
            "sr_r3_c4": "Deductible physical sample & shipping included · Delivery in ~1 month",
            "sr_r4_c1": "1,500 units",
            "sr_r4_c4": "Direct factory high-volume tier · Shipping included",
            "map_h3": "Clubs & Brands with CoolPadel Keychains",
            "map_p": "Select a region or click any marker to explore our official client clubs",
            "sr_clubs_h4": "Official clubs, academies and federations trusting CoolPadel Studios:"
        },
        "fr": {
            "og_img_alt": "Porte-clés de padel personnalisés en relief 3D CoolPadel Studios",
            "org_desc": "Fabricant B2B direct de porte-clés de padel et tennis personnalisés en gomme 3D pour clubs sportifs et tournois, et partenaire officiel des caméras Save my Play.",
            "bc_home": "Accueil",
            "bc_llaveros": "Porte-clés Padel",
            "prod_name": "Porte-clés Padel Personnalisés 3D - CoolPadel Studios",
            "prod_desc": "Porte-clés de padel personnalisés en gomme 3D haute densité avec le logo officiel de votre club ou tournoi. Échantillon physique réel pour 15€ (~15 jours ouvrés, 100% déduit de la commande), commande dès 100 unités et livraison en environ un mois avec frais de port inclus.",
            "prod_material": "Gomme PVC et silicone 3D haute densité avec anneau métallique renforcé",
            "howto_name": "Comment commander des porte-clés de padel personnalisés pour votre club",
            "howto_desc": "Processus officiel en 3 étapes pour concevoir et fabriquer des porte-clés de padel en relief 3D avec échantillon physique réel.",
            "step1_name": "Envoi du logo et modélisation 3D",
            "step1_text": "Envoyez-nous le logo de votre club pour recevoir une maquette numérique 3D sur ordinateur sans frais.",
            "step2_name": "Échantillon physique réel pour 15€",
            "step2_text": "Fabrication et expédition d'un échantillon physique réel avec votre logo sous ~15 jours ouvrés (les 15€ sont déduits à 100% de la commande finale).",
            "step3_name": "Validation et fabrication de la commande",
            "step3_text": "Production en série dès 100 unités (1,50€ à 3,00€/unité) et livraison en un mois environ selon le volume, port inclus.",
            "sr_h2": "Porte-clés de Padel Personnalisés 3D CoolPadel Studios",
            "sr_p": "Fabricant B2B spécialisé dans les porte-clés de padel et tennis personnalisés en relief 3D pour clubs, tournois et fédérations. Commandes dès 100 unités au tarif direct usine de 1,50€ à 3,00€ par unité (100 u. : 300€ | 250 u. : 625€ | 500 u. : 1 000€ | 1 500 u. : 2 250€). Échantillon physique réel préalable pour 15€ sous ~15 jours ouvrés (100% remboursé sur la commande finale). Livraison de la commande en environ un mois en France, Europe et USA.",
            "sr_caption": "Tarifs officiels de fabrication en gros de porte-clés de padel personnalisés 3D CoolPadel Studios",
            "sr_th_tier": "Palier de volume",
            "sr_th_unit": "Prix unitaire",
            "sr_th_total": "Montant estimé",
            "sr_th_cond": "Conditions et Délais",
            "sr_r1_c1": "100 unités (Commande minimale)",
            "sr_r1_c4": "Échantillon physique réel sous ~15 jours ouvrés : 15€ (100% déduit de la commande)",
            "sr_r2_c1": "250 unités",
            "sr_r2_c4": "Échantillon physique déductible · Livraison en ~1 mois",
            "sr_r3_c1": "500 unités",
            "sr_r3_c4": "Échantillon déductible et livraison incluse · Délai ~1 mois",
            "sr_r4_c1": "1 500 unités",
            "sr_r4_c4": "Tarif direct usine grand volume · Livraison incluse",
            "map_h3": "Clubs & Marques avec Porte-clés CoolPadel",
            "map_p": "Sélectionnez une zone ou cliquez sur un marqueur pour découvrir nos clubs officiels",
            "sr_clubs_h4": "Clubs, académies et fédérations clientes officielles de CoolPadel Studios :"
        },
        "it": {
            "og_img_alt": "Portachiavi da padel personalizzati in rilievo 3D CoolPadel Studios",
            "org_desc": "Produttore e distributore diretto B2B di portachiavi da padel e tennis personalizzati in gomma 3D per club sportivi e tornei, e partner ufficiale delle telecamere Save my Play.",
            "bc_home": "Home",
            "bc_llaveros": "Portachiavi Padel",
            "prod_name": "Portachiavi Padel Personalizzati 3D - CoolPadel Studios",
            "prod_desc": "Portachiavi da padel personalizzati in gomma 3D ad alta densità con il logo ufficiale del club o torneo. Campione fisico reale a 15€ (~15 giorni lavorativi, 100% scalato dall'ordine finale), ordini da 100 unità e consegna in circa un mese con spedizione inclusa.",
            "prod_material": "Gomma PVC e silicone 3D ad alta densità con anello metallico rinforzato",
            "howto_name": "Come ordinare portachiavi da padel personalizzati per il tuo club",
            "howto_desc": "Procedura ufficiale in 3 fasi per progettare e produrre portachiavi da padel in rilievo 3D con campione fisico reale.",
            "step1_name": "Invio del logo e progettazione 3D",
            "step1_text": "Inviaci il logo del tuo club per preparare il render digitale 3D al computer senza costi.",
            "step2_name": "Campione fisico reale a 15€",
            "step2_text": "Produciamo e spediamo un campione fisico reale con il logo del tuo club in ~15 giorni lavorativi (i 15€ vengono dedotti al 100% dall'ordine finale).",
            "step3_name": "Conferma e produzione dell'ordine",
            "step3_text": "Produzione in serie da 100 unità (da 1,50€ a 3,00€/unità) e consegna in circa un mese in base al volume con spedizione inclusa.",
            "sr_h2": "Portachiavi Padel Personalizzati 3D CoolPadel Studios",
            "sr_p": "Produttore B2B specializzato in portachiavi da padel e tennis personalizzati in rilievo 3D per club, tornei e federazioni. Ordini all'ingrosso da 100 unità a prezzo diretto di fabbrica da 1,50€ a 3,00€ per unità (100 u.: 300€ | 250 u.: 625€ | 500 u.: 1.000€ | 1.500 u.: 2.250€). Campione fisico reale personalizzato a 15€ in ~15 giorni lavorativi (100% rimborsabile con l'ordine finale). Consegna dell'ordine in circa un mese in Italia, Europa e USA.",
            "sr_caption": "Tariffe ufficiali di produzione all'ingrosso di portachiavi da padel personalizzati 3D CoolPadel Studios",
            "sr_th_tier": "Fascia di volume",
            "sr_th_unit": "Prezzo unitario",
            "sr_th_total": "Importo stimato",
            "sr_th_cond": "Condizioni e Tempi",
            "sr_r1_c1": "100 unità (Ordine minimo)",
            "sr_r1_c4": "Campione fisico reale in ~15 giorni lavorativi: 15€ (100% dedotto dall'ordine finale)",
            "sr_r2_c1": "250 unità",
            "sr_r2_c4": "Campione fisico deducibile · Consegna ordine in ~1 mese",
            "sr_r3_c1": "500 unità",
            "sr_r3_c4": "Campione deducibile e spedizione inclusa · Consegna in ~1 mese",
            "sr_r4_c1": "1.500 unità",
            "sr_r4_c4": "Tariffa diretta di fabbrica grandi volumi · Spedizione inclusa",
            "map_h3": "Club e Brand con Portachiavi CoolPadel",
            "map_p": "Seleziona un'area o clicca su qualsiasi indicatore per esplorare i nostri club ufficiali",
            "sr_clubs_h4": "Club, accademie e federazioni clienti ufficiali di CoolPadel Studios:"
        }
    }[active_lang]
    seo = seo_i18n

    html = f"""<!DOCTYPE html>
<html lang="{active_lang}" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{t['meta_title']}</title>
  <meta name="description" content="{t['meta_desc']}">
  <meta name="author" content="CoolPadel Studios">
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">
  <link rel="canonical" href="{page_url}">
  <link rel="icon" type="image/png" href="{asset_prefix}assets/images/favicon_transparente.png?v=transp3">
  <link rel="apple-touch-icon" sizes="180x180" href="{asset_prefix}assets/images/favicon_transparente.png?v=transp3">
  <link rel="manifest" href="{asset_prefix}site.webmanifest">
  <meta name="google-site-verification" content="google045b4db1401a0923">
  <meta name="theme-color" content="#0b1626">
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
  <meta name="apple-mobile-web-app-title" content="CoolPadel Studios">

  <!-- LLM & AI Search Engine Discovery (llmstxt.org) -->
  <link rel="alternate" type="text/markdown" href="https://coolpadelstudios.com/llms.txt" title="LLMs.txt">
  <link rel="alternate" type="text/markdown" href="https://coolpadelstudios.com/llms-full.txt" title="LLMs-Full.txt">

  <!-- Geo Tags for Local SEO & GEO (Madrid, Spain / Europe / Worldwide) -->
  <meta name="geo.region" content="ES-MD">
  <meta name="geo.placename" content="Madrid">
  <meta name="geo.position" content="40.4168;-3.7038">
  <meta name="ICBM" content="40.4168, -3.7038">

  <!-- Etiquetas Hreflang para SEO Internacional Multilingüe -->
  <link rel="alternate" hreflang="es" href="https://coolpadelstudios.com/">
  <link rel="alternate" hreflang="en" href="https://coolpadelstudios.com/en/">
  <link rel="alternate" hreflang="fr" href="https://coolpadelstudios.com/fr/">
  <link rel="alternate" hreflang="it" href="https://coolpadelstudios.com/it/">
  <link rel="alternate" hreflang="x-default" href="https://coolpadelstudios.com/">
  <meta name="language" content="{active_lang}">

  <!-- Open Graph / WhatsApp / Facebook / LinkedIn Previews -->
  <meta property="og:type" content="website">
  <meta property="og:locale" content="{og_locale}">
  <meta property="og:site_name" content="CoolPadel Studios">
  <meta property="og:url" content="{page_url}">
  <meta property="og:title" content="{t['meta_title']}">
  <meta property="og:description" content="{t['meta_desc']}">
  <meta property="og:image" content="https://coolpadelstudios.com/assets/images/slide-1.jpg">
  <meta property="og:image:alt" content="{seo_i18n['og_img_alt']}">

  <!-- Twitter / X Cards -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{t['meta_title']}">
  <meta name="twitter:description" content="{t['meta_desc']}">
  <meta name="twitter:image" content="https://coolpadelstudios.com/assets/images/slide-1.jpg">

  <!-- Datos Estructurados Schema.org JSON-LD (Google Rich Snippets & Generative AI / GEO) -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@graph": [
      {{
        "@type": "Organization",
        "@id": "https://coolpadelstudios.com/#organization",
        "name": "CoolPadel Studios",
        "alternateName": ["CoolPadel", "CoolPadel Madrid"],
        "url": "https://coolpadelstudios.com",
        "logo": {{
          "@type": "ImageObject",
          "url": "https://coolpadelstudios.com/assets/images/coolpadel-mascot-hd.png"
        }},
        "founder": {{
          "@type": "Person",
          "name": "Javier Villoria",
          "sameAs": "https://www.linkedin.com/in/javier-villoria-soleto-606737298/"
        }},
        "description": "{seo_i18n['org_desc']}",
        "sameAs": [
          "https://www.instagram.com/coolpadel_/",
          "https://www.linkedin.com/in/javier-villoria-soleto-606737298/",
          "https://www.wikidata.org/wiki/Q1229646",
          "https://www.wikidata.org/wiki/Q131557",
          "https://www.wikidata.org/wiki/Q1417088"
        ],
        "about": [
          {{ "@type": "Thing", "name": "Padel", "sameAs": "https://www.wikidata.org/wiki/Q1229646" }},
          {{ "@type": "Thing", "name": "Keychain", "sameAs": "https://www.wikidata.org/wiki/Q131557" }},
          {{ "@type": "Thing", "name": "Promotional Merchandise", "sameAs": "https://www.wikidata.org/wiki/Q1417088" }}
        ],
        "areaServed": [
          "ES", "IT", "FR", "PT", "DE", "GB", "US", "AE", "Worldwide"
        ],
        "knowsAbout": [
          "Llaveros de pádel",
          "Llaveros de padel personalizados",
          "Custom padel keychains",
          "Porte-clés padel personnalisés",
          "Portachiavi padel personalizzati",
          "Merchandising para clubes de pádel",
          "Welcome packs de pádel",
          "Cámaras pistas de pádel Save my Play",
          "Franquicias y cadenas de clubes de pádel",
          "Industria del padel"
        ],
        "contactPoint": {{
          "@type": "ContactPoint",
          "telephone": "+34-680-31-74-86",
          "contactType": "sales",
          "email": "javier@coolpadelstudios.com",
          "availableLanguage": ["Spanish", "English", "French", "Italian"]
        }}
      }},
      {{
        "@type": "WebSite",
        "@id": "https://coolpadelstudios.com/#website",
        "url": "https://coolpadelstudios.com",
        "name": "CoolPadel Studios",
        "alternateName": "CoolPadel",
        "publisher": {{ "@id": "https://coolpadelstudios.com/#organization" }},
        "inLanguage": "{active_lang}"
      }},
      {{
        "@type": "BreadcrumbList",
        "itemListElement": [
          {{
            "@type": "ListItem",
            "position": 1,
            "name": "{seo_i18n['bc_home']}",
            "item": "{page_url}"
          }},
          {{
            "@type": "ListItem",
            "position": 2,
            "name": "{seo_i18n['bc_llaveros']}",
            "item": "{page_url}#llaveros"
          }}
        ]
      }},
      {{
        "@type": "Product",
        "@id": "https://coolpadelstudios.com/#product-llaveros-padel",
        "inLanguage": "{active_lang}",
        "name": "{seo_i18n['prod_name']}",
        "alternateName": [
          "Llaveros de pádel",
          "Llaveros de padel personalizados",
          "Custom padel keychains",
          "Porte-clés padel personnalisés",
          "Portachiavi padel personalizzati",
          "Llaveros personalizados para clubs de pádel",
          "Merchandising para clubs de pádel",
          "Regalos torneos de pádel welcome pack"
        ],
        "description": "{seo_i18n['prod_desc']}",
        "category": "Sporting Goods > Racquet Sports > Padel > Accessories > Keychains",
        "keywords": "llaveros de padel, custom padel keychains, porte-clés padel, portachiavi padel, llaveros de pádel personalizados, merchandising clubes padel, welcome pack padel",
        "material": "{seo_i18n['prod_material']}",
        "image": [
          "https://coolpadelstudios.com/assets/images/llaveros%201.jpg",
          "https://coolpadelstudios.com/assets/images/llaveros%202.jpg",
          "https://coolpadelstudios.com/assets/images/slide-1.jpg"
        ],
        "brand": {{
          "@type": "Brand",
          "name": "CoolPadel"
        }},
        "sku": "CP-LLAVERO-PADEL-3D",
        "gtin13": "8437025698124",
        "mpn": "CP3D-2026",
        "offers": {{
          "@type": "AggregateOffer",
          "priceCurrency": "EUR",
          "lowPrice": "1.50",
          "highPrice": "3.00",
          "price": "1.50",
          "offerCount": "4",
          "availability": "https://schema.org/InStock",
          "itemCondition": "https://schema.org/NewCondition",
          "priceValidUntil": "2027-12-31",
          "seller": {{
            "@type": "Organization",
            "name": "CoolPadel"
          }},
          "hasMerchantReturnPolicy": {{
            "@type": "MerchantReturnPolicy",
            "applicableCountry": "ES",
            "returnPolicyCategory": "https://schema.org/MerchantReturnFiniteReturnWindow",
            "merchantReturnDays": 14,
            "returnMethod": "https://schema.org/ReturnByMail",
            "returnFees": "https://schema.org/FreeReturn"
          }},
          "shippingDetails": {{
            "@type": "OfferShippingDetails",
            "shippingRate": {{
              "@type": "MonetaryAmount",
              "value": "0.00",
              "currency": "EUR"
            }},
            "shippingDestination": {{
              "@type": "DefinedRegion",
              "addressCountry": ["ES", "FR", "IT", "PT", "DE", "BE", "GB", "US"]
            }},
            "deliveryTime": {{
              "@type": "ShippingDeliveryTime",
              "businessDays": {{
                "@type": "OpeningHoursSpecification",
                "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
              }},
              "cutoffTime": "14:00:00Z",
              "handlingTime": {{
                "@type": "QuantitativeValue",
                "minValue": 10,
                "maxValue": 15,
                "unitCode": "d"
              }},
              "transitTime": {{
                "@type": "QuantitativeValue",
                "minValue": 10,
                "maxValue": 15,
                "unitCode": "d"
              }}
            }}
          }}
        }}
      }},
      {{
        "@type": "HowTo",
        "inLanguage": "{active_lang}",
        "name": "{seo_i18n['howto_name']}",
        "description": "{seo_i18n['howto_desc']}",
        "step": [
          {{
            "@type": "HowToStep",
            "position": 1,
            "name": "{seo_i18n['step1_name']}",
            "text": "{seo_i18n['step1_text']}"
          }},
          {{
            "@type": "HowToStep",
            "position": 2,
            "name": "{seo_i18n['step2_name']}",
            "text": "{seo_i18n['step2_text']}"
          }},
          {{
            "@type": "HowToStep",
            "position": 3,
            "name": "{seo_i18n['step3_name']}",
            "text": "{seo_i18n['step3_text']}"
          }}
        ]
      }},
      {{
        "@type": "LocalBusiness",
        "@id": "https://coolpadelstudios.com/#localbusiness",
        "name": "CoolPadel",
        "image": "https://coolpadelstudios.com/assets/images/coolpadel-mascot-hd.png",
        "url": "https://coolpadelstudios.com",
        "telephone": "+34-680-31-74-86",
        "priceRange": "€€",
        "address": {{
          "@type": "PostalAddress",
          "streetAddress": "Chamartín",
          "postalCode": "28036",
          "addressLocality": "Madrid",
          "addressRegion": "Comunidad de Madrid",
          "addressCountry": "ES"
        }},
        "geo": {{
          "@type": "GeoCoordinates",
          "latitude": 40.4589,
          "longitude": -3.6761
        }},
        "sameAs": [
          "https://www.instagram.com/coolpadel_/",
          "https://www.linkedin.com/in/javier-villoria-soleto-606737298/"
        ],
        "openingHoursSpecification": {{
          "@type": "OpeningHoursSpecification",
          "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
          "opens": "00:00",
          "closes": "23:59"
        }}
      }},
      {{
        "@type": "FAQPage",
        "mainEntity": [
          {{
            "@type": "Question",
            "name": "{t_clean['faq_q1']}",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "{t_clean['faq_a1']}"
            }}
          }},
          {{
            "@type": "Question",
            "name": "{t_clean['faq_q2']}",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "{t_clean['faq_a2']}"
            }}
          }},
          {{
            "@type": "Question",
            "name": "{t_clean['faq_q3']}",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "{t_clean['faq_a3']}"
            }}
          }},
          {{
            "@type": "Question",
            "name": "{t_clean['faq_q4']}",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "{t_clean['faq_a4']}"
            }}
          }},
          {{
            "@type": "Question",
            "name": "{t_clean['faq_q5']}",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "{t_clean['faq_a5']}"
            }}
          }},
          {{
            "@type": "Question",
            "name": "{t_clean['faq_q6']}",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "{t_clean['faq_a6']}"
            }}
          }},
          {{
            "@type": "Question",
            "name": "{t_clean['faq_q7']}",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "{t_clean['faq_a7']}"
            }}
          }},
          {{
            "@type": "Question",
            "name": "{t_clean['faq_q8']}",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "{t_clean['faq_a8']}"
            }}
          }},
          {{
            "@type": "Question",
            "name": "{t_clean['faq_q9']}",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "{t_clean['faq_a9']}"
            }}
          }},
          {{
            "@type": "Question",
            "name": "{t_clean['faq_q10']}",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "{t_clean['faq_a10']}"
            }}
          }}
        ]
      }}
    ]
  }}
  </script>
  <link rel="alternate" type="application/rss+xml" title="CoolPadel Studios Feed" href="https://coolpadelstudios.com/rss.xml">
  <link rel="alternate" type="text/markdown" href="{asset_prefix}llms.txt" title="LLMs Info">
  <link rel="preload" as="image" href="{asset_prefix}assets/images/slide-1.jpg" fetchpriority="high">
  
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;600;700;800;900&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet" media="print" onload="this.media='all'">
  <noscript>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;600;700;800;900&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  </noscript>
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {{
      darkMode: 'class',
      theme: {{
        extend: {{
          fontFamily: {{
            outfit: ['Outfit', 'sans-serif'],
            jakarta: ['Plus Jakarta Sans', 'sans-serif'],
          }},
          colors: {{
            cool: {{
              navy: '#091322',
              dark: '#0e1d33',
              card: '#132845',
              blue: '#0284c7',
              cyan: '#76d3f6',
              orange: '#f2920b',
              amber: '#d97706'
            }}
          }},
          animation: {{
            'ticker-slow': 'tickerSlow 9s linear infinite',
            'ticker-trusted': 'tickerSlow 12s linear infinite',
          }},
          keyframes: {{
            tickerSlow: {{
              '0%': {{ transform: 'translateX(0%)' }},
              '100%': {{ transform: 'translateX(-50%)' }}
            }}
          }}
        }}
      }}
    }}
  </script>
  <script src="https://unpkg.com/lucide@0.468.0/dist/umd/lucide.min.js"></script>

  <!-- Leaflet CSS y JS para Mapa Interactivo de Clubes -->
  <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" integrity="sha256-p4NxAoJBhIIN+hmNHrzRCf9tD/miZyoHS5obTRR9BMY=" crossorigin="" />
  <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js" integrity="sha256-20nQCchB9co0qIjJZRGuk2/Z9VM+kNiyxNV1lvTlZBo=" crossorigin=""></script>

  <!-- Microsoft Clarity (Heatmaps y Grabaciones de Sesión) -->
  <script type="text/javascript">
    (function(c,l,a,r,i,t,y){{
      c[a]=c[a]||function(){{(c[a].q=c[a].q||[]).push(arguments)}};
      t=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i;
      y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);
    }})(window, document, "clarity", "script", "q7p8g52y9e");
  </script>
  <style>
    *, *::before, *::after {{
      box-sizing: border-box;
    }}
    html, body {{
      overflow-x: hidden;
      width: 100%;
      -webkit-text-size-adjust: 100%;
    }}
    body {{ font-family: 'Plus Jakarta Sans', sans-serif; }}
    h1, h2, h3, h4, .font-heading {{ font-family: 'Outfit', sans-serif; }}
    
    .ticker-wrap {{
      width: 100%;
      overflow: hidden;
      white-space: nowrap;
    }}
    .ticker-content {{
      display: inline-flex;
      white-space: nowrap;
    }}

    /* Coverflow 3D Styles */
    .coverflow-wrapper {{
      perspective: 1400px;
      overflow: hidden;
      width: 100%;
    }}
    .coverflow-slide {{
      position: absolute;
      transition: transform 0.65s cubic-bezier(0.25, 1, 0.5, 1), opacity 0.65s ease, filter 0.65s ease, box-shadow 0.65s ease;
      transform-style: preserve-3d;
      will-change: transform, opacity;
      backface-visibility: hidden;
      -webkit-backface-visibility: hidden;
      cursor: pointer;
    }}
    .coverflow-slide.active {{
      transform: translateX(0%) scale(1);
      z-index: 30;
      opacity: 1;
      filter: blur(0px);
      box-shadow: 0 20px 45px -12px rgba(0, 0, 0, 0.65);
      cursor: default;
    }}
    .coverflow-slide.prev {{
      transform: translateX(-56%) scale(0.88);
      z-index: 20;
      opacity: 0.65;
      filter: blur(1.5px);
      cursor: pointer;
      box-shadow: 0 16px 32px -8px rgba(0, 0, 0, 0.55);
    }}
    .coverflow-slide.next {{
      transform: translateX(56%) scale(0.88);
      z-index: 20;
      opacity: 0.65;
      filter: blur(1.5px);
      cursor: pointer;
      box-shadow: 0 16px 32px -8px rgba(0, 0, 0, 0.55);
    }}
    @media (min-width: 768px) {{
      .coverflow-slide.prev {{
        transform: translateX(-68%) scale(0.86);
      }}
      .coverflow-slide.next {{
        transform: translateX(68%) scale(0.86);
      }}
    }}
    @media (min-width: 1280px) {{
      .coverflow-slide.prev {{
        transform: translateX(-72%) scale(0.86);
      }}
      .coverflow-slide.next {{
        transform: translateX(72%) scale(0.86);
      }}
      .coverflow-slide.prev:hover {{
        transform: translateX(-69%) scale(0.88);
        opacity: 0.85;
      }}
      .coverflow-slide.next:hover {{
        transform: translateX(69%) scale(0.88);
        opacity: 0.85;
      }}
    }}
    .coverflow-slide.prev:hover, .coverflow-slide.next:hover {{
      opacity: 0.85;
    }}

    .glass-card-clean {{
      background: rgba(14, 29, 51, 0.75);
      backdrop-filter: blur(12px);
      border: 1px solid rgba(56, 189, 248, 0.18);
    }}

    /* Selector desplegable de idioma: solo 1 elemento naranja a la vez */
    .lang-opt-active {{
      background-color: #f2920b !important;
      color: #020617 !important;
      font-weight: 900 !important;
    }}
    #lang-dropdown-menu:hover .lang-opt-active:not(:hover),
    #lang-dropdown-menu-mob:hover .lang-opt-active:not(:hover) {{
      background-color: transparent !important;
      color: #334155 !important;
      font-weight: 700 !important;
    }}

    /* Slider de calculadora sin marcas ni selección accidental */
    #calc-slider-box, #slider-track, #slider-thumb, .tier-btn {{
      touch-action: none;
      -webkit-touch-callout: none;
      -webkit-user-select: none;
      -khtml-user-select: none;
      -moz-user-select: none;
      -ms-user-select: none;
      user-select: none;
      outline: none !important;
      -webkit-tap-highlight-color: transparent;
    }}

    /* Estilos Leaflet Map Google Relieve */
    #coolpadel-leaflet-map {{
      background: #e2e8f0;
      transition: background-color 0.3s ease;
    }}
    .country-map-label {{
      background: transparent !important;
      border: none !important;
      box-shadow: none !important;
      display: flex !important;
      align-items: center;
      justify-content: center;
      pointer-events: none !important;
    }}
    .country-map-label span {{
      font-family: 'Outfit', sans-serif;
      font-weight: 800;
      font-size: 11px;
      letter-spacing: 0.16em;
      text-transform: uppercase;
      color: #1e293b;
      text-shadow: 0 1px 3px rgba(255, 255, 255, 0.9), 0 0 8px rgba(255, 255, 255, 0.7);
      pointer-events: none;
      white-space: nowrap;
      user-select: none;
      transition: color 0.3s ease;
    }}
    .custom-pin-container {{
      position: relative;
      width: 28px;
      height: 28px;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
    }}
    .custom-pin-ping {{
      position: absolute;
      width: 100%;
      height: 100%;
      border-radius: 9999px;
      background: rgba(242, 146, 11, 0.45);
      animation: ping 2s cubic-bezier(0, 0, 0.2, 1) infinite;
    }}
    .custom-pin-dot {{
      position: relative;
      width: 18px;
      height: 18px;
      border-radius: 9999px;
      background: #091322;
      border: 2px solid #f2920b;
      box-shadow: 0 0 10px rgba(242, 146, 11, 0.8);
      display: flex;
      align-items: center;
      justify-content: center;
      transition: all 0.2s ease;
    }}
    .custom-pin-container:hover .custom-pin-dot {{
      transform: scale(1.35);
      background-color: #38bdf8;
      border-color: #ffffff;
      box-shadow: 0 0 16px rgba(56, 189, 248, 0.95);
    }}
    .leaflet-popup-content-wrapper {{
      background: #ffffff !important;
      color: #0f172a !important;
      border: 1px solid rgba(226, 232, 240, 0.9) !important;
      border-radius: 14px !important;
      box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.2) !important;
      padding: 0 !important;
      overflow: hidden !important;
    }}
    .leaflet-popup-content {{
      margin: 0 !important;
      line-height: 1.4 !important;
    }}
    .leaflet-popup-tip {{
      background: #ffffff !important;
    }}
  </style>
</head>
<body class="bg-[#0b1626] text-slate-100 min-h-screen relative selection:bg-cool-orange selection:text-white overflow-x-hidden w-full">

  <!-- 2. NAVBAR BLANCA RESPONSIVE: SELECTOR DESPLEGABLE DE IDIOMA + LOGOS + CONTACTAR -->
  <header class="sticky top-0 z-40 bg-white text-slate-900 border-b border-slate-200 shadow-sm w-full">
    <div class="w-full max-w-[1700px] mx-auto px-3 sm:px-6 lg:px-10 py-1.5 sm:py-0 h-auto sm:h-16 lg:h-18">
      
      <!-- DESKTOP NAVBAR (3 COLUMNAS: IZQUIERDA + CENTRO 100% + DERECHA) -->
      <div class="hidden sm:grid grid-cols-[1fr_auto_1fr] items-center h-full w-full gap-2 lg:gap-4">
        
        <!-- COLUMNA 1: OJOS + LLAVEROS, CÁMARAS PISTAS Y BLOG CENTRADOS ENTRE OJOS Y LOGO -->
        <div class="flex items-center justify-between min-w-0 h-full">
          <a href="{asset_prefix}#" class="group py-1 inline-flex items-center shrink-0">
            <img src="{asset_prefix}assets/images/eyes-thumb.png?v=fixed_eyes" alt="CoolPadel Eyes" width="24" height="24" style="height: 24px; max-height: 24px; width: auto;" class="object-contain group-hover:scale-110 transition duration-300">
          </a>
          <div class="flex-1 flex items-center justify-center min-w-0 gap-5 sm:gap-6 lg:gap-9 xl:gap-11 pl-2 sm:pl-4 lg:pl-6">
            <a href="{asset_prefix}#llaveros" class="font-heading font-black text-xs lg:text-[13px] tracking-wider uppercase text-slate-950 hover:text-[#f2920b] transition select-none whitespace-nowrap">
              Llaveros
            </a>
            <a href="{asset_prefix}camaras/" class="font-heading font-black text-xs lg:text-[13px] tracking-wider uppercase text-slate-950 hover:text-[#f2920b] transition select-none whitespace-nowrap">
              Cámaras pistas
            </a>
            <a href="{asset_prefix}blog/" class="font-heading font-black text-xs lg:text-[13px] tracking-wider uppercase text-slate-950 hover:text-[#f2920b] transition select-none whitespace-nowrap">
              Blog
            </a>
          </div>
        </div>

        <!-- COLUMNA 2: MASCOTA + COOLPADEL (MATEMÁTICAMENTE 100% CENTRADO EN PANTALLA) -->
        <div class="flex items-center justify-center shrink-0 px-2 lg:px-4">
          <a href="{asset_prefix}#" class="flex items-center justify-center gap-2 sm:gap-3 group py-1">
            <img src="{asset_prefix}assets/images/coolpadel-mascot-hd.png" alt="Mascota CoolPadel" width="46" height="46" style="height: 46px; max-height: 46px; width: auto;" class="object-contain group-hover:scale-105 transition">
            <img src="{asset_prefix}assets/images/coolpadel-typography-hd.png" alt="CoolPadel" width="130" height="26" style="height: 26px; max-height: 26px; width: auto;" class="object-contain">
          </a>
        </div>

        <!-- COLUMNA 3: CADENAS DE CLUBS CENTRADO ENTRE LOGO Y SELECTOR DE IDIOMA + CONTROLES A LA DERECHA -->
        <div class="flex items-center justify-between min-w-0 h-full">
          <div class="flex-1 flex items-center justify-center min-w-0 pr-4 lg:pr-8">
            <a href="{asset_prefix}franquicias-padel/" class="font-heading font-black text-xs lg:text-[13px] tracking-wider uppercase text-slate-950 hover:text-[#f2920b] transition select-none whitespace-nowrap">
              Cadenas de clubs
            </a>
          </div>

          <!-- BLOQUE A LA DERECHA DEL TODO: SELECTOR IDIOMA + CONTACTAR (SIN OJOS) -->
          <div class="flex items-center gap-2 sm:gap-3 shrink-0 ml-auto">
            <!-- SELECTOR DE IDIOMA EN DESPLEGABLE COMPACTO -->
            <div class="relative inline-block text-left" id="lang-dropdown-container">
              <button type="button" onclick="toggleLangDropdown(event)" id="lang-dropdown-btn" class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-full bg-slate-100 hover:bg-slate-200 border border-slate-200 text-xs font-black text-slate-900 shadow-xs transition cursor-pointer" aria-expanded="false" aria-haspopup="true">
                <span id="current-lang-code" class="uppercase font-black">{active_lang.upper()}</span>
                <i data-lucide="chevron-down" class="w-3.5 h-3.5 stroke-[2.5] text-slate-600 transition-transform duration-200" id="lang-dropdown-arrow"></i>
              </button>

              <!-- MENÚ DESPLEGABLE FLOTANTE -->
              <div id="lang-dropdown-menu" class="hidden absolute right-0 mt-2 w-24 bg-white rounded-2xl shadow-[0_12px_30px_rgba(0,0,0,0.15)] border border-slate-200 py-1.5 z-50 transition-all overflow-hidden">
                <button type="button" onclick="switchLanguage('es')" data-lang-opt="es" class="lang-opt {'lang-opt-active' if active_lang=='es' else 'text-slate-700 hover:bg-[#f2920b] hover:text-slate-950 font-bold'} w-full text-center px-4 py-2 text-xs transition duration-150 cursor-pointer">
                  ES
                </button>
                <button type="button" onclick="switchLanguage('en')" data-lang-opt="en" class="lang-opt {'lang-opt-active' if active_lang=='en' else 'text-slate-700 hover:bg-[#f2920b] hover:text-slate-950 font-bold'} w-full text-center px-4 py-2 text-xs transition duration-150 cursor-pointer">
                  EN
                </button>
                <button type="button" onclick="switchLanguage('fr')" data-lang-opt="fr" class="lang-opt {'lang-opt-active' if active_lang=='fr' else 'text-slate-700 hover:bg-[#f2920b] hover:text-slate-950 font-bold'} w-full text-center px-4 py-2 text-xs transition duration-150 cursor-pointer">
                  FR
                </button>
                <button type="button" onclick="switchLanguage('it')" data-lang-opt="it" class="lang-opt {'lang-opt-active' if active_lang=='it' else 'text-slate-700 hover:bg-[#f2920b] hover:text-slate-950 font-bold'} w-full text-center px-4 py-2 text-xs transition duration-150 cursor-pointer">
                  IT
                </button>
              </div>
            </div>

            <!-- BOTÓN CONTACTAR -->
            <a id="nav-contact-btn" href="https://wa.me/34680317486?text={wa_prefilled_encoded}" 
               target="_blank" rel="noopener noreferrer"
               class="group relative inline-flex items-center gap-1.5 px-3.5 sm:px-4 py-1.5 sm:py-2 rounded-full bg-[#f2920b] hover:bg-[#76d3f6] active:bg-[#76d3f6] text-slate-950 active:scale-95 font-heading font-black text-xs sm:text-xs lg:text-sm tracking-wider uppercase transition-all duration-300 shadow-[0_4px_12px_rgba(242,146,11,0.2)] hover:scale-105 shrink-0 overflow-hidden">
              <span data-i18n="nav_contact" class="font-black">{t['nav_contact']}</span>
              <div class="w-4 h-4 sm:w-5 sm:h-5 rounded-full bg-slate-950/10 group-hover:bg-slate-950 group-hover:text-white flex items-center justify-center transition-all duration-300 shrink-0">
                <i data-lucide="arrow-up-right" class="w-2.5 h-2.5 sm:w-3 sm:h-3 stroke-[3] group-hover:translate-x-0.5 group-hover:-translate-y-0.5 transition-transform duration-300"></i>
              </div>
            </a>
          </div>
        </div>

      </div>

      <!-- MÓVIL NAVBAR (2 FILAS RESPONSIVE PERFECTAMENTE ALINEADAS Y FLUIDAS) -->
      <div class="flex sm:hidden flex-col gap-1.5 py-1.5 w-full">
        <!-- FILA 1: LOGO CENTRADO (SIN OJOS A LA DERECHA) -->
        <div class="flex items-center justify-between w-full px-2">
          <a href="{asset_prefix}#" class="py-0.5 inline-flex items-center shrink-0" aria-label="CoolPadel Studios Home">
            <img src="{asset_prefix}assets/images/eyes-thumb.png?v=fixed_eyes" alt="" aria-hidden="true" width="18" height="18" style="height: 18px; max-height: 18px; width: auto;" class="object-contain">
          </a>
          <a href="{asset_prefix}#" class="flex items-center justify-center gap-1.5 py-0.5">
            <img src="{asset_prefix}assets/images/coolpadel-mascot-hd.png" alt="Mascota CoolPadel Studios" width="28" height="28" style="height: 28px; max-height: 28px; width: auto;" class="object-contain">
            <img src="{asset_prefix}assets/images/coolpadel-typography-hd.png" alt="CoolPadel Studios" width="90" height="18" style="height: 18px; max-height: 18px; width: auto;" class="object-contain">
          </a>
          <div class="w-[18px]"></div>
        </div>
        
        <!-- FILA 2: LLAVEROS + CÁMARAS PISTAS + BLOG + CADENAS DE CLUBS + IDIOMAS + CONTACTAR -->
        <div class="flex items-center justify-between w-full gap-1 pt-1 border-t border-slate-100 px-1 overflow-x-auto">
          <div class="flex items-center gap-3.5 sm:gap-4 shrink-0">
            <a href="{asset_prefix}#llaveros" class="font-heading font-black text-[10px] tracking-wider uppercase text-slate-950 hover:text-[#f2920b] transition whitespace-nowrap">
              Llaveros
            </a>
            <a href="{asset_prefix}camaras/" class="font-heading font-black text-[10px] tracking-wider uppercase text-slate-950 hover:text-[#f2920b] transition whitespace-nowrap">
              Cámaras pistas
            </a>
            <a href="{asset_prefix}blog/" class="font-heading font-black text-[10px] tracking-wider uppercase text-slate-950 hover:text-[#f2920b] transition whitespace-nowrap">
              Blog
            </a>
            <a href="{asset_prefix}franquicias-padel/" class="font-heading font-black text-[10px] tracking-wider uppercase text-slate-950 hover:text-[#f2920b] transition whitespace-nowrap">
              Cadenas de clubs
            </a>
          </div>

          <div class="flex items-center gap-1 shrink-0">
            <!-- DESPLEGABLE IDIOMA MÓVIL -->
            <div class="relative inline-block text-left" id="lang-dropdown-container-mob">
              <button type="button" onclick="toggleLangDropdownMob(event)" id="lang-dropdown-btn-mob" class="inline-flex items-center gap-1 px-2 py-0.5 rounded-full bg-slate-100 hover:bg-slate-200 border border-slate-200 text-[10px] font-black text-slate-900 shadow-xs transition cursor-pointer">
                <span id="current-lang-code-mob" class="uppercase font-black">{active_lang.upper()}</span>
                <i data-lucide="chevron-down" class="w-2.5 h-2.5 stroke-[2.5] text-slate-600" id="lang-dropdown-arrow-mob"></i>
              </button>
              <div id="lang-dropdown-menu-mob" class="hidden absolute right-0 mt-1 w-20 bg-white rounded-2xl shadow-xl border border-slate-200 py-1 z-50 transition-all overflow-hidden">
                <button type="button" onclick="switchLanguage('es')" data-lang-opt="es" class="lang-opt {'lang-opt-active' if active_lang=='es' else 'text-slate-700 hover:bg-[#f2920b] hover:text-slate-950 font-bold'} w-full text-center px-3 py-1.5 text-[11px] transition duration-150 cursor-pointer">
                  ES
                </button>
                <button type="button" onclick="switchLanguage('en')" data-lang-opt="en" class="lang-opt {'lang-opt-active' if active_lang=='en' else 'text-slate-700 hover:bg-[#f2920b] hover:text-slate-950 font-bold'} w-full text-center px-3 py-1.5 text-[11px] transition duration-150 cursor-pointer">
                  EN
                </button>
                <button type="button" onclick="switchLanguage('fr')" data-lang-opt="fr" class="lang-opt {'lang-opt-active' if active_lang=='fr' else 'text-slate-700 hover:bg-[#f2920b] hover:text-slate-950 font-bold'} w-full text-center px-3 py-1.5 text-[11px] transition duration-150 cursor-pointer">
                  FR
                </button>
                <button type="button" onclick="switchLanguage('it')" data-lang-opt="it" class="lang-opt {'lang-opt-active' if active_lang=='it' else 'text-slate-700 hover:bg-[#f2920b] hover:text-slate-950 font-bold'} w-full text-center px-3 py-1.5 text-[11px] transition duration-150 cursor-pointer">
                  IT
                </button>
              </div>
            </div>

            <a id="nav-contact-btn-mob" href="https://wa.me/34680317486?text={wa_prefilled_encoded}" 
               target="_blank" rel="noopener noreferrer"
               class="group relative inline-flex items-center justify-center gap-1 px-2.5 py-1 rounded-full bg-[#f2920b] active:bg-[#76d3f6] text-slate-950 active:scale-95 font-heading font-black text-[10px] uppercase tracking-wider transition-all duration-300 shadow-xs shrink-0">
              <span data-i18n="nav_contact" class="font-black">{t['nav_contact']}</span>
              <div class="w-3 h-3 rounded-full bg-slate-950/10 flex items-center justify-center">
                <i data-lucide="arrow-up-right" class="w-2 h-2 stroke-[3]"></i>
              </div>
            </a>
          </div>
        </div>
      </div>

    </div>
  </header>

  <!-- 3. HERO PRINCIPAL: FOTO GRANDE LLAVEROS PARA TU CLUB / COMUNIDAD -->
  <section class="relative bg-white select-none pt-2 sm:pt-4 pb-2 sm:pb-3">
    <div class="w-full max-w-6xl mx-auto px-3 sm:px-6">
      
      <!-- HERO CARD EN GRANDE -->
      <div id="coverflow-0" class="relative w-full h-[340px] sm:h-[420px] lg:h-[480px] xl:h-[520px] rounded-3xl sm:rounded-[2.2rem] overflow-hidden bg-neutral-900 shadow-[0_20px_50px_-12px_rgba(0,0,0,0.35)] border border-slate-200/80 group">
        <img src="{asset_prefix}assets/images/slide-1.jpg" alt="Llaveros de pádel personalizados para clubs y comunidades CoolPadel" width="1920" height="1080" class="w-full h-full object-cover group-hover:scale-[1.015] transition-transform duration-700 ease-out" fetchpriority="high" decoding="async">
        
        <!-- Degradado inferior para máxima legibilidad -->
        <div class="absolute inset-0 bg-gradient-to-t from-slate-950/90 via-slate-950/40 to-transparent pointer-events-none"></div>

        <!-- Contenido Hero (Bottom Left) -->
        <div class="absolute bottom-5 sm:bottom-9 left-5 sm:left-10 z-20 space-y-2.5 sm:space-y-3.5 max-w-[92%] sm:max-w-[85%] lg:max-w-[75%] pointer-events-auto">
          <h1 data-i18n="slide1_title" class="text-2xl sm:text-4xl lg:text-5xl font-black font-heading text-white uppercase tracking-tight leading-[1.12]">
            {t['slide1_title']}
          </h1>
          <div>
            <a href="#llaveros" class="group inline-flex items-center gap-2 sm:gap-2.5 px-4 sm:px-6 py-2 sm:py-3 rounded-full bg-[#f2920b] hover:bg-[#76d3f6] active:bg-[#76d3f6] text-slate-950 font-heading font-extrabold text-xs sm:text-sm tracking-wider uppercase shadow-[0_10px_25px_rgba(0,0,0,0.4)] hover:shadow-[0_14px_30px_rgba(118,211,246,0.5)] hover:scale-105 active:scale-95 transition-all duration-300 overflow-hidden">
              <span data-i18n="slide1_btn">{t['slide1_btn']}</span>
              <div class="w-5 h-5 sm:w-5.5 sm:h-5.5 rounded-full bg-slate-950/10 group-hover:bg-slate-950 group-hover:text-white flex items-center justify-center transition-all duration-300">
                <i data-lucide="arrow-right" class="w-3 h-3 sm:w-3.5 sm:h-3.5 stroke-[3] group-hover:translate-x-1 transition-transform duration-300"></i>
              </div>
            </a>
          </div>
        </div>
      </div>

      <!-- TEXTO EN ZONA DEBAJO DE LA FOTO (TRABAJAMOS CON CLUBS...) -->
      <div class="mt-3 sm:mt-5 mb-0 text-center px-4">
        <p data-i18n="trusted_text" class="text-[12px] sm:text-[15px] lg:text-[17px] font-heading font-extrabold uppercase tracking-widest text-slate-950 leading-snug">
          {t['trusted_text']}
        </p>
      </div>

    </div>
  </section>

  <!-- 4. CARROUSEL PASARELA CLUBS (ALTURA AJUSTADA PARA ESTAR VISIBLE DE INMEDIATO) -->
  <section class="py-2.5 sm:py-3.5 bg-white border-y border-slate-200 overflow-hidden shadow-xs">
    <div class="ticker-wrap py-0.5">
      <div class="ticker-content animate-ticker-trusted flex items-center gap-5 sm:gap-10 lg:gap-12">
        {ticker_html}
      </div>
    </div>
  </section>

  <!-- 5. SECCIÓN DETALLADA: LLAVEROS PARA CLUBS (FONDO CELESTE #3478a6) -->
  <section id="llaveros" itemscope itemtype="https://schema.org/Product" class="py-14 sm:py-20 bg-[#3478a6] relative border-b border-sky-700/40 text-white overflow-hidden">
    <!-- GEO & Generative AI Semantic Microdata Block (Invisible visually, accessible to Screen Readers and AI Crawlers) -->
    <div class="sr-only">
      <h2 itemprop="name">{seo['sr_h2']}</h2>
      <p itemprop="description">{seo['sr_p']}</p>
      <span itemprop="brand" itemscope itemtype="https://schema.org/Brand"><meta itemprop="name" content="CoolPadel Studios"></span>
      <meta itemprop="category" content="Sporting Goods &gt; Racquet Sports &gt; Padel &gt; Accessories &gt; Keychains">
      <meta itemprop="material" content="{seo['prod_material']}">
      <div itemprop="offers" itemscope itemtype="https://schema.org/AggregateOffer">
        <meta itemprop="priceCurrency" content="EUR">
        <meta itemprop="lowPrice" content="1.50">
        <meta itemprop="highPrice" content="3.00">
        <meta itemprop="price" content="1.50">
        <meta itemprop="offerCount" content="4">
        <meta itemprop="availability" content="https://schema.org/InStock">
      </div>
    </div>
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
      
      <!-- CABECERA DE SECCIÓN LLAVEROS -->
      <div class="max-w-3xl mx-auto text-center space-y-2 sm:space-y-3 mb-10 sm:mb-16">
        <h2 data-i18n="llaveros_title" class="text-2xl sm:text-5xl font-black font-heading text-white uppercase tracking-tight leading-tight">
          {t['llaveros_title']}
        </h2>
        <p data-i18n="llaveros_subtitle" class="text-white/90 text-sm sm:text-lg font-medium">
          {t['llaveros_subtitle']}
        </p>
      </div>

      <!-- DOS FOTOS: TENIS (IZQ) & PADEL (DCHA) -->
      <div class="grid md:grid-cols-2 gap-6 sm:gap-8 lg:gap-12 max-w-5xl mx-auto mb-12 sm:mb-16">
        
        <!-- CARD IZQUIERDA: TENIS -->
        <a href="/llaveros-tenis-personalizados/" class="bg-white border border-slate-200/90 rounded-3xl p-5 sm:p-7 shadow-[0_25px_50px_-12px_rgba(0,0,0,0.25)] hover:shadow-[0_35px_65px_-10px_rgba(0,0,0,0.35)] transition-all duration-300 group flex flex-col justify-between hover:-translate-y-1">
          <div class="aspect-[4/3] rounded-2xl overflow-hidden mb-4 sm:mb-5 bg-slate-100 shadow-[0_20px_40px_-10px_rgba(0,0,0,0.3)] border border-slate-200/90">
            <img src="{asset_prefix}assets/images/llaveros 2.jpg" alt="Llaveros de tenis y pádel personalizados con relieve 3D para clubs y torneos" width="736" height="1408" class="w-full h-full object-cover group-hover:scale-105 transition duration-500" loading="lazy" decoding="async">
          </div>
          <h3 data-i18n="card_tenis" class="font-heading font-black text-xl sm:text-2xl lg:text-3xl uppercase tracking-tight text-slate-950 text-center py-1">
            {t['card_tenis']}
          </h3>
        </a>

        <!-- CARD DERECHA: PADEL -->
        <a href="/llaveros-padel-personalizados/" class="bg-white border border-slate-200/90 rounded-3xl p-5 sm:p-7 shadow-[0_25px_50px_-12px_rgba(0,0,0,0.25)] hover:shadow-[0_35px_65px_-10px_rgba(0,0,0,0.35)] transition-all duration-300 group flex flex-col justify-between hover:-translate-y-1">
          <div class="aspect-[4/3] rounded-2xl overflow-hidden mb-4 sm:mb-5 bg-slate-100 shadow-[0_20px_40px_-10px_rgba(0,0,0,0.3)] border border-slate-200/90">
            <img src="{asset_prefix}assets/images/llaveros 1.jpg" alt="Llaveros de pádel de goma 3D personalizados con logo para clubes de pádel" width="768" height="1344" class="w-full h-full object-cover group-hover:scale-105 transition duration-500" loading="lazy" decoding="async">
          </div>
          <h3 data-i18n="card_padel" class="font-heading font-black text-xl sm:text-2xl lg:text-3xl uppercase tracking-tight text-[#f2920b] text-center py-1">
            {t['card_padel']}
          </h3>
        </a>

      </div>

      <!-- CALCULADORA DE PRESUPUESTO OFICIAL (RECUADRO BLANCO OFICIAL) -->
      <div class="max-w-3xl mx-auto bg-white rounded-3xl p-5 sm:p-10 border border-white/60 shadow-2xl text-slate-950">
        <div class="text-center mb-6 sm:mb-8">
          <h3 data-i18n="calc_title" class="text-xl sm:text-3xl font-black font-heading text-slate-950">
            {t['calc_title']}
          </h3>
        </div>

        <div class="space-y-6">
          
          <!-- Tabla estática oficial para crawlers de IA y accesibilidad (Sin impacto visual) -->
          <table class="sr-only">
            <caption>{seo['sr_caption']}</caption>
            <thead>
              <tr>
                <th scope="col">{seo['sr_th_tier']}</th>
                <th scope="col">{seo['sr_th_unit']}</th>
                <th scope="col">{seo['sr_th_total']}</th>
                <th scope="col">{seo['sr_th_cond']}</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>{seo['sr_r1_c1']}</td>
                <td>3,00 € / ud</td>
                <td>300 € (+IVA)</td>
                <td>{seo['sr_r1_c4']}</td>
              </tr>
              <tr>
                <td>{seo['sr_r2_c1']}</td>
                <td>2,50 € / ud</td>
                <td>625 € (+IVA)</td>
                <td>{seo['sr_r2_c4']}</td>
              </tr>
              <tr>
                <td>{seo['sr_r3_c1']}</td>
                <td>2,00 € / ud</td>
                <td>1.000 € (+IVA)</td>
                <td>{seo['sr_r3_c4']}</td>
              </tr>
              <tr>
                <td>{seo['sr_r4_c1']}</td>
                <td>1,50 € / ud</td>
                <td>2.250 € (+IVA)</td>
                <td>{seo['sr_r4_c4']}</td>
              </tr>
            </tbody>
          </table>
          
          <!-- Slider y Contador -->
          <div>
            <div class="flex justify-between items-end mb-3">
              <div>
                <span data-i18n="calc_label_qty" class="text-xs sm:text-sm font-bold text-slate-500 uppercase tracking-wider block">{t['calc_label_qty']}</span>
                <span id="calc-qty-badge" class="text-xl sm:text-3xl font-black font-heading text-slate-950">100 {t['calc_unit_name']}</span>
              </div>
              <div class="text-right">
                <span data-i18n="calc_label_price" class="text-xs sm:text-sm font-bold text-slate-500 uppercase tracking-wider block">{t['calc_label_price']}</span>
                <div class="flex items-baseline justify-end gap-1 sm:gap-1.5">
                  <span id="calc-price-badge" class="text-xl sm:text-3xl font-black font-heading text-[#76d3f6]">300 €</span>
                  <span id="calc-unit-badge" class="text-xs sm:text-sm font-bold text-slate-500">(3,00 €/{t['calc_unit_price']})</span>
                </div>
              </div>
            </div>

            <!-- Slider interactivo con Ojos exactamente centrados en cada punto -->
            <div class="relative py-4 select-none" id="calc-slider-box">
              
              <div class="mx-5 sm:mx-8">
                <!-- Barra / Carril limpio -->
                <div id="slider-track" class="relative w-full h-3 bg-slate-200 rounded-full cursor-pointer touch-none">
                  <!-- Progreso azul oficial #76d3f6 -->
                  <div id="slider-progress" class="absolute top-0 left-0 h-full bg-[#76d3f6] rounded-full transition-all duration-300" style="width: 0%;"></div>

                  <!-- Logo de los Ojos centrado exactamente sobre la barra -->
                  <div id="slider-thumb" 
                       class="absolute top-1/2 -translate-x-1/2 -translate-y-1/2 w-10 sm:w-11 h-5 sm:h-6 flex items-center justify-center cursor-grab active:cursor-grabbing hover:scale-115 active:scale-125 transition-all duration-300 z-30 pointer-events-none"
                       style="left: 0%;">
                    <img src="{asset_prefix}assets/images/eyes-thumb.png" alt="" aria-hidden="true" class="w-full h-full object-contain drop-shadow-[0_3px_5px_rgba(0,0,0,0.35)] select-none">
                  </div>
                </div>
                
                <!-- Marcas de escala rápida (sin salirse de los límites) -->
                <div class="relative w-full text-[11px] sm:text-sm font-extrabold text-slate-600 h-6 mt-4">
                  <button type="button" onclick="setTier(0)" class="tier-btn absolute left-0 translate-x-0 hover:text-[#f2920b] transition">100 uds</button>
                  <button type="button" onclick="setTier(1)" class="tier-btn absolute left-[33.333%] -translate-x-1/2 hover:text-[#f2920b] transition">250 uds</button>
                  <button type="button" onclick="setTier(2)" class="tier-btn absolute left-[66.666%] -translate-x-1/2 hover:text-[#f2920b] transition">500 uds</button>
                  <button type="button" onclick="setTier(3)" class="tier-btn absolute right-0 translate-x-0 hover:text-[#f2920b] transition">1.500 uds</button>
                </div>
              </div>

            </div>
          </div>

          <!-- Botón de WhatsApp Contactar Premium -->
          <div class="pt-2">
            <a id="calc-wa-btn" href="https://wa.me/34680317486?text={wa_prefilled_encoded}" target="_blank" rel="noopener noreferrer" class="group relative w-full py-4 sm:py-4.5 rounded-2xl font-heading font-black text-base sm:text-lg uppercase tracking-wider bg-[#f2920b] hover:bg-[#76d3f6] active:bg-[#76d3f6] text-slate-950 shadow-[0_10px_25px_rgba(242,146,11,0.35)] hover:shadow-[0_16px_35px_rgba(118,211,246,0.45)] hover:scale-[1.01] active:scale-[0.98] flex items-center justify-center gap-3 transition-all duration-300 overflow-hidden">
              <span data-i18n="btn_calc_wa" class="font-black">{t['btn_calc_wa']}</span>
              <div class="w-7 h-7 sm:w-8 sm:h-8 rounded-full bg-slate-950/10 group-hover:bg-slate-950 group-hover:text-white flex items-center justify-center transition-all duration-300">
                <i data-lucide="arrow-up-right" class="w-3.5 h-3.5 sm:w-4 sm:h-4 stroke-[3] group-hover:translate-x-0.5 group-hover:-translate-y-0.5 transition-transform duration-300"></i>
              </div>
            </a>
          </div>
        </div>
      </div>

    </div>
  </section>



  <!-- 6. MAPA INTERACTIVO: CLUBS Y MARCAS CON LLAVEROS COOLPADEL -->
  <section id="mapa-clubs" class="py-12 sm:py-16 bg-slate-50 relative border-b border-slate-200">
    <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <!-- CABECERA DEL MAPA -->
      <div class="text-center max-w-2xl mx-auto mb-6 sm:mb-8 space-y-2">
        <h3 class="text-xl sm:text-3xl font-black font-heading text-slate-950 uppercase tracking-tight">
          {seo['map_h3']}
        </h3>
        <p class="text-xs sm:text-sm text-slate-600 font-medium">
          {seo['map_p']}
        </p>
      </div>

      <!-- CONTENEDOR DEL MAPA Y DETALLES -->
      <div class="bg-white rounded-3xl p-4 sm:p-7 border border-slate-200/90 shadow-lg">
        
        <!-- Listado semántico HTML accesible de clubes para indexación de clientes y GEO (sr-only) -->
        <div class="sr-only">
          <h4>{seo['sr_clubs_h4']}</h4>
          <ul>
            {club_list_html}
          </ul>
        </div>
        
        <!-- FILTROS POR REGIÓN -->
        <div class="flex items-center justify-center gap-1.5 sm:gap-2.5 flex-wrap pb-4 sm:pb-6 border-b border-slate-100" id="map-filter-bar">
          <button type="button" onclick="focusMapRegion('all')" class="map-filter-btn px-3 sm:px-4 py-1.5 rounded-full text-xs font-bold transition cursor-pointer bg-slate-950 text-white shadow-xs" data-region="all">
            Todos (27)
          </button>
          <button type="button" onclick="focusMapRegion('es')" class="map-filter-btn px-3 sm:px-4 py-1.5 rounded-full text-xs font-bold transition cursor-pointer bg-slate-100 text-slate-700 hover:bg-slate-200" data-region="es">
            España (15)
          </button>
          <button type="button" onclick="focusMapRegion('it')" class="map-filter-btn px-3 sm:px-4 py-1.5 rounded-full text-xs font-bold transition cursor-pointer bg-slate-100 text-slate-700 hover:bg-slate-200" data-region="it">
            Italia (5)
          </button>
          <button type="button" onclick="focusMapRegion('fr')" class="map-filter-btn px-3 sm:px-4 py-1.5 rounded-full text-xs font-bold transition cursor-pointer bg-slate-100 text-slate-700 hover:bg-slate-200" data-region="fr">
            Francia (3)
          </button>
          <button type="button" onclick="focusMapRegion('be')" class="map-filter-btn px-3 sm:px-4 py-1.5 rounded-full text-xs font-bold transition cursor-pointer bg-slate-100 text-slate-700 hover:bg-slate-200" data-region="be">
            Bélgica (2)
          </button>
          <button type="button" onclick="focusMapRegion('other')" class="map-filter-btn px-3 sm:px-4 py-1.5 rounded-full text-xs font-bold transition cursor-pointer bg-slate-100 text-slate-700 hover:bg-slate-200" data-region="other">
            Austria & Dinamarca (2)
          </button>
        </div>

        <!-- GRID INTERACTIVO: MAPA LEAFLET A LA IZQUIERDA + PANEL DETALLE A LA DERECHA -->
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 items-stretch pt-4">
          
          <!-- MAPA LEAFLET INTERACTIVO PANNABLE/ZOOMABLE -->
          <div class="lg:col-span-8 relative bg-slate-100 rounded-2xl border border-slate-200/90 overflow-hidden shadow-inner min-h-[380px] sm:min-h-[500px]">
            <div id="coolpadel-leaflet-map" class="w-full h-full min-h-[380px] sm:min-h-[500px] z-10" style="min-height: 500px; width: 100%; background: #e2e8f0;"></div>
            

            <!-- HINT FLOTANTE INFERIOR -->
            <div class="absolute bottom-3 left-3 z-[400] bg-white/95 backdrop-blur-sm px-3.5 py-1.5 rounded-full border border-slate-200/90 shadow-sm pointer-events-none hidden sm:flex items-center gap-2 text-[11px] font-bold text-slate-700">
              <i data-lucide="hand" class="w-3.5 h-3.5 text-[#f2920b]"></i>
              <span>Arrastra para desplazarte o haz zoom en el mapa</span>
            </div>
          </div>

          <!-- PANEL LATERAL: INFORMACIÓN Y LOGO REAL DEL CLUB SELECCIONADO (FORMATO: SOLO LOGO Y DEBAJO NOMBRE Y UBICACIÓN CENTRADO) -->
          <div class="lg:col-span-4 flex flex-col justify-center items-center bg-white rounded-2xl p-5 sm:p-6 border border-slate-200 min-h-[380px] shadow-sm text-center" id="club-info-card">
            
            <div class="w-full flex-1 flex flex-col items-center justify-center p-6 bg-slate-50/70 rounded-2xl border border-slate-200/80 shadow-xs">
              <!-- CONTENEDOR LOGO REAL DEL CLUB -->
              <div class="h-40 sm:h-48 w-full flex items-center justify-center">
                <img id="club-logo-img" src="{asset_prefix}assets/images/Clubs/client-02.png" alt="Logo Club de Tenis Cambados" width="240" height="176" class="max-h-36 sm:max-h-44 max-w-[240px] w-auto h-auto object-contain transition-all duration-300">
              </div>

              <!-- NOMBRE Y UBICACIÓN CENTRADOS -->
              <div class="mt-5 space-y-1 text-center">
                <h4 id="club-name" class="font-heading font-black text-xl sm:text-2xl text-slate-950">
                  Club de Tenis Cambados
                </h4>
                <p id="club-location" class="text-xs sm:text-sm font-bold text-slate-500">
                  Cambados, Galicia (España)
                </p>
              </div>
            </div>

          </div>

        </div>

      </div>

    </div>
  </section>

  <!-- 7.5. SECCIÓN PREGUNTAS FRECUENTES (FAQ ACORDEÓN INTERACTIVO + GEO/SEO) -->
  <section id="faq" class="py-16 sm:py-24 bg-slate-50 relative border-b border-slate-200">
    <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <!-- CABECERA FAQ -->
      <div class="text-center mb-10 sm:mb-14">
        <h2 data-i18n="faq_section_title" class="text-2xl sm:text-4xl font-black font-heading text-slate-950 uppercase tracking-tight">
          {t['faq_section_title']}
        </h2>
      </div>

      <!-- ACORDEÓN DE PREGUNTAS (10 PREGUNTAS OFICIALES) -->
      <div class="space-y-3 sm:space-y-4" id="faq-accordion">
        
        <!-- PREGUNTA 1: PROCESO -->
        <div class="faq-item bg-white border border-slate-200/90 rounded-2xl overflow-hidden shadow-xs transition-all duration-200">
          <button type="button" onclick="toggleFaq(this)" class="w-full px-5 sm:px-6 py-4 sm:py-5 flex items-center justify-between text-left font-sans font-bold text-base sm:text-lg text-slate-900 hover:text-[#f2920b] transition gap-4 cursor-pointer">
            <span data-i18n="faq_q1">{t['faq_q1']}</span>
            <i data-lucide="chevron-down" class="faq-icon w-5 h-5 stroke-[2.5] text-slate-400 shrink-0 transition-transform duration-300"></i>
          </button>
          <div class="faq-answer hidden px-5 sm:px-6 pb-5 pt-3 text-slate-700 text-sm sm:text-base font-normal leading-relaxed sm:leading-loose border-t border-slate-100">
            <p data-i18n="faq_a1">{t['faq_a1']}</p>
          </div>
        </div>

        <!-- PREGUNTA 2: PEDIDO MÍNIMO Y PLAZOS -->
        <div class="faq-item bg-white border border-slate-200/90 rounded-2xl overflow-hidden shadow-xs transition-all duration-200">
          <button type="button" onclick="toggleFaq(this)" class="w-full px-5 sm:px-6 py-4 sm:py-5 flex items-center justify-between text-left font-sans font-bold text-base sm:text-lg text-slate-900 hover:text-[#f2920b] transition gap-4 cursor-pointer">
            <span data-i18n="faq_q2">{t['faq_q2']}</span>
            <i data-lucide="chevron-down" class="faq-icon w-5 h-5 stroke-[2.5] text-slate-400 shrink-0 transition-transform duration-300"></i>
          </button>
          <div class="faq-answer hidden px-5 sm:px-6 pb-5 pt-3 text-slate-700 text-sm sm:text-base font-normal leading-relaxed sm:leading-loose border-t border-slate-100">
            <p data-i18n="faq_a2">{t['faq_a2']}</p>
          </div>
        </div>

        <!-- PREGUNTA 3: PRECIOS, IVA Y FACTURACIÓN -->
        <div class="faq-item bg-white border border-slate-200/90 rounded-2xl overflow-hidden shadow-xs transition-all duration-200">
          <button type="button" onclick="toggleFaq(this)" class="w-full px-5 sm:px-6 py-4 sm:py-5 flex items-center justify-between text-left font-sans font-bold text-base sm:text-lg text-slate-900 hover:text-[#f2920b] transition gap-4 cursor-pointer">
            <span data-i18n="faq_q3">{t['faq_q3']}</span>
            <i data-lucide="chevron-down" class="faq-icon w-5 h-5 stroke-[2.5] text-slate-400 shrink-0 transition-transform duration-300"></i>
          </button>
          <div class="faq-answer hidden px-5 sm:px-6 pb-5 pt-3 text-slate-700 text-sm sm:text-base font-normal leading-relaxed sm:leading-loose border-t border-slate-100">
            <p data-i18n="faq_a3">{t['faq_a3']}</p>
          </div>
        </div>

        <!-- PREGUNTA 4: MUESTRA DESCONTABLE -->
        <div class="faq-item bg-white border border-slate-200/90 rounded-2xl overflow-hidden shadow-xs transition-all duration-200">
          <button type="button" onclick="toggleFaq(this)" class="w-full px-5 sm:px-6 py-4 sm:py-5 flex items-center justify-between text-left font-sans font-bold text-base sm:text-lg text-slate-900 hover:text-[#f2920b] transition gap-4 cursor-pointer">
            <span data-i18n="faq_q4">{t['faq_q4']}</span>
            <i data-lucide="chevron-down" class="faq-icon w-5 h-5 stroke-[2.5] text-slate-400 shrink-0 transition-transform duration-300"></i>
          </button>
          <div class="faq-answer hidden px-5 sm:px-6 pb-5 pt-3 text-slate-700 text-sm sm:text-base font-normal leading-relaxed sm:leading-loose border-t border-slate-100">
            <p data-i18n="faq_a4">{t['faq_a4']}</p>
          </div>
        </div>

        <!-- PREGUNTA 5: TAMAÑO LLAVERO (70MM) -->
        <div class="faq-item bg-white border border-slate-200/90 rounded-2xl overflow-hidden shadow-xs transition-all duration-200">
          <button type="button" onclick="toggleFaq(this)" class="w-full px-5 sm:px-6 py-4 sm:py-5 flex items-center justify-between text-left font-sans font-bold text-base sm:text-lg text-slate-900 hover:text-[#f2920b] transition gap-4 cursor-pointer">
            <span data-i18n="faq_q5">{t['faq_q5']}</span>
            <i data-lucide="chevron-down" class="faq-icon w-5 h-5 stroke-[2.5] text-slate-400 shrink-0 transition-transform duration-300"></i>
          </button>
          <div class="faq-answer hidden px-5 sm:px-6 pb-5 pt-3 text-slate-700 text-sm sm:text-base font-normal leading-relaxed sm:leading-loose border-t border-slate-100">
            <p data-i18n="faq_a5">{t['faq_a5']}</p>
          </div>
        </div>

        <!-- PREGUNTA 6: VENDER EN TIENDA / PRO-SHOP -->
        <div class="faq-item bg-white border border-slate-200/90 rounded-2xl overflow-hidden shadow-xs transition-all duration-200">
          <button type="button" onclick="toggleFaq(this)" class="w-full px-5 sm:px-6 py-4 sm:py-5 flex items-center justify-between text-left font-sans font-bold text-base sm:text-lg text-slate-900 hover:text-[#f2920b] transition gap-4 cursor-pointer">
            <span data-i18n="faq_q6">{t['faq_q6']}</span>
            <i data-lucide="chevron-down" class="faq-icon w-5 h-5 stroke-[2.5] text-slate-400 shrink-0 transition-transform duration-300"></i>
          </button>
          <div class="faq-answer hidden px-5 sm:px-6 pb-5 pt-3 text-slate-700 text-sm sm:text-base font-normal leading-relaxed sm:leading-loose border-t border-slate-100">
            <p data-i18n="faq_a6">{t['faq_a6']}</p>
          </div>
        </div>

        <!-- PREGUNTA 7: USOS Y OCASIONES (WELCOME PACKS, CENAS, PATROCINADORES) -->
        <div class="faq-item bg-white border border-slate-200/90 rounded-2xl overflow-hidden shadow-xs transition-all duration-200">
          <button type="button" onclick="toggleFaq(this)" class="w-full px-5 sm:px-6 py-4 sm:py-5 flex items-center justify-between text-left font-sans font-bold text-base sm:text-lg text-slate-900 hover:text-[#f2920b] transition gap-4 cursor-pointer">
            <span data-i18n="faq_q7">{t['faq_q7']}</span>
            <i data-lucide="chevron-down" class="faq-icon w-5 h-5 stroke-[2.5] text-slate-400 shrink-0 transition-transform duration-300"></i>
          </button>
          <div class="faq-answer hidden px-5 sm:px-6 pb-5 pt-3 text-slate-700 text-sm sm:text-base font-normal leading-relaxed sm:leading-loose border-t border-slate-100">
            <p data-i18n="faq_a7">{t['faq_a7']}</p>
          </div>
        </div>

        <!-- PREGUNTA 8: CLUBES Y MAPA OFICIAL -->
        <div class="faq-item bg-white border border-slate-200/90 rounded-2xl overflow-hidden shadow-xs transition-all duration-200">
          <button type="button" onclick="toggleFaq(this)" class="w-full px-5 sm:px-6 py-4 sm:py-5 flex items-center justify-between text-left font-sans font-bold text-base sm:text-lg text-slate-900 hover:text-[#f2920b] transition gap-4 cursor-pointer">
            <span data-i18n="faq_q8">{t['faq_q8']}</span>
            <i data-lucide="chevron-down" class="faq-icon w-5 h-5 stroke-[2.5] text-slate-400 shrink-0 transition-transform duration-300"></i>
          </button>
          <div class="faq-answer hidden px-5 sm:px-6 pb-5 pt-3 text-slate-700 text-sm sm:text-base font-normal leading-relaxed sm:leading-loose border-t border-slate-100">
            <p data-i18n="faq_a8">{t['faq_a8']}</p>
          </div>
        </div>

        <!-- PREGUNTA 9: PAÍSES Y ENVÍOS -->
        <div class="faq-item bg-white border border-slate-200/90 rounded-2xl overflow-hidden shadow-xs transition-all duration-200">
          <button type="button" onclick="toggleFaq(this)" class="w-full px-5 sm:px-6 py-4 sm:py-5 flex items-center justify-between text-left font-sans font-bold text-base sm:text-lg text-slate-900 hover:text-[#f2920b] transition gap-4 cursor-pointer">
            <span data-i18n="faq_q9">{t['faq_q9']}</span>
            <i data-lucide="chevron-down" class="faq-icon w-5 h-5 stroke-[2.5] text-slate-400 shrink-0 transition-transform duration-300"></i>
          </button>
          <div class="faq-answer hidden px-5 sm:px-6 pb-5 pt-3 text-slate-700 text-sm sm:text-base font-normal leading-relaxed sm:leading-loose border-t border-slate-100">
            <p data-i18n="faq_a9">{t['faq_a9']}</p>
          </div>
        </div>

        <!-- PREGUNTA 10: SAVE MY PLAY -->
        <div class="faq-item bg-white border border-slate-200/90 rounded-2xl overflow-hidden shadow-xs transition-all duration-200">
          <button type="button" onclick="toggleFaq(this)" class="w-full px-5 sm:px-6 py-4 sm:py-5 flex items-center justify-between text-left font-sans font-bold text-base sm:text-lg text-slate-900 hover:text-[#f2920b] transition gap-4 cursor-pointer">
            <span data-i18n="faq_q10">{t['faq_q10']}</span>
            <i data-lucide="chevron-down" class="faq-icon w-5 h-5 stroke-[2.5] text-slate-400 shrink-0 transition-transform duration-300"></i>
          </button>
          <div class="faq-answer hidden px-5 sm:px-6 pb-5 pt-3 text-slate-700 text-sm sm:text-base font-normal leading-relaxed sm:leading-loose border-t border-slate-100">
            <p data-i18n="faq_a10">{t['faq_a10']}</p>
          </div>
        </div>

      </div>

    </div>
  </section>

  <!-- 8. SECCIÓN CONTACTO (FONDO CELESTE #3478a6 & 20% MÁS ANCHA) -->
  <section id="contacto" class="pt-7 sm:pt-10 lg:pt-12 pb-12 sm:pb-16 lg:pb-20 bg-[#3478a6] relative border-t border-sky-700/40 text-white overflow-hidden">
    <div class="max-w-[1850px] mx-auto px-6 sm:px-14 lg:px-20 relative z-10">
      
      <!-- TÍTULO DE LA SECCIÓN ARRIBA DEL TODO -->
      <div class="max-w-4xl mx-auto text-center mb-6 sm:mb-8 lg:mb-10">
        <h2 data-i18n="contact_title" class="text-2xl sm:text-4xl lg:text-5xl font-black font-heading text-white uppercase tracking-tight leading-tight">
          {t['contact_title']}
        </h2>
      </div>

      <!-- BLOQUE DE CONTACTO CENTRADO Y 20% MÁS ESPACIOSO -->
      <div class="flex flex-col md:flex-row items-center justify-center gap-10 md:gap-20 lg:gap-24 w-full">
        
        <!-- COOLPADEL (MASCOTA + TIPOGRAFÍA) -->
        <div class="flex items-center justify-center gap-3.5">
          <img src="{asset_prefix}assets/images/coolpadel-mascot-hd.png" alt="CoolPadel Mascota" width="80" height="80" class="h-14 sm:h-18 lg:h-20 w-auto object-contain drop-shadow-md" loading="lazy">
          <img src="{asset_prefix}assets/images/coolpadel-typography-hd.png" alt="CoolPadel" width="200" height="40" class="h-7 sm:h-9 lg:h-10 w-auto object-contain drop-shadow-md" loading="lazy">
        </div>

        <!-- CORREO Y WHATSAPP OFICIAL DE JAVIER -->
        <div class="flex flex-col items-center justify-center text-center gap-4 sm:gap-6">
          <a href="mailto:javier@coolpadelstudios.com" 
             class="group inline-flex items-center gap-3 text-white hover:text-[#f2920b] font-sans font-bold text-sm sm:text-xl lg:text-2xl tracking-normal transition-all duration-300 hover:scale-105 active:scale-95 whitespace-nowrap">
            <i data-lucide="mail" class="w-5 h-5 sm:w-6 sm:h-6 text-[#f2920b] group-hover:text-white transition-colors shrink-0"></i>
            <span class="underline decoration-white/40 group-hover:decoration-[#f2920b] underline-offset-6">javier@coolpadelstudios.com</span>
          </a>

          <!-- BOTÓN WHATSAPP OFICIAL EN CONTACTO -->
          <a id="contact-wa-btn" href="https://wa.me/34680317486?text={wa_prefilled_encoded}" 
             target="_blank" rel="noopener noreferrer"
             class="group inline-flex items-center gap-3 px-8 sm:px-9 py-3 sm:py-3.5 rounded-full bg-[#25D366] hover:bg-[#20ba59] active:bg-[#20ba59] text-white font-sans font-black text-xs sm:text-sm tracking-wider uppercase shadow-md hover:shadow-xl hover:scale-105 active:scale-95 transition-all duration-300">
            <svg class="w-4 h-4 sm:w-5 sm:h-5 fill-current" viewBox="0 0 24 24">
              <path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981zm11.387-5.464c-.074-.124-.272-.198-.57-.347-.297-.149-1.758-.868-2.031-.967-.272-.099-.47-.149-.669.149-.198.297-.768.967-.941 1.165-.173.198-.347.223-.644.074-.297-.149-1.255-.462-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.297-.347.446-.521.151-.172.2-.296.3-.495.099-.198.05-.372-.025-.521-.075-.148-.669-1.611-.916-2.206-.242-.579-.487-.501-.669-.51l-.57-.01c-.198 0-.52.074-.792.372s-1.04 1.016-1.04 2.479 1.065 2.876 1.213 3.074c.149.198 2.095 3.2 5.076 4.487.709.306 1.263.489 1.694.626.712.226 1.36.194 1.872.118.571-.085 1.758-.719 2.006-1.413.248-.695.248-1.29.173-1.414z"/>
            </svg>
            <span data-i18n="contact_wa_btn">{t['contact_wa_btn']}</span>
          </a>
        </div>

      </div>

      <!-- ENLACES INTERNOS SEO Y COPYRIGHT (CON TRIGGER DE MODO ADMIN POR TRIPLE CLIC) -->
      <div class="mt-10 pt-6 border-t border-white/10 text-center select-none space-y-3 text-xs text-white/60">
        <nav aria-label="Soluciones y Directorio CoolPadel" class="flex flex-wrap items-center justify-center gap-x-3 gap-y-1.5">
          <a href="/llaveros-padel-personalizados/" class="hover:text-white underline decoration-white/30 underline-offset-2 transition">Llaveros de Pádel</a>
          <span class="opacity-30">·</span>
          <a href="/llaveros-tenis-personalizados/" class="hover:text-white underline decoration-white/30 underline-offset-2 transition">Llaveros de Tenis</a>
          <span class="opacity-30">·</span>
          <a href="/welcome-packs-torneos-padel/" class="hover:text-white underline decoration-white/30 underline-offset-2 transition">Welcome Packs Torneos</a>
          <span class="opacity-30">·</span>
          <a href="/llaveros-personalizados-clubs-padel/" class="hover:text-white underline decoration-white/30 underline-offset-2 transition">Merchandising Clubs</a>
          <span class="opacity-30">·</span>
          <a href="/camaras/" class="hover:text-white underline decoration-white/30 underline-offset-2 transition">Cámaras Save my Play</a>
          <span class="opacity-30">·</span>
          <a href="/camaras-grabacion-pistas-padel/" class="hover:text-white underline decoration-white/30 underline-offset-2 transition">Grabación Pistas Pádel</a>
          <span class="opacity-30">·</span>
          <a href="/franquicias-padel/" class="hover:text-white underline decoration-white/30 underline-offset-2 transition">Directorio Franquicias Pádel</a>
          <span class="opacity-30">·</span>
          <a href="/blog/" class="hover:text-white underline decoration-white/30 underline-offset-2 transition">Blog &amp; Informes</a>
        </nav>
        <div class="flex flex-col sm:flex-row items-center justify-center gap-2 text-white/50">
          <span id="admin-toggle-trigger" class="hover:text-white/80 transition cursor-pointer" title="Modo Administrador">
            © 2026 CoolPadel Studios · All rights reserved
          </span>
          <span class="hidden sm:inline opacity-30">·</span>
          <a href="/politica-de-devoluciones.html" class="hover:text-white/80 underline decoration-white/30 underline-offset-2 transition" title="Política de Devoluciones y Garantía">Política de Devoluciones</a>
          <span class="hidden sm:inline opacity-30">·</span>
          <a href="https://www.instagram.com/coolpadel_/" target="_blank" rel="noopener noreferrer" class="opacity-50 hover:opacity-90 text-[11px] transition text-white/80" title="Instagram CoolPadel">@coolpadel_</a>
        </div>
      </div>

    </div>
  </section>

  <!-- BOTÓN FLOTANTE OFICIAL DE WHATSAPP -->
  <a id="floating-wa-btn" href="https://wa.me/34680317486?text={wa_prefilled_encoded}" 
     target="_blank" rel="noopener noreferrer" 
     class="fixed bottom-5 right-5 sm:bottom-6 sm:right-6 z-50 p-3.5 sm:p-4 rounded-full bg-[#25D366] text-white shadow-[0_10px_30px_rgba(37,211,102,0.45)] hover:bg-[#20ba59] hover:scale-110 active:scale-95 transition flex items-center justify-center group"
     title="Hablar por WhatsApp con Javier">
    <svg class="w-6 h-6 sm:w-8 sm:h-8 fill-current" viewBox="0 0 24 24">
      <path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981zm11.387-5.464c-.074-.124-.272-.198-.57-.347-.297-.149-1.758-.868-2.031-.967-.272-.099-.47-.149-.669.149-.198.297-.768.967-.941 1.165-.173.198-.347.223-.644.074-.297-.149-1.255-.462-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.297-.347.446-.521.151-.172.2-.296.3-.495.099-.198.05-.372-.025-.521-.075-.148-.669-1.611-.916-2.206-.242-.579-.487-.501-.669-.51l-.57-.01c-.198 0-.52.074-.792.372s-1.04 1.016-1.04 2.479 1.065 2.876 1.213 3.074c.149.198 2.095 3.2 5.076 4.487.709.306 1.263.489 1.694.626.712.226 1.36.194 1.872.118.571-.085 1.758-.719 2.006-1.413.248-.695.248-1.29.173-1.414z"/>
    </svg>
    <span data-i18n="wa_floating_tooltip" class="max-w-0 overflow-hidden whitespace-nowrap group-hover:max-w-xs transition-all duration-300 ease-in-out text-xs font-black px-0 group-hover:px-2">
      {t['wa_floating_tooltip']}
    </span>
  </a>



  <!-- SCRIPTS & SISTEMA DE INTERNACIONALIZACIÓN (I18N) -->
  <script>
    lucide.createIcons();

    // DICCIONARIO REACTIVO MULTI-IDIOMA
    const I18N_DATA = {translations_json};
    let currentLang = '{active_lang}';
    const langFlags = {{ 'es': '🇪🇸', 'en': '🇬🇧', 'fr': '🇫🇷', 'it': '🇮🇹' }};

    function toggleLangDropdown(e) {{
      e.stopPropagation();
      const menu = document.getElementById('lang-dropdown-menu');
      const arrow = document.getElementById('lang-dropdown-arrow');
      if (!menu) return;
      const isHidden = menu.classList.contains('hidden');
      document.querySelectorAll('#lang-dropdown-menu, #lang-dropdown-menu-mob').forEach(m => m.classList.add('hidden'));
      if (isHidden) {{
        menu.classList.remove('hidden');
        if (arrow) arrow.style.transform = 'rotate(180deg)';
      }} else {{
        if (arrow) arrow.style.transform = 'rotate(0deg)';
      }}
    }}

    function toggleLangDropdownMob(e) {{
      e.stopPropagation();
      const menu = document.getElementById('lang-dropdown-menu-mob');
      const arrow = document.getElementById('lang-dropdown-arrow-mob');
      if (!menu) return;
      const isHidden = menu.classList.contains('hidden');
      document.querySelectorAll('#lang-dropdown-menu, #lang-dropdown-menu-mob').forEach(m => m.classList.add('hidden'));
      if (isHidden) {{
        menu.classList.remove('hidden');
        if (arrow) arrow.style.transform = 'rotate(180deg)';
      }} else {{
        if (arrow) arrow.style.transform = 'rotate(0deg)';
      }}
    }}

    document.addEventListener('click', () => {{
      const menu = document.getElementById('lang-dropdown-menu');
      const arrow = document.getElementById('lang-dropdown-arrow');
      if (menu) menu.classList.add('hidden');
      if (arrow) arrow.style.transform = 'rotate(0deg)';
      const menuMob = document.getElementById('lang-dropdown-menu-mob');
      const arrowMob = document.getElementById('lang-dropdown-arrow-mob');
      if (menuMob) menuMob.classList.add('hidden');
      if (arrowMob) arrowMob.style.transform = 'rotate(0deg)';
    }});

    function switchLanguage(lang) {{
      if (!I18N_DATA[lang]) return;
      currentLang = lang;
      
      try {{
        localStorage.setItem('coolpadel_lang', lang);
      }} catch(e) {{}}

      const dict = I18N_DATA[lang];

      // 1. Actualizar textos simples con data-i18n
      document.querySelectorAll('[data-i18n]').forEach(el => {{
        const key = el.getAttribute('data-i18n');
        if (dict[key]) {{
          el.innerHTML = dict[key];
        }}
      }});

      // 2. Actualizar placeholders
      document.querySelectorAll('[data-i18n-placeholder]').forEach(el => {{
        const key = el.getAttribute('data-i18n-placeholder');
        if (dict[key]) {{
          el.setAttribute('placeholder', dict[key]);
        }}
      }});

      // 3. Actualizar botones de WhatsApp
      const waMsg = encodeURIComponent(dict.wa_prefilled_msg);
      const waUrl = `https://wa.me/34680317486?text=${{waMsg}}`;
      
      const navWaBtn = document.getElementById('nav-contact-btn');
      if (navWaBtn) navWaBtn.href = waUrl;

      const navWaBtnMob = document.getElementById('nav-contact-btn-mob');
      if (navWaBtnMob) navWaBtnMob.href = waUrl;
      
      const smpWaBtn = document.getElementById('smp-contact-btn');
      if (smpWaBtn) smpWaBtn.href = waUrl;

      const contactWaBtn = document.getElementById('contact-wa-btn');
      if (contactWaBtn) contactWaBtn.href = waUrl;

      const floatWaBtn = document.getElementById('floating-wa-btn');
      if (floatWaBtn) floatWaBtn.href = waUrl;

      // 4. Actualizar labels y estilos del desplegable de idioma
      const codeEl = document.getElementById('current-lang-code');
      if (codeEl) codeEl.textContent = lang.toUpperCase();

      const codeElMob = document.getElementById('current-lang-code-mob');
      if (codeElMob) codeElMob.textContent = lang.toUpperCase();

      // Resaltar idioma activo con fondo naranja (#f2920b) y texto negro (solo 1 a la vez)
      document.querySelectorAll('[data-lang-opt]').forEach(btn => {{
        const optLang = btn.getAttribute('data-lang-opt');
        if (optLang === lang) {{
          btn.classList.add('lang-opt-active');
          btn.classList.remove('text-slate-700');
        }} else {{
          btn.classList.remove('lang-opt-active');
          btn.classList.add('text-slate-700');
        }}
      }});

      // Cerrar dropdowns tras seleccionar
      const menu = document.getElementById('lang-dropdown-menu');
      if (menu) menu.classList.add('hidden');
      const menuMob = document.getElementById('lang-dropdown-menu-mob');
      if (menuMob) menuMob.classList.add('hidden');

      // 5. Actualizar calculadora
      updateCalculator(currentTierIdx, false);

      // Re-renderizar iconos de Lucide
      lucide.createIcons();
    }}

    // HERO ÚNICO (Sin rotación de diapositivas)
    const heroCard = document.getElementById('coverflow-0');

    // Calculadora presupuesto con tarifario oficial e i18n
    const tiers = [
      {{ qty: '100', price: '300', unit: '3,00', pct: 0 }},
      {{ qty: '250', price: '625', unit: '2,50', pct: 33.333 }},
      {{ qty: '500', price: '1.000', unit: '2,00', pct: 66.666 }},
      {{ qty: '1500', price: '2.250', unit: '1,50', pct: 100 }}
    ];

    let currentTierIdx = 0;
    const qtyBadge = document.getElementById('calc-qty-badge');
    const priceBadge = document.getElementById('calc-price-badge');
    const unitBadge = document.getElementById('calc-unit-badge');
    const waBtn = document.getElementById('calc-wa-btn');
    const sliderThumb = document.getElementById('slider-thumb');
    const sliderProgress = document.getElementById('slider-progress');
    const sliderTrack = document.getElementById('slider-track');

    function updateCalculator(idx, isLiveDrag = false) {{
      currentTierIdx = idx;
      const tier = tiers[idx];
      const dict = I18N_DATA[currentLang] || I18N_DATA['es'];
      
      qtyBadge.textContent = `${{tier.qty}} ${{dict.calc_unit_name}}`;
      priceBadge.textContent = `${{tier.price}}€`;
      unitBadge.textContent = `(${{tier.unit}}€/${{dict.calc_unit_price}})`;
      
      if (sliderThumb && sliderProgress) {{
        if (isLiveDrag) {{
          sliderThumb.style.transition = 'none';
          sliderProgress.style.transition = 'none';
        }} else {{
          sliderThumb.style.transition = 'left 0.25s cubic-bezier(0.25, 1, 0.5, 1)';
          sliderProgress.style.transition = 'width 0.25s cubic-bezier(0.25, 1, 0.5, 1)';
        }}
        sliderThumb.style.left = `${{tier.pct}}%`;
        sliderProgress.style.width = `${{tier.pct}}%`;
      }}
      
      const customMsg = encodeURIComponent(`${{dict.wa_prefilled_msg}}, me interesa solicitar presupuesto de ${{tier.qty}} llaveros para mi club.`);
      waBtn.href = `https://wa.me/34680317486?text=${{customMsg}}`;
    }}

    window.setTier = function(idx) {{
      updateCalculator(idx, false);
    }};

    // Control táctil y ratón del Slider optimizado (arrastre instantáneo sin marcas ni retardo)
    let isDragging = false;
    const sliderBox = document.getElementById('calc-slider-box');

    function handleSliderInteraction(clientX, isLive = false) {{
      if (!sliderTrack) return;
      const rect = sliderTrack.getBoundingClientRect();
      const x = Math.max(0, Math.min(clientX - rect.left, rect.width));
      const ratio = x / rect.width;
      
      let closestIdx = 0;
      let minDiff = 999;
      tiers.forEach((t, i) => {{
        const diff = Math.abs((t.pct / 100) - ratio);
        if (diff < minDiff) {{
          minDiff = diff;
          closestIdx = i;
        }}
      }});
      updateCalculator(closestIdx, isLive);
    }}

    if (sliderBox) {{
      // Eventos táctiles
      sliderBox.addEventListener('touchstart', (e) => {{
        isDragging = true;
        if (e.touches && e.touches.length > 0) {{
          handleSliderInteraction(e.touches[0].clientX, true);
        }}
      }}, {{ passive: true }});

      sliderBox.addEventListener('touchmove', (e) => {{
        if (!isDragging) return;
        if (e.touches && e.touches.length > 0) {{
          handleSliderInteraction(e.touches[0].clientX, true);
          if (e.cancelable) e.preventDefault();
        }}
      }}, {{ passive: false }});

      sliderBox.addEventListener('touchend', () => {{
        if (isDragging) {{
          isDragging = false;
          updateCalculator(currentTierIdx, false);
        }}
      }}, {{ passive: true }});

      sliderBox.addEventListener('touchcancel', () => {{
        isDragging = false;
        updateCalculator(currentTierIdx, false);
      }}, {{ passive: true }});

      // Eventos de ratón / puntero
      sliderBox.addEventListener('pointerdown', (e) => {{
        isDragging = true;
        handleSliderInteraction(e.clientX, true);
        window.addEventListener('pointermove', onPointerMove);
        window.addEventListener('pointerup', onPointerUp);
      }});

      function onPointerMove(e) {{
        if (isDragging) handleSliderInteraction(e.clientX, true);
      }}

      function onPointerUp() {{
        if (isDragging) {{
          isDragging = false;
          updateCalculator(currentTierIdx, false);
        }}
        window.removeEventListener('pointermove', onPointerMove);
        window.removeEventListener('pointerup', onPointerUp);
      }}
    }}

    // TOGGLE ACORDEÓN FAQ CON TRACKING DE INTERÉS
    window.toggleFaq = function(btn) {{
      const answer = btn.nextElementSibling;
      const icon = btn.querySelector('.faq-icon');
      const isHidden = answer.classList.contains('hidden');
      
      document.querySelectorAll('.faq-answer').forEach(el => el.classList.add('hidden'));
      document.querySelectorAll('.faq-icon').forEach(el => el.classList.remove('rotate-180'));

      if (isHidden) {{
        answer.classList.remove('hidden');
        if (icon) icon.classList.add('rotate-180');
        
        // Registrar qué pregunta específica abrió el usuario
        hasOpenedFaq = true;
        const preguntaTexto = (btn.querySelector('span')?.textContent || btn.textContent || '').trim();
        trackEvent('faq_abierto', {{
          faq_pregunta: preguntaTexto,
          evento_desc: 'Abrió FAQ: ' + preguntaTexto.substring(0, 45)
        }});
      }}
    }};

    // ─────────────────────────────────────────────────────────────────
    // MAPA INTERACTIVO LEAFLET: CLUBS Y MARCAS REALES CON LOGOS
    // ─────────────────────────────────────────────────────────────────
    const ASSET_PREFIX = '{asset_prefix}';

    const MAP_CLUBS_DATA = [
      // ESPAÑA (15)
      {{
        id: 'cambados',
        name: 'Club de Tenis Cambados',
        region: 'es',
        location: 'Cambados, Galicia (España)',
        lat: 42.5147,
        lng: -8.8144,
        logo: ASSET_PREFIX + 'assets/images/Clubs/client-02.png'
      }},
      {{
        id: 'padel_zaleak',
        name: 'Pinondo Padel Zaleak',
        region: 'es',
        location: 'Durango, Bizkaia (España)',
        lat: 43.1697,
        lng: -2.6322,
        logo: ASSET_PREFIX + 'assets/images/Clubs/client-03.png'
      }},
      {{
        id: 'el_soto',
        name: 'Tenis Club El Soto',
        region: 'es',
        location: 'Zaragoza, Aragón (España)',
        lat: 41.6488,
        lng: -0.8891,
        logo: ASSET_PREFIX + 'assets/images/Clubs/client-04.png'
      }},
      {{
        id: 'higueruela',
        name: 'Club Deportivo Pádel Higueruela',
        region: 'es',
        location: 'Higueruela, Albacete (España)',
        lat: 38.9611,
        lng: -1.4422,
        logo: ASSET_PREFIX + 'assets/images/Clubs/client-07.png'
      }},
      {{
        id: 'vitasports',
        name: 'Vitasports Escuela de Tenis y Pádel',
        region: 'es',
        location: 'Cazalegas, Toledo (España)',
        lat: 40.0075,
        lng: -4.6744,
        logo: ASSET_PREFIX + 'assets/images/Clubs/client-08.png'
      }},
      {{
        id: 'ortigueira',
        name: 'Club de Pádel Ortigueira',
        region: 'es',
        location: 'Ortigueira, A Coruña (España)',
        lat: 43.6842,
        lng: -7.8544,
        logo: ASSET_PREFIX + 'assets/images/Clubs/client-09.png'
      }},
      {{
        id: 'reus_monterols',
        name: 'Club Tennis Reus Monterols',
        region: 'es',
        location: 'Reus, Tarragona (España)',
        lat: 41.1561,
        lng: 1.1069,
        logo: ASSET_PREFIX + 'assets/images/Clubs/client-11.png'
      }},
      {{
        id: 'vilamalla',
        name: 'Club Pádel Vilamalla',
        region: 'es',
        location: 'Vilamalla, Girona (España)',
        lat: 42.2158,
        lng: 2.9714,
        logo: ASSET_PREFIX + 'assets/images/Clubs/client-12.png'
      }},
      {{
        id: 'cabrera_anoia',
        name: "Padel Club Cabrera d'Anoia",
        region: 'es',
        location: "Cabrera d'Anoia, Barcelona (España)",
        lat: 41.4800,
        lng: 1.7058,
        logo: ASSET_PREFIX + 'assets/images/Clubs/client-13.png'
      }},
      {{
        id: 'padel_alba',
        name: 'Padel Alba',
        region: 'es',
        location: 'Alicante (España)',
        lat: 38.3452,
        lng: -0.4810,
        logo: ASSET_PREFIX + 'assets/images/Clubs/client-19.png'
      }},
      {{
        id: 'padeleiros_vigo',
        name: 'Padeleiros Vigo',
        region: 'es',
        location: 'Vigo, Pontevedra (España)',
        lat: 42.2406,
        lng: -8.7207,
        logo: ASSET_PREFIX + 'assets/images/Clubs/client-20.png'
      }},
      {{
        id: 'atm_malaga',
        name: 'A.T.M. Amigos del Tenis de Málaga',
        region: 'es',
        location: 'Málaga, Andalucía (España)',
        lat: 36.7213,
        lng: -4.4214,
        logo: ASSET_PREFIX + 'assets/images/Clubs/client-21.png'
      }},
      {{
        id: 'padel_addict',
        name: 'Padel Addict',
        region: 'es',
        location: 'Málaga / Madrid (España)',
        lat: 36.5101,
        lng: -4.8824,
        logo: ASSET_PREFIX + 'assets/images/Clubs/client-25.png'
      }},
      {{
        id: 'backspin_academy',
        name: 'Backspin Academy',
        region: 'es',
        location: 'Madrid (España)',
        lat: 40.4168,
        lng: -3.7038,
        logo: ASSET_PREFIX + 'assets/images/Clubs/client-26.png'
      }},
      {{
        id: 'espacio_herreria',
        name: 'Espacio Herrería',
        region: 'es',
        location: 'San Lorenzo de El Escorial, Madrid (España)',
        lat: 40.5908,
        lng: -4.1481,
        logo: ASSET_PREFIX + 'assets/images/Clubs/client-27.png'
      }},

      // ITALIA (5)
      {{
        id: 'fiorfiore',
        name: 'Fiorfiore Padel',
        region: 'it',
        location: 'Alba, Cuneo (Italia)',
        lat: 44.7009,
        lng: 8.0356,
        logo: ASSET_PREFIX + 'assets/images/Clubs/client-05.png'
      }},
      {{
        id: 'canzo',
        name: 'Tennis Life Canzo',
        region: 'it',
        location: 'Canzo, Como (Italia)',
        lat: 45.8509,
        lng: 9.2789,
        logo: ASSET_PREFIX + 'assets/images/Clubs/client-06.png'
      }},
      {{
        id: 'sant_agostino',
        name: "Tennis Club Sant'Agostino",
        region: 'it',
        location: "Sant'Agostino, Ferrara (Italia)",
        lat: 44.7925,
        lng: 11.3878,
        logo: ASSET_PREFIX + 'assets/images/Clubs/client-10.png'
      }},
      {{
        id: 'tennis_arca',
        name: 'Tennis Archa',
        region: 'it',
        location: 'Bérgamo, Lombardía (Italia)',
        lat: 45.6983,
        lng: 9.6773,
        logo: ASSET_PREFIX + 'assets/images/Clubs/client-tennis-arca.png'
      }},
      {{
        id: 'green_park',
        name: 'Club Green Park',
        region: 'it',
        location: 'Rivoli, Turín (Italia)',
        lat: 45.0703,
        lng: 7.5181,
        logo: ASSET_PREFIX + 'assets/images/Clubs/client-15.png'
      }},

      // FRANCIA (3)
      {{
        id: 'evreux',
        name: 'ALM Évreux Tennis Padel',
        region: 'fr',
        location: 'Évreux, Normandía (Francia)',
        lat: 49.0241,
        lng: 1.1508,
        logo: ASSET_PREFIX + 'assets/images/Clubs/client-14.png'
      }},
      {{
        id: 'le_garden',
        name: 'Le Garden Rennes',
        region: 'fr',
        location: 'Rennes, Bretaña (Francia)',
        lat: 48.1173,
        lng: -1.6778,
        logo: ASSET_PREFIX + 'assets/images/Clubs/client-17.png'
      }},
      {{
        id: 'usp_tennis_17',
        name: 'USP Tennis 17',
        region: 'fr',
        location: 'París, Île-de-France (Francia)',
        lat: 48.8837,
        lng: 2.3082,
        logo: ASSET_PREFIX + 'assets/images/Clubs/client-23.png'
      }},

      // BÉLGICA (2)
      {{
        id: 'royal_excelsior',
        name: 'Royal Excelsior Tennis Club',
        region: 'be',
        location: 'Lambermont, Liège (Bélgica)',
        lat: 50.5964,
        lng: 5.8344,
        logo: ASSET_PREFIX + 'assets/images/Clubs/client-16.png'
      }},
      {{
        id: 'padel_kiosk',
        name: 'Padel Kiosk',
        region: 'be',
        location: 'Amberes (Bélgica)',
        lat: 51.2194,
        lng: 4.4025,
        logo: ASSET_PREFIX + 'assets/images/Clubs/client-24.png'
      }},

      // AUSTRIA & DINAMARCA (2)
      {{
        id: 'austrian_padel',
        name: 'Austrian Padel Union',
        region: 'other',
        location: 'Viena (Austria)',
        lat: 48.2082,
        lng: 16.3738,
        logo: ASSET_PREFIX + 'assets/images/Clubs/client-18.png'
      }},
      {{
        id: 'cbs_padel',
        name: 'CBS Padel',
        region: 'other',
        location: 'Copenhague (Dinamarca)',
        lat: 55.6791,
        lng: 12.5348,
        logo: ASSET_PREFIX + 'assets/images/Clubs/client-22.png'
      }}
    ];

    let leafletMapInstance = null;
    let mapMarkersList = [];
    const GOOGLE_MAPS_API_KEY = 'AIzaSyDGYdWwepJ-wTOCIp9Y5gSXEteD50Ev24c';

    function initCoolPadelMap() {{
      const mapContainer = document.getElementById('coolpadel-leaflet-map');
      if (!mapContainer || typeof L === 'undefined') return;

      try {{
        leafletMapInstance = L.map('coolpadel-leaflet-map', {{
          center: [46.5, 3.5],
          zoom: 4,
          minZoom: 3,
          maxZoom: 18,
          scrollWheelZoom: false
        }});

        leafletMapInstance.on('focus', () => leafletMapInstance.scrollWheelZoom.enable());
        leafletMapInstance.on('click', () => leafletMapInstance.scrollWheelZoom.enable());

        // Capa Google Relieve (Terrain) oficial de alta definición
        L.tileLayer('https://mt{{s}}.google.com/vt/lyrs=p&x={{x}}&y={{y}}&z={{z}}&key=' + GOOGLE_MAPS_API_KEY, {{
          subdomains: ['0', '1', '2', '3'],
          maxZoom: 20,
          attribution: '&copy; Google Maps'
        }}).addTo(leafletMapInstance);

        const createPinIcon = () => L.divIcon({{
          className: 'custom-pin',
          html: `
            <div class="custom-pin-container">
              <span class="custom-pin-ping"></span>
              <div class="custom-pin-dot">
                <div style="width: 6px; height: 6px; border-radius: 9999px; background: #f2920b;"></div>
              </div>
            </div>
          `,
          iconSize: [28, 28],
          iconAnchor: [14, 14],
          popupAnchor: [0, -14]
        }});

        MAP_CLUBS_DATA.forEach(club => {{
          const marker = L.marker([club.lat, club.lng], {{
            icon: createPinIcon(),
            title: club.name
          }}).addTo(leafletMapInstance);

          const popupContent = `
            <div style="padding: 14px 16px; text-align: center; min-width: 170px; max-width: 220px; background: #ffffff;">
              <div style="height: 52px; display: flex; align-items: center; justify-content: center; margin-bottom: 8px;">
                <img src="${{club.logo}}" alt="${{club.name}}" style="max-height: 48px; max-width: 140px; width: auto; height: auto; object-fit: contain; margin: 0 auto; display: block;" />
              </div>
              <h4 style="font-family: 'Outfit', sans-serif; font-size: 14px; font-weight: 800; color: #0f172a; margin: 0 0 3px 0; line-height: 1.2;">
                ${{club.name}}
              </h4>
              <p style="font-size: 11px; color: #64748b; font-weight: 600; margin: 0;">
                ${{club.location}}
              </p>
            </div>
          `;

          marker.bindPopup(popupContent);

          marker.on('click', () => {{
            selectClubById(club.id);
          }});

          mapMarkersList.push({{ id: club.id, region: club.region, marker: marker, club: club }});
        }});

        selectClubById('cambados');

        setTimeout(() => {{
          if (leafletMapInstance) leafletMapInstance.invalidateSize();
        }}, 300);
      }} catch(err) {{
        console.warn('Leaflet init error:', err);
      }}
    }}

    window.selectClubById = function(clubId) {{
      const found = mapMarkersList.find(m => m.id === clubId);
      if (!found) return;
      const data = found.club;

      const logoEl = document.getElementById('club-logo-img');
      if (logoEl) {{
        logoEl.src = data.logo;
        logoEl.alt = 'Logo ' + data.name;
      }}

      const nameEl = document.getElementById('club-name');
      if (nameEl) nameEl.textContent = data.name;

      const locEl = document.getElementById('club-location');
      if (locEl) locEl.textContent = data.location;

      const card = document.getElementById('club-info-card');
      if (card) {{
        card.classList.add('ring-2', 'ring-[#f2920b]', 'transition-all');
        setTimeout(() => card.classList.remove('ring-2', 'ring-[#f2920b]'), 700);
      }}

      trackEvent('mapa_club_click', {{
        club_seleccionado: data.name,
        evento_desc: 'Clic en club del mapa: ' + data.name
      }});
    }};

    window.focusMapRegion = function(region) {{
      document.querySelectorAll('.map-filter-btn').forEach(btn => {{
        if (btn.getAttribute('data-region') === region) {{
          btn.className = 'map-filter-btn px-3 sm:px-4 py-1.5 rounded-full text-xs font-bold transition cursor-pointer bg-slate-950 text-white shadow-xs';
        }} else {{
          btn.className = 'map-filter-btn px-3 sm:px-4 py-1.5 rounded-full text-xs font-bold transition cursor-pointer bg-slate-100 text-slate-700 hover:bg-slate-200';
        }}
      }});

      if (!leafletMapInstance) initCoolPadelMap();
      if (!leafletMapInstance) return;

      if (region === 'all') {{
        leafletMapInstance.setView([47.5, 4.0], 4, {{ animate: true }});
        selectClubById('cambados');
      }} else if (region === 'es') {{
        leafletMapInstance.setView([40.2, -3.7], 6, {{ animate: true }});
        selectClubById('cambados');
      }} else if (region === 'it') {{
        leafletMapInstance.setView([44.5, 9.5], 6, {{ animate: true }});
        selectClubById('fiorfiore');
      }} else if (region === 'fr') {{
        leafletMapInstance.setView([48.6, 1.5], 6, {{ animate: true }});
        selectClubById('evreux');
      }} else if (region === 'be') {{
        leafletMapInstance.setView([50.8, 5.0], 8, {{ animate: true }});
        selectClubById('royal_excelsior');
      }} else if (region === 'other') {{
        leafletMapInstance.setView([51.0, 14.0], 5, {{ animate: true }});
        selectClubById('austrian_padel');
      }}
    }};

    function setupDeferredMap() {{
      const mapSec = document.getElementById('mapa-clubs');
      if (mapSec && 'IntersectionObserver' in window) {{
        const mapObs = new IntersectionObserver((entries, obs) => {{
          if (entries.some(e => e.isIntersecting)) {{
            obs.disconnect();
            initCoolPadelMap();
          }}
        }}, {{ rootMargin: '600px 0px' }});
        mapObs.observe(mapSec);
      }} else {{
        initCoolPadelMap();
      }}
    }}

    if (document.readyState === 'loading') {{
      document.addEventListener('DOMContentLoaded', setupDeferredMap);
    }} else {{
      setupDeferredMap();
    }}


    // URL del Webhook de Google Apps Script (Recepción de Leads y Analítica de Eventos)
    const GOOGLE_SHEETS_WEBHOOK_URL = 'https://script.google.com/macros/s/AKfycbxnF9JmVrikeAW7PdLc02r_1kkuSJVz1Ncl71ZeVGT37H0ji5DQ3DVw60122pcuYnxCgA/exec';

    // ─────────────────────────────────────────────────────────────────
    // MOTOR DE ANALÍTICA COMERCIAL AVANZADA
    // ─────────────────────────────────────────────────────────────────
    
    // 1. Detección y Gestión de Modo Administrador (Javier)
    const urlParams = new URLSearchParams(window.location.search);
    if (urlParams.get('admin') === '1' || urlParams.get('admin') === 'true' || urlParams.get('admin') === 'javier' || urlParams.get('yo') === '1') {{
      try {{ localStorage.setItem('cp_is_admin', 'true'); }} catch(e) {{}}
    }} else if (urlParams.get('admin') === '0' || urlParams.get('admin') === 'false' || urlParams.get('reset_admin') === '1') {{
      try {{ localStorage.removeItem('cp_is_admin'); }} catch(e) {{}}
    }}
    
    let isAdmin = false;
    try {{
      isAdmin = localStorage.getItem('cp_is_admin') === 'true';
    }} catch(e) {{}}

    // Trigger de activación Admin por triple clic en copyright
    try {{
      let adminClickCount = 0;
      let adminClickTimer = null;
      const adminTrigger = document.getElementById('admin-toggle-trigger');
      if (adminTrigger) {{
        adminTrigger.addEventListener('click', () => {{
          adminClickCount++;
          clearTimeout(adminClickTimer);
          adminClickTimer = setTimeout(() => {{ adminClickCount = 0; }}, 700);
          if (adminClickCount >= 3) {{
            adminClickCount = 0;
            const current = localStorage.getItem('cp_is_admin') === 'true';
            if (current) {{
              localStorage.removeItem('cp_is_admin');
              alert('👤 Modo Admin DESACTIVADO. Ahora se registrará como visitante normal.');
            }} else {{
              localStorage.setItem('cp_is_admin', 'true');
              alert('👤 Modo Admin ACTIVADO. Tus visitas aparecerán marcadas como "Javier (Admin)".');
            }}
            window.location.reload();
          }}
        }});
      }}
    }} catch(e) {{}}

    // 2. Atribución de Leads y Campañas (WhatsApp, Email, Redes)
    const pLead = urlParams.get('lead') || urlParams.get('club') || urlParams.get('nombre') || '';
    const pTel = urlParams.get('tel') || urlParams.get('phone') || urlParams.get('c') || '';
    const pSource = urlParams.get('utm_source') || urlParams.get('src') || '';
    const pCampaign = urlParams.get('utm_campaign') || urlParams.get('camp') || urlParams.get('ruta') || '';
    const pMedium = urlParams.get('utm_medium') || '';

    try {{
      if (pLead) localStorage.setItem('cp_lead_name', pLead);
      if (pTel) localStorage.setItem('cp_lead_tel', pTel);
      if (pSource) localStorage.setItem('cp_utm_source', pSource);
      if (pCampaign) localStorage.setItem('cp_utm_campaign', pCampaign);
    }} catch(e) {{}}

    const leadName = pLead || (function(){{ try {{ return localStorage.getItem('cp_lead_name') || ''; }} catch(e){{ return ''; }} }})();
    const leadTel = pTel || (function(){{ try {{ return localStorage.getItem('cp_lead_tel') || ''; }} catch(e){{ return ''; }} }})();
    const utmSource = pSource || (function(){{ try {{ return localStorage.getItem('cp_utm_source') || ''; }} catch(e){{ return ''; }} }})();
    const utmCampaign = pCampaign || (function(){{ try {{ return localStorage.getItem('cp_utm_campaign') || ''; }} catch(e){{ return ''; }} }})();

    // 3. ID de Sesión e ID de Visitante
    function generateUid(prefix) {{
      return prefix + '_' + Date.now().toString(36) + '_' + Math.random().toString(36).substring(2, 6);
    }}

    let sessionId = '';
    try {{
      sessionId = sessionStorage.getItem('cp_session_id');
      if (!sessionId) {{
        sessionId = generateUid('s');
        sessionStorage.setItem('cp_session_id', sessionId);
      }}
    }} catch(e) {{
      sessionId = generateUid('s');
    }}

    let visitorId = '';
    let visitCount = 1;
    let isReturningVisitor = false;
    let recurrenceLabel = '';
    try {{
      visitorId = localStorage.getItem('cp_visitor_id');
      const nowMs = Date.now();
      if (!visitorId) {{
        visitorId = generateUid('v');
        localStorage.setItem('cp_visitor_id', visitorId);
        localStorage.setItem('cp_visit_count', '1');
        localStorage.setItem('cp_first_visit', nowMs.toString());
        localStorage.setItem('cp_last_visit', nowMs.toString());
      }} else {{
        let count = parseInt(localStorage.getItem('cp_visit_count') || '1', 10);
        const firstVisitMs = parseInt(localStorage.getItem('cp_first_visit') || nowMs.toString(), 10);
        const lastVisitMs = parseInt(localStorage.getItem('cp_last_visit') || nowMs.toString(), 10);

        if (!sessionStorage.getItem('cp_counted_in_session')) {{
          count++;
          localStorage.setItem('cp_visit_count', count.toString());
          sessionStorage.setItem('cp_counted_in_session', 'true');

          const diffHours = Math.max(0, Math.round((nowMs - lastVisitMs) / (1000 * 60 * 60)));
          const diffDays = Math.floor(diffHours / 24);
          let tiempoAtras = diffHours < 1 ? 'hace minutos' : (diffHours < 24 ? `hace ${{diffHours}}h` : `hace ${{diffDays}}d`);
          recurrenceLabel = `🔁 ${{count}}ª visita (${{tiempoAtras}})`;

          localStorage.setItem('cp_last_visit', nowMs.toString());
        }} else {{
          const diffHours = Math.max(0, Math.round((nowMs - lastVisitMs) / (1000 * 60 * 60)));
          const diffDays = Math.floor(diffHours / 24);
          let tiempoAtras = diffHours < 1 ? 'hace minutos' : (diffHours < 24 ? `hace ${{diffHours}}h` : `hace ${{diffDays}}d`);
          recurrenceLabel = count > 1 ? `🔁 ${{count}}ª visita (${{tiempoAtras}})` : '';
        }}
        visitCount = count;
        if (visitCount > 1) isReturningVisitor = true;
      }}
    }} catch(e) {{
      visitorId = generateUid('v');
    }}

    // 4.1 Geolocalización Silenciosa por IP (Ciudad, Región y País)
    let geoUbicacion = 'España';
    try {{
      const cachedGeo = sessionStorage.getItem('cp_geo');
      if (cachedGeo) {{
        geoUbicacion = cachedGeo;
      }} else {{
        fetch('https://ipapi.co/json/')
          .then(res => res.json())
          .then(data => {{
            if (data && data.city) {{
              geoUbicacion = `${{data.city}}, ${{data.region || ''}}, ${{data.country_code || 'ES'}}`.replace(', ,', ',');
              sessionStorage.setItem('cp_geo', geoUbicacion);
              syncClarityTags();
            }}
          }}).catch(() => {{}});
      }}
    }} catch(e) {{}}

    // 4. Detección Inteligente de Dispositivo y Origen
    function getDeviceInfo() {{
      const ua = navigator.userAgent || '';
      const platform = navigator.platform || '';
      const maxTouchPoints = navigator.maxTouchPoints || 0;

      let os = 'Desconocido';
      if (/iPhone/i.test(ua)) {{
        os = 'iPhone';
      }} else if (/iPad/i.test(ua) || (platform === 'MacIntel' && maxTouchPoints > 1)) {{
        os = 'iPad';
      }} else if (/iPod/i.test(ua)) {{
        os = 'iPod';
      }} else if (/Android/i.test(ua)) {{
        os = 'Android';
      }} else if (/Windows|Win32|Win64|WOW64/i.test(ua)) {{
        os = 'Windows';
      }} else if (/Macintosh|MacIntel|MacPPC|Mac68K/i.test(ua)) {{
        os = 'Mac';
      }} else if (/CrOS/i.test(ua)) {{
        os = 'ChromeOS';
      }} else if (/Linux/i.test(ua) || /X11/i.test(ua)) {{
        os = 'Linux';
      }} else if (/mobile/i.test(ua)) {{
        os = 'Móvil';
      }} else {{
        os = 'PC / Mac';
      }}

      let app = '';
      if (/WhatsApp/i.test(ua)) app = ' (WhatsApp)';
      else if (/Instagram/i.test(ua)) app = ' (Instagram)';
      else if (/FBAN|FBAV/i.test(ua)) app = ' (Facebook)';
      else if (/LinkedIn/i.test(ua)) app = ' (LinkedIn)';

      return {{
        dispositivo: os + app,
        so: os,
        resolucion: `${{window.screen.width}}x${{window.screen.height}}`
      }};
    }}

    function getLeadIdentification() {{
      if (isAdmin) return 'Javier (Admin)';
      if (leadName && leadTel) return `${{leadName}} (${{leadTel}})`;
      if (leadName) return leadName;
      if (leadTel) return leadTel;
      return ''; // En blanco si no se conoce el lead
    }}

    // Sincronización de variables personalizadas con Microsoft Clarity
    function syncClarityTags() {{
      if (window.clarity) {{
        try {{
          window.clarity("set", "lead_label", getLeadIdentification() || "Anónimo");
          window.clarity("set", "lead_score", calculateLeadScore());
          window.clarity("set", "geo", geoUbicacion);
          window.clarity("set", "visitas_total", visitCount.toString());
          window.clarity("set", "es_reincidente", isReturningVisitor ? "true" : "false");
          window.clarity("set", "dispositivo", getDeviceInfo().dispositivo);
          window.clarity("identify", visitorId, sessionId, undefined, leadName || undefined);
        }} catch(e) {{}}
      }}
    }}

    function getTrafficTypeLabel() {{
      if (isAdmin) return '👤 Propio (Admin)';
      if (utmSource.includes('whatsapp') || leadTel || document.referrer.includes('whatsapp')) return '🎯 Lead WhatsApp';
      if (utmSource.includes('email') || utmSource.includes('resend')) return '✉️ Lead Email';
      if (leadName) return '🎯 Lead Identificado';
      return '🌐 Tráfico Web';
    }}

    function getChannelOrigin() {{
      if (utmSource) return `Campaña: ${{utmSource}}${{utmCampaign ? ' (' + utmCampaign + ')' : ''}}`;
      const ref = document.referrer || '';
      if (!ref) return 'Enlace Directo';
      if (ref.includes('whatsapp.com')) return 'WhatsApp Web/App';
      if (ref.includes('instagram.com')) return 'Instagram';
      if (ref.includes('linkedin.com')) return 'LinkedIn';
      if (ref.includes('google.')) return 'Búsqueda Google';
      if (ref.includes('bing.')) return 'Búsqueda Bing';
      if (ref.includes('facebook.com')) return 'Facebook';
      return ref.replace(/^https?:\\/\\//, '').split('/')[0];
    }}

    // 5. Tiempo Activo y Medición por Secciones (Micro-tiempos)
    let activeSeconds = 0;
    let lastTick = Date.now();
    const sectionTimes = {{
      'Hero': 0,
      'Calculadora': 0,
      'FAQ': 0,
      'Contacto': 0
    }};

    setInterval(() => {{
      if (!document.hidden) {{
        const now = Date.now();
        const diff = Math.round((now - lastTick) / 1000);
        if (diff > 0 && diff < 5) {{
          activeSeconds += diff;
          if (currentSection.includes('Calculadora')) sectionTimes['Calculadora'] += diff;
          else if (currentSection.includes('FAQ') || currentSection.includes('Frecuentes')) sectionTimes['FAQ'] += diff;
          else if (currentSection.includes('Contacto')) sectionTimes['Contacto'] += diff;
          else sectionTimes['Hero'] += diff;
        }}
        lastTick = now;
      }} else {{
        lastTick = Date.now();
      }}
    }}, 1000);

    function formatTime(sec) {{
      const m = Math.floor(sec / 60);
      const s = sec % 60;
      return `${{m}}m ${{s < 10 ? '0' : ''}}${{s}}s`;
    }}

    function getSectionTimesSummary() {{
      return Object.entries(sectionTimes)
        .filter(([_, s]) => s > 0)
        .map(([k, s]) => `${{k}}: ${{s}}s`)
        .join(' | ') || '-';
    }}

    let hasInteractedWithCalc = false;
    let hasOpenedFaq = false;
    let hasCopiedContact = false;

    // 5.1 Cálculo del Termómetro de Interés (Lead Score)
    function calculateLeadScore() {{
      if (isAdmin) return '👤 Propio (Admin)';
      let score = 0;
      if (activeSeconds >= 120) score += 40;
      else if (activeSeconds >= 45) score += 25;
      else if (activeSeconds >= 20) score += 10;

      if (maxScrollPercent >= 85) score += 35;
      else if (maxScrollPercent >= 50) score += 20;

      if (hasInteractedWithCalc) score += 30;
      if (hasOpenedFaq) score += 20;
      if (hasCopiedContact) score += 35;
      if (leadName || leadTel) score += 15;
      if (isReturningVisitor) score += 25;

      if (score >= 65) return '🔥 Muy Caliente (A)';
      if (score >= 35) return '⚡ Interesado (B)';
      return '👀 Curioso (C)';
    }}

    // 6. Scroll y Secciones Vistas
    let maxScrollPercent = 0;
    let currentSection = 'Cabecera / Hero';
    const visitedSectionsList = ['Cabecera / Hero'];

    // IntersectionObserver para mapear secciones reales
    try {{
      const sectionMap = [
        {{ id: 'coverflow-0', name: 'Hero / Llaveros 3D' }},
        {{ id: 'llaveros', name: 'Calculadora de Pistas' }},
        {{ id: 'faq', name: 'Preguntas Frecuentes' }},
        {{ id: 'contacto', name: 'Contacto Final' }}
      ];

      const secObserver = new IntersectionObserver((entries) => {{
        entries.forEach(entry => {{
          if (entry.isIntersecting) {{
            const match = sectionMap.find(s => s.id === entry.target.id);
            if (match) {{
              currentSection = match.name;
              if (!visitedSectionsList.includes(match.name)) {{
                visitedSectionsList.push(match.name);
              }}
            }}
          }}
        }});
      }}, {{ threshold: 0.25 }});

      sectionMap.forEach(s => {{
        const el = document.getElementById(s.id);
        if (el) secObserver.observe(el);
      }});
    }} catch(e) {{}}

    // Medición de porcentaje de scroll
    window.addEventListener('scroll', () => {{
      const h = document.documentElement;
      const b = document.body;
      const st = 'scrollTop';
      const sh = 'scrollHeight';
      const scrollable = (h[sh] || b[sh]) - h.clientHeight;
      if (scrollable <= 0) return;
      const pct = Math.min(100, Math.round(((h[st] || b[st]) / scrollable) * 100));
      if (pct > maxScrollPercent) maxScrollPercent = pct;
    }}, {{ passive: true }});

    // 6.1 Detección de Copy-Paste
    document.addEventListener('copy', () => {{
      const text = (window.getSelection() ? window.getSelection().toString() : '').trim();
      if (text.includes('680') || text.includes('317486') || text.includes('+34')) {{
        hasCopiedContact = true;
        trackEvent('copiar_telefono', {{ evento_desc: '📋 Copió Teléfono de Javier' }});
      }} else if (text.includes('@coolpadel') || text.includes('javier@')) {{
        hasCopiedContact = true;
        trackEvent('copiar_email', {{ evento_desc: '📋 Copió Email de Javier' }});
      }}
    }});

    // 7. Función Central de Envío de Analítica
    function trackEvent(eventName, extraData = {{}}) {{
      if (!GOOGLE_SHEETS_WEBHOOK_URL) return;
      try {{
        const dev = getDeviceInfo();
        const payload = {{
          tipo: 'analitica_evento',
          session_id: sessionId,
          visitor_id: visitorId,
          visita_num: visitCount,
          lead_label: getLeadIdentification(),
          lead_name: leadName,
          lead_tel: leadTel,
          geo_ubicacion: geoUbicacion,
          lead_score: calculateLeadScore(),
          es_admin: isAdmin,
          tipo_trafico: getTrafficTypeLabel(),
          evento: eventName,
          evento_desc: extraData.evento_desc || eventName,
          pagina: window.location.pathname || '/',
          seccion_actual: currentSection,
          secciones_recorridas: visitedSectionsList.join(' > '),
          scroll_max: maxScrollPercent + '%',
          tiempo_activo: formatTime(activeSeconds),
          tiempo_segundos: activeSeconds,
          tiempos_seccion: getSectionTimesSummary(),
          dispositivo: dev.dispositivo,
          resolucion: dev.resolucion,
          idioma: currentLang,
          origen_canal: getChannelOrigin(),
          campana_utm: utmCampaign || utmSource || '',
          url_completa: window.location.href,
          ...extraData
        }};

        const jsonPayload = JSON.stringify(payload);
        if (navigator.sendBeacon) {{
          navigator.sendBeacon(GOOGLE_SHEETS_WEBHOOK_URL, jsonPayload);
        }} else {{
          fetch(GOOGLE_SHEETS_WEBHOOK_URL, {{
            method: 'POST',
            mode: 'no-cors',
            headers: {{ 'Content-Type': 'application/json' }},
            body: jsonPayload,
            keepalive: true
          }}).catch(() => {{}});
        }}
      }} catch(e) {{}}
    }}

    // Descarga de PDF Informe con recolección de email a Google Sheets
    async function handleReportDownload(e) {{
      e.preventDefault();
      const emailInput = document.getElementById('report-email-input');
      const email = emailInput ? emailInput.value.trim() : '';
      if (!email) return;

      const reportFiles = {{
        'es': {{ url: '{asset_prefix}assets/reports/padel-industry-report-es.pdf', name: 'CoolPadel-Reportaje-Industria-Padel-2026-ES.pdf' }},
        'en': {{ url: '{asset_prefix}assets/reports/padel-industry-report-en.pdf', name: 'CoolPadel-Padel-Industry-Report-2026-ENG.pdf' }},
        'it': {{ url: '{asset_prefix}assets/reports/padel-industry-report-it.pdf', name: 'CoolPadel-Report-Industria-Padel-2026-IT.pdf' }},
        'fr': {{ url: '{asset_prefix}assets/reports/padel-industry-report-en.pdf', name: 'CoolPadel-Padel-Industry-Report-2026.pdf' }}
      }};
      const activeReport = reportFiles[currentLang] || reportFiles['es'];

      const link = document.createElement('a');
      link.href = activeReport.url;
      link.download = activeReport.name;
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);

      // Guardar Lead en Sheet y Notificar
      if (GOOGLE_SHEETS_WEBHOOK_URL) {{
        try {{
          const dev = getDeviceInfo();
          fetch(GOOGLE_SHEETS_WEBHOOK_URL, {{
            method: 'POST',
            mode: 'no-cors',
            headers: {{ 'Content-Type': 'application/json' }},
            body: JSON.stringify({{
              tipo: 'lead_email',
              email: email,
              origen: `Descarga Informe Industria Padel 2026 [${{currentLang.toUpperCase()}}]`,
              lead_label: getLeadIdentification(),
              lead_name: leadName,
              lead_tel: leadTel,
              campana_utm: utmCampaign || utmSource || '',
              dispositivo: dev.dispositivo,
              fecha: new Date().toISOString()
            }})
          }}).catch(() => {{}});
        }} catch (err) {{}}
      }}

      trackEvent('descarga_informe', {{
        email_lead: email,
        evento_desc: `📥 Descargó Informe 2026 (${{email}})`
      }});

      const dict = I18N_DATA[currentLang] || I18N_DATA['es'];
      if (dict) {{
        const btn = e.target.querySelector('button[type="submit"] span');
        if (btn) {{
          const originalText = btn.textContent;
          btn.textContent = dict.report_card1_btn_success || '¡Informe Descargado!';
          setTimeout(() => {{
            btn.textContent = originalText;
            emailInput.value = '';
          }}, 3500);
        }}
      }}
      try {{
        localStorage.setItem('coolpadel_lead_dismissed', 'true');
        sessionStorage.setItem('coolpadel_lead_dismissed', 'true');
      }} catch(e) {{}}
    }}

    // POP-UP LEAD MAGNET LOGIC (TEMPORIZADOR PROGRESIVO Y NO INTRUSIVO)
    let modalTriggered = false;
    const pageStartTime = Date.now();

    window.openLeadModal = function() {{
      try {{
        if (modalTriggered || sessionStorage.getItem('coolpadel_lead_dismissed') || localStorage.getItem('coolpadel_lead_dismissed')) return;
      }} catch(e) {{}}
      modalTriggered = true;
      const modal = document.getElementById('lead-modal');
      const content = document.getElementById('lead-modal-content');
      if (modal && content) {{
        modal.classList.remove('opacity-0', 'pointer-events-none');
        modal.classList.add('opacity-100', 'pointer-events-auto');
        content.classList.remove('scale-95');
        content.classList.add('scale-100');
        trackEvent('modal_lead_abierto', {{ evento_desc: 'Pop-up Lead Magnet Mostrado' }});
      }}
    }};

    window.closeLeadModal = function() {{
      try {{
        sessionStorage.setItem('coolpadel_lead_dismissed', 'true');
        localStorage.setItem('coolpadel_lead_dismissed', 'true');
      }} catch(e) {{}}
      const modal = document.getElementById('lead-modal');
      const content = document.getElementById('lead-modal-content');
      if (modal && content) {{
        modal.classList.add('opacity-0', 'pointer-events-none');
        modal.classList.remove('opacity-100', 'pointer-events-auto');
        content.classList.add('scale-95');
        content.classList.remove('scale-100');
      }}
    }};

    // Triggers para el Pop-up: 50 segundos, scroll profundo (> 88%), o exit-intent tras 30s
    setTimeout(() => {{ openLeadModal(); }}, 50000);

    window.addEventListener('scroll', () => {{
      const scrollPct = (window.scrollY + window.innerHeight) / document.documentElement.scrollHeight;
      if (scrollPct > 0.88) openLeadModal();
    }}, {{ passive: true }});

    document.addEventListener('mouseleave', (e) => {{
      if (Date.now() - pageStartTime > 30000 && e.clientY <= 0) openLeadModal();
    }});

    async function handlePopupDownload(e) {{
      e.preventDefault();
      const emailInput = document.getElementById('popup-email-input');
      const email = emailInput ? emailInput.value.trim() : '';
      if (!email) return;

      const reportFiles = {{
        'es': {{ url: '{asset_prefix}assets/reports/padel-industry-report-es.pdf', name: 'CoolPadel-Reportaje-Industria-Padel-2026-ES.pdf' }},
        'en': {{ url: '{asset_prefix}assets/reports/padel-industry-report-en.pdf', name: 'CoolPadel-Padel-Industry-Report-2026-ENG.pdf' }},
        'it': {{ url: '{asset_prefix}assets/reports/padel-industry-report-it.pdf', name: 'CoolPadel-Report-Industria-Padel-2026-IT.pdf' }},
        'fr': {{ url: '{asset_prefix}assets/reports/padel-industry-report-en.pdf', name: 'CoolPadel-Padel-Industry-Report-2026.pdf' }}
      }};
      const activeReport = reportFiles[currentLang] || reportFiles['es'];

      const link = document.createElement('a');
      link.href = activeReport.url;
      link.download = activeReport.name;
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);

      try {{
        localStorage.setItem('coolpadel_lead_dismissed', 'true');
        sessionStorage.setItem('coolpadel_lead_dismissed', 'true');
      }} catch(e) {{}}

      if (GOOGLE_SHEETS_WEBHOOK_URL) {{
        try {{
          const dev = getDeviceInfo();
          fetch(GOOGLE_SHEETS_WEBHOOK_URL, {{
            method: 'POST',
            mode: 'no-cors',
            headers: {{ 'Content-Type': 'application/json' }},
            body: JSON.stringify({{
              tipo: 'lead_email',
              email: email,
              origen: `Lead Magnet Pop-up Modal [${{currentLang.toUpperCase()}}]`,
              lead_label: getLeadIdentification(),
              lead_name: leadName,
              lead_tel: leadTel,
              campana_utm: utmCampaign || utmSource || '',
              dispositivo: dev.dispositivo,
              fecha: new Date().toISOString()
            }})
          }}).catch(() => {{}});
        }} catch (err) {{}}
      }}

      trackEvent('descarga_informe_popup', {{
        email_lead: email,
        evento_desc: `📥 Descargó Informe desde Pop-up (${{email}})`
      }});

      const dict = I18N_DATA[currentLang] || I18N_DATA['es'];
      const btn = e.target.querySelector('button[type="submit"] span');
      if (btn) {{
        btn.textContent = dict.popup_btn_success || '¡Descargando Informe!';
        setTimeout(() => {{
          closeLeadModal();
        }}, 2200);
      }}
    }}

    // INICIALIZACIÓN DE IDIOMA CON AUTO-DETECCIÓN INTELIGENTE POR NAVEGADOR
    try {{
      const urlLang = urlParams.get('lang');
      const savedLang = localStorage.getItem('coolpadel_lang');
      
      let detectedLang = null;
      if (!savedLang && !urlLang) {{
        const navLang = (navigator.language || navigator.userLanguage || '').toLowerCase();
        if (navLang.startsWith('fr')) detectedLang = 'fr';
        else if (navLang.startsWith('it')) detectedLang = 'it';
        else if (navLang.startsWith('es')) detectedLang = 'es';
        else detectedLang = 'en';
      }}

      const initialLang = urlLang || savedLang || detectedLang;
      if (initialLang && I18N_DATA[initialLang] && initialLang !== '{active_lang}') {{
        switchLanguage(initialLang);
      }} else {{
        updateCalculator(0);
      }}
    }} catch(e) {{
      updateCalculator(0);
    }}

    // TRACKING DE CARGA INICIAL Y CLICS EN BOTONES WHATSAPP / INTERACCIONES
    try {{
      // 1. Registro de Visita Inicial
      trackEvent('pageview', {{
        evento_desc: '🟢 Visita Web',
        path: window.location.pathname,
        lang_activa: currentLang
      }});
      
      // 2. Clics en WhatsApp con atribución del botón exacto
      const attachClick = (id, eventName, btnLabel, getExtra) => {{
        const el = document.getElementById(id);
        if (el) {{
          el.addEventListener('click', () => {{
            trackEvent(eventName, {{
              ubicacion: btnLabel,
              evento_desc: `🎯 Clic WhatsApp [${{btnLabel}}]`,
              ...(getExtra ? getExtra() : {{}})
            }});
          }});
        }}
      }};

      attachClick('nav-contact-btn', 'click_whatsapp_nav', 'Cabecera PC');
      attachClick('nav-contact-btn-mob', 'click_whatsapp_nav_mob', 'Cabecera Móvil');
      attachClick('calc-wa-btn', 'click_whatsapp_calc', 'Calculadora Llaveros', () => ({{
        tier_unidades: tiers[currentTierIdx]?.qty,
        tier_precio: tiers[currentTierIdx]?.price
      }}));
      attachClick('contact-wa-btn', 'click_whatsapp_footer', 'Contacto Footer');
      attachClick('floating-wa-btn', 'click_whatsapp_floating', 'Botón Flotante');

      // 3. Tracking de interacción con slider de la calculadora al soltar
      let lastTierTracked = 0;
      const originalUpdateCalc = updateCalculator;
      const trackCalculatorDebounced = (idx) => {{
        if (idx !== lastTierTracked) {{
          lastTierTracked = idx;
          hasInteractedWithCalc = true;
          const tData = tiers[idx];
          if (tData) {{
            trackEvent('calculadora_interaccion', {{
              tier_unidades: tData.qty,
              tier_precio: tData.price,
              evento_desc: `📊 Calculadora: ${{tData.qty}} llaveros (${{tData.price}}€)`
            }});
          }}
        }}
      }};
      
      if (sliderBox) {{
        sliderBox.addEventListener('pointerup', () => trackCalculatorDebounced(currentTierIdx));
        sliderBox.addEventListener('touchend', () => trackCalculatorDebounced(currentTierIdx));
      }}

      // 4. Registro de Sesión Finalizada al salir o cambiar de pestaña
      window.addEventListener('visibilitychange', () => {{
        if (document.visibilityState === 'hidden') {{
          trackEvent('sesion_finalizada', {{
            evento_desc: `🏁 Fin de Sesión (Tiempo: ${{formatTime(activeSeconds)}}, Scroll: ${{maxScrollPercent}}%)`
          }});
        }}
      }});

      window.addEventListener('pagehide', () => {{
        trackEvent('sesion_finalizada', {{
          evento_desc: `🏁 Fin de Sesión (Tiempo: ${{formatTime(activeSeconds)}}, Scroll: ${{maxScrollPercent}}%)`
        }});
      }});
    }} catch(e) {{}}
  </script>
</body>
</html>"""
    return html

def build_all():
    import sys
    if sys.platform == "win32" and hasattr(sys.stdout, "reconfigure"):
        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except Exception:
            pass
    print(">> Generando versiones con Responsive Movil y Multilingue (ES, EN, FR, IT)...")
    
    # 1. Página principal (Español)
    es_html = get_base_html("es", is_subfolder=False)
    with open("coolpadel-web/index.html", "w", encoding="utf-8") as f:
        f.write(es_html)
    print("  [OK] coolpadel-web/index.html (ES Principal)")

    # 2. Subcarpetas para indexación SEO multilingüe
    for lang in ["en", "fr", "it"]:
        os.makedirs(f"coolpadel-web/{lang}", exist_ok=True)
        lang_html = get_base_html(lang, is_subfolder=True)
        with open(f"coolpadel-web/{lang}/index.html", "w", encoding="utf-8") as f:
            f.write(lang_html)
        print(f"  [OK] coolpadel-web/{lang}/index.html ({lang.upper()} SEO Landing)")

    # 3. Sitemap Multilingüe
    from datetime import datetime
    today_iso = datetime.now().strftime("%Y-%m-%d")
    sitemap_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:xhtml="http://www.w3.org/1999/xhtml"
        xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">
  <url>
    <loc>https://coolpadelstudios.com/</loc>
    <xhtml:link rel="alternate" hreflang="es" href="https://coolpadelstudios.com/"/>
    <xhtml:link rel="alternate" hreflang="en" href="https://coolpadelstudios.com/en/"/>
    <xhtml:link rel="alternate" hreflang="fr" href="https://coolpadelstudios.com/fr/"/>
    <xhtml:link rel="alternate" hreflang="it" href="https://coolpadelstudios.com/it/"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="https://coolpadelstudios.com/"/>
    <lastmod>{today_iso}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
    <image:image>
      <image:loc>https://coolpadelstudios.com/assets/images/llaveros%201.jpg</image:loc>
      <image:title>Llaveros de pádel de goma 3D personalizados</image:title>
      <image:caption>Llaveros de pádel personalizados con logo oficial para clubes y torneos</image:caption>
    </image:image>
    <image:image>
      <image:loc>https://coolpadelstudios.com/assets/images/llaveros%202.jpg</image:loc>
      <image:title>Llaveros de tenis y pádel personalizados</image:title>
      <image:caption>Llaveros personalizados para academias y escuelas deportivas</image:caption>
    </image:image>
    <image:image>
      <image:loc>https://coolpadelstudios.com/assets/images/slide-1.jpg</image:loc>
      <image:title>Llaveros de pádel personalizados para clubs CoolPadel</image:title>
    </image:image>
  </url>
  <url>
    <loc>https://coolpadelstudios.com/en/</loc>
    <xhtml:link rel="alternate" hreflang="es" href="https://coolpadelstudios.com/"/>
    <xhtml:link rel="alternate" hreflang="en" href="https://coolpadelstudios.com/en/"/>
    <xhtml:link rel="alternate" hreflang="fr" href="https://coolpadelstudios.com/fr/"/>
    <xhtml:link rel="alternate" hreflang="it" href="https://coolpadelstudios.com/it/"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="https://coolpadelstudios.com/"/>
    <lastmod>{today_iso}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
  </url>
  <url>
    <loc>https://coolpadelstudios.com/fr/</loc>
    <xhtml:link rel="alternate" hreflang="es" href="https://coolpadelstudios.com/"/>
    <xhtml:link rel="alternate" hreflang="en" href="https://coolpadelstudios.com/en/"/>
    <xhtml:link rel="alternate" hreflang="fr" href="https://coolpadelstudios.com/fr/"/>
    <xhtml:link rel="alternate" hreflang="it" href="https://coolpadelstudios.com/it/"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="https://coolpadelstudios.com/"/>
    <lastmod>{today_iso}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
  </url>
  <url>
    <loc>https://coolpadelstudios.com/it/</loc>
    <xhtml:link rel="alternate" hreflang="es" href="https://coolpadelstudios.com/"/>
    <xhtml:link rel="alternate" hreflang="en" href="https://coolpadelstudios.com/en/"/>
    <xhtml:link rel="alternate" hreflang="fr" href="https://coolpadelstudios.com/fr/"/>
    <xhtml:link rel="alternate" hreflang="it" href="https://coolpadelstudios.com/it/"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="https://coolpadelstudios.com/"/>
    <lastmod>{today_iso}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
  </url>
  <url>
    <loc>https://coolpadelstudios.com/blog/</loc>
    <lastmod>2026-10-14</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://coolpadelstudios.com/blog/highlights-03/</loc>
    <lastmod>2026-10-14</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
  <url>
    <loc>https://coolpadelstudios.com/blog/highlights-02/</loc>
    <lastmod>2026-10-14</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
  <url>
    <loc>https://coolpadelstudios.com/blog/highlights-01/</loc>
    <lastmod>2026-10-14</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
  <url>
    <loc>https://coolpadelstudios.com/camaras/</loc>
    <xhtml:link rel="alternate" hreflang="es" href="https://coolpadelstudios.com/camaras/"/>
    <xhtml:link rel="alternate" hreflang="en" href="https://coolpadelstudios.com/en/camaras/"/>
    <xhtml:link rel="alternate" hreflang="fr" href="https://coolpadelstudios.com/fr/camaras/"/>
    <xhtml:link rel="alternate" hreflang="it" href="https://coolpadelstudios.com/it/camaras/"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="https://coolpadelstudios.com/camaras/"/>
    <lastmod>{today_iso}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.85</priority>
  </url>
  <url>
    <loc>https://coolpadelstudios.com/en/camaras/</loc>
    <xhtml:link rel="alternate" hreflang="es" href="https://coolpadelstudios.com/camaras/"/>
    <xhtml:link rel="alternate" hreflang="en" href="https://coolpadelstudios.com/en/camaras/"/>
    <xhtml:link rel="alternate" hreflang="fr" href="https://coolpadelstudios.com/fr/camaras/"/>
    <xhtml:link rel="alternate" hreflang="it" href="https://coolpadelstudios.com/it/camaras/"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="https://coolpadelstudios.com/camaras/"/>
    <lastmod>{today_iso}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://coolpadelstudios.com/fr/camaras/</loc>
    <xhtml:link rel="alternate" hreflang="es" href="https://coolpadelstudios.com/camaras/"/>
    <xhtml:link rel="alternate" hreflang="en" href="https://coolpadelstudios.com/en/camaras/"/>
    <xhtml:link rel="alternate" hreflang="fr" href="https://coolpadelstudios.com/fr/camaras/"/>
    <xhtml:link rel="alternate" hreflang="it" href="https://coolpadelstudios.com/it/camaras/"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="https://coolpadelstudios.com/camaras/"/>
    <lastmod>{today_iso}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://coolpadelstudios.com/it/camaras/</loc>
    <xhtml:link rel="alternate" hreflang="es" href="https://coolpadelstudios.com/camaras/"/>
    <xhtml:link rel="alternate" hreflang="en" href="https://coolpadelstudios.com/en/camaras/"/>
    <xhtml:link rel="alternate" hreflang="fr" href="https://coolpadelstudios.com/fr/camaras/"/>
    <xhtml:link rel="alternate" hreflang="it" href="https://coolpadelstudios.com/it/camaras/"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="https://coolpadelstudios.com/camaras/"/>
    <lastmod>{today_iso}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://coolpadelstudios.com/politica-de-devoluciones.html</loc>
    <lastmod>2026-10-14</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.6</priority>
  </url>
  <url>
    <loc>https://coolpadelstudios.com/camaras-grabacion-pistas-padel/</loc>
    <lastmod>{today_iso}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.95</priority>
  </url>
  <url>
    <loc>https://coolpadelstudios.com/llaveros-padel-personalizados/</loc>
    <lastmod>{today_iso}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.95</priority>
  </url>
  <url>
    <loc>https://coolpadelstudios.com/llaveros-tenis-personalizados/</loc>
    <lastmod>{today_iso}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
  </url>
  <url>
    <loc>https://coolpadelstudios.com/welcome-packs-torneos-padel/</loc>
    <lastmod>{today_iso}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
  </url>
  <url>
    <loc>https://coolpadelstudios.com/llaveros-personalizados-clubs-padel/</loc>
    <lastmod>{today_iso}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
  </url>
  <url>
    <loc>https://coolpadelstudios.com/franquicias-padel/</loc>
    <lastmod>{today_iso}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.95</priority>
  </url>
</urlset>
"""
    with open("coolpadel-web/sitemap.xml", "w", encoding="utf-8") as f:
        f.write(sitemap_xml)
    print("  [OK] coolpadel-web/sitemap.xml (Sitemap XML Multilingüe)")

    # 2.5. Página Blog & Newsletter (con Reportaje 2026 y Artículos de LinkedIn)
    try:
        from build_blog import generate_blog_html
        generate_blog_html()
    except Exception as e:
        print(f"  [ERROR] Al generar Blog: {e}")

    # 2.6. Landings B2B Transaccionales (Pádel, Tenis, Torneos, Clubs)
    try:
        from build_landing_pages import build_all_landings
        build_all_landings()
    except Exception as e:
        print(f"  [ERROR] Al generar Landings B2B: {e}")

    # 2.7. Directorio de Franquicias y Cadenas de Pádel (+1 Club)
    try:
        from build_franquicias import main as build_franquicias_main
        build_franquicias_main()
    except Exception as e:
        print(f"  [ERROR] Al generar Directorio de Franquicias: {e}")

    # 4. RSS Feed para indexación y agregadores de noticias/crawlers
    rss_xml = """<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
  <channel>
    <title>CoolPadel Studios | Llaveros de Pádel Personalizados &amp; Blog</title>
    <link>https://coolpadelstudios.com</link>
    <description>Fabricante directo de llaveros de pádel personalizados de goma 3D, tecnología Save my Play y Newsletter de la Industria.</description>
    <language>es-es</language>
    <atom:link href="https://coolpadelstudios.com/rss.xml" rel="self" type="application/rss+xml" />
    <item>
      <title>Llaveros de Pádel Personalizados para Clubs con Logo Oficial en Relieve 3D</title>
      <link>https://coolpadelstudios.com/llaveros-padel-personalizados/</link>
      <guid>https://coolpadelstudios.com/llaveros-padel-personalizados/</guid>
      <description>Fabricación de llaveros de pádel de goma 3D personalizados desde 100 unidades con diseño 3D gratis, muestra física previa en ~15 días laborables por 15€ (100% descontable) y entrega del pedido en torno a un mes.</description>
      <pubDate>Fri, 18 Sep 2026 10:00:00 +0200</pubDate>
    </item>
    <item>
      <title>Directorio Oficial de Franquicias y Cadenas de Pádel (167 Grupos y +828 Clubs)</title>
      <link>https://coolpadelstudios.com/franquicias-padel/</link>
      <guid>https://coolpadelstudios.com/franquicias-padel/</guid>
      <description>Base de datos verificada de las 167 franquicias, operadores multi-sede y cadenas de clubes de pádel en España, Europa, Estados Unidos y Latinoamérica.</description>
      <pubDate>Thu, 15 Oct 2026 10:00:00 +0200</pubDate>
    </item>
    <item>
      <title>Highlights #01: Padel World Summit 2026 - Startup Recap por Javier Villoria</title>
      <link>https://coolpadelstudios.com/blog/highlights-01/</link>
      <guid>https://coolpadelstudios.com/blog/highlights-01/</guid>
      <description>Conversaciones una a una con las 20 startups del Innovation Arena: la realidad del mercado de raqueta y cómo diferenciarse.</description>
      <pubDate>Wed, 14 Oct 2026 10:00:00 +0200</pubDate>
    </item>
    <item>
      <title>Highlights #02: ¿Por qué todos hablan de Estados Unidos y Reino Unido?</title>
      <link>https://coolpadelstudios.com/blog/highlights-02/</link>
      <guid>https://coolpadelstudios.com/blog/highlights-02/</guid>
      <description>Análisis del boom del pádel en EE. UU. y Reino Unido: inversión inmobiliaria, membresías premium y retos de rentabilidad para clubes.</description>
      <pubDate>Wed, 14 Oct 2026 10:00:00 +0200</pubDate>
    </item>
    <item>
      <title>Highlights #03: ¿Cómo crece realmente la industria del pádel?</title>
      <link>https://coolpadelstudios.com/blog/highlights-03/</link>
      <guid>https://coolpadelstudios.com/blog/highlights-03/</guid>
      <description>Análisis del crecimiento de oferta y demanda en la industria del pádel, academias y modelos de negocio de clubes.</description>
      <pubDate>Wed, 14 Oct 2026 10:00:00 +0200</pubDate>
    </item>
  </channel>
</rss>
"""
    with open("coolpadel-web/rss.xml", "w", encoding="utf-8") as f:
        f.write(rss_xml)
    print("  [OK] coolpadel-web/rss.xml (Feed RSS 2.0)")

    # 5. Google Merchant Center Feed (Google Shopping Free Listings)
    merchant_xml = """<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:g="http://base.google.com/ns/1.0">
  <channel>
    <title>CoolPadel Studios - Catálogo Oficial de Llaveros de Pádel</title>
    <link>https://coolpadelstudios.com</link>
    <description>Catálogo B2B de llaveros de pádel y tenis personalizados en goma 3D para Google Shopping y Google Merchant</description>
    <item>
      <g:id>LLAVERO-PADEL-100</g:id>
      <g:title>Llaveros de Pádel Personalizados 3D (Pack 100 unidades - 3,00 €/ud)</g:title>
      <g:description>Pack de 100 llaveros de pádel personalizados de goma 3D con logo oficial para clubes y torneos. Muestra física previa en ~15 días laborables y entrega en ~1 mes.</g:description>
      <g:link>https://coolpadelstudios.com/llaveros-padel-personalizados/</g:link>
      <g:image_link>https://coolpadelstudios.com/assets/images/llaveros%201.jpg</g:image_link>
      <g:additional_image_link>https://coolpadelstudios.com/assets/images/slide-1.jpg</g:additional_image_link>
      <g:availability>in_stock</g:availability>
      <g:price>300.00 EUR</g:price>
      <g:brand>CoolPadel</g:brand>
      <g:condition>new</g:condition>
      <g:google_product_category>Sporting Goods &gt; Racquet Sports &gt; Padel</g:google_product_category>
    </item>
    <item>
      <g:id>LLAVERO-PADEL-250</g:id>
      <g:title>Llaveros de Pádel Personalizados 3D (Pack 250 unidades - 2,50 €/ud)</g:title>
      <g:description>Pack de 250 llaveros de pádel personalizados de goma 3D con logo oficial para clubes y torneos (2,50 €/ud). Muestra física previa deducible y envíos incluidos.</g:description>
      <g:link>https://coolpadelstudios.com/llaveros-padel-personalizados/</g:link>
      <g:image_link>https://coolpadelstudios.com/assets/images/llaveros%201.jpg</g:image_link>
      <g:additional_image_link>https://coolpadelstudios.com/assets/images/slide-1.jpg</g:additional_image_link>
      <g:availability>in_stock</g:availability>
      <g:price>625.00 EUR</g:price>
      <g:brand>CoolPadel</g:brand>
      <g:condition>new</g:condition>
      <g:google_product_category>Sporting Goods &gt; Racquet Sports &gt; Padel</g:google_product_category>
    </item>
    <item>
      <g:id>LLAVERO-PADEL-500</g:id>
      <g:title>Llaveros de Pádel Personalizados 3D (Pack 500 unidades - 2,00 €/ud)</g:title>
      <g:description>Pack de 500 llaveros de pádel personalizados de goma 3D con logo oficial para clubes y welcome packs de torneos (2,00 €/ud). Muestra física previa deducible.</g:description>
      <g:link>https://coolpadelstudios.com/welcome-packs-torneos-padel/</g:link>
      <g:image_link>https://coolpadelstudios.com/assets/images/llaveros%201.jpg</g:image_link>
      <g:additional_image_link>https://coolpadelstudios.com/assets/images/slide-1.jpg</g:additional_image_link>
      <g:availability>in_stock</g:availability>
      <g:price>1000.00 EUR</g:price>
      <g:brand>CoolPadel</g:brand>
      <g:condition>new</g:condition>
      <g:google_product_category>Sporting Goods &gt; Racquet Sports &gt; Padel</g:google_product_category>
    </item>
    <item>
      <g:id>LLAVERO-PADEL-1500</g:id>
      <g:title>Llaveros de Pádel Personalizados 3D (Pack 1.500 unidades - 1,50 €/ud)</g:title>
      <g:description>Pack mayorista de 1.500 llaveros de pádel personalizados de goma 3D con logo oficial para grandes clubes, cadenas y circuitos (1,50 €/ud).</g:description>
      <g:link>https://coolpadelstudios.com/llaveros-personalizados-clubs-padel/</g:link>
      <g:image_link>https://coolpadelstudios.com/assets/images/llaveros%201.jpg</g:image_link>
      <g:additional_image_link>https://coolpadelstudios.com/assets/images/slide-1.jpg</g:additional_image_link>
      <g:availability>in_stock</g:availability>
      <g:price>2250.00 EUR</g:price>
      <g:brand>CoolPadel</g:brand>
      <g:condition>new</g:condition>
      <g:google_product_category>Sporting Goods &gt; Racquet Sports &gt; Padel</g:google_product_category>
    </item>
    <item>
      <g:id>LLAVERO-PADEL-MUESTRA</g:id>
      <g:title>Muestra Física Real Llavero de Pádel Personalizado (100% Descontable)</g:title>
      <g:description>Muestra física real de llavero de pádel en relieve 3D con el logotipo de tu club entregada en ~15 días laborables (100% descontable del pedido final).</g:description>
      <g:link>https://coolpadelstudios.com/#llaveros</g:link>
      <g:image_link>https://coolpadelstudios.com/assets/images/llaveros%202.jpg</g:image_link>
      <g:availability>in_stock</g:availability>
      <g:price>15.00 EUR</g:price>
      <g:brand>CoolPadel</g:brand>
      <g:condition>new</g:condition>
      <g:google_product_category>Sporting Goods &gt; Racquet Sports &gt; Padel</g:google_product_category>
    </item>
  </channel>
</rss>
"""
    with open("coolpadel-web/google-merchant-feed.xml", "w", encoding="utf-8") as f:
        f.write(merchant_xml)
    print("  [OK] coolpadel-web/google-merchant-feed.xml (Google Shopping Feed)")

if __name__ == "__main__":
    build_all()
