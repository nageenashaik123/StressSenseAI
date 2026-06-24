from predict import predict_stress

student = {

    "anxiety_level":18,
    "self_esteem":10,
    "mental_health_history":1,
    "depression":16,
    "headache":4,
    "blood_pressure":4,
    "sleep_quality":1,
    "breathing_problem":3,
    "noise_level":4,
    "living_conditions":2,
    "safety":2,
    "basic_needs":3,
    "academic_performance":2,
    "study_load":5,
    "teacher_student_relationship":2,
    "future_career_concerns":5,
    "social_support":1,
    "peer_pressure":4,
    "extracurricular_activities":1,
    "bullying":3
}

result = predict_stress(student)

print(result["stress_level"])
print(result["confidence"])
print(result["report"])