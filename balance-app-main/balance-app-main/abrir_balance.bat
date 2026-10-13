@echo off
title Servidor BalanceApp
echo =========================================
echo    Iniciando Servidor de BalanceApp
echo =========================================
echo.

cd /d "%~dp0"

echo [1/2] Liberando puerto 8000 e iniciando servidor...
:: Cerramos cualquier proceso previo para evitar conflictos
taskkill /F /IM python.exe /T >nul 2>&1

:: Iniciamos el servidor en el puerto 8000
start "Servidor BalanceApp" /b python -m http.server 8000 --directory balance-app

echo [2/2] Abriendo el navegador...
:: Esperamos un momento a que el servidor levante
timeout /t 2 /nobreak >nul

start http://127.0.0.1:8000

echo.
echo =========================================
echo ¡LISTO! La aplicacion ya deberia estar abierta.
echo.
echo Si no ves tus datos:
echo 1. Verifica que no haya errores en la consola (F12).
echo 2. Asegurate de que el servidor sigue corriendo aqui debajo.
echo =========================================
echo.
echo No cierres esta ventana mientras uses la app.
echo.
pause
