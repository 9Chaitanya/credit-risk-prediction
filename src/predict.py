import joblib
import numpy as np
from src.utils import preprocess_input

_model = joblib.load("models/rf_model.pkl")
_scaler = joblib.load("models/scaler.pkl")

FEATURE_ORDER = [
    "LIMIT_BAL","SEX","EDUCATION","MARRIAGE","AGE",
    "PAY_0","PAY_2","PAY_3","PAY_4","PAY_5","PAY_6",
    "BILL_AMT1","BILL_AMT2","BILL_AMT3","BILL_AMT4","BILL_AMT5","BILL_AMT6",
    "PAY_AMT1","PAY_AMT2","PAY_AMT3","PAY_AMT4","PAY_AMT5","PAY_AMT6"
]

def predict(input_dict):
    X = preprocess_input(input_dict, FEATURE_ORDER)
    X_scaled = _scaler.transform(X)

    prob = _model.predict_proba(X_scaled)[:, 1][0]

    label = int(_model.predict(X_scaled)[0])

    return {"label": label, "probability": float(prob)}