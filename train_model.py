import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score

from data_preprocessing import X_train, y_train, X_test, y_test


def evaluate_model(y_pred, y_test):
    acc = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)

    print(f"Accuracy: {round(acc, 3)}")
    print(f"F1 Score: {round(f1, 3)}")
    print(f"Precision: {round(precision, 3)}")
    print(f"Recall: {round(recall, 3)}")


# Random Forest
n_estimators = 150
max_depth = 9
max_features = 6
random_state = 42

rf_model = RandomForestClassifier(n_estimators = n_estimators,
                                  max_depth = max_depth,
                                  max_features = max_features,
                                  random_state = random_state)

rf_model.fit(X_train, y_train.values.ravel())

print("Model trained successfully!")

y_pred = rf_model.predict(X_test)

evaluate_model(y_test, y_pred)

# Save model
try:
    joblib.dump(rf_model, "trained_model/rf_model_customer_churn_pred.pkl")
    print("Model saved successfully at path: trained_model/rf_model_customer_churn_pred.pkl")
except Exception as e:
    print("Failed to save model.", e)

