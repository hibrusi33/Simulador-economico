# motor_economico.py
"""
Motor económico que utiliza Google Gemini para generar proyecciones realistas
"""

import os
import json
import google.generativeai as genai
from typing import Dict, List


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
        
        # Construir el prompt para Gemini
        prompt = f"""Actúa como un motor económico avanzado y geopolítico.

PAÍS: {pais_datos.get('nombre', codigo_pais)}
IDEOLOGÍA APLICADA: {ideologia}

RECURSOS Y CARACTERÍSTICAS (escala 0.0-1.0):
{json.dumps(pais_datos, indent=2)}

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
    
    def _generar_proyeccion_fallback(self, pais_datos: Dict, ideologia: str, codigo_pais: str) -> List[Dict]:
        """
        Genera una proyección sintética en caso de error con Gemini
        """
        pib_inicial = pais_datos.get('pib_inicial', 1000)
        proyeccion = []
        
        # Factores según ideología
        if ideologia.lower() in ["capitalismo", "capitalism"]:
            factor_crecimiento = 1.02
            bienestar_base = 60
            libertad_base = 85
        elif ideologia.lower() in ["comunismo", "communism"]:
            factor_crecimiento = 1.005
            bienestar_base = 70
            libertad_base = 40
        elif ideologia.lower() in ["teocracia", "theocracy"]:
            factor_crecimiento = 1.01
            bienestar_base = 55
            libertad_base = 35
        else:
            factor_crecimiento = 1.015
            bienestar_base = 65
            libertad_base = 70
        
        pib_actual = pib_inicial
        
        for mes in range(1, 51):
            # Añadir volatilidad
            volatilidad = (hash(codigo_pais + str(mes)) % 20 - 10) / 200
            pib_actual *= (factor_crecimiento + volatilidad)
            
            proyeccion.append({
                "mes": mes,
                "PIB": round(pib_actual, 2),
                "Bienestar": max(0, min(100, bienestar_base + (hash(str(mes)) % 20 - 10))),
                "Libertad": max(0, min(100, libertad_base + (hash(str(mes*2)) % 15 - 7)))
            })
        
        return proyeccion
