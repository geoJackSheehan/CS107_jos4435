#!/usr/bin/env python3
# File       : P3a.py
# Description: Regression base class
# Copyright 2022 Harvard University. All Rights Reserved.

import numpy as np

class Regression():

    def __init__(self):
        self.params = {} # emtpy dictionary

    def get_params(self):
        return self.params

    def set_params(self,**kwargs):
        raise NotImplementedError

    def fit(self,X,y):
        raise NotImplementedError

    def predict(self,X):
        X_0 = np.ones((len(X),1)) # introduce artifical column of ones to increase parameter space by 1
        total_X = np.append(np.array(X),X_0,axis=1)            
        prediction = np.dot(np.array(total_X),np.append(self.params['coefficient'],self.params['intercept'])) # vals in param dictionary
        return prediction

    def score(self,X,y):
        y_bar = sum(y)/len(y) # mean y
        y_pred = self.predict(X)
        SST = 0.0 # initial vals
        SSE = 0.0
        for i in range(len(y)): # calculate SST and SSE for each y
            SST += (y[i]-y_bar)**2
            SSE += (y[i]-y_pred[i])**2
        r_squared = 1-SSE/SST    
        return r_squared
