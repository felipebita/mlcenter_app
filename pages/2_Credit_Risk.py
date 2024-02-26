import streamlit as st
import pandas as pd
import requests

def main():
    st.set_page_config(page_title="Credit Risk Prediction", page_icon=":chart_with_upwards_trend:")
    with st.sidebar:
        st.image("img/logo.png")
        st.markdown("This is a portfolio project by Felipe Martins. If you want to see the code of this app and other data science projects check my [GitHub](https://github.com/felipebita).")
    
    st.header("Credit Risk Prediction")
    
    with st.expander('Information'):
        st.write(
            """ 
            The model implemented in this tool is the result of a portfolio project. The complete report on data processing, analysis, modeling and evaluation can be found in the following repository: [Credit Risk Modeling](https://github.com/felipebita/credit_risk).  
            """
            )
        
    st.write("Inser the borrower's information to get the prediction.")
    
    loan_amount = st.number_input("Loan Amount",min_value= 1.00)
    person_age = st.number_input("Person Age",min_value = 1)
    person_income = st.number_input("Person Income",min_value = 1.00)
    employ_length = st.number_input("Employment Length",min_value = 1)
    loan_percent_inc = st.number_input("Loan/income rate",min_value = 0.00, max_value=1.00)
    loan_intrate = st.number_input("Interest Rate (%)",min_value = 1.00)
    loan_grade = st.selectbox("Loan Grade ('A'=1,'G'=7)",(1, 2, 3, 4, 5, 6, 7))
    cred_hist_length = st.number_input("Credit History Length",min_value = 1)
    default_file = st.selectbox('Default on File',('Yes', 'No'))
    home_owner = st.selectbox('Home Ownership',('Own', 'Mortgage', 'Rent', 'Other'))
    loan_intent = st.selectbox('Loan Intent',('Education', 'Medical', 'Venture', 'Personal', 'Home Improvement', 'Debt Consolidation'))

    data = {'personage': person_age,
            'personincome': person_income,
            'personhomeownershipOWN':1 if home_owner == 'Own' else 0,
            'personhomeownershipMORTGAGE':1 if home_owner == 'Mortage' else 0, 
            'personhomeownershipRENT':1 if home_owner == 'Rent' else 0, 
            'personhomeownershipOTHER':1 if home_owner == 'Other' else 0, 
            'personemplength':employ_length,
            'loanintentEDUCATION':1 if loan_intent == 'Education' else 0,
            'loanintentMEDICAL':1 if loan_intent == 'Medical' else 0,
            'loanintentVENTURE':1 if loan_intent == 'Venture' else 0,
            'loanintentPERSONAL':1 if loan_intent == 'Personal' else 0,
            'loanintentHOMEIMPROVEMENT':1 if loan_intent == 'Home Improvement' else 0,
            'loanintentDEBTCONSOLIDATION':1 if loan_intent == 'Debt Consolidation' else 0,
            'loangrade':loan_grade,
            'loanamnt':loan_amount,
            'loanintrate':loan_intrate,
            'loanpercentincome':loan_percent_inc,
            'cbpersondefaultonfileN':1 if default_file == 'N' else 0,
            'cbpersondefaultonfileY':1 if default_file == 'Y' else 0,
            'cbpersoncredhistlength':cred_hist_length}
    
    column_names= data.keys()
    df = pd.DataFrame(data,columns = column_names, index=[0])
    st.write('This data is going to be sent to the model. Check if it is right.')
    st.table(df) 

    if st.button('Get Prediction'):
        with st.spinner("Processing"):
            api_url = "https://api-cr-waxugbmvta-uc.a.run.app/predict"  # Replace with your FastAPI server's URL
            response = requests.post(api_url, json=data)
            if response.status_code == 200:
                st.write("Credit Risk:", response.json().get("Credit Risk"))
            else:
                st.error("Error making API request")   
            

if __name__ == '__main__':
    main()