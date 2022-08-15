import pandas as pd
import numpy as np
from sklearn.preprocessing import *
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn import metrics               
from sklearn import preprocessing
from sklearn import utils
from sklearn.metrics import mean_absolute_error


def pps(df1,categorical_features=None,numerical_features=None):
    df=df1.fillna(value=df1.interpolate())
    df=df.fillna(value=df.mode())
    columns = ["Feature", "Target","PPS", "Type of Prediction", "Cross-Val Score", "Training Score","Naive-Baseline Score", "Model"]
    pps_df=pd.DataFrame(columns=columns)
    for i in df.columns:
        for j in df.columns:
            if(((categorical_features)!=None and j in categorical_features) or type(df[j])==str):
                model = DecisionTreeClassifier()
                lab_enc = preprocessing.LabelEncoder()
                label_encoded_y = np.array(lab_enc.fit_transform(df[j])).reshape(-1,1)
                x_train,x_test,y_train,y_test = train_test_split(np.array(df[i]).reshape(-1,1),label_encoded_y)
                model.fit(x_train,y_train)
                y_pred=model.predict(x_test)
                mode = np.full((len(x_test),1),df[j].mode())
                f1 = 0
                f1_naive=0
                if(df[j].unique().shape[0]>2):
                    f1 = metrics.f1_score(y_test,y_pred,average='weighted')
                    f1_naive = metrics.f1_score(y_test,mode,average='weighted')
                else:
                    f1=metrics.f1_score(y_test,y_pred)
                    f1_naive = metrics.f1_score(y_test,mode)
                pps_score=max(0,(f1-f1_naive)/(1 - f1_naive))
                cv_score=model.score(x_test,y_test)
                train_score=model.score(x_train,y_train)
                pps_df = pps_df.append({"Feature":i,"Target":j,"PPS":pps_score,"Type of Prediction":"Classification","Cross-Val Score":cv_score,"Training Score":train_score,"Naive-Baseline Score":f1_naive,"Model":"DecisionTreeClassifier()"},ignore_index=True)
            else:
                model = DecisionTreeRegressor()
                # lab_enc = preprocessing.LabelEncoder()
                # label_encoded_y = np.array(lab_enc.fit_transform(df[j])).reshape(-1,1)
                x_train,x_test,y_train,y_test = train_test_split(np.array(df[i]).reshape(-1,1),np.array(df[j]).reshape(-1,1))
                model.fit(x_train,y_train)
                median = np.full((len(x_test),1),df[j].median())
                naive_mae = metrics.mean_absolute_error(y_test, median)
                y_pred=model.predict(x_test)
                mae=metrics.mean_absolute_error(y_test,y_pred)
                train_score=mean_absolute_error(y_train,model.predict(x_train))
                pps_score = max(0,1 - mae/naive_mae)
                pps_df=pps_df.append({"Feature":i,"Target":j,"PPS":pps_score,"Type of Prediction":"Regression","Cross-Val Score":mae,"Training Score":train_score,"Naive-Baseline Score":naive_mae,"Model":"DecisionTreeRegressor()"},ignore_index=True)
    return pps_df