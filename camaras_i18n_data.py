# -*- coding: utf-8 -*-
"""
Diccionario completo y determinista de Camaras para FR, EN, IT, DE.
Estilo Javier: directo, natural, terminología real de pádel (courts, campi, Plätze, circoli),
enlaces internos resueltos y negritas clave preservadas. Cero coste de tokens de IA.
"""

from camaras_fr_data import FR_ARTICLES_DATA, FR_VIDEOS

# Actualizar coaching tools en FR con los 4 bloques completos como en ES
FR_ARTICLES_DATA["que-son-las-coaching-tools"] = {
    "title": "Que sont les outils de coaching (coaching tools) ?",
    "blocks": [
        [
            "Les <strong>coaching tools</strong> sont l'outil conçu pour que les entraîneurs de padel tirent un véritable profit des caméras pendant les cours de l'école ou de l'académie."
        ],
        [
            "Au lieu d'attendre la fin du match, le coach dispose d'une tablette connectée directement à la piste.",
            "Il peut mettre en pause le point que l'élève vient de jouer, revenir quelques secondes en arrière et lui montrer <strong>sur-le-champ ce qu'il a bien fait ou son erreur de placement</strong>."
        ],
        [
            "Directement sur l'écran de la tablette, l'entraîneur peut <strong>tracer des lignes de trajectoire, des angles de raquette et les zones</strong> où la balle aurait dû rebondir.",
            "Tout est enregistré en vidéo avec sa voix explicative en direct."
        ],
        [
            "À la fin de la séance, l'élève reçoit un lien direct sur son WhatsApp ou par e-mail avec les 3 ou 4 séquences commentées par son professeur.",
            "C'est un moyen redoutable de <strong>différencier votre académie de celle du club voisin</strong> et de fidéliser les joueurs qui cherchent à progresser."
        ],
    ],
}

