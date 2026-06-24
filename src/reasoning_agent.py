import ollama


def generate_report(
    prediction,
    confidence,
    top_features,
    student_profile
):

    prompt = f"""
You are an experienced Student Wellness Advisor.

Student Stress Level: {prediction}

Confidence: {confidence:.2f}%

Top Factors:
{top_features}

Student Profile:
{student_profile}

Generate a concise wellness report.

Sections:
1. Stress Assessment
2. Key Factors
3. Academic & Lifestyle Impact
4. Recommendations
5. Wellness Summary

Requirements:
- Keep report under 250 words.
- Use simple language.
- Avoid repetition.
- Give practical recommendations.
"""

    response = ollama.chat(
        model="phi3:mini",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]