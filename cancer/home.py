import streamlit as st
import streamlit.components.v1 as components
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
        <div class="gradient-text">Welcome to Chemo Chill</div>
        """

    # Render the gradient text
    st.markdown(gradient_text_html, unsafe_allow_html=True)

    st.write(":orange[A mission to revolutionize scalp cooling therapy in India ]")
    
    st.image('divider.png')
    
   

    st.write('Hair loss is a common and distressing side effect of chemotherapy, causing significant emotional and psychological strain for patients undergoing cancer treatment. Remarkably, around 14% of women refuse chemotherapy due to the fear of hair loss. Our solution, Chemo Chill, aims to address this issue by providing an innovative approach to mitigate hair fall during treatment, helping patients maintain their sense of identity and improving their overall treatment experience')
    
    st.write('')
    st.write('')
    col4, col5,col7, col6 , col8 = st.columns([0.11,0.45,0.07,0.5, 0.09])
    with col5:
        st.write('')
        
        components.html(
    """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
* {
  box-sizing: border-box;
  margin: 0; /* Remove default margin */
  padding: 0; /* Remove default padding */
}
body {
  font-family: Verdana, sans-serif;
}
.mySlides {
  display: none;
}
img {
  vertical-align: middle;
  width: 100%; /* Make images fill their containers */
  margin: 0; /* Remove any margin */
  padding: 0; /* Remove any padding */
}
/* Slideshow container */
.slideshow-container {
  max-width: 400px;
  max-height : 400px;
  position: 100%;
  margin: 0;
}

/* Number text (1/3 etc) */
.numbertext {
  color: #f2f2f2;
  font-size: 12px;
  padding: 8px 12px;
  position: absolute;
  top: 0;
}
/* Fading animation */
.fade {
  animation-name: fade;
  animation-duration: 1.9s;
}
@keyframes fade {
  from {opacity: .4} 
  to {opacity: 1}
}
</style>
</head>
<body>
<div class="slideshow-container">
  <div class="mySlides fade">
    <div class="numbertext">1 / 4</div>
    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSf22xEOqZQwUilYo5CnKYAM1VdVyWZI4Lykg&s">
    
  </div>
  <div class="mySlides fade">
    <div class="numbertext">2 / 4</div>
    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQeiBOAvfcs8QTRfbKs7h7QbHR1W5QkfC9GSg&s">
  </div>
  <div class="mySlides fade">
    <div class="numbertext">3 / 4</div>
    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRppAR5s5Q_aqc9cHs7Y0jBAMooPZGUcbRfgQ&s">
    
  </div>
  
</div>
<script>
  let slideIndex = 0;
  showSlides();

  function showSlides() {
    let i;
    let slides = document.getElementsByClassName("mySlides");
    for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";  
    }
    slideIndex++;
    if (slideIndex > slides.length) {slideIndex = 1}    
    slides[slideIndex-1].style.display = "block";  
    setTimeout(showSlides, 2000); // Change image every 2 seconds
  }
</script>
</body>
</html>
    """,
    height=300, width=400
)
    

    with col6:
        st.write("Our solution, Chemo Chill, is designed to address the significant concern of hair loss during chemotherapy using advanced cooling technology.")
        st.write("- Utilizing Peltier Modules: Chemo Chill incorporates Peltier modules to efficiently cool the scalp, minimizing hair loss during chemotherapy by reducing the metabolic activity of hair follicles.")
        st.write("- Real-Time Data Monitoring: Our system features real-time monitoring of temperature and other vital parameters, ensuring the cooling process is both safe and effective throughout the treatment. ")
        st.write("- Personalized Cooling Cap: The cooling cap is tailored to consider a wide range of patient-specific parameters such as age, gender, and cancer type, providing a customized and optimized cooling experience for each patient. ")
        st.write("- Market and Future Projections: By 2040, cancer cases are projected to reach 29.5 million annually. The market for cooling cap systems is expected to hit $250 million by 2026, highlighting a significant opportunity to deliver accessible and impactful solutions to patients.")
            


   
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    col1,col2,col3 = st.columns([0.5,1,0.5])
    with col2:
        st.write('   Project by team - :orange[BYTEBUDDIES] - Deekshith B , Sanjana W G, KM Skanda , Sanjana B J , Shreyashri ')
    
    
if __name__ == "__main__":
    app()
    
