import os
import numpy as np
import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score


# Load dataset as pandas dataframe
df = pd.read_csv("dataset/churn_modeling.csv")


# Define target variable and features
X = df[["CreditScore", "Geography", "Gender", "Age", "Tenure", "Balance", "NumOfProducts", "HasCrCard", "IsActiveMember", "EstimatedSalary"]].copy()
y = df[["Exited"]]


# Handling category labels present in `Geography` and `Gender` columns
# Get the distinct categories present in each categorical column
# print(X['Geography'].unique())
# print(X['Gender'].unique())

# Create dictionaries to map categorical values to numberic labels. OR Use LabelEncoder
geography_mapping = {'France': 0, 'Spain': 1, 'Germany': 2}
gender_mapping = {'Female': 0, 'Male': 1}

# Map categorical values to numbers using respective dictionaries
X['Geography'] = X['Geography'].map(geography_mapping)
X['Gender'] = X['Gender'].map(gender_mapping)

# Split data into training (80%) and test (20%) sets
# Use random_state and stratify parameters
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=3, stratify=y)

