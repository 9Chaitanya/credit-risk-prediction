from fastapi import FastAPI, HTTPException #lets you return structured HTTP errors
from pydantic import RootModel #declares & validate request bOdies
from typing import Dict
import joblib
from src.utils import preprocess_input

# create instance
app = FastAPI(text="Credit Risk API")

FEATURE_ORDER = [
    "LIMIT_BAL","SEX","EDUCATION","MARRIAGE","AGE",
    "PAY_0","PAY_2","PAY_3","PAY_4","PAY_5","PAY_6",
    "BILL_AMT1","BILL_AMT2","BILL_AMT3","BILL_AMT4","BILL_AMT5","BILL_AMT6",
    "PAY_AMT1","PAY_AMT2","PAY_AMT3","PAY_AMT4","PAY_AMT5","PAY_AMT6"
]

# load model
model = joblib.load("models/rf_model.pkl")
scaler = joblib.load("models/scaler.pkl")

# Define Input Schema
class InputData(RootModel[Dict[str, float]]):
    pass

@app.get("/")
def read_root():
    return{"status": "ok", "message": "Credit Risk Scoring API"}

@app.post("/predict")
def predict(data: InputData):
    try:
        input_dict = data.root
        X = preprocess_input(input_dict, FEATURE_ORDER)

        X_scaled = scaler.transform(X)

        prob = model.predict_proba(X_scaled)[:, 1][0]

        label = int(model.predict(X_scaled)[0])
        return {"Success": True, "Prediction": label, "Probability": prob}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    