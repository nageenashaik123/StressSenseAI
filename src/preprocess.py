import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
import joblib
import os

# ----------------------------
# Load Dataset
# ----------------------------

df = pd.read_csv("data/student_mental_health_burnout.csv")

print("Dataset Loaded")
print(df.shape)

# ----------------------------
# Remove Unnecessary Columns
# ----------------------------

df.drop(columns=["student_id"], inplace=True)

# ----------------------------
# Keep Selected Features
# ----------------------------

selected_columns = [
    "age",
    "gender",
    "course",
    "year",
    "daily_study_hours",
    "daily_sleep_hours",
    "screen_time_hours",
    "academic_pressure_score",
    "physical_activity_hours",
    "sleep_quality",
    "attendance_percentage",
    "cgpa",
    "internet_quality",
    "burnout_level"
]

df = df[selected_columns]

print("\nSelected Features:")
print(df.columns)

# ----------------------------
# Encode Categorical Features
# ----------------------------

categorical_cols = [
    "gender",
    "course",
    "year",
    "sleep_quality",
    "internet_quality",
    "burnout_level"
]

encoders = {}

for col in categorical_cols:
    le = LabelEncoder()

    df[col] = le.fit_transform(df[col])

    encoders[col] = le

print("\nEncoding Completed")

# ----------------------------
# Scale Numerical Features
# ----------------------------

numerical_cols = [
    "age",
    "daily_study_hours",
    "daily_sleep_hours",
    "screen_time_hours",
    "academic_pressure_score",
    "physical_activity_hours",
    "attendance_percentage",
    "cgpa"
]

scaler = StandardScaler()

df[numerical_cols] = scaler.fit_transform(df[numerical_cols])

print("Scaling Completed")

# ----------------------------
# Save Processed Dataset
# ----------------------------

os.makedirs("data", exist_ok=True)

df.to_csv(
    "data/processed_data.csv",
    index=False
)

# ----------------------------
# Save Encoders
# ----------------------------

os.makedirs("models", exist_ok=True)

joblib.dump(
    encoders,
    "models/label_encoders.pkl"
)

joblib.dump(
    scaler,
    "models/scaler.pkl"
)

print("\nProcessed Dataset Saved")
print("Encoders Saved")
print("Scaler Saved")

print("\nFinal Shape:")
print(df.shape)