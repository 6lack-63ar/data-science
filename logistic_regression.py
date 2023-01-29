# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 14:33:40 2023

@author: B3ar
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

data = pd.read_csv('https://raw.githubusercontent.com/dphi-official/Logistic-Regression/master/advertisement_data.csv')
#print(data.head())

data.info()
#data.describe()


#explatory data analysis



# Plotting histogram of the age variable
sns.set_style('whitegrid') # sets the style of the plots; it affects things like color of the axes, whether grid enabled or not.
data['Age'].hist(bins=30) # plots histogram with with bins = 30
plt.xlabel('Age') # labels the x - axis as 'Age'
plt.ylabel('Number of data points') # labels y - axis as 'Number of data points'

# Joint plot for 'Area Income' and 'Age'
# Plots two variables with bivariate and univariate graphs
sns.jointplot(x='Age',y='Area Income',data=data)

# Separate feature columns and target column
# We have freedom to chose features on which we want to train our model
X = data[['Daily Time Spent on Site', 'Age', 'Area Income','Daily Internet Usage', 'Male']] # feature columns
y = data['Clicked on Ad'] # target column
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)

print("Original shape of dataset: {}".format(data.shape)) # shape of original dataset
print("Shape of training dataset: {}".format(X_train.shape)) # shape of training dataset after split
print("Shape of testing dataset: {}".format(X_test.shape)) # shape of testing dataset after split


logmodel = LogisticRegression() # creating object 'logmodel' for LogisticRegression class
logmodel.fit(X_train,y_train) # Fitting the model
predictions = logmodel.predict(X_test) # predict for test data i.e. X_test

print(predictions)

# oututs prediction percentage from test data and the predictions made by the ml
print(accuracy_score(y_test,predictions))
