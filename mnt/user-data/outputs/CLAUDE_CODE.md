# 📘 Instrucciones para Claude Code

Este documento contiene información específica para que Claude Code pueda ayudarte mejor con este proyecto.

## 🎯 Contexto del Proyecto

Este es un **Simulador Geopolítico y Económico en Tiempo Real** que consta de:

1. **Backend**: FastAPI + Google Gemini AI (Python)
2. **Frontend**: React + Vite + Tailwind CSS + react-globe.gl

El proyecto permite a los usuarios:
- Seleccionar países en un globo 3D
- Asignar ideologías políticas (Capitalismo, Comunismo, etc.)
- Simular 50 meses de evolución económica con IA
- Visualizar resultados en tiempo real (PIB, Bienestar, Libertad)

---

## 📂 Estructura del Proyecto

```
simulador-geopolitico/
├── backend/                    # FastAPI + Google Gemini
│   ├── api.py                 # Endpoints REST principales
│   ├── atlas_economico.py     # BD de 15 países con recursos
│   ├── motor_economico.py     # Integración con Gemini AI
│   ├── requirements.txt       # Dependencias Python
│   └── .env.example          # Template para API keys
│
├── frontend/                   # React + Vite
│   ├── src/
│   │   ├── components/
│   │   │   ├── GlobeSelector.jsx    # Globo 3D interactivo
│   │   │   └── Sidebar.jsx          # Panel de control + gráficas
│   │   ├── App.jsx                   # Layout principal
│   │   └── index.css                 # Estilos Cyberpunk
│   └── package.json
│
├── .gitignore
└── README.md
```

---

## 🔑 Variables de Entorno Necesarias

### Backend (`backend/.env`)
```env
GEMINI_API_KEY=AIza...  # Obtener en https://makersuite.google.com/app/apikey
```

**Nota**: El `.env` está en `.gitignore`, así que deberás crearlo manualmente.

---

## 🚀 Comandos Útiles

