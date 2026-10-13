@echo off
echo =========================================
echo Importador de Resumenes Visa y Mastercard
echo =========================================
echo.
echo Extrayendo gastos de los PDFs...
python importar_pdfs.py
echo.
echo Proceso finalizado. El archivo "nuevos_gastos.json" esta listo.
pause
