import streamlit as st
import requests
import re
import easyocr
from PIL import Image
import time

# Set your Gemini API key directly in the code
GEMINI_API_KEY = 'AIzaSyDLIRP2NTdk2g8QUweaV18mRlAH3znimgU'

# Function to redact and anonymize sensitive information
def redact_info(text):
    text = re.sub(r'\b\d{12}\b', '[REDACTED AADHAAR]', text)  # Aadhaar card redaction
    text = re.sub(r'\b\d{10}\b', '[REDACTED PHONE]', text)     # Phone number redaction
    text = re.sub(r'\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b', '[REDACTED EMAIL]', text, flags=re.I)  # Email redaction
    text = re.sub(r'\b\w+@\w+\.\w+\b', '[REDACTED EMAIL]', text)  # Email redaction
    text = re.sub(r'\b[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\b', '[REDACTED IP]', text)  # IP Address redaction
    return text

# Function to extract text from image
def extract_text_from_image(image):
    reader = easyocr.Reader(['en'])
    result = reader.readtext(image)
    extracted_text = ' '.join([x[1] for x in result])
    return extracted_text

# Streamlit app layout configuration
def app():
    gradient_text_html = """
        <style>
        .gradient-text {
            font-weight: bold;
            background: -webkit-linear-gradient(left, #07539e, #4fc3f7, #ffffff);
            background: linear-gradient(to right, #07539e, #4fc3f7, #ffffff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            display: inline;
            font-size: 2.9em;
        }
        </style>
        <div class="gradient-text">Neurorehabilitation Assistant</div>
        """

    # Render the gradient text
    st.markdown(gradient_text_html, unsafe_allow_html=True)
    
    

    st.write("""
    Please provide the following details in the text area below:
    1. Age, Gender, and date of diagnosis or injury
    2. Current Symptoms, medical history including chronic conditions, past injuries, and current medications that might affect recovery.
    3. Pre-condition activity level, specific physical goals, and any short-term or long-term recovery goals.
    4. Current level of mobility and any aids being used (e.g., cane, walker, wheelchair).
    5. Assessment of memory, attention, executive function, and any difficulties with speech or language.
    6. Mood, anxiety, depression, or other psychological concerns.
    7. Social Support and Home Environment: Availability of support from family, friends, or caregivers, and any modifications made to the home to support recovery.
    8. Previous rehabilitation therapies undergone and their outcomes, and use of any specific neurorehabilitation devices or technologies (e.g., neuroprosthetics, functional electrical stimulation devices).
    9. :orange[DO NOT ENTER PERSONAL INFORMATION - PhoneNo, EmailID, AadharNo, Any other personal info]
    """)

    # Text area for user input
    user_input = st.text_area("Enter your details here:")
    
    # Image uploading option
    uploaded_file = st.file_uploader("Upload a hospital operation slip or similar document:", type=["png", "jpg", "jpeg", "pdf"])

    def generate_neurorehab_plan(user_input):
        prompt = f"""
        Patient Information:
        {user_input}
        
        Please act as a professional neurorehabilitation therapist and provide the following:
        1. A brief assessment based on the provided information.
        2. A detailed neurorehabilitation plan in a table format for daily exercises and activities, including descriptions and durations.
        3. Recommendations and precautions for the patient to ensure a safe and effective recovery process.

        The plan should cover:
        - Initial phase (weeks 1-2)
        - Intermediate phase (weeks 3-6)
        - Advanced phase (weeks 7-12)

        Ensure that the exercises and activities are appropriate for someone recovering from a neurological condition and that they progressively increase in intensity as the patient heals.
        """
        
        headers = {
            "Authorization": f"Bearer {GEMINI_API_KEY}",
            "Content-Type": "application/json"
        }
        data = {
            "prompt": prompt,
            "max_tokens": 300
        }
        response = requests.post("https://api.gemini.ai/v1/completions", headers=headers, json=data)
        return response.json()["choices"][0]["text"]

    if st.button("Generate Neurorehab Plan"):
        with st.spinner("Generating neurorehabilitation plan..."):
            time.sleep(4)
            generated_plan = generate_neurorehab_plan(user_input)
            st.success(generated_plan)

    if uploaded_file is not None:
        # Check if uploaded file is an image
        if uploaded_file.type.startswith('image'):
            # Display the image
            st.image(uploaded_file, caption='Uploaded Image', use_column_width=True)

            # Convert the file to an image for OCR
            image = Image.open(uploaded_file)
            extracted_text = extract_text_from_image(image)
            st.write("Extracted Text:")
            st.write(extracted_text)
        else:
            st.error('Please upload an image file')

if __name__ == "__main__":
    app()
