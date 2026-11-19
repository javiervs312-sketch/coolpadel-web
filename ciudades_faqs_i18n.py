# -*- coding: utf-8 -*-
"""
Diccionario determinista con las 2 preguntas/respuestas oficiales adicionales de entrega e inversión para Save My Play.
En 22 idiomas, exactas, sin alucinaciones, coherentes con la política comercial de Javier:
- Plazo de entrega oficial: 4 semanas desde la confirmación del pedido (envío internacional).
- Modalidad de inversión y propiedad: El hardware (180€ / divisa local) es propiedad 100% del club tras pago único, sin alquiler forzoso ni permanencia.
"""

EXTRA_FAQS_22 = {
    "es": {
        "faq5_q": "¿Cuánto tarda el envío y entrega de las cámaras Save My Play en {city}?",
        "faq5_a": "El plazo de entrega del hardware en {city} es de aproximadamente 4 semanas desde la confirmación del pedido. El envío incluye los anclajes de sujeción para postes y el cableado de conexión rápida.",
        "faq6_q": "¿El club es propietario del sistema de cámaras?",
        "faq6_a": "Sí, el hardware es propiedad al 100% del club mediante un pago único ({hw}). No hay cuotas de alquiler ocultas y los servicios en la nube ({rec} para grabación o {ai} para estadísticas) son de suscripción flexible sin permanencia.",
    },
    "en": {
        "faq5_q": "How long does shipping and delivery of Save My Play cameras take in {city}?",
        "faq5_a": "Delivery time to {city} is approximately 4 weeks from order confirmation. The shipment includes heavy-duty post mounts and quick-connect cables ready for 5-minute setup.",
        "faq6_q": "Does the club own the camera hardware outright?",
        "faq6_a": "Yes, the hardware is 100% owned by the club via a one-time purchase ({hw}). There are no forced hardware leases, and the software plans ({rec} for recording or {ai} for AI stats) operate on month-to-month flexible terms with zero lock-in.",
    },
    "it": {
        "faq5_q": "Quanto tempo richiede la spedizione e la consegna delle telecamere Save My Play a {city}?",
        "faq5_a": "I tempi di consegna dell'hardware a {city} sono di circa 4 settimane dalla conferma dell'ordine. La spedizione include i supporti di fissaggio per pali e il cablaggio di collegamento rapido.",
        "faq6_q": "Il club diventa proprietario al 100% dell'hardware?",
        "faq6_a": "Sì, l'hardware è di piena proprietà del club tramite pagamento unico ({hw}). Non ci sono costi di noleggio forzato e i piani software ({rec} per registrazione o {ai} per statistiche IA) sono senza vincoli né permanenza.",
    },
    "fr": {
        "faq5_q": "Quel est le délai de livraison des caméras Save My Play à {city} ?",
        "faq5_a": "Le délai de livraison du matériel à {city} est d'environ 4 semaines à compter de la confirmation de la commande. L'envoi comprend les fixations pour poteaux et les câbles de raccordement rapide.",
        "faq6_q": "Le club est-il propriétaire de son équipement vidéo ?",
        "faq6_a": "Oui, le matériel appartient à 100% au club via un paiement unique ({hw}). Il n'y a aucune location forcée et les abonnements logiciels ({rec} pour l'enregistrement ou {ai} pour les stats IA) sont sans engagement de durée.",
    },
    "de": {
        "faq5_q": "Wie lange dauert Versand und Lieferung der Save My Play Kameras nach {city}?",
        "faq5_a": "Die Lieferzeit der Hardware nach {city} beträgt ca. 4 Wochen ab Auftragsbestätigung. Die Lieferung umfasst die stabilen Pfostenhalterungen und Schnellverbindungskabel.",
        "faq6_q": "Ist der Club der vollständige Eigentümer der Hardware?",
        "faq6_a": "Ja, die Hardware geht durch eine einmalige Zahlung ({hw}) zu 100% in das Eigentum des Clubs über. Es gibt keine versteckte Miete, und die Software-Abos ({rec} für Aufnahme oder {ai} für KI-Statistiken) sind monatlich kündbar ohne Bindung.",
    },
    "sv": {
        "faq5_q": "Hur lång tid tar leveransen av Save My Play-kameror till {city}?",
        "faq5_a": "Leveranstiden för hårdvaran till {city} är cirka 4 veckor från orderbekräftelse. Försändelsen innehåller säkerhetsfästen för nätstolpar och snabbanslutningskablar.",
        "faq6_q": "Äger klubben kamerahårdvaran fullt ut?",
        "faq6_a": "Ja, klubben äger hårdvaran till 100% genom en engångsbetalning ({hw}). Det finns inga dolda hyresavtal, och mjukvaruabonnemangen ({rec} för inspelning eller {ai} för AI-statistik) har 0 månaders bindningstid.",
    },
    "pt": {
        "faq5_q": "Quanto tempo demora o envio e a entrega das câmaras Save My Play em {city}?",
        "faq5_a": "O prazo de entrega do equipamento em {city} é de aproximadamente 4 semanas após a confirmação da encomenda. O envio inclui os suportes de fixação a postes e os cabos de ligação rápida.",
        "faq6_q": "O clube é proprietário do equipamento de vídeo?",
        "faq6_a": "Sim, o hardware é propriedade a 100% do clube mediante pagamento único ({hw}). Não existe aluguer forçado e os planos de software ({rec} para gravação ou {ai} para estatísticas IA) funcionam mês a mês sem fidelização.",
    },
    "pt-br": {
        "faq5_q": "Quanto tempo leva o envio e entrega das câmeras Save My Play em {city}?",
        "faq5_a": "O prazo de entrega do hardware em {city} é de aproximadamente 4 semanas após a confirmação do pedido. O envio inclui os suportes de fixação em postes e cabos de conexão rápida.",
        "faq6_q": "O clube é proprietário definitivo dos equipamentos?",
        "faq6_a": "Sim, o hardware pertence 100% ao clube através de pagamento único ({hw}). Não há aluguel forçado e os planos de software ({rec} para gravação ou {ai} para estatísticas IA) são sem fidelidade.",
    },
    "nl": {
        "faq5_q": "Hoe lang duurt de levering van Save My Play camera's in {city}?",
        "faq5_a": "De levertijd van de hardware naar {city} bedraagt ongeveer 4 weken na orderbevestiging. De zending bevat stevige paalbevestigingen en snelaansluitkabels.",
        "faq6_q": "Is de club volledig eigenaar van het camerasysteem?",
        "faq6_a": "Ja, de hardware is 100% eigendom van de club via een eenmalige aankoop ({hw}). Er is geen verplichte lease en de softwareabonnementen ({rec} voor opname of {ai} voor AI-statistieken) zijn maandelijks opzegbaar zonder verplichtingen.",
    },
    "pl": {
        "faq5_q": "Ile czasu trwa dostawa kamer Save My Play do {city}?",
        "faq5_a": "Czas dostawy sprzętu do {city} wynosi około 4 tygodni od potwierdzenia zamówienia. Przesyłka zawiera solidne uchwyty słupowe oraz kable szybkiego montażu.",
        "faq6_q": "Czy klub staje się wyłącznym właścicielem sprzętu?",
        "faq6_a": "Tak, sprzęt przechodzi w 100% na własność klubu po jednorazowej opłacie ({hw}). Nie ma ukrytego wynajmu, a plany oprogramowania ({rec} za nagrywanie lub {ai} za statystyki AI) są elastyczne i bez okresu lojalnościowego.",
    },
    "da": {
        "faq5_q": "Hvor lang tid tager leveringen af Save My Play-kameraer til {city}?",
        "faq5_a": "Leveringstiden for hardwaren til {city} er cirka 4 uger fra ordrebekræftelse. Forsendelsen inkluderer solide stolpebeslag og kabler til hurtig tilslutning.",
        "faq6_q": "Ejer klubben kamerahardwaren fuldt ud?",
        "faq6_a": "Ja, klubben ejer hardwaren 100% gennem en engangsbetaling ({hw}). Der er ingen tvungen leasing, og softwareplanerne ({rec} for optagelse eller {ai} for AI-statistik) er uden bindingsperiode.",
    },
    "no": {
        "faq5_q": "Hvor lang tid tar leveringen av Save My Play-kameraer til {city}?",
        "faq5_a": "Leveringstiden for maskinvaren til {city} er omtrent 4 uker fra ordrebekreftelse. Forsendelsen inkluderer solide stolpefester og hurtigkoblingskabler.",
        "faq6_q": "Eier klubben kamerautstyret fullt ut?",
        "faq6_a": "Ja, klubben eier maskinvaren 100% via et engangskjøp ({hw}). Det er ingen skjulte leieavtaler, og programvareabonnementene ({rec} for opptak eller {ai} for AI-statistikk) er uten bindingstid.",
    },
    "fi": {
        "faq5_q": "Kuinka kauan Save My Play -kameroiden toimitus kestää kaupunkiin {city}?",
        "faq5_a": "Laitteiston toimitusaika kaupunkiin {city} on noin 4 viikkoa tilauksen vahvistamisesta. Toimitus sisältää tolppakiinnikkeet ja pikaliitäntäkaapelit.",
        "faq6_q": "Omistaako klubi kamerajärjestelmän kokonaan?",
        "faq6_a": "Kyllä, klubi omistaa laitteiston 100-prosenttisesti kertamaksulla ({hw}). Pakollisia laitevuokria ei ole, ja ohjelmistotilaukset ({rec} tallennukseen tai {ai} tekoälytilastoihin) ovat toistaiseksi voimassa ilman sitoutumisaikaa.",
    },
    "el": {
        "faq5_q": "Πόσο διαρκεί η αποστολή και παράδοση των καμερών Save My Play στην πόλη {city};",
        "faq5_a": "Ο χρόνος παράδοσης του εξοπλισμού στην πόλη {city} είναι περίπου 4 εβδομάδες από την επιβεβαίωση της παραγγελίας. Η αποστολή περιλαμβάνει βάσεις στερέωσης και καλώδια ταχείας σύνδεσης.",
        "faq6_q": "Ανήκει ο εξοπλισμός καμερών εξ ολοκλήρου στο club;",
        "faq6_a": "Ναι, ο εξοπλισμός ανήκει 100% στο club με εφάπαξ πληρωμή ({hw}). Δεν υπάρχουν κρυφά κόστη ενοικίασης και οι συνδρομές λογισμικού ({rec} ή {ai}) είναι μηνιαίες χωρίς καμία δέσμευση.",
    },
    "ar": {
        "faq5_q": "كم يستغرق شحن وتسليم كاميرات Save My Play إلى {city}؟",
        "faq5_a": "يستغرق وقت توصيل الأجهزة إلى {city} حوالي 4 أسابيع من تأكيد الطلب. تتضمن الشحنة دعامات التثبيت وكابلات التوصيل السريع.",
        "faq6_q": "هل يمتلك النادي نظام الكاميرات بالكامل؟",
        "faq6_a": "نعم، الأجهزة مملوكة للنادي بنسبة 100% عبر دفعة لمرة واحدة ({hw}). لا يوجد إيجار إجباري، وخطط البرامج ({rec} للتسجيل أو {ai} لإحصائيات الذكاء الاصطناعي) شهرية بدون أي التزام طويل الأجل.",
    },
    "cs": {
        "faq5_q": "Jak dlouho trvá doručení kamer Save My Play do města {city}?",
        "faq5_a": "Doba dodání hardwaru do města {city} je přibližně 4 týdny od potvrzení objednávky. Zásilka obsahuje pevné držáky na sloupky a kabely pro rychlé zapojení.",
        "faq6_q": "Vlastní klub kamerový hardware v plném rozsahu?",
        "faq6_a": "Ano, hardware je ve 100% vlastnictví klubu po jednorázové platbě ({hw}). Neexistuje žádný nucený pronájem a softwarové tarify ({rec} za záznam nebo {ai} za AI statistiky) jsou flexibilní bez vázanosti.",
    },
    "hr": {
        "faq5_q": "Koliko traje isporuka Save My Play kamera u grad {city}?",
        "faq5_a": "Rok isporuke opreme u {city} je otprilike 4 tjedna od potvrde narudžbe. Pošiljka uključuje nosače za stupove i kabele za brzo spajanje.",
        "faq6_q": "Je li klub u potpunom vlasništvu hardvera kamere?",
        "faq6_a": "Da, hardver je 100% u vlasništvu kluba jednokratnim plaćanjem ({hw}). Nema prisilnog najma, a softverske pretplate ({rec} za snimanje ili {ai} za AI statistiku) su bez ugovorne obveze.",
    },
    "ro": {
        "faq5_q": "Cât durează livrarea camerelor Save My Play în {city}?",
        "faq5_a": "Timpul de livrare a echipamentului în {city} este de aproximativ 4 săptămâni de la confirmarea comenzii. Coletul include suporturi sigure pentru stâlpi și cabluri de conectare rapidă.",
        "faq6_q": "Clubul deține în totalitate echipamentul video?",
        "faq6_a": "Da, hardware-ul este deținut 100% de club printr-o singură plată ({hw}). Nu există costuri ascunse de închiriere, iar abonamentele software ({rec} sau {ai}) sunt lunare fără perioadă minimă contractuală.",
    },
    "tr": {
        "faq5_q": "Save My Play kameralarının {city} şehrine teslimatı ne kadar sürer?",
        "faq5_a": "{city} şehrine donanım teslimat süresi sipariş onayından itibaren yaklaşık 4 haftadır. Gönderi, direk montaj aparatlarını ve hızlı bağlantı kablolarını içerir.",
        "faq6_q": "Kulüp kamera donanımının tam sahibi mi oluyor?",
        "faq6_a": "Evet, donanım tek seferlik ödeme ile ({hw}) %100 kulübün mülkiyetine geçer. Zorunlu kiralama yoktur ve yazılım planları ({rec} kayıt veya {ai} yapay zeka istatistikleri) taahhütsüzdür.",
    },
    "ja": {
        "faq5_q": "{city}へのSave My Playカメラの配送にはどれくらい時間がかかりますか？",
        "faq5_a": "ご注文確定後、{city}へのハードウェアのお届けは約4週間となります。頑丈なポール固定金具とクイック接続ケーブルが含まれています。",
        "faq6_q": "クラブ側がカメラ機器を完全に所有することになりますか？",
        "faq6_a": "はい、一括払い（{hw}）によりハードウェアは100%クラブの所有となります。強制的な機器リース契約はなく、ソフトウェアプラン（録画{rec}、AI分析{ai}）は縛りなしで月額利用可能です。",
    },
    "id": {
        "faq5_q": "Berapa lama pengiriman kamera Save My Play ke {city}?",
        "faq5_a": "Waktu pengiriman perangkat keras ke {city} adalah sekitar 4 minggu sejak konfirmasi pesanan. Pengiriman mencakup braket tiang kokoh dan kabel koneksi cepat.",
        "faq6_q": "Apakah klub memiliki perangkat kamera sepenuhnya?",
        "faq6_a": "Ya, perangkat keras 100% menjadi milik klub melalui pembayaran satu kali ({hw}). Tidak ada sewa wajib, dan paket langganan perangkat lunak ({rec} atau {ai}) fleksibel tanpa ikatan kontrak.",
    },
    "ca": {
        "faq5_q": "Quant triga l'enviament i lliurament de les càmeres Save My Play a {city}?",
        "faq5_a": "El termini de lliurament del maquinari a {city} és d'aproximadament 4 setmanes des de la confirmació de la comanda. L'enviament inclou les fixacions de seguretat per a pals i el cablejat de connexió ràpida.",
        "faq6_q": "El club és propietari del sistema de càmeres?",
        "faq6_a": "Sí, el maquinari és propietat al 100% del club mitjançant un pagament únic ({hw}). No hi ha quotes de lloguer forçoses i els serveis al núvol ({rec} per a enregistrament o {ai} per a estadístiques) són sense permanència.",
    }
}
