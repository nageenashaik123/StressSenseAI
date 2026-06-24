import pandas as pd

from sklearn.model_selection import (
    StratifiedKFold,
    cross_val_score
)

from sklearn.ensemble import RandomForestClassifier

# -----------------------------
# Load Dataset
# -----------------------------

df = pd.read_csv(
    "data/feature_engineered_data.csv"
)

X = df.drop(
    columns=["stress_level"]
)

y = df["stress_level"]

# -----------------------------
# Model
# -----------------------------

model = RandomForestClassifier(
    n_estimators=500,
    max_depth=10,
    min_samples_split=5,
    min_samples_leaf=2,
    random_state=42,
    n_jobs=-1
)

# -----------------------------
# 5 Fold CV
# -----------------------------

cv = StratifiedKFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)

scores = cross_val_score(
    model,
    X,
    y,
    cv=cv,
    scoring="accuracy"
)

print("\nFold Accuracies")
print(scores)

print("\nMean Accuracy")
print(scores.mean())

print("\nStandard Deviation")
print(scores.std())