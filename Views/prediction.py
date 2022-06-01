from matplotlib.ft2font import HORIZONTAL
import streamlit as st
from churn import *


def churnPredict():
    with st.form("my_form"):
            st.write("Please fill out all the fields of this form")
        
            col1, col2, col3, col4 = st.columns(4)
            acc_length = col1.text_input("Account length: ")
            location_code = col1.text_input("Location code: ")
            number_vm_messages = col1.text_input("VM message count: ")
            total_day_min = col1.text_input("per Day minutes: ")
            total_day_calls = col2.text_input("per Day calls: ")
            total_day_charge = col2.text_input("per Day charge: ")
            total_eve_min = col2.text_input("per Eve minutes: ")
            total_eve_calls = col2.text_input("per Eve calls: ")
            total_eve_charge = col3.text_input("per Eve charge: ")
            total_night_minutes = col3.text_input("per Night minutes: ")
            total_night_calls = col3.text_input("per Night calls: ")
            total_night_charge = col3.text_input("per Night charge: ")
            total_intl_minutes = col4.text_input("International minutes: ")
            total_intl_calls = col4.text_input("International calls: ")
            total_intl_charge = col4.text_input("International charge: ")
            customer_service_calls = col4.text_input("Customer Service Calls: ")

            # slider_val = st.slider("Form slider")
            # checkbox_val = st.checkbox("Form checkbox")
            
            type = st.radio(
                "Select Model",
                ('Random Forest', 'Logistic Regression', 'ADA Boost'))
            if type == 'Random Forest':
                rf = True;
            elif type == 'Logistic Regression':
                rf = True;
            elif type == 'ADA Boost':
                rf = True;
            
        # Every form must have a submit button.
            try:
                submitted = st.form_submit_button("Submit")
                if submitted:
                    new_row = {acc_length, 
                            location_code, 
                            number_vm_messages,
                            total_day_min,
                            total_day_calls,
                            total_day_charge,
                            total_eve_min,
                            total_eve_calls,
                            total_eve_charge,
                            total_night_minutes,
                            total_night_calls,
                            total_night_charge,
                            total_intl_minutes,
                            total_intl_calls,
                            total_intl_charge,
                            customer_service_calls}
                    
                    prediction = rf_model.predict(new_row)
                    if prediction == 0:
                        churn = 'NO CHURN'
                    else:
                        churn = 'CHURN'
                        
                    st.write("Predicted Churn for the entered details:", 
                            churn)
            except:
                st.write("Input all!")