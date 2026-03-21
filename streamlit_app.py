import streamlit as st
import pandas as pd
import joblib

st.title("Salary Prediction")

# โหลด model
model = joblib.load('model.pkl')

# input
rating = st.slider("Rating", 1.0, 5.0)
experience = st.slider("Experience (years)", 0, 20)

job = st.selectbox("Job Role", ["Android", "Backend", "Data Scientist"])
location = st.selectbox("Location", ["Bangalore", "Delhi", "Mumbai"])

input_data = pd.DataFrame([{
    'Rating': rating,
    'Experience': experience,
    'Job Roles': job,
    'Location': location
}])

if st.button("Predict Salary"):
    pred = model.predict(input_data)[0]
    st.success(f"💰 Salary: {pred:,.0f}")
