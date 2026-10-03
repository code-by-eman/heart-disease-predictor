import pickle
import pandas as pd
import streamlit as st

# same order the model was trained on
FEATURE_COLUMNS = ["age", "trestbps", "chol", "thalach"]

st.set_page_config(
    page_title="Heart Disease Risk Predictor",
    page_icon="❤️",
    layout="centered"
)

st.title("❤️ Heart Disease Risk Predictor")
st.write("Fill in the four values below and the model will give you a prediction.")

st.info("For learning purposes only. This is not medical advice or a diagnosis.")

try:
    with open("heart_disease_model.pkl", "rb") as model_file:
        model = pickle.load(model_file)
except FileNotFoundError:
    st.error(
        "The trained model wasn't found. Run every cell in Heart_Disease_ML.ipynb "
        "first to create heart_disease_model.pkl, then reload this page."
    )
    st.stop()

st.subheader("Your Details")

age = st.number_input("Age (years)", min_value=1, max_value=120, value=55, step=1)
trestbps = st.number_input(
    "Resting Blood Pressure (mm Hg)",
    min_value=50, max_value=250, value=140, step=1
)
chol = st.number_input(
    "Serum Cholesterol (mg/dl)",
    min_value=50, max_value=700, value=250, step=1
)
thalach = st.number_input(
    "Maximum Heart Rate Achieved",
    min_value=50, max_value=250, value=150, step=1
)

if st.button("Predict Heart Disease"):
    user_input = pd.DataFrame({
        "age": [age],
        "trestbps": [trestbps],
        "chol": [chol],
        "thalach": [thalach]
    })[FEATURE_COLUMNS]

    prediction = int(model.predict(user_input)[0])

    st.subheader("Result")

    if prediction == 1:
        st.error("Prediction: HEART DISEASE PRESENT")
    else:
        st.success("Prediction: NO HEART DISEASE")

    st.write("Values the model used:")
    st.dataframe(user_input, use_container_width=True)

st.caption("Trained on the UCI Heart Disease (Cleveland) dataset • For learning only")
