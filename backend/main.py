from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import random
import os
import joblib
import pandas as pd

app = FastAPI(title="Fatality Risk Predictor (Complete Mode)")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_DIR = os.path.join(BASE_DIR, "models")

# Load Models & Encoders (Global)
models = {}
try:
    if os.path.exists(MODEL_DIR):
        print("Loading ML models...")
        models['count'] = joblib.load(os.path.join(MODEL_DIR, "model_count.pkl"))
        models['risk'] = joblib.load(os.path.join(MODEL_DIR, "model_risk.pkl"))
        models['le_state'] = joblib.load(os.path.join(MODEL_DIR, "le_state.pkl"))
        models['le_district'] = joblib.load(os.path.join(MODEL_DIR, "le_district.pkl"))
        models['le_type'] = joblib.load(os.path.join(MODEL_DIR, "le_type.pkl"))
        models['le_cause'] = joblib.load(os.path.join(MODEL_DIR, "le_cause.pkl"))
        print("Real ML models loaded successfully.")
    else:
        print("Models directory not found. Running in Simulation Mode.")
except Exception as e:
    print(f"Error loading models: {e}. Falling back to simulation.")

class PredictionRequest(BaseModel):
    state: str
    district: str
    year: int
    death_type: str
    cause: str

@app.get("/")
def read_root():
    mode = "Complete (ML)" if 'count' in models else "Lite (Simulation)"
    return {"message": f"Fatality Risk Predictor API is running in {mode} Mode"}

@app.get("/options")
def get_options():
    # If we have encoders, use their classes for options
    if 'le_state' in models:
        return {
            "states": models['le_state'].classes_.tolist(),
            "districts": models['le_district'].classes_.tolist(),
            "types": models['le_type'].classes_.tolist(),
            "causes": models['le_cause'].classes_.tolist()
        }
    
    # Fallback to hardcoded demo options
    return {
        "states": ["Karnataka", "Maharashtra", "Delhi", "Kerala", "Tamil Nadu"],
        "districts": ["Bangalore", "Mumbai", "New Delhi", "Kochi", "Chennai"],
        "types": ["Accidental", "Natural"],
        "causes": ["Road Accident", "Heart Attack", "Fire", "Stroke", "Drowning"]
    }

@app.get("/analytics/{state}")
def get_state_analytics(state: str):
    # This would normally query the actual dataset
    # For now, we simulate state-wide comparison
    districts = ["Bangalore", "Mysore", "Hubli", "Mangalore", "Belgaum"] if state == "Karnataka" else ["Mumbai", "Pune", "Nagpur", "Nashik", "Aurangabad"]
    
    analysis = []
    for d in districts:
        risk = "High" if random.random() > 0.6 else "Low"
        analysis.append({"district": d, "risk": risk, "score": random.randint(100, 600)})
    
    return {"state": state, "data": analysis}

@app.post("/predict")
def predict(request: PredictionRequest):
    result = {"mode": "Simulated engine (fallback)"}
    
    if 'count' in models:
        try:
            # Prepare Features
            state_enc = models['le_state'].transform([request.state])[0]
            dist_enc = models['le_district'].transform([request.district])[0]
            type_enc = models['le_type'].transform([request.death_type])[0]
            cause_enc = models['le_cause'].transform([request.cause])[0]
            
            X = pd.DataFrame([[state_enc, dist_enc, request.year, type_enc, cause_enc]], 
                             columns=['State_Enc', 'District_Enc', 'Year', 'Type_Enc', 'Cause_Enc'])
            
            deaths = int(models['count'].predict(X)[0])
            risk_idx = int(models['risk'].predict(X)[0])
            risk_level = "High" if risk_idx == 1 else "Low"
            
            result = {
                "predicted_deaths": deaths,
                "risk_level": risk_level,
                "region": f"{request.district}, {request.state}",
                "mode": "ML Engine"
            }
        except Exception:
            pass

    if "predicted_deaths" not in result:
        # Simulation Logic (Fallback)
        seed = hash(request.state) + hash(request.district) + hash(request.cause) + request.year
        random.seed(seed)
        deaths = random.randint(50, 500)
        if request.year > 2025: deaths = int(deaths * 1.1)
        risk_level = "High" if deaths > 300 else "Low"
        result = {
            "predicted_deaths": deaths,
            "risk_level": risk_level,
            "region": f"{request.district}, {request.state}",
            "mode": "Simulated Engine"
        }

    # --- Extra Features Logic ---
    
    # 1. AI Insights
    insights = []
    if result["risk_level"] == "High":
        insights.append(f"Critical concern: Potential {result['predicted_deaths']} fatalities predicted.")
        insights.append(f"Recommended Action: Targeted safety intervention for {request.cause} in {request.state}.")
    else:
        insights.append(f"Trend Analysis: Stable fatality rate expected for {request.cause}.")
        insights.append("Maintain existing public health surveillance.")

    # 2. Historical Comparison (Simulated)
    prev_year = result["predicted_deaths"] * random.uniform(0.8, 1.2)
    change = ((result["predicted_deaths"] - prev_year) / prev_year) * 100
    
    # 3. Cause Distribution for the state
    cause_dist = [
        {"name": "Road Accident", "value": random.randint(20, 40)},
        {"name": "Natural", "value": random.randint(30, 50)},
        {"name": "Other", "value": random.randint(10, 20)}
    ]

    result.update({
        "ai_insights": insights,
        "historical_comparison": {
            "percentage": round(change, 1),
            "trend": "up" if change > 0 else "down"
        },
        "cause_distribution": cause_dist
    })
    
    return result

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
