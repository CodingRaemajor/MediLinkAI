import streamlit as st
from bedrock_handler import get_diagnosis_from_bedrock
from sns_alerts import send_health_alert
from dynamodb_handler import save_patient_record

st.set_page_config(page_title="MediLink AI", layout="centered")
st.title("🤖 MediLink AI – Symptom Checker")
st.subheader("Get a quick AI-powered health analysis")

# Form Inputs
name = st.text_input("👤 Your Name")
age = st.number_input("🎂 Age", min_value=1, max_value=120)
gender = st.selectbox("🚻 Gender", ["Male", "Female", "Other"])
symptoms = st.text_area("📝 Describe your symptoms (e.g., chest pain, fatigue)")

if st.button("🩺 Diagnose"):
    if not symptoms.strip():
        st.warning("Please enter your symptoms for diagnosis.")
    else:
        with st.spinner("🔍 MediLink AI is analyzing..."):
            diagnosis = get_diagnosis_from_bedrock(symptoms)
            st.success("✅ AI Diagnosis")
            st.markdown("🧠 **AI Health Insight:**")
            st.markdown(diagnosis.strip())

            save_patient_record(name, age, gender, symptoms, diagnosis)

            # Emergency Symptom Trigger
            critical_keywords = ["chest pain", "shortness of breath", "high fever", "low oxygen", "severe bleeding"]
            if any(kw in symptoms.lower() for kw in critical_keywords):
                send_health_alert(symptoms, name, age)
                st.error("🚨 Critical symptoms detected! An emergency alert has been sent.")