import os
from dotenv import load_dotenv
from langchain_openai import OpenAI

# Load environment variables
load_dotenv()

class AyurvedicAssistant:
    def __init__(self, api_key):
        self.llm = OpenAI(api_key=api_key)

    def generate_advice(self, query, age, gender, chief_complaint, family_history, medical_history, pills_taken):
        # Constructing a detailed prompt
        prompt = f"""
        Considering the following patient details:
        - Age: {age}
        - Gender: {gender}
        - Chief Complaint: {chief_complaint}
        {f"- Family History: {family_history}" if family_history else ""}
        {f"- Medical History: {medical_history}" if medical_history else ""}
        {f"- Pills Taken: {pills_taken}" if pills_taken else ""}

        As an Ayurvedic practitioner, provide a simple and effective Ayurvedic home remedy in a traditional format. The remedy should be concise and consider the patient's detailed history and condition. Encourage contacting an Ayurvedic Practitioner for complex conditions not treatable at home. Also encourage the user to just use this remedy for temporary relief and then see an ayurvedic pratitioner.
        """
        result = self.llm.generate(prompts=[prompt], max_tokens=400, temperature=0.6)
        
        advice_text = result.generations[0][0].text.strip()
        

        
        final_cta = "\n\nFor personalized Ayurvedic consultation and a comprehensive treatment plan tailored to your specific needs, talk to a professional Ayurvedic Practitioner."
        
        return advice_text + final_cta


