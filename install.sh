#!/bin/bash

# ============================================
# Script de Instalación Automática
# Simulador Geopolítico - Backend + Frontend
# ============================================

echo "🌍 SIMULADOR GEOPOLÍTICO - INSTALACIÓN AUTOMÁTICA"
echo "=================================================="
echo ""

# Colores para output
GREEN='\033[0;32m'
CYAN='\033[0;36m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Función para imprimir en verde
print_success() {
    echo -e "${GREEN}✓ $1${NC}"
}

# Función para imprimir en cyan
print_info() {
    echo -e "${CYAN}ℹ $1${NC}"
}

# Función para imprimir en rojo
print_error() {
    echo -e "${RED}✗ $1${NC}"
}

# Función para imprimir en amarillo
print_warning() {
    echo -e "${YELLOW}⚠ $1${NC}"
}

# Verificar que estamos en el directorio correcto
if [ ! -d "backend" ] || [ ! -d "frontend" ]; then
    print_error "Error: No se encontraron las carpetas 'backend' y 'frontend'"
    print_info "Asegúrate de ejecutar este script desde la raíz del proyecto"
    exit 1
fi

# ==================== BACKEND ====================
echo ""
print_info "1️⃣ CONFIGURANDO BACKEND (Python/FastAPI)"
echo "-------------------------------------------"

cd backend

# Verificar Python
if ! command -v python3 &> /dev/null; then
    print_error "Python 3 no está instalado"
    exit 1
fi

PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
print_success "Python $PYTHON_VERSION encontrado"

# Crear entorno virtual si no existe
if [ ! -d "venv" ]; then
    print_info "Creando entorno virtual..."
    python3 -m venv venv
    print_success "Entorno virtual creado"
else
    print_success "Entorno virtual ya existe"
fi

# Activar entorno virtual
print_info "Activando entorno virtual..."
source venv/bin/activate

# Instalar dependencias
print_info "Instalando dependencias de Python..."
pip install -q --upgrade pip
pip install -q -r requirements.txt
print_success "Dependencias de Python instaladas"

# Verificar archivo .env
if [ ! -f ".env" ]; then
    print_warning "Archivo .env no encontrado"
    print_info "Creando .env desde .env.example..."
    cp .env.example .env
    print_warning "IMPORTANTE: Edita backend/.env y añade tu GEMINI_API_KEY"
    print_info "Obtén tu API Key en: https://makersuite.google.com/app/apikey"
else
    print_success "Archivo .env encontrado"
fi

cd ..

# ==================== FRONTEND ====================
echo ""
print_info "2️⃣ CONFIGURANDO FRONTEND (React/Vite)"
echo "---------------------------------------"

cd frontend

# Verificar Node.js
if ! command -v node &> /dev/null; then
    print_error "Node.js no está instalado"
    exit 1
fi

NODE_VERSION=$(node --version)
print_success "Node.js $NODE_VERSION encontrado"

# Verificar npm
if ! command -v npm &> /dev/null; then
    print_error "npm no está instalado"
    exit 1
fi

NPM_VERSION=$(npm --version)
print_success "npm $NPM_VERSION encontrado"

# Instalar dependencias
print_info "Instalando dependencias de Node.js (esto puede tardar unos minutos)..."
npm install --silent
print_success "Dependencias de Node.js instaladas"

cd ..

# ==================== RESUMEN ====================
echo ""
echo "=================================================="
echo -e "${GREEN}✓ INSTALACIÓN COMPLETADA EXITOSAMENTE${NC}"
echo "=================================================="
echo ""
echo "📝 PRÓXIMOS PASOS:"
echo ""
echo "1️⃣ Configura tu API Key de Gemini:"
echo "   ${CYAN}nano backend/.env${NC}"
echo "   Añade: GEMINI_API_KEY=tu_clave_aqui"
echo ""
echo "2️⃣ Inicia el backend (Terminal 1):"
echo "   ${CYAN}cd backend${NC}"
echo "   ${CYAN}source venv/bin/activate${NC}"
echo "   ${CYAN}uvicorn api:app --reload --host 0.0.0.0 --port 8000${NC}"
echo ""
echo "3️⃣ Inicia el frontend (Terminal 2):"
echo "   ${CYAN}cd frontend${NC}"
echo "   ${CYAN}npm run dev${NC}"
echo ""
echo "4️⃣ Abre tu navegador en:"
echo "   ${GREEN}http://localhost:5173${NC}"
echo ""
echo "=================================================="
echo "🌍 ¡Disfruta del Simulador Geopolítico!"
echo "=================================================="
