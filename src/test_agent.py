from reasoning_agent import generate_report

prediction = "High"

confidence = 89.09

top_features = [
    "blood_pressure",
    "academic_stress_score",
    "sleep_quality",
    "social_support",
    "mental_distress_score"
]

student_profile = {
    "anxiety_level": 18,
    "self_esteem": 10,
    "depression": 16,
    "sleep_quality": 1,
    "social_support": 1,
    "academic_performance": 2,
    "study_load": 5
}

report = generate_report(
    prediction,
    confidence,
    top_features,
    student_profile
)

print(report)