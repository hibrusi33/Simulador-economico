# motor_economico.py
"""
Motor económico que utiliza Google Gemini para generar proyecciones realistas
"""

import os
import json
import math
import hashlib
import random
import google.generativeai as genai
from typing import Dict, List, Tuple


class MotorEconomico:
    """
    Clase que conecta con Google Gemini para generar simulaciones económicas
    """
    
    def __init__(self, api_key: str = None):
        """
        Inicializa la conexión con Gemini
        
        Args:
            api_key: API key de Google Gemini (si no se proporciona, busca en variable de entorno)
        """
        self.api_key = api_key or os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("API key de Gemini no proporcionada. Define GEMINI_API_KEY en el entorno.")
        
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel('gemini-1.5-flash')
    
    def proyectar_economia(self, pais_datos: Dict, ideologia: str, codigo_pais: str) -> List[Dict]:
        """
        Genera una proyección económica de 50 meses para un país
        
        Args:
            pais_datos: Diccionario con los recursos del país
            ideologia: Sistema político/económico (ej: "Capitalismo", "Comunismo", "Teocracia")
            codigo_pais: Código del país para referencia
        
        Returns:
            Lista de 50 diccionarios con PIB, Bienestar y Libertad por mes
        """
        
        pesos, indicadores = self._calcular_pesos_e_indicadores(pais_datos, ideologia, codigo_pais)

        # Construir el prompt para Gemini
        prompt = f"""Actúa como un motor económico avanzado y geopolítico.

PAÍS: {pais_datos.get('nombre', codigo_pais)}
IDEOLOGÍA APLICADA: {ideologia}

RECURSOS Y CARACTERÍSTICAS (escala 0.0-1.0):
{json.dumps(pais_datos, indent=2)}

PESOS DE MODELADO (para PIB/Bienestar/Libertad):
{json.dumps(pesos, indent=2)}

INDICADORES BASE CALCULADOS:
{json.dumps(indicadores, indent=2)}

TAREA:
Genera una proyección económica REALISTA de 50 meses para este país bajo la ideología "{ideologia}".

CONSIDERACIONES IMPORTANTES:
1. La ideología afecta dramáticamente el crecimiento económico, la distribución de riqueza y las libertades
2. Los recursos naturales y el capital humano son fundamentales
3. Introduce VOLATILIDAD realista (crisis económicas, tensiones geopolíticas, reformas)
4. El Capitalismo tiende a maximizar PIB pero puede generar desigualdad
5. El Comunismo redistribuye pero puede limitar innovación y libertades económicas
6. Las Teocracias priorizan valores religiosos sobre eficiencia económica
7. Eventos aleatorios: recesiones, booms tecnológicos, conflictos comerciales
8. Los meses 1-10 muestran ajuste al nuevo sistema
9. Los meses 11-30 muestran consolidación
10. Los meses 31-50 muestran efectos a largo plazo

FORMATO DE SALIDA (ESTRICTAMENTE JSON):
Devuelve un array JSON de exactamente 50 objetos, cada uno con:
{{
  "mes": [número del 1 al 50],
  "PIB": [valor numérico, puede crecer o decrecer, rango sugerido 0.5x a 3.0x del PIB inicial],
  "Bienestar": [0-100, calidad de vida, salud, educación],
  "Libertad": [0-100, libertades civiles y económicas]
}}

PIB inicial del país: {pais_datos.get('pib_inicial', 1000)} miles de millones USD

RESPONDE ÚNICAMENTE CON EL JSON, SIN TEXTO ADICIONAL."""

        try:
            # Llamar a Gemini
            response = self.model.generate_content(prompt)
            
            # Extraer el texto de la respuesta
            response_text = response.text.strip()
            
            # Limpiar markdown si existe
            if response_text.startswith("```json"):
                response_text = response_text[7:]
            if response_text.startswith("```"):
                response_text = response_text[3:]
            if response_text.endswith("```"):
                response_text = response_text[:-3]
            
            response_text = response_text.strip()
            
            # Parsear JSON
            proyeccion = json.loads(response_text)
            
            # Validar que sea una lista de 50 elementos
            if not isinstance(proyeccion, list):
                raise ValueError("La respuesta no es una lista")
            
            # Si hay menos de 50, rellenar con valores estables
            if len(proyeccion) < 50:
                ultimo_valor = proyeccion[-1] if proyeccion else {
                    "mes": 1,
                    "PIB": pais_datos.get('pib_inicial', 1000),
                    "Bienestar": 50,
                    "Libertad": 50
                }
                for i in range(len(proyeccion), 50):
                    proyeccion.append({
                        "mes": i + 1,
                        "PIB": ultimo_valor["PIB"] * (1 + (hash(codigo_pais + str(i)) % 10 - 5) / 100),
                        "Bienestar": ultimo_valor["Bienestar"],
                        "Libertad": ultimo_valor["Libertad"]
                    })
            
            # Tomar solo los primeros 50
            proyeccion = proyeccion[:50]
            
            # Asegurar que todos tengan el campo "mes"
            for idx, mes_data in enumerate(proyeccion):
                if "mes" not in mes_data:
                    mes_data["mes"] = idx + 1
            
            return proyeccion
            
        except json.JSONDecodeError as e:
            print(f"Error al parsear JSON de Gemini para {codigo_pais}: {e}")
            print(f"Respuesta recibida: {response_text[:500]}")
            # Fallback: generar proyección sintética
            return self._generar_proyeccion_fallback(pais_datos, ideologia, codigo_pais)
        
        except Exception as e:
            print(f"Error en proyección para {codigo_pais}: {e}")
            return self._generar_proyeccion_fallback(pais_datos, ideologia, codigo_pais)

    def _normalizar_recursos(self, pais_datos: Dict) -> Dict[str, float]:
        return {
            "recursos_fosiles": float(pais_datos.get("recursos_fosiles", 0.5)),
            "potencial_renovable": float(pais_datos.get("potencial_renovable", 0.5)),
            "tecnologia": float(pais_datos.get("tecnologia", 0.5)),
            "capital_humano": float(pais_datos.get("capital_humano", 0.5)),
            "tierra_arable": float(pais_datos.get("tierra_arable", 0.5)),
            "acceso_maritimo": float(pais_datos.get("acceso_maritimo", 0.5))
        }

    def _identificar_ideologia(self, ideologia: str) -> str:
        ideologia_norm = ideologia.lower()
        if "comun" in ideologia_norm:
            return "comunismo"
        if "teocra" in ideologia_norm:
            return "teocracia"
        if "autor" in ideologia_norm:
            return "autoritarismo"
        if "tecnocra" in ideologia_norm:
            return "tecnocracia"
        if "social" in ideologia_norm and "democr" in ideologia_norm:
            return "socialdemocracia"
        if "social" in ideologia_norm:
            return "socialismo"
        if "anarcocapital" in ideologia_norm:
            return "anarcocapitalismo"
        if "neoliberal" in ideologia_norm:
            return "neoliberalismo"
        return "capitalismo"

    def _calcular_pesos_e_indicadores(
        self,
        pais_datos: Dict,
        ideologia: str,
        codigo_pais: str
    ) -> Tuple[Dict, Dict]:
        recursos = self._normalizar_recursos(pais_datos)
        ideologia_base = self._identificar_ideologia(ideologia)

        pesos_ideologia = {
            "capitalismo": {
                "PIB": {"tecnologia": 0.30, "capital_humano": 0.25, "recursos_fosiles": 0.15, "potencial_renovable": 0.10, "acceso_maritimo": 0.10, "tierra_arable": 0.10},
                "Bienestar": {"capital_humano": 0.35, "tecnologia": 0.25, "potencial_renovable": 0.15, "tierra_arable": 0.15, "recursos_fosiles": 0.10},
                "Libertad": {"tecnologia": 0.25, "capital_humano": 0.25, "acceso_maritimo": 0.20, "potencial_renovable": 0.15, "tierra_arable": 0.15},
                "modificador_crecimiento": 0.012,
                "bono_bienestar": 2,
                "bono_libertad": 10,
                "volatilidad": 0.015
            },
            "neoliberalismo": {
                "PIB": {"tecnologia": 0.35, "capital_humano": 0.25, "recursos_fosiles": 0.15, "potencial_renovable": 0.05, "acceso_maritimo": 0.10, "tierra_arable": 0.10},
                "Bienestar": {"capital_humano": 0.30, "tecnologia": 0.20, "potencial_renovable": 0.15, "tierra_arable": 0.20, "recursos_fosiles": 0.15},
                "Libertad": {"tecnologia": 0.30, "capital_humano": 0.25, "acceso_maritimo": 0.20, "potencial_renovable": 0.10, "tierra_arable": 0.15},
                "modificador_crecimiento": 0.016,
                "bono_bienestar": 0,
                "bono_libertad": 12,
                "volatilidad": 0.02
            },
            "socialismo": {
                "PIB": {"capital_humano": 0.30, "tecnologia": 0.20, "tierra_arable": 0.20, "recursos_fosiles": 0.15, "potencial_renovable": 0.10, "acceso_maritimo": 0.05},
                "Bienestar": {"capital_humano": 0.40, "tierra_arable": 0.20, "potencial_renovable": 0.20, "tecnologia": 0.20},
                "Libertad": {"capital_humano": 0.30, "tecnologia": 0.20, "acceso_maritimo": 0.20, "potencial_renovable": 0.15, "tierra_arable": 0.15},
                "modificador_crecimiento": 0.006,
                "bono_bienestar": 6,
                "bono_libertad": 2,
                "volatilidad": 0.012
            },
            "socialdemocracia": {
                "PIB": {"capital_humano": 0.30, "tecnologia": 0.25, "potencial_renovable": 0.15, "tierra_arable": 0.15, "recursos_fosiles": 0.10, "acceso_maritimo": 0.05},
                "Bienestar": {"capital_humano": 0.45, "potencial_renovable": 0.20, "tecnologia": 0.20, "tierra_arable": 0.15},
                "Libertad": {"capital_humano": 0.30, "tecnologia": 0.25, "acceso_maritimo": 0.20, "potencial_renovable": 0.15, "tierra_arable": 0.10},
                "modificador_crecimiento": 0.009,
                "bono_bienestar": 8,
                "bono_libertad": 6,
                "volatilidad": 0.011
            },
            "comunismo": {
                "PIB": {"capital_humano": 0.30, "tierra_arable": 0.25, "recursos_fosiles": 0.20, "tecnologia": 0.15, "potencial_renovable": 0.05, "acceso_maritimo": 0.05},
                "Bienestar": {"capital_humano": 0.45, "tierra_arable": 0.25, "potencial_renovable": 0.15, "tecnologia": 0.15},
                "Libertad": {"capital_humano": 0.30, "tecnologia": 0.20, "acceso_maritimo": 0.15, "potencial_renovable": 0.15, "tierra_arable": 0.20},
                "modificador_crecimiento": 0.001,
                "bono_bienestar": 10,
                "bono_libertad": -15,
                "volatilidad": 0.01
            },
            "teocracia": {
                "PIB": {"recursos_fosiles": 0.25, "tierra_arable": 0.20, "potencial_renovable": 0.15, "capital_humano": 0.15, "tecnologia": 0.15, "acceso_maritimo": 0.10},
                "Bienestar": {"capital_humano": 0.35, "tierra_arable": 0.25, "potencial_renovable": 0.20, "recursos_fosiles": 0.20},
                "Libertad": {"capital_humano": 0.25, "tecnologia": 0.20, "acceso_maritimo": 0.15, "potencial_renovable": 0.20, "tierra_arable": 0.20},
                "modificador_crecimiento": -0.002,
                "bono_bienestar": 4,
                "bono_libertad": -20,
                "volatilidad": 0.014
            },
            "autoritarismo": {
                "PIB": {"recursos_fosiles": 0.22, "tecnologia": 0.22, "capital_humano": 0.18, "tierra_arable": 0.18, "potencial_renovable": 0.10, "acceso_maritimo": 0.10},
                "Bienestar": {"capital_humano": 0.35, "tierra_arable": 0.25, "potencial_renovable": 0.15, "tecnologia": 0.15, "recursos_fosiles": 0.10},
                "Libertad": {"capital_humano": 0.20, "tecnologia": 0.20, "acceso_maritimo": 0.20, "potencial_renovable": 0.20, "tierra_arable": 0.20},
                "modificador_crecimiento": 0.004,
                "bono_bienestar": 1,
                "bono_libertad": -25,
                "volatilidad": 0.018
            },
            "tecnocracia": {
                "PIB": {"tecnologia": 0.40, "capital_humano": 0.25, "potencial_renovable": 0.15, "recursos_fosiles": 0.10, "acceso_maritimo": 0.05, "tierra_arable": 0.05},
                "Bienestar": {"tecnologia": 0.30, "capital_humano": 0.35, "potencial_renovable": 0.20, "tierra_arable": 0.15},
                "Libertad": {"tecnologia": 0.30, "capital_humano": 0.25, "acceso_maritimo": 0.15, "potencial_renovable": 0.15, "tierra_arable": 0.15},
                "modificador_crecimiento": 0.014,
                "bono_bienestar": 4,
                "bono_libertad": 4,
                "volatilidad": 0.013
            },
            "anarcocapitalismo": {
                "PIB": {"tecnologia": 0.30, "capital_humano": 0.25, "recursos_fosiles": 0.20, "potencial_renovable": 0.10, "tierra_arable": 0.10, "acceso_maritimo": 0.05},
                "Bienestar": {"capital_humano": 0.30, "tecnologia": 0.20, "potencial_renovable": 0.15, "tierra_arable": 0.20, "recursos_fosiles": 0.15},
                "Libertad": {"tecnologia": 0.35, "capital_humano": 0.25, "acceso_maritimo": 0.15, "potencial_renovable": 0.15, "tierra_arable": 0.10},
                "modificador_crecimiento": 0.018,
                "bono_bienestar": -2,
                "bono_libertad": 15,
                "volatilidad": 0.025
            }
        }

        pesos = pesos_ideologia.get(ideologia_base, pesos_ideologia["capitalismo"])

        def calcular_score(pesos_recurso: Dict[str, float]) -> float:
            return sum(recursos[clave] * peso for clave, peso in pesos_recurso.items())

        score_pib = calcular_score(pesos["PIB"])
        score_bienestar = calcular_score(pesos["Bienestar"])
        score_libertad = calcular_score(pesos["Libertad"])

        seed = int(hashlib.sha256(codigo_pais.encode("utf-8")).hexdigest()[:8], 16)
        generador = random.Random(seed)
        factor_estructural = generador.uniform(-0.005, 0.007)

        resiliencia = (recursos["capital_humano"] * 0.45 +
                       recursos["tecnologia"] * 0.35 +
                       recursos["potencial_renovable"] * 0.20)

        estabilidad = (recursos["capital_humano"] * 0.40 +
                       recursos["tierra_arable"] * 0.25 +
                       recursos["acceso_maritimo"] * 0.15 +
                       recursos["potencial_renovable"] * 0.20)

        indicadores = {
            "score_pib": round(score_pib, 4),
            "score_bienestar": round(score_bienestar, 4),
            "score_libertad": round(score_libertad, 4),
            "resiliencia": round(resiliencia, 4),
            "estabilidad": round(estabilidad, 4),
            "factor_estructural": round(factor_estructural, 4),
            "ideologia_base": ideologia_base
        }

        pesos_salida = {
            "PIB": pesos["PIB"],
            "Bienestar": pesos["Bienestar"],
            "Libertad": pesos["Libertad"],
            "modificador_crecimiento": pesos["modificador_crecimiento"],
            "bono_bienestar": pesos["bono_bienestar"],
            "bono_libertad": pesos["bono_libertad"],
            "volatilidad": pesos["volatilidad"]
        }

        return pesos_salida, indicadores

    def _generar_proyeccion_fallback(self, pais_datos: Dict, ideologia: str, codigo_pais: str) -> List[Dict]:
        """
        Genera una proyección sintética en caso de error con Gemini
        """
        pib_inicial = pais_datos.get('pib_inicial', 1000)
        proyeccion = []

        recursos = self._normalizar_recursos(pais_datos)
        pesos, indicadores = self._calcular_pesos_e_indicadores(pais_datos, ideologia, codigo_pais)

        seed = int(hashlib.sha256(codigo_pais.encode("utf-8")).hexdigest()[:8], 16)
        generador = random.Random(seed)

        base_crecimiento_anual = (
            0.008 +
            indicadores["score_pib"] * 0.04 +
            recursos["tecnologia"] * 0.015 +
            recursos["capital_humano"] * 0.012 +
            pesos["modificador_crecimiento"] +
            indicadores["factor_estructural"]
        )

        crecimiento_mensual_base = (1 + base_crecimiento_anual) ** (1 / 12) - 1
        volatilidad_base = pesos["volatilidad"]

        pib_actual = pib_inicial
        bienestar_base = 35 + indicadores["score_bienestar"] * 55 + pesos["bono_bienestar"]
        libertad_base = 30 + indicadores["score_libertad"] * 55 + pesos["bono_libertad"]

        ciclo_fase = generador.uniform(0, math.pi * 2)
        shock_pendiente = 0.0

        for mes in range(1, 51):
            ciclo = math.sin((mes / 6) + ciclo_fase) * 0.0025

            prob_shock = 0.06 + (0.04 * (1 - indicadores["estabilidad"]))
            shock = 0.0
            if generador.random() < prob_shock:
                direccion = -1 if generador.random() < 0.7 else 1
                magnitud = generador.uniform(0.015, 0.05) * (1 - indicadores["resiliencia"] * 0.6)
                shock = direccion * magnitud
                shock_pendiente = shock * 0.6
            else:
                shock_pendiente *= 0.6

            ruido = generador.gauss(0, volatilidad_base / 3)

            crecimiento_mensual = crecimiento_mensual_base + ciclo + shock + shock_pendiente + ruido
            crecimiento_mensual = max(-0.08, min(0.10, crecimiento_mensual))

            pib_actual *= (1 + crecimiento_mensual)

            bienestar = bienestar_base
            bienestar += (crecimiento_mensual * 120)
            bienestar -= max(0, -shock) * 120
            bienestar += indicadores["resiliencia"] * 5

            libertad = libertad_base
            libertad += recursos["tecnologia"] * 5
            libertad -= max(0, -shock) * 40
            libertad += (crecimiento_mensual * 30)

            proyeccion.append({
                "mes": mes,
                "PIB": round(pib_actual, 2),
                "Bienestar": round(max(0, min(100, bienestar)), 2),
                "Libertad": round(max(0, min(100, libertad)), 2)
            })

        return proyeccion
