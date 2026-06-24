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
# Top 15 Features
# -----------------------------

selected_features = [

    "blood_pressure",

    "academic_stress_score",

    "environmental_stress_score",

    "physical_health_score",

    "social_support",

    "sleep_quality",

    "mental_distress_score",

    "teacher_student_relationship",

    "wellness_score",

    "academic_performance",

    "basic_needs",

    "depression",

    "self_esteem",

    "headache",

    "anxiety_level"
]

X = df[selected_features]

y = df["stress_level"]

print("\nSelected Features:")
print(len(selected_features))

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
# Random Forest
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
# Train
# -----------------------------

model.fit(
    X_train,
    y_train
)

print("\nTraining Completed")

# -----------------------------
# Save
# -----------------------------

joblib.dump(
    model,
    "models/top15_random_forest.pkl"
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