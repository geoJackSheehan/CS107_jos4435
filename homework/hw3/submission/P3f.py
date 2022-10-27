#!/usr/bin/env python3
# File       : P3f.py
# Description: Compare models' performances
# Copyright 2022 Harvard University. All Rights Reserved.

# imports
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from P3a import Regression as reg
from P3c import LinearRegression as linreg
from P3d import RidgeRegression as ridgereg

# data and model setup
dataset = datasets.fetch_california_housing()
X_train,X_test,y_train,y_test = train_test_split(dataset['data'],dataset['target'],test_size=0.2,random_state=42) # split dataset into training set and test set with 80%-20% training-test split 
ols_model = linreg() # instantiate LinearRegression object
ridge_model = ridgereg() # instantiate RidgeRegression object
alphas=np.arange(0,1.1,0.1) # varying alpha values with which to compare models 
ols_model.fit(X_train,y_train)
ols_model_scores = [ols_model.score(X_test,y_test)]*len(alphas)

# calculations
ridge_model_scores = [] # empty ridge scores container
for alpha in alphas:
    ridge_model.set_params(alpha=alpha)
    ridge_model.fit(X_train,y_train)
    score = ridge_model.score(X_test,y_test)
    ridge_model_scores.append(score) # add values to container

# plot details
plt.xlabel(r'$ \alpha $')
plt.ylabel(r'$ R^2 $ statistic')
plt.title('Model Comparison for California Housing Dataset')
# plot
line1 = plt.plot(alphas,ols_model_scores,label='Linear Regression')
line2 = plt.plot(alphas,ridge_model_scores,label='Ridge Regression')
plt.legend(loc='lower left')
plt.savefig('P3f.png')
plt.show()
