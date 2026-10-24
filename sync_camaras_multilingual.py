# -*- coding: utf-8 -*-
"""
Script de sincronización de la carta de ventas de Save my Play (/camaras/)
a Italiano (IT), Inglés (EN) y Francés (FR).
Mantiene el estilo personal, directo y cortante de Javier, adaptando referencias locales.
"""

import os
import re

# 1. Leer la versión española de referencia
with open('coolpadel-web/camaras/index.html', 'r', encoding='utf-8') as f:
    es_html = f.read()

# Definición de traducciones y localizaciones
LOCALES = {
    'it': {
        'lang': 'it',
        'locale': 'it_IT',
        'canonical': 'https://coolpadelstudios.com/it/camaras/',
        'geo_region': 'IT-RM',
        'geo_placename': 'Roma',
        'geo_position': '41.9028;12.4964',
        'icbm': '41.9028, 12.4964',
        'title': 'Save my Play: Telecamere con IA per Club di Padel',
        'meta_desc': 'Telecamere con IA per campi da padel: registrazione automatica con pulsante, clip in 25s sullo smartphone e zero opere murarie. Da 45 €/mese. Prenota la demo.',
        'og_title': 'Save my Play: Telecamere con IA per Club di Padel',
        'og_desc': 'Telecamere con IA per campi da padel: registrazione automatica con pulsante, clip in 25s sullo smartphone e zero opere murarie. Da 45 €/mese. Prenota la demo.',
        'schema_service_name': 'Save my Play - Registrazione campi e telecamere intelligenti',
        'schema_service_desc': 'Sistema di registrazione per campi da padel e tennis senza opere murarie e senza vincoli contrattuali per circoli sportivi.',
        'schema_breadcrumb_name': 'Telecamere per Campi da Padel',
        'schema_faq_q1': 'Quanto costa installare le telecamere su un campo da padel con Save my Play?',
        'schema_faq_a1': 'L\'hardware costa 180 € a telecamera e l\'abbonamento software con archiviazione cloud parte da 45 € al mese per campo, senza vincoli né costi nascosti.',
        'schema_faq_q2': 'Serve fare lavori o rompere muri per l\'installazione?',
        'schema_faq_a2': 'No. Si installa in circa 5 minuti senza canaline né cavi attraverso il circolo: richiede unicamente una presa standard da 220V e connessione Wi-Fi.',
        'schema_faq_q3': 'C\'è un contratto vincolante o permanenza minima?',
        'schema_faq_a3': 'Nessun vincolo né permanenza. Puoi cancellare il servizio in qualsiasi momento senza penali.',
        'calendly_locale': 'it',
        'calendly_url': 'https://calendly.com/javier-vs-312/demo-save-my-play?hide_landing_page_details=1&hide_gdpr_banner=1&locale=it',
        'calendly_direct': 'https://calendly.com/javier-vs-312/demo-save-my-play?locale=it',
        'fallback_link_text': 'Clicca qui per aprirlo direttamente',
        'fallback_prefix': 'Se non si apre il calendario:',
        'success_title': 'Fatto. Demo prenotata.',
        'success_details': 'Riceverai la conferma con il link via email.',
        'track_tag': '[IT]',
        'track_viewed': '👀 Visto Calendario Calendly [IT]',
        'track_selected': '🕒 Selezionata Data/Ora in Calendly [IT]',
        'track_booked': '🎯 DEMO PRENOTATA: ',
        'success_js_template': 'Fatto. Demo prenotata${clubStr}. Riceverai la conferma via email con il link d\'accesso.',
        # Contenido <main>
        'h1': 'Molti club in Italia si pentono di aver installato telecamere sui loro campi.',
        'p_si_has_leido': 'Sì, hai letto bene.',
        'p_no_son_uno': 'E non sono né uno né due.',
        'p_si_piensas': '<strong>Se stai pensando di mettere telecamere, questo ti interessa.</strong>',
        'p_si_ya_tienes': '<strong>Se hai già telecamere montate, ancora di più.</strong>',
        'box1_p1': '701 parole = 2,5 minuti di lettura',
        'box1_p2': 'Ti faranno risparmiare parecchi soldi e vari grattacapi.',
        'box1_p3': 'Non credermi sulla parola, fa lo stesso.',
        'box1_p4': '<strong>Tanto alla fine mi darai ragione.</strong>',
        'h2_errores': 'I 3 errori di cui i club si pentono',
        'p_hay_mas_de': 'In Italia ci sono più di 3.500 circoli.',
        'p_todas_pistas': 'I campi da padel sono tutti praticamente identici, a parte il colore dell\'erba sintetica.',
        'p_camaras_diferencian': '<strong>Le telecamere ti differenziano subito dai circoli vicini.</strong>',
        'p_servicio_premium': 'Offri un servizio premium che i tuoi giocatori adorano e condividono sui social.',
        'p_con_tu_logo': 'E sempre con il logo del tuo club impresso sullo schermo.',
        'p_no_la_lies': '<strong>Ma non rovinare tutto con questi errori:</strong>',
        'h3_error1': 'Errore 1: Analytics e statistiche con IA',
        'p_e1_1': 'Sembra una bella idea, vero?',
        'p_e1_2': 'Avere un\'IA che ti analizza la partita, conta i colpi e ti dice pure dove devi migliorare.',
        'p_e1_3': '<strong>La realtà è che alla terza partita ti accorgi che la tua mappa di calore è identica a quella delle partite prima.</strong>',
        'p_e1_4': 'E che sapere quante volée incrociate hai fatto è un dato che non cambia la vita a nessun giocatore amatoriale.',
        'p_e1_5': 'Mi piange il cuore vedere la barca di soldi che pagano ogni mese piccoli circoli a Perugia, Brescia o Taranto, per fare un esempio.',
        'p_e1_6': '<strong>Pagare quei prezzi non è affatto redditizio. È pura follia.</strong>',
        'p_e1_7': '<strong>È questione di buonsenso.</strong>',
        'h3_error2': 'Errore 2: Periodi di prova e Vincoli contrattuali pluriennali',
        'p_e2_1': 'Attenzione ai periodi di prova gratuiti.',
        'p_e2_2': '<strong>Molta attenzione.</strong>',
        'p_e2_3': 'Il copione è sempre questo:',
        'p_e2_4': '1º Durante il primo mese vedi che la gente lo usa con entusiasmo.',
        'p_e2_5': '2º Pensando che continuerà così per sempre, firmi un vincolo di 2 o 3 anni.',
        'p_e2_6': '3º Quando la novità iniziale svanisce, tu sei costretto a continuare a pagare ogni mese.',
        'p_e2_7': '<strong>Non legarti le mani con contratti vincolanti.</strong>',
        'h3_error3': 'Errore 3: La maggior parte delle aziende usa normali telecamere di videosorveglianza',
        'p_e3_1': 'Il video finale sembra la registrazione di una rapina in banca.',
        'p_e3_2': 'La qualità delle immagini è pessima.',
        'p_e3_3': 'Un modo infallibile per capire se sono telecamere di videosorveglianza è guardare le linee del campo.',
        'p_e3_4': '<strong>Se le vedi incurvate a barilotto, pessimo segnale.</strong>',
        'p_e3_5': 'Durante la demo ricordamelo e ti faccio vedere la differenza a schermo.',
        'h3_extra': 'ERRORE EXTRA: Te lo spiego direttamente durante la demo online.',
        'box_conc_p1': '<strong>Conclusione:</strong>',
        'box_conc_p2': 'Tantissimi circoli si pentono amaramente delle telecamere e dei contratti che firmano.',
        'box_conc_p3': 'Ripeto: non fidarti ciecamente di chi vende queste cose come me.',
        'box_conc_p4': '<strong>Parla con altri gestori di circoli e ascolta cosa raccontano loro.</strong>',
        'h2_savemyplay': 'Save My Play in 3 punti',
        'img_alt1': 'Telecamera Save my Play che riprende partita di padel',
        'img_alt2': 'Giocatori di padel che rivedono replay e highlights sullo smartphone',
        'img_alt3': 'Campo da padel panoramico con sistema Save my Play',
        'bp1': 'Piano A: 136 € al mese. Include statistiche con IA. Te lo sconsiglio sinceramente.<br>Piano B: 45 € al mese. Include registrazioni, highlights, dirette streaming su YouTube, coaching tools... tutto illimitato.',
        'bp2': 'Nessun vincolo contrattuale: se vuoi cancellare la sottoscrizione, te ne vai quando vuoi.<br>Non vogliamo clienti insoddisfatti bloccati con noi, non conviene a nessuno.<br>Il 97% dei circoli continua volontariamente con noi ogni mese.',
        'bp3': 'Investimento iniziale per la telecamera di 180 €, una per campo.<br>Zero opere murarie: si monta in 5 minuti con solo Wi-Fi e una presa elettrica standard.<br>A causa dell\'alta richiesta, i tempi di consegna sono leggermente più lunghi del solito: circa 4 settimane.',
        'box_180_p1': '<strong>Come?? 180 € di costo iniziale per le telecamere?</strong>',
        'box_180_p2': 'È il prezzo da pagare per non doverti vergognare della qualità dei video del tuo circolo.',
        'box_180_p3': 'Le produciamo noi a Chicago e il solo costo vivo supera ampiamente quei 180 €.',
        'box_180_p4': 'Se ti sembra comunque caro, dimmelo pure e ti passo volentieri i contatti di altre aziende concorrenti.',
        'box_180_p5': 'Inoltre, le telecamere funzionano esclusivamente con il nostro software proprietario.',
        'box_180_p6': '<strong>Se cancelli l\'abbonamento non possono essere riutilizzate per altro.</strong>',
        'h2_buenos': 'Ora tocca parlare di quanto siamo bravi.',
        'p_buenos_1': 'Sarò il più sintetico possibile.',
        'p_buenos_2': 'Siamo installati su più di 1.600 campi in tutto il mondo.',
        'p_buenos_3': 'La Federazione Americana di Padel (USPA) ci ha scelto ufficialmente per registrare i tornei FIP.',
        'p_buenos_4': 'E alla Federazione Tennis americana trasmettiamo in diretta streaming ogni weekend su oltre 100 campi contemporaneamente.',
        'p_buenos_5': 'Se non avevi ancora sentito parlare di noi in Italia, è semplicemente perché il mercato europeo è arrivato dopo. C\'è molto più budget all\'estero.',
        'h2_paso': 'Prossimo passo: Scegli una data per la demo online',
        'p_paso_1': 'Se non ti interessa, sei troppo occupato o per ora non lo vedi fattibile, dimmelo subito senza problemi.',
        'p_paso_2': 'Se invece hai letto fin qui, hai domande e vuoi vedere esattamente come funziona tutto dal vivo, prenota uno slot per la demo.'
    },
    'en': {
        'lang': 'en',
        'locale': 'en_US',
        'canonical': 'https://coolpadelstudios.com/en/camaras/',
        'geo_region': 'GB',
        'geo_placename': 'London',
        'geo_position': '51.5074;-0.1278',
        'icbm': '51.5074, -0.1278',
        'title': 'Save my Play: AI Cameras for Padel Clubs',
        'meta_desc': 'AI cameras for padel courts: automated recording with smart net button, 25s mobile clips and no construction works. From €45/mo. Book a demo.',
        'og_title': 'Save my Play: AI Cameras for Padel Clubs',
        'og_desc': 'AI cameras for padel courts: automated recording with smart net button, 25s mobile clips and no construction works. From €45/mo. Book a demo.',
        'schema_service_name': 'Save my Play - Smart Court Recording & AI Cameras',
        'schema_service_desc': 'Smart video recording system for padel and tennis courts with no building works and no lock-in contracts for sports clubs.',
        'schema_breadcrumb_name': 'Padel Court Cameras',
        'schema_faq_q1': 'How much does it cost to install Save my Play cameras on a court?',
        'schema_faq_a1': 'Hardware is €180 per camera and the cloud software subscription starts from €45 per month per court, with zero lock-in contracts or hidden fees.',
        'schema_faq_q2': 'Are construction works required for installation?',
        'schema_faq_a2': 'No. It installs in about 5 minutes with zero wall drilling across the venue: all it requires is a standard 220V plug and club Wi-Fi.',
        'schema_faq_q3': 'Is there any minimum term or lock-in contract?',
        'schema_faq_a3': 'No contract, no commitment. You can cancel your subscription at any time without penalties.',
        'calendly_locale': 'en',
        'calendly_url': 'https://calendly.com/javier-vs-312/demo-save-my-play?hide_landing_page_details=1&hide_gdpr_banner=1&locale=en',
        'calendly_direct': 'https://calendly.com/javier-vs-312/demo-save-my-play?locale=en',
        'fallback_link_text': 'Click here to open it directly',
        'fallback_prefix': 'If the calendar does not load:',
        'success_title': 'Done. Demo booked.',
        'success_details': 'You will receive confirmation and the meeting link via email.',
        'track_tag': '[EN]',
        'track_viewed': '👀 Viewed Calendly Calendar [EN]',
        'track_selected': '🕒 Selected Date/Time in Calendly [EN]',
        'track_booked': '🎯 DEMO BOOKED: ',
        'success_js_template': 'Done. Demo booked${clubStr}. You will receive confirmation and the meeting link via email.',
        # Contenido <main>
        'h1': 'Many clubs in the UK and Europe regret installing cameras on their courts.',
        'p_si_has_leido': 'Yes, you read that right.',
        'p_no_son_uno': 'And it\'s definitely not just one or two.',
        'p_si_piensas': '<strong>If you are thinking about installing cameras, this is for you.</strong>',
        'p_si_ya_tienes': '<strong>If you already have cameras installed, even more so.</strong>',
        'box1_p1': '701 words = 2.5 minutes read',
        'box1_p2': 'They will save you serious money and plenty of headaches.',
        'box1_p3': 'Don\'t take my word for it, honestly.',
        'box1_p4': '<strong>You\'ll see I was right soon enough.</strong>',
        'h2_errores': 'The 3 mistakes club managers end up regretting',
        'p_hay_mas_de': 'There are thousands of racquet clubs popping up across Europe.',
        'p_todas_pistas': 'Most courts look virtually identical, except for the turf colour.',
        'p_camaras_diferencian': '<strong>Cameras instantly set you apart from neighbouring clubs.</strong>',
        'p_servicio_premium': 'With a premium feature players love, re-watch and share all over social media.',
        'p_con_tu_logo': 'And always with your club\'s logo on screen.',
        'p_no_la_lies': '<strong>Just make sure you don\'t make these mistakes:</strong>',
        'h3_error1': 'Mistake 1: AI Analytics and Complex Stats',
        'p_e1_1': 'Sounds impressive on paper, doesn\'t it?',
        'p_e1_2': 'Having an AI break down your technique, count your shots and claim to fix your backhand.',
        'p_e1_3': '<strong>The reality is that by their third match, amateur players realize their heatmap looks just like the previous one.</strong>',
        'p_e1_4': 'And counting how many topspin volleys they hit provides zero real value to their weekly Sunday game.',
        'p_e1_5': 'It breaks my heart seeing small local clubs paying crazy monthly fees for features nobody uses after week two.',
        'p_e1_6': '<strong>Paying those rates makes zero financial sense. It\'s nonsense.</strong>',
        'p_e1_7': '<strong>It\'s just common sense.</strong>',
        'h3_error2': 'Mistake 2: Free trials and 3-year lock-in contracts',
        'p_e2_1': 'Watch out for free trial offers.',
        'p_e2_2': '<strong>Seriously, watch out.</strong>',
        'p_e2_3': 'Here is how it usually goes down:',
        'p_e2_4': '1º During month one, members try it because it\'s fresh and new.',
        'p_e2_5': '2º Assuming hype will stay at 100% forever, you sign a 2 or 3-year contract.',
        'p_e2_6': '3º When initial hype cools down, you\'re stuck paying thousands every month.',
        'p_e2_7': '<strong>Never mortgage your club\'s future with a multi-year lock-in contract.</strong>',
        'h3_error3': 'Mistake 3: Most vendors just install generic CCTV security cameras',
        'p_e3_1': 'The match video looks like bank robbery CCTV footage.',
        'p_e3_2': 'Image quality and frame rate are terrible for fast racquet sports.',
        'p_e3_3': 'A quick giveaway of cheap CCTV lenses is court lines.',
        'p_e3_4': '<strong>If court lines look curved like a fishbowl, run away.</strong>',
        'p_e3_5': 'During our quick demo, remind me and I\'ll show you the visual comparison.',
        'h3_extra': 'EXTRA MISTAKE: I will tell you this one live on our online demo.',
        'box_conc_p1': '<strong>Bottom line:</strong>',
        'box_conc_p2': 'A lot of clubs genuinely regret the camera contracts they rushed into.',
        'box_conc_p3': 'Again, don\'t take sales pitches like mine at face value.',
        'box_conc_p4': '<strong>Talk to fellow club owners and ask them directly.</strong>',
        'h2_savemyplay': 'Save My Play in 3 points',
        'img_alt1': 'Save my Play camera recording padel match on court',
        'img_alt2': 'Padel players reviewing replays and video highlights on their mobile',
        'img_alt3': 'Panoramic padel court with Save my Play camera system',
        'bp1': 'Plan A: €136/month. Includes AI stats. Honestly, I don\'t recommend it.<br>Plan B: €45/month. Includes court recordings, instant highlights, live YouTube streaming, coaching tools... unlimited.',
        'bp2': 'Zero lock-in contracts: cancel anytime and walk away with no questions asked.<br>We don\'t want unhappy trapped clients, it\'s bad business.<br>97% of clubs voluntarily stay with us month after month.',
        'bp3': 'Upfront hardware cost of €180 per camera, one per court.<br>No construction works: mounts in 5 minutes with just Wi-Fi and a standard power plug.<br>Due to high demand, delivery currently takes around 4 weeks.',
        'box_180_p1': '<strong>Wait, €180 upfront for the cameras?</strong>',
        'box_180_p2': 'It\'s the fair price to avoid being embarrassed by your club\'s video quality.',
        'box_180_p3': 'We manufacture our own cameras in Chicago and production costs exceed €180.',
        'box_180_p4': 'If it still feels steep, tell me straight and I\'ll gladly share contact details of other vendors.',
        'box_180_p5': 'Keep in mind our cameras work exclusively with our proprietary software.',
        'box_180_p6': '<strong>If you cancel your subscription, they cannot be repurposed.</strong>',
        'h2_buenos': 'Now the part where we brag about our track record.',
        'p_buenos_1': 'I\'ll keep it as short as possible.',
        'p_buenos_2': 'Installed across more than 1,600 courts worldwide.',
        'p_buenos_3': 'Selected by the US Padel Association to broadcast and record their official FIP tournaments.',
        'p_buenos_4': 'And for the United States Tennis Association (USTA), we livestream every weekend across 100+ courts simultaneously.',
        'p_buenos_5': 'If you hadn\'t heard of us yet, it\'s simply because the UK/EU padel market was later in our rollout. There\'s bigger volume abroad.',
        'h2_paso': 'Next step: Book a slot for your online demo',
        'p_paso_1': 'If you\'re not interested, too busy, or it\'s not the right time, let me know straight away.',
        'p_paso_2': 'If you read all the way here, have questions and want to see exactly how it works on screen, pick a time below.'
    },
    'fr': {
        'lang': 'fr',
        'locale': 'fr_FR',
        'canonical': 'https://coolpadelstudios.com/fr/camaras/',
        'geo_region': 'FR-IDF',
        'geo_placename': 'Paris',
        'geo_position': '48.8566;2.3522',
        'icbm': '48.8566, 2.3522',
        'title': 'Save my Play : Caméras avec IA pour Clubs de Padel',
        'meta_desc': 'Caméras IA pour pistes de padel : enregistrement automatique avec bouton au filet, clips en 25s sur smartphone et sans travaux. Dès 45 €/mois. Réservez une démo.',
        'og_title': 'Save my Play : Caméras avec IA pour Clubs de Padel',
        'og_desc': 'Caméras IA pour pistes de padel : enregistrement automatique avec bouton au filet, clips en 25s sur smartphone et sans travaux. Dès 45 €/mois. Réservez une démo.',
        'schema_service_name': 'Save my Play - Enregistrement de courts et caméras intelligentes',
        'schema_service_desc': 'Système d\'enregistrement vidéo pour pistes de padel et tennis sans travaux et sans engagement pour clubs sportifs.',
        'schema_breadcrumb_name': 'Caméras pour Pistes de Padel',
        'schema_faq_q1': 'Combien coûte l\'installation des caméras Save my Play sur un court ?',
        'schema_faq_a1': 'Le matériel coûte 180 € par caméra et l\'abonnement cloud démarre à 45 € par mois et par piste, sans engagement ni frais cachés.',
        'schema_faq_q2': 'Faut-il réaliser des travaux ou percer des tranchées ?',
        'schema_faq_a2': 'Non. L\'installation prend environ 5 minutes sans goulottes ni câblage à travers le club : une prise standard 220V et une connexion Wi-Fi suffisent.',
        'schema_faq_q3': 'Y a-t-il un engagement de durée minimale ?',
        'schema_faq_a3': 'Aucun engagement. Vous pouvez résilier votre abonnement à tout moment sans la moindre pénalité.',
        'calendly_locale': 'fr',
        'calendly_url': 'https://calendly.com/javier-vs-312/demo-save-my-play?hide_landing_page_details=1&hide_gdpr_banner=1&locale=fr',
        'calendly_direct': 'https://calendly.com/javier-vs-312/demo-save-my-play?locale=fr',
        'fallback_link_text': 'Cliquez ici pour l\'ouvrir directement',
        'fallback_prefix': 'Si le calendrier ne s\'affiche pas :',
        'success_title': 'C\'est fait. Démo réservée.',
        'success_details': 'Vous recevrez la confirmation et le lien d\'accès par email.',
        'track_tag': '[FR]',
        'track_viewed': '👀 Calendrier Calendly affiché [FR]',
        'track_selected': '🕒 Date/Heure sélectionnée sur Calendly [FR]',
        'track_booked': '🎯 DÉMO RÉSERVÉE : ',
        'success_js_template': 'C\'est fait. Démo réservée${clubStr}. Vous recevrez la confirmation et le lien par email.',
        # Contenido <main>
        'h1': 'Beaucoup de clubs en France regrettent d\'avoir installé des caméras sur leurs terrains.',
        'p_si_has_leido': 'Oui, vous avez bien lu.',
        'p_no_son_uno': 'Et ce n\'est pas un cas isolé.',
        'p_si_piensas': '<strong>Si vous envisagez d\'équiper vos pistes de caméras, ceci vous concerne directement.</strong>',
        'p_si_ya_tienes': '<strong>Si vous en avez déjà, c\'est encore plus important.</strong>',
        'box1_p1': '701 mots = 2,5 minutes de lecture',
        'box1_p2': 'Ils vont vous faire économiser beaucoup d\'argent et pas mal d\'ennuis.',
        'box1_p3': 'Ne me croyez pas sur parole, peu importe.',
        'box1_p4': '<strong>Vous finirez par me donner raison.</strong>',
        'h2_errores': 'Les 3 erreurs que les clubs finissent par regretter',
        'p_hay_mas_de': 'Il y a plus de 2 000 pistes de padel en France et le marché explose.',
        'p_todas_pistas': 'La plupart des terrains se ressemblent, hormis la couleur de la moquette.',
        'p_camaras_diferencian': '<strong>Les caméras vous différencient immédiatement des clubs voisins.</strong>',
        'p_servicio_premium': 'Avec une prestation premium que vos joueurs adorent et partagent sur les réseaux.',
        'p_con_tu_logo': 'Et toujours avec le logo de votre club affiché à l\'écran.',
        'p_no_la_lies': '<strong>Mais évitez de tomber dans ces pièges classiques :</strong>',
        'h3_error1': 'Erreur 1 : Les analytics et statistiques par IA',
        'p_e1_1': 'Sur le papier, l\'idée paraît séduisante.',
        'p_e1_2': 'Une IA qui décortique vos matchs, compte vos coups et prétend vous expliquer comment jouer.',
        'p_e1_3': '<strong>La réalité, c\'est qu\'au troisième match, vos joueurs réalisent que leur carte de chaleur ressemble exactement à la précédente.</strong>',
        'p_e1_4': 'Et savoir combien de volées liftées ils ont frappées n\'apporte strictement rien à un joueur du dimanche.',
        'p_e1_5': 'Ça me désole de voir les sommes folles que paient chaque mois des petits clubs à Bordeaux, Reims ou Montpellier pour ça.',
        'p_e1_6': '<strong>Payer de tels tarifs n\'est absolument pas rentable. C\'est insensé.</strong>',
        'p_e1_7': '<strong>C\'est du simple bon sens.</strong>',
        'h3_error2': 'Erreur 2 : Périodes d\'essai gratuites et Engagements sur plusieurs années',
        'p_e2_1': 'Méfiez-vous des périodes d\'essai gratuites.',
        'p_e2_2': '<strong>Vraiment, méfiez-vous.</strong>',
        'p_e2_3': 'Le piège est presque toujours le même :',
        'p_e2_4': '1º Pendant le premier mois, la nouveauté attire les joueurs.',
        'p_e2_5': '2º Pensant que ce sera comme ça tout le temps, vous signez un engagement ferme de 2 ou 3 ans.',
        'p_e2_6': '3º Dès que l\'engouement initial retombe, vous êtes bloqué à payer chaque mois.',
        'p_e2_7': '<strong>N\'hypothéquez jamais votre club avec un engagement pluriannuel.</strong>',
        'h3_error3': 'Erreur 3 : La plupart des prestataires utilisent de vulgaires caméras de surveillance',
        'p_e3_1': 'Le rendu final ressemble à l\'enregistrement d\'un braquage de banque.',
        'p_e3_2': 'La qualité d\'image et la fluidité sont catastrophiques pour un sport rapide.',
        'p_e3_3': 'Un excellent indicateur pour repérer une caméra de sécurité : les lignes du court.',
        'p_e3_4': '<strong>Si les lignes apparaissent courbées en œil-de-bœuf, fuyez.</strong>',
        'p_e3_5': 'Pendant la démo en ligne, rappelez-le moi et je vous montrerai la différence en direct.',
        'h3_extra': 'ERREUR SUPPLÉMENTAIRE : Je vous l\'explique directement pendant notre démo en ligne.',
        'box_conc_p1': '<strong>Conclusion :</strong>',
        'box_conc_p2': 'Beaucoup de gérants regrettent amèrement les caméras et les contrats signés trop vite.',
        'box_conc_p3': 'Encore une fois : ne croyez pas aveuglément les commerciaux comme moi.',
        'box_conc_p4': '<strong>Parlez à d\'autres gérants de clubs et écoutez leurs retours d\'expérience.</strong>',
        'h2_savemyplay': 'Save My Play en 3 points',
        'img_alt1': 'Caméra Save my Play enregistrant un match sur piste de padel',
        'img_alt2': 'Joueurs de padel visionnant leurs replays et highlights sur smartphone',
        'img_alt3': 'Piste de padel panoramique équipée du système Save my Play',
        'bp1': 'Plan A : 136 € par mois. Inclut les statistiques IA. Je ne vous le conseille pas.<br>Plan B : 45 € par mois. Inclut enregistrements, highlights, live streaming sur YouTube, coaching tools... tout en illimité.',
        'bp2': 'Zéro engagement : si vous voulez résilier, vous partez quand vous voulez sans frais.<br>Nous ne voulons pas de clients mécontents piégés par contrat.<br>97 % des clubs restent fidèles chaque mois de leur plein gré.',
        'bp3': 'Investissement initial de 180 € par caméra, une seule par piste.<br>Aucun travaux : s\'installe en 5 minutes avec seulement le Wi-Fi et une prise de courant.<br>Face à une très forte demande, le délai d\'expédition est d\'environ 4 semaines.',
        'box_180_p1': '<strong>Comment ? 180 € d\'investissement initial par caméra ?</strong>',
        'box_180_p2': 'C\'est le prix juste pour ne pas avoir honte de la qualité vidéo offerte à vos membres.',
        'box_180_p3': 'Nous fabriquons nous-mêmes nos caméras à Chicago et le coût de revient dépasse ces 180 €.',
        'box_180_p4': 'Si cela vous paraît cher malgré tout, dites-le moi et je vous transmettrai volontiers les coordonnées de confrères.',
        'box_180_p5': 'Par ailleurs, nos caméras fonctionnent uniquement avec notre écosystème logiciel propriétaire.',
        'box_180_p6': '<strong>Si vous résiliez l\'abonnement, elles ne peuvent pas être recyclées pour un autre usage.</strong>',
        'h2_buenos': 'Maintenant, parlons un peu de notre expérience.',
        'p_buenos_1': 'Je vais faire aussi court que possible.',
        'p_buenos_2': 'Nous équipons plus de 1 600 pistes à travers le monde.',
        'p_buenos_3': 'La Fédération Américaine de Padel nous a choisis pour enregistrer ses tournois officiels FIP.',
        'p_buenos_4': 'Et pour la Fédération Américaine de Tennis (USTA), nous retransmettons chaque week-end en direct sur plus de 100 courts en continu.',
        'p_buenos_5': 'Si vous ne nous connaissiez pas encore en France, c\'est simplement parce que nous avons démarré par d\'autres pays à plus fort volume.',
        'h2_paso': 'Étape suivante : Réserver un créneau pour la démo en ligne',
        'p_paso_1': 'Si cela ne vous intéresse pas, que vous êtes trop pris ou que ce n\'est pas le moment, dites-le moi sans détour.',
        'p_paso_2': 'Si vous avez lu jusqu\'ici, que vous avez des questions et souhaitez voir concrètement l\'outil fonctionner, choisissez un créneau pour la démo.'
    }
}

