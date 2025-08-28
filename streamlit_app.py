import streamlit as st
from PIL import Image
import requests

BACKEND_URL = 'https://cycle-vs-bike.onrender.com'

st.title("Cycle vs Bike Classifier")

img = st.file_uploader(
    "Choose an image of a cycle or bike", 
    type=['jpg', 'jpeg', 'png', 'bmp', 'webp']
)

if img is not None:
    # st.write(uploaded_file.type)
    if img.type.startswith('image/'):
        image = Image.open(img)
        st.image(image, use_container_width=True)

        send_img = {"file": (img.name, img.getvalue(), img.type)}
        response = requests.post(BACKEND_URL, files=send_img)
        
        if response.status_code == 200:
            result = response.json()
            st.success(f"Prediction: {result['prediction']}")
            st.info(f"Confidence: {result['confidence']*100:.2f}%")
        else:
            st.error("error")
