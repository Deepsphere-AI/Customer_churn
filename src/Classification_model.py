import streamlit as st
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier

def Classification_models(vAR_input_model_type):
    w1,col1,col2,w2= st.columns((1.5,3,4,.1))
    cc2,cc1,cc3=st.columns((1.5,7,.1))
    w11,col11,col22,w22= st.columns((1.5,3,4,.1))
    w111,col111,col222,w222= st.columns((1.5,3,4,.1))
    cc22,cc11,cc33=st.columns((1.5,7,.1))
    w1111,col1111,col2222,w2222= st.columns((1.5,3,4,.1))
    cc222,cc111,cc333=st.columns((1.5,7,.1))
    with col1:
        st.write("### ")
        st.write("## ")
        st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Training data upload</span></p>", unsafe_allow_html=True)
    with col2:
        vAR_input_training_data = st.file_uploader(' ',key='train')
        if vAR_input_training_data is not None:
            training_data = pd.read_excel(vAR_input_training_data)
            with cc1:
                st.write("# ")
                st.write(training_data)
            with col22:
                if st.button("Train the Model"):
                    st.success("Training Process Completed")
            # Data Preprocessing for Training Data
            training_data['Purchase Date'] = pd.to_datetime(training_data['Purchase Date'], format='%m%d%Y')
            label_encoder = LabelEncoder()
            training_data['Product'] = label_encoder.fit_transform(training_data['Product'])
            training_data['Gender'] = label_encoder.fit_transform(training_data['Gender'])

            scaler = StandardScaler()
            numerical_cols = ['Quantity', 'Price', 'Service Call', 'Service Failure Rate%', 'Customer Lifetime(Days)']
            training_data[numerical_cols] = scaler.fit_transform(training_data[numerical_cols])

            # Separating features and target variable for Training Data
            X_train = training_data.drop(['CustomerID', 'Purchase Date', 'Service Start Date', 'Churn'], axis=1)
            y_train = training_data['Churn']

            # Model Training
            if vAR_input_model_type == 'Logistic Regression':
                rf_classifier = LogisticRegression(random_state=42)
            if vAR_input_model_type == 'Decision Trees':
                rf_classifier = DecisionTreeClassifier(random_state=42)
            if vAR_input_model_type == 'Random Forest':
                rf_classifier = RandomForestClassifier(random_state=42)
            rf_classifier.fit(X_train, y_train)
            
            with col111:
                st.write("# ")
                st.write("# ")
                st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Test data upload</span></p>", unsafe_allow_html=True)
            with col222:
                vAR_input_test_data = st.file_uploader(' ',key='test')
            if vAR_input_test_data is not None:
                testing_data = pd.read_excel(vAR_input_test_data)
                with cc11:
                    st.write("# ")
                    st.write(testing_data)
                show_testing_data = pd.read_excel(vAR_input_test_data)
                with col1111:
                    st.write("# ")
                    st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Feature Selection</span></p>", unsafe_allow_html=True)
                with col2222:
                    vAR_input_feature_selection = st.multiselect(' ',testing_data.columns.values,key='fetureselection')
                if vAR_input_feature_selection != []:
                    # Data Preprocessing for Testing Data
                    testing_data['Product'] = label_encoder.fit_transform(testing_data['Product'])
                    testing_data['Gender'] = label_encoder.fit_transform(testing_data['Gender'])
                    testing_data[numerical_cols] = scaler.transform(testing_data[numerical_cols])

                    # Removing unwanted columns from Testing Data
                    X_test = testing_data.drop(['CustomerID', 'Purchase Date', 'Service Start Date', 'Reason for The customer to Churn / Non Churn'], axis=1)

                    # Predicting the target variable for Testing Data
                    y_pred_test = rf_classifier.predict(X_test)
                    with col2222:
                        if st.button("Test & Predict"):
                            with cc111:
                                selected_feature = show_testing_data[vAR_input_feature_selection]
                                selected_feature['Predicted'] = y_pred_test
                                st.write("# ")
                                st.write(selected_feature)