def generate_page(target_lang):
    info = LOCALES[target_lang]
    
    # Clonamos la base de es_html
    html = es_html
    
    # Reemplazo de metadatos básicos de <html lang="...">
    html = re.sub(r'<html lang="[^"]+"', f'<html lang="{info["lang"]}"', html, count=1)
    
    # Meta título y descripción
    html = re.sub(r'<title>.*?</title>', f'<title>{info["title"]}</title>', html, count=1)
    html = re.sub(r'<meta name="description" content=".*?">', f'<meta name="description" content="{info["meta_desc"]}">', html, count=1)
    
    # Canonical
    html = re.sub(r'<link rel="canonical" href=".*?">', f'<link rel="canonical" href="{info["canonical"]}">', html, count=1)
    
    # OpenGraph & Twitter
    html = re.sub(r'<meta property="og:locale" content=".*?">', f'<meta property="og:locale" content="{info["locale"]}">', html, count=1)
    html = re.sub(r'<meta property="og:title" content=".*?">', f'<meta property="og:title" content="{info["og_title"]}">', html, count=1)
    html = re.sub(r'<meta property="og:description" content=".*?">', f'<meta property="og:description" content="{info["og_desc"]}">', html, count=1)
    html = re.sub(r'<meta property="og:url" content=".*?">', f'<meta property="og:url" content="{info["canonical"]}">', html, count=1)
    html = re.sub(r'<meta name="twitter:title" content=".*?">', f'<meta name="twitter:title" content="{info["og_title"]}">', html, count=1)
    html = re.sub(r'<meta name="twitter:description" content=".*?">', f'<meta name="twitter:description" content="{info["og_desc"]}">', html, count=1)
    
    # Geo tags
    html = re.sub(r'<meta name="geo\.region" content=".*?">', f'<meta name="geo.region" content="{info["geo_region"]}">', html, count=1)
    html = re.sub(r'<meta name="geo\.placename" content=".*?">', f'<meta name="geo.placename" content="{info["geo_placename"]}">', html, count=1)
    html = re.sub(r'<meta name="geo\.position" content=".*?">', f'<meta name="geo.position" content="{info["geo_position"]}">', html, count=1)
    html = re.sub(r'<meta name="ICBM" content=".*?">', f'<meta name="ICBM" content="{info["icbm"]}">', html, count=1)
    
    # Schema.org JSON-LD
    html = re.sub(r'\"@id\": \"https://coolpadelstudios\.com/camaras/#article\"', f'\"@id\": \"{info["canonical"]}#article\"', html)
    html = re.sub(r'\"headline\": \".*?\"', f'\"headline\": \"{info["h1"]}\"', html, count=1)
    html = re.sub(r'\"description\": \".*?\"', f'\"description\": \"{info["meta_desc"]}\"', html, count=1)
    html = re.sub(r'\"mainEntityOfPage\": \"https://coolpadelstudios\.com/camaras/\"', f'\"mainEntityOfPage\": \"{info["canonical"]}\"', html)
    
    html = re.sub(r'\"@id\": \"https://coolpadelstudios\.com/camaras/#service\"', f'\"@id\": \"{info["canonical"]}#service\"', html)
    html = re.sub(r'\"name\": \"Save my Play - Grabación de pistas y cámaras inteligentes\"', f'\"name\": \"{info["schema_service_name"]}\"', html)
    html = re.sub(r'\"description\": \"Sistema de grabación en pista de pádel y tenis sin obras y sin permanencia para clubes deportivos\."', f'\"description\": \"{info["schema_service_desc"]}\"', html)
    html = re.sub(r'\"url\": \"https://coolpadelstudios\.com/camaras/\"', f'\"url\": \"{info["canonical"]}\"', html)
    
    html = re.sub(r'\"@id\": \"https://coolpadelstudios\.com/camaras/#breadcrumb\"', f'\"@id\": \"{info["canonical"]}#breadcrumb\"', html)
    html = re.sub(r'\"name\": \"Cámaras para Pistas de Pádel\"', f'\"name\": \"{info["schema_breadcrumb_name"]}\"', html)
    html = re.sub(r'\"item\": \"https://coolpadelstudios\.com/camaras/\"', f'\"item\": \"{info["canonical"]}\"', html)
    
    # FAQ Schema
    html = re.sub(r'\"name\": \"¿Cuánto cuesta poner cámaras en una pista de pádel con Save my Play\?\"', f'\"name\": \"{info["schema_faq_q1"]}\"', html)
    html = re.sub(r'\"text\": \"El hardware cuesta 180 € por cámara y la suscripción de software y almacenamiento en la nube es desde 45 € al mes por pista, sin permanencia ni costes ocultos\."', f'\"text\": \"{info["schema_faq_a1"]}\"', html)
    html = re.sub(r'\"name\": \"¿Se necesita obra para la instalación\?\"', f'\"name\": \"{info["schema_faq_q2"]}\"', html)
    html = re.sub(r'\"text\": \"No\. No requiere canalizaciones ni obras civiles complejas: solo un enchufe estándar de 220V y conexión Wi-Fi\."', f'\"text\": \"{info["schema_faq_a2"]}\"', html)
    html = re.sub(r'\"name\": \"¿Existe permanencia obligatoria en la suscripción\?\"', f'\"name\": \"{info["schema_faq_q3"]}\"', html)
    html = re.sub(r'\"text\": \"No hay ninguna permanencia obligatoria\. Puedes cancelar en cualquier momento sin penalizaciones ni ataduras contractuales\."', f'\"text\": \"{info["schema_faq_a3"]}\"', html)
    
    # 2. Generar el contenido <main> traducido y adaptado
    main_content = f"""<main>

        <!-- TÍTULO PRINCIPAL -->
        <h1 class="main-title reveal-on-scroll">
            {info['h1']}
        </h1>

        <p class="reveal-on-scroll">
            {info['p_si_has_leido']}
        </p>

        <p class="reveal-on-scroll">
            {info['p_no_son_uno']}
        </p>

        <p class="reveal-on-scroll">
            {info['p_si_piensas']}
        </p>

        <p class="reveal-on-scroll">
            {info['p_si_ya_tienes']}
        </p>

        <!-- SEPARACIÓN 1 -->
        <hr class="sub-divider reveal-on-scroll">

        <!-- CAJA DESTACADA 1 -->
        <div class="lead-warning reveal-on-scroll">
            <p>
                {info['box1_p1']}
            </p>
            <p>
                {info['box1_p2']}
            </p>
            <p>
                {info['box1_p3']}
            </p>
            <p>
                {info['box1_p4']}
            </p>
        </div>

        <!-- TÍTULO SECCIÓN ERRORES -->
        <h2 class="section-title-inline reveal-on-scroll">
            {info['h2_errores']}
        </h2>

        <p class="reveal-on-scroll">
            {info['p_hay_mas_de']}
        </p>

        <p class="reveal-on-scroll">
            {info['p_todas_pistas']}
        </p>

        <p class="reveal-on-scroll">
            {info['p_camaras_diferencian']}
        </p>

        <p class="reveal-on-scroll">
            {info['p_servicio_premium']}
        </p>

        <p class="reveal-on-scroll">
            {info['p_con_tu_logo']}
        </p>

        <p class="reveal-on-scroll">
            {info['p_no_la_lies']}
        </p>

        <!-- ERROR 1 -->
        <h3 class="decision-title reveal-on-scroll">
            {info['h3_error1']}
        </h3>

        <p class="reveal-on-scroll">
            {info['p_e1_1']}
        </p>

        <p class="reveal-on-scroll">
            {info['p_e1_2']}
        </p>

        <p class="reveal-on-scroll">
            {info['p_e1_3']}
        </p>

        <p class="reveal-on-scroll">
            {info['p_e1_4']}
        </p>

        <p class="reveal-on-scroll">
            {info['p_e1_5']}
        </p>

        <p class="reveal-on-scroll">
            {info['p_e1_6']}
        </p>

        <p class="reveal-on-scroll">
            {info['p_e1_7']}
        </p>

        <!-- ERROR 2 -->
        <h3 class="decision-title reveal-on-scroll">
            {info['h3_error2']}
        </h3>

        <p class="reveal-on-scroll">
            {info['p_e2_1']}
        </p>

        <p class="reveal-on-scroll">
            {info['p_e2_2']}
        </p>

        <p class="reveal-on-scroll">
            {info['p_e2_3']}
        </p>

        <p class="reveal-on-scroll">
            {info['p_e2_4']}
        </p>

        <p class="reveal-on-scroll">
            {info['p_e2_5']}
        </p>

        <p class="reveal-on-scroll">
            {info['p_e2_6']}
        </p>

        <p class="reveal-on-scroll">
            {info['p_e2_7']}
        </p>

        <!-- ERROR 3 -->
        <h3 class="decision-title reveal-on-scroll">
            {info['h3_error3']}
        </h3>

        <p class="reveal-on-scroll">
            {info['p_e3_1']}
        </p>

        <p class="reveal-on-scroll">
            {info['p_e3_2']}
        </p>

        <p class="reveal-on-scroll">
            {info['p_e3_3']}
        </p>

        <p class="reveal-on-scroll">
            {info['p_e3_4']}
        </p>

        <p class="reveal-on-scroll">
            {info['p_e3_5']}
        </p>

        <!-- ERROR EXTRA -->
        <h3 class="decision-title reveal-on-scroll">
            {info['h3_extra']}
        </h3>

        <!-- CONCLUSIÓN EN CAJA DESTACADA -->
        <div class="lead-warning reveal-on-scroll" style="margin-top: 3.5rem;">
            <p>
                {info['box_conc_p1']}
            </p>
            <p>
                {info['box_conc_p2']}
            </p>
            <p>
                {info['box_conc_p3']}
            </p>
            <p>
                {info['box_conc_p4']}
            </p>
        </div>

        <!-- SEPARACIÓN 1 SOLO SALTO -->
        <hr class="sub-divider reveal-on-scroll">

        <!-- SAVE MY PLAY EN 3 PUNTOS -->
        <h2 class="section-title reveal-on-scroll" style="margin-top: 2rem; border-top: none; padding-top: 0;">
            {info['h2_savemyplay']}
        </h2>

        <!-- 3 FOTOS EN PISTA -->
        <div class="reveal-on-scroll" style="margin: 1.8rem 0 1.5rem;">
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 0.765rem;">
                <div style="border-radius: 10px; overflow: hidden; border: 2px solid #111; box-shadow: 0 8px 20px rgba(0,0,0,0.12);">
                    <img src="/assets/images/savemyplay-1.jpg" alt="{info['img_alt1']}" width="320" height="135" decoding="async" style="width: 100%; height: 135px; object-fit: cover; display: block;" loading="lazy">
                </div>
                <div style="border-radius: 10px; overflow: hidden; border: 2px solid #111; box-shadow: 0 8px 20px rgba(0,0,0,0.12);">
                    <img src="/assets/images/savemyplay-2.jpg" alt="{info['img_alt2']}" width="320" height="135" decoding="async" style="width: 100%; height: 135px; object-fit: cover; display: block;" loading="lazy">
                </div>
                <div style="border-radius: 10px; overflow: hidden; border: 2px solid #111; box-shadow: 0 8px 20px rgba(0,0,0,0.12);">
                    <img src="/assets/images/savemyplay-3.jpg" alt="{info['img_alt3']}" width="320" height="135" decoding="async" style="width: 100%; height: 135px; object-fit: cover; display: block;" loading="lazy">
                </div>
            </div>
        </div>

        <!-- BULLET POINTS SAVE MY PLAY -->
        <ul class="puntos-list reveal-on-scroll">
            <li>
                {info['bp1']}
            </li>
            <li>
                {info['bp2']}
            </li>
            <li>
                {info['bp3']}
            </li>
        </ul>

        <!-- CAJA DESTACADA 180€ -->
        <div class="lead-warning reveal-on-scroll">
            <p>
                {info['box_180_p1']}
            </p>
            <p>
                {info['box_180_p2']}
            </p>
            <p>
                {info['box_180_p3']}
            </p>
            <p>
                {info['box_180_p4']}
            </p>
            <p>
                {info['box_180_p5']}
            </p>
            <p>
                {info['box_180_p6']}
            </p>
        </div>

        <!-- SEPARACIÓN -->
        <hr class="sub-divider reveal-on-scroll">

        <!-- AHORA TOCA HABLAR DE LO BUENOS QUE SOMOS -->
        <h2 class="section-title reveal-on-scroll" style="margin-top: 2rem; border-top: none; padding-top: 0;">
            {info['h2_buenos']}
        </h2>

        <p class="reveal-on-scroll">
            {info['p_buenos_1']}
        </p>

        <p class="reveal-on-scroll">
            {info['p_buenos_2']}
        </p>

        <p class="reveal-on-scroll">
            {info['p_buenos_3']}
        </p>

        <p class="reveal-on-scroll">
            {info['p_buenos_4']}
        </p>

        <p class="reveal-on-scroll">
            {info['p_buenos_5']}
        </p>

        <!-- SEPARACIÓN -->
        <hr class="sub-divider reveal-on-scroll">

        <!-- SIGUIENTE PASO -->
        <h2 class="section-title reveal-on-scroll" style="margin-top: 2.25rem; border-top: none; padding-top: 0;">
            {info['h2_paso']}
        </h2>

        <p class="reveal-on-scroll">
            {info['p_paso_1']}
        </p>

        <p class="reveal-on-scroll">
            {info['p_paso_2']}
        </p>

        <!-- TARJETA DE CONFIRMACIÓN AL AGENDAR EN CALENDLY -->
        <div id="calendlySuccessCard" class="calendly-success-card">
            <h4>{info['success_title']}</h4>
            <p id="calendlySuccessDetails">{info['success_details']}</p>
        </div>

        <!-- CALENDARIO CALENDLY INCRUSTADO DIRECTAMENTE -->
        <div id="calendlyContainer" class="reveal-on-scroll calendly-embed-container">
            <div id="calendlyWidget" class="calendly-inline-widget" data-url="{info['calendly_url']}" style="min-width:320px;height:700px;"></div>
        </div>

        <p class="reveal-on-scroll calendly-fallback-text">
            {info['fallback_prefix']} <a href="{info['calendly_direct']}" target="_blank" rel="noopener noreferrer">{info['fallback_link_text']}</a>
        </p>

    </main>"""

    # Sustituir <main>...</main> en html
    html = re.sub(r'<main>.*?</main>', main_content, html, flags=re.DOTALL)
    
    # 3. Adaptar el script de Calendly y tracking post-main
    post_tracking_code = """    <!-- SCRIPT DE REVELADO SUAVE A MEDIDA QUE SE DESLIZA (SCROLL) -->
    <script>
        document.addEventListener('DOMContentLoaded', () => {
            const revealElements = document.querySelectorAll('.reveal-on-scroll');
            const revealCallback = (entries, observer) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        entry.target.classList.add('is-visible');
                        observer.unobserve(entry.target);
                    }
                });
            };
            const revealObserver = new IntersectionObserver(revealCallback, {
                root: null,
                threshold: 0.05,
                rootMargin: '0px 0px -20px 0px'
            });
            revealElements.forEach(el => revealObserver.observe(el));
        });
    </script>

    <!-- MOTOR UNIFICADO DE ANALÍTICA COMERCIAL Y ORGÁNICA (SEO / GEO / AEO) -->
    <script src="/assets/js/cp-analytics.js?v=20261020b"></script>
    <script>
        window.addEventListener('message', (e) => {
            try {
                if (!e.data || typeof e.data !== 'object') return;
                const cEvent = e.data.event;
                const urlParams = new URLSearchParams(window.location.search);
                const leadName = urlParams.get('lead') || urlParams.get('club') || urlParams.get('nombre') || localStorage.getItem('cp_lead_name') || '';
                const leadTel = urlParams.get('tel') || urlParams.get('phone') || urlParams.get('c') || localStorage.getItem('cp_lead_tel') || '';

                if (cEvent === 'calendly.event_type_viewed' && window.cpTrackEvent) {
                    window.cpTrackEvent('calendly_visto', { evento_desc: '__TRACK_VIEWED__' });
                } else if (cEvent === 'calendly.date_and_time_selected' && window.cpTrackEvent) {
                    window.cpTrackEvent('calendly_hora_seleccionada', { evento_desc: '__TRACK_SELECTED__' });
                } else if (cEvent === 'calendly.event_scheduled') {
                    const payloadCalendly = e.data.payload || {};
                    if (window.cpTrackEvent) {
                        window.cpTrackEvent('demo_agendada', {
                            tipo: 'reunion_calendly',
                            evento_desc: `__TRACK_BOOKED__${leadName || 'Club'}${leadTel ? ' ' + leadTel : ''}`,
                            lead_nombre: leadName,
                            lead_tel: leadTel,
                            calendly_uri: payloadCalendly.event ? payloadCalendly.event.uri : ''
                        });
                    }
                    const successCard = document.getElementById('calendlySuccessCard');
                    const successDetails = document.getElementById('calendlySuccessDetails');
                    if (successCard && successDetails) {
                        const clubStr = leadName ? ` (${leadName})` : '';
                        successDetails.innerHTML = `__SUCCESS_JS_TEMPLATE__`;
                        successCard.style.display = 'block';
                        successCard.scrollIntoView({ behavior: 'smooth', block: 'center' });
                    }
                }
            } catch (err) {}
        });
    </script>
</body>
</html>"""

    post_tracking_code = post_tracking_code.replace('__TRACK_VIEWED__', info['track_viewed'])
    post_tracking_code = post_tracking_code.replace('__TRACK_SELECTED__', info['track_selected'])
    post_tracking_code = post_tracking_code.replace('__TRACK_BOOKED__', info['track_booked'])
    post_tracking_code = post_tracking_code.replace('__SUCCESS_JS_TEMPLATE__', info['success_js_template'])

    # Sustituir todo tras </main>
    main_end_idx = html.find('</main>') + 7
    html = html[:main_end_idx] + '\n\n' + post_tracking_code

    # Guardar archivo destino
    out_dir = f"coolpadel-web/{target_lang}/camaras"
    os.makedirs(out_dir, exist_ok=True)
    out_file = os.path.join(out_dir, "index.html")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated {out_file} ({len(html)} bytes, {len(html.splitlines())} lines)")

if __name__ == '__main__':
    for lang in ['it', 'en', 'fr']:
        generate_page(lang)
    print("All language versions generated successfully!")
