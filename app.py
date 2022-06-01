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
        
    #         st.altair_chart(chart, use_container_width=True)

