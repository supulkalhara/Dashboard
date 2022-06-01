from pandas import DataFrame
from sklearn.datasets import load_wine
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
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
        st.markdown("Hello there! You can see the [GitHub Repository](https://github.com/tdenzl/BuLiAn) from here.")
        
    try:
                    
        st.subheader('Model Accuracy:')
        col1, col2, col3 = st.columns(3)
        col1.metric("Logistic Regression", "{:.2f}%".format(lr_accuracy*100), "-low" )
        col2.metric("Random Forest",  "{:.2f}%".format(rf_accuracy*100), "high")
        col3.metric("ADA Boost",  "{:.2f}%".format(ada_accuracy*100), "high")
        
        st.text("")
        no_churns = chatterbox.loc[chatterbox['Churn'] == 0]['account_length'].count()
        churns = chatterbox.loc[chatterbox['Churn'] == 1]['account_length'].count()
        col1, col2, col3, col4 = st.columns(4)
        
        col1.metric('Total: ', no_churns+churns)
        col2.metric('Available: ', no_churns)
        col3.metric('Churns: ', churns)
        col4.metric('Churn rate:', "{:.2f}%".format(churns/(no_churns+churns)*100))
        
        
        '''
        intertiol_plan,
        total_day_min,
        total_day_charge,
        customer_service_calls
        total_charge
        total_mins
        '''
        
        count_no_int_plan_no_churn = chatterbox.loc[(chatterbox['intertiol_plan'] == 0) & (chatterbox['total_intl_calls'] > 0) & (chatterbox['Churn'] == 0)]['account_length'].count()
        count_no_int_plan_yes_churn = chatterbox.loc[(chatterbox['intertiol_plan'] == 0) & (chatterbox['total_intl_calls'] > 0) & (chatterbox['Churn'] == 1)]['account_length'].count()
        count_yes_int_plan_no_churn = chatterbox.loc[(chatterbox['intertiol_plan'] == 1) & (chatterbox['total_intl_calls'] > 0) & (chatterbox['Churn'] == 0)]['account_length'].count()
        count_yes_int_plan_yes_churn = chatterbox.loc[(chatterbox['intertiol_plan'] == 1) & (chatterbox['total_intl_calls'] > 0) & (chatterbox['Churn'] == 1)]['account_length'].count()
        plt.figure()
        x=['no int plan no churn', 'no int plan churn', 'int plan no churn', 'int plan churn ']
        y=[count_no_int_plan_no_churn, count_no_int_plan_yes_churn, count_yes_int_plan_no_churn, count_yes_int_plan_yes_churn]
    
    
        data = pd.DataFrame({
            'index': x,
            'count': y,
        }).set_index('index')

        col1, col2 = st.columns(2)
        col2.write("")
        col2.write("")
        col2.write("")
        col2.write("Varience of churn with International plan")
        col2.bar_chart(data)
        
        
        
        with st.expander("variance of churn with features:"):
            option = col1.selectbox(
            'Categorical Feature:',
            (['location_code', 'intertiol_plan', 'voice_mail_plan'])) 
            
            plt.figure()
            
            if option == 'location_code':
                count_0 = chatterbox.loc[(chatterbox['Churn'] == 1) & (chatterbox[option] == 0)]['account_length'].count()
                count_1 = chatterbox.loc[(chatterbox['Churn'] == 1) & (chatterbox[option] == 1)]['account_length'].count()
                count_2 = chatterbox.loc[(chatterbox['Churn'] == 1) & (chatterbox[option] == 2)]['account_length'].count()

                x = ['445','452','547']
                y = [count_0, count_1, count_2]
                
            else:
                count_0 = chatterbox.loc[(chatterbox['Churn'] == 1) & (chatterbox[option] == 0)]['account_length'].count()
                count_1 = chatterbox.loc[(chatterbox['Churn'] == 1) & (chatterbox[option] == 1)]['account_length'].count()
                
                x = ['No','Yes']
                y = [count_0, count_1]
                
            data = pd.DataFrame({
                'index': x,
                'churn': y,
            }).set_index('index')
            
            col1.bar_chart(data)
        
                
    except URLError as e:
        st.error(
            """
            **This demo requires internet access.**

            Connection error: %s
        """
            % e.reason
    )