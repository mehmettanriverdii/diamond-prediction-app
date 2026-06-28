import joblib
import pandas as pd
from pathlib import Path

MODEL_PATH = Path(__file__).parent.parent / "artifacts" / "diamond_model.pkl"

def load_model():
    if not MODEL_PATH.exists():
        raise FileNotFoundError(f"Model not found: {MODEL_PATH}")

    return joblib.load(MODEL_PATH)

model = load_model()

def predict(features: dict) -> float:
    df = pd.DataFrame([features])
    prediction = model.predict(df)
    return round(float(prediction[0]), 2)
