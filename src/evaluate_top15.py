import joblib

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)

# -----------------------------
# Load Model
# -----------------------------

model = joblib.load(
    "models/top15_random_forest.pkl"
)

X_test = joblib.load(
    "models/X_test.pkl"
)

y_test = joblib.load(
    "models/y_test.pkl"
)

# -----------------------------
# Prediction
# -----------------------------

y_pred = model.predict(X_test)

# -----------------------------
# Metrics
# -----------------------------

accuracy = accuracy_score(
    y_test,
    y_pred
)

precision = precision_score(
    y_test,
    y_pred,
    average="weighted"
)

recall = recall_score(
    y_test,
    y_pred,
    average="weighted"
)

f1 = f1_score(
    y_test,
    y_pred,
    average="weighted"
)

print("\nAccuracy")
print(accuracy)

print("\nPrecision")
print(precision)

print("\nRecall")
print(recall)

print("\nF1 Score")
print(f1)

print("\nConfusion Matrix")
print(
    confusion_matrix(
        y_test,
        y_pred
    )
)

print("\nClassification Report")
print(
    classification_report(
        y_test,
        y_pred
    )
)