# -*- coding: utf-8 -*-
"""
Respuestas directas y precisas (Answer-First) para AEO (Google AI Overviews, Perplexity, ChatGPT Search)
y Meta Descriptions enriquecidas (120-155 caracteres) para los 20 artículos de cámaras en los 5 idiomas.
"""

AEO_FAQS_AND_DESCS = {
    "es": {
        "por-donde-empezar-si-estoy-pensando-en-poner-camaras": {
            "desc": "Descubre por dónde empezar antes de poner cámaras en tu club de pádel: habla con otros clubes, compara precios y evita contratos de permanencia.",
            "answer": "Antes de elegir modelo, decide si tu club realmente necesita cámaras. Te aconsejo hablar primero con 2 o 3 clubes que ya las tengan instaladas para conocer su experiencia real, comparar los presupuestos de varias empresas y no firmar nunca contratos de permanencia."
        },
        "errores-clubs-se-arrepienten-de-poner-camaras": {
            "desc": "Los 3 errores más comunes de clubes al poner cámaras: pagar caras analíticas que nadie usa, firmar contratos largos y usar cámaras CCTV baratas.",
            "answer": "Los tres errores principales son: 1) Pagar cuotas caras por estadísticas de IA que el 95% de los jugadores amateurs no utiliza; 2) Firmar permanencias largas tras la euforia del primer mes; y 3) Instalar cámaras de videovigilancia baratas que deforman las líneas de la pista con efecto ojo de pez."
        },
        "camaras-de-padel-o-videovigilancia": {
            "desc": "Aprende a diferenciar cámaras deportivas de pádel frente a cámaras de videovigilancia CCTV estándar mirando las líneas de la pista y la óptica.",
            "answer": "La forma más rápida de detectarlo es mirar las líneas de la pista en el vídeo: si se ven curvas o con distorsión ojo de pez, son cámaras de videovigilancia baratas adaptadas. Las cámaras deportivas de pádel tienen óptica rectilínea de alta definición que muestra líneas rectas y nítidas de pared a pared."
        },
        "cuanto-cuesta-poner-camaras": {
            "desc": "¿Cuánto cuesta poner cámaras en tu club? Hardware en propiedad por 180 € y cuota de software desde 27 a 45 €/mes por pista sin permanencia.",
            "answer": "En Save My Play el coste es de 180 € de pago único por pista por la cámara en propiedad, y una cuota de software de 45 € al mes por pista (rebajada a 41 €, 36 € o 27 € según el número de pistas), sin obras y con cancelación mes a mes sin permanencia."
        },
        "inversion-inicial-camaras-180-euros": {
            "desc": "¿Por qué hay una inversión inicial de 180 € por cámara? Fabricación propia en USA con óptica deportiva y sin inflar las cuotas mensuales.",
            "answer": "Cobramos 180 € por cámara porque las fabricamos nosotros mismos en Chicago y California con óptica deportiva real en lugar de importar cámaras CCTV de bajo coste. Al cobrar el hardware a precio de fábrica casi a coste, podemos mantener la cuota mensual en solo 45 €/mes sin atarte a contratos largos."
        },
        "es-caro-save-my-play": {
            "desc": "¿Es caro Save My Play? Comparativa real de costes: 45 €/mes frente a los contratos de renting de 150-250 €/mes de la competencia.",
            "answer": "No es caro. Frente a sistemas de renting que exigen contratos de 3 a 5 años pagando entre 150 € y 250 € mensuales por pista, Save My Play cuesta 180 € de hardware en propiedad y 45 €/mes sin permanencia, amortizable con un incremento de apenas 0,50 € por reserva."
        },
        "es-rentable-poner-camaras": {
            "desc": "¿Es rentable poner cámaras de pádel en tu club? Cómo amortizar la cuota de 45 €/mes con horas valle, patrocinadores y torneos.",
            "answer": "Sí, es rentable activando 4 vías: llenando horas valle atrayendo a jugadores que quieren grabarse, vendiendo patrocinios con logos en pantalla, grabando torneos y cobrando un pequeño suplemento de 0,50 € por jugador en las reservas (amortizando los 45 €/mes en solo 22 partidos al mes)."
        },
        "por-que-no-recomiendo-plan-analytics": {
            "desc": "Por qué desaconsejo el plan de estadísticas de 136 €/mes al 95 % de los clubes: analíticas complejas que los jugadores apenas abren.",
            "answer": "No recomiendo el plan de 136 €/mes porque el 95% de los jugadores amateurs juegan por diversión y solo quieren compartir sus mejores puntos en WhatsApp o Instagram. Pagar casi 100 € extra al mes por mapas de calor y porcentajes de golpeo que casi nadie mira no es rentable para un club social."
        },
        "que-pasa-si-cancelo": {
            "desc": "¿Qué pasa si cancelas tu suscripción a Save My Play? Te quedas las cámaras en propiedad y no pagas penalización alguna.",
            "answer": "Si cancelas la suscripción no hay penalización ni permanencia: la cancelas con un clic en Stripe. Las cámaras son de tu propiedad y te las quedas en el club, aunque solo funcionarán si vuelves a reactivar el servicio cloud de Save My Play."
        },
        "como-montar-camara-save-my-play": {
            "desc": "Montaje de cámaras Save My Play en 10 minutos por pista: fijación rápida al poste a 4 metros, conexión a 220V y WiFi sin obras.",
            "answer": "Se monta en 10 minutos por pista con una escalera, un enchufe de 220V y cobertura WiFi. La cámara se fija mediante una abrazadera con tuerca de apriete a la estructura o poste a 4 metros de altura, sin necesidad de rozas ni zanjas de cableado."
        },
        "problemas-con-las-camaras": {
            "desc": "¿Qué ocurre si una cámara falla o se estropea? Cobertura completa, suspensión de la cuota mensual y reemplazo rápido.",
            "answer": "Si una cámara presenta cualquier fallo técnico en uso normal, congelamos inmediatamente la cuota de esa pista y enviamos un reemplazo o asistencia directa por WhatsApp para solucionarlo en 24-48 horas sin coste extra para el club."
        },
        "que-son-las-coaching-tools": {
            "desc": "Qué son las coaching tools de Save My Play: herramientas para monitores con pausa en tablet, trazado de líneas y notas de voz.",
            "answer": "Las coaching tools permiten a los monitores y entrenadores de la escuela pausar cualquier jugada a pie de pista en una tablet, dibujar trayectorias y ángulos sobre la pantalla, y grabar notas de voz explicativas para enviárselas directamente al teléfono del alumno."
        },
        "camaras-en-exterior-lluvia-nieve-viento": {
            "desc": "¿Aguantan las cámaras en pistas de pádel exteriores? Carcasa sellada IP contra lluvia torrencial, heladas, viento y pelotazos.",
            "answer": "Sí, están preparadas para la intemperie. Cuentan con carcasa deportiva estanca sellada con protección contra lluvia torrencial, condensación, nieve, viento fuerte e impactos accidentales de bolas de pádel a alta velocidad."
        },
        "como-ver-highlights-sin-app": {
            "desc": "Cómo descargan los jugadores sus mejores jugadas sin app: pulsador en poste, escaneo de código QR y visor en el navegador web.",
            "answer": "Los jugadores pulsan el botón en la red tras un gran punto. Al terminar el partido escanean el código QR ubicado en el poste con la cámara de su móvil y los clips de 25 segundos se abren directamente en el navegador sin descargar apps de tiendas ni registrar contraseñas."
        },
        "mejores-empresas-camaras-padel-espana": {
            "desc": "Comparativa de empresas de cámaras de pádel en España: Padmi, Aiball, Rackety y Save My Play. Modelos, costes y diferencias.",
            "answer": "Las principales alternativas en España son Padmi (dos cámaras y analítica IA), Aiball (estadísticas avanzadas y nivelado) y Rackety (con reservas y chatbots). Save My Play se diferencia por su coste accesible (180 € hardware y 45 €/mes), cero obras, pulsador físico y cero permanencia."
        },
        "por-que-no-conocia-save-my-play": {
            "desc": "¿Por qué no conocías Save My Play en España? Empresa estadounidense con +1.500 cámaras que ahora expande en Europa con CoolPadel.",
            "answer": "Save My Play nació en Estados Unidos, donde equipa a más de 1.500 pistas y es cámara oficial de la USTA y USA Padel. Su expansión en Europa se ha centrado en el boca a boca entre directores, distribuyéndose en España y la UE en exclusiva a través de CoolPadel Studios."
        },
        "save-my-play-en-pocas-palabras": {
            "desc": "Save My Play en cifras: +1.600 pistas activas en el mundo, cámara oficial de torneos FIP de Miami y USTA National Campus.",
            "answer": "Save My Play cuenta con más de 1.600 pistas activas en todo el mundo, retransmite torneos oficiales FIP de la Federación Internacional de Pádel y el circuito de la USTA en Florida, destacando por su equipo cercano y un sistema intuitivo de solo dos botones."
        },
        "por-que-coolpadel-colabora-con-save-my-play": {
            "desc": "Por qué CoolPadel se alió con Save My Play: tecnología con el mayor potencial del sector y atención directa sin intermediarios.",
            "answer": "CoolPadel se alió con Save My Play porque comprobamos en ferias internacionales que ofrece la tecnología más fiable, directa y honesta del mercado. Javier Villoria gestiona el asesoramiento, demos y soporte para clubes en España y Europa."
        },
        "he-comprado-camaras-que-pasa-ahora": {
            "desc": "He comprado cámaras Save My Play, ¿cuál es el proceso? Pago por Stripe, envío preconfigurado en 4 semanas y soporte de montaje.",
            "answer": "El proceso consta de 4 pasos: 1) Pago seguro en Stripe; 2) Alta de tu club en el panel cloud; 3) Envío de las cámaras configuradas en ~4 semanas; 4) Montaje en 10 minutos y activación de la cuota mensual solo cuando las cámaras estén en marcha."
        },
        "por-que-no-me-interesa-venderte-una-camara": {
            "desc": "Por qué no me interesa venderte una cámara si no estás convencido: un modelo rentable solo si el club las aprovecha a largo plazo.",
            "answer": "Vender una cámara a 180 € a un club que no está convencido y cancela al mes nos hace perder dinero a ambos, ya que fabricar cada cámara nos cuesta más que el precio de venta. Solo trabajamos con clubes que ven claro el valor del sistema a largo plazo."
        }
    },
    "fr": {
        "por-donde-empezar-si-estoy-pensando-en-poner-camaras": {
            "desc": "Conseils d'expert avant d'installer des caméras dans votre club de padel : retours d'autres clubs, devis et zéro engagement.",
            "answer": "Avant de choisir un modèle, vérifiez si votre club en a réellement l'utilité. Échangez d'abord avec des gestionnaires de clubs déjà équipés, comparez les offres et refusez tout contrat vous liant sur plusieurs années."
        },
        "errores-clubs-se-arrepienten-de-poner-camaras": {
            "desc": "Les 3 erreurs majeures des clubs avec les caméras : payer des statistiques inutiles, signer des engagements longs et caméras CCTV.",
            "answer": "Les trois erreurs courantes sont : 1) Payer des options IA chères que les joueurs amateurs délaissent ; 2) Signer des contrats bloquants de 3 à 5 ans ; et 3) Acheter du matériel de vidéosurveillance déformant l'image en œil-de-bœuf."
        },
        "cuanto-cuesta-poner-camaras": {
            "desc": "Tarifs clairs pour installer des caméras de padel : 180 € d'achat matériel par piste et abonnement logiciel dès 45 €/mois sans engagement.",
            "answer": "Chez Save My Play, l'investissement matériel est de 180 € par piste (boîtier en pleine propriété), avec un abonnement mensuel de 45 €/mois par piste (dégressif jusqu'à 27 €) sans engagement ni travaux lourds."
        },
        "que-pasa-si-cancelo": {
            "desc": "Résiliation d'abonnement Save My Play : vous conservez vos caméras en propriété et arrêtez les mensualités sans pénalité.",
            "answer": "Vous pouvez résilier votre abonnement mensuel Stripe à tout moment sans frais ni préavis. Les caméras achetées à 180 € restent la propriété définitive de votre club."
        },
        "que-son-las-coaching-tools": {
            "desc": "Outils de coaching Save My Play : analyse sur tablette au bord du court, ralenti, dessin de trajectoires et notes vocales.",
            "answer": "Les coaching tools permettent aux enseignants d'analyser les coups en direct sur tablette au bord de la piste, de tracer des repères visuels sur les ralentis et d'envoyer un débriefing vocal commenté sur le smartphone de l'élève."
        },
        "mejores-empresas-camaras-padel-espana": {
            "desc": "Comparatif des systèmes de caméras pour clubs de padel : Padmi, Aiball, Rackety et Save My Play.",
            "answer": "Le marché compte des acteurs axés sur l'IA tactique (Padmi, Aiball) ou la gestion globale (Rackety). Save My Play se démarque par son accessibilité (180 € matériel, 45 €/mois), sa pose en 10 min et sa totale liberté sans contrat pluriannuel."
        }
    },
    "en": {
        "por-donde-empezar-si-estoy-pensando-en-poner-camaras": {
            "desc": "Where to start before installing padel court cameras: talk to peers, compare transparent quotes and avoid lock-in contracts.",
            "answer": "First determine if court video brings genuine value to your members. Speak to experienced club directors, evaluate transparent pricing models, and strictly avoid long-term lock-in agreements."
        },
        "errores-clubs-se-arrepienten-de-poner-camaras": {
            "desc": "3 costly mistakes clubs make with padel cameras: overpaying for AI stats, signing multi-year leases, and cheap CCTV hardware.",
            "answer": "The three biggest pitfalls are: 1) Overpaying for complex AI stats that 95% of casual players ignore; 2) Signing 3-5 year leasing contracts; and 3) Installing repurposed security cameras with distorted fish-eye angles."
        },
        "cuanto-cuesta-poner-camaras": {
            "desc": "How much do padel court cameras cost? €180 owned hardware per court and €45/month software subscription with zero lock-in.",
            "answer": "Save My Play requires a one-time €180 hardware fee per court (you own the camera) and a flexible €45/month software subscription per court (tiered down to €27 for larger clubs), with zero construction works and month-to-month cancellation."
        },
        "que-pasa-si-cancelo": {
            "desc": "What happens if you cancel your camera subscription? You own the cameras permanently with zero exit penalties.",
            "answer": "You can cancel your month-to-month subscription in Stripe anytime with zero penalties. The cameras belong to your club permanently."
        },
        "que-son-las-coaching-tools": {
            "desc": "Save My Play coaching tools explained: tablet instant replay, slow-motion trajectory drawing, and voice feedback for coaches.",
            "answer": "Coaching tools empower club pros to review points courtside on a tablet, draw stroke mechanics on slow-motion video, and record voice notes sent straight to student phones."
        },
        "mejores-empresas-camaras-padel-espana": {
            "desc": "Comprehensive comparison of padel court camera companies: Padmi, Aiball, Rackety, and Save My Play.",
            "answer": "Leading platforms include Padmi (dual cameras and AI stats), Aiball (advanced federative analytics), and Rackety (booking automation). Save My Play stands out for fair pricing (€180 hardware, €45/mo), instant net buttons, and zero lock-in."
        }
    },
    "it": {
        "cuanto-cuesta-poner-camaras": {
            "desc": "Quanto costa installare telecamere nel tuo circolo di padel: 180 € acquisto per campo e canone software da 45 €/mese senza vincoli.",
            "answer": "Il costo di Save My Play è di 180 € una tantum a campo per la telecamera di proprietà e 45 € al mese per campo (fino a 27 € per volumi maggiori), senza opere murarie e con disdetta libera mese per mese."
        },
        "que-pasa-si-cancelo": {
            "desc": "Cosa succede se annulli l'abbonamento Save My Play? Tieni le telecamere di tua proprietà senza alcuna penale.",
            "answer": "Puoi annullare l'abbonamento mensile Stripe in qualsiasi momento senza penali. Le telecamere acquistate a 180 € restano di esclusiva proprietà del tuo circolo."
        },
        "que-son-las-coaching-tools": {
            "desc": "Cosa sono le coaching tools Save My Play: moviola su tablet a bordo campo, linee di traiettoria e note vocali per i maestri.",
            "answer": "Le coaching tools consentono ai maestri di rivedere i punti su tablet direttamente in campo, evidenziare traiettorie al rallentatore e inviare analisi vocali sullo smartphone dell'allievo."
        }
    },
    "de": {
        "cuanto-cuesta-poner-camaras": {
            "desc": "Was kosten Padel-Platz-Kameras? 180 € Hardware-Kauf pro Platz und ab 45 €/Monat Software ohne Vertragsbindung.",
            "answer": "Save My Play kostet einmalig 180 € pro Platz für die eigene Kamera und 45 € monatlich pro Platz für die Software (ab 27 € für größere Anlagen), ohne Baumaßnahmen und monatlich kündbar."
        },
        "que-pasa-si-cancelo": {
            "desc": "Was passiert bei Kündigung des Save My Play Abos? Die Kameras bleiben Ihr Eigentum ohne Strafgebühren.",
            "answer": "Sie können das monatliche Abonnement jederzeit ohne Strafen kündigen. Die gekauften Kameras bleiben dauerhaft Eigentum Ihrer Padel-Anlage."
        }
    }
}
