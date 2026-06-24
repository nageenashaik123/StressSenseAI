# StressSenseAI
AI-Powered Student Stress Detection and Wellness Recommendation System
Good idea. A GitHub README should show **Inputs, Workflow, Technologies, Outputs, Architecture, and Sample Results**. Use this improved version.

# 🧠 StressSense AI

### AI-Powered Student Stress Detection and Wellness Recommendation System

StressSense AI is an intelligent student wellness assessment platform that combines **Machine Learning, Explainable AI, and Agentic AI** to predict student stress levels and generate personalized wellness recommendations.

---

# 📌 Problem Statement

University students often experience stress due to academic pressure, mental health challenges, physical health issues, social factors, and environmental conditions. Early identification of stress can help improve mental well-being, academic performance, and overall quality of life.

StressSense AI provides an AI-driven solution that predicts stress levels and generates personalized wellness insights to support students in managing their mental health proactively.

---

# 🚀 Features

✅ Student Wellness Questionnaire

✅ Stress Level Prediction

✅ Confidence Score Estimation

✅ Explainable AI Analysis

✅ Personalized Recommendations

✅ AI Reasoning Agent (Phi3)

✅ Streamlit Dashboard

✅ PDF Wellness Report

---

# 🎯 User Input

The system collects responses through an interactive questionnaire.

### Mental Health

* Anxiety Level (0–20)
* Depression Level (0–20)
* Self Esteem (0–30)
* Mental Health History (0 or 1)

### Physical Health

* Sleep Quality (0–5)
* Headache Frequency (0–5)
* Blood Pressure Issues (0–5)
* Breathing Problems (0–5)

### Academic Factors

* Academic Performance (0–5)
* Study Load (0–5)
* Teacher Relationship (0–5)
* Career Concerns (0–5)
* Peer Pressure (0–5)

### Environmental Factors

* Social Support (0–5)
* Noise Level (0–5)
* Living Conditions (0–5)
* Safety (0–5)
* Basic Needs (0–5)
* Extracurricular Activities (0–5)
* Bullying (0–5)

---

# 🏗️ System Workflow

```text
Student Questionnaire
            ↓
Feature Engineering
            ↓
Random Forest Classifier
            ↓
Stress Prediction
            ↓
Confidence Score
            ↓
Feature Importance Analysis
            ↓
Phi3 AI Reasoning Agent
            ↓
Personalized Wellness Report
            ↓
PDF Report Generation
```

---

# ⚙️ Feature Engineering

The system creates 5 wellness indicators.

### Mental Distress Score

Based on:

* Anxiety
* Depression
* Mental Health History

### Physical Health Score

Based on:

* Headache
* Blood Pressure
* Breathing Problems
* Sleep Quality

### Environmental Stress Score

Based on:

* Noise
* Living Conditions
* Safety
* Basic Needs

### Academic Stress Score

Based on:

* Study Load
* Career Concerns
* Academic Performance
* Peer Pressure

### Wellness Score

Based on:

* Self Esteem
* Social Support
* Teacher Relationship
* Extracurricular Activities

---

# 🤖 Technologies Used

### Machine Learning

* Random Forest Classifier

### Explainable AI

* Feature Importance Analysis

### Agentic AI

* Phi3 Mini (Ollama)

### Web Application

* Streamlit

### Data Processing

* Python
* Pandas
* NumPy
* Scikit-Learn

### Report Generation

* ReportLab PDF

---

# 📊 Dataset Information

| Property            | Value                    |
| ------------------- | ------------------------ |
| Records             | 1100                     |
| Original Features   | 20                       |
| Engineered Features | 5                        |
| Total Features      | 25                       |
| Classes             | Low, Medium, High Stress |

---

# 📈 Model Performance

### Random Forest Classifier

| Metric    | Score  |
| --------- | ------ |
| Accuracy  | 89.09% |
| Precision | 89.16% |
| Recall    | 89.09% |
| F1 Score  | 89.09% |

### Cross Validation

* 5 Fold Cross Validation
* Mean Accuracy: 88.45%

---

# 🔍 Explainable AI Results

Top contributing factors identified by the model:

1. Blood Pressure
2. Academic Stress Score
3. Environmental Stress Score
4. Physical Health Score
5. Social Support
6. Sleep Quality
7. Mental Distress Score
8. Teacher Relationship

---

# 🧠 Agentic AI Reasoning

The Phi3 AI Agent receives:

* Predicted Stress Level
* Confidence Score
* Important Features
* Student Profile

The agent generates:

* Stress Analysis
* Primary Causes
* Academic Risks
* Lifestyle Risks
* Recommendations
* Wellness Summary

---

# 📄 Sample Output

### Prediction

```text
Stress Level: High Stress

Confidence: 72.92%
```

### AI Reasoning Summary

```text
Primary Causes:
High anxiety, depression, poor sleep quality,
and academic pressure.

Academic Risks:
Reduced concentration, burnout risk,
declining academic performance.

Lifestyle Risks:
Poor sleep habits and inadequate stress
management.

Recommendations:
Improve sleep schedule, seek counseling,
practice relaxation techniques, and maintain
healthy social interactions.
```

---

# 🎯 Target Users

* University Students
* College Students
* Educational Institutions
* Student Counseling Centers
* Academic Advisors
* Mentors
* Mental Health Support Programs
* Educational Researchers

---

# 🌍 Impact

StressSense AI enables early identification and management of student stress through AI-driven assessments. By combining machine learning, explainable AI, and agentic reasoning, the system provides personalized wellness insights and recommendations that support mental well-being, academic success, and healthier learning environments.

---

# 🛠️ Installation

```bash
git clone https://github.com/nageenashaik123/StressSenseAI.git

cd StressSenseAI
```

Create Environment:

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

Install Dependencies:

```bash
pip install -r requirements.txt
```

Run Ollama:

```bash
ollama run phi3:mini
```

Run Application:

```bash
streamlit run app.py
```

---

# 📂 Project Structure

```text
StressSenseAI
│
├── app.py
├── data
├── models
├── src
│   ├── predict.py
│   ├── reasoning_agent.py
│   ├── explainability.py
│   ├── feature_engineering.py
│
├── requirements.txt
└── README.md
```

---

# 👨‍💻 Developed By

**Nageena Shaik**

B.Tech Computer Science Engineering

AI • Machine Learning • Data Science • ServiceNow

This version looks much stronger for GitHub, internship reviews, hackathons, and recruiter portfolios because it clearly shows **inputs → processing → AI components → outputs → impact**.

