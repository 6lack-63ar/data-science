# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 13:49:34 2023

@author: B3ar
"""

#sample data set
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import linear_model


class_data ={
    
    
   
     'weight': [112, 123, 176, 145, 198, 211, 145, 181, 90, 101], 
                    'height': [181, 165, 167, 154, 181, 202, 201, 153, 142, 169],
                    'drinks alcohol': [0, 1, 1, 1, 0, 1, 1, 1, 0, 1],
                    'healthy': [0, 1, 1, 1, 0, 0, 1, 1, 1, 1]
    
    }



data = pd.DataFrame(class_data)
print(data.head())

x_data = data[['weight', 'height', 'drinks alcohol']]
y_data = data['healthy']
x_train, x_test, y_train, y_test = train_test_split(x_data, y_data ,test_size = 0.2, shuffle=False)

print(x_train.head())


linear_regression_model = linear_model.LinearRegression()
linear_regression_model.fit(x_train, y_train)

y_pred = linear_regression_model.predict(x_test)

print(y_pred)