### Backend
```bash
# Activar entorno virtual
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Instalar dependencias
cd backend
pip install -r requirements.txt

# Iniciar servidor
uvicorn api:app --reload --host 0.0.0.0 --port 8000
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

---

## 🧩 Componentes Principales

### Backend

#### `api.py`
- **Puerto**: 8000
- **CORS**: Habilitado para todos los orígenes (`*`)
- **Endpoints**:
  - `GET /atlas` - Todos los países
  - `GET /atlas/{codigo}` - País específico
  - `POST /simular_mundo` - Ejecutar simulación
  - `GET /health` - Estado del servicio

#### `atlas_economico.py`
- Diccionario `ATLAS_MUNDIAL` con 15 países
- Cada país tiene 7 variables (0.0-1.0):
  - `recursos_fosiles`
  - `potencial_renovable`
  - `tecnologia`
  - `capital_humano`
  - `tierra_arable`
  - `acceso_maritimo`
  - `pib_inicial`

#### `motor_economico.py`
- Clase `MotorEconomico` que conecta con Gemini
- Método `proyectar_economia()` genera 50 meses
- Fallback sintético si Gemini falla

### Frontend

#### `GlobeSelector.jsx`
- Usa `react-globe.gl` y `three.js`
- Props importantes:
  - `currentMonthData` - Datos del mes actual
  - `onSelectCountry` - Callback al hacer clic
  - `selectedCountries` - Array de códigos seleccionados
- Visualización:
  - `polygonAltitude` → PIB (extrusión vertical)
  - `polygonCapColor` → Bienestar (rojo→amarillo→verde)
  - `polygonsTransitionDuration` → 1000ms

#### `Sidebar.jsx`
- Gestiona dos fases: `'setup'` y `'running'`
- En Setup:
  - Muestra recursos con barras de progreso
  - Rejilla de 10 ideologías con iconos
  - Botón "INICIAR SIMULACIÓN"
- En Running:
  - Progreso temporal (Mes X/50)
  - Gráficas Recharts:
    - LineChart comparativo (todos los países)
    - AreaChart detallado (país individual)

#### `App.jsx`
- Estado global:
  - `gamePhase`: 'setup' | 'running'
  - `selectedCountries`: {countryCode: ideology}
  - `simulationData`: Respuesta del backend
  - `currentMonth`: 0-49
- Layout responsive:
  - Desktop: Sidebar (1/3) + Globo (2/3)
  - Mobile: Globo arriba + Controles abajo

---

## 🎨 Estética Cyberpunk

### Colores Principales
- **Background**: Negro (#000000)
- **Acentos**: Cyan (#00ffff)
- **Borders**: Cyan semitransparente (#00ffff con opacidad 20-30%)
- **Gradientes**: De cyan a azul/púrpura

### Tipografía
- **Font**: Courier New, monospace
- **Títulos**: Bold, tracking-wider
- **Texto**: Gris claro (#d1d5db)

### Componentes Visuales
- Fondos con `backdrop-blur-sm`
- Bordes finos con opacidad baja
- Transiciones suaves (300-1000ms)
- Sombras con efecto neón en botones importantes

---

## 🐛 Problemas Comunes y Soluciones

### Backend

**Error: "GEMINI_API_KEY no proporcionada"**
```bash
# Crear archivo .env en backend/
cd backend
cp .env.example .env
# Editar .env y añadir la clave
```

**Error: "ModuleNotFoundError: No module named 'fastapi'"**
```bash
# Activar venv y reinstalar
source venv/bin/activate
pip install -r requirements.txt
```

**Puerto 8000 ya en uso**
```bash
# Cambiar puerto en api.py o matar proceso
lsof -ti:8000 | xargs kill -9  # Mac/Linux
```

### Frontend

**Error: "Cannot find module 'react-globe.gl'"**
```bash
cd frontend
npm install react-globe.gl three d3-scale-chromatic recharts
```

**Error: "Failed to fetch" al iniciar simulación**
- Verifica que el backend esté corriendo en puerto 8000
- Comprueba que CORS esté habilitado (ya lo está por defecto)

**Globo no se renderiza**
- Verifica que WebGL esté habilitado en el navegador
- Comprueba la consola del navegador por errores de Three.js

---

## 🔍 Datos de Ejemplo

### Request a `/simular_mundo`
```json
{
  "configuracion": {
    "Spain": "Socialismo Democrático",
    "USA": "Capitalismo Neoliberal",
    "China": "Comunismo"
  }
}
```

### Response esperada
```json
{
  "exito": true,
  "paises_simulados": 3,
  "resultados": {
    "Spain": {
      "nombre": "España",
      "ideologia": "Socialismo Democrático",
      "recursos": { ... },
      "proyeccion": [
        { "mes": 1, "PIB": 1600, "Bienestar": 70, "Libertad": 80 },
        { "mes": 2, "PIB": 1620, "Bienestar": 72, "Libertad": 79 },
        ...
      ]
    }
  }
}
```

---

## 📊 Mapeo de Códigos País

| Código Backend | Código ISO (GeoJSON) | Nombre Completo |
|----------------|----------------------|-----------------|
| USA | USA | Estados Unidos |
| China | CHN | China |
| Russia | RUS | Rusia |
| Germany | DEU | Alemania |
| Japan | JPN | Japón |
| Spain | ESP | España |
| India | IND | India |
| Brazil | BRA | Brasil |
| SaudiArabia | SAU | Arabia Saudita |
| France | FRA | Francia |
| UK | GBR | Reino Unido |
| Mexico | MEX | México |
| SouthKorea | KOR | Corea del Sur |
| Australia | AUS | Australia |
| Canada | CAN | Canadá |

**Importante**: El mapeo está hardcodeado en `GlobeSelector.jsx` en el objeto `isoToBackendCode`.

---

## 🧪 Testing Manual

### Flujo Básico
1. Iniciar backend y frontend
2. Abrir http://localhost:5173
3. Hacer clic en 3 países del globo
4. Asignar ideologías diferentes a cada uno
5. Presionar "INICIAR SIMULACIÓN"
6. Esperar 10-30 segundos (Gemini procesando)
7. Observar animación de 50 meses (1.2s por mes)
8. Verificar que:
   - Países cambian de altura según PIB
   - Colores cambian según Bienestar
   - Gráficas se actualizan correctamente
   - Controles funcionan (Pausar/Reanudar/Reiniciar)

---

## 💡 Sugerencias para Mejoras Futuras

Si quieres extender el proyecto, considera:

1. **Persistencia**: Guardar simulaciones en localStorage o base de datos
2. **Exportación**: Descargar resultados como CSV/JSON
3. **Eventos Aleatorios**: Guerras, pandemias, descubrimientos tecnológicos
4. **Comercio**: Relaciones comerciales entre países
5. **Modo Multijugador**: Varios usuarios controlando diferentes países
6. **Análisis Comparativo**: Vista de ranking mundial
7. **Predicción ML**: Entrenar modelo con datos históricos reales
8. **Modo Desafío**: Objetivos específicos a cumplir

---

## 🛠️ Tips para Claude Code

- El proyecto usa **ES6 imports** en todo el frontend
- Los componentes React usan **hooks** (useState, useEffect)
- No hay TypeScript (todo es JavaScript puro)
- El backend usa **async/await** para llamadas a Gemini
- CORS está configurado para permitir `*` en desarrollo
- La API de Gemini puede tardar varios segundos en responder

---

## 📚 Recursos Útiles

- **FastAPI Docs**: https://fastapi.tiangolo.com/
- **react-globe.gl**: https://github.com/vasturiano/react-globe.gl
- **Recharts**: https://recharts.org/
- **Tailwind CSS**: https://tailwindcss.com/docs
- **Google Gemini**: https://ai.google.dev/docs

---

**¿Necesitas ayuda? Claude Code está listo para asistirte con cualquier aspecto del proyecto.**