EN_ARTICLES_DATA = {
    "por-donde-empezar-si-estoy-pensando-en-poner-camaras": {
        "title": "I'm thinking about installing cameras in my club, where do I start?",
        "blocks": [
            [
                "I completely understand if you feel a bit lost.",
                "You have probably seen other clubs installing cameras on their courts and you are wondering whether you should do the same.",
                "First of all, <strong>I recommend that you be cautious</strong>.",
                "Just because everyone else is doing it doesn't automatically mean it's the right move for your club.",
            ],
            [
                "Here is what I would do in your shoes:",
            ],
            [
                "1º <strong>Talk to clubs that already have cameras installed.</strong> Ideally clubs on the other side of the country so they have no conflict of interest and tell you the unfiltered truth. Most camera providers list their partner clubs on their websites.",
            ],
            [
                "2º <strong>Talk to different camera companies</strong> and hear what they offer. In Spain and Europe, besides Save My Play (who I work with), there are Rackety, Padmi, AIball, Courtmaster and a few smaller startups. Below you have my calendar in case you want to book a quick call.",
            ],
            [
                "3º <strong>Gather the feedback from both clubs and providers, compare, discuss it internally and decide.</strong> The first decision is not which brand of cameras to buy. First you have to decide <strong>whether you actually want cameras or not</strong>.",
            ],
            [
                'As your first read, I strongly recommend <a href="../errores-clubs-se-arrepienten-de-poner-camaras/">The 3 mistakes of clubs that regret installing cameras</a>.',
            ],
        ],
    },
    "errores-clubs-se-arrepienten-de-poner-camaras": {
        "title": "The 3 mistakes of clubs that regret installing cameras",
        "blocks": [
            [
                "Yes, you read that right.",
                "And it's not just one or two isolated cases.",
                "I spend every day speaking with padel club owners and managers, and these <strong>3 mistakes are repeated over and over again</strong>.",
                "I know that investing in court cameras is not a decision you want to get wrong.",
                "Take two minutes to read this and understand our perspective.",
                "Whatever you decide afterwards, you will make a much better-informed decision.",
            ],
            [
                "Error 1: AI analytics and shot statistics",
                "The idea sounds cool on paper, right?",
                "An AI that analyzes your match, counts how many shots you hit and tells you what to improve.",
                "The reality is that by your third match using it, you realize <strong>your heat map looks almost identical to every previous match</strong>.",
                "And knowing your percentage of sliced backhands with double spin is a metric that adds zero real value to 99% of amateur players.",
            ],
            [
                "It genuinely pains me to see the monthly fees that small local clubs pay for these AI stats packages.",
                "<strong>It is simply not profitable</strong> to pay those prices.",
                "It makes no financial sense.",
                "It's basic common sense.",
            ],
            [
                "Error 2: Free trial periods and long lock-in contracts",
                "Be very careful with free trial periods.",
                "Seriously.",
                "This is how the classic trap works:",
            ],
            [
                "1º <strong>During the first month</strong>, the novelty effect kicks in and everyone tries the cameras.",
            ],
            [
                "2º <strong>You sign a multi-year lock-in contract</strong> assuming usage will stay that high forever.",
            ],
            [
                "3º <strong>When the initial hype fades</strong>, you are stuck paying high monthly fees for years.",
            ],
            [
                "<strong>Never tie your club down</strong> with a mandatory lock-in contract.",
            ],
            [
                "Error 3: Most providers use generic CCTV surveillance cameras",
                "The video ends up looking like security footage from a bank robbery.",
                "The image quality and frame rate are poor.",
                "A dead giveaway to spot a surveillance camera is to look at the court lines.",
                "If the court lines look curved or fisheye-distorted, <strong>that's a bad sign</strong>.",
            ],
            [
                "When we do the online demo, remind me and I will show you the side-by-side difference.",
            ],
            [
                "ERROR EXTRA: I will share this one with you live during our online demo.",
            ],
            [
                "Conclusion:",
                "Quite a few clubs end up regretting the contracts and camera systems they signed up for.",
            ],
            [
                "I insist: don't just take my word for it.",
                "<strong>Talk directly to clubs that already have cameras</strong> and let them tell you their real experience.",
            ],
        ],
    },
    "camaras-de-padel-o-videovigilancia": {
        "title": "How to tell if my cameras are true padel cameras or CCTV surveillance cameras?",
        "blocks": [
            [
                "Beyond the obvious difference in video sharpness, there is an instant way to spot it.",
                "<strong>Just look at the lines of the court</strong>.",
                "Once you notice this detail, you won't be able to unsee it.",
                "Let me show you a real example.",
            ],
            [
                "In this image, you can immediately see that the court lines are not straight: <strong>they are visibly curved</strong>.",
                "The entire court is warped by a cheap wide-angle fisheye lens.",
                "That is the unmistakable signature of a generic CCTV security camera.",
            ],
            [
                "The lines of a padel court <strong>should always look straight</strong>.",
                "As close as possible to an official Premier Padel TV broadcast.",
            ],
        ],
    },
    "cuanto-cuesta-poner-camaras": {
        "title": "How much does it cost to install cameras in my padel club?",
        "blocks": [
            [
                "One of the first questions on your mind is probably: how much does it actually cost to put Save My Play cameras on my club's courts?",
                "Here is the exact breakdown, <strong>price per court</strong>.",
                "Only one camera is needed per court.",
                "We know this is an important business decision, so here are all the numbers upfront with full transparency:",
            ],
            [
                "We offer two monthly plans with zero lock-in:",
                '<strong>Plan A: €136 per month.</strong> Includes AI shot statistics and heat maps. I do not recommend it to 95% of clubs (<a href="../por-que-no-recomiendo-plan-analytics/">Why I don\'t recommend the €136/month AI plan</a>).',
                "<strong>Plan B: €45 per month.</strong> For the price of just one or two court bookings per month, your camera records full matches, instant highlights, YouTube live streams and coaching tools... unlimited.",
                "<strong>Zero lock-in contract.</strong>",
                "If you ever want to stop, you cancel your Stripe subscription in one click. No paperwork, no penalties.",
                "We don't want unhappy clubs locked into a contract; it doesn't benefit anyone in the long run.",
                "Even without lock-in, <strong>97% of clubs voluntarily stay with us</strong> month after month.",
            ],
            [
                '<strong>Initial hardware investment of €180 per camera</strong>, one camera per court (<a href="../inversion-inicial-camaras-180-euros/">Why is there an initial €180 hardware investment?</a>).',
                "No civil works or trenching required: it mounts in 5 minutes using just Wi-Fi and a standard power outlet.",
                "Due to high demand, shipping currently takes around 4 weeks. Customs duties are roughly €20. And if your club meets a few simple criteria, your first month's subscription can be free.",
            ],
        ],
    },
    "inversion-inicial-camaras-180-euros": {
        "title": "Why is there an initial investment of €180 for the cameras?",
        "blocks": [
            [
                "I know that <strong>this €180 upfront cost is one of the most common questions</strong> I get from clubs.",
                "It's a real cost, especially when some competitors advertise 'free hardware'. So you can make the best decision for your club, here is the exact reason behind it.",
            ],
            [
                "The main reason is that <strong>we manufacture our own cameras</strong>.",
                'That is rare in this industry. Most companies buy generic CCTV security cameras made in China because they are cheap (<a href="../camaras-de-padel-o-videovigilancia/">in this guide I show you how to spot them</a>). We design and manufacture ours in Chicago and California.',
                "In my opinion, the image quality is night and day. Players want their best rallies to share on Instagram and WhatsApp. You can't give them video that looks like <strong>security footage of a bank robbery</strong>.",
            ],
            [
                "Manufacturing each unit costs us <strong>significantly more than €180</strong>.",
                "We sell the hardware at a loss and recover the difference over time through the monthly subscription. €180 is the entry point for dedicated sports optics.",
                "If we gave the cameras away for €0 upfront, we would run out of working capital to manufacture more units unless we drastically raised the monthly fee. And in the long run, high monthly fees hurt your club much more than the initial €180. That's why <strong>our monthly plans are as competitive as possible</strong>.",
            ],
        ],
    },
    "es-caro-save-my-play": {
        "title": "Is Save My Play expensive?",
        "blocks": [
            [
                "This is a completely fair question that many club managers ask me. Here is how I see it.",
                "First of all, court cameras are <strong>not a product for 100% of clubs</strong>. It is a premium, differentiating service for your players. We are not trying to be in every single club, and that exclusivity is part of its value.",
            ],
            [
                "Now let's compare it with other providers. Our €136/month AI analytics plan is around the market average, though we don't recommend it to most clubs.",
                "However, our <strong>€45 per month plan</strong> is one of the most competitive prices you will find anywhere. Some brand-new startups might offer temporary discounts while testing beta products, but among established providers with proven hardware, it's hard to beat.",
                "In any case, compare options. <strong>Price isn't everything</strong>: look closely at video clarity, ease of use without apps, and whether they lock you into a multi-year contract.",
            ],
        ],
    },
    "es-rentable-poner-camaras": {
        "title": "Is it profitable to install cameras on my padel courts?",
        "blocks": [
            [
                "We know that padel clubs scrutinize every single expense. Naturally, you want to know whether installing cameras on your courts will actually generate a return. Here is our honest view.",
            ],
            [
                "First, let's be transparent: our €136/month AI analytics plan is <strong>not recommended for 95% of clubs</strong> because we don't believe the extra monthly cost pays for itself in most venues.",
            ],
            [
                "On the other hand, with our €45/month plan (plus the €180 camera hardware), here are the four concrete ways clubs make a return:",
            ],
            [
                "1º <strong>Stand out from competing clubs in your area:</strong> you offer a modern service players love. Players book at your club specifically to record their matches, boosting occupancy and positioning your venue as the reference club in town.",
            ],
            [
                "2º <strong>Organic social media marketing:</strong> your club's logo and local sponsor logos appear on every video clip. Players love uploading their best points to Instagram, TikTok and WhatsApp groups, giving your club free daily exposure.",
            ],
            [
                "3º <strong>Tournaments and academy coaching:</strong> live-streaming finals on YouTube and using tablet coaching tools during lessons adds huge value to events and coaching programs.",
            ],
            [
                "4º <strong>Direct monetization:</strong> some clubs add a tiny surcharge on camera courts. Charging just <strong>€0.50 extra per court booking</strong> covers the entire system (since €45/month is only €1.50 per day per court).",
            ],
        ],
    },
    "por-que-no-recomiendo-plan-analytics": {
        "title": "Why don't I recommend the €136/month AI plan to 95% of clubs?",
        "blocks": [
            [
                'If you have read our guide on <a href="../errores-clubs-se-arrepienten-de-poner-camaras/">the 3 mistakes clubs make when installing cameras</a>, the reason <strong>should be crystal clear</strong>.',
                "For 95% of clubs, paying €136 every month for AI heat maps and shot counts that amateur players check twice out of curiosity and then ignore is simply not a profitable investment.",
            ],
        ],
    },
    "que-pasa-si-cancelo": {
        "title": "What happens if I cancel my subscription? Do I keep the cameras?",
        "blocks": [
            [
                "This is a very common question clubs ask me before starting.",
            ],
            [
                'To give you full context: as explained in <a href="../inversion-inicial-camaras-180-euros/">why there is an initial €180 investment</a>, we manufacture the padel cameras ourselves. One camera per court. <strong>We have zero lock-in period</strong>—no binding contract, just a monthly subscription you can cancel anytime.',
            ],
            [
                "So what happens if you cancel?",
                "Yes, <strong>the cameras are yours and you keep them</strong>. However, they are built specifically to run on our cloud software, so they won't work as standalone third-party cameras.",
            ],
            [
                "Buying a camera and cancelling after one month <strong>is a failure for both you and us</strong>. You lose €180, and we lose money because manufacturing each unit costs us much more than €180. That's why we never push clubs to equip 10 courts on day one: we recommend starting with one or two courts first.",
            ],
            [
                "That honest approach is how we get <strong>97% of clubs to stay with us voluntarily</strong> every single month.",
            ],
        ],
    },
    "como-montar-camara-save-my-play": {
        "title": "How long does it take to install a Save My Play camera?",
        "blocks": [
            [
                "<strong>10 minutes.</strong>",
                "A ladder, <strong>Wi-Fi and a standard power outlet</strong>. That is literally all you need to install a camera.",
                "The camera clamps onto the 4-meter court fence or post with a single tightening nut. You plug the power cable into a standard socket and connect it to your club's Wi-Fi in a couple of minutes.",
            ],
            [
                "You also have the option of connecting it via Ethernet cable to your router. If you already have network cables running to the courts, great. If not, it's not worth paying for civil works: <strong>the vast majority of clubs run smoothly on Wi-Fi</strong>.",
            ],
        ],
    },
    "problemas-con-las-camaras": {
        "title": "What happens if there are technical problems with the cameras?",
        "blocks": [
            [
                "As long as the cameras are used normally, <strong>we take full responsibility</strong> for any technical issues that may arise.",
                "We work with over 1,500 clubs across countries with extreme weather conditions, so the hardware is battle-tested. If anything ever fails, <strong>we obviously pause your billing during that time</strong> and our support team steps in immediately to fix or replace the unit.",
            ],
        ],
    },
    "que-son-las-coaching-tools": {
        "title": "What are coaching tools?",
        "blocks": [
            [
                "<strong>Coaching tools</strong> are designed so padel coaches can get real, practical value out of the court cameras during academy lessons.",
            ],
            [
                "Instead of waiting until the lesson is over, the coach has a tablet connected live to the court.",
                "They can pause the point the student just played, scrub back in slow motion, and show them <strong>on the spot what they did well or where their positioning broke down</strong>.",
            ],
            [
                "Right on the tablet screen, the coach can <strong>draw ball trajectories, racket angles and target zones</strong> while recording their voice explanation.",
            ],
            [
                "At the end of the session, the student receives a direct link on WhatsApp or email with the 3 or 4 clips reviewed by their coach.",
                "It is a powerful way to <strong>differentiate your padel academy from rival clubs</strong> and retain students who want to improve.",
            ],
        ],
    },
    "camaras-en-exterior-lluvia-nieve-viento": {
        "title": "Do the cameras hold up on outdoor courts (rain, snow, wind)?",
        "blocks": [
            [
                "We manufacture a single weatherproof camera model that <strong>withstands whatever nature throws at it</strong>.",
                "<strong>High wind, snow, heavy rain, sun and direct ball impacts.</strong> It is engineered specifically for outdoor courts, which means it works effortlessly both outdoors and indoors.",
            ],
        ],
    },
    "como-ver-highlights-sin-app": {
        "title": "Why is there no Save My Play app? How do players watch their highlights?",
        "blocks": [
            [
                "The last thing a player wants one minute before stepping onto the court is to download an app, create an account and remember a password. What if signal is weak inside the club? For everyone to actually use the system, it has to be frictionless. Here is the process:",
            ],
            [
                "1º <strong>Scan the QR code</strong> at the court entrance.",
            ],
            [
                "2º <strong>Press the red button</strong> to start recording the full match.",
            ],
            [
                "3º <strong>Enter basic details:</strong> email address, match duration, optional YouTube live stream, or AI dead-time trimming.",
            ],
            [
                "4º <strong>Raise your arms facing the camera</strong> after any great point (or press the physical green button on the post) to bookmark that highlight.",
            ],
            [
                "5º <strong>Receive an email about an hour after finishing</strong> with your full match and saved highlights ready to watch and share—<strong>without downloading any mobile app</strong>.",
            ],
        ],
    },
    "mejores-empresas-camaras-padel-espana": {
        "title": "What are the best padel camera companies in Spain and Europe?",
        "blocks": [
            [
                'In Spain and Europe today there are several major court camera providers (<a href="../por-que-no-conocia-save-my-play/">here is why you might not have heard of Save My Play before</a>).',
            ],
            [
                "Each company has its own <strong>distinct vision</strong> of how court cameras should work. We bet on different hardware and different business models. That is why I always encourage you to talk to each provider, listen and compare—and above all, ask clubs that already use them.",
            ],
            [
                "<strong>Padmi:</strong> the provider with the most courts in Spain (around 82 courts across 56 clubs), using two cameras per court. They focus heavily on AI shot statistics alongside highlights, have a very polished brand aesthetic, and partner with the Adidas Padel Tour.",
            ],
            [
                "<strong>Aiball:</strong> present in several clubs in Spain, focusing on AI statistics and an objective player-leveling system. Pro player Ari Sánchez is a partner in the company, and they were named Best Startup at the Padel World Summit 2025.",
            ],
            [
                "<strong>Rackety:</strong> installed in around 50 clubs, combining match recording and AI stats with court booking software and WhatsApp chatbots in an all-in-one club management suite.",
            ],
        ],
    },
    "por-que-no-conocia-save-my-play": {
        "title": "Why had I never heard of Save My Play?",
        "blocks": [
            [
                "We are an <strong>American company</strong>.",
                "Even though Spain has more padel courts than any other country, historically it was a tougher market for us compared to the US and northern Europe, where clubs routinely equip every single court on day one—so <strong>we prioritized those international clients</strong>.",
                "Today we operate on more than <strong>1,500 club courts</strong> worldwide across padel, tennis and pickleball.",
            ],
        ],
    },
    "save-my-play-en-pocas-palabras": {
        "title": "Now let's talk about how good we are at Save My Play",
        "blocks": [
            [
                "I'll keep this brief.",
                "We are installed on more than <strong>1,600 courts around the world</strong>.",
                "The United States Padel Association (USPA) chose us to broadcast their official FIP tournaments, and the United States Tennis Association (USTA) streams live every weekend across more than 100 courts at its National Campus.",
            ],
            [
                "Even so, <strong>we are a lean team of fewer than 10 people</strong>.",
                "And that is what club managers value most: <strong>closeness and direct support</strong>. If anything goes wrong, you talk directly to us—your issue never gets lost in corporate bureaucracy.",
            ],
            [
                "We also refuse to overcomplicate things. If <strong>two buttons are enough</strong> to get the cameras running reliably, we don't add a third.",
            ],
        ],
    },
    "por-que-coolpadel-colabora-con-save-my-play": {
        "title": "Why does CoolPadel collaborate with Save My Play?",
        "blocks": [
            [
                "My favorite part of working in the padel industry is visiting trade shows and talking to founders at every booth.",
                "From knowing the market inside out, I consider Save My Play to be the court camera company with the <strong>greatest global potential</strong>—and just as importantly, <strong>they are honest, reliable people</strong>.",
                "Because Save My Play faces huge demand in the US, we teamed up so that at CoolPadel <strong>we manage and support clubs across Europe</strong>: Spain, France, the UK, Italy, Germany and beyond.",
            ],
        ],
    },
    "he-comprado-camaras-que-pasa-ahora": {
        "title": "I bought Save My Play cameras. What is the process now?",
        "blocks": [
            [
                "1º <strong>Payment via Stripe:</strong> I send you the payment link. Billing is processed in USD since Save My Play is a US company (paying in dollars via your bank usually saves on currency conversion fees).",
            ],
            [
                "2º <strong>Club account registration:</strong> you receive the link to create your Save My Play club account, and your cameras are automatically assigned to your venue.",
            ],
            [
                "3º <strong>Manufacturing & shipping:</strong> your cameras arrive in roughly 4 to 5 weeks.",
            ],
            [
                "4º <strong>Delivery & activation:</strong> you pay around €20 in customs duties upon delivery, mount the cameras in 10 minutes, and your monthly subscription only starts counting once the cameras are live on court.",
            ],
        ],
    },
    "por-que-no-me-interesa-venderte-una-camara": {
        "title": "Why am I not interested in selling you a camera if you're not convinced?",
        "blocks": [
            [
                "If I sell you a camera for €180, you test it half-heartedly and cancel after a month, <strong>we have all lost</strong>.",
                "You lose €180 and your time, and we lose money because manufacturing the hardware costs us far more than €180. We only want to work with clubs that truly see the value and want a long-term win-win.",
            ],
        ],
    },
}

