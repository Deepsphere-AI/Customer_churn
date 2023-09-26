import streamlit as st
from src.Classification_model import Classification_models
def prev1():
    st.session_state['preview1']="No"
def prev2():
    st.session_state['preview2']="No"
def prev3():
    st.session_state['preview3']="No"

def QuestionAnswering():
    w1,col1,col2,w2=st.columns((1.5,3,4,.1))
    cc2,cc1,cc3=st.columns((2,6,0.2))
    col11,col22,col33=st.columns((2,8,0.2))
    with col1:
        st.write("### ")
        st.write(" ")
        st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Problem Statement</span></p>", unsafe_allow_html=True)
    with col2:
        vAR_input_problem_type = st.selectbox(' ',['Select the Problem Statement','Customer Churn: Who is going to churn?','Customer Churn: When will the churn occur?','Customer Churn: Why does the churn occurs?'])
    if vAR_input_problem_type == 'Customer Churn: Who is going to churn?':
        with col1:
            st.write("## ")
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Problem type</span></p>", unsafe_allow_html=True)
        with col2:
            vAR_input_type = st.selectbox(' ',['Select','Classification','Clustring'])
        
        if vAR_input_type == 'Classification':
            with col1:
                st.write("# ")
                st.write(" ")
                st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Problem type</span></p>", unsafe_allow_html=True)
            with col2:
                vAR_input_model_type = st.selectbox(' ',['Select','Logistic Regression','Decision Trees','Random Forest'])
            if vAR_input_model_type != "Select":
                Classification_models(vAR_input_model_type)