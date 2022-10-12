#!/usr/bin/env python3
# File       : P3d.py
# Description: RidgeRegression derived class
# Copyright 2022 Harvard University. All Rights Reserved.

#imports 
import numpy as np
from P3c import LinearRegression

# RidgeRegression class
class RidgeRegression(LinearRegression): # inherit from LinearRegression
    
    # calculations
    def fit(self,X,y): # generate fit function for Ridge
        X_0 = np.ones((len(X),1)) # introduce artifical column of ones to increase parameter space by 1
        total_X = np.append(np.array(X),X_0,axis=1)
        X_T = np.transpose(total_X) # matrix transpose
        X_product = np.dot(X_T,total_X) # matrix multiplication
        gamma = self.params['alpha']*np.identity(len(total_X[0])) # gamma equals alpha * identity matrix
        gamma_T = np.transpose(gamma) # matrix transpose
        gamma_product = np.dot(gamma_T,gamma) # matrix multiplication
        beta_hat = np.dot(np.dot(np.linalg.pinv(X_product+gamma_product),X_T),y) # matrix multiplication with inverse matrix to solve for new beta_hat
        beta = beta_hat[:-1]
        beta_0 = beta_hat[-1]
        self.params['coefficient'] = beta # store in params dictionary
        self.params['intercept'] = beta_0           

    def set_params(self,**kwargs): # set the regularization coefficient alpha
        self.params['alpha'] = kwargs['alpha']   
