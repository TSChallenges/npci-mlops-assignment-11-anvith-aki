import joblib
import numpy as np
import pandas as pd


geography_mapping = {'France': 0, 'Spain': 1, 'Germany': 2}
gender_mapping = {'Female': 0, 'Male': 1}


# Load model
try:
    rf_model = joblib.load("trained_model/rf_model_customer_churn_pred.pkl")
    if __name__ == "__main__":
        print("Model loaded successfully from path: trained_model/rf_model_customer_churn_pred.pkl")
except Exception as e:
    print("Failed to load model.", e)


# Inference
sample_input = {
    'CreditScore': 600,
    'Geography': geography_mapping['France'],
    'Gender': gender_mapping['Female'],
    'Age': 40,
    'Tenure': 3,
    'Balance': 60000.0,
    'NumOfProducts': 2,
    'HasCrCard': 1,
    'IsActiveMember': 1,
    'EstimatedSalary': 50000.0
}

sample_input_df = pd.DataFrame(sample_input, index=[0])


def make_prediction(sample_input_df):
    prediction = rf_model.predict(sample_input_df)
    label = "Likely to Exit" if prediction[0] == 1 else "Less likely to Exit"
    return {"prediction": label}


if __name__ == "__main__":
    pred = make_prediction(sample_input_df)
    print(pred)
