import streamlit as st
import pandas as pd
import joblib

# -----------------------------
# Load files
# -----------------------------
model = joblib.load("readmission_model.pkl")
feature_names = joblib.load("feature_names.pkl")
defaults = joblib.load("defaults.pkl")

st.set_page_config(
    page_title="Healthcare Readmission Predictor",
    page_icon="🏥",
    layout="wide"
)

st.title("🏥 Healthcare Readmission Risk Predictor")
st.write(
    "Predict whether a patient is at risk of being readmitted within 30 days."
)

st.sidebar.header("Patient Information")

# Start with default values
patient = defaults.copy()

# User-editable top features
patient["num_lab_procedures"] = st.sidebar.number_input(
    "Number of Lab Procedures",
    value=int(defaults["num_lab_procedures"])
)

patient["num_medications"] = st.sidebar.number_input(
    "Number of Medications",
    value=int(defaults["num_medications"])
)

patient["time_in_hospital"] = st.sidebar.slider(
    "Days in Hospital",
    1,
    14,
    int(defaults["time_in_hospital"])
)

patient["number_inpatient"] = st.sidebar.number_input(
    "Previous Inpatient Visits",
    value=int(defaults["number_inpatient"])
)

patient["num_procedures"] = st.sidebar.number_input(
    "Number of Procedures",
    value=int(defaults["num_procedures"])
)

patient["age"] = st.sidebar.slider(
    "Age (Encoded)",
    0,
    9,
    int(defaults["age"])
)

patient["diag_1"] = st.sidebar.number_input(
    "Primary Diagnosis Code (Encoded)",
    value=int(defaults["diag_1"])
)

patient["diag_2"] = st.sidebar.number_input(
    "Secondary Diagnosis Code (Encoded)",
    value=int(defaults["diag_2"])
)

patient["diag_3"] = st.sidebar.number_input(
    "Tertiary Diagnosis Code (Encoded)",
    value=int(defaults["diag_3"])
)

patient["medical_specialty"] = st.sidebar.number_input(
    "Medical Specialty (Encoded)",
    value=int(defaults["medical_specialty"])
)

input_df = pd.DataFrame([patient])

# Ensure correct column order
input_df = input_df[feature_names]

if st.button("Predict Readmission Risk"):

    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]

    st.subheader("Prediction")

    if prediction == 1:
        st.error("🔴 High Risk of Readmission")
    else:
        st.success("🟢 Low Risk of Readmission")

    st.metric(
        "Probability of Readmission",
        f"{probability*100:.1f}%"
    )

    st.progress(float(probability))

    st.write("### Patient Input")
    st.dataframe(input_df)