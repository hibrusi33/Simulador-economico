@echo off
REM ============================================
REM Script de Instalacion Automatica - Windows
REM Simulador Geopolitico - Backend + Frontend
REM ============================================

echo.
echo ======================================================
echo   SIMULADOR GEOPOLITICO - INSTALACION AUTOMATICA
echo ======================================================
echo.

REM Verificar que estamos en el directorio correcto
if not exist "backend\" (
    echo [ERROR] No se encontro la carpeta 'backend'
    echo Asegurate de ejecutar este script desde la raiz del proyecto
    pause
    exit /b 1
)

if not exist "frontend\" (
    echo [ERROR] No se encontro la carpeta 'frontend'
    echo Asegurate de ejecutar este script desde la raiz del proyecto
    pause
    exit /b 1
)

REM ==================== BACKEND ====================
echo.
echo [1/2] CONFIGURANDO BACKEND (Python/FastAPI)
echo -------------------------------------------
echo.

cd backend

REM Verificar Python
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python 3 no esta instalado
    echo Descargalo en: https://www.python.org/downloads/
    pause
    exit /b 1
)

echo [OK] Python encontrado

REM Crear entorno virtual si no existe
if not exist "venv\" (
    echo [INFO] Creando entorno virtual...
    python -m venv venv
    echo [OK] Entorno virtual creado
) else (
    echo [OK] Entorno virtual ya existe
)

REM Activar entorno virtual
echo [INFO] Activando entorno virtual...
call venv\Scripts\activate.bat

REM Instalar dependencias
echo [INFO] Instalando dependencias de Python...
python -m pip install --upgrade pip --quiet
pip install -r requirements.txt --quiet
echo [OK] Dependencias de Python instaladas

REM Verificar archivo .env
if not exist ".env" (
    echo [WARN] Archivo .env no encontrado
    echo [INFO] Creando .env desde .env.example...
    copy .env.example .env
    echo.
    echo ============================================================
    echo   IMPORTANTE: Edita backend\.env y anade tu GEMINI_API_KEY
    echo   Obten tu API Key en: https://makersuite.google.com/app/apikey
    echo ============================================================
    echo.
) else (
    echo [OK] Archivo .env encontrado
)

cd ..

REM ==================== FRONTEND ====================
echo.
echo [2/2] CONFIGURANDO FRONTEND (React/Vite)
echo ---------------------------------------
echo.

cd frontend

REM Verificar Node.js
node --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Node.js no esta instalado
    echo Descargalo en: https://nodejs.org/
    pause
    exit /b 1
)

echo [OK] Node.js encontrado

REM Verificar npm
npm --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] npm no esta instalado
    pause
    exit /b 1
)

echo [OK] npm encontrado

REM Instalar dependencias
echo [INFO] Instalando dependencias de Node.js (esto puede tardar unos minutos)...
call npm install --silent
echo [OK] Dependencias de Node.js instaladas

cd ..

REM ==================== RESUMEN ====================
echo.
echo ======================================================
echo   INSTALACION COMPLETADA EXITOSAMENTE
echo ======================================================
echo.
echo PROXIMOS PASOS:
echo.
echo 1. Configura tu API Key de Gemini:
echo    Edita: backend\.env
echo    Anade: GEMINI_API_KEY=tu_clave_aqui
echo.
echo 2. Inicia el backend (Terminal 1):
echo    cd backend
echo    venv\Scripts\activate
echo    uvicorn api:app --reload --host 0.0.0.0 --port 8000
echo.
echo 3. Inicia el frontend (Terminal 2):
echo    cd frontend
echo    npm run dev
echo.
echo 4. Abre tu navegador en:
echo    http://localhost:5173
echo.
echo ======================================================
echo   Disfruta del Simulador Geopolitico!
echo ======================================================
echo.

pause
