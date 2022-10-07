#!/usr/bin/env python3
# File       : exercise_2.py
# Created    : oct 4
# Coder      : Haoxue, Jack
# Listener   : Sarah
# Sharer     : Shirley

from exercise_1 import Layer
import matplotlib.pyplot as plt
import numpy as np

class Linear(Layer):
	def __init__(self, shape):
		linear = lambda x: x
		super().__init__(shape, linear)
	
	def update(self, weights, bias):
		self.weights = weights
		self.bias = bias

class Autoencoder():
	def __init__(self, shape):
		self.encoder = Linear(shape)
		self.decoder = Linear([shape[1],shape[0]])
	def encode(self, inputs):
		return self.encoder(inputs)
	def decode(self, code):
		return self.decoder(code)

	@classmethod
	def from_pretrained(cls, encoder_weight, encoder_bias, decoder_weight, decoder_bias):
		# assert the encoder shape vs. decoder shape
		ae = cls(encoder_weight.shape)
		ae.encoder.update(encoder_weight, encoder_bias)
		ae.decoder.update(decoder_weight, decoder_bias)
		return ae
    
data = np.load('autoencoder.npz')
test_digit, enc_w, enc_b, dec_w, dec_b = [data[x] for x in data.files] 

ae = Autoencoder.from_pretrained(enc_w, enc_b, dec_w, dec_b)

recon = ae.decode(ae.encode(test_digit[0])) # encode/decode pass 
fig, ax = plt.subplots(1, 2, sharex=True, sharey=True) 
ax[0].imshow(test_digit[0].reshape(28, 28), cmap='gray_r') 
ax[1].imshow(recon.reshape(28, 28), cmap='gray_r')
plt.show()
fig.savefig('test_digit.png', bbox_inches='tight')
