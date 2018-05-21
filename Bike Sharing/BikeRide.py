# -*- coding: utf-8 -*-
"""
Created on Thu May 10 20:15:57 2018

@author: M61958
"""

import numpy as np
import pandas as pd 

bikes = pd.read_csv('train.csv')
bikes_test = pd.read_csv('test.csv')

bikes.rename(columns = {'count' : 'Total' } , inplace=True )  

dt = bikes_test['datetime']

from sklearn.cross_validation import train_test_split
from sklearn.ensemble import RandomForestRegressor , GradientBoostingRegressor
from sklearn.metrics import mean_squared_error

temp = pd.DatetimeIndex(bikes['datetime'])
bikes['daysofweek'] = temp.dayofweek
bikes['hour'] = temp.hour
bikes["month"] = temp.month
bikes['year']= temp.year

temp_test = pd.DatetimeIndex(bikes_test['datetime'])
bikes_test['daysofweek'] = temp_test.dayofweek
bikes_test['hour'] = temp_test.hour
bikes_test["month"] = temp_test.month
bikes_test['year']= temp_test.year

import seaborn as sns
#sns.pairplot(bikes,x_vars=['season', 'weather','temp', 'humidity'],y_vars=['Total'],kind='reg' )
#sns.pairplot(bikes, x_vars=['holiday', 'workingday','atemp', 'windspeed'], y_vars=['Total'], kind='reg')
sns.heatmap(bikes.corr())

x = bikes.drop(['casual','registered','Total','datetime'],axis=1)
x.info()
y = bikes['Total']

new_y = np.log(y + 1)

X_train, X_test, y_train, y_test = train_test_split(x, new_y, test_size = 0.33, random_state = 42)
rf = RandomForestRegressor()
rf.fit(X_train, y_train)
prediction = rf.predict(X_test)
mean_squared_error(y_test, prediction) 

rf.fit(x, new_y)
bikes_test= bikes_test.drop(['datetime'],axis=1)
prediction = rf.predict(bikes_test)
prediction = np.exp(prediction) - 1

df=pd.DataFrame({'datetime':dt, 'count':prediction})
df
#sns.factorplot(data=bikes,x='weather',y='Total' , col ='season')