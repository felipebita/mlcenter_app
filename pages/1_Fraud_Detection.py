import streamlit as st
import pandas as pd
import requests

def main():
    st.set_page_config(page_title="Fraud Detection", page_icon=":credit_card:")
    with st.sidebar:
        st.image("img/logo.png")
        st.markdown("This is a portfolio project by Felipe Martins. If you want to see the code of this app and other data science projects check my [GitHub](https://github.com/felipebita).")
    
    st.header("Fraud Detection")

    with st.expander('Information'):
        st.write(
            """ 
            The model implemented in this tool is the result of a portfolio project. The complete report on data processing, analysis, modeling and evaluation can be found in the following repository: [Fraudulent Transaction Detection](https://github.com/felipebita/fraud_detection).  
            """
            )
    
    st.write('Inser the data from the transaction to get the prediction.')
    amount = st.number_input("Transaction Amount",min_value = 1.00)
    old_bal_origin = st.number_input("Customer Old Balance",min_value = 1.00)
    new_bal_origin = st.number_input("Customer New Balance",min_value = 0.00)
    old_bal_dest = st.number_input("Recipient Old Balance",min_value = 0.00)
    new_bal_dest = st.number_input("Recipient New Balance",min_value = 1.00)
    category = st.selectbox('Category',('TRANSFER', 'CASH_OUT'))

    column_names = ['type_CASH_OUT', 'type_TRANSFER', 'amount', 'oldbalanceOrg', 'newbalanceOrig', 'oldbalanceDest', 'newbalanceDest']
    data = {'type_CASH_OUT': 0 if category == 'TRANSFER' else 1,
            'type_TRANSFER': 0 if category == 'CASH_OUT' else 1,
            'amount':amount,
            'oldbalanceOrg':old_bal_origin, 
            'newbalanceOrig':new_bal_origin, 
            'oldbalanceDest':old_bal_dest, 
            'newbalanceDest':new_bal_dest}
    
    df = pd.DataFrame(data,columns = column_names, index=[0])
    st.write('This data is going to be sent to the model. Check if it is right.')
    st.table(df) 

    if st.button('Get Prediction'):
        with st.spinner("Processing"):
            api_url = "https://api-fd-waxugbmvta-uc.a.run.app/predict"  
            response = requests.post(api_url, json=data)
            if response.status_code == 200:
                st.write("Prediction:", response.json().get("prediction"))
            else:
                st.error("Error making API request")   
            

if __name__ == '__main__':
    main()