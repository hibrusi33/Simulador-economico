# 🌍 Simulador Geopolítico y Económico en Tiempo Real

![Versión](https://img.shields.io/badge/versión-1.0.0-cyan)
![Python](https://img.shields.io/badge/Python-3.10+-blue)
![React](https://img.shields.io/badge/React-18.3-61dafb)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115-009688)

**Simulador económico mundial impulsado por IA** que permite visualizar en 3D cómo diferentes sistemas políticos (Capitalismo, Comunismo, Teocracia, etc.) afectan la economía de países reales durante 50 meses.

## 📸 Preview

- 🌍 **Globo terráqueo 3D interactivo** con países que se elevan según su PIB
- 🎨 **Estética Cyberpunk Minimalista** (fondo negro, neón cyan)
- 📊 **Gráficas en tiempo real** con Recharts
- 🤖 **Motor de IA con Google Gemini** para proyecciones económicas realistas

---

## 🏗️ Arquitectura

```
simulador-geopolitico/
├── backend/                    # FastAPI + Google Gemini
│   ├── api.py                 # Endpoints REST
│   ├── atlas_economico.py     # Base de datos de 15 países
│   ├── motor_economico.py     # Integración con Gemini AI
│   ├── requirements.txt
│   └── README.md
│
├── frontend/                   # React + Vite + Tailwind
│   ├── src/
│   │   ├── components/
│   │   │   ├── GlobeSelector.jsx    # Globo 3D (react-globe.gl)
│   │   │   └── Sidebar.jsx          # Panel de control y gráficas
│   │   ├── App.jsx                   # Layout principal
│   │   ├── main.jsx
│   │   └── index.css                 # Estilos Cyberpunk
│   ├── package.json
│   ├── vite.config.js
│   └── README.md
│
├── .gitignore
└── README.md                   # Este archivo
```

---

## 🚀 Instalación Rápida

### Requisitos Previos

- **Python 3.10+**
- **Node.js 18+** y npm
- **API Key de Google Gemini** ([obtener aquí](https://makersuite.google.com/app/apikey))

### 1️⃣ Clonar el Repositorio

```bash
git clone https://github.com/tu-usuario/simulador-geopolitico.git
cd simulador-geopolitico
```

### 2️⃣ Backend (Python/FastAPI)

```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# En Linux/Mac:
source venv/bin/activate
# En Windows:
venv\Scripts\activate

# Instalar dependencias
cd backend
pip install -r requirements.txt

# Configurar API Key de Gemini
cp .env.example .env
# Editar .env y añadir tu GEMINI_API_KEY

# Iniciar servidor
uvicorn api:app --reload --host 0.0.0.0 --port 8000
```

El backend estará disponible en **http://localhost:8000**

### 3️⃣ Frontend (React/Vite)

```bash
# En otra terminal
cd frontend
npm install

# Iniciar servidor de desarrollo
npm run dev
```

El frontend estará disponible en **http://localhost:5173**

---

## 🎮 Cómo Usar

### Fase 1: Configuración
1. **Haz clic en países del globo 3D** para seleccionarlos
2. **Asigna una ideología** a cada país:
   - 💰 Capitalismo
   - 🚩 Comunismo
   - 🕌 Teocracia
   - ⚙️ Tecnocracia
   - Y más...
3. **Revisa los recursos del país** (petróleo, tecnología, capital humano, etc.)
4. **Presiona "INICIAR SIMULACIÓN"**

### Fase 2: Simulación
- La simulación avanza automáticamente **mes a mes** (1.2 seg/mes)
- Los países se **elevan o hunden** en el globo según su PIB
- Los colores cambian según el **Bienestar**:
  - 🟢 Verde = Alto Bienestar (80-100)
  - 🟡 Amarillo = Medio (40-80)
  - 🔴 Rojo = Bajo (0-40)
- **Gráficas interactivas** muestran la evolución económica
- Puedes **pausar, reanudar o reiniciar** en cualquier momento

---

## 🌍 Países Disponibles

| Código | País | PIB Inicial | Recursos Destacados |
|--------|------|-------------|---------------------|
| USA | Estados Unidos | $25,000B | Tecnología (95%), Recursos Fósiles (85%) |
| China | China | $18,000B | Tecnología (85%), Capital Humano (75%) |
| Russia | Rusia | $2,000B | Recursos Fósiles (95%) |
| Germany | Alemania | $4,500B | Tecnología (92%), Capital Humano (90%) |
| Japan | Japón | $4,200B | Tecnología (93%), Acceso Marítimo (95%) |
| Spain | España | $1,600B | Potencial Renovable (85%) |
| India | India | $3,500B | Tierra Arable (70%), Potencial Renovable (80%) |
| Brazil | Brasil | $2,000B | Potencial Renovable (90%), Tierra Arable (80%) |
| ... | ... | ... | ... |

*Total: 15 países*

---

## 🤖 Motor de IA (Google Gemini)

El backend utiliza **Google Gemini 1.5 Flash** para generar proyecciones económicas realistas:

- ✅ **Toma en cuenta**:
  - Recursos naturales del país
  - Ideología política asignada
  - Capital humano y tecnología
  - Acceso a mercados (marítimo, tierra arable)

- ✅ **Genera**:
  - 50 meses de proyecciones
  - PIB, Bienestar y Libertad por mes
  - Volatilidad y eventos geopolíticos aleatorios

- ✅ **Fallback**:
  - Si Gemini falla, usa algoritmo sintético básico

---

## 📡 API Endpoints

### Backend (puerto 8000)

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/` | Información de la API |
| GET | `/atlas` | Todos los países con recursos |
| GET | `/atlas/{codigo_pais}` | Datos de un país específico |
| POST | `/simular_mundo` | Ejecutar simulación de 50 meses |
| GET | `/health` | Estado del servicio |

**Ejemplo de uso:**

```bash
# Obtener datos de España
curl http://localhost:8000/atlas/Spain

# Simular economía
curl -X POST http://localhost:8000/simular_mundo \
  -H "Content-Type: application/json" \
  -d '{
    "configuracion": {
      "Spain": "Socialismo Democrático",
      "USA": "Capitalismo Neoliberal"
    }
  }'
```

---

## 🎨 Stack Tecnológico

### Backend
- **FastAPI** - Framework web moderno
- **Google Gemini AI** - Motor de inteligencia artificial
- **Pydantic** - Validación de datos
- **Uvicorn** - Servidor ASGI

### Frontend
- **React 18** - Biblioteca UI
- **Vite** - Build tool ultrarrápido
- **Tailwind CSS** - Estilos utility-first
- **react-globe.gl** - Visualización 3D del globo
- **Three.js** - Renderizado WebGL
- **Recharts** - Gráficas interactivas
- **d3-scale-chromatic** - Interpolación de colores

---

## 🛠️ Desarrollo

### Scripts Disponibles

**Backend:**
```bash
# Desarrollo
uvicorn api:app --reload

# Producción
uvicorn api:app --host 0.0.0.0 --port 8000
```

**Frontend:**
```bash
npm run dev      # Servidor de desarrollo
npm run build    # Compilar para producción
npm run preview  # Preview de producción
```

### Variables de Entorno

**Backend (`backend/.env`):**
```env
GEMINI_API_KEY=tu_api_key_aqui
```

---

## 📝 Características Destacadas

### ✨ Visualización 3D Avanzada
- Países se extruyen verticalmente según PIB
- Interpolación de colores suave (rojo → amarillo → verde)
- Transiciones animadas de 1000ms entre estados
- Tooltips informativos con datos económicos
- Atmósfera cyberpunk con neón cyan

### 📊 Gráficas Interactivas
- **Comparativa Mundial**: LineChart con todas las economías
- **Análisis Detallado**: AreaChart con PIB + Bienestar + Libertad
- Tooltips personalizados estilo cyberpunk
- Leyendas interactivas
- Gradientes de color para áreas

### 🎮 UX/UI Profesional
- Diseño responsive (móvil + escritorio)
- Estética cyberpunk minimalista
- Feedback visual inmediato
- Animaciones fluidas
- Controles intuitivos

---

## 🐛 Troubleshooting

**Problema:** "GEMINI_API_KEY no proporcionada"
- **Solución:** Crea el archivo `backend/.env` con tu API Key

**Problema:** CORS errors
- **Solución:** El backend ya tiene CORS habilitado para `*`

**Problema:** Globo no se muestra
- **Solución:** Verifica que `react-globe.gl` esté instalado: `npm install react-globe.gl`

**Problema:** Backend no responde
- **Solución:** Verifica que esté corriendo en puerto 8000 y sin errores

**Problema:** Simulación muy lenta
- **Solución:** Normal. Gemini procesa cada país individualmente (10-30s por simulación)

---

## 📄 Licencia

Este proyecto está bajo la licencia MIT. Ver archivo `LICENSE` para más detalles.

---

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Por favor:

1. Fork el proyecto
2. Crea una rama (`git checkout -b feature/nueva-funcionalidad`)
3. Commit tus cambios (`git commit -m 'Añadir nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Abre un Pull Request

---

## 🙏 Agradecimientos

- **Google Gemini** por el motor de IA
- **react-globe.gl** por la visualización 3D
- **Recharts** por las gráficas
- **Tailwind CSS** por el sistema de diseño

---

## 📧 Contacto

Si tienes preguntas o sugerencias, abre un issue en GitHub.

---

**⚡ ¡Disfruta simulando el colapso económico mundial!** 🌍📉😄
