import streamlit as st
from churn import *
import matplotlib.pyplot as plt
import plotly.figure_factory as ff
import plotly.graph_objects as go
import seaborn as sns
import altair as alt

def show_correlations(dataframe, show_chart = True):
    fig = plt.figure()
    corr = dataframe.corr()
    if show_chart == True:
        sns.heatmap(corr, 
                    xticklabels=corr.columns.values,
                    yticklabels=corr.columns.values,
                    annot=False)
    return fig

def feature_importance(X, rf_model):
    feature_names = [f"feature {i}" for i in range(X.shape[1])]
    importances = rf_model.feature_importances_
    std = np.std([tree.feature_importances_ for tree in rf_model.estimators_], axis=0)
    forest_importances = pd.Series(importances, index=feature_names)
    fig, ax = plt.subplots()
    forest_importances.plot.bar(yerr=std, ax=ax)
    ax.set_title("Feature importances using MDI")
    ax.set_ylabel("Mean decrease in impurity")
    return fig

def aboutView():    
    
#--------------------------------------
    st.subheader("Correlations")
    st.write("Select the features that you need to see correlation")
    col1, col2, col3, col4 = st.columns(4)
    
    col = list(pre_processed_dataset_train.columns)
    correlation_df = show_correlations(pre_processed_dataset_train[col],show_chart=True)
    
    
    option = col1.selectbox(
        'Feature 1',
        (pre_processed_dataset_train.columns))   

    option2 = col2.selectbox(
        'Feature 2',
        (pre_processed_dataset_train.columns))
    
    result = pre_processed_dataset_train[option].corr(pre_processed_dataset_train[option2])
    
    if (result < 0.5):
        col3.metric("Correlation", "{:.2f}".format(result), "- low")
    else:
        col3.metric("Correlation", "{:.2f}".format(result), "+ high")
        
    
    with col4.expander(""):
        col4.write("See heatmap:")
        # col4.write(correlation_df)
        
#--------------------------------------
    st.subheader("Feature Analysis")
    st.write("Select the features that you need to see relation")
    col1, col2, col3, col4 = st.columns(4)
    
    option3 = col1.selectbox(
        'Graph type',
        ('Bar plot', 
         'Histogram', 
         'Line Chart', 
         'Area plot', 
         'Scatter plot')
    )   
        
    
    if (option3 == 'Bar plot'):
        option4 = col2.selectbox(
        'Feature 1:',
        (pre_processed_dataset_train.columns))  
        
        type = st.radio(
            "Do you want to plot 2 fetures?",
            ('No', 'Yes'))
        if type == 'No':
            st.bar_chart(pre_processed_dataset_train[option3])
        elif type == 'Yes':
            option5 = col3.selectbox(
            'Feature 2:',
            (pre_processed_dataset_train.columns))
            
            if (option4 != option5):
                chart_data = pd.DataFrame(columns=[option4, option5])
                st.bar_chart(chart_data)
            else:
                original_title = '<p style="font-family:Courier; color:red; font-size: 15px;">You cannot select the same feature</p>'
                st.markdown(original_title, unsafe_allow_html=True)

    elif (option3 == 'Histogram'):
        option4 = col2.selectbox(
        'Feature 1:',
        (pre_processed_dataset_train.columns))  
        
        type = st.radio(
            "Do you want to plot 2 fetures?",
            ('No', 'Yes'))
        if type == 'No':
            fig = ff.create_distplot(pre_processed_dataset_train[option4], option4, bin_size=[.1, .25, .5])
            st.plotly_chart(fig, use_container_width=True)
            
        elif type == 'Yes':
            option5 = col3.selectbox(
            'Feature 2:',
            (pre_processed_dataset_train.columns))
            
            if (option4 != option5):
                x1 = pre_processed_dataset_train[option4]
                x2 = pre_processed_dataset_train[option5]
                
                group_labels = [option4, option5]
                
                hist_data = [x1, x2]
                fig = ff.create_distplot(hist_data, group_labels, bin_size=[.1, .25, .5])
                st.plotly_chart(fig, use_container_width=True)
            else:
                original_title = '<p style="font-family:Courier; color:red; font-size: 15px;">You cannot select the same feature</p>'
                st.markdown(original_title, unsafe_allow_html=True)
        
    elif (option3 == 'Line Chart') :
        option4 = col2.selectbox(
        'Feature 1:',
        (pre_processed_dataset_train.columns))  
        
        type = st.radio(
            "Do you want to plot 2 fetures?",
            ('No', 'Yes'))
        if type == 'No':
            fig = ff.create_distplot(pre_processed_dataset_train[option4], option4)
            st.line_chart(fig)
            
        elif type == 'Yes':
            option5 = col3.selectbox(
            'Feature 2:',
            (pre_processed_dataset_train.columns))
            
            if (option4 != option5):
                # x1 = pre_processed_dataset_train[option4]
                # x2 = pre_processed_dataset_train[option5]
                group_labels = [option4, option5]
                
                chart_data = pd.DataFrame(columns=[option4, option5])
                fig = ff.create_distplot(chart_data, group_labels)
                st.plotly_chart(fig)
            else:
                original_title = '<p style="font-family:Courier; color:red; font-size: 15px;">You cannot select the same feature</p>'
                st.markdown(original_title, unsafe_allow_html=True)
        
    elif (option3 == 'Area plot'):
        st.area_chart(pre_processed_dataset_train)
        
        
    elif (option3 == 'Scatter plot'):
        option4 = col2.selectbox(
        'Feature 1:',
        (pre_processed_dataset_train.columns))  
        
        type = st.radio(
            "Do you want to plot 2 fetures?",
            ('No', 'Yes'))
        if type == 'No':
            fig = ff.create_distplot(pre_processed_dataset_train[option4], option4)
            st.map(fig)
            
        elif type == 'Yes':
            option5 = col3.selectbox(
            'Feature 2:',
            (pre_processed_dataset_train.columns))
            
            if (option4 != option5):
                # x1 = pre_processed_dataset_train[option4]
                # x2 = pre_processed_dataset_train[option5]
                group_labels = [option4, option5]
                chart_data = pd.DataFrame(columns=[option4, option5])
                fig = ff.create_distplot(chart_data, group_labels)
                st.map(fig)
            else:
                original_title = '<p style="font-family:Courier; color:red; font-size: 15px;">You cannot select the same feature</p>'
                st.markdown(original_title, unsafe_allow_html=True)
                

    
    # def plotGraph():
    #     st.write(pre_processed_dataset_train.plot(x=option, y=option2, kind="hist"))
    # st.button("Plot", on_click=plotGraph)
     
    st.subheader("Feature Analysis")   
    with st.expander(""):
        st.write("See feature importance:")
        st.write(feature_importance(X, rf_model))