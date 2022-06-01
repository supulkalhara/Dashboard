# -*- coding: utf-8 -*-
"""Introduction_to_Data_Science.ipynb
Original file is located at
    https://colab.research.google.com/drive/18JrI7VKT5de6daZ9sAgHd1cxx2M1PaGo

# **Data Pre-processing**
"""
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import AdaBoostClassifier
from sklearn import metrics
from sklearn.model_selection import train_test_split

import pandas as pd
import numpy as np


def iqr(df , features):
  for f in features:
    mean = df[f].mean()
    Q1 = df[f].quantile(0.25)
    Q3 = df[f].quantile(0.75)
    IQR = Q3 - Q1
    lower_range = Q1 - (1.5 * IQR)
    upper_range = Q3 + (1.5 * IQR)
    df[f] = np.where(df[f] <lower_range,lower_range ,df[f])
    df[f] = np.where(df[f] >upper_range, upper_range,df[f])
  return df


# RandomForestClassifier
def random_forest(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=101)
    model_rf = RandomForestClassifier(n_estimators=1000 , 
                                      oob_score = True, 
                                      n_jobs = -1,
                                      random_state =50, 
                                      max_features = "auto",
                                      max_leaf_nodes = 30)
    model_rf.fit(X_train, y_train)
    preds = model_rf.predict(X_test)
    return model_rf, metrics.accuracy_score(y_test, preds)
  
  
# LogisticRegression
def logistic_regression(X, y):
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)
  model = LogisticRegression()
  result = model.fit(X_train, y_train)
  prediction_test = model.predict(X_test)
  return prediction_test, metrics.accuracy_score(y_test, prediction_test)


#ADA Boost
def ada_boost(X, y):
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=99)
  model = AdaBoostClassifier()
  model.fit(X_train,y_train)
  preds = model.predict(X_test)
  return preds, metrics.accuracy_score(y_test, preds)


"""## **Load CSV**"""
chatterbox = pd.read_csv('Train_Dataset.csv')
chatterbox_test = pd.read_csv('Test_Dataset.csv')

"""## **Data Cleaning**"""
customer_id_temp = chatterbox['customer_id']
customer_id_temp_test = chatterbox_test['customer_id']
chatterbox = chatterbox.drop(columns=['customer_id', 'Unnamed: 20'])
chatterbox_test = chatterbox_test.drop(columns=['customer_id', 'Unnamed: 19', 'Unnamed: 20'])
obj_features = ['location_code', 'intertiol_plan' , 'voice_mail_plan' , 'Churn']
num_features = list(set(chatterbox.columns) - set(obj_features))

chatterbox = chatterbox.drop_duplicates()
chatterbox_test = chatterbox_test.drop_duplicates()

for f in num_features:
  chatterbox[f] = np.where(chatterbox[f] < 0, np.NaN , chatterbox[f])
  chatterbox_test[f] = np.where(chatterbox_test[f] < 0, np.NaN , chatterbox_test[f])
chatterbox = chatterbox.dropna()
chatterbox_test = chatterbox_test.dropna()

rem_features = ['total_day_min', 'total_day_calls', 'total_day_charge', 
                'total_eve_min', 'total_eve_calls', 'total_eve_charge', 
                'total_night_minutes', 'total_night_calls', 'total_night_charge', 
                'total_intl_minutes', 'total_intl_calls', 'total_intl_charge']

chatterbox = iqr(chatterbox, rem_features)
chatterbox_test = iqr(chatterbox_test, rem_features)

# chatterbox = pd.concat([customer_id_temp, chatterbox], axis=1).reindex(chatterbox.index)
# chatterbox_test = pd.concat([customer_id_temp_test, chatterbox_test], axis=1).reindex(chatterbox_test.index)

chatterbox['intertiol_plan'].replace(to_replace='yes', value=1, inplace=True)
chatterbox['intertiol_plan'].replace(to_replace='no',  value=0, inplace=True)

chatterbox['intertiol_plan'].replace(to_replace='yes', value=1, inplace=True)
chatterbox['intertiol_plan'].replace(to_replace='no',  value=0, inplace=True)

chatterbox['voice_mail_plan'].replace(to_replace='yes', value=1, inplace=True)
chatterbox['voice_mail_plan'].replace(to_replace='no',  value=0, inplace=True)

chatterbox['voice_mail_plan'].replace(to_replace='yes', value=1, inplace=True)
chatterbox['voice_mail_plan'].replace(to_replace='no',  value=0, inplace=True)

chatterbox['Churn'].replace(to_replace='Yes', value=1, inplace=True)
chatterbox['Churn'].replace(to_replace='No',  value=0, inplace=True)

chatterbox['location_code'].replace(to_replace=445.0, value=0, inplace=True)
chatterbox['location_code'].replace(to_replace=452.0,  value=1, inplace=True)
chatterbox['location_code'].replace(to_replace=547.0,  value=2, inplace=True)

chatterbox['total_mins'] = chatterbox['total_day_min'] + chatterbox['total_eve_min'] + chatterbox['total_night_minutes']
chatterbox['total_calls'] = chatterbox['total_day_calls'] + chatterbox['total_eve_calls'] + chatterbox['total_night_calls']
chatterbox['total_charge'] = chatterbox['total_day_charge'] + chatterbox['total_eve_charge'] + chatterbox['total_night_charge']
chatterbox['avg_min_per_call'] = chatterbox['total_mins']  / chatterbox['total_calls']

num_features = list(set(chatterbox.columns) - set(obj_features))
pre_processed_dataset_train = chatterbox
pre_processed_dataset_test = chatterbox_test
# student_id = "190482K.csv"

# pre_processed_dataset_train.to_csv("Train_Dataset_"+student_id, index=False)
# pre_processed_dataset_test.to_csv("Test_Dataset_"+student_id, index=False)



y = chatterbox['Churn']
X = chatterbox.drop(columns=['Churn'])



rf_model, rf_accuracy = random_forest(X, y)
lr_model, lr_accuracy = logistic_regression(X, y)
ada_model, ada_accuracy = ada_boost(X, y)
