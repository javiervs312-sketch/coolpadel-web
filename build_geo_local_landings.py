#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generador de Landings B2B Geo-Locales específicas por idioma y mercado.
Cada país ataca únicamente sus propias ciudades clave con contenido, modismos y GEO Schema nativos.
"""
import os
import re
import urllib.parse
from datetime import datetime

DOMAIN = "https://coolpadelstudios.com"
TODAY = datetime.utcnow().strftime("%Y-%m-%d")

LOCAL_LANDINGS = [
    # ========================== ES (España) ==========================
    {
        "lang": "es",
        "slug": "camaras-padel-madrid",
        "geo_region": "ES-MD",
        "geo_placename": "Madrid, España",
        "geo_position": "40.4168;-3.7038",
        "title": "Cámaras Pádel Madrid [Hub Oficial · 45€/mes] | Save My Play",
        "meta_desc": "Cámaras Save my Play en Madrid y zona centro (+1.500 pistas). Grabación en 5 min sin obras, repeticiones por QR, cuota desde 45€/mes y soporte directo.",
        "badge": "MADRID HUB · SAVE MY PLAY ESPAÑA",
        "breadcrumb_leaf": "Pistas Madrid",
        "h1": "Cámaras Inteligentes para Pistas de Pádel en Madrid",
        "subtitle": "Equipa tus pistas en la Comunidad de Madrid con la tecnología en pista líder: grabación Full HD con pulsador en red, descarga de highlights por QR y retransmisión de torneos sin obras.",
        "hero_img": "assets/images/savemyplay-1.jpg",
        "hero_img_alt": "Cámaras Save my Play para pistas de pádel en Madrid",
        "wa_msg": "Hola Javier, tenemos un club de pádel en Madrid y queremos información y demo de Save My Play",
        "price_anchor": "Hardware 180 € / pista · Software 45 €/mes · Soporte local en Madrid",
        "target_audience": "Directores de clubes de pádel, complejos municipales y academias en Madrid, Alcobendas, Pozuelo, Las Rozas, Alcalá y Getafe.",
        "quick_summary": {
            "label_1": "Hardware Pista", "val_1": "180 € en propiedad por pista",
            "label_2": "Cuota Software", "val_2": "45 € / mes por pista · Sin permanencia",
            "label_3": "Soporte Central", "val_3": "Equipo técnico directo en Madrid",
            "label_4": "Instalación", "val_4": "Montaje en 5 min sin cables ni rozas",
            "p": "Instalación oficial de cámaras Save My Play en Madrid. Retransmisión de torneos y descarga inmediata de clips de 25 segundos para tus jugadores sin necesidad de registrarse en apps."
        },
        "benefits": [
            ("Soporte Directo y Demos en Madrid", "Atención directa con Javier Villoria y demos online en 15 minutos para gerentes y directores de escuela."),
            ("Envío Inmediato en 24-48h", "Stock disponible en España sin esperas transatlánticas ni trámites de aduana."),
            ("Autonomía 100% Digital en Pista", "Los jugadores escanean el código QR en el poste y descargan sus mejores jugadas al instante.")
        ],
        "faqs": [
            ("¿Dais cobertura en toda la Comunidad de Madrid?", "Sí, atendemos Madrid capital, Pozuelo, Majadahonda, Las Rozas, Alcobendas, San Sebastián de los Reyes, Alcorcón, Getafe, Alcalá de Henares y alrededores."),
            ("¿Requiere obras o cables por la pista?", "Cero obras. El hardware se fija al poste en 5 minutos y se alimenta de la corriente de la pista."),
            ("¿Hay contrato de permanencia?", "No. Pagas mes a mes (45€/mes) y cancelas cuando quieras sin penalización.")
        ]
    },
    {
        "lang": "es",
        "slug": "camaras-padel-barcelona",
        "geo_region": "ES-CT",
        "geo_placename": "Barcelona, Catalunya",
        "geo_position": "41.3879;2.1699",
        "title": "Cámaras Pádel Barcelona y Cataluña [45€/mes] | Save My Play",
        "meta_desc": "Cámaras Save my Play en Barcelona y Cataluña. Grabación con pulsador en red, descarga instantánea por QR y 0 permanencia para clubes de pádel.",
        "badge": "BARCELONA & CATALUÑA · SAVE MY PLAY",
        "breadcrumb_leaf": "Pistas Barcelona",
        "h1": "Cámaras y Grabación de Partidos de Pádel en Barcelona",
        "subtitle": "La solución de vídeo más ágil para clubes indoor y outdoor en Barcelona y Cataluña: repetición instantánea en móvil, retransmisión de torneos y cero permanencia.",
        "hero_img": "assets/images/savemyplay-2.jpg",
        "hero_img_alt": "Cámaras Save my Play para pistas de pádel en Barcelona y Cataluña",
        "wa_msg": "Hola Javier, tenemos un club de pádel en Barcelona y queremos presupuesto para cámaras Save My Play",
        "price_anchor": "Hardware 180 € / pista · Software 45 €/mes · Envíos inmediatos",
        "target_audience": "Gerentes y clubes de pádel en Barcelona, área metropolitana y provincias de Girona, Tarragona y Lleida.",
        "quick_summary": {
            "label_1": "Hardware Pista", "val_1": "180 € en propiedad por pista",
            "label_2": "Cuota Software", "val_2": "45 € / mes por pista · Sin permanencia",
            "label_3": "Resistencia", "val_3": "Carcasa sellada IP para clima costero e indoor",
            "label_4": "Puesta en Marcha", "val_4": "Envío configurado en 48h con montaje en 5 min",
            "p": "Sistemas de grabación inteligente en pista Save My Play para clubes de pádel en Barcelona, Badalona, Sant Cugat, Sabadell y Cataluña."
        },
        "benefits": [
            ("Retransmisión de Circuitos y Ligas Catalanas", "Emite en directo por YouTube con marcadores las fases finales de torneos catalanes federados y sociales."),
            ("Resistencia a Ambientes Costeros e Indoor", "Carcasa sellada IP resistente a la humedad marina y condensación habitual en centros deportivos del litoral."),
            ("Autonomía 100% Digital", "Los jugadores descargan en segundos escaneando el código QR con cualquier smartphone.")
        ],
        "faqs": [
            ("¿En qué municipios de Barcelona dais cobertura?", "Enviamos e instalamos en Barcelona capital, Hospitalet, Badalona, Sant Cugat del Vallès, Sabadell, Terrassa, Mataró, Castelldefels y toda Cataluña."),
            ("¿Cuánto tarda el envío y puesta en marcha?", "Enviamos el equipo configurado en 48 horas. Solo necesitas atornillar la fijación al poste (5 minutos) y conectar a 220V."),
            ("¿Se pueden personalizar los vídeos con el escudo del club?", "Sí, cada clip descargado o emitido en streaming incluye el logo oficial del club y patrocinadores.")
        ]
    },
    {
        "lang": "es",
        "slug": "camaras-padel-valencia",
        "geo_region": "ES-VC",
        "geo_placename": "Valencia, España",
        "geo_position": "39.4699;-0.3763",
        "title": "Cámaras Pistas Pádel Valencia [0 Obras · 45€/mes] | Save My Play",
        "meta_desc": "Cámaras Save my Play en Valencia y Comunidad Valenciana (Paterna, Torrent, Alzira, Gandia). Grabación en 5 min sin obras, pulsador en red y 0 permanencia.",
        "badge": "COMUNIDAD VALENCIANA · SAVE MY PLAY",
        "breadcrumb_leaf": "Pistas Valencia",
        "h1": "Cámaras Inteligentes para Pistas de Pádel en Valencia",
        "subtitle": "La tecnología de pista para clubes de pádel en Valencia y Alicante: grabación de partidos con pulsador en red, repeticiones por QR y retransmisión de torneos sin obras.",
        "hero_img": "assets/images/savemyplay-1.jpg",
        "hero_img_alt": "Cámaras Save my Play para pistas de pádel en clubes de Valencia",
        "wa_msg": "Hola Javier, tenemos pistas de pádel en Valencia y queremos presupuesto para cámaras Save My Play",
        "price_anchor": "Hardware 180 € / pista · Software 45 €/mes · Sin obras ni permanencia",
        "target_audience": "Directores de clubes de pádel, complejos indoor y clubes de tenis en Valencia, Castellón y Alicante.",
        "quick_summary": {
            "label_1": "Hardware Pista", "val_1": "180 € en propiedad por pista",
            "label_2": "Cuota Software", "val_2": "45 € / mes por pista · Sin permanencia",
            "label_3": "Resistencia", "val_3": "Tratamiento sellado IP para clima costero e indoor",
            "label_4": "Instalación", "val_4": "Montaje en 5 min sin rozas ni cortes de reservas",
            "p": "Instalación de cámaras inteligentes Save My Play en clubes de pádel de Valencia, Paterna, Torrent, Sagunto y Gandia."
        },
        "benefits": [
            ("Cobertura Completa en la Comunidad Valenciana", "Envíos configurados en 48 horas para clubes de Valencia, Alicante y Castellón."),
            ("Resistencia al Clima Mediterráneo", "Carcasa sellada IP preparada para humedad costera y calor en pistas outdoor y naves industriales."),
            ("Monetización y Llenado de Horas Valle", "Atrae a jugadores de ligas locales y escuelas que buscan grabarse y compartir jugadas en redes.")
        ],
        "faqs": [
            ("¿En qué localidades de Valencia dais servicio?", "Damos servicio a Valencia capital, Paterna, Torrent, Alzira, Gandia, Sagunto, Manises, Xàtiva y municipios limítrofes."),
            ("¿Cuánto tiempo cuesta poner las cámaras en un club de Valencia?", "El montaje se realiza en 5 minutos por pista. Un club de 8 pistas queda listo en una sola mañana sin parar partidos."),
            ("¿Los jugadores tienen que instalar alguna app?", "No. El jugador pulsa el botón en el poste tras un gran punto y al salir de pista escanea el QR con la cámara de su móvil.")
        ]
    },
    {
        "lang": "es",
        "slug": "camaras-padel-malaga",
        "geo_region": "ES-AN",
        "geo_placename": "Málaga, Andalucía",
        "geo_position": "36.7213;-4.4214",
        "title": "Cámaras Pistas Pádel Málaga & Costa del Sol [45€/mes] | Save My Play",
        "meta_desc": "Cámaras Save my Play en Málaga y Costa del Sol (Marbella, Fuengirola, Mijas, Estepona). Grabación de pádel en 5 min sin obras, sin cables y sin permanencia.",
        "badge": "MÁLAGA & COSTA DEL SOL · SAVE MY PLAY",
        "breadcrumb_leaf": "Pistas Málaga & Costa del Sol",
        "h1": "Cámaras de Pádel en Málaga y Costa del Sol",
        "subtitle": "La solución de grabación favorita para el epicentro del pádel europeo: Marbella, Fuengirola, Mijas y Málaga capital. Descarga de jugadas por QR y retransmisión de torneos.",
        "hero_img": "assets/images/savemyplay-3.jpg",
        "hero_img_alt": "Cámaras Save my Play para clubes de pádel en Málaga y Costa del Sol",
        "wa_msg": "Hola Javier, gestionamos un club de pádel en la Costa del Sol y queremos información de cámaras Save My Play",
        "price_anchor": "Hardware 180 € / pista · Cuota 45 €/mes · Calidad óptica deportiva",
        "target_audience": "Clubes turísticos, resorts, academias internacionales y complejos de pádel en Málaga y la Costa del Sol.",
        "quick_summary": {
            "label_1": "Hardware Pista", "val_1": "180 € en propiedad por pista",
            "label_2": "Cuota Software", "val_2": "45 € / mes por pista · Sin permanencia",
            "label_3": "Público Internacional", "val_3": "Visor QR multilingüe (ES, EN, FR, DE, SE)",
            "label_4": "Instalación", "val_4": "5 min fijada al poste sin zanjas ni obras",
            "p": "Cámaras de grabación deportiva Save My Play para clubes de pádel en Málaga, Marbella, Benalmádena, Fuengirola y Estepona."
        },
        "benefits": [
            ("Ideal para Jugadores Internacionales en la Costa del Sol", "Sin registros obligatorios ni apps: el código QR abre el vídeo en el navegador móvil en segundos."),
            ("Streaming Profesional para Torneos y Circuitos", "Emite en directo a YouTube torneos internacionales FIP o circuitos sociales con marcadores y patrocinadores."),
            ("Cero Obras Civiles en Pistas Panorámicas", "Fijación universal que no daña el cristal ni la estructura metálica de pistas premium.")
        ],
        "faqs": [
            ("¿Funciona bien con jugadores extranjeros que vienen de vacaciones?", "Perfectamente. No requiere descargar apps de tiendas regionales: se escanea el código QR y el vídeo se descarga en el navegador."),
            ("¿Resiste las altas temperaturas y el sol en Málaga?", "Sí, cuenta con protección térmica y óptica deportiva antirreflejo para luz solar directa y focos LED de noche."),
            ("¿Cómo se realiza el soporte y los envíos?", "Enviamos las cámaras configuradas listas para conectar a corriente en 48 horas.")
        ]
    },

    # ========================== EN (UK & USA) ==========================
    {
        "lang": "en",
        "slug": "padel-court-cameras-london",
        "geo_region": "GB-LND",
        "geo_placename": "London, United Kingdom",
        "geo_position": "51.5074;-0.1278",
        "title": "Smart Padel Court Cameras in London & UK | Save My Play",
        "meta_desc": "Smart AI padel court cameras for clubs in London, Bristol & South East England. Instant net button highlights, QR mobile replays, and zero lock-in from €45/mo.",
        "badge": "LONDON & UK · SAVE MY PLAY",
        "breadcrumb_leaf": "London Courts",
        "h1": "Smart Padel Court Recording Cameras in London & South East UK",
        "subtitle": "Equip your padel venue in London with the leading court recording technology: instant net push button replays, 1080p YouTube tournament streaming, and zero civil works.",
        "hero_img": "assets/images/savemyplay-1.jpg",
        "hero_img_alt": "Smart AI padel court recording cameras in London",
        "wa_msg": "Hello Javier, we manage a padel club in London/UK and want information on Save My Play court cameras",
        "price_anchor": "Hardware €180 / court · Software from €45/mo · No lock-in",
        "target_audience": "Padel venue managers, racquets clubs, and leisure operators in Greater London, Surrey, Hertfordshire, and South East UK.",
        "quick_summary": {
            "label_1": "Hardware Cost", "val_1": "€180 one-time per court (owned)",
            "label_2": "Monthly Software", "val_2": "From €45/month/court · Cancel anytime",
            "label_3": "Installation", "val_3": "5-minute post clamp · Zero trenching",
            "label_4": "Replays", "val_4": "Net button + Instant QR download",
            "p": "Turnkey smart court recording for clubs in London. Broadcast your club matches to YouTube Live and allow players to download 25-second highlights in seconds."
        },
        "benefits": [
            ("Zero Civil Works & Fast 5-Min Setup", "No conduit piping or ground trenching required. Mounts securely onto the court post in 5 minutes."),
            ("Players Love the Net Push Button", "Tap the net band button after a memorable rally. A 25-second Full HD highlight clip is ready via QR scan."),
            ("1080p YouTube Live Streaming", "Broadcast UK tournaments, LTA circuits, and club championships straight to YouTube with custom sponsor watermarks.")
        ],
        "faqs": [
            ("Do players need to download an app?", "No. Players scan the court QR code with their smartphone camera. The video opens instantly in their browser with zero registration hassle."),
            ("How long does shipping to the UK take?", "Hardware ships directly to the UK within 3-5 business days pre-configured and ready to plug in."),
            ("Is there a multi-year lock-in contract?", "No! You own your cameras (€180) and software is month-to-month with total freedom to pause or cancel.")
        ]
    },
    {
        "lang": "en",
        "slug": "padel-court-cameras-miami",
        "geo_region": "US-FL",
        "geo_placename": "Miami, Florida, USA",
        "geo_position": "25.7617;-80.1918",
        "title": "Padel Court Cameras in Miami & Florida [From $49/mo] | Save My Play",
        "meta_desc": "Official USTA & USA Padel court cameras in Miami & South Florida (Wynwood, Brickell, Coral Gables). Zero civil works, instant QR highlights, and no long contracts.",
        "badge": "MIAMI & FLORIDA · USA PADEL OFFICIAL",
        "breadcrumb_leaf": "Miami Courts",
        "h1": "AI Padel Court Recording Cameras in Miami & South Florida",
        "subtitle": "The smart recording system powering premier clubs across Miami and the US: instant net button replays, 1080p live streaming, and rectilinear optics engineered in California & Chicago.",
        "hero_img": "assets/images/savemyplay-2.jpg",
        "hero_img_alt": "Padel court recording cameras in Miami and South Florida",
        "wa_msg": "Hello Javier, we run a padel venue in Miami/Florida and want a demo of the Save My Play court camera system",
        "price_anchor": "Hardware $199 / court · Software from $49/mo · Fast US shipping",
        "target_audience": "Padel club owners, real estate developers, and hospitality resorts in Miami, Fort Lauderdale, Palm Beach, and across Florida.",
        "quick_summary": {
            "label_1": "US Accreditation", "val_1": "Official camera of USTA & USA Padel",
            "label_2": "Hardware Ownership", "val_2": "$199 one-time per court",
            "label_3": "Monthly Plan", "val_3": "From $49/mo · Month-to-month",
            "label_4": "Installation", "val_4": "5-minute post mounting without works",
            "p": "Engineered for high-volume American padel clubs. Instant social media sharing on Instagram & TikTok directly from courtside QR codes."
        },
        "benefits": [
            ("Official USA Padel & USTA Camera", "Trusted by over 1,500 active courts across the United States and Europe."),
            ("Rectilinear American Sports Optics", "Designed specifically for fast ball sports without fish-eye distortion, ensuring crisp line-to-net clarity."),
            ("Zero Contract Lock-in", "Avoid restrictive multi-year equipment leases. You own the hardware and maintain 100% venue independence.")
        ],
        "faqs": [
            ("Does it withstand Florida heat and humidity?", "Yes. The sealed IP casing is weather-resistant and engineered for direct sunlight and high tropical humidity."),
            ("Can we monetize court recordings?", "Yes! Clubs charge an add-on booking fee or attract local sponsors whose logos appear automatically on all player videos."),
            ("How do players get their videos?", "They tap the net button after great points and scan the post QR code with their phone camera to download clips instantly.")
        ]
    },

    # ========================== FR (France) ==========================
    {
        "lang": "fr",
        "slug": "cameras-padel-paris",
        "geo_region": "FR-IDF",
        "geo_placename": "Paris, Île-de-France",
        "geo_position": "48.8566;2.3522",
        "title": "Caméras Terrains Padel Paris & Île-de-France [Dès 45€/mois] | Save My Play",
        "meta_desc": "Caméras intelligentes Save my Play à Paris et en Île-de-France. Bouton au filet, téléchargement QR instantané et diffusion YouTube sans aucuns travaux.",
        "badge": "PARIS & ÎLE-DE-FRANCE · SAVE MY PLAY",
        "breadcrumb_leaf": "Terrains Paris",
        "h1": "Caméras Intelligentes pour Terrains de Padel à Paris & Région Parisienne",
        "subtitle": "La solution d'enregistrement vidéo de référence pour les complexes sportifs parisiens : bouton poussoir sans fil au filet, téléchargement de clips par QR code et zéro engagement.",
        "hero_img": "assets/images/savemyplay-1.jpg",
        "hero_img_alt": "Caméras Save my Play pour terrains de padel à Paris",
        "wa_msg": "Bonjour Javier, nous gérons un club de padel à Paris / Île-de-France et souhaitons des informations sur Save My Play",
        "price_anchor": "Matériel 180 € / piste · Logiciel dès 45 €/mois · Zéro engagement",
        "target_audience": "Gérants de clubs de padel, complexes municipaux et structures privées à Paris, Boulogne, Saint-Denis, Versailles et en Île-de-France.",
        "quick_summary": {
            "label_1": "Matériel Piste", "val_1": "180 € en pleine propriété par piste",
            "label_2": "Abonnement", "val_2": "Dès 45 € / mois · Résiliation libre",
            "label_3": "Installation", "val_3": "Fixation au poteau en 5 min sans saignée",
            "label_4": "Téléchargement", "val_4": "Scan QR immédiat sans application",
            "p": "Système de captation vidéo autonome pour clubs de padel franciliens. Replays instantanés de 25 secondes et streaming 1080p pour vos tournois P100, P250 ou P500."
        },
        "benefits": [
            ("Pose Rapide en 5 Minutes Sans Travaux", "Aucune tranchée ni câble au sol. Se fixe directement sur le poteau de la piste."),
            ("Les Joueurs Adorent le Bouton au Filet", "Après un point d'anthologie, les joueurs cliquent sur le bouton du filet. Le clip est prêt par scan QR en 25 secondes."),
            ("Diffusion YouTube Live en 1080p", "Retransmettez vos tournois officiels FFT directement sur YouTube avec le logo de vos sponsors.")
        ],
        "faqs": [
            ("Les joueurs doivent-ils installer une application ?", "Non. Le joueur scanne le QR code avec l'appareil photo de son smartphone et la vidéo s'ouvre directement dans son navigateur web."),
            ("Combien de temps prend la livraison en France ?", "Expédition sous 48 heures préconfigurée, prête à brancher."),
            ("Y a-t-il un engagement sur plusieurs années ?", "Non ! Vous êtes propriétaire du matériel (180 €) et l'abonnement mensuel (45 €/mois) est sans engagement.")
        ]
    },
    {
        "lang": "fr",
        "slug": "cameras-padel-lyon",
        "geo_region": "FR-ARA",
        "geo_placename": "Lyon, Auvergne-Rhône-Alpes",
        "geo_position": "45.7640;4.8357",
        "title": "Caméras Pistes Padel Lyon & Rhône-Alpes [45€/mois] | Save My Play",
        "meta_desc": "Caméras Save my Play à Lyon et en Rhône-Alpes. Installation en 5 minutes sans travaux, bouton au filet et vidéos par QR code pour complexes de padel.",
        "badge": "LYON & RHÔNE-ALPES · SAVE MY PLAY",
        "breadcrumb_leaf": "Terrains Lyon",
        "h1": "Caméras et Enregistrement Vidéo de Padel à Lyon et Région Rhône-Alpes",
        "subtitle": "Équipez votre club de padel à Lyon avec la technologie en piste américaine : bouton poussoir au filet, replays instantanés et retransmission de tournois sans travaux.",
        "hero_img": "assets/images/savemyplay-3.jpg",
        "hero_img_alt": "Caméras pour pistes de padel à Lyon et Rhône-Alpes",
        "wa_msg": "Bonjour Javier, nous avons un club de padel à Lyon/Rhône-Alpes et souhaitons un devis pour les caméras Save My Play",
        "price_anchor": "Matériel 180 € / piste · Abonnement 45 €/mois · 0 travaux",
        "target_audience": "Responsables de clubs de padel à Lyon, Villeurbanne, Saint-Étienne, Grenoble, Annecy et dans toute la région Rhône-Alpes.",
        "quick_summary": {
            "label_1": "Investissement", "val_1": "180 € par piste (matériel en propriété)",
            "label_2": "Logiciel", "val_2": "Dès 45 € / mois · Sans engagement",
            "label_3": "Outils Coachs", "val_3": "Ralenti et analyse tactique sur tablette",
            "label_4": "Installation", "val_4": "5 minutes chrono par terrain",
            "p": "Solution d'enregistrement vidéo fluide et autonome pour les centres sportifs indoor et outdoor de la région lyonnaise."
        },
        "benefits": [
            ("Optique Haute Précision Rectiligne", "Conçue aux États-Unis pour les sports de balle rapides, sans distorsion fish-eye."),
            ("Outil Idéal pour les Enseignants et Cours", "Permet aux moniteurs de revoir les séquences de jeu au ralenti sur tablette pendant les entraînements."),
            ("Engagement Zéro Contrainte", "Vous restez maître de vos installations sans contrat de leasing étouffant sur 5 ans.")
        ],
        "faqs": [
            ("Est-ce compatible avec les logiciels de réservation comme Playtomic ?", "Totalement. Le système fonctionne en autonomie complète sur le court, sans aucune interférence avec vos réservations."),
            ("Quel débit internet est nécessaire ?", "Une connexion Wi-Fi ou 4G/5G avec 5 à 10 Mbps d'upload par terrain suffit pour le Full HD."),
            ("Comment les vidéos sont-elles stockées ?", "Les clips sont traités dans le cloud sécurisé et accessibles immédiatement par simple lien QR.")
        ]
    },

    # ========================== IT (Italia) ==========================
    {
        "lang": "it",
        "slug": "telecamere-padel-roma",
        "geo_region": "IT-62",
        "geo_placename": "Roma, Lazio, Italia",
        "geo_position": "41.9028;12.4964",
        "title": "Telecamere Campi Padel Roma [0 Opere Murarie · 45€/mese] | Save My Play",
        "meta_desc": "Telecamere intelligenti Save my Play a Roma e nel Lazio (+1.500 campi). Pulsante a rete, video istantanei con QR e streaming YouTube senza vincoli.",
        "badge": "ROMA & LAZIO · SAVE MY PLAY",
        "breadcrumb_leaf": "Campi Roma",
        "h1": "Telecamere Intelligenti per Campi da Padel a Roma e nel Lazio",
        "subtitle": "Porta nel tuo circolo di padel a Roma la tecnologia di registrazione leader: pulsante senza fili a rete per replay immediati, download via QR code e zero vincoli pluriennali.",
        "hero_img": "assets/images/savemyplay-1.jpg",
        "hero_img_alt": "Telecamere Save my Play per campi da padel a Roma",
        "wa_msg": "Ciao Javier, gestiamo un circolo di padel a Roma e vorremmo informazioni e demo di Save My Play",
        "price_anchor": "Hardware 180 € / campo · Software 45 €/mese · Zero vincoli",
        "target_audience": "Gestori di circoli di padel, complessi sportivi e maestri a Roma, Fiumicino, Tivoli, Latina e in tutto il Lazio.",
        "quick_summary": {
            "label_1": "Hardware Campo", "val_1": "180 € di proprietà per campo",
            "label_2": "Canone Software", "val_2": "45 € / mese per campo · Disdetta libera",
            "label_3": "Opere Murarie", "val_3": "0 opere civili · Montaggio in 5 min",
            "label_4": "Download", "val_4": "Scan QR istantaneo senza app",
            "p": "Installazione rapida di telecamere sportive Save My Play per circoli di padel a Roma. Riprese Full HD senza effetto fish-eye e streaming in diretta per tornei."
        },
        "benefits": [
            ("Montaggio in 5 Minuti Senza Lavori", "Nessuna traccia né canalina sul campo. Si fissa saldamente direttamente al palo della recinzione."),
            ("I Giocatori Amano il Pulsante a Rete", "Dopo un punto spettacolare, i giocatori premono il pulsante a rete e ricevono il video in 25 secondi scansionando il QR."),
            ("Streaming YouTube Live Full HD", "Trasmetti le finali dei tornei sociali e delle gare federali FITP direttamente sul canale YouTube del circolo.")
        ],
        "faqs": [
            ("I giocatori devono registrarsi o scaricare un'app?", "No. I giocatori inquadrano il QR code con la fotocamera dello smartphone e il video si apre subito nel browser."),
            ("Quanto tempo richiede la spedizione in Italia?", "Spedizione in 48 ore pre-configurata e pronta per l'alimentazione 220V."),
            ("C'è un contratto vincolante per più anni?", "No! Sei proprietario delle telecamere (180 €) e l'abbonamento software (45 €/mese) è mensile senza penali.")
        ]
    },
    {
        "lang": "it",
        "slug": "telecamere-padel-milano",
        "geo_region": "IT-25",
        "geo_placename": "Milano, Lombardia, Italia",
        "geo_position": "45.4642;9.1900",
        "title": "Telecamere Campi Padel Milano & Lombardia [45€/mese] | Save My Play",
        "meta_desc": "Telecamere Save my Play per campi da padel a Milano, Monza e Lombardia. Registrazione partite in 5 min senza scavi, replay con QR e disdetta libera.",
        "badge": "MILANO & LOMBARDIA · SAVE MY PLAY",
        "breadcrumb_leaf": "Campi Milano",
        "h1": "Telecamere e Registrazione Partite di Padel a Milano e Lombardia",
        "subtitle": "La soluzione video più innovativa per circoli indoor e outdoor a Milano: replay istantanei su smartphone, analisi tattica per lezioni e zero permanenza.",
        "hero_img": "assets/images/savemyplay-2.jpg",
        "hero_img_alt": "Telecamere per campi da padel a Milano Save my Play",
        "wa_msg": "Ciao Javier, abbiamo un circolo di padel a Milano/Lombardia e vorremmo un preventivo per le telecamere Save My Play",
        "price_anchor": "Hardware 180 € / campo · Software 45 €/mese · Ottica sportiva",
        "target_audience": "Titolari di circoli di padel a Milano, Monza, Bergamo, Brescia, Como e Varese.",
        "quick_summary": {
            "label_1": "Hardware", "val_1": "180 € a campo (hardware tuo)",
            "label_2": "Software", "val_2": "45 € / mese · Nessun vincolo",
            "label_3": "Analisi Maestri", "val_3": "Replay rallentatore per lezioni",
            "label_4": "Installazione", "val_4": "5 minuti per campo",
            "p": "Telecamere con ottica rettilinea senza fish-eye per circoli ad alta rotazione a Milano e Lombardia."
        },
        "benefits": [
            ("Ottica Rettilinea Americana ad Alta Definizione", "Nessuna distorsione da telecamera di sicurezza: linee di campo perfettamente dritte da fondo campo alla rete."),
            ("Monetizzazione Diretta per il Circolo", "Aumenta la fedeltà dei giocatori e attira sponsor locali con loghi sovrimpressi sui video."),
            ("Totale Libertà Contrattuale", "Non resti vincolato a contratti quinquennali. L'hardware è tuo e gestisci il circolo con piena indipendenza.")
        ],
        "faqs": [
            ("Funziona con i sistemi di prenotazione come Playtomic?", "Sì, funziona in completa autonomia sul campo senza toccare le prenotazioni."),
            ("I maestri possono usarlo durante le lezioni?", "Certamente, i video e i replay al rallentatore possono essere visualizzati immediatamente su tablet."),
            ("Come si riceve l'assistenza?", "Forniamo assistenza diretta e supporto continuo via WhatsApp.")
        ]
    }
]


def render_local_landing(l):
    lang = l["lang"]
    slug = l["slug"]

    if lang == "es":
        page_url = f"{DOMAIN}/{slug}/"
        path_prefix = ""
        asset_prefix = "../"
    else:
        page_url = f"{DOMAIN}/{lang}/{slug}/"
        path_prefix = f"{lang}/"
        asset_prefix = "../../"

    # Breadcrumb label
    home_name = "Inicio" if lang == "es" else ("Home" if lang in ["en", "it"] else "Accueil")
    camaras_name = "Cámaras" if lang == "es" else ("Cameras" if lang == "en" else ("Caméras" if lang == "fr" else "Telecamere"))
    camaras_url = f"{DOMAIN}/{path_prefix}camaras/" if lang == "es" else f"{DOMAIN}/save-my-play/"

    # FAQ HTML
    faq_html = ""
    faq_schema_items = []
    for q, a in l["faqs"]:
        faq_html += f"""
        <details class="group bg-white rounded-2xl p-4 sm:p-5 border border-slate-200/90 shadow-2xs transition hover:border-[#f2920b]">
          <summary class="flex items-center justify-between font-heading font-black text-sm sm:text-base text-slate-950 cursor-pointer list-none select-none">
            <span>{q}</span>
            <span class="w-6 h-6 rounded-full bg-slate-100 text-slate-700 group-open:rotate-180 group-open:bg-[#f2920b] group-open:text-slate-950 flex items-center justify-center transition-transform text-xs shrink-0 ml-3">▼</span>
          </summary>
          <p class="mt-3 text-slate-600 text-xs sm:text-sm leading-relaxed border-t border-slate-100 pt-3">{a}</p>
        </details>"""
        faq_schema_items.append(f"""{{
          "@type": "Question",
          "name": "{q}",
          "acceptedAnswer": {{
            "@type": "Answer",
            "text": "{a}"
          }}
        }}""")

    faqs_schema_json = ",\n        ".join(faq_schema_items)

    # Benefits HTML
    benefits_html = ""
    for b_title, b_desc in l["benefits"]:
        benefits_html += f"""
        <div class="bg-white rounded-3xl p-6 sm:p-8 border border-slate-200/90 shadow-xl transition hover:border-[#f2920b] space-y-3">
          <div class="w-10 h-10 rounded-2xl bg-amber-500/10 flex items-center justify-center text-[#f2920b]">
            <i data-lucide="check" class="w-5 h-5"></i>
          </div>
          <h3 class="text-base sm:text-lg font-black font-heading text-slate-950">{b_title}</h3>
          <p class="text-xs sm:text-sm text-slate-600 leading-relaxed">{b_desc}</p>
        </div>"""

    # Schema JSON-LD
    schema_json = f"""{{
    "@context": "https://schema.org",
    "@graph": [
      {{
        "@type": "ImageObject",
        "@id": "{page_url}#primaryimage",
        "url": "{DOMAIN}/{l['hero_img']}",
        "contentUrl": "{DOMAIN}/{l['hero_img']}",
        "width": 1000,
        "height": 1000,
        "caption": "{l['hero_img_alt']}",
        "representativeOfPage": true,
        "creator": {{
          "@type": "Organization",
          "name": "CoolPadel"
        }}
      }},
      {{
        "@type": "Organization",
        "@id": "https://coolpadelstudios.com/#organization",
        "name": "CoolPadel",
        "alternateName": "CoolPadel",
        "url": "https://coolpadelstudios.com",
        "logo": "https://coolpadelstudios.com/assets/images/coolpadel-mascot-hd.png",
        "sameAs": [
          "https://www.instagram.com/coolpadel_/",
          "https://www.linkedin.com/in/javier-villoria-soleto-606737298/",
          "https://maps.google.com/?cid=5000443597205028051"
        ]
      }},
      {{
        "@type": "BreadcrumbList",
        "@id": "{page_url}#breadcrumb",
        "itemListElement": [
          {{
            "@type": "ListItem",
            "position": 1,
            "name": "{home_name}",
            "item": "{DOMAIN}/{path_prefix}"
          }},
          {{
            "@type": "ListItem",
            "position": 2,
            "name": "{camaras_name}",
            "item": "{camaras_url}"
          }},
          {{
            "@type": "ListItem",
            "position": 3,
            "name": "{l['breadcrumb_leaf']}",
            "item": "{page_url}"
          }}
        ]
      }},
      {{
        "@type": "FAQPage",
        "@id": "{page_url}#faq",
        "mainEntity": [
          {faqs_schema_json}
        ]
      }},
      {{
        "@type": "Product",
        "name": "{l['h1']} - Save my Play",
        "description": "{l['meta_desc']}",
        "image": "{DOMAIN}/{l['hero_img']}",
        "sku": "SMP-COURT-SYSTEM-{slug.upper()[:12]}",
        "brand": {{
          "@type": "Brand",
          "name": "Save my Play"
        }},
        "offers": [
          {{
            "@type": "Offer",
            "name": "Hardware Unit",
            "priceCurrency": "EUR",
            "price": "180.00",
            "priceValidUntil": "2027-12-31",
            "availability": "https://schema.org/InStock",
            "hasMerchantReturnPolicy": {{
              "@type": "MerchantReturnPolicy",
              "applicableCountry": "ES",
              "returnPolicyCategory": "https://schema.org/MerchantReturnFiniteReturnWindow",
              "merchantReturnDays": 14,
              "returnMethod": "https://schema.org/ReturnByMail",
              "returnFees": "https://schema.org/FreeReturn",
              "merchantReturnLink": "https://coolpadelstudios.com/politica-de-devoluciones.html"
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
              }}
            }}
          }},
          {{
            "@type": "Offer",
            "name": "Monthly Software Subscription",
            "priceCurrency": "EUR",
            "price": "45.00",
            "priceValidUntil": "2027-12-31",
            "availability": "https://schema.org/InStock"
          }}
        ]
      }}
    ]
  }}"""

    # Button label
    btn_wa_text = "Solicitar información por WhatsApp" if lang == "es" else ("Request Info on WhatsApp" if lang == "en" else ("Demander des infos sur WhatsApp" if lang == "fr" else "Richiedi informazioni su WhatsApp"))
    btn_demo_text = "Ver Demo Online" if lang == "es" else ("Watch Online Demo" if lang == "en" else ("Voir la démo en ligne" if lang == "fr" else "Guarda la demo online"))

    html = f"""<!DOCTYPE html>
