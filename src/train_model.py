import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# -----------------------------
# Load Dataset
# -----------------------------

df = pd.read_csv(
    "data/feature_engineered_data.csv"
)

print("Dataset Loaded")
print(df.shape)

# -----------------------------
# Features and Target
# -----------------------------

X = df.drop(
    columns=["stress_level"]
)

y = df["stress_level"]

print("\nFeatures Shape:")
print(X.shape)

print("\nTarget Shape:")
print(y.shape)

# -----------------------------
# Train Test Split
# -----------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    stratify=y,
    random_state=42
)

print("\nTraining Samples:", len(X_train))
print("Testing Samples :", len(X_test))

# -----------------------------
# Random Forest Model
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
# Train Model
# -----------------------------

model.fit(
    X_train,
    y_train
)

print("\nModel Training Completed")

# -----------------------------
# Save Model
# -----------------------------

joblib.dump(
    model,
    "models/random_forest_model.pkl"
)

joblib.dump(
    X_test,
    "models/X_test.pkl"
)

joblib.dump(
    y_test,
    "models/y_test.pkl"
)

print("Model Saved")