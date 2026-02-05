import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib
import os

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "../data/dataset.csv")
MODEL_DIR = os.path.join(BASE_DIR, "models")

os.makedirs(MODEL_DIR, exist_ok=True)

def train():
    print("Loading data...")
    if not os.path.exists(DATA_PATH):
        print("Data file not found. Run scripts/generate_data.py first.")
        return

    df = pd.read_csv(DATA_PATH)
    
    # Encoders
    le_state = LabelEncoder()
    le_district = LabelEncoder()
    le_type = LabelEncoder()
    le_cause = LabelEncoder()
    
    df['State_Enc'] = le_state.fit_transform(df['State'])
    df['District_Enc'] = le_district.fit_transform(df['District'])
    df['Type_Enc'] = le_type.fit_transform(df['Type'])
    df['Cause_Enc'] = le_cause.fit_transform(df['Cause'])
    
    # Feature Engineering
    # Predict Death Count
    X = df[['State_Enc', 'District_Enc', 'Year', 'Type_Enc', 'Cause_Enc']]
    y = df['Deaths']
    
    print("Training Count Predictor...")
    model_count = RandomForestRegressor(n_estimators=100, random_state=42)
    model_count.fit(X, y)
    
    # Risk Classification (High/Low) - Simple threshold logic for demo
    # We'll use clustering logic or just a classifier on a derived target
    # Let's say > 75th percentile is "High Risk"
    threshold = df['Deaths'].quantile(0.75)
    df['Risk_Level'] = (df['Deaths'] > threshold).astype(int)
    
    print("Training Risk Classifier...")
    model_risk = RandomForestClassifier(n_estimators=100, random_state=42)
    model_risk.fit(X, df['Risk_Level'])

    # Save artifacts
    print("Saving models...")
    joblib.dump(model_count, os.path.join(MODEL_DIR, "model_count.pkl"))
    joblib.dump(model_risk, os.path.join(MODEL_DIR, "model_risk.pkl"))
    
    joblib.dump(le_state, os.path.join(MODEL_DIR, "le_state.pkl"))
    joblib.dump(le_district, os.path.join(MODEL_DIR, "le_district.pkl"))
    joblib.dump(le_type, os.path.join(MODEL_DIR, "le_type.pkl"))
    joblib.dump(le_cause, os.path.join(MODEL_DIR, "le_cause.pkl"))
    
    print("Training complete.")

if __name__ == "__main__":
    train()
