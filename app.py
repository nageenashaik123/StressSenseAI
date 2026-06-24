import sys
sys.path.append("src")

import streamlit as st
import pandas as pd
from predict import predict_stress
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="StressSense AI",
    page_icon="🧠",
    layout="wide"
)

# ==================================================
# CSS
# ==================================================

st.markdown("""
<style>

.main {
    background-color: #F8FAFC;
}

.stButton > button {
    width: 100%;
    height: 55px;
    border-radius: 12px;
    font-size: 18px;
    font-weight: bold;
}

div[data-testid="metric-container"] {
    border-radius: 15px;
    padding: 15px;
    border: 1px solid #E5E7EB;
}

</style>
""", unsafe_allow_html=True)

# ==================================================
# SIDEBAR
# ==================================================

with st.sidebar:

    st.title("🧠 StressSense AI")

    st.write(
        "Student Wellness Assessment System"
    )

    st.success(
        "Random Forest Accuracy: 89.09%"
    )

    st.info(
        "Powered by Phi3 + Ollama"
    )

# ==================================================
# HEADER
# ==================================================

st.title("🧠 StressSense AI")

st.markdown(
"""
### Student Wellness Assessment

Answer the questionnaire below and our AI system will:

- Predict stress level
- Explain key factors
- Generate recommendations
- Create a wellness report
"""
)

# ==================================================
# TABS
# ==================================================

tab1, tab2, tab3, tab4 = st.tabs(
    [
        "Mental Health",
        "Physical Health",
        "Academic",
        "Environment"
    ]
)

# ==================================================
# MENTAL HEALTH
# ==================================================

with tab1:

    anxiety_level = st.slider(
        "Anxiety Level",
        0,
        20,
        10
    )

    depression = st.slider(
        "Depression Level",
        0,
        20,
        10
    )

    self_esteem = st.slider(
        "Self Esteem",
        0,
        30,
        15
    )

    mental_health_history = st.selectbox(
        "Mental Health History",
        [0, 1]
    )

# ==================================================
# PHYSICAL HEALTH
# ==================================================

with tab2:

    sleep_quality = st.slider(
        "Sleep Quality",
        0,
        5,
        3
    )

    headache = st.slider(
        "Headache Frequency",
        0,
        5,
        2
    )

    blood_pressure = st.slider(
        "Blood Pressure Issues",
        0,
        5,
        2
    )

    breathing_problem = st.slider(
        "Breathing Problems",
        0,
        5,
        2
    )

# ==================================================
# ACADEMIC
# ==================================================

with tab3:

    academic_performance = st.slider(
        "Academic Performance",
        0,
        5,
        3
    )

    study_load = st.slider(
        "Study Load",
        0,
        5,
        3
    )

    teacher_student_relationship = st.slider(
        "Teacher Relationship",
        0,
        5,
        3
    )

    future_career_concerns = st.slider(
        "Career Concerns",
        0,
        5,
        3
    )

    peer_pressure = st.slider(
        "Peer Pressure",
        0,
        5,
        2
    )

# ==================================================
# ENVIRONMENT
# ==================================================

with tab4:

    social_support = st.slider(
        "Social Support",
        0,
        5,
        3
    )

    noise_level = st.slider(
        "Noise Level",
        0,
        5,
        2
    )

    living_conditions = st.slider(
        "Living Conditions",
        0,
        5,
        3
    )

    safety = st.slider(
        "Safety",
        0,
        5,
        3
    )

    basic_needs = st.slider(
        "Basic Needs",
        0,
        5,
        3
    )

    extracurricular_activities = st.slider(
        "Extracurricular Activities",
        0,
        5,
        2
    )

    bullying = st.slider(
        "Bullying",
        0,
        5,
        1
    )

# ==================================================
# STUDENT DATA
# ==================================================

student_data = {
    "anxiety_level": anxiety_level,
    "self_esteem": self_esteem,
    "mental_health_history": mental_health_history,
    "depression": depression,
    "headache": headache,
    "blood_pressure": blood_pressure,
    "sleep_quality": sleep_quality,
    "breathing_problem": breathing_problem,
    "noise_level": noise_level,
    "living_conditions": living_conditions,
    "safety": safety,
    "basic_needs": basic_needs,
    "academic_performance": academic_performance,
    "study_load": study_load,
    "teacher_student_relationship": teacher_student_relationship,
    "future_career_concerns": future_career_concerns,
    "social_support": social_support,
    "peer_pressure": peer_pressure,
    "extracurricular_activities": extracurricular_activities,
    "bullying": bullying
}

# ==================================================
# BUTTON
# ==================================================

predict_btn = st.button(
    "🧠 Analyze My Wellness"
)

# ==================================================
# PDF FUNCTION
# ==================================================

def create_pdf(report_text):

    pdf_file = "StressSense_Report.pdf"

    doc = SimpleDocTemplate(
        pdf_file
    )

    styles = getSampleStyleSheet()

    story = []

    story.append(
        Paragraph(
            "StressSense AI Wellness Report",
            styles["Title"]
        )
    )

    story.append(
        Spacer(1, 12)
    )

    story.append(
        Paragraph(
            report_text.replace("\n", "<br/>"),
            styles["BodyText"]
        )
    )

    doc.build(story)

    return pdf_file

# ==================================================
# PREDICTION
# ==================================================

if predict_btn:

    with st.spinner("Analyzing..."):

        result = predict_stress(
            student_data
        )

    stress_level = result["stress_level"]
    confidence = result["confidence"]
    report = result["report"]

    st.divider()

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "Stress Level",
            stress_level
        )

    with c2:
        st.metric(
            "Confidence",
            f"{confidence:.2f}%"
        )

    with c3:
        st.metric(
            "Risk",
            "High" if confidence >= 80 else "Moderate"
        )

    st.subheader(
        "Confidence Score"
    )

    st.progress(
        confidence / 100
    )

    st.subheader(
        "AI Wellness Report"
    )

    st.write(
        report
    )

    pdf_path = create_pdf(
        report
    )

    with open(
        pdf_path,
        "rb"
    ) as file:

        st.download_button(
            label="📄 Download Wellness Report",
            data=file,
            file_name="StressSense_Report.pdf",
            mime="application/pdf"
        )