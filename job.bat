@echo off
REM 1) Cambia al directorio de tu instalación de conda
CALL "C:\Users\chris\anaconda3\Scripts\activate.bat" scrappers

REM 2) Opcional: ve al directorio donde está tu script
CD /D "F:\kick\bot_inspection_monitor_57\local"

REM 3) Ejecuta tu script Python
python bot.py