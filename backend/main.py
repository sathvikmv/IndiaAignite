from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import random

app = FastAPI(title="Fatality Risk Predictor (Lite Mode)")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mock Data for Options
STATES = ["Karnataka", "Maharashtra", "Delhi", "Kerala", "Tamil Nadu"]
DISTRICTS = {
    "Karnataka": ["Bangalore", "Mysore", "Hubli"],
    "Maharashtra": ["Mumbai", "Pune", "Nagpur"],
    "Delhi": ["New Delhi", "North Delhi"],
    "Kerala": ["Kochi", "Thiruvananthapuram"],
    "Tamil Nadu": ["Chennai", "Coimbatore"]
}
TYPES = ["Accidental", "Natural"]
CAUSES = ["Road Accident", "Heart Attack", "Fire", "Stroke", "Drowning"]

class PredictionRequest(BaseModel):
    state: str
    district: str
    year: int
    death_type: str
    cause: str

@app.get("/")
def read_root():
    return {"message": "Fatality Risk Predictor API is running (Lite Mode)"}

@app.get("/options")
def get_options():
    return {
        "states": STATES,
        "districts": [d for sublist in DISTRICTS.values() for d in sublist], # Flattened for simplicity
        "types": TYPES,
        "causes": CAUSES
    }

@app.post("/predict")
def predict(request: PredictionRequest):
    # Simulation Logic (No Heavy ML needed for Demo)
    # We use hashing to make the "randomness" deterministic for the same inputs
    seed =  hash(request.state) + hash(request.district) + hash(request.cause) + request.year
    random.seed(seed)
    
    base_deaths = random.randint(50, 500)
    
    # Simple trend logic
    if request.year > 2025:
        base_deaths = int(base_deaths * 1.1)
    
    risk_level = "High" if base_deaths > 300 else "Low"
    
    return {
        "predicted_deaths": base_deaths,
        "risk_level": risk_level,
        "region": f"{request.district}, {request.state}",
        "cause_analysis": f"Projected trend for {request.cause} in {request.year}"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