<html lang="{lang}" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
  <title>{l['title']}</title>
  <meta name="description" content="{l['meta_desc']}">
  <meta name="author" content="CoolPadel">
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">
  <link rel="canonical" href="{page_url}">

  <meta name="language" content="{lang}">
  <link rel="icon" type="image/png" href="{asset_prefix}assets/images/favicon_transparente.png?v=transp3">
  <link rel="apple-touch-icon" sizes="180x180" href="{asset_prefix}assets/images/favicon_transparente.png?v=transp3">
  <meta name="theme-color" content="#0b1626">

  <!-- Resource Hints & Core Web Vitals -->
  <link rel="dns-prefetch" href="https://fonts.googleapis.com">
  <link rel="dns-prefetch" href="https://fonts.gstatic.com">
  <link rel="dns-prefetch" href="https://cdn.tailwindcss.com">
  <link rel="dns-prefetch" href="https://unpkg.com">

  <!-- GEO Tags Nativas de Ciudad -->
  <meta name="geo.region" content="{l['geo_region']}">
  <meta name="geo.placename" content="{l['geo_placename']}">
  <meta name="geo.position" content="{l['geo_position']}">
  <meta name="ICBM" content="{l['geo_position'].replace(';', ', ')}">

  <!-- Open Graph -->
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="CoolPadel">
  <meta property="og:url" content="{page_url}">
  <meta property="og:title" content="{l['title']}">
  <meta property="og:description" content="{l['meta_desc']}">
  <meta property="og:image" content="{DOMAIN}/{l['hero_img']}">
  <meta property="og:image:width" content="1000">
  <meta property="og:image:height" content="1000">

  <!-- Twitter Cards -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{l['title']}">
  <meta name="twitter:description" content="{l['meta_desc']}">
  <meta name="twitter:image" content="{DOMAIN}/{l['hero_img']}">

  <!-- Schema.org JSON-LD -->
  <script type="application/ld+json">
  {schema_json}
  </script>

  <!-- Google Fonts: Inter & Outfit -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Outfit:wght@600;700;800;900&display=swap" rel="stylesheet">

  <script src="https://cdn.tailwindcss.com"></script>
  <script src="https://unpkg.com/lucide@latest"></script>

  <style>
    body {{ font-family: 'Inter', sans-serif; }}
    .font-heading {{ font-family: 'Outfit', sans-serif; }}
  </style>
