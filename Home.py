import streamlit as st
from st_pages import Page, show_pages

def main():
    st.set_page_config(page_title="MLCenter", page_icon=":bank:")
    left_co, cent_co,last_co = st.columns([1,5,1])
    with cent_co:
        st.image("img/logo.png")
        hide_img_fs = '''
            <style>
            button[title="View fullscreen"]{
                visibility: hidden;}
            </style>
            '''

        st.markdown(hide_img_fs, unsafe_allow_html=True)
    
    st.write(
    """ 
    MLCenter is a Predictive Analytics Hub, currently featuring two robust models specializing in credit risk prediction and fraudulent transactions detection. 
    Users can seamlessly submit data through our user-friendly interface, obtaining real-time predictions that empower informed decision-making in financial 
    transactions.
    
    Looking ahead, MLCenter is set to introduce insightful features, including a dive into the training data's intricacies, providing users with a deeper 
    understanding of the models. Additionally, forthcoming updates will offer comprehensive statistics on new predictions, allowing users to explore trends, 
    success rates, and performance metrics, further enriching their grasp of the predictive analytics landscape. Stay connected with MLCenter as we continue 
    to evolve, equipping users with actionable insights and a centralized platform for their predictive analytics needs.
    """
    )

    with st.sidebar: 
        show_pages(
        [
            Page("Home.py", "Home", ":bank:"),
            Page("pages/1_Fraud_Detection.py", "Fraud Detection", ":credit_card:"),
            Page("pages/2_Credit_Risk.py", "Credit Risk", ":chart_with_upwards_trend:"),
        ])
        st.image("img/logo.png")
        hide_img_fs = '''
            <style>
            button[title="View fullscreen"]{
                visibility: hidden;}
            </style>
            '''

        st.markdown(hide_img_fs, unsafe_allow_html=True)
        st.markdown("This is a portfolio project by Felipe Martins. If you want to see the code of this app and other data science projects check my [GitHub](https://github.com/felipebita).")

if __name__ == '__main__':
    main()