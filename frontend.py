import streamlit as st
import requests
import json

def main():
    st.title("CUSTOMER CHURN PREDICTION")
    gender = st.selectbox("Gender",("Male","Female"))
    if gender == "Male":
        gender = 1
    else:
        gender = 0
    SeniorCitizen = st.selectbox("SeniorCitizen",("Yes","No"))
    if SeniorCitizen == "Yes":
        SeniorCitizen = 1
    else:
        SeniorCitizen = 0
    Partner = st.selectbox("Partner",("Yes","No"))
    if Partner == "Yes":
        Partner = 0
    else:
        Partner = 1
    Dependents = st.selectbox("Dependents",("Yes","No"))
    if Dependents == "Yes":
        Dependents = 1
    else:
        Dependents = 0
    PhoneService = st.selectbox("PhoneService",("Yes","No"))
    if PhoneService == "Yes":
        PhoneService = 1
    else:
        PhoneService = 0
    MultipleLines = st.selectbox("MultipleLines",("No phone service", "No", "Yes"))
    if MultipleLines == "No phone service":
        MultipleLines = 0
    elif MultipleLines == "No":
        MultipleLines = 1
    else:
        MultipleLines = 2
    InternetService = st.selectbox("InternetService",("DSL", "Fiber optic", "No"))
    if InternetService == "DSL":
        InternetService = 0
    elif InternetService == "Fiber optic":
        InternetService = 1
    else:
        InternetService = 2
    OnlineSecurity = st.selectbox("OnlineSecurity",("No", "Yes", "No internet service"))
    if OnlineSecurity == "No":
        OnlineSecurity = 0
    elif OnlineSecurity == "Yes":
        OnlineSecurity = 1
    else:
        OnlineSecurity = 2
    OnlineBackup = st.selectbox("OnlineBackup",("Yes", "No", "No internet service"))
    if OnlineBackup == "Yes":
        OnlineBackup = 0
    elif OnlineBackup == "No":
        OnlineBackup = 1
    else:
        OnlineBackup = 2
    DeviceProtection = st.selectbox("DeviceProtection",("No", "Yes", "No internet service"))
    if DeviceProtection == "No":
        DeviceProtection = 0
    elif DeviceProtection == "Yes":
        DeviceProtection = 1
    else:
        DeviceProtection = 2
    TechSupport = st.selectbox("TechSupport",("No", "Yes", "No internet service"))
    if TechSupport == "No":
        TechSupport = 0
    elif TechSupport == "Yes":
        TechSupport = 1
    else:
        TechSupport = 2
    StreamingTV = st.selectbox("StreamingTV",("No", "Yes", "No internet service"))
    if StreamingTV == "No":
        StreamingTV = 0
    elif StreamingTV == "Yes":
        StreamingTV = 1
    else:
        StreamingTV = 2
    StreamingMovies = st.selectbox("StreamingMovies",("No", "Yes", "No internet service"))
    if StreamingMovies == "No":
        StreamingMovies = 0
    elif StreamingMovies == "Yes":
        StreamingMovies = 1
    else:
        StreamingMovies = 2
    Contract = st.selectbox("Contract",("Month-to-month", "One year", "Two year"))
    if Contract == "Month-to-month":
        Contract = 0
    elif Contract == "One year":
        Contract = 1
    else:
        Contract = 2
    PaperlessBilling = st.selectbox("PaperlessBilling",("Yes", "No"))
    if PaperlessBilling == "Yes":
        PaperlessBilling = 0
    else:
        PaperlessBilling = 1
    PaymentMethod = st.selectbox("PaymentMethod",("Electronic check", "Mailed check", "Bank transfer(automatic)","Credit card (automatic)"))
    if PaymentMethod == "Electronic check":
        PaymentMethod = 0
    elif PaymentMethod == "Mailed check":
        PaymentMethod = 1
    elif PaymentMethod == "Bank transfer(automatic)":
        PaymentMethod = 2
    else:
        PaymentMethod = 3
    MonthlyCharges = st.number_input("Enter the monthly charges")
    TotalCharges = st.number_input("Enter the TotalCharges")
    Tenure = st.number_input("Enter the tenure month")
    if(Tenure>0 and Tenure<=12):
        Tenure = 0
    elif(Tenure>12 and Tenure <=24):
        Tenure = 1
    elif(Tenure>24 and Tenure <=36):
        Tenure = 2
    elif(Tenure>36 and Tenure <=48):
        Tenure = 3
    elif(Tenure>48 and Tenure<=60):
        Tenure = 4
    else:
        Tenure = 5
        
    input_data = {
        "gender": gender,
        "SeniorCitizen": SeniorCitizen,
        "Partner":  Partner,
        "Dependents": Dependents,
        "PhoneService": PhoneService,
        "MultipleLines": MultipleLines,
        "InternetService": InternetService,
        "OnlineSecurity": OnlineSecurity,
        "OnlineBackup": OnlineBackup,
        "DeviceProtection": DeviceProtection,
        "TechSupport": TechSupport,
        "StreamingTV": StreamingTV,
        "StreamingMovies": StreamingMovies,
        "Contract": Contract,
        "PaperlessBilling": PaperlessBilling,
        "PaymentMethod": PaymentMethod,
        "MonthlyCharges": MonthlyCharges,
        "TotalCharges": TotalCharges,
        "Tenure": Tenure
    }
    prediction = 0
    if st.button("Predict"):
        prediction = requests.post(url="http://127.0.0.1:8000/predict",data=json.dumps(input_data))
        prediction = prediction.json()
        p=prediction['prediction']
        if p == 1:
            st.write('You are likely to churn')
        else:
            st.write('You are less likely to churn')

if __name__=='__main__':
    main()