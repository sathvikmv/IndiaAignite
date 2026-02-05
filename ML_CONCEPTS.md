# 🧠 AI & Machine Learning Concepts

This project implements advanced Machine Learning techniques to analyze mortality data. Here are the core concepts used:

## 1. Ensemble Learning (Random Forest)
We utilize **Random Forest**, a powerful ensemble learning method that constructs a multitude of "Decision Trees" at training time.
*   **Why it's used**: It is highly accurate and robust against overfitting compared to single decision trees.
*   **Implementation**: Used in `backend/train_model.py` for both counting deaths and classifying risk.

## 2. Supervised Learning Tasks
The system performs two distinct supervised learning tasks:
*   **Regression Analysis**: Uses `RandomForestRegressor` to predict a continuous numerical value — the specific **Number of Deaths**.
*   **Classification**: Uses `RandomForestClassifier` to categorize regions into discrete labels — **High Risk** vs. **Low Risk**.

## 3. Label Encoding (Feature Transformation)
Machine Learning models require numerical input. We used **Label Encoding** to transform categorical text data into machine-readable integers:
*   *State Names* (e.g., "Karnataka" ➝ `0`, "Delhi" ➝ `1`)
*   *Cause Categories* (e.g., "Accidental" ➝ `0`, "Natural" ➝ `1`)

## 4. Statistical Pattern Injection
To train the model effectively on synthetic data, we embedded realistic statistical patterns:
*   **Linear Trend Injection**: Simulating year-over-year increases for specific causes like "Road Accidents".
*   **Gaussian Noise (Normal Distribution)**: Adding random variation to the data to make the model robust against real-world unpredictability.
*   **Anomaly Simulation**: Injecting specific "spikes" (like epidemics) to test the model's ability to handle outlier events.

## 5. Threshold-Based Risk Profiling
We apply statistical thresholding (using data quantiles) to determine the frontier between "Normal" and "High" risk, allowing the AI to dynamically adapt its warnings based on the data distribution rather than fixed numbers.
