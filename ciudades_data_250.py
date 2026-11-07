# -*- coding: utf-8 -*-
"""
Top 5 ciudades más grandes y de mayor actividad de pádel para cada uno de los 50 países.
Estructurado por el slug del país con:
- name: Nombre nativo / local de la ciudad
- slug: Slug limpio para la URL (ej: madrid, stockholm, milano, paris)
- courts: Estimación de pistas del área metropolitana para credibilidad y contexto local
"""

CITIES_50 = {
    # 1. España
    "espana": [
        {"name": "Madrid", "slug": "madrid", "courts": 3200},
        {"name": "Barcelona", "slug": "barcelona", "courts": 1950},
        {"name": "Valencia", "slug": "valencia", "courts": 850},
        {"name": "Sevilla", "slug": "sevilla", "courts": 720},
        {"name": "Málaga", "slug": "malaga", "courts": 980},
    ],
    # 2. Italia
    "italia": [
        {"name": "Roma", "slug": "roma", "courts": 2100},
        {"name": "Milano", "slug": "milano", "courts": 1650},
        {"name": "Torino", "slug": "torino", "courts": 580},
        {"name": "Napoli", "slug": "napoli", "courts": 490},
        {"name": "Palermo", "slug": "palermo", "courts": 410},
    ],
    # 3. Argentina
    "argentina": [
        {"name": "Buenos Aires", "slug": "buenos-aires", "courts": 2800},
        {"name": "Córdoba", "slug": "cordoba", "courts": 850},
        {"name": "Rosario", "slug": "rosario", "courts": 620},
        {"name": "Mendoza", "slug": "mendoza", "courts": 440},
        {"name": "La Plata", "slug": "la-plata", "courts": 390},
    ],
    # 4. Suecia
    "suecia": [
        {"name": "Stockholm", "slug": "stockholm", "courts": 1200},
        {"name": "Göteborg", "slug": "goteborg", "courts": 820},
        {"name": "Malmö", "slug": "malmo", "courts": 510},
        {"name": "Uppsala", "slug": "uppsala", "courts": 280},
        {"name": "Västerås", "slug": "vasteras", "courts": 210},
    ],
    # 5. Francia
    "francia": [
        {"name": "Paris", "slug": "paris", "courts": 890},
        {"name": "Marseille", "slug": "marseille", "courts": 420},
        {"name": "Lyon", "slug": "lyon", "courts": 380},
        {"name": "Toulouse", "slug": "toulouse", "courts": 340},
        {"name": "Nice", "slug": "nice", "courts": 290},
    ],
    # 6. Países Bajos
    "paises-bajos": [
        {"name": "Amsterdam", "slug": "amsterdam", "courts": 610},
        {"name": "Rotterdam", "slug": "rotterdam", "courts": 430},
        {"name": "Den Haag", "slug": "den-haag", "courts": 350},
        {"name": "Utrecht", "slug": "utrecht", "courts": 310},
        {"name": "Eindhoven", "slug": "eindhoven", "courts": 260},
    ],
    # 7. México
    "mexico": [
        {"name": "Ciudad de México", "slug": "ciudad-de-mexico", "courts": 1150},
        {"name": "Guadalajara", "slug": "guadalajara", "courts": 580},
        {"name": "Monterrey", "slug": "monterrey", "courts": 640},
        {"name": "Puebla", "slug": "puebla", "courts": 320},
        {"name": "Cancún", "slug": "cancun", "courts": 280},
    ],
    # 8. Chile
    "chile": [
        {"name": "Santiago", "slug": "santiago", "courts": 1400},
        {"name": "Valparaíso", "slug": "valparaiso", "courts": 360},
        {"name": "Concepción", "slug": "concepcion", "courts": 310},
        {"name": "Antofagasta", "slug": "antofagasta", "courts": 220},
        {"name": "La Serena", "slug": "la-serena", "courts": 210},
    ],
    # 9. Bélgica
    "belgica": [
        {"name": "Bruxelles", "slug": "bruxelles", "courts": 480},
        {"name": "Antwerpen", "slug": "antwerpen", "courts": 420},
        {"name": "Gent", "slug": "gent", "courts": 330},
        {"name": "Liège", "slug": "liege", "courts": 260},
        {"name": "Brugge", "slug": "brugge", "courts": 210},
    ],
    # 10. Paraguay
    "paraguay": [
        {"name": "Asunción", "slug": "asuncion", "courts": 520},
        {"name": "Ciudad del Este", "slug": "ciudad-del-este", "courts": 280},
        {"name": "San Lorenzo", "slug": "san-lorenzo", "courts": 190},
        {"name": "Luque", "slug": "luque", "courts": 180},
        {"name": "Encarnación", "slug": "encarnacion", "courts": 140},
    ],
    # 11. Dinamarca
    "dinamarca": [
        {"name": "København", "slug": "kobenhavn", "courts": 550},
        {"name": "Aarhus", "slug": "aarhus", "courts": 310},
        {"name": "Odense", "slug": "odense", "courts": 190},
        {"name": "Aalborg", "slug": "aalborg", "courts": 170},
        {"name": "Esbjerg", "slug": "esbjerg", "courts": 120},
    ],
    # 12. Portugal
    "portugal": [
        {"name": "Lisboa", "slug": "lisboa", "courts": 680},
        {"name": "Porto", "slug": "porto", "courts": 490},
        {"name": "Braga", "slug": "braga", "courts": 220},
        {"name": "Coimbra", "slug": "coimbra", "courts": 160},
        {"name": "Faro", "slug": "faro", "courts": 180},
    ],
    # 13. Egipto
    "egipto": [
        {"name": "Cairo", "slug": "cairo", "courts": 650},
        {"name": "Alexandria", "slug": "alexandria", "courts": 280},
        {"name": "Giza", "slug": "giza", "courts": 240},
        {"name": "New Cairo", "slug": "new-cairo", "courts": 260},
        {"name": "El Gouna", "slug": "el-gouna", "courts": 110},
    ],
    # 14. Sudáfrica
    "sudafrica": [
        {"name": "Johannesburg", "slug": "johannesburg", "courts": 380},
        {"name": "Cape Town", "slug": "cape-town", "courts": 420},
        {"name": "Durban", "slug": "durban", "courts": 210},
        {"name": "Pretoria", "slug": "pretoria", "courts": 240},
        {"name": "Gqeberha", "slug": "gqeberha", "courts": 120},
    ],
    # 15. Arabia Saudí
    "arabia-saudi": [
        {"name": "Riyadh", "slug": "riyadh", "courts": 690},
        {"name": "Jeddah", "slug": "jeddah", "courts": 420},
        {"name": "Dammam", "slug": "dammam", "courts": 260},
        {"name": "Khobar", "slug": "khobar", "courts": 230},
        {"name": "Medina", "slug": "medina", "courts": 120},
    ],
    # 16. Finlandia
    "finlandia": [
        {"name": "Helsinki", "slug": "helsinki", "courts": 380},
        {"name": "Espoo", "slug": "espoo", "courts": 220},
        {"name": "Tampere", "slug": "tampere", "courts": 210},
        {"name": "Vantaa", "slug": "vantaa", "courts": 180},
        {"name": "Turku", "slug": "turku", "courts": 160},
    ],
    # 17. Gran Bretaña
    "gran-bretana": [
        {"name": "London", "slug": "london", "courts": 580},
        {"name": "Manchester", "slug": "manchester", "courts": 240},
        {"name": "Birmingham", "slug": "birmingham", "courts": 210},
        {"name": "Bristol", "slug": "bristol", "courts": 170},
        {"name": "Edinburgh", "slug": "edinburgh", "courts": 150},
    ],
    # 18. Brasil
    "brasil": [
        {"name": "São Paulo", "slug": "sao-paulo", "courts": 720},
        {"name": "Porto Alegre", "slug": "porto-alegre", "courts": 510},
        {"name": "Curitiba", "slug": "curitiba", "courts": 390},
        {"name": "Rio de Janeiro", "slug": "rio-de-janeiro", "courts": 340},
        {"name": "Belo Horizonte", "slug": "belo-horizonte", "courts": 260},
    ],
    # 19. Emiratos Árabes Unidos
    "emiratos-arabes-unidos": [
        {"name": "Dubai", "slug": "dubai", "courts": 780},
        {"name": "Abu Dhabi", "slug": "abu-dhabi", "courts": 360},
        {"name": "Sharjah", "slug": "sharjah", "courts": 190},
        {"name": "Ajman", "slug": "ajman", "courts": 110},
        {"name": "Ras Al Khaimah", "slug": "ras-al-khaimah", "courts": 90},
    ],
    # 20. Alemania
    "alemania": [
        {"name": "Berlin", "slug": "berlin", "courts": 340},
        {"name": "München", "slug": "munchen", "courts": 310},
        {"name": "Frankfurt", "slug": "frankfurt", "courts": 260},
        {"name": "Köln", "slug": "koln", "courts": 240},
        {"name": "Hamburg", "slug": "hamburg", "courts": 220},
    ],
    # 21. Estados Unidos
    "estados-unidos": [
        {"name": "Miami", "slug": "miami", "courts": 620},
        {"name": "Houston", "slug": "houston", "courts": 310},
        {"name": "Austin", "slug": "austin", "courts": 280},
        {"name": "Los Angeles", "slug": "los-angeles", "courts": 260},
        {"name": "New York", "slug": "new-york", "courts": 240},
    ],
    # 22. Noruega
    "noruega": [
        {"name": "Oslo", "slug": "oslo", "courts": 310},
        {"name": "Bergen", "slug": "bergen", "courts": 190},
        {"name": "Trondheim", "slug": "trondheim", "courts": 160},
        {"name": "Stavanger", "slug": "stavanger", "courts": 150},
        {"name": "Drammen", "slug": "drammen", "courts": 110},
    ],
    # 23. Austria
    "austria": [
        {"name": "Wien", "slug": "wien", "courts": 320},
        {"name": "Graz", "slug": "graz", "courts": 180},
        {"name": "Linz", "slug": "linz", "courts": 140},
        {"name": "Salzburg", "slug": "salzburg", "courts": 130},
        {"name": "Innsbruck", "slug": "innsbruck", "courts": 110},
    ],
    # 24. Suiza
    "suiza": [
        {"name": "Zürich", "slug": "zurich", "courts": 280},
        {"name": "Genève", "slug": "geneve", "courts": 210},
        {"name": "Basel", "slug": "basel", "courts": 170},
        {"name": "Lausanne", "slug": "lausanne", "courts": 150},
        {"name": "Bern", "slug": "bern", "courts": 130},
    ],
    # 25. Polonia
    "polonia": [
        {"name": "Warszawa", "slug": "warszawa", "courts": 290},
        {"name": "Kraków", "slug": "krakow", "courts": 190},
        {"name": "Wrocław", "slug": "wroclaw", "courts": 160},
        {"name": "Poznań", "slug": "poznan", "courts": 140},
        {"name": "Gdańsk", "slug": "gdansk", "courts": 120},
    ],
    # 26. Andorra
    "andorra": [
        {"name": "Andorra la Vella", "slug": "andorra-la-vella", "courts": 55},
        {"name": "Escaldes-Engordany", "slug": "escaldes-engordany", "courts": 40},
        {"name": "Sant Julià de Lòria", "slug": "sant-julia-de-loria", "courts": 28},
        {"name": "La Massana", "slug": "la-massana", "courts": 22},
        {"name": "Encamp", "slug": "encamp", "courts": 18},
    ],
    # 27. Grecia
    "grecia": [
        {"name": "Athina", "slug": "athina", "courts": 260},
        {"name": "Thessaloniki", "slug": "thessaloniki", "courts": 180},
        {"name": "Patra", "slug": "patra", "courts": 90},
        {"name": "Heraklion", "slug": "heraklion", "courts": 80},
        {"name": "Larissa", "slug": "larissa", "courts": 70},
    ],
    # 28. Qatar
    "qatar": [
        {"name": "Doha", "slug": "doha", "courts": 380},
        {"name": "Al Rayyan", "slug": "al-rayyan", "courts": 190},
        {"name": "Al Wakrah", "slug": "al-wakrah", "courts": 120},
        {"name": "Lusail", "slug": "lusail", "courts": 160},
        {"name": "Al Khor", "slug": "al-khor", "courts": 80},
    ],
    # 29. Colombia
    "colombia": [
        {"name": "Bogotá", "slug": "bogota", "courts": 420},
        {"name": "Medellín", "slug": "medellin", "courts": 380},
        {"name": "Cali", "slug": "cali", "courts": 210},
        {"name": "Barranquilla", "slug": "barranquilla", "courts": 180},
        {"name": "Bucaramanga", "slug": "bucaramanga", "courts": 140},
    ],
    # 30. Kuwait
    "kuwait": [
        {"name": "Kuwait City", "slug": "kuwait-city", "courts": 350},
        {"name": "Hawalli", "slug": "hawalli", "courts": 210},
        {"name": "Salmiya", "slug": "salmiya", "courts": 180},
        {"name": "Al Ahmadi", "slug": "al-ahmadi", "courts": 130},
        {"name": "Farwaniya", "slug": "farwaniya", "courts": 110},
    ],
    # 31. Croacia
    "croacia": [
        {"name": "Zagreb", "slug": "zagreb", "courts": 180},
        {"name": "Split", "slug": "split", "courts": 110},
        {"name": "Rijeka", "slug": "rijeka", "courts": 80},
        {"name": "Osijek", "slug": "osijek", "courts": 60},
        {"name": "Zadar", "slug": "zadar", "courts": 50},
    ],
    # 32. Indonesia
    "indonesia": [
        {"name": "Jakarta", "slug": "jakarta", "courts": 290},
        {"name": "Bali", "slug": "bali", "courts": 310},
        {"name": "Surabaya", "slug": "surabaya", "courts": 140},
        {"name": "Bandung", "slug": "bandung", "courts": 120},
        {"name": "Medan", "slug": "medan", "courts": 90},
    ],
    # 33. Marruecos
    "marruecos": [
        {"name": "Casablanca", "slug": "casablanca", "courts": 240},
        {"name": "Rabat", "slug": "rabat", "courts": 160},
        {"name": "Marrakech", "slug": "marrakech", "courts": 180},
        {"name": "Tanger", "slug": "tanger", "courts": 130},
        {"name": "Agadir", "slug": "agadir", "courts": 90},
    ],
    # 34. Irlanda
    "irlanda": [
        {"name": "Dublin", "slug": "dublin", "courts": 210},
        {"name": "Cork", "slug": "cork", "courts": 90},
        {"name": "Galway", "slug": "galway", "courts": 70},
        {"name": "Limerick", "slug": "limerick", "courts": 60},
        {"name": "Waterford", "slug": "waterford", "courts": 40},
    ],
    # 35. Turquía
    "turquia": [
        {"name": "Istanbul", "slug": "istanbul", "courts": 260},
        {"name": "Ankara", "slug": "ankara", "courts": 140},
        {"name": "Izmir", "slug": "izmir", "courts": 130},
        {"name": "Antalya", "slug": "antalya", "courts": 150},
        {"name": "Bursa", "slug": "bursa", "courts": 80},
    ],
    # 36. Túnez
    "tunez": [
        {"name": "Tunis", "slug": "tunis", "courts": 160},
        {"name": "Sousse", "slug": "sousse", "courts": 90},
        {"name": "Sfax", "slug": "sfax", "courts": 70},
        {"name": "Hammamet", "slug": "hammamet", "courts": 60},
        {"name": "Djerba", "slug": "djerba", "courts": 40},
    ],
    # 37. Uruguay
    "uruguay": [
        {"name": "Montevideo", "slug": "montevideo", "courts": 240},
        {"name": "Punta del Este", "slug": "punta-del-este", "courts": 140},
        {"name": "Maldonado", "slug": "maldonado", "courts": 90},
        {"name": "Salto", "slug": "salto", "courts": 60},
        {"name": "Paysandú", "slug": "paysandu", "courts": 50},
    ],
    # 38. Venezuela
    "venezuela": [
        {"name": "Caracas", "slug": "caracas", "courts": 290},
        {"name": "Valencia", "slug": "valencia-ve", "courts": 160},
        {"name": "Maracaibo", "slug": "maracaibo", "courts": 130},
        {"name": "Barquisimeto", "slug": "barquisimeto", "courts": 110},
        {"name": "Maracay", "slug": "maracay", "courts": 90},
    ],
    # 39. Costa Rica
    "costa-rica": [
        {"name": "San José", "slug": "san-jose", "courts": 190},
        {"name": "Escazú", "slug": "escazu", "courts": 110},
        {"name": "Santa Ana", "slug": "santa-ana", "courts": 90},
        {"name": "Heredia", "slug": "heredia", "courts": 80},
        {"name": "Alajuela", "slug": "alajuela", "courts": 70},
    ],
    # 40. República Dominicana
    "republica-dominicana": [
        {"name": "Santo Domingo", "slug": "santo-domingo", "courts": 220},
        {"name": "Punta Cana", "slug": "punta-cana", "courts": 160},
        {"name": "Santiago de los Caballeros", "slug": "santiago-de-los-caballeros", "courts": 90},
        {"name": "La Romana", "slug": "la-romana", "courts": 70},
        {"name": "Puerto Plata", "slug": "puerto-plata", "courts": 50},
    ],
    # 41. Panamá
    "panama": [
        {"name": "Ciudad de Panamá", "slug": "ciudad-de-panama", "courts": 240},
        {"name": "Costa del Este", "slug": "costa-del-este", "courts": 90},
        {"name": "San Francisco", "slug": "san-francisco-pa", "courts": 80},
        {"name": "Chorrera", "slug": "chorrera", "courts": 50},
        {"name": "David", "slug": "david", "courts": 40},
    ],
    # 42. Ecuador
    "ecuador": [
        {"name": "Quito", "slug": "quito", "courts": 210},
        {"name": "Guayaquil", "slug": "guayaquil", "courts": 190},
        {"name": "Cuenca", "slug": "cuenca", "courts": 90},
        {"name": "Samborondón", "slug": "samborondon", "courts": 80},
        {"name": "Manta", "slug": "manta", "courts": 50},
    ],
    # 43. Australia
    "australia": [
        {"name": "Sydney", "slug": "sydney", "courts": 240},
        {"name": "Melbourne", "slug": "melbourne", "courts": 210},
        {"name": "Brisbane", "slug": "brisbane", "courts": 140},
        {"name": "Perth", "slug": "perth", "courts": 110},
        {"name": "Gold Coast", "slug": "gold-coast", "courts": 90},
    ],
    # 44. Japón
    "japon": [
        {"name": "Tokyo", "slug": "tokyo", "courts": 230},
        {"name": "Osaka", "slug": "osaka", "courts": 140},
        {"name": "Nagoya", "slug": "nagoya", "courts": 90},
        {"name": "Fukuoka", "slug": "fukuoka", "courts": 80},
        {"name": "Yokohama", "slug": "yokohama", "courts": 70},
    ],
    # 45. Líbano
    "libano": [
        {"name": "Beirut", "slug": "beirut", "courts": 180},
        {"name": "Jounieh", "slug": "jounieh", "courts": 90},
        {"name": "Tripoli", "slug": "tripoli", "courts": 60},
        {"name": "Byblos", "slug": "byblos", "courts": 50},
        {"name": "Saida", "slug": "saida", "courts": 40},
    ],
    # 46. Bahréin
    "bahrein": [
        {"name": "Manama", "slug": "manama", "courts": 160},
        {"name": "Riffa", "slug": "riffa", "courts": 90},
        {"name": "Muharraq", "slug": "muharraq", "courts": 70},
        {"name": "Hamad Town", "slug": "hamad-town", "courts": 50},
        {"name": "A'ali", "slug": "a-ali", "courts": 40},
    ],
    # 47. Omán
    "oman": [
        {"name": "Muscat", "slug": "muscat", "courts": 170},
        {"name": "Salalah", "slug": "salalah", "courts": 70},
        {"name": "Sohar", "slug": "sohar", "courts": 50},
        {"name": "Seeb", "slug": "seeb", "courts": 60},
        {"name": "Bawshar", "slug": "bawshar", "courts": 40},
    ],
    # 48. India
    "india": [
        {"name": "Mumbai", "slug": "mumbai", "courts": 190},
        {"name": "Bengaluru", "slug": "bengaluru", "courts": 170},
        {"name": "Delhi", "slug": "delhi", "courts": 160},
        {"name": "Hyderabad", "slug": "hyderabad", "courts": 120},
        {"name": "Goa", "slug": "goa", "courts": 80},
    ],
    # 49. República Checa
    "republica-checa": [
        {"name": "Praha", "slug": "praha", "courts": 180},
        {"name": "Brno", "slug": "brno", "courts": 90},
        {"name": "Ostrava", "slug": "ostrava", "courts": 60},
        {"name": "Plzeň", "slug": "plzen", "courts": 50},
        {"name": "Olomouc", "slug": "olomouc", "courts": 40},
    ],
    # 50. Rumanía
    "rumania": [
        {"name": "București", "slug": "bucuresti", "courts": 190},
        {"name": "Cluj-Napoca", "slug": "cluj-napoca", "courts": 90},
        {"name": "Timișoara", "slug": "timisoara", "courts": 70},
        {"name": "Iași", "slug": "iasi", "courts": 60},
        {"name": "Brașov", "slug": "brasov", "courts": 50},
    ],
}
