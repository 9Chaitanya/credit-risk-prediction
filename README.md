# 🏦 Credit Risk Scoring

### 📘 Overview
This project predicts credit default risk using Random Forest and Deployment of FastAPI backend & Streamlit UI on Render. Aim was to make end-to-end ml project.

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
