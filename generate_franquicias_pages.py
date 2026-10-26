#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generador de Páginas Individuales para cada Franquicia y Cadena de Pádel.
Genera versiones 100% nativas y localizadas en 4 idiomas (ES, EN, FR, IT)
para eliminar cualquier sospecha de contenido duplicado ante Googlebot.
"""

import os
import sys
import json
import html
import urllib.parse

if sys.platform == "win32" and hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

# Importar dataset
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from dataset_franquicias import FRANQUICIAS

COUNTRY_NAMES = {
    "Alemania": {"en": "Germany", "fr": "Allemagne", "it": "Germania"},
    "Arabia Saudí": {"en": "Saudi Arabia", "fr": "Arabie Saoudite", "it": "Arabia Saudita"},
    "Argentina": {"en": "Argentina", "fr": "Argentine", "it": "Argentina"},
    "Australia": {"en": "Australia", "fr": "Australie", "it": "Australia"},
    "Austria": {"en": "Austria", "fr": "Autriche", "it": "Austria"},
    "Brasil": {"en": "Brazil", "fr": "Brésil", "it": "Brasile"},
    "Bélgica": {"en": "Belgium", "fr": "Belgique", "it": "Belgio"},
    "Catar": {"en": "Qatar", "fr": "Qatar", "it": "Qatar"},
    "Chile": {"en": "Chile", "fr": "Chili", "it": "Cile"},
    "Dinamarca": {"en": "Denmark", "fr": "Danemark", "it": "Danimarca"},
    "Emiratos Árabes": {"en": "United Arab Emirates", "fr": "Émirats Arabes Unis", "it": "Emirati Arabi Uniti"},
    "España": {"en": "Spain", "fr": "Espagne", "it": "Spagna"},
    "Estados Unidos": {"en": "United States", "fr": "États-Unis", "it": "Stati Uniti"},
    "Finlandia": {"en": "Finland", "fr": "Finlande", "it": "Finlandia"},
    "Francia": {"en": "France", "fr": "France", "it": "Francia"},
    "Irlanda": {"en": "Ireland", "fr": "Irlande", "it": "Irlanda"},
    "Italia": {"en": "Italy", "fr": "Italie", "it": "Italia"},
    "Kuwait": {"en": "Kuwait", "fr": "Koweït", "it": "Kuwait"},
    "México": {"en": "Mexico", "fr": "Mexique", "it": "Messico"},
    "Noruega": {"en": "Norway", "fr": "Norvège", "it": "Norvegia"},
    "Países Bajos": {"en": "Netherlands", "fr": "Pays-Bas", "it": "Paesi Bassi"},
    "Portugal": {"en": "Portugal", "fr": "Portugal", "it": "Portogallo"},
    "Reino Unido": {"en": "United Kingdom", "fr": "Royaume-Uni", "it": "Regno Unito"},
    "Sudáfrica": {"en": "South Africa", "fr": "Afrique du Sud", "it": "Sudafrica"},
    "Suecia": {"en": "Sweden", "fr": "Suède", "it": "Svezia"},
    "Suiza": {"en": "Switzerland", "fr": "Suisse", "it": "Svizzera"},
}

MODELO_NAMES = {
    "Cadena Multiclub": {"en": "Multi-club Network", "fr": "Chaîne Multiclub", "it": "Catena Multiclub"},
    "Franquicia": {"en": "Padel Franchise", "fr": "Franchise de Padel", "it": "Franchigia Padel"},
    "Franquicia Padel": {"en": "Padel Franchise", "fr": "Franchise de Padel", "it": "Franchigia Padel"},
    "Operador Global": {"en": "Global Operator", "fr": "Opérateur Global", "it": "Operatore Globale"},
    "Club Independiente": {"en": "Independent Club", "fr": "Club Indépendant", "it": "Club Indipendente"},
}

I18N = {
    "es": {
        "nav_llaveros": "LLAVEROS",
        "nav_camaras": "CÁMARAS",
        "nav_blog": "Blog",
        "nav_cadenas": "Cadenas de clubs",
        "nav_contacto": "Contactar",
        "bc_home": "Inicio",
        "bc_dir": "Franquicias Pádel",
        "bc_dir_schema": "Directorio de Franquicias de Pádel",
        "btn_back_dir": "Volver al Directorio Completo",
        "hq_label": "Sede Principal",
        "founders_label": "Promotores",
        "metric_clubs": "Clubes / Sedes",
        "metric_courts": "Pistas Totales",
        "metric_software": "Software",
        "metric_inv": "Inversión Media",
        "btn_inquire": "Consultar Equipamiento para {nombre}",
        "btn_official_web": "Web Oficial",
        "sedes_title": "Sedes y Complejos de Referencia",
        "sedes_audit": "Datos auditados en censo continuo 2026",
        "sedes_view_map": "Ver mapa global →",
        "sedes_facilities_in": "Instalaciones en {ciudad}, {pais}",
        "sedes_extra": "+ {cnt} centros adicionales verificados en red.",
        "exp_title": "Modelo de Expansión & Inversores",
        "exp_contract": "Tipo de Contrato",
        "exp_profile": "Perfil de Club Idóneo",
        "exp_fees": "Canon & Royalties",
        "exp_diff": "Diferencial Competitivo",
        "tech_title": "Especificaciones Técnicas de Instalación",
        "tech_courts": "Pistas y Cubiertas",
        "tech_software": "Software y App",
        "tech_automation": "Domótica y Accesos",
        "tech_recording": "Grabación de Partidos",
        "tech_hospitality": "Hospitality & Pro-Shop",
        "b2b_badge": "EQUIPAMIENTO B2B OFICIAL",
        "b2b_title": "¿Gestionas o estás abriendo un centro de {nombre}?",
        "b2b_desc": "CoolPadel Studios suministra la tecnología de pista y el merchandising oficial para que los clubes de la red aumenten su facturación por partido y fidelicen a sus jugadores:",
        "b2b_box1_title": "Cámaras Save my Play sin obras",
        "b2b_box1_desc": "180 € hardware por pista y 45 €/mes. Pulsador en poste, descarga QR y streaming a YouTube sin tocar cableado ni hacer zanjas.",
        "b2b_box2_title": "Llaveros 3D de Goma Oficiales",
        "b2b_box2_desc": "Llaveros de pala en relieve tridimensional con el escudo del club. Muestra previa en 15 días laborables por 15€ descontables del pedido.",
        "b2b_cta_wa": "Hablar con Javier sobre {nombre}",
        "b2b_cta_specs": "Ver Especificaciones Save my Play",
        "tools_badge": "Calculadoras Oficiales 2026",
        "tools_title": "Simuladores Gratuitos para Abrir o Equipar un Club como {nombre}",
        "tools_view_all": "Ver todas las herramientas →",
        "tool_1_title": "🏗️ Coste de Montar Pistas",
        "tool_1_desc": "Simula CAPEX de pistas panorámicas, solera, césped y amortización.",
        "tool_2_title": "📹 Calculadora ROI Cámaras",
        "tool_2_desc": "Calcula el retorno de instalar cámaras Save my Play (45 €/mes).",
        "tool_3_title": "🎾 Generador de Americana",
        "tool_3_desc": "Crea cruces para 8 a 24 jugadores y compártelos por WhatsApp.",
        "tool_4_title": "🏆 Cuadros de Torneo",
        "tool_4_desc": "Genera cuadros de 8, 16 y 32 parejas con consolación e impresión.",
        "peers_title": "Otras Cadenas y Franquicias de Pádel Relacionadas ({pais})",
        "peers_compare": "Comparar las 167 franquicias →",
        "contact_badge": "Contacto B2B CoolPadel",
        "contact_title": "¿Interesado en {nombre} o en Franquicias de Pádel?",
        "contact_desc": "Te asesoramos sobre digitalización, cámaras Save my Play y merchandising para instalaciones de pádel.",
        "contact_wa_title": "WhatsApp Directo",
        "contact_wa_desc": "Respuesta inmediata por chat para dudas sobre clubes.",
        "contact_wa_btn": "Hablar por WhatsApp",
        "contact_email_title": "Email Corporativo",
        "contact_email_desc": "Envíanos tu propuesta de expansión o dossier de club.",
        "contact_back_btn": "Volver al Directorio y Comparador de Franquicias de Pádel",
        "footer_brand_desc": "Fabricación de llaveros de pádel personalizados 3D y sistemas de cámaras de grabación en pista Save my Play.",
        "footer_col1_title": "Soluciones B2B",
        "footer_col2_title": "Herramientas & SaaS",
        "footer_col3_title": "Directorio & Hubs",
        "footer_col4_title": "Guías & Blog B2B",
        "footer_rights": "© 2026 CoolPadel Studios · All rights reserved",
        "footer_return_policy": "Política de Devoluciones",
        "faq_q1": "¿Cuántos centros y pistas opera {nombre}?",
        "faq_a1": "{nombre} cuenta con una red de {num_clubs} y un parque total estimado de {num_pistas} en {pais}.",
        "faq_q2": "¿Qué software de reservas utiliza {nombre}?",
        "faq_a2": "{nombre} gestiona sus pistas con {software}, permitiendo reservas para socios y jugadores.",
        "faq_q3": "¿Es compatible {nombre} con las cámaras de grabación Save my Play?",
        "faq_a3": "Sí. Save my Play se fija en los postes de las pistas de {nombre} sin obras ni canalizaciones (180 € hardware y 45 €/mes software), compatible con cualquier software de reservas.",
    },
    "en": {
        "nav_llaveros": "KEYCHAINS",
        "nav_camaras": "CAMERAS",
        "nav_blog": "Blog",
        "nav_cadenas": "Club Networks",
        "nav_contacto": "Contact",
        "bc_home": "Home",
        "bc_dir": "Padel Franchises",
        "bc_dir_schema": "Padel Club Networks & Franchises Directory",
        "btn_back_dir": "Back to Full Directory",
        "hq_label": "Headquarters",
        "founders_label": "Founders",
        "metric_clubs": "Clubs / Venues",
        "metric_courts": "Total Courts",
        "metric_software": "Software",
        "metric_inv": "Average Investment",
        "btn_inquire": "Equipment Inquiry for {nombre}",
        "btn_official_web": "Official Website",
        "sedes_title": "Key Locations & Signature Clubs",
        "sedes_audit": "Continuously verified in 2026 padel census",
        "sedes_view_map": "View global directory →",
        "sedes_facilities_in": "Facilities in {ciudad}, {pais}",
        "sedes_extra": "+ {cnt} additional verified clubs across network.",
        "exp_title": "Expansion Model & Franchise Opportunities",
        "exp_contract": "Contract Type",
        "exp_profile": "Ideal Club Profile",
        "exp_fees": "Fees & Royalties",
        "exp_diff": "Competitive Edge",
        "tech_title": "Technical Specifications & Court Standards",
        "tech_courts": "Courts & Canopy",
        "tech_software": "Software & App",
        "tech_automation": "Access Control & Automation",
        "tech_recording": "Video Recording Systems",
        "tech_hospitality": "Hospitality & Pro-Shop",
        "b2b_badge": "OFFICIAL B2B EQUIPMENT",
        "b2b_title": "Managing or opening a {nombre} club?",
        "b2b_desc": "CoolPadel Studios supplies court video systems and official custom merchandising to help club networks boost revenue per match and drive player loyalty:",
        "b2b_box1_title": "Save my Play Cameras (No Trenching)",
        "b2b_box1_desc": "€180 hardware per court and €45/month. Post push-button, instant QR download and YouTube live streaming with zero cable trenching.",
        "b2b_box2_title": "Custom 3D Rubber Keychains",
        "b2b_box2_desc": "3D custom racket-shaped keychains molded with your club crest. Pre-production physical sample delivered in 15 business days for €15 (deductible).",
        "b2b_cta_wa": "Talk to Javier about {nombre}",
        "b2b_cta_specs": "View Save my Play Specs",
        "tools_badge": "Official 2026 Calculators",
        "tools_title": "Free Calculators to Launch or Equip a Club like {nombre}",
        "tools_view_all": "View all tools →",
        "tool_1_title": "🏗️ Court Construction Cost",
        "tool_1_desc": "Simulate CAPEX for panoramic courts, slab, turf and payback period.",
        "tool_2_title": "📹 Camera ROI Calculator",
        "tool_2_desc": "Calculate return on investment for Save my Play cameras (€45/month).",
        "tool_3_title": "🎾 Americano Generator",
        "tool_3_desc": "Generate balanced match rotations for 8 to 24 players and share via WhatsApp.",
        "tool_4_title": "🏆 Tournament Bracket Maker",
        "tool_4_desc": "Generate single elimination brackets for 8, 16 or 32 pairs with consolation.",
        "peers_title": "Other Related Padel Networks & Franchises ({pais})",
        "peers_compare": "Compare all 167 networks →",
        "contact_badge": "CoolPadel B2B Inquiries",
        "contact_title": "Interested in {nombre} or Padel Franchises?",
        "contact_desc": "We advise operators on club digitization, Save my Play court cameras and custom merchandise for padel facilities.",
        "contact_wa_title": "Direct WhatsApp",
        "contact_wa_desc": "Instant response via chat for club inquiries.",
        "contact_wa_btn": "Chat on WhatsApp",
        "contact_email_title": "Corporate Email",
        "contact_email_desc": "Send us your expansion deck or equipment inquiry.",
        "contact_back_btn": "Back to Padel Franchises Directory & Comparison",
        "footer_brand_desc": "Custom 3D padel keychains manufacturing and Save my Play on-court autonomous recording cameras.",
        "footer_col1_title": "B2B Solutions",
        "footer_col2_title": "Tools & SaaS",
        "footer_col3_title": "Directory & Hubs",
        "footer_col4_title": "Guides & B2B Blog",
        "footer_rights": "© 2026 CoolPadel Studios · All rights reserved",
        "footer_return_policy": "Return & Warranty Policy",
        "faq_q1": "How many clubs and courts does {nombre} operate?",
        "faq_a1": "{nombre} operates a network of {num_clubs} and an estimated total of {num_pistas} in {pais}.",
        "faq_q2": "What booking software does {nombre} use?",
        "faq_a2": "{nombre} manages its courts with {software}, facilitating bookings for members and players.",
        "faq_q3": "Is {nombre} compatible with Save my Play recording cameras?",
        "faq_a3": "Yes. Save my Play mounts onto court posts at {nombre} with zero civil works or trenching (€180 hardware and €45/month software), fully compatible with any booking software.",
    },
    "fr": {
        "nav_llaveros": "PORTE-CLÉS",
        "nav_camaras": "CAMÉRAS",
        "nav_blog": "Blog",
        "nav_cadenas": "Réseaux de Clubs",
        "nav_contacto": "Contact",
        "bc_home": "Accueil",
        "bc_dir": "Franchises Padel",
        "bc_dir_schema": "Annuaire des Franchises et Réseaux de Padel",
        "btn_back_dir": "Retour à l'Annuaire Complet",
        "hq_label": "Siège Principal",
        "founders_label": "Fondateurs",
        "metric_clubs": "Clubs / Centres",
        "metric_courts": "Pistes Totales",
        "metric_software": "Logiciel",
        "metric_inv": "Investissement Moyen",
        "btn_inquire": "Demander Équipement pour {nombre}",
        "btn_official_web": "Site Officiel",
        "sedes_title": "Centres et Complexes de Référence",
        "sedes_audit": "Données auditées - recensement padel 2026",
        "sedes_view_map": "Voir l'annuaire mondial →",
        "sedes_facilities_in": "Installations à {ciudad}, {pais}",
        "sedes_extra": "+ {cnt} centres supplémentaires vérifiés sur le réseau.",
        "exp_title": "Modèle de Développement & Franchise",
        "exp_contract": "Type de Contrat",
        "exp_profile": "Profil de Club Idéal",
        "exp_fees": "Droits d'Entrée & Redevances",
        "exp_diff": "Avantage Concurrentiel",
        "tech_title": "Spécifications Techniques des Installations",
        "tech_courts": "Pistes & Couvertures",
        "tech_software": "Logiciel & App",
        "tech_automation": "Contrôle d'Accès & Domotique",
        "tech_recording": "Enregistrement Vidéo des Matchs",
        "tech_hospitality": "Hospitality & Pro-Shop",
        "b2b_badge": "ÉQUIPEMENT B2B OFFICIEL",
        "b2b_title": "Vous gérez ou ouvrez un club {nombre} ?",
        "b2b_desc": "CoolPadel Studios fournit les caméras vidéo sur piste et le merchandising personnalisé pour maximiser les revenus par partie et fidéliser vos joueurs :",
        "b2b_box1_title": "Caméras Save my Play sans travaux",
        "b2b_box1_desc": "180 € matériel par piste et 45 €/mois. Bouton sur poteau, téléchargement QR et live YouTube sans tranchées ni passage de câbles complexe.",
        "b2b_box2_title": "Porte-clés 3D en Caoutchouc Officiels",
        "b2b_box2_desc": "Porte-clés raquette en relief 3D avec logo du club. Échantillon réel sous 15 jours ouvrés pour 15€ (déductibles de votre commande).",
        "b2b_cta_wa": "Échanger avec Javier sur {nombre}",
        "b2b_cta_specs": "Voir Spécifications Save my Play",
        "tools_badge": "Calculateurs Officiels 2026",
        "tools_title": "Simulateurs Gratuits pour Ouvrir ou Équiper un Club comme {nombre}",
        "tools_view_all": "Voir tous les outils →",
        "tool_1_title": "🏗️ Coût Construction Pistes",
        "tool_1_desc": "Simulez le CAPEX des pistes panoramiques, dalle, gazon et rentabilité.",
        "tool_2_title": "📹 Calculateur ROI Caméras",
        "tool_2_desc": "Calculez le retour sur investissement des caméras Save my Play (45 €/mois).",
        "tool_3_title": "🎾 Générateur Tournoi Americana",
        "tool_3_desc": "Générez des rotations équilibrées de 8 à 24 joueurs avec partage WhatsApp.",
        "tool_4_title": "🏆 Tableaux de Tournoi",
        "tool_4_desc": "Créez des tableaux à élimination directe pour 8, 16 ou 32 paires avec consolante.",
        "peers_title": "Autres Réseaux et Franchises de Padel Associés ({pais})",
        "peers_compare": "Comparer les 167 réseaux →",
        "contact_badge": "Contact B2B CoolPadel",
        "contact_title": "Intéressé par {nombre} ou les Franchises de Padel ?",
        "contact_desc": "Nous accompagnons les gérants dans la digitalisation, les caméras Save my Play et le merchandising personnalisé pour clubs de padel.",
        "contact_wa_title": "WhatsApp Direct",
        "contact_wa_desc": "Réponse immédiate par messagerie pour toute question club.",
        "contact_wa_btn": "Discuter sur WhatsApp",
        "contact_email_title": "Email Entreprise",
        "contact_email_desc": "Envoyez-nous votre dossier d'extension ou demande d'équipement.",
        "contact_back_btn": "Retour à l'Annuaire et Comparateur des Franchises de Padel",
        "footer_brand_desc": "Fabrication de porte-clés padel 3D sur-mesure et systèmes de caméras autonomes Save my Play.",
        "footer_col1_title": "Solutions B2B",
        "footer_col2_title": "Outils & SaaS",
        "footer_col3_title": "Annuaire & Hubs",
        "footer_col4_title": "Guides & Blog B2B",
        "footer_rights": "© 2026 CoolPadel Studios · Tous droits réservés",
        "footer_return_policy": "Politique de Retour & Garantie",
        "faq_q1": "Combien de centres et de pistes exploite {nombre} ?",
        "faq_a1": "{nombre} dispose d'un réseau de {num_clubs} et d'un total estimé de {num_pistas} en {pais}.",
        "faq_q2": "Quel logiciel de réservation utilise {nombre} ?",
        "faq_a2": "{nombre} gère ses pistes avec {software}, facilitant les réservations des adhérents et joueurs.",
        "faq_q3": "{nombre} est-il compatible avec les caméras d'enregistrement Save my Play ?",
        "faq_a3": "Oui. Save my Play se fixe sur les poteaux des pistes de {nombre} sans travaux ni tranchées (180 € matériel et 45 €/mois logiciel), compatible avec tout logiciel de réservation.",
    },
    "it": {
        "nav_llaveros": "PORTACHIAVI",
        "nav_camaras": "TELECAMERE",
        "nav_blog": "Blog",
        "nav_cadenas": "Reti di Club",
        "nav_contacto": "Contatti",
        "bc_home": "Home",
        "bc_dir": "Franchigie Padel",
        "bc_dir_schema": "Directory delle Franchigie di Padel",
        "btn_back_dir": "Torna alla Directory Completa",
        "hq_label": "Sede Principale",
        "founders_label": "Fondatori",
        "metric_clubs": "Club / Sedi",
        "metric_courts": "Campi Totali",
        "metric_software": "Software",
        "metric_inv": "Investimento Medio",
        "btn_inquire": "Richiedi Attrezzature per {nombre}",
        "btn_official_web": "Sito Ufficiale",
        "sedes_title": "Sedi e Centri di Riferimento",
        "sedes_audit": "Dati verificati nel censimento padel 2026",
        "sedes_view_map": "Vedi mappa globale →",
        "sedes_facilities_in": "Strutture a {ciudad}, {pais}",
        "sedes_extra": "+ {cnt} ulteriori centri verificati nella rete.",
        "exp_title": "Modello di Espansione & Franchising",
        "exp_contract": "Tipo di Contratto",
        "exp_profile": "Profilo Ideale del Club",
        "exp_fees": "Fee d'Ingresso & Royalty",
        "exp_diff": "Vantaggio Competitivo",
        "tech_title": "Specifiche Tecniche degli Impianti",
        "tech_courts": "Campi & Coperture",
        "tech_software": "Software & App",
        "tech_automation": "Controllo Accessi & Domotica",
        "tech_recording": "Registrazione Video delle Partite",
        "tech_hospitality": "Hospitality & Pro-Shop",
        "b2b_badge": "FORNITURA B2B UFFICIALE",
        "b2b_title": "Gestisci o stai aprendo un centro {nombre}?",
        "b2b_desc": "CoolPadel Studios fornisce telecamere per campi da padel e merchandising personalizzato per aumentare i ricavi per partita e fidelizzare i giocatori:",
        "b2b_box1_title": "Telecamere Save my Play senza opere murarie",
        "b2b_box1_desc": "180 € hardware per campo e 45 €/mese. Pulsante su palo, download QR immediato e live YouTube senza cavi interrati o canaline.",
        "b2b_box2_title": "Portachiavi 3D in Gomma Ufficiali",
        "b2b_box2_desc": "Portachiavi pala 3D personalizzati con lo stemma del club. Campione fisico in 15 giorni lavorativi a 15€ (scontabili dall'ordine).",
        "b2b_cta_wa": "Parla con Javier di {nombre}",
        "b2b_cta_specs": "Vedi Specifiche Save my Play",
        "tools_badge": "Calcolatori Ufficiali 2026",
        "tools_title": "Simulatori Gratuiti per Aprire o Attrezzare un Club come {nombre}",
        "tools_view_all": "Vedi tutti gli strumenti →",
        "tool_1_title": "🏗️ Costo Costruzione Campi",
        "tool_1_desc": "Simula CAPEX per campi panoramici, massetto, manto e ammortamento.",
        "tool_2_title": "📹 Calcolatore ROI Telecamere",
        "tool_2_desc": "Calcola il ritorno dell'installazione delle telecamere Save my Play (45 €/mese).",
        "tool_3_title": "🎾 Generatore di Torneo Americana",
        "tool_3_desc": "Crea rotazioni equilibrate per 8-24 giocatori e condividile via WhatsApp.",
        "tool_4_title": "🏆 Tabelloni di Torneo",
        "tool_4_desc": "Genera tabelloni a eliminazione diretta per 8, 16 o 32 coppie con tabellone di consolazione.",
        "peers_title": "Altre Reti e Franchigie di Padel Collegate ({pais})",
        "peers_compare": "Confronta tutte le 167 reti →",
        "contact_badge": "Contatto B2B CoolPadel",
        "contact_title": "Interessato a {nombre} o alle Franchigie di Padel?",
        "contact_desc": "Offriamo consulenza su digitalizzazione, telecamere Save my Play e merchandising personalizzato per centri di padel.",
        "contact_wa_title": "WhatsApp Diretto",
        "contact_wa_desc": "Risposta immediata via chat per domande sui club.",
        "contact_wa_btn": "Chatta su WhatsApp",
        "contact_email_title": "Email Aziendale",
        "contact_email_desc": "Inviaci la tua proposta di espansione o richiesta per il club.",
        "contact_back_btn": "Torna alla Directory e Comparatore delle Franchigie di Padel",
        "footer_brand_desc": "Produzione di portachiavi da padel personalizzati 3D e telecamere di registrazione autonoma Save my Play.",
        "footer_col1_title": "Soluzioni B2B",
        "footer_col2_title": "Strumenti & SaaS",
        "footer_col3_title": "Directory & Hub",
        "footer_col4_title": "Guide & Blog B2B",
        "footer_rights": "© 2026 CoolPadel Studios · Tutti i diritti riservati",
        "footer_return_policy": "Politica di Reso & Garanzia",
        "faq_q1": "Quanti centri e campi gestisce {nombre}?",
        "faq_a1": "{nombre} conta su una rete di {num_clubs} e un totale stimato di {num_pistas} in {pais}.",
        "faq_q2": "Quale software di prenotazione utilizza {nombre}?",
        "faq_a2": "{nombre} gestisce i suoi campi con {software}, consentendo prenotazioni per soci e giocatori.",
        "faq_q3": "{nombre} è compatibile con le telecamere di registrazione Save my Play?",
        "faq_a3": "Sì. Save my Play si installa sui pali dei campi di {nombre} senza opere murarie o canaline (180 € hardware e 45 €/mese software), compatibile con qualsiasi software di prenotazione.",
    }
}

def escape_txt(text):
    if not text:
        return ""
    return html.escape(str(text))

def localize_country(pais_es, lang="es"):
    if lang == "es":
        return pais_es
    return COUNTRY_NAMES.get(pais_es, {}).get(lang, pais_es)

def localize_modelo(modelo_es, lang="es"):
    if lang == "es":
        return modelo_es
    return MODELO_NAMES.get(modelo_es, {}).get(lang, modelo_es)

def localize_phrase(text, lang="es"):
    if not text or lang == "es":
        return text
    
    phrase_maps = {
        "en": {
            "Pistas de pádel reglamentarias": "Official regulation padel courts",
            "Accesos automatizados": "Automated access control & lighting",
            "Compatible con cámaras fijas autónomas Save my Play": "Compatible with Save my Play standalone court cameras",
            "Zona social y cafetería": "Clubhouse lounge & pro-shop / café",
            "Cadena propia y/o franquicia": "Corporate network & franchise agreements",
            "Franquicia y máster franquicia": "Franchise & master franchise models",
            "Cadena propia": "Directly owned club network",
            "Naves industriales y clubes deportivos": "Industrial buildings & sports complexes",
            "Consultar condiciones": "Inquire for terms",
            "A convenir": "On request / customized",
            "Software estándar": "Standard management software",
        },
        "fr": {
            "Pistas de pádel reglamentarias": "Pistes de padel réglementaires",
            "Accesos automatizados": "Contrôle d'accès et éclairage automatisés",
            "Compatible con cámaras fijas autónomas Save my Play": "Compatible avec les caméras autonomes Save my Play",
            "Zona social y cafetería": "Espace club-house et café / pro-shop",
            "Cadena propia y/o franquicia": "Réseau propre et/ou contrats de franchise",
            "Franquicia y máster franquicia": "Franchise et master franchise",
            "Cadena propia": "Réseau de clubs en propre",
            "Naves industriales y clubes deportivos": "Bâtiments industriels et complexes sportifs",
            "Consultar condiciones": "Consulter les conditions",
            "A convenir": "À convenir / sur mesure",
            "Software estándar": "Logiciel de gestion standard",
        },
        "it": {
            "Pistas de pádel reglamentarias": "Campi da padel regolamentari",
            "Accesos automatizados": "Controllo accessi e illuminazione automatizzati",
            "Compatible con cámaras fijas autónomas Save my Play": "Compatibile con le telecamere autonome Save my Play",
            "Zona social y cafetería": "Clubhouse, caffetteria e pro-shop",
            "Cadena propia y/o franquicia": "Rete diretta e/o contratti di franchising",
            "Franquicia y máster franquicia": "Franchising e master franchising",
            "Cadena propia": "Rete di club a gestione diretta",
            "Naves industriales y clubes deportivos": "Capannoni industriali e centri sportivi",
            "Consultar condiciones": "Consultare le condizioni",
            "A convenir": "Su richiesta / su misura",
            "Software estándar": "Software di gestione standard",
        }
    }
    
    mapping = phrase_maps.get(lang, {})
    return mapping.get(text, text)


def generate_single_page(f, lang="es"):
    t = I18N.get(lang, I18N["es"])
    fid = f["id"]
    nombre = f["nombre"]
    pais_es = f["pais"]
    pais_loc = localize_country(pais_es, lang)
    pais_codigo = f.get("pais_codigo", "ES")
    bandera = f.get("bandera", "🎾")
    ciudad = f.get("ciudad_sede", "")
    
    modelo_es = f.get("modelo", "Cadena Multiclub")
    modelo_loc = localize_modelo(modelo_es, lang)
    badge_cls = f.get("modelo_badge", "bg-sky-100 text-sky-800 border-sky-200")
    
    num_clubs = f.get("num_clubs", "N/A")
    num_pistas = f.get("num_pistas", "N/A")
    software = f.get("software", "Software estándar")
    software_display = software.split('/')[0].strip()
    fundadores = f.get("fundadores", "N/D")
    web = f.get("web", "")
    
    diferencial_raw = f.get("diferencial", "")
    diferencial = localize_phrase(diferencial_raw, lang) if lang != "es" else diferencial_raw

    tech = f.get("tecnologia_pistas", {})
    exp = f.get("modelo_expansion", {})

    pistas_desc = localize_phrase(tech.get("pistas", "Pistas de pádel reglamentarias"), lang)
    software_desc = localize_phrase(tech.get("software", software), lang)
    domotica_desc = localize_phrase(tech.get("domotica", "Accesos automatizados"), lang)
    grabacion_desc = localize_phrase(tech.get("grabacion", "Compatible con cámaras fijas autónomas Save my Play"), lang)
    restauracion_desc = localize_phrase(tech.get("restauracion", "Zona social y cafetería"), lang)

    tipo_contrato = localize_phrase(exp.get("tipo_contrato", "Cadena propia y/o franquicia"), lang)
    perfil_club = localize_phrase(exp.get("perfil_club", "Naves industriales y clubes deportivos"), lang)
    canon_royalties = localize_phrase(exp.get("canon_royalties", "Consultar condiciones"), lang)
    inversion_media = localize_phrase(exp.get("inversion_media", "A convenir"), lang)

    path_prefix = "" if lang == "es" else f"{lang}/"
    home_url = "/" if lang == "es" else f"/{lang}/"
    asset_prefix = "../../" if lang == "es" else "../../../"
    canonical_url = f"https://coolpadelstudios.com/franquicias-padel/{fid}/" if lang == "es" else f"https://coolpadelstudios.com/{lang}/franquicias-padel/{fid}/"
    hub_url = "/franquicias-padel/" if lang == "es" else f"/{lang}/franquicias-padel/"
    og_locale = {"es": "es_ES", "en": "en_US", "fr": "fr_FR", "it": "it_IT"}.get(lang, "es_ES")

    # Tagline y Resumen Localizados para evitar duplicación
    if lang == "es":
        tagline = f.get("tagline", "")
        resumen = f.get("resumen", "")
    elif lang == "en":
        tagline = f"Leading {modelo_loc.lower()} operating {num_clubs} and {num_pistas} across {pais_loc}."
        resumen = f"{nombre} is a premier padel club network headquartered in {ciudad} ({pais_loc}). The operator manages {num_clubs} with approximately {num_pistas}, utilizing {software_display} for seamless player bookings and compatible with Save my Play autonomous court recording."
    elif lang == "fr":
        tagline = f"Réseau majeur de {modelo_loc.lower()} exploitant {num_clubs} et {num_pistas} en {pais_loc}."
        resumen = f"{nombre} est un réseau de référence du padel basé à {ciudad} ({pais_loc}). L'opérateur gère {num_clubs} avec environ {num_pistas}, s'appuyant sur {software_display} pour la réservation des joueurs et compatible avec les caméras Save my Play."
    else:  # it
        tagline = f"Rete leader di {modelo_loc.lower()} con {num_clubs} e {num_pistas} in {pais_loc}."
        resumen = f"{nombre} è una rete di riferimento nel mondo del padel con sede a {ciudad} ({pais_loc}). Il gruppo gestisce {num_clubs} con circa {num_pistas}, integrando {software_display} per la gestione dei campi e compatibile con le telecamere Save my Play."

    wa_msgs = {
        "es": f"Hola Javier, estoy viendo la ficha de {nombre} en el directorio de franquicias y quiero consultar sobre equipamiento de cámaras Save my Play y llaveros 3D.",
        "en": f"Hello Javier, I am viewing {nombre} in the padel franchise directory and want to inquire about Save my Play cameras and 3D custom keychains.",
        "fr": f"Bonjour Javier, je consulte la fiche de {nombre} sur l'annuaire des franchises et souhaite des informations sur les caméras Save my Play et porte-clés 3D.",
        "it": f"Ciao Javier, sto guardando la scheda di {nombre} nella directory franchigie e vorrei informazioni su telecamere Save my Play e portachiavi 3D."
    }
    wa_msg = wa_msgs.get(lang, wa_msgs["es"])
    wa_url = f"https://api.whatsapp.com/send?phone=34680317486&text={urllib.parse.quote(wa_msg)}"

    # Sedes
    sedes = f.get("sedes_principales", [])
    sub_clubs = f.get("sub_clubs", [])
    sedes_items = []
    if sub_clubs:
        for sc in sub_clubs[:12]:
            s_nom = sc.get("nombre", "")
            s_ciu = sc.get("ciudad", "")
            s_pis = sc.get("pistas", "")
            extra = f" · {s_pis}" if s_pis else ""
            q = urllib.parse.quote(f"{s_nom} {s_ciu} padel")
            maps_link = f"https://www.google.com/maps/search/?api=1&query={q}"
            sedes_items.append(f'''<li class="p-2.5 rounded-xl bg-slate-50 hover:bg-amber-50/70 border border-slate-200/80 transition flex items-center justify-between gap-3 group">
              <div class="flex items-center gap-2.5 min-w-0">
                <span class="w-7 h-7 rounded-lg bg-white border border-slate-200 flex items-center justify-center text-xs group-hover:bg-[#f2920b] group-hover:text-slate-950 shrink-0 shadow-2xs">🎾</span>
                <div class="truncate">
                  <strong class="text-xs sm:text-sm font-black text-slate-950 group-hover:text-[#f2920b] transition block truncate">{escape_txt(s_nom)}</strong>
                  <span class="text-[11px] text-slate-500 font-medium">{escape_txt(s_ciu)}{escape_txt(extra)}</span>
                </div>
              </div>
              <a href="{maps_link}" target="_blank" rel="noopener noreferrer" class="shrink-0 inline-flex items-center gap-1 px-2.5 py-1 rounded-lg bg-white hover:bg-[#f2920b] hover:text-slate-950 border border-slate-200 text-[11px] font-bold text-slate-600 transition shadow-2xs">
                <span>Google Maps</span>
                <i data-lucide="arrow-up-right" class="w-3 h-3"></i>
              </a>
            </li>''')
        if len(sub_clubs) > 12:
            sedes_items.append(f'<li class="text-xs text-slate-500 font-bold italic pt-2 text-center">{t["sedes_extra"].format(cnt=len(sub_clubs)-12)}</li>')
    elif sedes:
        for s in sedes[:12]:
            q = urllib.parse.quote(f"{s} padel")
            maps_link = f"https://www.google.com/maps/search/?api=1&query={q}"
            sedes_items.append(f'''<li class="p-2.5 rounded-xl bg-slate-50 hover:bg-amber-50/70 border border-slate-200/80 transition flex items-center justify-between gap-3 group">
              <div class="flex items-center gap-2.5 min-w-0">
                <span class="w-7 h-7 rounded-lg bg-white border border-slate-200 flex items-center justify-center text-xs group-hover:bg-[#f2920b] group-hover:text-slate-950 shrink-0 shadow-2xs">🎾</span>
                <strong class="text-xs sm:text-sm font-black text-slate-950 group-hover:text-[#f2920b] transition truncate">{escape_txt(s)}</strong>
              </div>
              <a href="{maps_link}" target="_blank" rel="noopener noreferrer" class="shrink-0 inline-flex items-center gap-1 px-2.5 py-1 rounded-lg bg-white hover:bg-[#f2920b] hover:text-slate-950 border border-slate-200 text-[11px] font-bold text-slate-600 transition shadow-2xs">
                <span>Google Maps</span>
                <i data-lucide="arrow-up-right" class="w-3 h-3"></i>
              </a>
            </li>''')
    else:
        inst_txt = t["sedes_facilities_in"].format(ciudad=ciudad, pais=pais_loc)
        sedes_items.append(f'<li class="flex items-start gap-2.5 py-1.5"><i data-lucide="map-pin" class="w-4 h-4 text-[#f2920b] shrink-0 mt-0.5"></i><span>{escape_txt(inst_txt)}</span></li>')
    sedes_html = "\n".join(sedes_items)

    # Franquicias relacionadas con enlace en el idioma correcto
    same_country = [x for x in FRANQUICIAS if x["id"] != fid and x.get("pais") == pais_es]
    other_country = [x for x in FRANQUICIAS if x["id"] != fid and x.get("pais") != pais_es]
    idx_self = next((i for i, x in enumerate(FRANQUICIAS) if x["id"] == fid), 0)
    pool = same_country + other_country
    peers = []
    if pool:
        for offset in range(min(6, len(pool))):
            peers.append(pool[(idx_self + offset) % len(pool)])

    peers_cards = []
    for pf in peers:
        pf_url = f"/franquicias-padel/{pf['id']}/" if lang == "es" else f"/{lang}/franquicias-padel/{pf['id']}/"
        pf_pais_loc = localize_country(pf.get('pais', ''), lang)
        peers_cards.append(f"""
        <a href="{pf_url}" class="group block bg-white hover:bg-slate-50 rounded-2xl p-4 border border-slate-200 hover:border-[#f2920b] transition shadow-2xs">
          <div class="flex items-center justify-between gap-2 mb-1.5">
            <span class="font-heading font-black text-sm text-slate-900 group-hover:text-[#f2920b] transition">{escape_txt(pf.get('bandera', '🎾'))} {escape_txt(pf['nombre'])}</span>
            <span class="text-[10px] font-bold px-2 py-0.5 rounded-full bg-slate-100 text-slate-600">{escape_txt(pf.get('num_clubs', ''))}</span>
          </div>
          <p class="text-xs text-slate-500 line-clamp-2">{escape_txt(pf.get('ciudad_sede', ''))} ({escape_txt(pf_pais_loc)}) · {escape_txt(pf.get('num_pistas', ''))} · {escape_txt(pf.get('software', '').split('/')[0].strip())}</p>
        </a>""")
    peers_html = "\n".join(peers_cards)

    loc_titles = {
        "es": f"{nombre} ({pais_loc}) | Franquicia de Pádel",
        "en": f"{nombre} ({pais_loc}) | Padel Club Network & Franchise",
        "fr": f"{nombre} ({pais_loc}) | Réseau & Franchise de Padel",
        "it": f"{nombre} ({pais_loc}) | Rete & Franchigia di Padel"
    }
    localized_title = loc_titles.get(lang, loc_titles["es"])
    if len(escape_txt(localized_title)) > 60:
        localized_title = f"{nombre[:30]} ({pais_loc}) | Padel"

    loc_descs = {
        "es": f"{nombre} ({pais_loc}): {num_clubs}, {num_pistas}, reservas en {software_display}, modelo {modelo_loc} e inversión para clubes de pádel.",
        "en": f"{nombre} ({pais_loc}): {num_clubs}, {num_pistas}, booking with {software_display}, {modelo_loc} model and Save my Play camera compatibility.",
        "fr": f"{nombre} ({pais_loc}): {num_clubs}, {num_pistas}, réservations sur {software_display}, modèle {modelo_loc} et caméras Save my Play.",
        "it": f"{nombre} ({pais_loc}): {num_clubs}, {num_pistas}, prenotazioni con {software_display}, modello {modelo_loc} e telecamere Save my Play."
    }
    localized_desc = loc_descs.get(lang, loc_descs["es"])
    if len(localized_desc) > 155:
        localized_desc = localized_desc[:152].rsplit(' ', 1)[0] + "..."

    # URLs hreflang limpias
    es_href = f"https://coolpadelstudios.com/franquicias-padel/{fid}/"
    en_href = f"https://coolpadelstudios.com/en/franquicias-padel/{fid}/"
    fr_href = f"https://coolpadelstudios.com/fr/franquicias-padel/{fid}/"
    it_href = f"https://coolpadelstudios.com/it/franquicias-padel/{fid}/"

    # Enlaces localizados para el footer
    tool_coste_url = f"{home_url}herramientas/calculadora-coste-pistas-padel/"
    tool_roi_url = f"{home_url}herramientas/calculadora-roi-camaras-padel/"
    tool_americana_url = f"{home_url}herramientas/generador-americana-padel/"
    tool_cuadros_url = f"{home_url}herramientas/generador-cuadros-torneo-padel/"
    tools_hub_url = f"{home_url}herramientas/"
    camaras_url = f"{home_url}camaras/"
    save_my_play_url = f"{home_url}save-my-play/"
    blog_url = f"{home_url}blog/"

    faq_q1_txt = t["faq_q1"].format(nombre=nombre)
    faq_a1_txt = t["faq_a1"].format(nombre=nombre, num_clubs=num_clubs, num_pistas=num_pistas, pais=pais_loc)
    faq_q2_txt = t["faq_q2"].format(nombre=nombre)
    faq_a2_txt = t["faq_a2"].format(nombre=nombre, software=software)
    faq_q3_txt = t["faq_q3"].format(nombre=nombre)
    faq_a3_txt = t["faq_a3"].format(nombre=nombre)

    page_html = f"""<!DOCTYPE html>
