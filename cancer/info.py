import streamlit as st
import pandas as pd


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
        <div class="gradient-text">Chemo Cool Assistant</div>
        """

    # Render the gradient text
    st.markdown(gradient_text_html, unsafe_allow_html=True)
    
    



    st.write('Cooling caps are devices used to reduce hair loss in patients undergoing chemotherapy. They work by cooling the scalp, which reduces the blood flow to hair follicles, thereby minimizing the amount of chemotherapy drugs that reach the hair follicles. This process is also known as scalp hypothermia.')
    st.image('divider.png')
    st.subheader(" 1. :orange[Usage Guidelines]")
    st.write("- Before Treatment: The cooling cap should be worn 30 minutes before the chemotherapy session begins.")
    st.write("- During Treatment: The cap should remain in place throughout the entire chemotherapy session.")
    st.write("- After Treatment: The cooling cap should continue to be worn for 90 minutes after the chemotherapy session ends")
   

    st.subheader(" 2. :orange[Temperature Guidelines]")

    st.write("If the cooling cap is set to 3°C to 8°C, it maintains the scalp temperature within the range of 18°C to 22°C.")

    col7,col8,col9 = st.columns([0.4, 1 , 0.6])

    with col8:
        data = {
            "Female": ["0-8", "9-18", "19-55", "56-65", "65+"],
            "Male": ["0-8", "9-18", "19-55", "56-65", "65+"],
            "Temperature": ["8°C", "6°C", "4°C", "5°C", "8°C"]
        }
        df = pd.DataFrame(data)
        st.table(df)

    st.header(" 3. :orange[Precautions]")
    st.write("Before using the cooling cap, ensure the patient does not have")
    st.write(" - Cold Sensitivity: Patients who experience discomfort or adverse reactions to cold temperatures.")
    st.write(" - Cold Agglutinin Disease: A condition where antibodies in the blood clump together in response to cold temperatures, leading to complications.")
    st.write(" - Cryoglobulinemia: Presence of abnormal proteins in the blood that can become insoluble and precipitate at cold temperatures, causing circulation problems.")

    st.write(" - Cold Urticaria: A skin condition characterized by hives or welts when exposed to cold temperatures. ")

    st.write('')

    st.subheader(" 4. :orange[Imp Information]")

    col4, col5 = st.columns([1,1])

    with col4:
        st.write("**Cooling caps are recommended for use with the following types of cancers**")
        st.markdown("""
        - Solid tumor cancers:
        - Breast cancer
        - Prostate cancer
        - Ovarian cancer
        - Uterine cancer
        - Lung cancer
        - Pancreatic Cancer
        - Kidney Cancer
        - Bladder Cancer
        - Liver Cancer
        - Stomach Cancer
        - Esophageal Cancer
        - Thyroid Cancer
                """)

    with col5:
        st.write("**Cooling caps should not be used for**")
        st.write('Hematologic Cancers:')
        st.write(" - Leukemia")
        st.write(" - Lymphoma")
        st.write(" - Multiple Myeloma")

        st.write('')
        st.write(" - Melanoma (Skin Cancer)")
        st.write(" - Brain Tumors (Brain Cancer) ")
        st.write(" - Blood-related cancers where chemotherapy affects the entire body's blood system.")



    st.subheader(" 5. :orange[Challenges and Limitations]")
    st.write("- Not Suitable for All Patients: As mentioned, patients with specific cold-related conditions cannot use the cooling cap. ")
    st.write("- Varied Effectiveness: The success rate can vary based on the type and dosage of chemotherapy drugs used ")
    st.write("- Comfort Issues: Some patients may find the cap uncomfortable due to the cold temperature.")
    st.write("-  Duration: The need to wear the cap before, during, and after treatment sessions can be inconvenient and time-consuming.")



    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')

    

    
if __name__ == "__main__":
    app()

   