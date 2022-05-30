from urllib.error import URLError
from churn import *

import altair as alt
import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st

st.set_page_config(layout="wide")
 
row0_spacer1, row0_1, row0_spacer2, row0_2, row0_spacer3 = st.columns((.1, 2.3, .1, 1.3, .1))
with row0_1:
    st.title('Customer Churn Prediction Dashboard')
with row0_2:
    st.text("")
    st.subheader('By [Supul Pushpakumara](https://www.linkedin.com/in/supul-pushpakumara-323a38151)')
row3_spacer1, row3_1, row3_spacer2 = st.columns((.1, 3.2, .1))
with row3_1:
    st.markdown("Hello there! Have you ever spent your weekend watching the German Bundesliga and had your friends complain about how 'players definitely used to run more' ? However, you did not want to start an argument because you did not have any stats at hand? Well, this interactive application containing Bundesliga data from season 2013/2014 to season 2019/2020 allows you to discover just that! If you're on a mobile device, I would recommend switching over to landscape for viewing ease.")
    st.markdown("You can find the source code in the [GitHub Repository](https://github.com/tdenzl/BuLiAn)")
    
try:
    df = pre_processed_dataset_train
    with st.expander("See summary of the dataset"):
        st.write(chatterbox.describe())
        
    st.subheader('Accuracy')
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Logistic Regression", "50%", )
    col2.metric("Random Forest", "50%")
    col3.metric("XGB Classifier", "50%")
    col4.metric("R² Score", "0.98")
    
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
        
    # Every form must have a submit button.
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
            # st.write("acc_length", acc_length, 
            #          "location_code", location_code,
            #          "number_vm_messages", number_vm_messages,
            #          "total_day_min", total_day_min,
            #          "total_day_calls", total_day_calls,
            #          "total_day_charge", total_day_charge,
            #          "total_eve_min", total_eve_min,
            #          "total_eve_calls", total_eve_calls,
            #          "total_eve_charge", total_eve_charge,
            #          "total_night_minutes", total_night_minutes,
            #          "total_night_calls", total_night_calls,
            #          "total_night_charge", total_night_charge,
            #          "total_intl_minutes", total_intl_minutes,
            #          "total_intl_calls", total_intl_calls,
            #          "total_intl_charge", total_intl_charge,
            #          "customer_service_calls", customer_service_calls
            #          )

#         data = df.loc[countries]

#         data = data.T.reset_index()
#         data = pd.melt(data, id_vars=["index"]).rename(
#             columns={"index": "year", "value": "Gross Agricultural Product ($B)"}
#         )
#         chart = (
#             alt.Chart(data)
#             .mark_area(opacity=0.3)
#             .encode(
#                 x="year:T",
#                 y=alt.Y("Gross Agricultural Product ($B):Q", stack=None),
#                 color="Region:N",
#             )
#         )
#         st.altair_chart(chart, use_container_width=True)
except URLError as e:
    st.error(
        """
        **This demo requires internet access.**

        Connection error: %s
    """
        % e.reason
    )