<html lang="{lang}" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
  <title>{escape_txt(localized_title)}</title>
  <meta name="description" content="{escape_txt(localized_desc)}">
  <link rel="canonical" href="{canonical_url}">

  <!-- SEO Multilingüe Hreflang Simétrico -->
  <link rel="alternate" hreflang="es" href="{es_href}">
  <link rel="alternate" hreflang="en" href="{en_href}">
  <link rel="alternate" hreflang="fr" href="{fr_href}">
  <link rel="alternate" hreflang="it" href="{it_href}">
  <link rel="alternate" hreflang="x-default" href="{es_href}">
  <meta name="language" content="{lang}">

  <!-- Open Graph -->
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="CoolPadel Studios">
  <meta property="og:locale" content="{og_locale}">
  <meta property="og:url" content="{canonical_url}">
  <meta property="og:title" content="{escape_txt(localized_title)}">
  <meta property="og:description" content="{escape_txt(localized_desc)}">
  <meta property="og:image" content="https://coolpadelstudios.com/assets/images/savemyplay-1.jpg">

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{escape_txt(localized_title)}">
  <meta name="twitter:description" content="{escape_txt(localized_desc)}">
  <meta name="twitter:image" content="https://coolpadelstudios.com/assets/images/savemyplay-1.jpg">
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">

  <!-- Favicon -->
  <link rel="icon" type="image/png" href="{asset_prefix}assets/images/favicon_transparente.png?v=transp3">
  <link rel="apple-touch-icon" sizes="180x180" href="{asset_prefix}assets/images/favicon_transparente.png?v=transp3">
  <meta name="theme-color" content="#0b1626">

  <!-- LLM & AI Discovery -->
  <link rel="alternate" type="text/markdown" href="https://coolpadelstudios.com/llms.txt" title="LLMs.txt">
  <link rel="alternate" type="text/markdown" href="https://coolpadelstudios.com/llms-full.txt" title="LLMs-Full.txt">

  <!-- Tailwind CSS & Lucide Icons -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script src="https://unpkg.com/lucide@0.468.0/dist/umd/lucide.min.js"></script>

  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@600;700;800;900&family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">

  <!-- Microsoft Clarity -->
  <script type="text/javascript">
    (function(c,l,a,r,i,t,y){{
      c[a]=c[a]||function(){{(c[a].q=c[a].q||[]).push(arguments)}};
      t=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i;
      y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);
    }})(window, document, "clarity", "script", "q7p8g52y9e");
  </script>

  <!-- Schema.org SportsOrganization, BreadcrumbList & FAQPage -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@graph": [
      {{
        "@type": "SportsOrganization",
        "@id": "{canonical_url}#organization",
        "name": "{escape_txt(nombre)}",
        "description": "{escape_txt(resumen or tagline)}",
        "url": "{web or canonical_url}",
        "address": {{
          "@type": "PostalAddress",
          "addressLocality": "{escape_txt(ciudad)}",
          "addressCountry": "{pais_codigo}"
        }}
      }},
      {{
        "@type": "BreadcrumbList",
        "itemListElement": [
          {{
            "@type": "ListItem",
            "position": 1,
            "name": "{escape_txt(t['bc_home'])}",
            "item": "https://coolpadelstudios.com{home_url}"
          }},
          {{
            "@type": "ListItem",
            "position": 2,
            "name": "{escape_txt(t['bc_dir_schema'])}",
            "item": "https://coolpadelstudios.com{hub_url}"
          }},
          {{
            "@type": "ListItem",
            "position": 3,
            "name": "{escape_txt(nombre)}",
            "item": "{canonical_url}"
          }}
        ]
      }},
      {{
        "@type": "FAQPage",
        "mainEntity": [
          {{
            "@type": "Question",
            "name": "{escape_txt(faq_q1_txt)}",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "{escape_txt(faq_a1_txt)}"
            }}
          }},
          {{
            "@type": "Question",
            "name": "{escape_txt(faq_q2_txt)}",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "{escape_txt(faq_a2_txt)}"
            }}
          }},
          {{
            "@type": "Question",
            "name": "{escape_txt(faq_q3_txt)}",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "{escape_txt(faq_a3_txt)}"
            }}
          }}
        ]
      }}
    ]
  }}
  </script>

  <style>
    body {{ font-family: 'Plus Jakarta Sans', sans-serif; }}
    h1, h2, h3, h4, .font-heading {{ font-family: 'Outfit', sans-serif; }}
    .bg-textured-blue {{
      background-color: #3478a6;
      background-image: linear-gradient(rgba(52, 120, 166, 0.40), rgba(52, 120, 166, 0.40)), url('{asset_prefix}assets/images/branding/textura_editorial_coolpadel.webp');
      background-blend-mode: normal, soft-light;
      background-size: cover;
      background-position: center;
    }}
  </style>
