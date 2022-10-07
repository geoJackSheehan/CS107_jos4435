#!/usr/bin/env python3
# File       : exercise_1.py
# Created    : oct 4
# Coder      : Haoxue, Jack
# Listener   : Sarah
# Sharer     : Shirley

import numpy as np

class Layer:

	def __init__(self,shape,activation):
		self.activation = activation
		self.weights=np.random.uniform(0,1,shape[0]*shape[1]).reshape(shape)
		self.bias = np.random.normal(0,1,shape[1]).reshape(1,-1).transpose()


	def __call__(self,inputs):

        #check dimensions
        	try:
            		assert len(inputs) == self.weights.shape[0]
        	except:
            		raise Exception("Inputs do not have the correct length")
        #try:
        #    assert self.weights.shape == self.shape
        #except:
        #    raise Exception("Weights do not have correct shape")
        #try:
        #    assert len(self.bias)==self.weights.shape[1]
        #except:
        #    raise Exception("Bias does not have correct length")


        	result=self.activation(self.weights.transpose().dot(inputs)+self.bias)
        	return np.array(result)

	def __repr__(self):
		class_name = type(self).__name__
		instance_state = self.state
		return f"{class_name}({instance_state})"

	def __str__(self):
		"""String representation for user-level pretty print"""
		class_name = type(self).__name__
		instance_state = self.state
		return f"An instance of {class_name} with self.state={instance_state}"

if __name__ == "__main__":

	#define activation function
	sigmoid = lambda x: 1./(1+np.exp(-x))

	shape1=(4,3)
	shape2=(3,5)

	#define network layers
	layer1 = Layer(shape1,sigmoid)
	layer2 = Layer(shape2,sigmoid)

	inputs=np.random.uniform(0.0, 1.0, 4).reshape(-1,1)
	# Run inputs through the network
	print('NN output dimensions: ',layer2(layer1(inputs)))
	print('print str: ', print(layer2(layer1(inputs))))
	print('repr result: ', repr(layer1(inputs)))
	print('repr result 2: ', repr(layer2(layer1(inputs))))
	#print('eval result: ', eval(repr(layer1(inputs))))

	# the following line does not working saying that 'array is not defined'. we reason that this is a problem related to numpy library and we did not go into it
	#repr_result = eval(repr(layer1(inputs)))
	#repr(repr_result)

	print("Test for exceptions: weights do not have correct shape")
	shape1=(4,3)
	shape2=(3,5)
