# api.py
"""
API FastAPI para el simulador geopolítico
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict, List
import os

from atlas_economico import obtener_pais, listar_paises, obtener_datos_completos
from motor_economico import MotorEconomico


# Modelos Pydantic
class ConfiguracionSimulacion(BaseModel):
    configuracion: Dict[str, str]  # {"Spain": "Comunismo", "USA": "Capitalismo", ...}


# Inicializar FastAPI
app = FastAPI(
    title="Simulador Geopolítico API",
    description="Backend para simulación económica y geopolítica mundial",
    version="1.0.0"
)

# Configurar CORS - Permitir todos los orígenes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todos los orígenes
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos HTTP
    allow_headers=["*"],  # Permite todos los headers
)

# Inicializar motor económico
motor = None

try:
    motor = MotorEconomico()
    print("✅ Motor económico inicializado correctamente con Gemini API")
except Exception as e:
    print(f"⚠️ Advertencia: No se pudo inicializar Gemini ({e}). Se usará modo fallback.")


# ==================== ENDPOINTS ====================

@app.get("/")
def raiz():
    """
    Endpoint raíz de bienvenida
    """
    return {
        "mensaje": "🌍 Simulador Geopolítico API",
        "version": "1.0.0",
        "endpoints": {
            "atlas": "/atlas",
            "pais_especifico": "/atlas/{codigo_pais}",
            "simular": "/simular_mundo"
        }
    }


@app.get("/atlas")
def obtener_atlas():
    """
    Devuelve el atlas completo de países con todos sus recursos
    """
    return {
        "paises": obtener_datos_completos(),
        "total": len(listar_paises())
    }


@app.get("/atlas/{codigo_pais}")
def obtener_datos_pais(codigo_pais: str):
    """
    Devuelve los recursos y características de un país específico
    
    Args:
        codigo_pais: Código del país (ej: "USA", "Spain", "China")
    
    Returns:
        Datos del país o error 404 si no existe
    """
    pais = obtener_pais(codigo_pais)
    
    if not pais:
        raise HTTPException(
            status_code=404,
            detail=f"País '{codigo_pais}' no encontrado. Países disponibles: {', '.join(listar_paises())}"
        )
    
    return {
        "codigo": codigo_pais,
        "datos": pais
    }


@app.post("/simular_mundo")
async def simular_mundo(config: ConfiguracionSimulacion):
    """
    Ejecuta una simulación completa del mundo económico
    
    Args:
        config: Objeto con configuración {codigo_pais: ideologia}
                Ejemplo: {"Spain": "Comunismo", "USA": "Capitalismo", "Russia": "Teocracia"}
    
    Returns:
        Objeto con proyecciones de 50 meses para cada país configurado
    """
    
    if not motor:
        raise HTTPException(
            status_code=503,
            detail="Motor económico no disponible. Configura GEMINI_API_KEY en variables de entorno."
        )
    
    configuracion = config.configuracion
    
    if not configuracion:
        raise HTTPException(
            status_code=400,
            detail="Debe proporcionar al menos un país con su ideología"
        )
    
    resultados = {}
    
    # Iterar sobre cada país configurado
    for codigo_pais, ideologia in configuracion.items():
        print(f"🔄 Simulando {codigo_pais} con ideología: {ideologia}")
        
        # Obtener datos del país
        pais_datos = obtener_pais(codigo_pais)
        
        if not pais_datos:
            print(f"⚠️ País {codigo_pais} no encontrado, saltando...")
            continue
        
        try:
            # Generar proyección con el motor económico
            proyeccion = motor.proyectar_economia(pais_datos, ideologia, codigo_pais)
            
            resultados[codigo_pais] = {
                "nombre": pais_datos.get("nombre", codigo_pais),
                "ideologia": ideologia,
                "recursos": pais_datos,
                "proyeccion": proyeccion
            }
            
            print(f"✅ Simulación completada para {codigo_pais}")
            
        except Exception as e:
            print(f"❌ Error simulando {codigo_pais}: {e}")
            resultados[codigo_pais] = {
                "nombre": pais_datos.get("nombre", codigo_pais),
                "ideologia": ideologia,
                "error": str(e)
            }
    
    return {
        "exito": True,
        "paises_simulados": len(resultados),
        "resultados": resultados
    }


@app.get("/health")
def health_check():
    """
    Endpoint para verificar el estado del servicio
    """
    gemini_status = "conectado" if motor else "desconectado"
    
    return {
        "status": "activo",
        "gemini_api": gemini_status,
        "paises_disponibles": len(listar_paises())
    }


# Ejecutar con: uvicorn api:app --reload --host 0.0.0.0 --port 8000
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
