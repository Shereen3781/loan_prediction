import streamlit as st
import pandas as pd
import joblib
import sklearn
import category_encoders

Model = joblib.load("Model.pkl")
Inputs = joblib.load("Inputs.pkl")

def Make_Prdiction(Gender,Married,Dependents,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area):
    Pr_df = pd.DataFrame(columns=Inputs)
    Pr_df.at[0,"Gender"] = Gender
    Pr_df.at[0,"Married"] = Married
    Pr_df.at[0,"Dependents"] = Dependents
    Pr_df.at[0,"Education"] = Education
    Pr_df.at[0,"Self_Employed)"] = Self_Employed
    Pr_df.at[0,"ApplicantIncome"] = ApplicantIncome
    Pr_df.at[0,"CoapplicantIncome"] = CoapplicantIncome
    Pr_df.at[0,"LoanAmount"] = LoanAmount
    Pr_df.at[0,"Loan_Amount_Term"] = Loan_Amount_Term
    Pr_df.at[0,"Credit_History"] = Credit_History
    Pr_df.at[0,"Property_Area"] = Property_Area
    result = Model.predict(Pr_df)
    return result[0]
    
def main():
    st.title("Loan Prediction")
    Gender= st.selectbox("Gender",['Male', 'Female'])
    Married= st.selectbox("Married",['No', 'Yes'])
    Dependents= st.selectbox("Dependents",['0', '1', '2', '3+'])
    Education= st.selectbox("Education",['Graduate', 'Not Graduate'])
    Self_Employed= st.selectbox("Self_Employed",['No', 'Yes'])
    ApplicantIncome= st.slider("ApplicantIncome", min_value=150, max_value=81000, value=0, step=20)
    CoapplicantIncome= st.slider("CoapplicantIncome", min_value=0, max_value=42000, value=0, step=20)
    LoanAmount= st.slider("LoanAmount", min_value=9, max_value=700, value=0, step=20)
    Loan_Amount_Term= st.selectbox("Loan_Amount_Term",[360, 120, 240, 180, 60, 300, 480, 36, 84, 12])
    Credit_History= st.selectbox("Credit_History",[1,0])
    Property_Area= st.selectbox("Property_Area",['Urban', 'Rural', 'Semiurban'])

    if st.button("Predict"):
        Results = Make_Prdiction(Gender,Married,Dependents,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area)
        list_success = ["Your application is accepted" , "Your application is rejected"]
        st.text(list_success[Results])
main()