IT_ARTICLES_DATA = {
    "por-donde-empezar-si-estoy-pensando-en-poner-camaras": {
        "title": "Sto pensando di installare telecamere nel mio circolo, da dove comincio?",
        "blocks": [
            [
                "Capisco perfettamente che tu possa sentirti un po' disorientato.",
                "Avrai sicuramente visto diversi circoli installare telecamere sui propri campi da padel e ti sarai chiesto se convenga farlo anche a te.",
                "Prima di tutto, <strong>ti consiglio di essere prudente</strong>.",
                "Solo perché lo fanno molti non significa automaticamente che sia la scelta giusta per il tuo club.",
            ],
            [
                "Ecco cosa farei al tuo posto:",
            ],
            [
                "1º <strong>Parla con i circoli che hanno già installato le telecamere.</strong> Meglio se si trovano dall'altra parte del paese, così non sono tuoi concorrenti diretti e ti diranno la pura verità. Sui siti dei fornitori trovi quasi sempre l'elenco dei club partner.",
            ],
            [
                "2º <strong>Parla con diverse aziende di telecamere</strong> e ascolta cosa propongono. In Spagna e in Europa, oltre a Save My Play con cui lavoro, ci sono Rackety, Padmi, AIball, Courtmaster e altre realtà più piccole. In fondo alla pagina trovi il mio calendario se vuoi fissare una chiacchierata.",
            ],
            [
                "3º <strong>Raccogli i pareri dei club e delle aziende, confronta, parlane con i soci del circolo e decidi.</strong> La vera decisione iniziale non è quale marca scegliere, ma capire <strong>se vuoi davvero installare le telecamere oppure no</strong>.",
            ],
            [
                'Come prima lettura ti consiglio questo articolo: <a href="../errores-clubs-se-arrepienten-de-poner-camaras/">I 3 errori dei club che si pentono di aver installato le telecamere</a>.',
            ],
        ],
    },
    "errores-clubs-se-arrepienten-de-poner-camaras": {
        "title": "I 3 errori dei club che si pentono di aver installato le telecamere",
        "blocks": [
            [
                "Sì, hai letto bene.",
                "E non parliamo di uno o due casi isolati.",
                "Passo le mie giornate a parlare con gestori di circoli di padel e questi <strong>3 errori si ripetono continuamente</strong>.",
                "So bene che investire nelle telecamere è una scelta su cui non vuoi sbagliare.",
                "Ti consiglio di leggere queste righe per capire il nostro punto di vista: qualunque cosa deciderai, lo farai con molta più consapevolezza.",
            ],
            [
                "Errore 1: Statistiche e analisi con Intelligenza Artificiale",
                "Sulla carta l'idea sembra fantastica, vero?",
                "Un'intelligenza artificiale che analizza la partita, conta quanti colpi fai e ti dice cosa migliorare.",
                "La realtà è che alla terza partita ti accorgi che <strong>la tua mappa di calore è identica a quella delle partite precedenti</strong>.",
                "E sapere la percentuale di rovesci tagliati con doppio effetto è un dato che non serve assolutamente a nulla al 99% dei giocatori amatoriali.",
            ],
            [
                "Mi dispiace vedere le cifre altissime che piccoli circoli di provincia pagano ogni mese per queste funzioni.",
                "<strong>Non è redditizio</strong> pagare quei canoni.",
                "È una follia.",
                "È pura logica.",
            ],
            [
                "Errore 2: Periodi di prova gratuita e vincoli di permanenza",
                "Fai molta attenzione ai cosiddetti periodi di prova gratuita.",
                "Occhio.",
                "Il meccanismo classico è sempre questo:",
            ],
            [
                "1º <strong>Durante il primo mese</strong> c'è l'effetto novità e tutti i giocatori provano il sistema.",
            ],
            [
                "2º <strong>Firmi un contratto pluriennale vincolante</strong> pensando che l'entusiasmo rimarrà identico tutto l'anno.",
            ],
            [
                "3º <strong>Quando l'effetto novità cala</strong>, tu continui a pagare canoni pesanti per anni.",
            ],
            [
                "<strong>Non ipotecare il tuo circolo</strong> con un vincolo di permanenza.",
            ],
            [
                "Errore 3: La maggior parte dei fornitori usa normali telecamere di videosorveglianza",
                "Il video finale sembra il filmato di una rapina in banca.",
                "La qualità dell'immagine è scarsa e poco fluida.",
                "Un ottimo indicatore per capire se sono telecamere di sorveglianza sono le linee del campo.",
                "Se le linee appaiono curve, <strong>brutto segno</strong>.",
            ],
            [
                "Quando faremo la demo online, ricordamelo e ti mostrerò la differenza in diretta.",
            ],
            [
                "ERRORE EXTRA: Te lo svelerò a voce durante la demo online.",
            ],
            [
                "Conclusione:",
                "Diversi circoli si pentono dei contratti e delle telecamere che hanno sottoscritto.",
            ],
            [
                "Insisto: non fidarti ciecamente dei commerciali o di chi, come me, lavora nel settore.",
                "<strong>Parla direttamente con i circoli</strong> che le usano già e fatti raccontare la loro esperienza reale.",
            ],
        ],
    },
    "camaras-de-padel-o-videovigilancia": {
        "title": "Come capire se le telecamere sono da padel o di semplice videosorveglianza?",
        "blocks": [
            [
                "Oltre alla nitidezza dell'immagine, che salta subito all'occhio, c'è un trucco semplicissimo per riconoscerle all'istante.",
                "<strong>Guardando le linee del campo</strong>.",
                "Una volta notato questo dettaglio, lo vedrai sempre.",
                "Ti mostro un esempio concreto.",
            ],
            [
                "In questa immagine si nota subito che le linee del campo da padel non sono dritte: <strong>sono visibilmente curve</strong>.",
                "Tutta l'inquadratura è deformata da una lente grandangolare economica a occhio di pesce.",
                "Questo è il marchio di fabbrica delle telecamere di videosorveglianza (CCTV).",
            ],
            [
                "Le linee del campo <strong>devono vedersi perfettamente dritte</strong>.",
                "Il più vicino possibile alle riprese televisive ufficiali del Premier Padel.",
            ],
        ],
    },
    "cuanto-cuesta-poner-camaras": {
        "title": "Quanto costa installare le telecamere nel mio circolo di padel?",
        "blocks": [
            [
                "Una delle prime domande che ti passerà per la testa è: quanto costa installare le telecamere Save My Play sui campi del mio circolo?",
                "Ecco la risposta chiara e trasparente, con il <strong>prezzo per campo</strong>.",
                "Si installa una sola telecamera per ogni campo.",
                "Sappiamo che è una decisione importante per il tuo club, quindi ecco tutti i numeri senza sorprese:",
            ],
            [
                "Abbiamo due piani mensili:",
                '<strong>Piano A: 136 € al mese.</strong> Include statistiche e analisi con IA. Non lo consiglio al 95% dei circoli (<a href="../por-que-no-recomiendo-plan-analytics/">Perché non consiglio il piano da 136 € al mese</a>).',
                "<strong>Piano B: 45 € al mese.</strong> Al costo di un paio d'ore di affitto campo al mese, hai una telecamera che registra partite complete, highlights automatici, dirette su YouTube e coaching tools... senza limiti.",
                "<strong>Senza alcun vincolo di permanenza.</strong>",
                "Se non vuoi continuare, annulli l'abbonamento Stripe con un clic quando vuoi. Nessun contratto vincolante.",
                "Non vogliamo clienti scontenti obbligati a restare: a lungo termine non conviene a nessuno.",
                "Eppure, <strong>il 97% dei circoli resta volontariamente con noi</strong> mese dopo mese.",
            ],
            [
                '<strong>Investimento iniziale per la telecamera di 180 €</strong>, una per campo (<a href="../inversion-inicial-camaras-180-euros/">Perché è previsto un investimento iniziale di 180 €?</a>).',
                "Zero lavori edili o scavi: si monta in 5 minuti con il solo Wi-Fi e una presa di corrente.",
                "Vista l'alta richiesta, la spedizione richiede circa 4 settimane. Gli oneri doganali sono di circa 20 €. Se rispetti alcuni semplici requisiti, il primo mese di abbonamento può essere gratuito.",
            ],
        ],
    },
    "inversion-inicial-camaras-180-euros": {
        "title": "Perché è previsto un investimento iniziale di 180 € per le telecamere?",
        "blocks": [
            [
                "So che <strong>questi 180 € iniziali sono una delle obiezioni più frequenti</strong> che ricevo dai circoli.",
                "È una cifra concreta, soprattutto quando altri fornitori pubblicizzano hardware 'gratuito'. Per aiutarti a prendere la decisione migliore, ti spiego esattamente il motivo.",
            ],
            [
                "La ragione principale è che <strong>produciamo noi stessi le nostre telecamere</strong>.",
                'Non è affatto la norma nel settore. Di solito si comprano telecamere di videosorveglianza prodotte in serie in Cina perché costano pochissimo (<a href="../camaras-de-padel-o-videovigilancia/">in questo articolo ti mostro come distinguerle</a>). Noi invece le progettiamo e produciamo a Chicago e in California.',
                "La qualità video non ha paragoni. I giocatori vogliono condividere i loro punti migliori su Instagram e WhatsApp: non puoi offrirgli una qualità che sembri <strong>il filmato di una rapina in banca</strong>.",
            ],
            [
                "Produrre ogni singola unità ci costa <strong>molto più di 180 €</strong>.",
                "Vendiamo la telecamera in perdita all'inizio e recuperiamo l'investimento nel tempo grazie al canone mensile. 180 € è il prezzo d'ingresso per avere un'ottica sportiva dedicata.",
                "Se non chiedessimo questo contributo iniziale, dovremmo alzare drasticamente il canone mensile per sostenere la produzione. E nel medio periodo pagheresti molto di più, perché la vera spesa per un circolo sono i canoni mensili ricorrenti. Ecco perché <strong>i nostri canoni mensili sono i più competitivi possibili</strong>.",
            ],
        ],
    },
    "es-caro-save-my-play": {
        "title": "Save My Play è costoso?",
        "blocks": [
            [
                "È una domanda legittima che molti gestori mi pongono. Ecco come la vedo.",
                "Innanzitutto, <strong>non è un prodotto pensato per il 100% dei circoli</strong>. È un servizio premium che differenzia il tuo club. Non cerchiamo di essere ovunque a tutti i costi, e proprio questa esclusività dà valore ai club che lo installano.",
            ],
            [
                "Confrontiamolo ora con gli altri fornitori. Il piano da 136 €/mese con statistiche IA è in linea con la media del mercato, ma non lo consigliamo alla maggior parte dei club.",
                "Il <strong>piano da 45 € al mese</strong> per campo, invece, è uno dei prezzi migliori che troverai in Europa. Qualche nuova startup in fase di test può offrire sconti temporanei per trovare i primi clienti, ma tra le aziende consolidate è difficile trovare un rapporto qualità-prezzo simile.",
                "In ogni caso, confronta sempre. <strong>Il prezzo non è tutto</strong>: valuta la qualità dell'immagine, l'assenza di vincoli contrattuali e la semplicità per i giocatori.",
            ],
        ],
    },
    "es-rentable-poner-camaras": {
        "title": "È redditizio installare telecamere sui miei campi da padel?",
        "blocks": [
            [
                "Sappiamo bene che i circoli valutano ogni spesa con la lente d'ingrandimento. Vuoi capire se installare le telecamere nel tuo club sia davvero un investimento redditizio. Ecco la nostra opinione sincera.",
            ],
            [
                "Prima di tutto, ti diciamo con totale trasparenza che il piano da 136 €/mese con analisi IA <strong>non è consigliato per il 90% dei circoli</strong> perché difficilmente si ripaga da solo.",
            ],
            [
                "Al contrario, con il piano da 45 €/mese più i 180 € della telecamera, ecco i 4 vantaggi concreti che generano ritorno economico:",
            ],
            [
                "1º <strong>Valore differenziale rispetto ai circoli della zona:</strong> offri un servizio moderno che attira nuovi giocatori e aumenta le prenotazioni, posizionando il tuo centro come il club più innovativo.",
            ],
            [
                "2º <strong>Contenuti online e visibilità:</strong> puoi inserire il logo del tuo circolo e dei tuoi sponsor su ogni video. I giocatori condividono i punti sui social e su WhatsApp, facendoti pubblicità organica gratuita ogni giorno.",
            ],
            [
                "3º <strong>Registrazione di tornei e lezioni:</strong> un valore aggiunto enorme per i tornei del weekend e per i maestri della scuola padel con tablet in campo.",
            ],
            [
                "4º <strong>Monetizzazione diretta:</strong> basta applicare <strong>0,50 € in più a prenotazione campo</strong> per ripagare interamente il sistema (45 € al mese equivalgono a soli 1,50 € al giorno per campo).",
            ],
        ],
    },
    "por-que-no-recomiendo-plan-analytics": {
        "title": "Perché non consiglio il piano da 136 € al mese al 95% dei circoli?",
        "blocks": [
            [
                'Se hai letto il nostro articolo sui <a href="../errores-clubs-se-arrepienten-de-poner-camaras/">3 errori che commettono i club</a>, il motivo <strong>dovrebbe essere piuttosto chiaro</strong>.',
                "Per il 95% dei circoli, pagare 136 € ogni mese per grafici e mappe di calore IA che gli amatori guardano due volte per curiosità prima di stancarsi non è un investimento sostenibile.",
            ],
        ],
    },
    "que-pasa-si-cancelo": {
        "title": "Cosa succede se disdico l'abbonamento? Le telecamere restano a me?",
        "blocks": [
            [
                "Questa è una domanda molto frequente che mi fanno i gestori dei circoli.",
            ],
            [
                'Per darti tutto il contesto: come spiegato nell\'articolo sull\'<a href="../inversion-inicial-camaras-180-euros/">investimento iniziale di 180 €</a>, produciamo noi stessi le telecamere da padel. Una telecamera per campo. <strong>Non abbiamo alcun vincolo di permanenza</strong>: nessun contratto bloccante, puoi disdire quando vuoi.',
            ],
            [
                "E cosa succede se decidi di annullare l'abbonamento?",
                "Sì, <strong>le telecamere sono tue e restano a te</strong>. Tuttavia funzionano esclusivamente con il nostro software cloud, quindi non possono essere riutilizzate con altri sistemi.",
            ],
            [
                "Acquistare una telecamera e disdire dopo un mese <strong>è un fallimento sia per te che per noi</strong>. Tu perdi 180 €, e noi perdiamo denaro perché produrle ci costa molto più di 180 €. Per questo consigliamo sempre di iniziare provando su uno o due campi prima di attrezzare tutto il circolo.",
            ],
            [
                "Ed è proprio così che otteniamo che <strong>il 97% dei circoli resti volontariamente con noi</strong> ogni mese.",
            ],
        ],
    },
    "como-montar-camara-save-my-play": {
        "title": "Quanto tempo ci vuole per montare una telecamera Save My Play?",
        "blocks": [
            [
                "<strong>10 minuti.</strong>",
                "Una scala, <strong>il Wi-Fi e una presa di corrente</strong>. Non serve letteralmente nient'altro per installare la telecamera.",
                "La telecamera si fissa alla griglia o al palo a 4 metri di altezza stringendo un semplice dado. Si collega il cavo alla presa elettrica e la configurazione Wi-Fi richiede due minuti.",
            ],
            [
                "C'è anche l'alternativa di collegarla via cavo Ethernet al router. Se hai già il cavo tirato fino al campo, ottimo. Altrimenti non vale la pena spendere soldi in lavori: <strong>la stragrande maggioranza dei circoli usa il Wi-Fi senza problemi</strong>.",
            ],
        ],
    },
    "problemas-con-las-camaras": {
        "title": "Cosa succede se ci sono problemi tecnici con le telecamere?",
        "blocks": [
            [
                "Finché vengono utilizzate correttamente in campo, <strong>ci assumiamo la piena responsabilità</strong> di qualsiasi problema tecnico possa sorgere.",
                "Lavoriamo con oltre 1.500 circoli in tutto il mondo, in paesi con condizioni climatiche estreme. Le telecamere sono super collaudate. Se dovesse verificarsi un guasto, <strong>ovviamente non ti addebiteremo nulla durante quel periodo</strong> e interverremo subito per risolverlo o sostituire l'unità.",
            ],
        ],
    },
    "que-son-las-coaching-tools": {
        "title": "Cosa sono le coaching tools?",
        "blocks": [
            [
                "Le <strong>coaching tools</strong> sono lo strumento pensato per permettere ai maestri di padel di sfruttare davvero le telecamere durante le lezioni della scuola.",
            ],
            [
                "Invece di aspettare la fine della partita, l'istruttore ha un tablet collegato in diretta al campo.",
                "Può mettere in pausa il punto appena giocato dall'allievo, tornare indietro al rallentatore e mostrargli <strong>all'istante cosa ha fatto bene o dove ha sbagliato posizione</strong>.",
            ],
            [
                "Direttamente sullo schermo del tablet, il maestro può <strong>disegnare linee di traiettoria, angoli di racchetta e zone di rimbalzo</strong>, registrando tutto con la propria voce.",
            ],
            [
                "A fine lezione, l'allievo riceve un link diretto su WhatsApp o via email con i 3 o 4 clip commentati dal maestro.",
                "È un modo straordinario per <strong>differenziare la tua scuola padel da quella dei circoli vicini</strong> e fidelizzare gli allievi.",
            ],
        ],
    },
    "camaras-en-exterior-lluvia-nieve-viento": {
        "title": "Le telecamere resistono sui campi all'aperto (pioggia, neve, vento)?",
        "blocks": [
            [
                "Produciamo un unico modello di telecamera progettato per <strong>resistere a qualsiasi condizione atmosferica</strong>.",
                "<strong>Vento forte, neve, pioggia battente, sole e pallate dirette.</strong> Nasce per i campi outdoor ed è quindi perfetta sia all'aperto che sui campi indoor.",
            ],
        ],
    },
    "como-ver-highlights-sin-app": {
        "title": "Perché non c'è un'app Save My Play? Come vedo i miei highlights?",
        "blocks": [
            [
                "L'ultima cosa che un giocatore vuole fare un minuto prima di entrare in campo è scaricare un'app e registrarsi. E se dentro il club c'è poco campo? Perché tutti la usino davvero, l'esperienza deve essere immediata. Ecco come funziona:",
            ],
            [
                "1º <strong>Inquadrare il codice QR</strong> all'ingresso del campo.",
            ],
            [
                "2º <strong>Premere il pulsante rosso</strong> per avviare la registrazione dell'intera partita.",
            ],
            [
                "3º <strong>Inserire i dati essenziali:</strong> email, durata della partita, eventuale diretta YouTube o taglio automatico dei tempi morti con IA.",
            ],
            [
                "4º <strong>Alzare le braccia guardando la telecamera</strong> dopo ogni bel punto (o premere il pulsante verde sul palo) per salvare l'highlight.",
            ],
            [
                "5º <strong>Ricevere un'email circa un'ora dopo la fine</strong> con la partita intera e i punti salvati pronti da scaricare e condividere—<strong>senza dover scaricare alcuna app</strong>.",
            ],
        ],
    },
    "mejores-empresas-camaras-padel-espana": {
        "title": "Quali sono le migliori aziende di telecamere da padel in Spagna e in Europa?",
        "blocks": [
            [
                'Oggi in Spagna e in Europa operano diverse aziende di telecamere per campi da padel (<a href="../por-que-no-conocia-save-my-play/">qui ti spiego perché forse non avevi mai sentito parlare di Save My Play</a>).',
            ],
            [
                "Ogni azienda ha la propria <strong>visione specifica</strong> del mercato, puntando su tecnologie e modelli di business differenti. Per questo ti consiglio sempre di parlare con ciascun fornitore, ascoltare e confrontare—e soprattutto di chiedere un parere ai circoli che le usano già.",
            ],
            [
                "<strong>Padmi:</strong> è l'azienda con più campi in Spagna (82 campi in 56 club), con due telecamere per campo. Puntano molto sulle statistiche IA oltre agli highlights, hanno un'immagine di marca molto curata e sono partner dell'Adidas Padel Tour.",
            ],
            [
                "<strong>Aiball:</strong> presente in diversi club spagnoli, si concentra sulle statistiche IA e su un sistema oggettivo di livellamento dei giocatori. La giocatrice professionista Ari Sánchez è socia del progetto, premiato come Miglior Startup al Padel World Summit 2025.",
            ],
            [
                "<strong>Rackety:</strong> presente in circa 50 club, unisce la trasmissione delle partite e le statistiche IA a un software gestionale di prenotazione campi e chatbot WhatsApp.",
            ],
        ],
    },
    "por-que-no-conocia-save-my-play": {
        "title": "Perché non avevo mai sentito parlare di Save My Play?",
        "blocks": [
            [
                "Siamo un'<strong>azienda americana</strong>.",
                "Negli Stati Uniti e nel resto del mondo molti circoli installano telecamere su tutti i loro campi fin dal primo giorno, e <strong>abbiamo dato priorità a quei mercati</strong>.",
                "Oggi siamo presenti su oltre <strong>1.500 campi di club</strong> in tutto il mondo tra padel, tennis e pickleball.",
            ],
        ],
    },
    "save-my-play-en-pocas-palabras": {
        "title": "Save My Play in poche parole: chi siamo e cosa facciamo",
        "blocks": [
            [
                "Sarò il più breve possibile.",
                "Siamo installati su oltre <strong>1.600 campi in tutto il mondo</strong>.",
                "La Federazione Americana di Padel (USPA) ci ha scelto per registrare i suoi tornei ufficiali FIP, e ogni weekend trasmettiamo in diretta su oltre 100 campi per la Federazione Americana di Tennis (USTA).",
            ],
            [
                "Nonostante questi numeri, <strong>siamo un team snello di meno di 10 persone</strong>.",
                "Ed è proprio questo che i circoli apprezzano di più: <strong>la vicinanza</strong>. Se qualcosa non va, parli direttamente con noi e risolviamo subito il problema senza passaggi burocratici.",
            ],
            [
                "Inoltre non complichiamo le cose inutilmente: se con <strong>due pulsanti</strong> le telecamere funzionano alla perfezione, non ne mettiamo tre.",
            ],
        ],
    },
    "por-que-coolpadel-colabora-con-save-my-play": {
        "title": "Perché CoolPadel collabora con Save My Play?",
        "blocks": [
            [
                "La parte che preferisco del lavorare nel mondo del padel è partecipare alle fiere di settore e confrontarmi con tutte le aziende.",
                "Conoscendo bene il mercato, ritengo che Save My Play sia l'azienda con il <strong>maggior potenziale in assoluto</strong>—e, cosa altrettanto importante, <strong>sono persone serie e affidabili</strong>.",
                "Vista l'enorme richiesta globale, in CoolPadel <strong>gestiamo direttamente i circoli in Europa</strong>: Italia, Spagna, Francia, Regno Unito, Germania...",
            ],
        ],
    },
    "he-comprado-camaras-que-pasa-ahora": {
        "title": "Ho acquistato le telecamere Save My Play. Qual è il processo adesso?",
        "blocks": [
            [
                "1º <strong>Pagamento tramite Stripe:</strong> ti invio il link di pagamento. La transazione avviene in dollari poiché siamo un'azienda statunitense (pagare in dollari tramite la tua banca evita commissioni di cambio extra).",
            ],
            [
                "2º <strong>Registrazione dell'account del circolo:</strong> ricevi il link per creare il tuo profilo Save My Play e le telecamere vengono associate automaticamente al tuo club.",
            ],
            [
                "3º <strong>Produzione e spedizione:</strong> in circa 4 settimane le telecamere arrivano al tuo circolo.",
            ],
            [
                "4º <strong>Ricezione e attivazione:</strong> alla consegna si saldano circa 20 € di oneri doganali, monti le telecamere in 10 minuti e l'abbonamento mensile parte solo da quando le metti effettivamente in funzione.",
            ],
        ],
    },
    "por-que-no-me-interesa-venderte-una-camara": {
        "title": "Perché non mi interessa venderti una telecamera se non sei convinto?",
        "blocks": [
            [
                "Se ti vendo una telecamera a 180 €, la provi senza convinzione e disdici dopo un mese, <strong>abbiamo perso tutti</strong>.",
                "Tu perdi 180 € e tempo, e noi perdiamo denaro perché produrla ci costa molto più di 180 €. Vogliamo lavorare solo con circoli convinti che cercano una collaborazione duratura.",
            ],
        ],
    },
}

