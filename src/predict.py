import pandas as pd
import joblib

from reasoning_agent import generate_report
from explainability import get_top_features
# -----------------------------
# Load Model
# -----------------------------

model = joblib.load(
    "models/random_forest_model.pkl"
)

# -----------------------------
# Prediction Function
# -----------------------------

def predict_stress(student_data):

    # -----------------------------
    # Convert to DataFrame
    # -----------------------------

    df = pd.DataFrame([student_data])

    # -----------------------------
    # Feature Engineering
    # -----------------------------

    df["mental_distress_score"] = (
        df["anxiety_level"]
        +
        df["depression"]
        +
        (df["mental_health_history"] * 10)
    )

    df["physical_health_score"] = (
        df["headache"]
        +
        df["blood_pressure"]
        +
        df["breathing_problem"]
        +
        (5 - df["sleep_quality"])
    )

    df["environmental_stress_score"] = (
        df["noise_level"]
        +
        (5 - df["living_conditions"])
        +
        (5 - df["safety"])
        +
        (5 - df["basic_needs"])
    )

    df["academic_stress_score"] = (
        df["study_load"]
        +
        df["future_career_concerns"]
        +
        (5 - df["academic_performance"])
        +
        df["peer_pressure"]
    )

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
    # Prediction
    # -----------------------------

    prediction = model.predict(df)[0]

    probabilities = model.predict_proba(df)[0]

    confidence = max(probabilities) * 100

    # -----------------------------
    # Label Mapping
    # -----------------------------

    label_map = {
        0: "Low Stress",
        1: "Medium Stress",
        2: "High Stress"
    }

    stress_label = label_map[prediction]

    # -----------------------------
    # Top Features
    # -----------------------------

    top_features = get_top_features(df)
    # -----------------------------
    # Agent Report
    # -----------------------------

    report = generate_report(
        stress_label,
        confidence,
        top_features,
        student_data
    )

    return {
    "stress_level": stress_label,
    "confidence": confidence,
    "report": report,
    "top_features": top_features,
    "probabilities": probabilities.tolist()
}