import streamlit as st
import joblib
import numpy as np

# Load the model
model = joblib.load("boston_model.pkl")

st.title("Boston Housing Price Predictor 🏠")

# Create input fields
crim = st.number_input("crim", value=0.00632)
zn = st.number_input("zn", value=18.0)
indus = st.number_input("indus", value=2.31)
chas = st.selectbox("chas (0 = no, 1 = yes)", [0, 1])
nox = st.number_input("nox", value=0.538)
rm = st.number_input("rm", value=6.575)
age = st.number_input("age", value=65.2)
dis = st.number_input("dis", value=4.09)
rad = st.number_input("rad", value=1)
tax = st.number_input("tax", value=296)
ptratio = st.number_input("ptratio", value=15.3)
b = st.number_input("b", value=396.9)
lstat = st.number_input("lstat", value=4.98)

# Predict button
if st.button("Predict"):
    data = np.array([[crim, zn, indus, chas, nox, rm, age, dis, rad, tax, ptratio, b, lstat]])
    prediction = model.predict(data)
    st.success(f"Predicted House Price: ${prediction[0]:.2f}k")

# Run in cmd: streamlit run app_streamlit.py

# in docker: change the CMD:
#    ["streamlit", "run", "app_streamlit.py", "--server.address=0.0.0.0", "--server.port=8501"]