DE_ARTICLES_DATA = {
    "por-donde-empezar-si-estoy-pensando-en-poner-camaras": {
        "title": "Ich überlege, Kameras in meinem Club zu installieren – wo fange ich an?",
        "blocks": [
            [
                "Ich verstehe vollkommen, wenn Sie sich am Anfang etwas orientierungslos fühlen.",
                "Wahrscheinlich haben Sie gesehen, dass andere Padel-Clubs Kameras auf ihren Plätzen installieren, und fragen sich nun, ob Sie das auch tun sollten.",
                "Zunächst einmal <strong>empfehle ich Ihnen, vorsichtig zu sein</strong>.",
                "Nur weil viele es machen, heißt das noch lange nicht, dass es automatisch die beste Entscheidung für Ihren Club ist.",
            ],
            [
                "So würde ich an Ihrer Stelle vorgehen:",
            ],
            [
                "1º <strong>Sprechen Sie mit Clubs, die bereits Kameras installiert haben.</strong> Idealerweise mit Anlagen in einer anderen Region, damit keine direkte Konkurrenz besteht und man Ihnen ehrlich die Wahrheit sagt. Auf den Websites der Anbieter finden Sie meist Referenzclubs.",
            ],
            [
                "2º <strong>Sprechen Sie mit verschiedenen Kamera-Anbietern</strong> und hören Sie sich deren Konzepte an. In Spanien und Europa gibt es neben Save My Play (mit denen ich arbeite) unter anderem Rackety, Padmi, AIball und Courtmaster. Unten auf der Seite finden Sie meinen Kalender, falls Sie unverbindlich sprechen möchten.",
            ],
            [
                "3º <strong>Vergleichen Sie die Aussagen der Clubs und der Anbieter, besprechen Sie alles intern im Club und entscheiden Sie dann.</strong> Die erste Frage lautet nicht, welche Marke Sie kaufen, sondern <strong>ob Sie überhaupt Kameras installieren möchten oder nicht</strong>.",
            ],
            [
                'Als erste Lektüre empfehle ich Ihnen diesen Artikel: <a href="../errores-clubs-se-arrepienten-de-poner-camaras/">Die 3 Fehler von Clubs, die die Installation von Kameras bereuen</a>.',
            ],
        ],
    },
    "errores-clubs-se-arrepienten-de-poner-camaras": {
        "title": "Die 3 Fehler von Clubs, die die Installation von Kameras bereuen",
        "blocks": [
            [
                "Ja, Sie haben richtig gelesen.",
                "Und es handelt sich nicht um Einzelfälle.",
                "Ich spreche täglich mit Padel-Club-Betreibern, und diese <strong>3 Fehler wiederholen sich immer und immer wieder</strong>.",
                "Ich weiß, dass die Investition in Platzkameras eine Entscheidung ist, bei der man keinen teuren Fehler machen möchte.",
                "Nehmen Sie sich kurz Zeit, unsere Sichtweise zu lesen – wie auch immer Sie sich danach entscheiden, Sie treffen eine fundiertere Wahl.",
            ],
            [
                "Fehler 1: KI-Analysen und Schlagstatistiken",
                "Die Idee klingt auf dem Papier großartig, oder?",
                "Eine KI analysiert das Match, zählt jeden Schlag und sagt dem Spieler, was er verbessern muss.",
                "Die Realität sieht so aus: Spätestens beim dritten Match merkt man, dass <strong>die eigene Heatmap fast genauso aussieht wie in den Spielen zuvor</strong>.",
                "Und die genaue Quote geschnittener Vorhände mit doppeltem Drall bringt 99 % der Freizeitspieler keinerlei echten Mehrwert.",
            ],
            [
                "Es tut mir ehrlich leid zu sehen, welche hohen Monatspreise kleine Clubs für solche KI-Statistikpakete zahlen.",
                "<strong>Es ist schlichtweg nicht rentabel</strong>, diese Preise zu zahlen.",
                "Das rechnet sich nicht.",
                "Das ist gesunder Menschenverstand.",
            ],
            [
                "Fehler 2: Kostenlose Testphasen und lange Vertragsbindungen",
                "Seien Sie äußerst vorsichtig bei kostenlosen Probemonaten.",
                "Wirklich.",
                "Die klassische Falle läuft fast immer so ab:",
            ],
            [
                "1º <strong>Im ersten Monat</strong> ist alles neu und viele Spieler probieren die Kameras neugierig aus.",
            ],
            [
                "2º <strong>Sie unterschreiben einen mehrjährigen Knebelvertrag</strong>, weil Sie glauben, die Nutzung bleibt dauerhaft so hoch.",
            ],
            [
                "3º <strong>Sobald der erste Hype nachlässt</strong>, zahlen Sie trotzdem jahrelang jeden Monat weiter.",
            ],
            [
                "<strong>Binden Sie Ihren Club niemals</strong> an lange Mindestvertragslaufzeiten.",
            ],
            [
                "Fehler 3: Die meisten Anbieter nutzen einfache Überwachungskameras",
                "Das fertige Video sieht dann aus wie die Überwachungsaufnahme eines Banküberfalls.",
                "Die Bildqualität ist schwach und verzerrt.",
                "Ein klarer Indikator für Überwachungskameras sind die Linien des Padel-Platzes.",
                "Wenn die Platzlinien gekrümmt sind, ist das <strong>ein schlechtes Zeichen</strong>.",
            ],
            [
                "Erinnern Sie mich in unserer Online-Demo gerne daran, dann zeige ich Ihnen den Unterschied im direkten Vergleich.",
            ],
            [
                "EXTRA-FEHLER: Diesen Punkt verrate ich Ihnen persönlich während unserer Online-Demo.",
            ],
            [
                "Fazit:",
                "Einige Clubs bereuen die Verträge und Kamerasysteme, für die sie sich entschieden haben.",
            ],
            [
                "Ich betone es immer wieder: Glauben Sie nicht blind Vertrieblern oder Leuten wie mir.",
                "<strong>Sprechen Sie direkt mit den Clubs</strong>, die bereits Kameras nutzen, und lassen Sie sich deren echte Erfahrungen schildern.",
            ],
        ],
    },
    "camaras-de-padel-o-videovigilancia": {
        "title": "Wie erkenne ich, ob meine Kameras echte Padel-Kameras oder Überwachungskameras sind?",
        "blocks": [
            [
                "Abgesehen von der offensichtlichen Bildschärfe gibt es einen ganz einfachen Trick, um den Unterschied sofort zu erkennen.",
                "<strong>Achten Sie auf die Linien des Padel-Platzes</strong>.",
                "Sobald Sie dieses Detail einmal gesehen haben, fällt es Ihnen jedes Mal sofort auf.",
                "Ich zeige Ihnen ein konkretes Beispiel.",
            ],
            [
                "Auf diesem Bild sieht man sofort, dass die Linien des Platzes nicht gerade sind: <strong>sie sind deutlich gekrümmt</strong>.",
                "Das gesamte Bild wird durch ein billiges Fisheye-Weitwinkelobjektiv verzerrt.",
                "Das ist das typische Merkmal gewöhnlicher CCTV-Überwachungskameras.",
            ],
            [
                "Die Linien des Padel-Platzes <strong>sollten immer gerade aussehen</strong>.",
                "So nah wie möglich an einer offiziellen TV-Übertragung von Premier Padel.",
            ],
        ],
    },
    "cuanto-cuesta-poner-camaras": {
        "title": "Was kostet die Installation von Kameras in meinem Padel-Club?",
        "blocks": [
            [
                "Eine der ersten Fragen, die Ihnen durch den Kopf geht, lautet sicher: Was kostet es konkret, Save My Play-Kameras auf den Plätzen meines Clubs zu installieren?",
                "Hier ist die transparente Antwort – <strong>Preis pro Padel-Platz</strong>.",
                "Pro Platz wird nur eine einzige Kamera benötigt.",
                "Wir wissen, dass Sie diese Investition genau kalkulieren müssen. Deshalb nennen wir Ihnen hier alle Zahlen offen und ohne Kleingedrucktes:",
            ],
            [
                "Wir bieten zwei monatliche Tarife an:",
                '<strong>Plan A: 136 € pro Monat.</strong> Inklusive KI-Statistiken und Heatmaps. Ich empfehle diesen Tarif 95 % der Clubs ausdrücklich nicht (<a href="../por-que-no-recomiendo-plan-analytics/">Warum ich den 136-€-Tarif nicht empfehle</a>).',
                "<strong>Plan B: 45 € pro Monat.</strong> Für den Gegenwert von ein bis zwei Platzbuchungen im Monat erhalten Sie eine Kamera für komplette Match-Aufnahmen, automatische Highlights, YouTube-Livestreams und Coaching-Tools... unbegrenzt.",
                "<strong>Ohne jegliche Mindestvertragslaufzeit.</strong>",
                "Wenn Sie nicht weitermachen möchten, kündigen Sie das Stripe-Abo jederzeit mit einem Klick. Kein Knebelvertrag.",
                "Wir wollen keine unzufriedenen Kunden, die nur wegen eines Vertrags bleiben – das bringt langfristig niemandem etwas.",
                "Trotzdem <strong>bleiben 97 % der Clubs jeden Monat freiwillig bei uns</strong>.",
            ],
            [
                '<strong>Einmalige Anfangsinvestition für die Kamera von 180 €</strong> pro Platz (<a href="../inversion-inicial-camaras-180-euros/">Warum gibt es eine Anfangsinvestition von 180 €?</a>).',
                "Ohne Bauarbeiten: Die Kamera ist in 5 Minuten montiert – Sie brauchen nur WLAN und eine Steckdose.",
                "Aufgrund der hohen Nachfrage beträgt die Lieferzeit aktuell etwa 4 Wochen. Hinzu kommen rund 20 € Zollgebühren. Wenn Ihr Club bestimmte Voraussetzungen erfüllt, kann der erste Beitragsmonat kostenlos sein.",
            ],
        ],
    },
    "inversion-inicial-camaras-180-euros": {
        "title": "Warum gibt es eine Anfangsinvestition von 180 € für die Kameras?",
        "blocks": [
            [
                "Ich weiß, dass <strong>diese einmaligen 180 € eine der häufigsten Fragen</strong> sind, die mir Clubs stellen.",
                "Es ist ein spürbarer Betrag, zumal manche Mitbewerber mit vermeintlich 'kostenloser Hardware' werben. Damit Sie die beste Entscheidung treffen können, erkläre ich Ihnen offen den Hintergrund.",
            ],
            [
                "Der Hauptgrund ist, dass <strong>wir unsere Kameras selbst herstellen</strong>.",
                'Das ist in der Branche alles andere als selbstverständlich. Üblicherweise werden günstige Überwachungskameras aus chinesischer Massenproduktion verwendet (<a href="../camaras-de-padel-o-videovigilancia/">in diesem Artikel zeige ich Ihnen, wie Sie den Unterschied erkennen</a>). Wir fertigen unsere Kameras in Chicago und Kalifornien.',
                "Die Bildqualität ist ein Unterschied wie Tag und Nacht. Spieler möchten ihre besten Ballwechsel auf Instagram und WhatsApp teilen – da darf das Video nicht aussehen wie <strong>die Überwachungsaufnahme eines Banküberfalls</strong>.",
            ],
            [
                "Die Herstellung kostet uns <strong>deutlich mehr als 180 € pro Kamera</strong>.",
                "Wir geben die Hardware beim Kauf unter Herstellungskosten ab und amortisieren die Differenz über die Laufzeit. 180 € sind der faire Einstiegspreis für echte Sportoptik.",
                "Würden wir die Kameras für 0 € verschenken, müssten wir die monatlichen Gebühren massiv erhöhen, um liquide zu bleiben. Auf Dauer käme Sie das viel teurer, denn der größte Kostenblock entsteht über die monatlichen Raten. Genau deshalb <strong>sind unsere Monatsgebühren so wettbewerbsfähig wie möglich</strong>.",
            ],
        ],
    },
    "es-caro-save-my-play": {
        "title": "Ist Save My Play teuer?",
        "blocks": [
            [
                "Das ist eine absolut berechtigte Frage. Hier ist meine ehrliche Einschätzung.",
                "Erstens ist das System <strong>kein Produkt für 100 % aller Clubs</strong>. Es ist ein Premium-Service, mit dem Sie sich abheben. Wir müssen nicht in jedem Club vertreten sein – genau das macht den Mehrwert für unsere Partnerclubs aus.",
            ],
            [
                "Vergleichen wir die Preise mit dem Markt: Unser KI-Statistik-Tarif für 136 €/Monat liegt im Marktdurchschnitt, wird von uns aber den meisten Clubs gar nicht empfohlen.",
                "Unser <strong>Tarif für 45 € pro Monat</strong> hingegen gehört zu den besten Konditionen auf dem Markt. Manche ganz neuen Startups bieten in ihrer Testphase zwar Lockangebote an, aber unter etablierten Anbietern mit ausgereifter Hardware ist dieses Preis-Leistungs-Verhältnis kaum zu schlagen.",
                "Vergleichen Sie in Ruhe. <strong>Der Preis ist nicht alles</strong>: Achten Sie auf die Bildqualität, die Vertragsfreiheit und darauf, wie einfach das System für Ihre Spieler ist.",
            ],
        ],
    },
    "es-rentable-poner-camaras": {
        "title": "Lohnt es sich wirtschaftlich, Kameras auf meinen Padel-Plätzen zu installieren?",
        "blocks": [
            [
                "Wir wissen, dass Clubs jede Ausgabe genau prüfen. Sie möchten wissen, ob sich Kameras auf Ihren Plätzen finanziell rechnen. Hier ist unsere ehrliche Meinung.",
            ],
            [
                "Vorweg ganz offen: Unseren 136-€-Tarif mit KI-Statistiken <strong>empfehlen wir 90 % der Clubs nicht</strong>, weil sich dieser Aufpreis im normalen Cluballtag selten direkt amortisiert.",
            ],
            [
                "Beim Tarif für 45 €/Monat (plus 180 € einmalig für die Kamera) gibt es vier klare Hebel, über die Clubs ihre Investition zurückspielen:",
            ],
            [
                "1º <strong>Alleinstellungsmerkmal in Ihrer Region:</strong> Sie bieten einen modernen Premium-Service. Spieler buchen gezielt bei Ihnen, um ihre Matches aufzunehmen – das steigert die Auslastung und stärkt Ihr Image als innovativer Club.",
            ],
            [
                "2º <strong>Organische Reichweite in sozialen Netzwerken:</strong> Sie können das Logo Ihres Clubs und lokaler Sponsoren fest im Video einblenden. Spieler teilen ihre Highlights begeistert auf Instagram und WhatsApp und machen so täglich kostenlose Werbung für Ihren Club.",
            ],
            [
                "3º <strong>Turniere und Training:</strong> Livestreams auf YouTube bei Clubturnieren und das direkte Video-Feedback per Tablet im Training bieten einen enormen Mehrwert.",
            ],
            [
                "4º <strong>Direkte Monetarisierung:</strong> Einige Clubs erheben einen kleinen Aufschlag. Schon mit <strong>0,50 € mehr pro Platzbuchung</strong> trägt sich das System von selbst (45 € im Monat entsprechen nur 1,50 € pro Tag und Platz).",
            ],
        ],
    },
    "por-que-no-recomiendo-plan-analytics": {
        "title": "Warum empfehle ich den 136-€-Monatstarif 95 % der Clubs nicht?",
        "blocks": [
            [
                'Wenn Sie unseren Artikel über <a href="../errores-clubs-se-arrepienten-de-poner-camaras/">die 3 häufigsten Fehler von Clubs</a> gelesen haben, <strong>sollte der Grund klar sein</strong>.',
                "Für 95 % der Anlagen lohnt es sich schlichtweg nicht, jeden Monat 136 € für KI-Heatmaps und Schlagstatistiken zu zahlen, die Freizeitspieler zweimal neugierig anschauen und danach kaum noch nutzen.",
            ],
        ],
    },
    "que-pasa-si-cancelo": {
        "title": "Was passiert, wenn ich mein Abonnement kündige? Behalte ich die Kameras?",
        "blocks": [
            [
                "Das ist eine sehr häufige und berechtigte Frage von Clubbetreibern.",
            ],
            [
                'Kurz zum Hintergrund: Wie im Artikel über <a href="../inversion-inicial-camaras-180-euros/">die Anfangsinvestition von 180 €</a> erklärt, fertigen wir unsere Padel-Kameras selbst. Eine Kamera pro Platz. <strong>Wir haben keinerlei Mindestvertragslaufzeit</strong> – es ist ein flexibles Monatsabo, das Sie jederzeit kündigen können.',
            ],
            [
                "Und was passiert, wenn Sie kündigen?",
                "Ja, <strong>die Kameras gehören Ihnen und Sie behalten sie</strong>. Da sie jedoch speziell für unsere Cloud-Software entwickelt wurden, lassen sie sich nicht mit Fremdsystemen weiterverwenden.",
            ],
            [
                "Eine Kamera zu kaufen und nach einem Monat zu kündigen, <strong>ist für Sie und für uns ein Misserfolg</strong>. Sie verlieren 180 €, und wir legen drauf, weil uns die Produktion deutlich mehr als 180 € kostet. Deshalb raten wir immer dazu, erst auf einem Platz zu starten und das System in Ruhe zu testen.",
            ],
            [
                "Genau dank dieser Offenheit <strong>bleiben 97 % der Clubs jeden Monat freiwillig bei uns</strong>.",
            ],
        ],
    },
    "como-montar-camara-save-my-play": {
        "title": "Wie lange dauert die Montage einer Save My Play-Kamera?",
        "blocks": [
            [
                "<strong>10 Minuten.</strong>",
                "Eine Leiter, <strong>WLAN und eine normale Steckdose</strong>. Mehr brauchen Sie für die Montage einer Kamera nicht.",
                "Die Kamera wird mit einer Feststellmutter direkt am 4-Meter-Gitter oder Pfosten befestigt. Anschließend stecken Sie das Stromkabel in die Steckdose und verbinden die Kamera kinderleicht mit dem WLAN.",
            ],
            [
                "Alternativ können Sie die Kamera auch per Netzwerkkabel (Ethernet) mit dem Router verbinden. Wenn bereits ein Kabel am Platz liegt, perfekt. Falls nicht, lohnen sich teure Verlegearbeiten kaum: <strong>Die allermeisten Clubs nutzen problemlos WLAN</strong>.",
            ],
        ],
    },
    "problemas-con-las-camaras": {
        "title": "Was passiert, wenn technische Probleme mit den Kameras auftreten?",
        "blocks": [
            [
                "Solange Sie ordentlich mit der Hardware umgehen, <strong>übernehmen wir die volle Verantwortung</strong> für alle technischen Probleme.",
                "Wir arbeiten weltweit mit über 1.500 Clubs unter verschiedensten klimatischen Bedingungen zusammen. Sollte dennoch einmal ein Defekt auftreten, <strong>berechnen wir Ihnen für diese Ausfallzeit selbstverständlich keine Gebühren</strong> und kümmern uns schnellstmöglich um die Behebung oder den Austausch.",
            ],
        ],
    },
    "que-son-las-coaching-tools": {
        "title": "Was sind die Coaching-Tools?",
        "blocks": [
            [
                "Die <strong>Coaching-Tools</strong> wurden entwickelt, damit Padel-Trainer während des Unterrichts auf dem Platz einen echten Mehrwert aus den Kameras ziehen können.",
            ],
            [
                "Statt bis zum Ende der Trainerstunde zu warten, ist der Coach mit einem Tablet live mit der Platzkamera verbunden.",
                "Er kann den gerade gespielten Ballwechsel pausieren, zurückspulen und dem Schüler <strong>sofort auf dem Platz zeigen, was gut war oder wo der Stellungsfehler lag</strong>.",
            ],
            [
                "Direkt auf dem Tablet-Bildschirm kann der Trainer <strong>Laufwege, Schlagwinkel und Zielzonen einzeichnen</strong>, während seine gesprochene Erklärung live mitaufgezeichnet wird.",
            ],
            [
                "Nach dem Training erhält der Schüler per WhatsApp oder E-Mail einen direkten Link mit den 3 bis 4 kommentierten Videoclips seines Trainers.",
                "Das ist eine erstklassige Möglichkeit, <strong>Ihre Padel-Schule von anderen Clubs abzuheben</strong> und ambitionierte Spieler langfristig zu binden.",
            ],
        ],
    },
    "camaras-en-exterior-lluvia-nieve-viento": {
        "title": "Halten die Kameras auf Außenplätzen (Regen, Schnee, Wind) stand?",
        "blocks": [
            [
                "Wir bauen ein einziges, extrem robustes Kameramodell, das <strong>jeder Witterung standhält</strong>.",
                "<strong>Sturm, Schnee, Starkregen, Hitze und direkte Balltreffer.</strong> Das Gehäuse ist speziell für Outdoor-Plätze konzipiert und funktioniert damit sowohl im Freien als auch in der Halle absolut zuverlässig.",
            ],
        ],
    },
    "como-ver-highlights-sin-app": {
        "title": "Warum gibt es keine Save My Play-App? Wie sehe ich meine Highlights?",
        "blocks": [
            [
                "Das Letzte, was ein Spieler eine Minute vor Matchbeginn tun möchte, ist eine App herunterzuladen. Was, wenn der Empfang in der Halle schwach ist? Damit wirklich jeder das System nutzt, muss es kinderleicht sein. So funktioniert der Ablauf:",
            ],
            [
                "1º <strong>QR-Code scannen</strong> direkt am Platzeingang.",
            ],
            [
                "2º <strong>Roten Knopf drücken</strong>, um die Aufnahme des gesamten Matches zu starten.",
            ],
            [
                "3º <strong>Kurze Angaben eintragen:</strong> E-Mail-Adresse, Spielzeit, optionaler YouTube-Livestream oder automatischer KI-Zuschnitt der Pausen.",
            ],
            [
                "4º <strong>Nach jedem starken Punkt die Arme Richtung Kamera heben</strong> (oder den grünen Knopf am Pfosten drücken), und der letzte Ballwechsel wird als Highlight markiert.",
            ],
            [
                "5º <strong>Etwa eine Stunde nach Spielende erhalten Sie eine E-Mail</strong> mit dem kompletten Match und Ihren gespeicherten Highlights – <strong>komplett ohne App-Download</strong>.",
            ],
        ],
    },
    "mejores-empresas-camaras-padel-espana": {
        "title": "Welche sind die besten Anbieter für Padel-Kameras in Spanien und Europa?",
        "blocks": [
            [
                'In Spanien und Europa gibt es heute mehrere große Anbieter für Platzkameras (<a href="../por-que-no-conocia-save-my-play/">hier erfahren Sie, warum Sie vielleicht noch nie von Save My Play gehört haben</a>).',
            ],
            [
                "Jedes Unternehmen verfolgt seine <strong>eigene Vision</strong> beim Thema Kameras, setzt auf unterschiedliche Technologien und Geschäftsmodelle. Deshalb rate ich Ihnen: Sprechen Sie mit jedem Anbieter, vergleichen Sie in Ruhe und fragen Sie vor allem Clubs, die die Systeme bereits im Alltag nutzen.",
            ],
            [
                "<strong>Padmi:</strong> der Anbieter mit den meisten Plätzen in Spanien (82 Plätze in 56 Clubs), nutzt zwei Kameras pro Platz. Neben Highlights liegt der Fokus stark auf KI-Statistiken, begleitet von einem sehr hochwertigen Markenauftritt als Partner der Adidas Padel Tour.",
            ],
            [
                "<strong>Aiball:</strong> in mehreren spanischen Clubs vertreten, spezialisiert auf KI-Spielanalysen und ein objektives Spielstärken-System. Profi-Spielerin Ari Sánchez ist Partnerin des Unternehmens, das auf dem Padel World Summit 2025 als Bestes Startup ausgezeichnet wurde.",
            ],
            [
                "<strong>Rackety:</strong> in rund 50 Clubs im Einsatz; kombiniert Match-Übertragungen und KI-Statistiken mit einem Platzbuchungssystem sowie WhatsApp-Chatbots zu einer Komplettlösung für den Club.",
            ],
        ],
    },
    "por-que-no-conocia-save-my-play": {
        "title": "Warum hatte ich noch nie von Save My Play gehört?",
        "blocks": [
            [
                "Wir sind ein <strong>amerikanisches Unternehmen</strong>.",
                "Obwohl Spanien weltweit die meisten Padel-Plätze hat, haben wir uns zunächst auf Märkte konzentriert, in denen Clubs fast selbstverständlich sofort alle Plätze ihrer Anlage mit Kameras ausstatten – <strong>diese Kunden hatten für uns Priorität</strong>.",
                "Inzwischen sind wir auf mehr als <strong>1.500 Club-Plätzen weltweit</strong> im Einsatz – im Padel, Tennis und Pickleball.",
            ],
        ],
    },
    "save-my-play-en-pocas-palabras": {
        "title": "Save My Play in wenigen Worten: Wer wir sind",
        "blocks": [
            [
                "Ich fasse mich kurz.",
                "Unsere Kameras laufen auf mehr als <strong>1.600 Plätzen weltweit</strong>.",
                "Der US-amerikanische Padel-Verband (USPA) nutzt unser System für seine offiziellen FIP-Turniere, und der US-Tennisverband (USTA) überträgt jedes Wochenende live von über 100 Plätzen seines National Campus.",
            ],
            [
                "Trotzdem <strong>sind wir im Kernteam weniger als 10 Personen</strong>.",
                "Und genau das schätzen die Clubs: <strong>die persönliche Nähe</strong>. Wenn etwas nicht funktioniert, sprechen Sie direkt mit uns und das Anliegen geht nicht in einer Hotline verloren.",
            ],
            [
                "Außerdem machen wir Dinge nicht unnötig kompliziert: Wenn Ihre Kameras mit <strong>zwei Knöpfen</strong> perfekt laufen, bauen wir keinen dritten ein.",
            ],
        ],
    },
    "por-que-coolpadel-colabora-con-save-my-play": {
        "title": "Warum arbeitet CoolPadel mit Save My Play zusammen?",
        "blocks": [
            [
                "Was mir in der Padel-Branche am meisten Spaß macht, ist der persönliche Austausch auf Fachmessen mit allen Herstellern.",
                "Dadurch kenne ich den Markt sehr genau: Für mich hat Save My Play unter allen Kamera-Anbietern das <strong>größte Potenzial</strong> – und mindestens genauso wichtig: <strong>es sind ehrliche, verlässliche Menschen</strong>.",
                "Da Save My Play weltweit extrem stark nachgefragt wird, betreuen wir von CoolPadel aus <strong>die Clubs in Europa</strong>: Deutschland, Österreich, Schweiz, Spanien, Frankreich, Großbritannien und Italien.",
            ],
        ],
    },
    "he-comprado-camaras-que-pasa-ahora": {
        "title": "Ich habe Kameras von Save My Play gekauft. Wie geht es jetzt weiter?",
        "blocks": [
            [
                "1º <strong>Zahlung über Stripe:</strong> Ich sende Ihnen den Zahlungslink. Abgerechnet wird in US-Dollar, da wir ein amerikanisches Unternehmen sind (die Zahlung in Dollar über Ihre Hausbank spart meist Wechselkursgebühren).",
            ],
            [
                "2º <strong>Registrierung Ihres Club-Kontos:</strong> Sie erhalten den Link zur Erstellung Ihres Save My Play-Kontos, dem Ihre Kameras automatisch zugewiesen werden.",
            ],
            [
                "3º <strong>Produktion & Versand:</strong> In rund 4 bis 5 Wochen treffen die Kameras bei Ihnen im Club ein.",
            ],
            [
                "4º <strong>Empfang & Start:</strong> Bei Lieferung fallen ca. 20 € Zollgebühren an. Die monatliche Laufzeit beginnt erst ab dem Tag, an dem Sie die Kameras auf dem Platz in Betrieb nehmen.",
            ],
        ],
    },
    "por-que-no-me-interesa-venderte-una-camara": {
        "title": "Warum möchte ich Ihnen keine Kamera verkaufen, wenn Sie nicht überzeugt sind?",
        "blocks": [
            [
                "Wenn ich Ihnen eine Kamera für 180 € verkaufe, Sie das System halbherzig testen und nach einem Monat kündigen, <strong>haben wir alle verloren</strong>.",
                "Sie verlieren 180 € und Zeit, und wir legen Geld drauf, weil die Herstellung der Kamera deutlich mehr als 180 € kostet. Wir möchten nur mit Clubs arbeiten, die vom Mehrwert überzeugt sind.",
            ],
        ],
    },
}

