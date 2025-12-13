#!/usr/bin/env pwsh
# Script para actualizar y reconstruir completamente el frontend

Write-Host "🔄 Actualizando repositorio..." -ForegroundColor Cyan

# Ir a la raíz del proyecto
Set-Location $PSScriptRoot

# Hacer pull de los cambios
git pull origin claude/review-repository-01Gc8rQArkZNSjMrKBgbQm7Z

Write-Host "🗑️  Limpiando archivos de construcción..." -ForegroundColor Yellow

# Ir a frontend
Set-Location frontend

# Eliminar node_modules y archivos de construcción
if (Test-Path "node_modules") {
    Remove-Item -Recurse -Force node_modules
    Write-Host "✅ node_modules eliminado" -ForegroundColor Green
}

if (Test-Path "package-lock.json") {
    Remove-Item -Force package-lock.json
    Write-Host "✅ package-lock.json eliminado" -ForegroundColor Green
}

if (Test-Path "dist") {
    Remove-Item -Recurse -Force dist
    Write-Host "✅ dist eliminado" -ForegroundColor Green
}

if (Test-Path ".vite") {
    Remove-Item -Recurse -Force .vite
    Write-Host "✅ .vite eliminado" -ForegroundColor Green
}

Write-Host "`n📦 Instalando dependencias..." -ForegroundColor Cyan
npm install

Write-Host "`n🚀 Iniciando servidor de desarrollo..." -ForegroundColor Green
Write-Host "⚠️  IMPORTANTE: Cuando abras http://localhost:5173 presiona Ctrl+Shift+R para limpiar caché" -ForegroundColor Yellow
Write-Host ""

npm run dev
