import streamlit as st
from img_classification import teachable_machine_classification

st.title("Image Classification")
st.header("Pneumonia classification from chest X-ray")
st.text("Upload a Chest X-ray Image for image classification as pneumonia or normal")

uploaded_file = st.file_uploader("Choose a brain MRI ...", type="jpg")
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded MRI.', use_column_width=True)
    st.write("")
    st.write("Classifying...")
    label = teachable_machine_classification(image, 'brain_tumor_classification.h5')
    if label == 0:
        st.write("The MRI scan has a brain tumor")
    else:
        st.write("The MRI scan is healthy")