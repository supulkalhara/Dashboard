import streamlit as st
from churn import *
import matplotlib.pyplot as plt
import plotly.figure_factory as ff
import plotly.graph_objects as go
import plotly.express as px
import seaborn as sns

def show_correlations(dataframe, show_chart = True):
    corr = dataframe.corr()
    if show_chart == True:
        fig = px.imshow(corr,
                        text_auto=True,
                        width=600,
                        height=600)
    return fig

def feature_importance(X, rf_model):
    importances = rf_model.feature_importances_
    st.write(X.columns)
    fig = px.bar(x=X.columns, y=importances)
    return fig

def aboutView():    
    
#--------------------------------------

    df = pre_processed_dataset_train
    with st.expander("See summary of the dataset"):
            st.write(df.describe())
            
            
    st.subheader("Correlations")
    st.write("Select the features that you need to see correlation")
    col1, col2, plots , col5 = st.columns((1, 0.5, 4, 3))
    
    col = list(pre_processed_dataset_train.columns)
    correlation_df = show_correlations(pre_processed_dataset_train[col],show_chart=True)
    
    
    option = col1.selectbox(
        'Feature 1',
        (pre_processed_dataset_train.columns))   

    option2 = col1.selectbox(
        'Feature 2',
        (pre_processed_dataset_train.columns))
    
    result = pre_processed_dataset_train[option].corr(pre_processed_dataset_train[option2])
    
    if (result < 0.5):
        col2.metric("Correlation", "{:.2f}".format(result), "- low")
    else:
        col2.metric("Correlation", "{:.2f}".format(result), "+ high")
        
    col5.plotly_chart(correlation_df, use_container_width=True)
        
#--------------------------------------
    col1.write("")
    col1.write("")
    col1.write("")
    col1.subheader("Feature Analysis")
    col1.write("Select the features that you need to see relation")
    # col1, col2, col3, col4 = st.columns(4)
    
    option3 = col1.selectbox(
        'Graph type',
        ('Bar plot', 
         'Histogram', 
         'Line Chart', 
         'Area plot', 
         'Scatter plot'
         ) # 
    )   
        
    
    if (option3 == 'Bar plot'):
        option4 = col1.selectbox(
        'Feature 1:',
        (num_features))  
        
        type = col1.radio(
            "Do you want to plot 2 fetures?",
            ('No', 'Yes'))
        if type == 'No':
            plots.bar_chart(pre_processed_dataset_train[option4])
        elif type == 'Yes':
            option5 = col1.selectbox(
            'Feature 2:',
            (num_features))
            
            if (option4 != option5):
    
                chart_data = [pre_processed_dataset_train[option4], pre_processed_dataset_train[option5]]
                plots.bar_chart(chart_data)
            else:
                original_title = '<p style="font-family:Courier; color:red; font-size: 15px;">You cannot select the same feature</p>'
                plots.markdown(original_title, unsafe_allow_html=True)

    elif (option3 == 'Histogram'):
        option4 = col1.selectbox(
        'Feature 1:',
        (num_features))  
        
        type = st.radio(
            "Do you want to plot 2 fetures?",
            ('No', 'Yes'))
        if type == 'No':
            fig = ff.create_distplot([pre_processed_dataset_train[option4]], [option4])
            plots.plotly_chart(fig, use_container_width=True)
            
        elif type == 'Yes':
            option5 = col1.selectbox(
            'Feature 2:',
            (num_features))
            
            if (option4 != option5):
                x1 = pre_processed_dataset_train[option4]
                x2 = pre_processed_dataset_train[option5]
                
                group_labels = [option4, option5]
                
                hist_data = [x1, x2]
                fig = ff.create_distplot(hist_data, group_labels, bin_size=[.1, .25, .5])
                plots.plotly_chart(fig, use_container_width=True)
            else:
                original_title = '<p style="font-family:Courier; color:red; font-size: 15px;">You cannot select the same feature</p>'
                st.markdown(original_title, unsafe_allow_html=True)
        
    elif (option3 == 'Line Chart') :
        option4 = col1.selectbox(
        'Feature 1:',
        (num_features))  

        option5 = col1.selectbox(
        'Feature 2:',
        (num_features))
        
        if (option4 != option5):
            x1 = pre_processed_dataset_train[option4]
            x2 = pre_processed_dataset_train[option5]
            group_labels = [option4, option5]
            
            chart_data = [x1, x2]
            fig = ff.create_distplot(chart_data, group_labels)
            plots.plotly_chart(fig)
        else:
            original_title = '<p style="font-family:Courier; color:red; font-size: 15px;">You cannot select the same feature</p>'
            st.markdown(original_title, unsafe_allow_html=True)
        
    elif (option3 == 'Area plot'):
        plots.area_chart(pre_processed_dataset_train)
        
    elif (option3 == 'Scatter plot'):
        option4 = col1.selectbox(
        'Feature 1:',
        (num_features))  
        
        option5 = col1.selectbox(
        'Feature 2:',
        (num_features))
        
        if (option4 != option5):
            x1 = pre_processed_dataset_train[option4]
            x2 = pre_processed_dataset_train[option5]
            group_labels = [option4, option5]
            fig = px.scatter(pre_processed_dataset_train,
                             x=option4,
                             y=option5,
            )
            plots.plotly_chart(fig)
        else:
            original_title = '<p style="font-family:Courier; color:red; font-size: 15px;">You cannot select the same feature</p>'
            plots.markdown(original_title, unsafe_allow_html=True)
                
    st.subheader("Feature Importance")   
    st.write("See feature importance using random forest:")
    fig = feature_importance(X, rf_model)
    st.plotly_chart(fig, use_container_width=True)