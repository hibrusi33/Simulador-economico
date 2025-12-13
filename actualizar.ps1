# Script de actualización automática
Write-Host "🔄 Actualizando Simulador Geopolítico..." -ForegroundColor Cyan

# Detener cualquier proceso de Node
Write-Host "⏹️ Deteniendo procesos..."
Get-Process node -ErrorAction SilentlyContinue | Stop-Process -Force

# Ir a la raíz del proyecto
Set-Location $PSScriptRoot

# Descartar TODOS los cambios locales
Write-Host "🗑️ Limpiando cambios locales..."
git reset --hard HEAD
git clean -fd

# Hacer pull
Write-Host "📥 Descargando última versión..."
git pull origin claude/review-repository-01Gc8rQArkZNSjMrKBgbQm7Z

# Verificar versión
$lastCommit = git log --oneline -1
Write-Host "✅ Versión actual: $lastCommit" -ForegroundColor Green

# Actualizar frontend
Write-Host "`n📦 Actualizando frontend..."
Set-Location frontend

# Eliminar caché
Write-Host "🧹 Limpiando caché..."
Remove-Item -Recurse -Force node_modules -ErrorAction SilentlyContinue
Remove-Item -Force package-lock.json -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force node_modules\.vite -ErrorAction SilentlyContinue

# Reinstalar
Write-Host "📦 Instalando dependencias..."
npm install

Write-Host "`n✅ ACTUALIZACIÓN COMPLETADA" -ForegroundColor Green
Write-Host "`nAhora ejecuta:" -ForegroundColor Yellow
Write-Host "  Terminal 1 (Backend):  cd backend && uvicorn api:app --reload --host 0.0.0.0 --port 8000"
Write-Host "  Terminal 2 (Frontend): cd frontend && npm run dev"
Write-Host "`nLuego abre: http://localhost:5173 (presiona Ctrl+Shift+R para limpiar caché del navegador)"
