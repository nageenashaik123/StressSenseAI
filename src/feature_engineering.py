import pandas as pd

# -----------------------------
# Load Dataset
# -----------------------------

df = pd.read_csv(
    "data/StressLevelDataset.csv"
)

print("Dataset Loaded")
print(df.shape)

# -----------------------------
# Mental Distress Score
# -----------------------------

df["mental_distress_score"] = (
    df["anxiety_level"]
    +
    df["depression"]
    +
    (df["mental_health_history"] * 10)
)

# -----------------------------
# Physical Health Score
# -----------------------------

df["physical_health_score"] = (
    df["headache"]
    +
    df["blood_pressure"]
    +
    df["breathing_problem"]
    +
    (5 - df["sleep_quality"])
)

# -----------------------------
# Environmental Stress Score
# -----------------------------

df["environmental_stress_score"] = (
    df["noise_level"]
    +
    (5 - df["living_conditions"])
    +
    (5 - df["safety"])
    +
    (5 - df["basic_needs"])
)

# -----------------------------
# Academic Stress Score
# -----------------------------

df["academic_stress_score"] = (
    df["study_load"]
    +
    df["future_career_concerns"]
    +
    (5 - df["academic_performance"])
    +
    df["peer_pressure"]
)

# -----------------------------
# Wellness Score
# -----------------------------

df["wellness_score"] = (
    df["self_esteem"]
    +
    df["social_support"]
    +
    df["teacher_student_relationship"]
    +
    df["extracurricular_activities"]
)

# -----------------------------
# Save
# -----------------------------

df.to_csv(
    "data/feature_engineered_data.csv",
    index=False
)

print("\nFeature Engineering Completed")

print("\nNew Shape:")
print(df.shape)

print("\nDataset Saved")