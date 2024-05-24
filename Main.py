import streamlit as st
from helper import AyurvedicAssistant  # Ensure this import is correct
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    st.error("API key not found. Please check your .env file.")
else:
    assistant = AyurvedicAssistant(api_key=api_key)
    st.title("Brahma: Your Ayurvedic AI Assistant")

    # Collecting additional details
    age = st.number_input("Age", min_value=1, max_value=120)
    gender = st.selectbox("Gender", ["Male", "Female", "Other", "Prefer not to say"])
    chief_complaint = st.text_input("What is bothering you?")
    family_history = st.text_area("Any family medical history?", "")
    medical_history = st.text_area("Your medical history", "")
    meds_taken = st.text_area("Any medicine taken?", "")

    if st.button("Get Ayurvedic Advice"):
        if chief_complaint:  # Assuming chief complaint is the minimum required input
            advice = assistant.generate_advice(
                query=chief_complaint,  # Using chief complaint as the primary query
                age=age, 
                gender=gender, 
                chief_complaint=chief_complaint, 
                family_history=family_history, 
                medical_history=medical_history, 
                pills_taken=meds_taken
            )
            st.markdown(advice, unsafe_allow_html=True)
        else:
            st.warning("Please enter the chief complaint to receive Ayurvedic advice.")
