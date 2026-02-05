# 🔮 Fatality Risk & Cause-Shift Predictor
### AI-Based System for Mortality Trend Analysis

---

## 📖 Project Overview
The **Fatality Risk & Cause-Shift Predictor** is an AI-driven system designed to analyze and predict mortality trends across India. Using historical data patterns of **Accidental Deaths** and **Natural Causes**, the system identifies high-risk regions and forecasts future shifts in dominant causes of death.

Unlike traditional dashboards that only *show* past data, this project **predicts** the future, providing actionable intelligence for disaster management and policy planning.

### 🚀 Key Problem Solved
Government data is often static. This system turns static CSV data into dynamic **predictive intelligence**, answering questions like:
*   *"Will road accidents increase in Bangalore next year?"*
*   *"Is creating a high-risk zone for Natural causes in 2026?"*

---

## 🛠️ Technology Stack

### **Frontend (User Interface)**
*   **HTML5 & CSS3**: Built with a **Modern Dark Mode** aesthetic using CSS Variables and Flexbox/Grid layouts.
*   **JavaScript (Vanilla)**: logical handling for API communication and DOM manipulation.
*   **Chart.js**: Dynamic, interactive line charts to visualize predicted death trends over the next 5 years.
*   **Responsive Design**: Fully compatible with Desktops, Tablets, and Mobile devices.

### **Backend (API & Logic)**
*   **Python**: The core programming language.
*   **FastAPI**: A modern, high-performance web framework for building APIs. It serves the predictions to the frontend alongside the data options.
*   **Uvicorn**: A lightning-fast ASGI server to run the Python application.

### **AI & Data Science Components**
*   **Predictive Engine**: 
    *   Uses **Deterministic Simulation Algorithms** (in the current Lite version) to model trends based on historical baselines.
    *   *Full Version Capability*: Scikit-Learn (Random Forest Regressor) for precise numerical forecasting.
*   **Data Processing**: 
    *   **Pandas & NumPy**: Used for handling the dataset structure and numerical operations.
    *   **Synthetic Data Generation**: A custom script mimics the complexities of the official "Accidental Deaths & Suicides in India" dataset for training/testing.

---

## 🧩 Project Architecture

1.  **Input Layer**: User selects State, District, and Cause of Death.
2.  **Processing Layer**: 
    *   The Backend accepts these parameters.
    *   The **Risk Engine** calculates a "Preventable Death Potential Score".
    *   The **Trend Predictor** projects the death count for the target year.
3.  **Output Layer**: 
    *   JSON response containing **Predicted Count**, **Risk Level (High/Low)**, and **Trend Analysis**.
    *   Frontend renders this as a Risk Card and a Trend Graph.

---

## 📂 Folder Structure

*   `backend/`: Contains the FastAPI server (`main.py`) and ML logic (`train_model.py`).
*   `frontend/`: Contains the UI (`index.html`), Styles (`style.css`), and Logic (`script.js`).
*   `scripts/`: Utilities to generate synthetic training data (`generate_data.py`).
*   `data/`: Stores the CSV datasets.

---

## 🔮 Future Enhancements
*   **Real Data Integration**: Direct API connection to `data.gov.in`.
*   **Geospatial Mapping**: Heatmaps using Google Maps API or Leaflet.js.
*   **Report Generation**: Auto-generate PDF reports for government officials.
