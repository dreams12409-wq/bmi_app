import streamlit as st
st.title("BMI Checker")
st.write("Calculate your Body Mass Index")
height = st.number_input("Height (cm)", value=175.0)
weight = st.number_input("Weight (kg)", value=70.0)
if st.button("Calculate BMI"):
    bmi = weight / ((height / 100) ** 2)
    st.subheader(f"Your BMI is: {bmi:.2f}")
    
