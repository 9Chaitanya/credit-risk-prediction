import pandas as pd


def preprocess_input(input_dict, feature_order):
    df = pd.DataFrame([input_dict])
    df = df[feature_order]
    return df