</head>
<body class="bg-slate-50 text-slate-900 antialiased selection:bg-[#f2920b] selection:text-slate-950 flex flex-col min-h-screen">

  <!-- Header Flotante -->
  <header class="sticky top-0 z-40 bg-white/95 backdrop-blur-md border-b border-slate-200/90 shadow-2xs">
    <div class="max-w-6xl mx-auto px-4 sm:px-6 h-16 flex items-center justify-between">
      <a href="{DOMAIN}/{path_prefix}" class="flex items-center gap-2.5 group">
        <img src="{asset_prefix}assets/images/coolpadel-mascot-hd.png" alt="CoolPadel Logo" width="34" height="34" class="w-8 h-8 object-contain">
        <span class="font-heading font-black text-lg text-slate-950 tracking-tight">Cool<span class="text-[#f2920b]">Padel</span></span>
      </a>
      <div class="flex items-center gap-3">
        <a href="https://wa.me/34680317486?text={urllib.parse.quote(l['wa_msg'])}" target="_blank" rel="noopener noreferrer" class="inline-flex items-center gap-2 px-4 py-2 rounded-xl bg-[#25D366] hover:bg-[#20ba59] text-white text-xs sm:text-sm font-bold shadow-sm transition">
          <i data-lucide="message-circle" class="w-4 h-4"></i>
          <span>WhatsApp</span>
        </a>
      </div>
    </div>
  </header>

  <!-- Breadcrumb Visual -->
  <div class="bg-slate-100 border-b border-slate-200/80 text-xs py-2.5 px-4 sm:px-6">
    <div class="max-w-6xl mx-auto flex items-center gap-2 text-slate-500 overflow-x-auto whitespace-nowrap">
      <a href="{DOMAIN}/{path_prefix}" class="hover:text-slate-950 transition font-medium">{home_name}</a>
      <span>›</span>
      <a href="{camaras_url}" class="hover:text-slate-950 transition font-medium">{camaras_name}</a>
      <span>›</span>
      <span class="text-slate-900 font-bold">{l['breadcrumb_leaf']}</span>
    </div>
  </div>

  <!-- Hero Section -->
  <main class="flex-grow">
    <section class="relative bg-gradient-to-b from-[#0b1626] to-[#08101a] text-white py-14 sm:py-20 px-4 sm:px-6 overflow-hidden">
      <div class="max-w-6xl mx-auto grid grid-cols-1 lg:grid-cols-12 gap-10 items-center">
        <div class="lg:col-span-7 space-y-6">
          <div class="inline-flex items-center gap-2 px-3.5 py-1 rounded-full bg-white/10 border border-white/20 text-[#f2920b] text-xs font-black tracking-wide uppercase">
            <i data-lucide="map-pin" class="w-3.5 h-3.5"></i>
            <span>{l['badge']}</span>
          </div>
          <h1 class="text-2xl sm:text-4xl lg:text-5xl font-black font-heading tracking-tight leading-tight">
            {l['h1']}
          </h1>
          <p class="text-sm sm:text-base text-slate-300 leading-relaxed">
            {l['subtitle']}
          </p>
          <div class="inline-flex items-center gap-2 px-4 py-2 rounded-2xl bg-amber-500/10 border border-[#f2920b]/30 text-[#f2920b] font-bold text-xs sm:text-sm">
            <i data-lucide="tag" class="w-4 h-4"></i>
            <span>{l['price_anchor']}</span>
          </div>
          <div class="flex flex-wrap gap-3 pt-2">
            <a href="https://wa.me/34680317486?text={urllib.parse.quote(l['wa_msg'])}" target="_blank" rel="noopener noreferrer" class="inline-flex items-center gap-2 px-6 py-3.5 rounded-2xl bg-[#f2920b] hover:bg-[#d98006] text-slate-950 font-black font-heading text-sm shadow-lg shadow-amber-500/20 transition hover:scale-105">
              <i data-lucide="message-circle" class="w-4 h-4"></i>
              <span>{btn_wa_text}</span>
            </a>
            <a href="{camaras_url}" class="inline-flex items-center gap-2 px-6 py-3.5 rounded-2xl bg-white/10 hover:bg-white/20 text-white font-bold text-sm border border-white/20 transition">
              <i data-lucide="play" class="w-4 h-4"></i>
              <span>{btn_demo_text}</span>
            </a>
          </div>
        </div>
        <div class="lg:col-span-5">
          <div class="relative rounded-3xl overflow-hidden border border-white/15 shadow-2xl bg-slate-900/50">
            <img src="{asset_prefix}{l['hero_img']}" alt="{l['hero_img_alt']}" width="600" height="400" class="w-full h-auto object-cover hover:scale-105 transition-transform duration-500">
            <div class="absolute inset-0 bg-gradient-to-t from-slate-950/80 via-transparent to-transparent flex items-end p-6">
              <p class="text-xs font-semibold text-slate-300">Save my Play · Chicago & California Tech</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Resumen Clave -->
    <section class="max-w-6xl mx-auto px-4 sm:px-6 -mt-8 relative z-20">
      <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
        <div class="bg-white rounded-2xl p-4 sm:p-5 border border-slate-200/90 shadow-md">
          <span class="text-[11px] font-bold text-slate-500 uppercase tracking-wider block">{l['quick_summary']['label_1']}</span>
          <span class="text-sm sm:text-base font-black font-heading text-slate-950 mt-1 block">{l['quick_summary']['val_1']}</span>
        </div>
        <div class="bg-white rounded-2xl p-4 sm:p-5 border border-slate-200/90 shadow-md">
          <span class="text-[11px] font-bold text-slate-500 uppercase tracking-wider block">{l['quick_summary']['label_2']}</span>
          <span class="text-sm sm:text-base font-black font-heading text-slate-950 mt-1 block">{l['quick_summary']['val_2']}</span>
        </div>
        <div class="bg-white rounded-2xl p-4 sm:p-5 border border-slate-200/90 shadow-md">
          <span class="text-[11px] font-bold text-slate-500 uppercase tracking-wider block">{l['quick_summary']['label_3']}</span>
          <span class="text-sm sm:text-base font-black font-heading text-slate-950 mt-1 block">{l['quick_summary']['val_3']}</span>
        </div>
        <div class="bg-white rounded-2xl p-4 sm:p-5 border border-slate-200/90 shadow-md">
          <span class="text-[11px] font-bold text-slate-500 uppercase tracking-wider block">{l['quick_summary']['label_4']}</span>
          <span class="text-sm sm:text-base font-black font-heading text-slate-950 mt-1 block">{l['quick_summary']['val_4']}</span>
        </div>
      </div>
    </section>

    <!-- Beneficios -->
    <section class="py-14 sm:py-20 px-4 sm:px-6 max-w-6xl mx-auto">
      <div class="text-center max-w-2xl mx-auto mb-10 space-y-2">
        <h2 class="text-xl sm:text-3xl font-black font-heading text-slate-950 uppercase tracking-tight">
          Ventajas para tu Club
        </h2>
        <p class="text-xs sm:text-sm text-slate-500">
          La tecnología que llena horas valle y fideliza a tus jugadores.
        </p>
      </div>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
        {benefits_html}
      </div>
    </section>

    <!-- FAQs -->
    <section class="py-12 px-4 sm:px-6 max-w-4xl mx-auto">
      <div class="text-center max-w-2xl mx-auto mb-8 space-y-2">
        <h2 class="text-xl sm:text-3xl font-black font-heading text-slate-950 uppercase tracking-tight">
          Preguntas Frecuentes
        </h2>
        <p class="text-xs sm:text-sm text-slate-500">
          Respuestas directas sobre la instalación y el funcionamiento del sistema.
        </p>
      </div>
      <div class="space-y-3">
        {faq_html}
      </div>
    </section>
  </main>

  <!-- Footer Oficial -->
  <footer class="bg-[#0b1626] text-white py-12 px-4 sm:px-6 border-t border-slate-800 text-xs mt-16">
    <div class="max-w-6xl mx-auto space-y-8">
      <div class="flex flex-col sm:flex-row items-center justify-between gap-4 border-b border-white/10 pb-6">
        <a href="{DOMAIN}/{path_prefix}" class="flex items-center gap-2">
          <img src="{asset_prefix}assets/images/coolpadel-mascot-hd.png" alt="CoolPadel" width="28" height="28" class="w-7 h-7 object-contain">
          <span class="font-heading font-black text-base text-white">Cool<span class="text-[#f2920b]">Padel</span> Studios</span>
        </a>
        <p class="text-slate-400">Madrid · Javier Villoria Soleto · WhatsApp: +34 680 31 74 86</p>
      </div>
      <div class="text-center text-slate-500 text-[11px]">
        © 2026 CoolPadel Studios · Distribuidor Partner Oficial Save my Play. Todos los derechos reservados.
      </div>
    </div>
  </footer>

  <script>
    if (typeof lucide !== 'undefined') {{
      lucide.createIcons();
    }}
  </script>
</body>
</html>
"""
    return html


def build_all_local_landings():
    print(">> Generando Landings Geo-Locales Nativas por Idioma...")
    generated_urls = []
    for l in LOCAL_LANDINGS:
        lang = l["lang"]
        slug = l["slug"]

        if lang == "es":
            out_dir = f"coolpadel-web/{slug}"
            page_path = f"/{slug}/"
        else:
            out_dir = f"coolpadel-web/{lang}/{slug}"
            page_path = f"/{lang}/{slug}/"

        os.makedirs(out_dir, exist_ok=True)
        html_content = render_local_landing(l)
        with open(f"{out_dir}/index.html", "w", encoding="utf-8") as f:
            f.write(html_content)

        generated_urls.append(page_path)
        print(f"  [OK] {lang.upper()} -> {page_path}")

    return generated_urls


if __name__ == "__main__":
    urls = build_all_local_landings()
    print(f">> Total landings geo-locales nativas generadas: {len(urls)}")
