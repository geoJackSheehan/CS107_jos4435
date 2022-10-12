#!/usr/bin/env python3
# File       : P3e.py
# Description: Regression base class
# Copyright 2022 Harvard University. All Rights Reserved.

# imports
from sklearn import datasets
from sklearn.model_selection import train_test_split
from P3a import Regression as reg
from P3c import LinearRegression as linreg
from P3d import RidgeRegression as ridgereg

# data and model setup
dataset = datasets.fetch_california_housing() # use the california housing dataset from sklearn
X_train,X_test,y_train,y_test = train_test_split(dataset['data'],dataset['target'],test_size=0.2,random_state=42) # split dataset into training set and test set with 80%-20% training-test split 
ols_model = linreg() # instantiate LinearRegression object
ridge_model = ridgereg() # instantiate RidgeRegression object
ridge_model.set_params(alpha=0.1) 
models = [ols_model,ridge_model] # list the models

# calculations
scores = [] # empty scores container
for model in models: # compute the best fit coefficients for each model
    model.fit(X_train, y_train)
    score = model.score(X_test,y_test)
    scores.append(score) # add values to container
    print(f"{model.__class__.__name__} R-squared: "+str(score)) # print R^2 statistic
    print(model.get_params())
