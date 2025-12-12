# 📁 Estructura Completa del Proyecto

```
simulador-geopolitico/
│
├── 📄 .gitignore                    # Ignora venv, node_modules, .env, etc.
├── 📄 README.md                     # Documentación principal
├── 📄 CLAUDE_CODE.md                # Guía específica para Claude Code
├── 📄 LICENSE                       # Licencia MIT (opcional)
│
├── 🔧 install.sh                    # Script de instalación Linux/Mac
├── 🔧 install.bat                   # Script de instalación Windows
│
├── 📂 backend/                      # Backend Python/FastAPI
│   │
│   ├── 📄 api.py                   # Endpoints REST (puerto 8000)
│   │   ├── GET  /                  # Bienvenida
│   │   ├── GET  /atlas             # Todos los países
│   │   ├── GET  /atlas/{codigo}    # País específico
│   │   ├── POST /simular_mundo     # Ejecutar simulación ⭐
│   │   └── GET  /health            # Estado del servicio
│   │
│   ├── 📄 atlas_economico.py       # Base de datos de 15 países
│   │   └── ATLAS_MUNDIAL           # Diccionario con recursos (0.0-1.0)
│   │       ├── USA, China, Russia
│   │       ├── Germany, Japan, Spain
│   │       ├── India, Brazil, SaudiArabia
│   │       ├── France, UK, Mexico
│   │       └── SouthKorea, Australia, Canada
│   │
│   ├── 📄 motor_economico.py       # Motor de IA con Google Gemini
│   │   └── MotorEconomico
│   │       ├── __init__()          # Conecta con Gemini API
│   │       ├── proyectar_economia() # Genera 50 meses de datos
│   │       └── _generar_proyeccion_fallback() # Backup sintético
│   │
│   ├── 📄 requirements.txt         # Dependencias Python
│   │   ├── fastapi==0.115.0
│   │   ├── uvicorn[standard]==0.32.0
│   │   ├── google-generativeai==0.8.3
│   │   └── pydantic==2.9.0
│   │
│   ├── 📄 .env.example             # Template para variables de entorno
│   ├── 📄 .env                     # ⚠️ API Keys (NO subir a Git)
│   ├── 📄 README.md                # Documentación del backend
│   │
│   └── 📂 venv/                    # ⚠️ Entorno virtual Python (ignorado)
│
├── 📂 frontend/                    # Frontend React/Vite
│   │
│   ├── 📂 src/
│   │   │
│   │   ├── 📂 components/
│   │   │   │
│   │   │   ├── 📄 GlobeSelector.jsx    # Globo 3D interactivo ⭐
│   │   │   │   ├── react-globe.gl      # Visualización 3D
│   │   │   │   ├── polygonAltitude     # Altura = PIB
│   │   │   │   ├── polygonCapColor     # Color = Bienestar
│   │   │   │   ├── polygonsTransitionDuration: 1000ms
│   │   │   │   └── Mapeo ISO → Backend (isoToBackendCode)
│   │   │   │
│   │   │   └── 📄 Sidebar.jsx          # Panel de control ⭐
│   │   │       ├── Fase Setup:
│   │   │       │   ├── Lista de países seleccionados
│   │   │       │   ├── Barras de recursos (rojo/amarillo/verde)
│   │   │       │   ├── Rejilla de ideologías (10 botones)
│   │   │       │   └── Botón "INICIAR SIMULACIÓN"
│   │   │       │
│   │   │       └── Fase Running:
│   │   │           ├── Progreso temporal (Mes X/50)
│   │   │           ├── Selector de país para análisis
│   │   │           ├── LineChart (comparativa mundial)
│   │   │           └── AreaChart (país individual)
│   │   │
│   │   ├── 📄 App.jsx                  # Layout principal ⭐
│   │   │   ├── Estado Global:
│   │   │   │   ├── gamePhase ('setup' | 'running')
│   │   │   │   ├── selectedCountries {code: ideology}
│   │   │   │   ├── simulationData
│   │   │   │   ├── currentMonth (0-49)
│   │   │   │   └── currentMonthData
│   │   │   │
│   │   │   └── Layout Responsive:
│   │   │       ├── Desktop: Sidebar (1/3) + Globo (2/3)
│   │   │       └── Mobile: Globo arriba + Controles abajo
│   │   │
│   │   ├── 📄 main.jsx                 # Entry point React
│   │   └── 📄 index.css                # Estilos Cyberpunk ⭐
│   │       ├── Tailwind directives
│   │       ├── Scrollbar personalizado cyan
│   │       ├── Animación glow
│   │       └── Efectos opcionales (scanline, glitch)
│   │
│   ├── 📄 index.html                   # HTML base
│   ├── 📄 package.json                 # Dependencias Node.js
│   │   ├── react@18.3.1
│   │   ├── react-globe.gl@2.27.2
│   │   ├── three@0.160.0
│   │   ├── recharts@2.12.0
│   │   ├── d3-scale-chromatic@3.1.0
│   │   └── tailwindcss@3.4.1
│   │
│   ├── 📄 vite.config.js               # Configuración Vite
│   ├── 📄 tailwind.config.js           # Colores cyberpunk
│   ├── 📄 postcss.config.js            # PostCSS + Autoprefixer
│   ├── 📄 README.md                    # Documentación del frontend
│   │
│   └── 📂 node_modules/                # ⚠️ Dependencias (ignorado)
│
└── 📂 .git/                            # Control de versiones Git

```

