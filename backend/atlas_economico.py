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