</head>
<body class="bg-textured-blue text-slate-900 antialiased selection:bg-[#f2920b] selection:text-slate-950 min-h-screen flex flex-col">

  <!-- Header Oficial CoolPadel con Selector de Idioma -->
  <header class="fixed top-0 left-0 w-full z-50 bg-white/95 backdrop-blur-md border-b border-slate-200/80 shadow-xs w-full">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 sm:h-20 flex items-center justify-between">
      <a href="{home_url}" class="flex items-center gap-2 group shrink-0" aria-label="CoolPadel Home">
        <img src="{asset_prefix}assets/images/coolpadel-mascot-hd.png" alt="Mascota CoolPadel" width="44" height="44" class="h-8 sm:h-11 w-auto object-contain group-hover:scale-105 transition" fetchpriority="high">
        <img src="{asset_prefix}assets/images/coolpadel-typography-hd.png" alt="CoolPadel" width="140" height="28" class="h-5 sm:h-7 w-auto object-contain" fetchpriority="high">
      </a>
      
      <div class="flex items-center gap-2 sm:gap-4 lg:gap-6">
        <a href="{home_url}#llaveros" class="hidden sm:inline-block font-heading font-black text-xs uppercase tracking-wider text-slate-700 hover:text-[#f2920b] transition whitespace-nowrap">{t['nav_llaveros']}</a>
        <a href="{camaras_url}" class="hidden sm:inline-block font-heading font-black text-xs uppercase tracking-wider text-slate-700 hover:text-[#f2920b] transition whitespace-nowrap">{t['nav_camaras']}</a>
        <a href="{blog_url}" class="hidden sm:inline-block font-heading font-black text-xs uppercase tracking-wider text-slate-700 hover:text-[#f2920b] transition whitespace-nowrap">{t['nav_blog']}</a>
        <a href="{hub_url}" class="hidden sm:inline-block font-heading font-black text-xs uppercase tracking-wider text-[#f2920b] transition whitespace-nowrap">{t['nav_cadenas']}</a>

        <!-- SELECTOR DE IDIOMA DIRECTO -->
        <div class="relative inline-block text-left" id="lang-dropdown-container">
          <button type="button" onclick="toggleLangDropdown(event)" id="lang-dropdown-btn" class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-full bg-slate-100 hover:bg-slate-200 border border-slate-200 text-xs font-black text-slate-900 shadow-xs transition cursor-pointer" aria-expanded="false" aria-haspopup="true">
            <span class="uppercase font-black">{lang.upper()}</span>
            <i data-lucide="chevron-down" class="w-3.5 h-3.5 stroke-[2.5] text-slate-600 transition-transform duration-200" id="lang-dropdown-arrow"></i>
          </button>
          <div id="lang-dropdown-menu" class="hidden absolute right-0 mt-2 w-24 bg-white rounded-2xl shadow-[0_12px_30px_rgba(0,0,0,0.15)] border border-slate-200 py-1.5 z-50 transition-all overflow-hidden">
            <a href="/franquicias-padel/{fid}/" class="lang-opt block {'font-black bg-amber-50 text-[#f2920b]' if lang=='es' else 'text-slate-700 hover:bg-[#f2920b] hover:text-slate-950 font-bold'} w-full text-center px-4 py-2 text-xs transition duration-150">ES</a>
            <a href="/en/franquicias-padel/{fid}/" class="lang-opt block {'font-black bg-amber-50 text-[#f2920b]' if lang=='en' else 'text-slate-700 hover:bg-[#f2920b] hover:text-slate-950 font-bold'} w-full text-center px-4 py-2 text-xs transition duration-150">EN</a>
            <a href="/fr/franquicias-padel/{fid}/" class="lang-opt block {'font-black bg-amber-50 text-[#f2920b]' if lang=='fr' else 'text-slate-700 hover:bg-[#f2920b] hover:text-slate-950 font-bold'} w-full text-center px-4 py-2 text-xs transition duration-150">FR</a>
            <a href="/it/franquicias-padel/{fid}/" class="lang-opt block {'font-black bg-amber-50 text-[#f2920b]' if lang=='it' else 'text-slate-700 hover:bg-[#f2920b] hover:text-slate-950 font-bold'} w-full text-center px-4 py-2 text-xs transition duration-150">IT</a>
          </div>
        </div>

        <a id="nav-contact-btn" href="{home_url}#contacto" class="inline-flex items-center gap-1.5 px-3.5 sm:px-4 py-1.5 sm:py-2 rounded-full bg-[#f2920b] hover:bg-[#76d3f6] text-slate-950 font-heading font-black text-xs uppercase tracking-wider transition shadow-sm hover:scale-105 active:scale-95 cursor-pointer">
          <span>{t['nav_contacto']}</span>
          <i data-lucide="arrow-down" class="w-3 h-3 stroke-[3]"></i>
        </a>

        <a href="{home_url}" class="group py-1 inline-flex items-center shrink-0 pl-1" aria-label="CoolPadel Eyes">
          <img src="{asset_prefix}assets/images/eyes-thumb.png?v=fixed_eyes" alt="CoolPadel Eyes" width="28" height="28" style="height: 26px; max-height: 26px; width: auto;" class="object-contain group-hover:scale-110 transition duration-300">
        </a>
      </div>
    </div>
  </header>
  <div class="h-16 sm:h-20 w-full shrink-0" aria-hidden="true"></div>

  <!-- Breadcrumbs -->
  <div class="max-w-5xl mx-auto px-4 sm:px-6 pt-6 pb-2">
    <nav class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-white/90 backdrop-blur-xs shadow-xs text-xs text-slate-600 flex-wrap" aria-label="Breadcrumb">
      <a href="{home_url}" class="hover:text-[#f2920b] transition">{escape_txt(t['bc_home'])}</a>
      <i data-lucide="chevron-right" class="w-3.5 h-3.5 text-slate-400"></i>
      <a href="{hub_url}" class="hover:text-[#f2920b] transition">{escape_txt(t['bc_dir'])}</a>
      <i data-lucide="chevron-right" class="w-3.5 h-3.5 text-slate-400"></i>
      <span class="text-slate-950 font-bold">{escape_txt(nombre)}</span>
    </nav>
  </div>

  <!-- Contenedor Principal -->
  <main class="max-w-5xl mx-auto px-4 sm:px-6 py-6 pb-16">

    <!-- Hero Card -->
    <div class="bg-white rounded-3xl p-6 sm:p-10 border border-slate-200/90 shadow-sm mb-8">
      <div class="flex items-start justify-between gap-4 flex-wrap mb-4">
        <div class="flex items-center gap-2">
          <span class="text-3xl sm:text-4xl">{bandera}</span>
          <span class="inline-block px-3 py-1 rounded-full text-xs font-bold border {badge_cls}">
            {escape_txt(modelo_loc)}
          </span>
          <span class="text-xs font-bold text-slate-500 bg-slate-100 px-2.5 py-1 rounded-md">
            {escape_txt(pais_loc)}
          </span>
        </div>
        <a href="{hub_url}" class="text-xs font-bold text-slate-500 hover:text-slate-900 flex items-center gap-1 transition">
          <i data-lucide="arrow-left" class="w-3.5 h-3.5"></i>
          <span>{escape_txt(t['btn_back_dir'])}</span>
        </a>
      </div>

      <h1 class="text-3xl sm:text-5xl font-heading font-black text-slate-950 tracking-tight mb-3">
        {escape_txt(nombre)}
      </h1>
      <p class="text-xs sm:text-sm font-semibold text-slate-500 flex items-center gap-1.5 mb-5">
        <i data-lucide="map-pin" class="w-4 h-4 text-[#f2920b]"></i>
        <span>{escape_txt(t['hq_label'])}: <strong>{escape_txt(ciudad)}</strong> ({escape_txt(pais_loc)}) · {escape_txt(t['founders_label'])}: {escape_txt(fundadores)}</span>
      </p>

      {f'<p class="text-base sm:text-lg text-slate-700 font-medium leading-relaxed mb-6 border-l-4 border-[#f2920b] pl-4">{escape_txt(tagline)}</p>' if tagline else ''}

      <p class="text-slate-600 text-sm sm:text-base leading-relaxed mb-8">
        {escape_txt(resumen)}
      </p>

      <!-- Métricas Clave Grid -->
      <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 p-4 bg-slate-50 rounded-2xl border border-slate-200/80 mb-6">
        <div>
          <span class="block text-[11px] uppercase font-bold text-slate-400 mb-0.5">{escape_txt(t['metric_clubs'])}</span>
          <span class="font-heading font-black text-lg sm:text-xl text-slate-950">{escape_txt(num_clubs)}</span>
        </div>
        <div>
          <span class="block text-[11px] uppercase font-bold text-slate-400 mb-0.5">{escape_txt(t['metric_courts'])}</span>
          <span class="font-heading font-black text-lg sm:text-xl text-slate-950">{escape_txt(num_pistas)}</span>
        </div>
        <div>
          <span class="block text-[11px] uppercase font-bold text-slate-400 mb-0.5">{escape_txt(t['metric_software'])}</span>
          <span class="font-heading font-bold text-sm sm:text-base text-slate-800 truncate block" title="{escape_txt(software)}">{escape_txt(software_display)}</span>
        </div>
        <div>
          <span class="block text-[11px] uppercase font-bold text-slate-400 mb-0.5">{escape_txt(t['metric_inv'])}</span>
          <span class="font-heading font-bold text-xs sm:text-sm text-slate-800">{escape_txt(inversion_media)}</span>
        </div>
      </div>

      <!-- Botones de Acción -->
      <div class="flex items-center gap-3 flex-wrap">
        <a href="{wa_url}" target="_blank" rel="noopener"
           class="inline-flex items-center justify-center gap-2 bg-[#25D366] hover:bg-[#20ba5a] text-slate-950 font-black px-6 py-3.5 rounded-xl text-xs sm:text-sm transition shadow-sm">
          <i data-lucide="message-circle" class="w-4 h-4"></i>
          <span>{escape_txt(t['btn_inquire'].format(nombre=nombre))}</span>
        </a>
        {f'<a href="{web}" target="_blank" rel="noopener nofollow" class="inline-flex items-center justify-center gap-2 bg-slate-100 hover:bg-slate-200 text-slate-800 font-bold px-5 py-3.5 rounded-xl text-xs sm:text-sm border border-slate-200 transition"><i data-lucide="globe" class="w-4 h-4 text-slate-500"></i><span>{escape_txt(t["btn_official_web"])}</span><i data-lucide="external-link" class="w-3.5 h-3.5 text-slate-400"></i></a>' if web and web != "https://coolpadelstudios.com/franquicias-padel/" else ''}
      </div>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 gap-8 mb-8">
      
      <!-- Bloque 1: Sedes Principales -->
      <div class="bg-white rounded-3xl p-6 sm:p-8 border border-slate-200/90 shadow-sm flex flex-col justify-between">
        <div>
          <h2 class="text-xl font-heading font-black text-slate-950 mb-4 flex items-center gap-2">
            <i data-lucide="building-2" class="w-5 h-5 text-[#f2920b]"></i>
            <span>{escape_txt(t['sedes_title'])}</span>
          </h2>
          <ul class="text-slate-700 text-sm divide-y divide-slate-100">
            {sedes_html}
          </ul>
        </div>
        <div class="pt-4 mt-4 border-t border-slate-100 text-xs text-slate-500 flex items-center justify-between">
          <span>{escape_txt(t['sedes_audit'])}</span>
          <a href="{hub_url}" class="text-[#f2920b] font-bold hover:underline">{escape_txt(t['sedes_view_map'])}</a>
        </div>
      </div>

      <!-- Bloque 2: Modelo de Negocio y Expansión -->
      <div class="bg-white rounded-3xl p-6 sm:p-8 border border-slate-200/90 shadow-sm flex flex-col justify-between">
        <div>
          <h2 class="text-xl font-heading font-black text-slate-950 mb-4 flex items-center gap-2">
            <i data-lucide="briefcase" class="w-5 h-5 text-[#f2920b]"></i>
            <span>{escape_txt(t['exp_title'])}</span>
          </h2>
          <div class="space-y-3 text-sm text-slate-700">
            <div class="p-3 bg-slate-50 rounded-xl border border-slate-100">
              <span class="block text-[11px] font-bold uppercase text-slate-400 mb-0.5">{escape_txt(t['exp_contract'])}</span>
              <span class="font-semibold text-slate-900">{escape_txt(tipo_contrato)}</span>
            </div>
            <div class="p-3 bg-slate-50 rounded-xl border border-slate-100">
              <span class="block text-[11px] font-bold uppercase text-slate-400 mb-0.5">{escape_txt(t['exp_profile'])}</span>
              <span class="text-slate-800">{escape_txt(perfil_club)}</span>
            </div>
            <div class="p-3 bg-slate-50 rounded-xl border border-slate-100">
              <span class="block text-[11px] font-bold uppercase text-slate-400 mb-0.5">{escape_txt(t['exp_fees'])}</span>
              <span class="text-slate-800">{escape_txt(canon_royalties)}</span>
            </div>
            {f'<div class="p-3 bg-amber-50/60 rounded-xl border border-amber-200/60"><span class="block text-[11px] font-bold uppercase text-amber-700 mb-0.5">{escape_txt(t["exp_diff"])}</span><span class="text-slate-800">{escape_txt(diferencial)}</span></div>' if diferencial else ''}
          </div>
        </div>
      </div>

    </div>

    <!-- Bloque 3: Especificaciones Técnicas y Compatibilidad de Pista -->
    <div class="bg-white rounded-3xl p-6 sm:p-8 border border-slate-200/90 shadow-sm mb-8">
      <h2 class="text-xl font-heading font-black text-slate-950 mb-6 flex items-center gap-2">
        <i data-lucide="cpu" class="w-5 h-5 text-[#3478a6]"></i>
        <span>{escape_txt(t['tech_title'])}</span>
      </h2>
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4 text-xs sm:text-sm">
        <div class="p-4 bg-slate-50 rounded-2xl border border-slate-200/70">
          <span class="block font-bold text-slate-900 mb-1 flex items-center gap-1.5">
            <i data-lucide="box" class="w-4 h-4 text-slate-500"></i>
            <span>{escape_txt(t['tech_courts'])}</span>
          </span>
          <span class="text-slate-600 leading-relaxed block">{escape_txt(pistas_desc)}</span>
        </div>
        <div class="p-4 bg-slate-50 rounded-2xl border border-slate-200/70">
          <span class="block font-bold text-slate-900 mb-1 flex items-center gap-1.5">
            <i data-lucide="smartphone" class="w-4 h-4 text-slate-500"></i>
            <span>{escape_txt(t['tech_software'])}</span>
          </span>
          <span class="text-slate-600 leading-relaxed block">{escape_txt(software_desc)}</span>
        </div>
        <div class="p-4 bg-slate-50 rounded-2xl border border-slate-200/70">
          <span class="block font-bold text-slate-900 mb-1 flex items-center gap-1.5">
            <i data-lucide="key" class="w-4 h-4 text-slate-500"></i>
            <span>{escape_txt(t['tech_automation'])}</span>
          </span>
          <span class="text-slate-600 leading-relaxed block">{escape_txt(domotica_desc)}</span>
        </div>
        <div class="p-4 bg-slate-50 rounded-2xl border border-slate-200/70">
          <span class="block font-bold text-slate-900 mb-1 flex items-center gap-1.5">
            <i data-lucide="video" class="w-4 h-4 text-slate-500"></i>
            <span>{escape_txt(t['tech_recording'])}</span>
          </span>
          <span class="text-slate-600 leading-relaxed block">{escape_txt(grabacion_desc)}</span>
        </div>
        <div class="p-4 bg-slate-50 rounded-2xl border border-slate-200/70 col-span-1 sm:col-span-2">
          <span class="block font-bold text-slate-900 mb-1 flex items-center gap-1.5">
            <i data-lucide="coffee" class="w-4 h-4 text-slate-500"></i>
            <span>{escape_txt(t['tech_hospitality'])}</span>
          </span>
          <span class="text-slate-600 leading-relaxed block">{escape_txt(restauracion_desc)}</span>
        </div>
      </div>
    </div>

    <!-- Módulo B2B: Soluciones CoolPadel para esta Cadena -->
    <div class="bg-gradient-to-br from-[#0b1626] to-[#152e4d] rounded-3xl p-6 sm:p-10 text-white shadow-xl mb-8">
      <div class="max-w-3xl">
        <span class="inline-block px-3 py-1 rounded-full bg-[#f2920b] text-slate-950 font-black text-xs uppercase tracking-wider mb-4">
          {escape_txt(t['b2b_badge'])}
        </span>
        <h2 class="text-2xl sm:text-3xl font-heading font-black mb-3">
          {escape_txt(t['b2b_title'].format(nombre=nombre))}
        </h2>
        <p class="text-slate-300 text-sm sm:text-base leading-relaxed mb-6">
          {escape_txt(t['b2b_desc'])}
        </p>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 mb-8">
          <div class="p-4 bg-white/10 rounded-2xl border border-white/15 backdrop-blur">
            <div class="flex items-center gap-2 mb-2 text-[#f2920b] font-bold text-sm">
              <i data-lucide="video" class="w-4 h-4"></i>
              <span>{escape_txt(t['b2b_box1_title'])}</span>
            </div>
            <p class="text-xs text-slate-300 leading-relaxed">
              {escape_txt(t['b2b_box1_desc'])}
            </p>
          </div>
          <div class="p-4 bg-white/10 rounded-2xl border border-white/15 backdrop-blur">
            <div class="flex items-center gap-2 mb-2 text-[#f2920b] font-bold text-sm">
              <i data-lucide="tag" class="w-4 h-4"></i>
              <span>{escape_txt(t['b2b_box2_title'])}</span>
            </div>
            <p class="text-xs text-slate-300 leading-relaxed">
              {escape_txt(t['b2b_box2_desc'])}
            </p>
          </div>
        </div>

        <div class="flex items-center gap-4 flex-wrap">
          <a href="{wa_url}" target="_blank" rel="noopener"
             class="inline-flex items-center justify-center gap-2 bg-[#25D366] hover:bg-[#20ba5a] text-slate-950 font-black px-6 py-3.5 rounded-xl text-xs sm:text-sm transition">
            <i data-lucide="message-circle" class="w-4 h-4"></i>
            <span>{escape_txt(t['b2b_cta_wa'].format(nombre=nombre))}</span>
          </a>
          <a href="{save_my_play_url}" 
             class="inline-flex items-center justify-center gap-2 bg-white/10 hover:bg-white/20 text-white font-bold px-5 py-3.5 rounded-xl text-xs sm:text-sm border border-white/20 transition">
            <span>{escape_txt(t['b2b_cta_specs'])}</span>
          </a>
        </div>
      </div>
    </div>

    <!-- Herramientas Gratuitas para Gestores e Inversores -->
    <div class="bg-white rounded-3xl p-6 sm:p-8 border border-slate-200 shadow-xs space-y-4">
      <div class="flex items-center justify-between flex-wrap gap-2">
        <div>
          <span class="text-[11px] font-black uppercase tracking-wider text-[#f2920b]">{escape_txt(t['tools_badge'])}</span>
          <h2 class="text-lg sm:text-xl font-heading font-black text-slate-900">{escape_txt(t['tools_title'].format(nombre=nombre))}</h2>
        </div>
        <a href="{tools_hub_url}" class="text-xs font-bold text-[#3478a6] hover:underline">{escape_txt(t['tools_view_all'])}</a>
      </div>
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-3 text-xs">
        <a href="{tool_coste_url}" class="p-3.5 rounded-2xl bg-slate-50 hover:bg-amber-50 border border-slate-200 hover:border-[#f2920b] transition">
          <div class="font-heading font-black text-slate-900 mb-1">{escape_txt(t['tool_1_title'])}</div>
          <p class="text-slate-600">{escape_txt(t['tool_1_desc'])}</p>
        </a>
        <a href="{tool_roi_url}" class="p-3.5 rounded-2xl bg-slate-50 hover:bg-amber-50 border border-slate-200 hover:border-[#f2920b] transition">
          <div class="font-heading font-black text-slate-900 mb-1">{escape_txt(t['tool_2_title'])}</div>
          <p class="text-slate-600">{escape_txt(t['tool_2_desc'])}</p>
        </a>
        <a href="{tool_americana_url}" class="p-3.5 rounded-2xl bg-slate-50 hover:bg-amber-50 border border-slate-200 hover:border-[#f2920b] transition">
          <div class="font-heading font-black text-slate-900 mb-1">{escape_txt(t['tool_3_title'])}</div>
          <p class="text-slate-600">{escape_txt(t['tool_3_desc'])}</p>
        </a>
        <a href="{tool_cuadros_url}" class="p-3.5 rounded-2xl bg-slate-50 hover:bg-amber-50 border border-slate-200 hover:border-[#f2920b] transition">
          <div class="font-heading font-black text-slate-900 mb-1">{escape_txt(t['tool_4_title'])}</div>
          <p class="text-slate-600">{escape_txt(t['tool_4_desc'])}</p>
        </a>
      </div>
    </div>

    <!-- Malla de Interlinking: Otras Franquicias y Cadenas en el mismo mercado -->
    <div class="space-y-4 pt-6">
      <div class="flex items-center justify-between flex-wrap gap-2">
        <h2 class="text-lg sm:text-xl font-heading font-black text-slate-900">{escape_txt(t['peers_title'].format(pais=pais_loc))}</h2>
        <a href="{hub_url}" class="text-xs font-bold text-[#f2920b] hover:underline">{escape_txt(t['peers_compare'])}</a>
      </div>
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3.5">
        {peers_html}
      </div>
    </div>

    <!-- CONTACTO DIRECTO -->
    <section id="contacto" class="mt-12 bg-white rounded-3xl p-6 sm:p-10 border border-slate-200/90 shadow-md text-center">
      <span class="inline-block text-[#f2920b] text-xs font-bold uppercase tracking-wider mb-3">
        {escape_txt(t['contact_badge'])}
      </span>
      <h2 class="font-heading font-black text-2xl sm:text-3xl text-slate-950 uppercase tracking-tight mb-3">
        {escape_txt(t['contact_title'].format(nombre=nombre))}
      </h2>
      <p class="text-slate-600 text-sm sm:text-base max-w-xl mx-auto mb-8">
        {escape_txt(t['contact_desc'])}
      </p>

      <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 max-w-2xl mx-auto text-left">
        <div class="bg-slate-50 rounded-2xl p-5 border border-slate-200 flex flex-col justify-between">
          <div>
            <div class="w-10 h-10 rounded-xl bg-[#25D366]/15 text-[#25D366] flex items-center justify-center mb-3">
              <i data-lucide="message-circle" class="w-5 h-5 stroke-[2.5]"></i>
            </div>
            <h3 class="font-heading font-black text-base text-slate-950 mb-1">{escape_txt(t['contact_wa_title'])}</h3>
            <p class="text-slate-500 text-xs mb-3">{escape_txt(t['contact_wa_desc'])}</p>
          </div>
          <a href="{wa_url}" target="_blank" rel="noopener noreferrer"
             class="inline-flex items-center justify-center gap-2 w-full py-2.5 rounded-xl bg-[#25D366] hover:bg-[#20ba5a] text-slate-950 font-black text-xs uppercase tracking-wider transition">
            <i data-lucide="message-circle" class="w-4 h-4"></i>
            <span>{escape_txt(t['contact_wa_btn'])}</span>
          </a>
        </div>

        <div class="bg-slate-50 rounded-2xl p-5 border border-slate-200 flex flex-col justify-between">
          <div>
            <div class="text-[#f2920b] flex items-center justify-start mb-3">
              <i data-lucide="mail" class="w-5 h-5 stroke-[2.5]"></i>
            </div>
            <h3 class="font-heading font-black text-base text-slate-950 mb-1">{escape_txt(t['contact_email_title'])}</h3>
            <p class="text-slate-500 text-xs mb-3">{escape_txt(t['contact_email_desc'])}</p>
          </div>
          <a href="mailto:info@coolpadelstudios.com"
             class="inline-flex items-center justify-center gap-2 w-full py-2.5 rounded-xl bg-slate-950 hover:bg-slate-800 text-white font-black text-xs uppercase tracking-wider transition">
            <i data-lucide="mail" class="w-4 h-4"></i>
            <span>info@coolpadelstudios.com</span>
          </a>
        </div>
      </div>
    </section>

    <!-- Enlaces de Retorno y Directorio -->
    <div class="text-center py-6">
      <a href="{hub_url}" class="inline-flex items-center gap-2 px-5 py-2.5 rounded-full bg-white/90 text-sm font-bold text-slate-800 hover:text-[#f2920b] shadow-xs transition">
        <i data-lucide="arrow-left" class="w-4 h-4"></i>
        <span>{escape_txt(t['contact_back_btn'])}</span>
      </a>
    </div>

  </main>

  <!-- FOOTER INFERIOR LOCALIZADO -->
  <footer class="relative z-20 bg-[#3478a6] bg-textured-blue text-white pt-14 pb-10 border-t border-sky-700/40 text-xs">
    <div class="max-w-[1700px] mx-auto px-4 sm:px-8 space-y-10">
      
      <!-- TOP: BRANDING Y DESCRIPCIÓN B2B -->
      <div class="flex flex-col sm:flex-row items-center justify-between gap-4 pb-8 border-b border-white/20">
        <div class="flex items-center gap-3.5">
          <img src="{asset_prefix}assets/images/coolpadel-mascot-hd.png" alt="CoolPadel Mascota" width="60" height="60" class="h-10 sm:h-12 w-auto object-contain drop-shadow-sm" loading="lazy">
          <img src="{asset_prefix}assets/images/coolpadel-typography-hd.png" alt="CoolPadel" width="160" height="32" class="h-5 sm:h-6 w-auto object-contain drop-shadow-sm" loading="lazy">
        </div>
        <p class="text-white/80 text-xs text-center sm:text-right max-w-md font-medium">
          {escape_txt(t['footer_brand_desc'])}
        </p>
      </div>

      <!-- 4 COLUMNAS DE SILOS TEMÁTICOS SEO -->
      <nav aria-label="SEO Silos" class="grid grid-cols-2 lg:grid-cols-4 gap-8 text-left">
        
        <!-- COLUMNA 1: SOLUCIONES B2B -->
        <div class="space-y-3">
          <div class="font-heading font-black text-sm uppercase tracking-wider text-white">
            {escape_txt(t['footer_col1_title'])}
          </div>
          <ul class="space-y-2 text-white/80 font-normal">
            <li><a href="{home_url}#llaveros" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">{escape_txt(t['nav_llaveros'])} 3D</a></li>
            <li><a href="{save_my_play_url}" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">Save my Play</a></li>
            <li><a href="{camaras_url}" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">{escape_txt(t['nav_camaras'])}</a></li>
          </ul>
        </div>

        <!-- COLUMNA 2: HERRAMIENTAS & SOFTWARE -->
        <div class="space-y-3">
          <div class="font-heading font-black text-sm uppercase tracking-wider text-white">
            {escape_txt(t['footer_col2_title'])}
          </div>
          <ul class="space-y-2 text-white/80 font-normal">
            <li><a href="{tools_hub_url}" class="hover:text-white underline decoration-white/20 underline-offset-2 transition font-bold text-white">{escape_txt(t['tools_title'].format(nombre='Club'))}</a></li>
            <li><a href="{tool_americana_url}" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">{escape_txt(t['tool_3_title'])}</a></li>
            <li><a href="{tool_cuadros_url}" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">{escape_txt(t['tool_4_title'])}</a></li>
            <li><a href="{tool_coste_url}" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">{escape_txt(t['tool_1_title'])}</a></li>
            <li><a href="{tool_roi_url}" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">{escape_txt(t['tool_2_title'])}</a></li>
          </ul>
        </div>

        <!-- COLUMNA 3: DIRECTORIO & HUBS LOCALES -->
        <div class="space-y-3">
          <div class="font-heading font-black text-sm uppercase tracking-wider text-white">
            {escape_txt(t['footer_col3_title'])}
          </div>
          <ul class="space-y-2 text-white/80 font-normal">
            <li><a href="{hub_url}" class="hover:text-white underline decoration-white/20 underline-offset-2 transition font-bold text-white">{escape_txt(t['bc_dir_schema'])}</a></li>
            <li><a href="{blog_url}barometro-camaras-padel-2026/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">Barómetro Cámaras 2026</a></li>
          </ul>
        </div>

        <!-- COLUMNA 4: GUÍAS DEL SECTOR -->
        <div class="space-y-3">
          <div class="font-heading font-black text-sm uppercase tracking-wider text-white">
            {escape_txt(t['footer_col4_title'])}
          </div>
          <ul class="space-y-2 text-white/80 font-normal">
            <li><a href="{blog_url}" class="hover:text-white underline decoration-white/20 underline-offset-2 transition font-bold text-white">{escape_txt(t['nav_blog'])}</a></li>
            <li><a href="{blog_url}como-organizar-torneo-padel-americana-reglas-cuadros/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">Americana Pádel Reglas</a></li>
            <li><a href="{blog_url}rentabilidad-camaras-pistas-padel/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">Precios y ROI de Cámaras</a></li>
            <li><a href="{blog_url}sistemas-grabacion-pistas-padel-comparativa/" class="hover:text-white underline decoration-white/20 underline-offset-2 transition">Comparativa Cámaras</a></li>
          </ul>
        </div>

      </nav>

      <!-- BOTTOM: COPYRIGHT Y ENLACES LEGALES -->
      <div class="pt-8 border-t border-white/20 flex flex-col sm:flex-row items-center justify-between gap-3 text-white/75 text-center sm:text-left">
        <span>
          {escape_txt(t['footer_rights'])}
        </span>
        <div class="flex items-center gap-3">
          <a href="/politica-de-devoluciones.html" class="hover:text-white/90 underline decoration-white/30 underline-offset-2 transition">{escape_txt(t['footer_return_policy'])}</a>
          <span class="opacity-40">·</span>
          <a href="https://www.instagram.com/coolpadel_/" target="_blank" rel="noopener noreferrer" class="opacity-75 hover:opacity-100 transition text-white">@coolpadel_</a>
        </div>
      </div>

    </div>
  </footer>

  <script>
    lucide.createIcons();

    function toggleLangDropdown(e) {{
      e.stopPropagation();
      var menu = document.getElementById('lang-dropdown-menu');
      var arrow = document.getElementById('lang-dropdown-arrow');
      if (!menu) return;
      var isHidden = menu.classList.contains('hidden');
      menu.classList.toggle('hidden', !isHidden);
      if (arrow) arrow.style.transform = isHidden ? 'rotate(180deg)' : 'rotate(0deg)';
    }}

    document.addEventListener('click', function(e) {{
      var menu = document.getElementById('lang-dropdown-menu');
      var arrow = document.getElementById('lang-dropdown-arrow');
      if (menu && !menu.classList.contains('hidden')) {{
        menu.classList.add('hidden');
        if (arrow) arrow.style.transform = 'rotate(0deg)';
      }}
    }});
  </script>
  <script src="/assets/js/cp-analytics.js" defer></script>
</body>
</html>
"""
    if lang == "es":
        target_dir = os.path.join(BASE_DIR, "franquicias-padel", fid)
    else:
        target_dir = os.path.join(BASE_DIR, lang, "franquicias-padel", fid)
    os.makedirs(target_dir, exist_ok=True)
    target_file = os.path.join(target_dir, "index.html")
    with open(target_file, "w", encoding="utf-8") as fp:
        fp.write(page_html)
    return target_file


def main():
    print(f">> Generando páginas individuales para {len(FRANQUICIAS)} franquicias en 4 idiomas (ES, EN, FR, IT)...")
    for lang in ["es", "en", "fr", "it"]:
        count = 0
        for f in FRANQUICIAS:
            generate_single_page(f, lang=lang)
            count += 1
        print(f"  [OK] Completadas {count} fichas de franquicias para {lang.upper()}")


if __name__ == "__main__":
    main()