---

## 🔑 Archivos Clave

### ⭐ Más Importantes

1. **`backend/api.py`** - API REST principal
2. **`backend/motor_economico.py`** - Integración con Gemini AI
3. **`frontend/src/App.jsx`** - Lógica principal del frontend
4. **`frontend/src/components/GlobeSelector.jsx`** - Visualización 3D
5. **`frontend/src/components/Sidebar.jsx`** - Panel de control y gráficas

### 📝 Configuración

- **`backend/.env`** - API Keys (crear manualmente)
- **`backend/requirements.txt`** - Dependencias Python
- **`frontend/package.json`** - Dependencias Node.js
- **`frontend/tailwind.config.js`** - Colores personalizados

### 📚 Documentación

- **`README.md`** - Guía general del proyecto
- **`CLAUDE_CODE.md`** - Referencia para Claude Code
- **`backend/README.md`** - Guía del backend
- **`frontend/README.md`** - Guía del frontend

---

## 📊 Flujo de Datos

```
┌─────────────────────────────────────────────────────────┐
│                     USUARIO (Browser)                    │
│                  http://localhost:5173                   │
└───────────────────────────┬─────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────┐
│                  FRONTEND (React/Vite)                   │
├─────────────────────────────────────────────────────────┤
│  ┌─────────────────┐  ┌────────────────────────────┐   │
│  │   App.jsx       │  │  GlobeSelector.jsx         │   │
│  │  (Estado Global)│──│  • Visualización 3D         │   │
│  │                 │  │  • polygonAltitude = PIB    │   │
│  │  gamePhase      │  │  • polygonColor = Bienestar │   │
│  │  selectedCountries│ └────────────────────────────┘   │
│  │  simulationData │                                    │
│  │  currentMonth   │  ┌────────────────────────────┐   │
│  └────────┬────────┘  │  Sidebar.jsx               │   │
│           │           │  • Panel de control         │   │
│           └───────────│  • Gráficas Recharts        │   │
│                       │  • Barras de recursos       │   │
│                       └────────────────────────────┘   │
└─────────────────────────────────────────────────────────┘
                            │
                   POST /simular_mundo
                   {configuracion: {...}}
                            │
                            ▼
┌─────────────────────────────────────────────────────────┐
│               BACKEND (FastAPI - Puerto 8000)            │
├─────────────────────────────────────────────────────────┤
│  ┌──────────────────────────────────────────────────┐  │
│  │  api.py (Endpoints REST)                         │  │
│  │  • /atlas                                        │  │
│  │  • /atlas/{codigo}                               │  │
│  │  • /simular_mundo ⭐                             │  │
│  │  • /health                                       │  │
│  └─────────┬────────────────────────────────────────┘  │
│            │                                            │
│            ▼                                            │
│  ┌──────────────────────────────────────────────────┐  │
│  │  motor_economico.py                              │  │
│  │  • proyectar_economia()                          │  │
│  │  • Llama a Google Gemini API                     │  │
│  │  • Genera 50 meses de datos                      │  │
│  └─────────┬────────────────────────────────────────┘  │
│            │                                            │
│            ▼                                            │
│  ┌──────────────────────────────────────────────────┐  │
│  │  atlas_economico.py                              │  │
│  │  ATLAS_MUNDIAL = {                               │  │
│  │    "Spain": {...},                               │  │
│  │    "USA": {...},                                 │  │
│  │    ...                                           │  │
│  │  }                                               │  │
│  └──────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────┐
│              GOOGLE GEMINI API (Gemini 1.5 Flash)        │
│  • Procesa recursos + ideología                         │
│  • Genera proyecciones económicas realistas             │
│  • Devuelve 50 meses con PIB, Bienestar, Libertad       │
└─────────────────────────────────────────────────────────┘
```

---

## 🎯 Puntos de Entrada

### Para Desarrollo

```bash
# Terminal 1: Backend
cd backend
source venv/bin/activate  # Linux/Mac
uvicorn api:app --reload --host 0.0.0.0 --port 8000

# Terminal 2: Frontend
cd frontend
npm run dev
```

### Para Producción

```bash
# Backend
cd backend
uvicorn api:app --host 0.0.0.0 --port 8000

# Frontend
cd frontend
npm run build
npm run preview
```

---

## 📦 Tamaños Aproximados

- **Backend** (sin venv): ~50 KB
- **Backend** (con venv): ~200 MB
- **Frontend** (sin node_modules): ~100 KB
- **Frontend** (con node_modules): ~400 MB
- **Total con dependencias**: ~600 MB

---

## 🔐 Archivos Sensibles (NO subir a Git)

- ❌ `backend/.env` - Contiene GEMINI_API_KEY
- ❌ `backend/venv/` - Entorno virtual Python
- ❌ `frontend/node_modules/` - Dependencias Node.js
- ❌ `frontend/dist/` - Build de producción
- ❌ Cualquier archivo `*.log`

Todos estos están incluidos en `.gitignore` ✅

---

**Esta estructura está optimizada para desarrollo colaborativo y despliegue rápido.**
