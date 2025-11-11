# 🏦 Credit Risk Scoring with Explainable AI (XAI)

### 📘 Overview
This project predicts credit default risk using Logistic Regression, Random Forest, and XGBoost, and provides model explainability using SHAP.

### 📁 Structure
- `data/` – Raw and preprocessed datasets
- `notebooks/` – Data exploration, training, and explainability notebooks
- `src/` – Reusable scripts for training, prediction
- `app/` – FastAPI app exposing model inference 

### ⚙️ How to Run
```bash
pip install -r requirements.txt
python src/train.py
uvicorn app.api:app --reload
