from sklearn.datasets import load_wine
import streamlit as st
from urllib.error import URLError
from churn import *


def homeView():
    row0_spacer1, row0_1, row0_spacer2, row0_2, row0_spacer3 = st.columns((.1, 2.3, .1, 1.3, .1))
    with row0_1:
        st.title('Customer Churn Prediction Dashboard')
    with row0_2:
        st.text("")
        st.subheader('By [Supul Pushpakumara](https://www.linkedin.com/in/supul-pushpakumara-323a38151)')
        
    row3_spacer1, row3_1, row3_spacer2 = st.columns((.1, 3.2, .1))
    with row3_1:
        st.markdown("Hello there!  [GitHub Repository](https://github.com/tdenzl/BuLiAn)")
        
    try:
        df = pre_processed_dataset_train
        with st.expander("See summary of the dataset"):
            st.write(df.describe())
            
        st.subheader('Accuracy')
        col1, col2, col3 = st.columns(3)
        col1.metric("Logistic Regression", "{:.2f}%".format(lr_accuracy*100), "-low" )
        col2.metric("Random Forest",  "{:.2f}%".format(rf_accuracy*100), "high")
        col3.metric("ADA Boost",  "{:.2f}%".format(ada_accuracy*100), "high")
        
    except URLError as e:
        st.error(
            """
            **This demo requires internet access.**

            Connection error: %s
        """
            % e.reason
    )