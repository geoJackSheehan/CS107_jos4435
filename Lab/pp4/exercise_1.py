#!/usr/bin/env python3

# Worked with Chiara Chung-Halpern and Annabel Yim

# Imports
import numpy as np

# Functions
def make_layer(shape,activation):
    def layer(inputs,weights,bias):
        out = activation(inputs*weights + bias)
        return out
    return layer

# Test
shape1=(1,100) # [number of inputs, number of neural units]
shape2=(1,100)
activation1=np.tanh # activation function
activation2=np.tanh
layer1=make_layer(shape1,activation1)
layer2=make_layer(shape2,activation2)
weight1=np.random.rand(shape1[0],shape1[1]) # matrix of size shape
weight2=np.random.rand(shape2[0],shape2[1])
bias1=np.random.rand(1,shape1[1]) # vector of size shape[1]
bias2=np.random.rand(1,shape2[1])
inputs = [np.random.uniform(0,1,100).reshape(1,-1)] #100 neural units
outputs = layer2(layer1(inputs,weight1,bias1),weight2,bias2) # layer 1 runs using input, then is input to layer 2
print(outputs)