CAMARAS_I18N = {
    "fr": {
        "articles": FR_ARTICLES_DATA,
        "videos": FR_VIDEOS,
        "hub_eyebrow": "Ce que vous devez savoir",
        "hub_title": "Caméras pour clubs de padel",
        "hub_intro": [
            "Nous savons que vous voulez prendre la meilleure décision concernant les caméras<br>L'expérience nous montre que les clubs apprécient d'avoir des informations utiles à disposition",
            "Et que si vous n'avez aucun intérêt à vous informer, cela ne vaut pas la peine de faire une démo en ligne",
            "C'est pourquoi nous avons voulu être les más sincères et transparents possible",
            "Au fil de vos lectures, vous vous rendrez compte par vous-même si c'est une bonne idée d'installer des caméras ou non<br>Et si vous souhaitez les prendre chez Save My Play ou chez une autre entreprise",
            "Quelle que soit votre décision, ce sera la meilleure pour vous comme pour nous",
            "Ainsi, si nous faisons la démo, vous aurez de bien meilleures questions et nous rentabiliserons au mieux notre temps d'échange",
        ],
        "next_step_title": "Étape suivante",
        "next_step_p1": "Si vous hésitez encore, découvrez ci-dessus nos guides détaillés sur les caméras de padel.",
        "next_step_p2": "Si vous avez des questions précises et souhaitez voir concrètement le système en direct, réservez votre créneau pour la démo.",
        "read_article": "Lire l'article",
        "related_title": "Articles recommandés",
        "nav_camaras": "CAMÉRAS",
    },
    "en": {
        "articles": EN_ARTICLES_DATA,
        "videos": {
            "como-ver-highlights-sin-app": (
                "How to save highlights on court",
                "Raise your arms facing the camera or press the green button on the post to save your best point instantly.",
                "https://www.youtube-nocookie.com/embed/Z0vnvyrUbPQ",
            ),
            "como-montar-camara-save-my-play": (
                "How easy it is to use",
                "In just 10 minutes and with only two buttons, your camera is recording full matches, highlights and live streams effortlessly.",
                "https://www.youtube-nocookie.com/embed/LuzDvB5Umfs",
            ),
            "save-my-play-en-pocas-palabras": (
                "Live broadcast of the Miami FIP tournament",
                "This is what an official live broadcast looks like with Save My Play cameras at international FIP tournaments.",
                "https://www.youtube-nocookie.com/embed/4xwrrveDZxg?start=5623",
            ),
            "que-son-las-coaching-tools": (
                "On-court coaching tools",
                "With the coaching tools you can pause the rally on a tablet, draw trajectories and record voice feedback for your students.",
                "https://www.youtube-nocookie.com/embed/FcnCWaYahP8",
            ),
        },
        "hub_eyebrow": "What you need to know",
        "hub_title": "Cameras for padel clubs",
        "hub_intro": [
            "We know you want to make the best decision about court cameras<br>Experience tells us that clubs appreciate having honest, useful information upfront",
            "And if you're not interested in reading up first, doing an online demo isn't worth your time",
            "That is why we have been as direct and transparent as possible",
            "Along the way you will figure out whether installing cameras makes sense for your club or not<br>And whether you want them from Save My Play or from another provider",
            "Whatever you decide, it will be better for both you and us",
            "That way, if we do jump on a demo call, you will have much better questions and we'll make the most of our time",
        ],
        "next_step_title": "Next step",
        "next_step_p1": "If you're still not sure, check out the camera guides above—they will help you decide.",
        "next_step_p2": "If you have questions and want me to walk you through how everything works live, pick a time for a demo.",
        "read_article": "Read article",
        "related_title": "Recommended articles",
        "nav_camaras": "CAMERAS",
    },
    "it": {
        "articles": IT_ARTICLES_DATA,
        "videos": {
            "como-ver-highlights-sin-app": (
                "Come salvare gli highlights in campo",
                "Alza le braccia guardando la telecamera o premi il pulsante verde sul palo per salvare all'istante il tuo punto migliore.",
                "https://www.youtube-nocookie.com/embed/Z0vnvyrUbPQ",
            ),
            "como-montar-camara-save-my-play": (
                "Quanto è facile da usare",
                "In soli 10 minuti e con soli due pulsanti hai la telecamera pronta a registrare partite, highlights e dirette senza complicazioni.",
                "https://www.youtube-nocookie.com/embed/LuzDvB5Umfs",
            ),
            "save-my-play-en-pocas-palabras": (
                "Diretta ufficiale del torneo FIP di Miami",
                "Ecco come appare una trasmissione live ufficiale con le telecamere Save My Play nei tornei internazionali FIP.",
                "https://www.youtube-nocookie.com/embed/4xwrrveDZxg?start=5623",
            ),
            "que-son-las-coaching-tools": (
                "Strumenti di allenamento in campo",
                "Con le coaching tools puoi mettere in pausa l'azione sul tablet, disegnare traiettorie e registrare note vocali per i tuoi allievi.",
                "https://www.youtube-nocookie.com/embed/FcnCWaYahP8",
            ),
        },
        "hub_eyebrow": "Quello que devi sapere",
        "hub_title": "Telecamere per club di padel",
        "hub_intro": [
            "Sappiamo che vuoi prendere la decisione migliore sulle telecamere<br>L'esperienza ci insegna che i circoli apprezzano avere informazioni chiare e utili a disposizione",
            "E che se non hai interesse a informarti prima, non vale la pena fare la demo online",
            "Per questo abbiamo cercato di essere il più sinceri e trasparenti possibile",
            "Leggendo capirai se installare le telecamere nel tuo circolo è una buona idea oppure no<br>E se preferisci sceglierle con Save My Play o con un'altra azienda",
            "Qualunque sia la tua scelta, sarà meglio sia per voi che per noi",
            "Così, se faremo la demo, avrai domande più mirate e sfrutteremo al meglio il nostro tempo",
        ],
        "next_step_title": "Passo successivo",
        "next_step_p1": "Se hai ancora qualche dubbio, qui sopra trovi altri articoli sulle telecamere che ti aiuteranno a chiarirti le idee.",
        "next_step_p2": "Se hai domande e vuoi vedere bene come funziona tutto in diretta, prenota il tuo spazio per la demo.",
        "read_article": "Leggi l'articolo",
        "related_title": "Articoli consigliati",
        "nav_camaras": "TELECAMERE",
    },
    "de": {
        "articles": DE_ARTICLES_DATA,
        "videos": {
            "como-ver-highlights-sin-app": (
                "So speichern Sie Highlights direkt auf dem Platz",
                "Heben Sie die Arme Richtung Kamera oder drücken Sie den grünen Knopf am Pfosten, um Ihren besten Punkt sofort zu speichern.",
                "https://www.youtube-nocookie.com/embed/Z0vnvyrUbPQ",
            ),
            "como-montar-camara-save-my-play": (
                "Kinderleichte Bedienung",
                "In nur 10 Minuten und mit nur zwei Knöpfen zeichnet Ihre Kamera Matches, Highlights und Livestreams unkompliziert auf.",
                "https://www.youtube-nocookie.com/embed/LuzDvB5Umfs",
            ),
            "save-my-play-en-pocas-palabras": (
                "Live-Übertragung des FIP-Turniers in Miami",
                "So sieht ein offizieller Livestream mit Save My Play-Kameras bei internationalen FIP-Turnieren aus.",
                "https://www.youtube-nocookie.com/embed/4xwrrveDZxg?start=5623",
            ),
            "que-son-las-coaching-tools": (
                "Trainingstools direkt auf dem Platz",
                "Mit den Coaching-Tools können Sie den Ballwechsel auf dem Tablet anhalten, Laufwege einzeichnen und Sprachnotizen für Ihre Schüler aufnehmen.",
                "https://www.youtube-nocookie.com/embed/FcnCWaYahP8",
            ),
        },
        "hub_eyebrow": "Alles, was Sie vor der Installation von Kameras wissen müssen",
        "hub_title": "Kameras für Padel-Clubs",
        "hub_intro": [
            "Wir wissen, dass Sie die beste Entscheidung beim Thema Platzkameras treffen möchten<br>Unsere Erfahrung zeigt, dass Clubs ehrliche und praxisnahe Informationen vorab schätzen",
            "Und wenn Sie sich vorab gar nicht informieren möchten, lohnt sich auch keine Online-Demo",
            "Deshalb sind wir in diesen Artikeln so offen und transparent wie möglich",
            "Beim Lesen werden Sie schnell merken, ob Kameras für Ihren Club sinnvoll sind oder nicht<br>Und ob Sie sich für Save My Play oder einen anderen Anbieter entscheiden möchten",
            "Wie auch immer Ihre Entscheidung ausfällt – es ist besser für Sie und für uns",
            "Wenn wir danach die Online-Demo machen, haben Sie gezieltere Fragen und wir nutzen unsere gemeinsame Zeit optimal",
        ],
        "next_step_title": "Nächster Schritt",
        "next_step_p1": "Wenn Sie noch unsicher sind, finden Sie oben weitere Artikel über Kameras, die Ihnen weiterhelfen.",
        "next_step_p2": "Wenn Sie Fragen haben und live sehen möchten, wie alles funktioniert, buchen Sie hier Ihren Termin für die Demo.",
        "read_article": "Artikel lesen",
        "related_title": "Empfohlene Artikel",
        "nav_camaras": "KAMERAS",
    },
}
