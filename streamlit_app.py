import streamlit as stimport streamlimport streamlit as stit as stimport streamlit as st

st.set_page_config(page_title="Aviator Predictor", page_icon="✈️")

st.title("✈️ Aviator Predictor")
st.write("Enter previous number(s) to predict the next:")

prev = st.number_input("Previous Round", min_value=1)
rounds = st.number_input("Number of Rounds", min_value=1)

if st.button("Predict"):
    prediction = (prev + rounds) % 100  # Dummy formula
        st.success(f"🎯 Prediction: {prediction}")

st.set_page_config(page_title="Aviator Predictor", page_icon="✈️")
if st.button("Predict"):
@eamlit_app.p
st.title("✈️ Aviator Predictor")
st.write("Enter previous number(s) to predict the next:")

prev = st.number_input("Previous Round", min_value=1)
rounds = st.number_input("Number of Rounds", min_value=1)

if st.button("Predict"):
    prediction = (prev + rounds) % 100  # dummy formula
        st.success(f"🎯 Prediction: {prediction}")