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
