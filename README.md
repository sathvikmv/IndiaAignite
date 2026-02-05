# Fatality Risk & Cause-Shift Predictor

⚠️ **Original AI Project using IndiaAI Datasets**

This project predicts fatality hotspots and future trends in accidental and natural deaths in India.

## Setup Instructions

### 1. Install Dependencies
```bash
cd backend
pip install -r requirements.txt
```

### 2. Generate Data & Train Models
```bash
# From the root directory
python scripts/generate_data.py
python backend/train_model.py
```

### 3. Run the Backend API
```bash
# From the root directory
uvicorn backend.main:app --reload
```

### 4. Run the Frontend
Simply open `frontend/index.html` in your browser.
