# 🛠️ Comandos Útiles - Simulador Geopolítico

## 📋 Tabla de Contenidos
- [Setup Inicial](#setup-inicial)
- [Desarrollo](#desarrollo)
- [Testing](#testing)
- [Debugging](#debugging)
- [Git](#git)
- [Producción](#producción)
- [Troubleshooting](#troubleshooting)

---

## 🚀 Setup Inicial

### Instalación Automática
```bash
# Linux/Mac
chmod +x install.sh
./install.sh

# Windows
install.bat
```

### Instalación Manual

#### Backend
```bash
cd backend

# Crear y activar entorno virtual
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Instalar dependencias
pip install -r requirements.txt

# Configurar .env
cp .env.example .env
nano .env  # Añadir GEMINI_API_KEY
```

#### Frontend
```bash
cd frontend

# Instalar dependencias
npm install

# O con yarn
yarn install
```

---

## 💻 Desarrollo

### Backend

```bash
# Activar entorno virtual
cd backend
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Iniciar servidor de desarrollo (con hot-reload)
uvicorn api:app --reload --host 0.0.0.0 --port 8000

# Iniciar en otro puerto
uvicorn api:app --reload --port 8001

# Ver logs detallados
uvicorn api:app --reload --log-level debug
```

### Frontend

```bash
cd frontend

# Iniciar servidor de desarrollo
npm run dev

# Iniciar en otro puerto
npm run dev -- --port 3000

# Abrir navegador automáticamente
npm run dev -- --open
```

---

## 🧪 Testing

### Backend

```bash
cd backend
source venv/bin/activate

# Test manual con curl
curl http://localhost:8000/

# Test de endpoints
curl http://localhost:8000/atlas
curl http://localhost:8000/atlas/Spain
curl http://localhost:8000/health

# Test de simulación
curl -X POST http://localhost:8000/simular_mundo \
  -H "Content-Type: application/json" \
  -d '{"configuracion": {"Spain": "Comunismo", "USA": "Capitalismo"}}'
```

### Frontend

```bash
cd frontend

# Ejecutar build de prueba
npm run build

# Preview del build
npm run preview
```

---

## 🐛 Debugging

### Backend

```bash
# Ver logs del servidor
# Los logs aparecen automáticamente en la terminal donde ejecutaste uvicorn

# Python debugger (añadir en el código)
import pdb; pdb.set_trace()

# Ver variables de entorno
cd backend
source venv/bin/activate
python -c "import os; print(os.getenv('GEMINI_API_KEY'))"
```

### Frontend

```bash
# Inspeccionar en navegador
# F12 o Ctrl+Shift+I (Windows/Linux)
# Cmd+Option+I (Mac)

# Logs en consola (añadir en el código)
console.log('Debug:', variable);
console.table(data);

# Limpiar caché de Vite
rm -rf frontend/.vite
npm run dev
```

---

## 📦 Git

### Inicializar Repositorio

```bash
# Inicializar Git
git init

# Añadir archivos
git add .

# Commit inicial
git commit -m "🎉 Initial commit - Simulador Geopolítico"

# Conectar con GitHub
git remote add origin https://github.com/tu-usuario/simulador-geopolitico.git
git branch -M main
git push -u origin main
```

### Flujo de Trabajo

```bash
# Ver estado
git status

# Añadir archivos
git add .
git add backend/api.py
git add frontend/src/App.jsx

# Commit
git commit -m "✨ feat: Añadir gráficas detalladas"

# Push
git push origin main

# Pull (actualizar local)
git pull origin main

# Ver historial
git log --oneline --graph
```

### Branches

```bash
# Crear branch
git checkout -b feature/nueva-funcionalidad

# Cambiar de branch
git checkout main

# Listar branches
git branch

# Merge branch
git checkout main
git merge feature/nueva-funcionalidad

# Eliminar branch
git branch -d feature/nueva-funcionalidad
```

---

## 🚀 Producción

### Backend

```bash
cd backend
source venv/bin/activate

# Iniciar en modo producción
uvicorn api:app --host 0.0.0.0 --port 8000 --workers 4

# Con Gunicorn (recomendado)
pip install gunicorn
gunicorn api:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```

### Frontend

```bash
cd frontend

# Build de producción
npm run build

# Preview del build
npm run preview

# El build estará en frontend/dist/
# Servir con cualquier servidor estático:
npx serve dist -p 3000
```

---

## 🔧 Mantenimiento

### Backend

```bash
cd backend
source venv/bin/activate

# Actualizar pip
pip install --upgrade pip

# Actualizar una dependencia
pip install --upgrade fastapi

# Actualizar todas las dependencias
pip install --upgrade -r requirements.txt

# Listar dependencias instaladas
pip list

# Generar nuevo requirements.txt
pip freeze > requirements.txt
```

### Frontend

```bash
cd frontend

# Actualizar dependencias
npm update

# Actualizar una dependencia específica
npm install react@latest

# Ver dependencias desactualizadas
npm outdated

# Auditoría de seguridad
npm audit
npm audit fix
```

---

## 🔍 Troubleshooting

### Backend

```bash
# Puerto 8000 ocupado
# Linux/Mac
lsof -ti:8000 | xargs kill -9

# Windows
netstat -ano | findstr :8000
taskkill /PID <PID> /F

# Reinstalar dependencias
cd backend
rm -rf venv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Verificar instalación de uvicorn
pip show uvicorn
```

### Frontend

```bash
# Limpiar node_modules
cd frontend
rm -rf node_modules package-lock.json
npm install

# Limpiar caché de npm
npm cache clean --force

# Limpiar caché de Vite
rm -rf .vite

# Verificar versión de Node
node --version
npm --version
```

### CORS Issues

```bash
# Verificar que el backend esté corriendo
curl http://localhost:8000/health

# Verificar CORS en api.py
# Debe tener: allow_origins=["*"]
```

### Gemini API

```bash
# Verificar API Key
cd backend
source venv/bin/activate
python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('Key:', os.getenv('GEMINI_API_KEY')[:10] + '...')"

# Test directo de Gemini
python << EOF
import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
model = genai.GenerativeModel('gemini-1.5-flash')
response = model.generate_content('Hola')
print(response.text)
EOF
```

---

## 📊 Monitoreo

### Ver Logs

```bash
# Backend logs (aparecen en terminal de uvicorn)
# Para guardarlos en archivo:
cd backend
source venv/bin/activate
uvicorn api:app --reload 2>&1 | tee backend.log

# Frontend logs
# Usar las DevTools del navegador (F12)
```

### Recursos del Sistema

```bash
# Ver procesos Python
ps aux | grep python

# Ver procesos Node
ps aux | grep node

# Uso de puertos
netstat -tuln | grep LISTEN
```

---

## 🎨 Desarrollo de Estilos

### Tailwind CSS

```bash
cd frontend

# Regenerar CSS (si usas watch mode)
npx tailwindcss -i ./src/index.css -o ./dist/output.css --watch

# Ver todas las clases disponibles
npx tailwindcss -h
```

---

## 📱 Testing Responsive

```bash
# Frontend - Iniciar en diferentes dispositivos
cd frontend
npm run dev -- --host

# Esto permitirá acceso desde otros dispositivos en tu red local
# Accede desde: http://<tu-ip>:5173
```

---

## 🔐 Seguridad

```bash
# Verificar .env no esté en Git
git status | grep .env

# Ver lo que se ignorará
git status --ignored

# Limpiar cache de Git si subiste .env por error
git rm --cached backend/.env
git commit -m "Remove .env from tracking"
```

---

## 💡 Tips Útiles

### Aliases Útiles (añadir a ~/.bashrc o ~/.zshrc)

```bash
# Backend
alias sim-backend="cd ~/simulador-geopolitico/backend && source venv/bin/activate && uvicorn api:app --reload"

# Frontend
alias sim-frontend="cd ~/simulador-geopolitico/frontend && npm run dev"

# Ambos en tmux/screen
alias sim-start="tmux new-session -d -s sim 'cd ~/simulador-geopolitico/backend && source venv/bin/activate && uvicorn api:app --reload' \; split-window -h 'cd ~/simulador-geopolitico/frontend && npm run dev' \; attach"
```

### Scripts NPM Personalizados (añadir a frontend/package.json)

```json
{
  "scripts": {
    "dev": "vite",
    "dev:open": "vite --open",
    "dev:host": "vite --host",
    "build": "vite build",
    "preview": "vite preview",
    "clean": "rm -rf node_modules dist .vite",
    "reinstall": "npm run clean && npm install"
  }
}
```

---

**¿Necesitas más comandos? Pregunta en los issues del repositorio!** 🚀
