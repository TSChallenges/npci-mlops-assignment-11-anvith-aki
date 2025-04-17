
import pandas as pd
from predict import make_prediction, geography_mapping, gender_mapping

from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse
from pydantic import BaseModel


app = FastAPI()

# Swagger Documentation  avaiable on this endpoint ->   /docs 

@app.get("/")
def index():
    """Basic HTML response."""
    body = (
        "<html>"
        "<body style='padding: 10px;'>"
        "<h1>Welcome to the API</h1>"
        "<div>"
        "Check the Swagger UI: <a href='/docs'>here</a>"
        "</div>"
        "</body>"
        "</html>"
    )

    return HTMLResponse(content=body)


# Prediction endpoint

class Feature(BaseModel):
    CreditScore: float
    Geography: str
    Gender: str
    Age: int
    Tenure: float
    Balance: float
    NumOfProducts: int
    HasCrCard: int
    IsActiveMember: int
    EstimatedSalary: float


def predict_customer_churn(CreditScore, Geography, Gender, Age, Tenure, Balance, NumOfProducts, HasCrCard, IsActiveMember, EstimatedSalary):
    sample_input = {
            'CreditScore': CreditScore,
            'Geography': geography_mapping[Geography],
            'Gender': gender_mapping[Gender],
            'Age': Age,
            'Tenure': Tenure,
            'Balance': Balance,
            'NumOfProducts': NumOfProducts,
            'HasCrCard': HasCrCard,
            'IsActiveMember': IsActiveMember,
            'EstimatedSalary': EstimatedSalary
            }

    sample_input_df = pd.DataFrame(sample_input, index=[0])
    label = make_prediction(sample_input_df)

    return label['prediction']


example_input = {
            "CreditScore": 600,
            "Geography": 'France',
            "Gender": "Female",
            "Age": 40,
            "Tenure": 3,
            "Balance": 60000.0,
            "NumOfProducts": 2,
            "HasCrCard": 1,
            "IsActiveMember": 1,
            "EstimatedSalary": 50000.0
        }


@app.post("/predict")
def func5(f: Feature = Body(..., example=example_input)):
    label = predict_customer_churn(
        f.CreditScore,
        f.Geography,
        f.Gender,
        f.Age,
        f.Tenure,
        f.Balance,
        f.NumOfProducts,
        f.HasCrCard,
        f.IsActiveMember,
        f.EstimatedSalary,
        )
    return {"prediction": label}


# Webserver -> Uvicorn
import uvicorn
uvicorn.run(app, host="0.0.0.0", port=8080)
