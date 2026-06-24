import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
import joblib
import os

# -------------------------
# Load Dataset
# -------------------------

df = pd.read_csv(
    "data/feature_engineered_data.csv"
)

print("Dataset Loaded")
print(df.shape)

# -------------------------
# Remove student_id
# -------------------------

if "student_id" in df.columns:
    df.drop(columns=["student_id"], inplace=True)

# -------------------------
# Keep Required Columns
# -------------------------

final_columns = [

    "age",
    "gender",
    "course",
    "year",

    "daily_study_hours",
    "daily_sleep_hours",
    "screen_time_hours",

    "stress_level",
    "anxiety_score",
    "depression_score",

    "academic_pressure_score",
    "financial_stress_score",
    "social_support_score",

    "physical_activity_hours",

    "sleep_quality",

    "attendance_percentage",
    "cgpa",

    "internet_quality",

    "study_sleep_ratio",
    "screen_sleep_ratio",
    "lifestyle_balance_score",
    "academic_load_score",

    "burnout_level"
]

df = df[final_columns]

# -------------------------
# Label Encoding
# -------------------------

categorical_cols = [

    "gender",
    "course",
    "year",
    "stress_level",
    "sleep_quality",
    "internet_quality",
    "burnout_level"
]

encoders = {}

for col in categorical_cols:

    le = LabelEncoder()

    df[col] = le.fit_transform(df[col])

    encoders[col] = le

print("Encoding Completed")

# -------------------------
# Scaling
# -------------------------

numerical_cols = [

    "age",

    "daily_study_hours",
    "daily_sleep_hours",
    "screen_time_hours",

    "anxiety_score",
    "depression_score",

    "academic_pressure_score",
    "financial_stress_score",
    "social_support_score",

    "physical_activity_hours",

    "attendance_percentage",
    "cgpa",

    "study_sleep_ratio",
    "screen_sleep_ratio",
    "lifestyle_balance_score",
    "academic_load_score"
]

scaler = StandardScaler()

df[numerical_cols] = scaler.fit_transform(
    df[numerical_cols]
)

print("Scaling Completed")

# -------------------------
# Save Files
# -------------------------

os.makedirs("models", exist_ok=True)

df.to_csv(
    "data/final_dataset.csv",
    index=False
)

joblib.dump(
    scaler,
    "models/scaler.pkl"
)

joblib.dump(
    encoders,
    "models/label_encoders.pkl"
)
print("\nBurnout Classes:")
print(encoders["burnout_level"].classes_)

print("\nFinal Dataset Saved")
print("\nFinal Shape:")
print(df.shape)