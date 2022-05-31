from churn import *
from Views import home,about,prediction


import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(layout="wide")

selected = option_menu(None, ["Home", "About Data", 'Predict'], 
    icons=['house', "bar-chart-line-fill", 'chevron-double-right'], 
    menu_icon="cast", default_index=0, orientation="horizontal",
    styles={
            "container": {"padding": "0!important"},
            "icon": {"color": "orange"}, 
            "nav-link": {"margin":"0px", "--hover-color": "#eee"},
        })

if selected == 'About Data':
    about.aboutView()
        
elif selected == 'Predict':
    prediction.churnPredict()
   
else:
    home.homeView()
        
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

