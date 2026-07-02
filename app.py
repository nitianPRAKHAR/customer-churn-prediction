import streamlit as st
import pandas as pd
import joblib

# ----------------------------
# Load the saved model, encoders, and column order
# ----------------------------
model = joblib.load("churn_model.pkl")
encoders = joblib.load("encoders.pkl")
columns = joblib.load("columns.pkl")

st.title("Customer Churn Prediction App")
st.write("Fill in the customer details below and click Predict to check if the customer is likely to churn.")

# ----------------------------
# Input fields (one for each column the model was trained on)
# ----------------------------

st.header("Customer Details")

gender = st.selectbox("Gender", ["Female", "Male"])
senior_citizen = st.selectbox("Senior Citizen", ["No", "Yes"])
partner = st.selectbox("Has Partner", ["No", "Yes"])
dependents = st.selectbox("Has Dependents", ["No", "Yes"])
tenure = st.number_input("Tenure (months with the company)", min_value=0, max_value=100, value=12)

st.header("Services")

phone_service = st.selectbox("Phone Service", ["No", "Yes"])
multiple_lines = st.selectbox("Multiple Lines", ["No", "No phone service", "Yes"])
internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
online_security = st.selectbox("Online Security", ["No", "No internet service", "Yes"])
online_backup = st.selectbox("Online Backup", ["No", "No internet service", "Yes"])
device_protection = st.selectbox("Device Protection", ["No", "No internet service", "Yes"])
tech_support = st.selectbox("Tech Support", ["No", "No internet service", "Yes"])
streaming_tv = st.selectbox("Streaming TV", ["No", "No internet service", "Yes"])
streaming_movies = st.selectbox("Streaming Movies", ["No", "No internet service", "Yes"])

st.header("Account Info")

contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
paperless_billing = st.selectbox("Paperless Billing", ["No", "Yes"])
payment_method = st.selectbox(
    "Payment Method",
    ["Bank transfer (automatic)", "Credit card (automatic)", "Electronic check", "Mailed check"]
)
monthly_charges = st.number_input("Monthly Charges", min_value=0.0, value=70.0)
total_charges = st.number_input("Total Charges", min_value=0.0, value=1000.0)

# ----------------------------
# Predict button
# ----------------------------

if st.button("Predict"):

    # Put all inputs into a dictionary first, in plain text form
    input_dict = {
        "gender": gender,
        "SeniorCitizen": 1 if senior_citizen == "Yes" else 0,
        "Partner": partner,
        "Dependents": dependents,
        "tenure": tenure,
        "PhoneService": phone_service,
        "MultipleLines": multiple_lines,
        "InternetService": internet_service,
        "OnlineSecurity": online_security,
        "OnlineBackup": online_backup,
        "DeviceProtection": device_protection,
        "TechSupport": tech_support,
        "StreamingTV": streaming_tv,
        "StreamingMovies": streaming_movies,
        "Contract": contract,
        "PaperlessBilling": paperless_billing,
        "PaymentMethod": payment_method,
        "MonthlyCharges": monthly_charges,
        "TotalCharges": total_charges,
    }

    # Convert dictionary into a one-row DataFrame
    input_df = pd.DataFrame([input_dict])

    # Encode the text columns using the SAME encoders used during training
    for col in encoders:
        if col in input_df.columns:
            input_df[col] = encoders[col].transform(input_df[col])

    # Make sure columns are in the exact same order as during training
    input_df = input_df[columns]

    # Predict
    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]  # probability of churn (class 1)

    st.header("Result")

    if prediction == 1:
        st.error(f"This customer is likely to CHURN. (Churn probability: {probability:.2%})")
    else:
        st.success(f"This customer is likely to STAY. (Churn probability: {probability:.2%})")
