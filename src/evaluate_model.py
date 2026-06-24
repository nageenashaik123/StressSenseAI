import joblib
import pandas as pd

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)

# ---------------------------------
# Load Model
# ---------------------------------

model = joblib.load(
    "models/random_forest_model.pkl"
)

# ---------------------------------
# Load Test Data
# ---------------------------------

X_test = joblib.load(
    "models/X_test.pkl"
)

y_test = joblib.load(
    "models/y_test.pkl"
)

print("Model Loaded")
print("Test Data Loaded")

# ---------------------------------
# Prediction
# ---------------------------------

y_pred = model.predict(X_test)

# ---------------------------------
# Diagnostics
# ---------------------------------

print("\nUnique Classes in y_test:")
print(sorted(y_test.unique()))

print("\nUnique Predicted Classes:")
print(sorted(set(y_pred)))

print("\nPrediction Counts:")
print(pd.Series(y_pred).value_counts())

# ---------------------------------
# Metrics
# ---------------------------------

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

# ---------------------------------
# Results
# ---------------------------------

print("\n==============================")
print("MODEL EVALUATION RESULTS")
print("==============================")

print(f"\nAccuracy : {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall   : {recall:.4f}")
print(f"F1 Score : {f1:.4f}")

# ---------------------------------
# Confusion Matrix
# ---------------------------------

cm = confusion_matrix(
    y_test,
    y_pred
)

print("\nConfusion Matrix")
print(cm)

# ---------------------------------
# Classification Report
# ---------------------------------

print("\nClassification Report")

print(
    classification_report(
        y_test,
        y_pred
    )
)

# ---------------------------------
# Per-Class Recall
# ---------------------------------

report = classification_report(
    y_test,
    y_pred,
    output_dict=True
)

print("\nPer-Class Recall")

for cls in ["0", "1", "2"]:
    print(
        f"Class {cls}: "
        f"{report[cls]['recall']*100:.2f}%"
    )