#!/usr/bin/env python3
# File       : P3c.py
# Description: LinearRegression derived class
# Copyright 2022 Harvard University. All Rights Reserved.

# imports
import numpy as np
from P3a import Regression 

# LinearRegression class
class LinearRegression(Regression): # inherit from Regression

    # calculations
    def fit(self, X, y): # generate fit function for OLS
        X_0 = np.ones((len(X), 1)) # introduce artifical column of ones to increase parameter space by 1
        total_X = np.append(np.array(X), X_0, axis=1)
        X_T = np.transpose(total_X) # matrix transpose
        X_product = np.dot(X_T,total_X)  # matrix multiplication
        beta_hat = np.dot(np.dot(np.linalg.pinv(X_product), X_T), y) # matrix multiplication with inverse matrix to solve for beta_hat
        beta = beta_hat[:-1]
        beta_0 = beta_hat[-1]
        self.params['coefficient'] = beta # store in params dictionary
        self.params['intercept'] = beta_0
