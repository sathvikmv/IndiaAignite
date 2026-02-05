# 🏗️ System Architecture Diagram

Below is the architectural flow of the Fatality Risk Predictor system.

## 🔷 Interactive Flow Diagram (Mermaid)

```mermaid
graph TD
    %% Nodes
    User([👤 User])
    Browser[🌐 Frontend UI\n(HTML/CSS/JS)]
    API[⚙️ Backend API\n(FastAPI)]
    
    subgraph "AI Inference Engine"
        Encoder[🔣 Label Encoder]
        Regressor[📈 Random Forest Regressor]
        Classifier[⚠️ Random Forest Classifier]
    end
    
    subgraph "Data Storage"
        CSV[(📊 Dataset.csv)]
        Models[[📦 Saved Models .pkl]]
    end

    %% Connections
    User -->|Selects Region| Browser
    Browser -->|POST /predict| API
    
    API -->|Raw Input| Encoder
    Encoder -->|Encoded Features| Regressor
    Encoder -->|Encoded Features| Classifier
    
    Models -.->|Load Weights| Regressor
    Models -.->|Load Weights| Classifier
    
    Regressor -->|Predicted Count| API
    Classifier -->|Risk Level| API
    
    API -->|JSON Response| Browser
    Browser -->|Render Charts| User
```

## 📐 Data Flow Explanation

1.  **Input Layer**: The user selects the `State`, `District`, and `Cause` in the browser.
2.  **Transmission**: The request is sent asynchronously via `fetch()` to the **FastAPI** server running on `localhost:8000`.
3.  **Processing**:
    *   The backend loads the pre-trained `.pkl` models (saved using `joblib`).
    *   Inputs are converted to numbers (Label Encoding).
4.  **Prediction**:
    *   **Model A** predicts the *number* of deaths.
    *   **Model B** predicts the *category* of risk (High/Low).
5.  **Output**: The results are packed into a JSON object and visualized as a chart in the UI.
