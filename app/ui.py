import streamlit as st
import requests
import json

st.title("Credit-Risk-Prediction")

st.markdown("""
Enter your input data as JSON below.  
Example format:
```json
{
    "LIMIT_BAL": 20000,
    "SEX": 2,
    "EDUCATION": 2,
    "MARRIAGE": 1,
    "AGE": 24,
    "PAY_0": 2,
    "PAY_2": 2,
    "PAY_3": -1,
    "PAY_4": -1,
    "PAY_5": -2,
    "PAY_6": -2,
    "BILL_AMT1": 3913,
    "BILL_AMT2": 3102,
    "BILL_AMT3": 689,
    "BILL_AMT4": 0,
    "BILL_AMT5": 0,
    "BILL_AMT6": 0,
    "PAY_AMT1": 0,
    "PAY_AMT2": 689,
    "PAY_AMT3": 0,
    "PAY_AMT4": 0,
    "PAY_AMT5": 0,
    "PAY_AMT6": 0
}
""")

user_input = st.text_area("Paste JSON here", height=300)

if st.button("Predict"):
    try:
        data = json.loads(user_input)
        api_url = ""
        response = requests.post(api_url, json=data)

        if response.status_code == 200:
            result = response.json()
            st.success("Prediction succesful!")
            st.write(result)
        else:
            st.error(f"API Error {response.status_code}: {response.text}")
        
    except json.JSONDecodeError:
        st.error("Invalid Json Format. Please Check Your Input.")