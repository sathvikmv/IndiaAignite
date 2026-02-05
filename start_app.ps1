$ErrorActionPreference = "Stop"

Write-Host "Starting Lite Mode..." -ForegroundColor Green

# Install only if needed (fast)
pip install fastapi uvicorn

Write-Host "Starting Server..." -ForegroundColor Green
python -m uvicorn backend.main:app --port 8000 --reload
