@echo off
echo ===================================================
echo   FATALITY RISK PREDICTOR - INSTANT LAUNCHER
echo ===================================================

echo [1/3] Installing lightweight dependencies...
pip install fastapi uvicorn

echo [2/3] Opening Frontend...
start "" "frontend\index.html"

echo [3/3] Starting Local Server...
echo ---------------------------------------------------
echo DO NOT CLOSE THIS WINDOW while using the app.
echo App is running. Go to your browser!
echo ---------------------------------------------------
python -m uvicorn backend.main:app --port 8000 --reload

pause
