# atlas_economico.py
"""
Base de datos de países con variables económicas y de recursos normalizadas (0.0 - 1.0)
"""

ATLAS_MUNDIAL = {
    "USA": {
        "nombre": "Estados Unidos",
        "recursos_fosiles": 0.85,
        "potencial_renovable": 0.75,
        "tecnologia": 0.95,
        "capital_humano": 0.88,
        "tierra_arable": 0.72,
        "acceso_maritimo": 0.90,
        "pib_inicial": 25000  # Miles de millones USD
    },
    "China": {
        "nombre": "China",
        "recursos_fosiles": 0.70,
        "potencial_renovable": 0.65,
        "tecnologia": 0.85,
        "capital_humano": 0.75,
        "tierra_arable": 0.55,
        "acceso_maritimo": 0.80,
        "pib_inicial": 18000
    },
    "Russia": {
        "nombre": "Rusia",
        "recursos_fosiles": 0.95,
        "potencial_renovable": 0.40,
        "tecnologia": 0.65,
        "capital_humano": 0.70,
        "tierra_arable": 0.60,
        "acceso_maritimo": 0.75,
        "pib_inicial": 2000
    },
    "Germany": {
        "nombre": "Alemania",
        "recursos_fosiles": 0.30,
        "potencial_renovable": 0.70,
        "tecnologia": 0.92,
        "capital_humano": 0.90,
        "tierra_arable": 0.50,
        "acceso_maritimo": 0.60,
        "pib_inicial": 4500
    },
    "Japan": {
        "nombre": "Japón",
        "recursos_fosiles": 0.10,
        "potencial_renovable": 0.45,
        "tecnologia": 0.93,
        "capital_humano": 0.92,
        "tierra_arable": 0.25,
        "acceso_maritimo": 0.95,
        "pib_inicial": 4200
    },
    "Spain": {
        "nombre": "España",
        "recursos_fosiles": 0.20,
        "potencial_renovable": 0.85,
        "tecnologia": 0.75,
        "capital_humano": 0.80,
        "tierra_arable": 0.45,
        "acceso_maritimo": 0.88,
        "pib_inicial": 1600
    },
    "India": {
        "nombre": "India",
        "recursos_fosiles": 0.50,
        "potencial_renovable": 0.80,
        "tecnologia": 0.60,
        "capital_humano": 0.55,
        "tierra_arable": 0.70,
        "acceso_maritimo": 0.70,
        "pib_inicial": 3500
    },
    "Brazil": {
        "nombre": "Brasil",
        "recursos_fosiles": 0.65,
        "potencial_renovable": 0.90,
        "tecnologia": 0.55,
        "capital_humano": 0.60,
        "tierra_arable": 0.80,
        "acceso_maritimo": 0.85,
        "pib_inicial": 2000
    },
    "SaudiArabia": {
        "nombre": "Arabia Saudita",
        "recursos_fosiles": 1.0,
        "potencial_renovable": 0.70,
        "tecnologia": 0.50,
        "capital_humano": 0.55,
        "tierra_arable": 0.10,
        "acceso_maritimo": 0.80,
        "pib_inicial": 1100
    },
    "France": {
        "nombre": "Francia",
        "recursos_fosiles": 0.25,
        "potencial_renovable": 0.65,
        "tecnologia": 0.88,
        "capital_humano": 0.87,
        "tierra_arable": 0.55,
        "acceso_maritimo": 0.75,
        "pib_inicial": 3000
    },
    "UK": {
        "nombre": "Reino Unido",
        "recursos_fosiles": 0.40,
        "potencial_renovable": 0.75,
        "tecnologia": 0.90,
        "capital_humano": 0.88,
        "tierra_arable": 0.40,
        "acceso_maritimo": 0.95,
        "pib_inicial": 3200
    },
    "Mexico": {
        "nombre": "México",
        "recursos_fosiles": 0.60,
        "potencial_renovable": 0.70,
        "tecnologia": 0.50,
        "capital_humano": 0.58,
        "tierra_arable": 0.50,
        "acceso_maritimo": 0.82,
        "pib_inicial": 1500
    },
    "SouthKorea": {
        "nombre": "Corea del Sur",
        "recursos_fosiles": 0.15,
        "potencial_renovable": 0.40,
        "tecnologia": 0.94,
        "capital_humano": 0.91,
        "tierra_arable": 0.30,
        "acceso_maritimo": 0.90,
        "pib_inicial": 1800
    },
    "Australia": {
        "nombre": "Australia",
        "recursos_fosiles": 0.88,
        "potencial_renovable": 0.92,
        "tecnologia": 0.82,
        "capital_humano": 0.85,
        "tierra_arable": 0.35,
        "acceso_maritimo": 1.0,
        "pib_inicial": 1700
    },
    "Canada": {
        "nombre": "Canadá",
        "recursos_fosiles": 0.90,
        "potencial_renovable": 0.88,
        "tecnologia": 0.85,
        "capital_humano": 0.89,
        "tierra_arable": 0.50,
        "acceso_maritimo": 0.88,
        "pib_inicial": 2200
    },
    "Italy": {
        "nombre": "Italia",
        "recursos_fosiles": 0.25,
        "potencial_renovable": 0.60,
        "tecnologia": 0.80,
        "capital_humano": 0.82,
        "tierra_arable": 0.45,
        "acceso_maritimo": 0.85,
        "pib_inicial": 2200
    },
    "Argentina": {
        "nombre": "Argentina",
        "recursos_fosiles": 0.55,
        "potencial_renovable": 0.85,
        "tecnologia": 0.60,
        "capital_humano": 0.70,
        "tierra_arable": 0.75,
        "acceso_maritimo": 0.70,
        "pib_inicial": 630
    },
    "Turkey": {
        "nombre": "Turquía",
        "recursos_fosiles": 0.35,
        "potencial_renovable": 0.70,
        "tecnologia": 0.65,
        "capital_humano": 0.68,
        "tierra_arable": 0.55,
        "acceso_maritimo": 0.80,
        "pib_inicial": 906
    },
    "Indonesia": {
        "nombre": "Indonesia",
        "recursos_fosiles": 0.60,
        "potencial_renovable": 0.75,
        "tecnologia": 0.55,
        "capital_humano": 0.58,
        "tierra_arable": 0.50,
        "acceso_maritimo": 0.95,
        "pib_inicial": 1300
    },
    "Nigeria": {
        "nombre": "Nigeria",
        "recursos_fosiles": 0.80,
        "potencial_renovable": 0.70,
        "tecnologia": 0.40,
        "capital_humano": 0.45,
        "tierra_arable": 0.60,
        "acceso_maritimo": 0.75,
        "pib_inicial": 477
    },
    "Egypt": {
        "nombre": "Egipto",
        "recursos_fosiles": 0.50,
        "potencial_renovable": 0.85,
        "tecnologia": 0.50,
        "capital_humano": 0.55,
        "tierra_arable": 0.30,
        "acceso_maritimo": 0.80,
        "pib_inicial": 476
    },
    "Poland": {
        "nombre": "Polonia",
        "recursos_fosiles": 0.45,
        "potencial_renovable": 0.55,
        "tecnologia": 0.70,
        "capital_humano": 0.75,
        "tierra_arable": 0.55,
        "acceso_maritimo": 0.60,
        "pib_inicial": 688
    },
    "Thailand": {
        "nombre": "Tailandia",
        "recursos_fosiles": 0.35,
        "potencial_renovable": 0.65,
        "tecnologia": 0.60,
        "capital_humano": 0.65,
        "tierra_arable": 0.50,
        "acceso_maritimo": 0.85,
        "pib_inicial": 536
    },
    "Netherlands": {
        "nombre": "Países Bajos",
        "recursos_fosiles": 0.40,
        "potencial_renovable": 0.75,
        "tecnologia": 0.90,
        "capital_humano": 0.92,
        "tierra_arable": 0.40,
        "acceso_maritimo": 0.95,
        "pib_inicial": 1070
    },
    "SouthAfrica": {
        "nombre": "Sudáfrica",
        "recursos_fosiles": 0.75,
        "potencial_renovable": 0.80,
        "tecnologia": 0.55,
        "capital_humano": 0.60,
        "tierra_arable": 0.40,
        "acceso_maritimo": 0.85,
        "pib_inicial": 420
    },
    # Europa
    "Norway": {
        "nombre": "Noruega",
        "recursos_fosiles": 0.95,
        "potencial_renovable": 0.95,
        "tecnologia": 0.92,
        "capital_humano": 0.95,
        "tierra_arable": 0.20,
        "acceso_maritimo": 1.0,
        "pib_inicial": 580
    },
    "Sweden": {
        "nombre": "Suecia",
        "recursos_fosiles": 0.30,
        "potencial_renovable": 0.90,
        "tecnologia": 0.93,
        "capital_humano": 0.94,
        "tierra_arable": 0.35,
        "acceso_maritimo": 0.85,
        "pib_inicial": 635
    },
    "Finland": {
        "nombre": "Finlandia",
        "recursos_fosiles": 0.25,
        "potencial_renovable": 0.85,
        "tecnologia": 0.91,
        "capital_humano": 0.93,
        "tierra_arable": 0.30,
        "acceso_maritimo": 0.80,
        "pib_inicial": 301
    },
    "Denmark": {
        "nombre": "Dinamarca",
        "recursos_fosiles": 0.35,
        "potencial_renovable": 0.88,
        "tecnologia": 0.90,
        "capital_humano": 0.92,
        "tierra_arable": 0.55,
        "acceso_maritimo": 0.95,
        "pib_inicial": 405
    },
    "Belgium": {
        "nombre": "Bélgica",
        "recursos_fosiles": 0.20,
        "potencial_renovable": 0.55,
        "tecnologia": 0.87,
        "capital_humano": 0.88,
        "tierra_arable": 0.45,
        "acceso_maritimo": 0.90,
        "pib_inicial": 632
    },
    "Switzerland": {
        "nombre": "Suiza",
        "recursos_fosiles": 0.15,
        "potencial_renovable": 0.85,
        "tecnologia": 0.95,
        "capital_humano": 0.96,
        "tierra_arable": 0.25,
        "acceso_maritimo": 0.0,
        "pib_inicial": 869
    },
    "Austria": {
        "nombre": "Austria",
        "recursos_fosiles": 0.25,
        "potencial_renovable": 0.80,
        "tecnologia": 0.85,
        "capital_humano": 0.87,
        "tierra_arable": 0.38,
        "acceso_maritimo": 0.0,
        "pib_inicial": 516
    },
    "Portugal": {
        "nombre": "Portugal",
        "recursos_fosiles": 0.15,
        "potencial_renovable": 0.82,
        "tecnologia": 0.75,
        "capital_humano": 0.77,
        "tierra_arable": 0.40,
        "acceso_maritimo": 0.95,
        "pib_inicial": 287
    },
    "Greece": {
        "nombre": "Grecia",
        "recursos_fosiles": 0.25,
        "potencial_renovable": 0.75,
        "tecnologia": 0.70,
        "capital_humano": 0.72,
        "tierra_arable": 0.35,
        "acceso_maritimo": 0.95,
        "pib_inicial": 239
    },
    "Czech": {
        "nombre": "República Checa",
        "recursos_fosiles": 0.40,
        "potencial_renovable": 0.50,
        "tecnologia": 0.78,
        "capital_humano": 0.80,
        "tierra_arable": 0.50,
        "acceso_maritimo": 0.0,
        "pib_inicial": 330
    },
    "Romania": {
        "nombre": "Rumania",
        "recursos_fosiles": 0.50,
        "potencial_renovable": 0.70,
        "tecnologia": 0.65,
        "capital_humano": 0.68,
        "tierra_arable": 0.60,
        "acceso_maritimo": 0.70,
        "pib_inicial": 351
    },
    "Hungary": {
        "nombre": "Hungría",
        "recursos_fosiles": 0.35,
        "potencial_renovable": 0.55,
        "tecnologia": 0.72,
        "capital_humano": 0.74,
        "tierra_arable": 0.55,
        "acceso_maritimo": 0.0,
        "pib_inicial": 212
    },
    "Ireland": {
        "nombre": "Irlanda",
        "recursos_fosiles": 0.25,
        "potencial_renovable": 0.88,
        "tecnologia": 0.89,
        "capital_humano": 0.90,
        "tierra_arable": 0.40,
        "acceso_maritimo": 1.0,
        "pib_inicial": 563
    },
    "Ukraine": {
        "nombre": "Ucrania",
        "recursos_fosiles": 0.55,
        "potencial_renovable": 0.65,
        "tecnologia": 0.60,
        "capital_humano": 0.70,
        "tierra_arable": 0.75,
        "acceso_maritimo": 0.70,
        "pib_inicial": 200
    },
    # Asia-Pacífico
    "Vietnam": {
        "nombre": "Vietnam",
        "recursos_fosiles": 0.45,
        "potencial_renovable": 0.70,
        "tecnologia": 0.58,
        "capital_humano": 0.62,
        "tierra_arable": 0.50,
        "acceso_maritimo": 0.90,
        "pib_inicial": 433
    },
    "Philippines": {
        "nombre": "Filipinas",
        "recursos_fosiles": 0.35,
        "potencial_renovable": 0.80,
        "tecnologia": 0.55,
        "capital_humano": 0.60,
        "tierra_arable": 0.45,
        "acceso_maritimo": 0.95,
        "pib_inicial": 440
    },
    "Malaysia": {
        "nombre": "Malasia",
        "recursos_fosiles": 0.65,
        "potencial_renovable": 0.75,
        "tecnologia": 0.70,
        "capital_humano": 0.72,
        "tierra_arable": 0.30,
        "acceso_maritimo": 0.95,
        "pib_inicial": 447
    },
    "Singapore": {
        "nombre": "Singapur",
        "recursos_fosiles": 0.05,
        "potencial_renovable": 0.30,
        "tecnologia": 0.97,
        "capital_humano": 0.96,
        "tierra_arable": 0.05,
        "acceso_maritimo": 1.0,
        "pib_inicial": 515
    },
    "Bangladesh": {
        "nombre": "Bangladesh",
        "recursos_fosiles": 0.30,
        "potencial_renovable": 0.60,
        "tecnologia": 0.45,
        "capital_humano": 0.50,
        "tierra_arable": 0.65,
        "acceso_maritimo": 0.75,
        "pib_inicial": 460
    },
    "Pakistan": {
        "nombre": "Pakistán",
        "recursos_fosiles": 0.40,
        "potencial_renovable": 0.70,
        "tecnologia": 0.48,
        "capital_humano": 0.52,
        "tierra_arable": 0.55,
        "acceso_maritimo": 0.75,
        "pib_inicial": 375
    },
    "NewZealand": {
        "nombre": "Nueva Zelanda",
        "recursos_fosiles": 0.50,
        "potencial_renovable": 0.92,
        "tecnologia": 0.83,
        "capital_humano": 0.88,
        "tierra_arable": 0.40,
        "acceso_maritimo": 1.0,
        "pib_inicial": 252
    },
    # América
    "Colombia": {
        "nombre": "Colombia",
        "recursos_fosiles": 0.70,
        "potencial_renovable": 0.85,
        "tecnologia": 0.58,
        "capital_humano": 0.62,
        "tierra_arable": 0.50,
        "acceso_maritimo": 0.85,
        "pib_inicial": 380
    },
    "Chile": {
        "nombre": "Chile",
        "recursos_fosiles": 0.45,
        "potencial_renovable": 0.88,
        "tecnologia": 0.68,
        "capital_humano": 0.72,
        "tierra_arable": 0.25,
        "acceso_maritimo": 1.0,
        "pib_inicial": 344
    },
    "Peru": {
        "nombre": "Perú",
        "recursos_fosiles": 0.55,
        "potencial_renovable": 0.80,
        "tecnologia": 0.52,
        "capital_humano": 0.58,
        "tierra_arable": 0.35,
        "acceso_maritimo": 0.85,
        "pib_inicial": 268
    },
    "Venezuela": {
        "nombre": "Venezuela",
        "recursos_fosiles": 0.98,
        "potencial_renovable": 0.85,
        "tecnologia": 0.45,
        "capital_humano": 0.55,
        "tierra_arable": 0.40,
        "acceso_maritimo": 0.85,
        "pib_inicial": 100
    },
    "Ecuador": {
        "nombre": "Ecuador",
        "recursos_fosiles": 0.60,
        "potencial_renovable": 0.75,
        "tecnologia": 0.50,
        "capital_humano": 0.55,
        "tierra_arable": 0.45,
        "acceso_maritimo": 0.80,
        "pib_inicial": 121
    },
    "Cuba": {
        "nombre": "Cuba",
        "recursos_fosiles": 0.30,
        "potencial_renovable": 0.65,
        "tecnologia": 0.52,
        "capital_humano": 0.70,
        "tierra_arable": 0.45,
        "acceso_maritimo": 0.95,
        "pib_inicial": 107
    },
    # África
    "Kenya": {
        "nombre": "Kenia",
        "recursos_fosiles": 0.25,
        "potencial_renovable": 0.80,
        "tecnologia": 0.48,
        "capital_humano": 0.52,
        "tierra_arable": 0.50,
        "acceso_maritimo": 0.75,
        "pib_inicial": 130
    },
    "Ethiopia": {
        "nombre": "Etiopía",
        "recursos_fosiles": 0.30,
        "potencial_renovable": 0.75,
        "tecnologia": 0.35,
        "capital_humano": 0.40,
        "tierra_arable": 0.55,
        "acceso_maritimo": 0.0,
        "pib_inicial": 156
    },
    "Ghana": {
        "nombre": "Ghana",
        "recursos_fosiles": 0.55,
        "potencial_renovable": 0.70,
        "tecnologia": 0.45,
        "capital_humano": 0.50,
        "tierra_arable": 0.55,
        "acceso_maritimo": 0.80,
        "pib_inicial": 77
    },
    "Morocco": {
        "nombre": "Marruecos",
        "recursos_fosiles": 0.25,
        "potencial_renovable": 0.85,
        "tecnologia": 0.55,
        "capital_humano": 0.58,
        "tierra_arable": 0.45,
        "acceso_maritimo": 0.90,
        "pib_inicial": 143
    },
    "Algeria": {
        "nombre": "Argelia",
        "recursos_fosiles": 0.85,
        "potencial_renovable": 0.88,
        "tecnologia": 0.50,
        "capital_humano": 0.55,
        "tierra_arable": 0.25,
        "acceso_maritimo": 0.80,
        "pib_inicial": 226
    },
    # Medio Oriente
    "Iran": {
        "nombre": "Irán",
        "recursos_fosiles": 0.95,
        "potencial_renovable": 0.75,
        "tecnologia": 0.62,
        "capital_humano": 0.68,
        "tierra_arable": 0.35,
        "acceso_maritimo": 0.85,
        "pib_inicial": 389
    },
    "UAE": {
        "nombre": "Emiratos Árabes Unidos",
        "recursos_fosiles": 0.95,
        "potencial_renovable": 0.85,
        "tecnologia": 0.85,
        "capital_humano": 0.82,
        "tierra_arable": 0.05,
        "acceso_maritimo": 0.95,
        "pib_inicial": 509
    },
    "Israel": {
        "nombre": "Israel",
        "recursos_fosiles": 0.35,
        "potencial_renovable": 0.85,
        "tecnologia": 0.95,
        "capital_humano": 0.92,
        "tierra_arable": 0.25,
        "acceso_maritimo": 0.80,
        "pib_inicial": 530
    },
    "Qatar": {
        "nombre": "Catar",
        "recursos_fosiles": 0.98,
        "potencial_renovable": 0.80,
        "tecnologia": 0.75,
        "capital_humano": 0.72,
        "tierra_arable": 0.05,
        "acceso_maritimo": 0.95,
        "pib_inicial": 237
    },
    "Kuwait": {
        "nombre": "Kuwait",
        "recursos_fosiles": 0.95,
        "potencial_renovable": 0.75,
        "tecnologia": 0.70,
        "capital_humano": 0.68,
        "tierra_arable": 0.05,
        "acceso_maritimo": 0.90,
        "pib_inicial": 185
    },
    # Más países importantes
    "NorthKorea": {
        "nombre": "Corea del Norte",
        "recursos_fosiles": 0.45,
        "potencial_renovable": 0.60,
        "tecnologia": 0.45,
        "capital_humano": 0.58,
        "tierra_arable": 0.35,
        "acceso_maritimo": 0.70,
        "pib_inicial": 40
    },
    "Taiwan": {
        "nombre": "Taiwán",
        "recursos_fosiles": 0.10,
        "potencial_renovable": 0.45,
        "tecnologia": 0.92,
        "capital_humano": 0.90,
        "tierra_arable": 0.30,
        "acceso_maritimo": 1.0,
        "pib_inicial": 790
    },
    "HongKong": {
        "nombre": "Hong Kong",
        "recursos_fosiles": 0.0,
        "potencial_renovable": 0.20,
        "tecnologia": 0.94,
        "capital_humano": 0.92,
        "tierra_arable": 0.05,
        "acceso_maritimo": 1.0,
        "pib_inicial": 382
    },
    # Europa adicional
    "Serbia": {
        "nombre": "Serbia",
        "recursos_fosiles": 0.40,
        "potencial_renovable": 0.60,
        "tecnologia": 0.62,
        "capital_humano": 0.68,
        "tierra_arable": 0.55,
        "acceso_maritimo": 0.0,
        "pib_inicial": 63
    },
    "Croatia": {
        "nombre": "Croacia",
        "recursos_fosiles": 0.30,
        "potencial_renovable": 0.65,
        "tecnologia": 0.70,
        "capital_humano": 0.73,
        "tierra_arable": 0.45,
        "acceso_maritimo": 0.95,
        "pib_inicial": 70
    },
    "Bulgaria": {
        "nombre": "Bulgaria",
        "recursos_fosiles": 0.35,
        "potencial_renovable": 0.60,
        "tecnologia": 0.65,
        "capital_humano": 0.70,
        "tierra_arable": 0.50,
        "acceso_maritimo": 0.75,
        "pib_inicial": 89
    },
    "Slovakia": {
        "nombre": "Eslovaquia",
        "recursos_fosiles": 0.30,
        "potencial_renovable": 0.55,
        "tecnologia": 0.75,
        "capital_humano": 0.78,
        "tierra_arable": 0.48,
        "acceso_maritimo": 0.0,
        "pib_inicial": 115
    },
    "Slovenia": {
        "nombre": "Eslovenia",
        "recursos_fosiles": 0.25,
        "potencial_renovable": 0.70,
        "tecnologia": 0.80,
        "capital_humano": 0.83,
        "tierra_arable": 0.35,
        "acceso_maritimo": 0.60,
        "pib_inicial": 63
    },
    "Lithuania": {
        "nombre": "Lituania",
        "recursos_fosiles": 0.20,
        "potencial_renovable": 0.60,
        "tecnologia": 0.73,
        "capital_humano": 0.78,
        "tierra_arable": 0.50,
        "acceso_maritimo": 0.75,
        "pib_inicial": 71
    },
    "Latvia": {
        "nombre": "Letonia",
        "recursos_fosiles": 0.20,
        "potencial_renovable": 0.65,
        "tecnologia": 0.70,
        "capital_humano": 0.75,
        "tierra_arable": 0.45,
        "acceso_maritimo": 0.80,
        "pib_inicial": 43
    },
    "Estonia": {
        "nombre": "Estonia",
        "recursos_fosiles": 0.45,
        "potencial_renovable": 0.70,
        "tecnologia": 0.85,
        "capital_humano": 0.88,
        "tierra_arable": 0.35,
        "acceso_maritimo": 0.85,
        "pib_inicial": 38
    },
    "Belarus": {
        "nombre": "Bielorrusia",
        "recursos_fosiles": 0.35,
        "potencial_renovable": 0.50,
        "tecnologia": 0.60,
        "capital_humano": 0.72,
        "tierra_arable": 0.55,
        "acceso_maritimo": 0.0,
        "pib_inicial": 72
    },
    "Iceland": {
        "nombre": "Islandia",
        "recursos_fosiles": 0.10,
        "potencial_renovable": 1.0,
        "tecnologia": 0.88,
        "capital_humano": 0.92,
        "tierra_arable": 0.05,
        "acceso_maritimo": 1.0,
        "pib_inicial": 28
    },
    "Luxembourg": {
        "nombre": "Luxemburgo",
        "recursos_fosiles": 0.05,
        "potencial_renovable": 0.40,
        "tecnologia": 0.92,
        "capital_humano": 0.93,
        "tierra_arable": 0.30,
        "acceso_maritimo": 0.0,
        "pib_inicial": 87
    },
    # Asia adicional
    "Myanmar": {
        "nombre": "Myanmar",
        "recursos_fosiles": 0.55,
        "potencial_renovable": 0.75,
        "tecnologia": 0.35,
        "capital_humano": 0.42,
        "tierra_arable": 0.50,
        "acceso_maritimo": 0.80,
        "pib_inicial": 65
    },
    "Cambodia": {
        "nombre": "Camboya",
        "recursos_fosiles": 0.30,
        "potencial_renovable": 0.70,
        "tecnologia": 0.40,
        "capital_humano": 0.45,
        "tierra_arable": 0.50,
        "acceso_maritimo": 0.70,
        "pib_inicial": 30
    },
    "Laos": {
        "nombre": "Laos",
        "recursos_fosiles": 0.35,
        "potencial_renovable": 0.80,
        "tecnologia": 0.38,
        "capital_humano": 0.43,
        "tierra_arable": 0.45,
        "acceso_maritimo": 0.0,
        "pib_inicial": 19
    },
    "Nepal": {
        "nombre": "Nepal",
        "recursos_fosiles": 0.15,
        "potencial_renovable": 0.85,
        "tecnologia": 0.35,
        "capital_humano": 0.42,
        "tierra_arable": 0.35,
        "acceso_maritimo": 0.0,
        "pib_inicial": 40
    },
    "SriLanka": {
        "nombre": "Sri Lanka",
        "recursos_fosiles": 0.20,
        "potencial_renovable": 0.75,
        "tecnologia": 0.50,
        "capital_humano": 0.60,
        "tierra_arable": 0.45,
        "acceso_maritimo": 1.0,
        "pib_inicial": 75
    },
    "Afghanistan": {
        "nombre": "Afganistán",
        "recursos_fosiles": 0.50,
        "potencial_renovable": 0.70,
        "tecnologia": 0.25,
        "capital_humano": 0.30,
        "tierra_arable": 0.30,
        "acceso_maritimo": 0.0,
        "pib_inicial": 20
    },
    "Kazakhstan": {
        "nombre": "Kazajistán",
        "recursos_fosiles": 0.90,
        "potencial_renovable": 0.75,
        "tecnologia": 0.58,
        "capital_humano": 0.68,
        "tierra_arable": 0.45,
        "acceso_maritimo": 0.0,
        "pib_inicial": 225
    },
    "Uzbekistan": {
        "nombre": "Uzbekistán",
        "recursos_fosiles": 0.70,
        "potencial_renovable": 0.65,
        "tecnologia": 0.48,
        "capital_humano": 0.55,
        "tierra_arable": 0.40,
        "acceso_maritimo": 0.0,
        "pib_inicial": 90
    },
    "Mongolia": {
        "nombre": "Mongolia",
        "recursos_fosiles": 0.75,
        "potencial_renovable": 0.85,
        "tecnologia": 0.45,
        "capital_humano": 0.58,
        "tierra_arable": 0.15,
        "acceso_maritimo": 0.0,
        "pib_inicial": 15
    },
    # América adicional
    "Uruguay": {
        "nombre": "Uruguay",
        "recursos_fosiles": 0.20,
        "potencial_renovable": 0.90,
        "tecnologia": 0.65,
        "capital_humano": 0.75,
        "tierra_arable": 0.70,
        "acceso_maritimo": 0.85,
        "pib_inicial": 71
    },
    "Paraguay": {
        "nombre": "Paraguay",
        "recursos_fosiles": 0.15,
        "potencial_renovable": 0.88,
        "tecnologia": 0.48,
        "capital_humano": 0.55,
        "tierra_arable": 0.60,
        "acceso_maritimo": 0.0,
        "pib_inicial": 42
    },
    "Bolivia": {
        "nombre": "Bolivia",
        "recursos_fosiles": 0.60,
        "potencial_renovable": 0.80,
        "tecnologia": 0.45,
        "capital_humano": 0.52,
        "tierra_arable": 0.35,
        "acceso_maritimo": 0.0,
        "pib_inicial": 44
    },
    "CostaRica": {
        "nombre": "Costa Rica",
        "recursos_fosiles": 0.15,
        "potencial_renovable": 0.95,
        "tecnologia": 0.60,
        "capital_humano": 0.72,
        "tierra_arable": 0.40,
        "acceso_maritimo": 0.90,
        "pib_inicial": 68
    },
    "Panama": {
        "nombre": "Panamá",
        "recursos_fosiles": 0.20,
        "potencial_renovable": 0.75,
        "tecnologia": 0.58,
        "capital_humano": 0.65,
        "tierra_arable": 0.30,
        "acceso_maritimo": 1.0,
        "pib_inicial": 77
    },
    "Guatemala": {
        "nombre": "Guatemala",
        "recursos_fosiles": 0.35,
        "potencial_renovable": 0.75,
        "tecnologia": 0.45,
        "capital_humano": 0.48,
        "tierra_arable": 0.45,
        "acceso_maritimo": 0.75,
        "pib_inicial": 95
    },
    "DominicanRep": {
        "nombre": "República Dominicana",
        "recursos_fosiles": 0.25,
        "potencial_renovable": 0.70,
        "tecnologia": 0.52,
        "capital_humano": 0.58,
        "tierra_arable": 0.45,
        "acceso_maritimo": 0.95,
        "pib_inicial": 115
    },
    # África adicional
    "Tanzania": {
        "nombre": "Tanzania",
        "recursos_fosiles": 0.45,
        "potencial_renovable": 0.80,
        "tecnologia": 0.38,
        "capital_humano": 0.42,
        "tierra_arable": 0.55,
        "acceso_maritimo": 0.80,
        "pib_inicial": 79
    },
    "Uganda": {
        "nombre": "Uganda",
        "recursos_fosiles": 0.35,
        "potencial_renovable": 0.75,
        "tecnologia": 0.35,
        "capital_humano": 0.40,
        "tierra_arable": 0.55,
        "acceso_maritimo": 0.0,
        "pib_inicial": 49
    },
    "Cameroon": {
        "nombre": "Camerún",
        "recursos_fosiles": 0.55,
        "potencial_renovable": 0.75,
        "tecnologia": 0.38,
        "capital_humano": 0.43,
        "tierra_arable": 0.50,
        "acceso_maritimo": 0.75,
        "pib_inicial": 47
    },
    "IvoryCoast": {
        "nombre": "Costa de Marfil",
        "recursos_fosiles": 0.45,
        "potencial_renovable": 0.70,
        "tecnologia": 0.40,
        "capital_humano": 0.44,
        "tierra_arable": 0.55,
        "acceso_maritimo": 0.80,
        "pib_inicial": 79
    },
    "Senegal": {
        "nombre": "Senegal",
        "recursos_fosiles": 0.40,
        "potencial_renovable": 0.80,
        "tecnologia": 0.42,
        "capital_humano": 0.46,
        "tierra_arable": 0.45,
        "acceso_maritimo": 0.85,
        "pib_inicial": 31
    },
    "Angola": {
        "nombre": "Angola",
        "recursos_fosiles": 0.85,
        "potencial_renovable": 0.75,
        "tecnologia": 0.38,
        "capital_humano": 0.40,
        "tierra_arable": 0.40,
        "acceso_maritimo": 0.85,
        "pib_inicial": 67
    },
    "Tunisia": {
        "nombre": "Túnez",
        "recursos_fosiles": 0.45,
        "potencial_renovable": 0.80,
        "tecnologia": 0.55,
        "capital_humano": 0.62,
        "tierra_arable": 0.45,
        "acceso_maritimo": 0.90,
        "pib_inicial": 47
    },
    "Libya": {
        "nombre": "Libia",
        "recursos_fosiles": 0.92,
        "potencial_renovable": 0.88,
        "tecnologia": 0.45,
        "capital_humano": 0.50,
        "tierra_arable": 0.15,
        "acceso_maritimo": 0.90,
        "pib_inicial": 45
    },
    "Zimbabwe": {
        "nombre": "Zimbabue",
        "recursos_fosiles": 0.55,
        "potencial_renovable": 0.70,
        "tecnologia": 0.35,
        "capital_humano": 0.48,
        "tierra_arable": 0.50,
        "acceso_maritimo": 0.0,
        "pib_inicial": 31
    },
    # Oceanía
    "PapuaNewGuinea": {
        "nombre": "Papúa Nueva Guinea",
        "recursos_fosiles": 0.60,
        "potencial_renovable": 0.85,
        "tecnologia": 0.30,
        "capital_humano": 0.35,
        "tierra_arable": 0.30,
        "acceso_maritimo": 1.0,
        "pib_inicial": 30
    },
    # Medio Oriente adicional
    "Iraq": {
        "nombre": "Irak",
        "recursos_fosiles": 0.95,
        "potencial_renovable": 0.70,
        "tecnologia": 0.45,
        "capital_humano": 0.50,
        "tierra_arable": 0.30,
        "acceso_maritimo": 0.65,
        "pib_inicial": 207
    },
    "Syria": {
        "nombre": "Siria",
        "recursos_fosiles": 0.50,
        "potencial_renovable": 0.70,
        "tecnologia": 0.42,
        "capital_humano": 0.48,
        "tierra_arable": 0.40,
        "acceso_maritimo": 0.70,
        "pib_inicial": 40
    },
    "Jordan": {
        "nombre": "Jordania",
        "recursos_fosiles": 0.25,
        "potencial_renovable": 0.82,
        "tecnologia": 0.58,
        "capital_humano": 0.65,
        "tierra_arable": 0.20,
        "acceso_maritimo": 0.50,
        "pib_inicial": 50
    },
    "Lebanon": {
        "nombre": "Líbano",
        "recursos_fosiles": 0.15,
        "potencial_renovable": 0.65,
        "tecnologia": 0.60,
        "capital_humano": 0.68,
        "tierra_arable": 0.30,
        "acceso_maritimo": 0.85,
        "pib_inicial": 33
    },
    "Oman": {
        "nombre": "Omán",
        "recursos_fosiles": 0.85,
        "potencial_renovable": 0.80,
        "tecnologia": 0.68,
        "capital_humano": 0.70,
        "tierra_arable": 0.10,
        "acceso_maritimo": 0.95,
        "pib_inicial": 108
    },
    "Yemen": {
        "nombre": "Yemen",
        "recursos_fosiles": 0.60,
        "potencial_renovable": 0.75,
        "tecnologia": 0.30,
        "capital_humano": 0.35,
        "tierra_arable": 0.25,
        "acceso_maritimo": 0.90,
        "pib_inicial": 21
    },
    # Países pequeños pero importantes
    "Bahrain": {
        "nombre": "Baréin",
        "recursos_fosiles": 0.75,
        "potencial_renovable": 0.70,
        "tecnologia": 0.75,
        "capital_humano": 0.78,
        "tierra_arable": 0.05,
        "acceso_maritimo": 1.0,
        "pib_inicial": 44
    },
    "Cyprus": {
        "nombre": "Chipre",
        "recursos_fosiles": 0.20,
        "potencial_renovable": 0.75,
        "tecnologia": 0.72,
        "capital_humano": 0.78,
        "tierra_arable": 0.30,
        "acceso_maritimo": 1.0,
        "pib_inicial": 28
    },
    "Malta": {
        "nombre": "Malta",
        "recursos_fosiles": 0.05,
        "potencial_renovable": 0.70,
        "tecnologia": 0.78,
        "capital_humano": 0.82,
        "tierra_arable": 0.20,
        "acceso_maritimo": 1.0,
        "pib_inicial": 18
    },
    # Países genéricos para resto del mundo
    "Greenland": {
        "nombre": "Groenlandia",
        "recursos_fosiles": 0.60,
        "potencial_renovable": 0.90,
        "tecnologia": 0.75,
        "capital_humano": 0.80,
        "tierra_arable": 0.01,
        "acceso_maritimo": 1.0,
        "pib_inicial": 3
    },
    "Madagascar": {
        "nombre": "Madagascar",
        "recursos_fosiles": 0.40,
        "potencial_renovable": 0.80,
        "tecnologia": 0.32,
        "capital_humano": 0.38,
        "tierra_arable": 0.45,
        "acceso_maritimo": 1.0,
        "pib_inicial": 15
    },
    "Mozambique": {
        "nombre": "Mozambique",
        "recursos_fosiles": 0.70,
        "potencial_renovable": 0.80,
        "tecnologia": 0.30,
        "capital_humano": 0.35,
        "tierra_arable": 0.50,
        "acceso_maritimo": 0.90,
        "pib_inicial": 19
    },
    "Zambia": {
        "nombre": "Zambia",
        "recursos_fosiles": 0.50,
        "potencial_renovable": 0.75,
        "tecnologia": 0.35,
        "capital_humano": 0.42,
        "tierra_arable": 0.45,
        "acceso_maritimo": 0.0,
        "pib_inicial": 29
    },
    "Namibia": {
        "nombre": "Namibia",
        "recursos_fosiles": 0.65,
        "potencial_renovable": 0.88,
        "tecnologia": 0.42,
        "capital_humano": 0.50,
        "tierra_arable": 0.20,
        "acceso_maritimo": 0.85,
        "pib_inicial": 12
    },
    "Botswana": {
        "nombre": "Botsuana",
        "recursos_fosiles": 0.55,
        "potencial_renovable": 0.85,
        "tecnologia": 0.48,
        "capital_humano": 0.55,
        "tierra_arable": 0.15,
        "acceso_maritimo": 0.0,
        "pib_inicial": 18
    },
    "Sudan": {
        "nombre": "Sudán",
        "recursos_fosiles": 0.65,
        "potencial_renovable": 0.78,
        "tecnologia": 0.32,
        "capital_humano": 0.38,
        "tierra_arable": 0.40,
        "acceso_maritimo": 0.75,
        "pib_inicial": 34
    },
    "SouthSudan": {
        "nombre": "Sudán del Sur",
        "recursos_fosiles": 0.75,
        "potencial_renovable": 0.70,
        "tecnologia": 0.20,
        "capital_humano": 0.25,
        "tierra_arable": 0.35,
        "acceso_maritimo": 0.0,
        "pib_inicial": 3
    },
    "Somalia": {
        "nombre": "Somalia",
        "recursos_fosiles": 0.55,
        "potencial_renovable": 0.75,
        "tecnologia": 0.18,
        "capital_humano": 0.22,
        "tierra_arable": 0.30,
        "acceso_maritimo": 0.95,
        "pib_inicial": 8
    },
    "Congo": {
        "nombre": "República del Congo",
        "recursos_fosiles": 0.80,
        "potencial_renovable": 0.85,
        "tecnologia": 0.28,
        "capital_humano": 0.32,
        "tierra_arable": 0.40,
        "acceso_maritimo": 0.70,
        "pib_inicial": 13
    },
    "DRC": {
        "nombre": "Rep. Dem. del Congo",
        "recursos_fosiles": 0.85,
        "potencial_renovable": 0.90,
        "tecnologia": 0.25,
        "capital_humano": 0.28,
        "tierra_arable": 0.45,
        "acceso_maritimo": 0.60,
        "pib_inicial": 61
    },
    # Europa adicional
    "Albania": {
        "nombre": "Albania",
        "recursos_fosiles": 0.30,
        "potencial_renovable": 0.70,
        "tecnologia": 0.48,
        "capital_humano": 0.55,
        "tierra_arable": 0.42,
        "acceso_maritimo": 0.75,
        "pib_inicial": 18
    },
    "NorthMacedonia": {
        "nombre": "Macedonia del Norte",
        "recursos_fosiles": 0.28,
        "potencial_renovable": 0.55,
        "tecnologia": 0.50,
        "capital_humano": 0.58,
        "tierra_arable": 0.48,
        "acceso_maritimo": 0.0,
        "pib_inicial": 14
    },
    "Bosnia": {
        "nombre": "Bosnia-Herzegovina",
        "recursos_fosiles": 0.35,
        "potencial_renovable": 0.65,
        "tecnologia": 0.48,
        "capital_humano": 0.55,
        "tierra_arable": 0.40,
        "acceso_maritimo": 0.20,
        "pib_inicial": 23
    },
    "Montenegro": {
        "nombre": "Montenegro",
        "recursos_fosiles": 0.25,
        "potencial_renovable": 0.68,
        "tecnologia": 0.52,
        "capital_humano": 0.60,
        "tierra_arable": 0.35,
        "acceso_maritimo": 0.70,
        "pib_inicial": 6
    },
    "Moldova": {
        "nombre": "Moldavia",
        "recursos_fosiles": 0.20,
        "potencial_renovable": 0.45,
        "tecnologia": 0.45,
        "capital_humano": 0.58,
        "tierra_arable": 0.68,
        "acceso_maritimo": 0.0,
        "pib_inicial": 14
    },
    "Armenia": {
        "nombre": "Armenia",
        "recursos_fosiles": 0.25,
        "potencial_renovable": 0.58,
        "tecnologia": 0.55,
        "capital_humano": 0.68,
        "tierra_arable": 0.32,
        "acceso_maritimo": 0.0,
        "pib_inicial": 19
    },
    "Georgia": {
        "nombre": "Georgia",
        "recursos_fosiles": 0.30,
        "potencial_renovable": 0.75,
        "tecnologia": 0.52,
        "capital_humano": 0.65,
        "tierra_arable": 0.42,
        "acceso_maritimo": 0.60,
        "pib_inicial": 24
    },
    "Azerbaijan": {
        "nombre": "Azerbaiyán",
        "recursos_fosiles": 0.82,
        "potencial_renovable": 0.55,
        "tecnologia": 0.50,
        "capital_humano": 0.62,
        "tierra_arable": 0.48,
        "acceso_maritimo": 0.0,
        "pib_inicial": 78
    },
    # Asia adicional
    "Turkmenistan": {
        "nombre": "Turkmenistán",
        "recursos_fosiles": 0.90,
        "potencial_renovable": 0.48,
        "tecnologia": 0.42,
        "capital_humano": 0.55,
        "tierra_arable": 0.35,
        "acceso_maritimo": 0.0,
        "pib_inicial": 57
    },
    "Kyrgyzstan": {
        "nombre": "Kirguistán",
        "recursos_fosiles": 0.35,
        "potencial_renovable": 0.70,
        "tecnologia": 0.40,
        "capital_humano": 0.58,
        "tierra_arable": 0.32,
        "acceso_maritimo": 0.0,
        "pib_inicial": 11
    },
    "Tajikistan": {
        "nombre": "Tayikistán",
        "recursos_fosiles": 0.32,
        "potencial_renovable": 0.72,
        "tecnologia": 0.38,
        "capital_humano": 0.52,
        "tierra_arable": 0.28,
        "acceso_maritimo": 0.0,
        "pib_inicial": 11
    },
    "TimorLeste": {
        "nombre": "Timor Oriental",
        "recursos_fosiles": 0.65,
        "potencial_renovable": 0.55,
        "tecnologia": 0.25,
        "capital_humano": 0.35,
        "tierra_arable": 0.30,
        "acceso_maritimo": 0.80,
        "pib_inicial": 3
    },
    "Brunei": {
        "nombre": "Brunéi",
        "recursos_fosiles": 0.88,
        "potencial_renovable": 0.45,
        "tecnologia": 0.68,
        "capital_humano": 0.75,
        "tierra_arable": 0.15,
        "acceso_maritimo": 0.85,
        "pib_inicial": 15
    },
    "Maldives": {
        "nombre": "Maldivas",
        "recursos_fosiles": 0.05,
        "potencial_renovable": 0.80,
        "tecnologia": 0.48,
        "capital_humano": 0.62,
        "tierra_arable": 0.05,
        "acceso_maritimo": 1.0,
        "pib_inicial": 6
    },
    "Bhutan": {
        "nombre": "Bután",
        "recursos_fosiles": 0.15,
        "potencial_renovable": 0.85,
        "tecnologia": 0.42,
        "capital_humano": 0.58,
        "tierra_arable": 0.20,
        "acceso_maritimo": 0.0,
        "pib_inicial": 3
    },
    # América adicional
    "Belize": {
        "nombre": "Belice",
        "recursos_fosiles": 0.25,
        "potencial_renovable": 0.70,
        "tecnologia": 0.40,
        "capital_humano": 0.55,
        "tierra_arable": 0.42,
        "acceso_maritimo": 0.90,
        "pib_inicial": 3
    },
    "ElSalvador": {
        "nombre": "El Salvador",
        "recursos_fosiles": 0.20,
        "potencial_renovable": 0.65,
        "tecnologia": 0.45,
        "capital_humano": 0.58,
        "tierra_arable": 0.55,
        "acceso_maritimo": 0.70,
        "pib_inicial": 32
    },
    "Honduras": {
        "nombre": "Honduras",
        "recursos_fosiles": 0.22,
        "potencial_renovable": 0.68,
        "tecnologia": 0.40,
        "capital_humano": 0.50,
        "tierra_arable": 0.48,
        "acceso_maritimo": 0.75,
        "pib_inicial": 32
    },
    "Nicaragua": {
        "nombre": "Nicaragua",
        "recursos_fosiles": 0.25,
        "potencial_renovable": 0.72,
        "tecnologia": 0.38,
        "capital_humano": 0.52,
        "tierra_arable": 0.52,
        "acceso_maritimo": 0.80,
        "pib_inicial": 15
    },
    "Jamaica": {
        "nombre": "Jamaica",
        "recursos_fosiles": 0.20,
        "potencial_renovable": 0.68,
        "tecnologia": 0.48,
        "capital_humano": 0.62,
        "tierra_arable": 0.35,
        "acceso_maritimo": 1.0,
        "pib_inicial": 17
    },
    "Haiti": {
        "nombre": "Haití",
        "recursos_fosiles": 0.10,
        "potencial_renovable": 0.50,
        "tecnologia": 0.25,
        "capital_humano": 0.35,
        "tierra_arable": 0.45,
        "acceso_maritimo": 0.85,
        "pib_inicial": 20
    },
    "TrinidadTobago": {
        "nombre": "Trinidad y Tobago",
        "recursos_fosiles": 0.75,
        "potencial_renovable": 0.52,
        "tecnologia": 0.55,
        "capital_humano": 0.68,
        "tierra_arable": 0.30,
        "acceso_maritimo": 1.0,
        "pib_inicial": 24
    },
    "Bahamas": {
        "nombre": "Bahamas",
        "recursos_fosiles": 0.15,
        "potencial_renovable": 0.75,
        "tecnologia": 0.58,
        "capital_humano": 0.72,
        "tierra_arable": 0.15,
        "acceso_maritimo": 1.0,
        "pib_inicial": 14
    },
    "Barbados": {
        "nombre": "Barbados",
        "recursos_fosiles": 0.12,
        "potencial_renovable": 0.70,
        "tecnologia": 0.60,
        "capital_humano": 0.75,
        "tierra_arable": 0.25,
        "acceso_maritimo": 1.0,
        "pib_inicial": 6
    },
    "Guyana": {
        "nombre": "Guyana",
        "recursos_fosiles": 0.80,
        "potencial_renovable": 0.75,
        "tecnologia": 0.38,
        "capital_humano": 0.52,
        "tierra_arable": 0.48,
        "acceso_maritimo": 0.85,
        "pib_inicial": 15
    },
    "Suriname": {
        "nombre": "Surinam",
        "recursos_fosiles": 0.68,
        "potencial_renovable": 0.70,
        "tecnologia": 0.42,
        "capital_humano": 0.58,
        "tierra_arable": 0.38,
        "acceso_maritimo": 0.80,
        "pib_inicial": 4
    },
    # África adicional
    "Chad": {
        "nombre": "Chad",
        "recursos_fosiles": 0.65,
        "potencial_renovable": 0.70,
        "tecnologia": 0.22,
        "capital_humano": 0.28,
        "tierra_arable": 0.35,
        "acceso_maritimo": 0.0,
        "pib_inicial": 12
    },
    "Mali": {
        "nombre": "Mali",
        "recursos_fosiles": 0.45,
        "potencial_renovable": 0.75,
        "tecnologia": 0.25,
        "capital_humano": 0.32,
        "tierra_arable": 0.42,
        "acceso_maritimo": 0.0,
        "pib_inicial": 19
    },
    "Niger": {
        "nombre": "Níger",
        "recursos_fosiles": 0.68,
        "potencial_renovable": 0.78,
        "tecnologia": 0.20,
        "capital_humano": 0.28,
        "tierra_arable": 0.35,
        "acceso_maritimo": 0.0,
        "pib_inicial": 16
    },
    "BurkinaFaso": {
        "nombre": "Burkina Faso",
        "recursos_fosiles": 0.42,
        "potencial_renovable": 0.72,
        "tecnologia": 0.25,
        "capital_humano": 0.32,
        "tierra_arable": 0.48,
        "acceso_maritimo": 0.0,
        "pib_inicial": 19
    },
    "Rwanda": {
        "nombre": "Ruanda",
        "recursos_fosiles": 0.25,
        "potencial_renovable": 0.65,
        "tecnologia": 0.42,
        "capital_humano": 0.52,
        "tierra_arable": 0.58,
        "acceso_maritimo": 0.0,
        "pib_inicial": 13
    },
    "Burundi": {
        "nombre": "Burundi",
        "recursos_fosiles": 0.22,
        "potencial_renovable": 0.60,
        "tecnologia": 0.20,
        "capital_humano": 0.35,
        "tierra_arable": 0.52,
        "acceso_maritimo": 0.0,
        "pib_inicial": 3
    },
    "Eritrea": {
        "nombre": "Eritrea",
        "recursos_fosiles": 0.35,
        "potencial_renovable": 0.68,
        "tecnologia": 0.25,
        "capital_humano": 0.38,
        "tierra_arable": 0.28,
        "acceso_maritimo": 0.90,
        "pib_inicial": 2
    },
    "Liberia": {
        "nombre": "Liberia",
        "recursos_fosiles": 0.45,
        "potencial_renovable": 0.75,
        "tecnologia": 0.25,
        "capital_humano": 0.38,
        "tierra_arable": 0.45,
        "acceso_maritimo": 0.85,
        "pib_inicial": 4
    },
    "SierraLeone": {
        "nombre": "Sierra Leona",
        "recursos_fosiles": 0.52,
        "potencial_renovable": 0.72,
        "tecnologia": 0.25,
        "capital_humano": 0.35,
        "tierra_arable": 0.48,
        "acceso_maritimo": 0.90,
        "pib_inicial": 4
    },
    "Guinea": {
        "nombre": "Guinea",
        "recursos_fosiles": 0.58,
        "potencial_renovable": 0.78,
        "tecnologia": 0.28,
        "capital_humano": 0.38,
        "tierra_arable": 0.52,
        "acceso_maritimo": 0.80,
        "pib_inicial": 19
    },
    "Togo": {
        "nombre": "Togo",
        "recursos_fosiles": 0.35,
        "potencial_renovable": 0.68,
        "tecnologia": 0.32,
        "capital_humano": 0.42,
        "tierra_arable": 0.55,
        "acceso_maritimo": 0.75,
        "pib_inicial": 8
    },
    "Benin": {
        "nombre": "Benín",
        "recursos_fosiles": 0.30,
        "potencial_renovable": 0.70,
        "tecnologia": 0.32,
        "capital_humano": 0.42,
        "tierra_arable": 0.58,
        "acceso_maritimo": 0.70,
        "pib_inicial": 18
    },
    "Mauritania": {
        "nombre": "Mauritania",
        "recursos_fosiles": 0.62,
        "potencial_renovable": 0.80,
        "tecnologia": 0.28,
        "capital_humano": 0.38,
        "tierra_arable": 0.22,
        "acceso_maritimo": 0.90,
        "pib_inicial": 10
    },
    "Gambia": {
        "nombre": "Gambia",
        "recursos_fosiles": 0.20,
        "potencial_renovable": 0.65,
        "tecnologia": 0.28,
        "capital_humano": 0.38,
        "tierra_arable": 0.52,
        "acceso_maritimo": 0.75,
        "pib_inicial": 2
    },
    "Gabon": {
        "nombre": "Gabón",
        "recursos_fosiles": 0.82,
        "potencial_renovable": 0.85,
        "tecnologia": 0.38,
        "capital_humano": 0.52,
        "tierra_arable": 0.35,
        "acceso_maritimo": 0.90,
        "pib_inicial": 20
    },
    "CAR": {
        "nombre": "Rep. Centroafricana",
        "recursos_fosiles": 0.55,
        "potencial_renovable": 0.78,
        "tecnologia": 0.18,
        "capital_humano": 0.25,
        "tierra_arable": 0.42,
        "acceso_maritimo": 0.0,
        "pib_inicial": 3
    },
    "Malawi": {
        "nombre": "Malaui",
        "recursos_fosiles": 0.28,
        "potencial_renovable": 0.72,
        "tecnologia": 0.25,
        "capital_humano": 0.38,
        "tierra_arable": 0.58,
        "acceso_maritimo": 0.0,
        "pib_inicial": 13
    },
    "Lesotho": {
        "nombre": "Lesoto",
        "recursos_fosiles": 0.15,
        "potencial_renovable": 0.68,
        "tecnologia": 0.32,
        "capital_humano": 0.48,
        "tierra_arable": 0.30,
        "acceso_maritimo": 0.0,
        "pib_inicial": 3
    },
    "Eswatini": {
        "nombre": "Esuatini",
        "recursos_fosiles": 0.22,
        "potencial_renovable": 0.58,
        "tecnologia": 0.38,
        "capital_humano": 0.48,
        "tierra_arable": 0.45,
        "acceso_maritimo": 0.0,
        "pib_inicial": 5
    },
    "Djibouti": {
        "nombre": "Yibuti",
        "recursos_fosiles": 0.15,
        "potencial_renovable": 0.75,
        "tecnologia": 0.35,
        "capital_humano": 0.42,
        "tierra_arable": 0.10,
        "acceso_maritimo": 1.0,
        "pib_inicial": 4
    },
    "Mauritius": {
        "nombre": "Mauricio",
        "recursos_fosiles": 0.10,
        "potencial_renovable": 0.70,
        "tecnologia": 0.58,
        "capital_humano": 0.72,
        "tierra_arable": 0.42,
        "acceso_maritimo": 1.0,
        "pib_inicial": 15
    },
    # Oceanía adicional
    "Fiji": {
        "nombre": "Fiyi",
        "recursos_fosiles": 0.15,
        "potencial_renovable": 0.78,
        "tecnologia": 0.45,
        "capital_humano": 0.62,
        "tierra_arable": 0.35,
        "acceso_maritimo": 1.0,
        "pib_inicial": 5
    },
    "SolomonIslands": {
        "nombre": "Islas Salomón",
        "recursos_fosiles": 0.20,
        "potencial_renovable": 0.75,
        "tecnologia": 0.32,
        "capital_humano": 0.45,
        "tierra_arable": 0.30,
        "acceso_maritimo": 1.0,
        "pib_inicial": 2
    },
    "Vanuatu": {
        "nombre": "Vanuatu",
        "recursos_fosiles": 0.12,
        "potencial_renovable": 0.72,
        "tecnologia": 0.35,
        "capital_humano": 0.48,
        "tierra_arable": 0.28,
        "acceso_maritimo": 1.0,
        "pib_inicial": 1
    },
    "Samoa": {
        "nombre": "Samoa",
        "recursos_fosiles": 0.10,
        "potencial_renovable": 0.70,
        "tecnologia": 0.38,
        "capital_humano": 0.58,
        "tierra_arable": 0.32,
        "acceso_maritimo": 1.0,
        "pib_inicial": 1
    },
    "Tonga": {
        "nombre": "Tonga",
        "recursos_fosiles": 0.08,
        "potencial_renovable": 0.68,
        "tecnologia": 0.35,
        "capital_humano": 0.55,
        "tierra_arable": 0.28,
        "acceso_maritimo": 1.0,
        "pib_inicial": 0.5
    }
}


def obtener_pais(codigo_pais: str) -> dict:
    """
    Obtiene la información de un país por su código
    
    Args:
        codigo_pais: Código del país (ej: "USA", "Spain")
    
    Returns:
        Diccionario con los datos del país o None si no existe
    """
    return ATLAS_MUNDIAL.get(codigo_pais)


def listar_paises() -> list:
    """
    Devuelve lista de todos los códigos de países disponibles
    """
    return list(ATLAS_MUNDIAL.keys())


def obtener_datos_completos() -> dict:
    """
    Devuelve el atlas completo
    """
    return ATLAS_MUNDIAL
