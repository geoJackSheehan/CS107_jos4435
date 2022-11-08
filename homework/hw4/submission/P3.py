#!/usr/bin/env python3
# File       : P3.py
# Description: Numerical approximation closures
# Copyright 2022 Harvard University. All Rights Reserved.
import numpy as np
import matplotlib.pyplot as plt


def approximate(f,eps):
    def closure(x):
        x = (f(x+eps)-f(x))/eps
        return x
    return closure


if __name__ == "__main__":
    x = np.arange(4,8.1,.1)/20
    eps = [1*10**-1,1*10**-7,1*10**-15]
    # I would have made this a loop for each eps value if we didn't have to change the line type in our plot. Since we do, I chose to do the 3 types separately, since I believe a loop would have made it more complicated
    approx1 = approximate(np.log,eps[0])(x)
    approx2 = approximate(np.log,eps[1])(x)
    approx3 = approximate(np.log,eps[2])(x)
    
    actual = 1/x
    
    plt.plot(x,approx1,label='$ \epsilon = 1$x$10^{-1} $')
    plt.plot(x,approx2,label='$ \epsilon = 1$x$10^{-7} $')
    plt.plot(x,approx3,label='$ \epsilon = 1$x$10^{-15} $')
    
    plt.plot(x,actual,label='analytical derivative',linestyle=':',color='black')
    plt.title("Compare $ f'_{FD}(x) $ at $\epsilon$ values and actual $f'(x) $")
    plt.xlabel('x')
    plt.ylabel(" $f'(x) $")
    plt.legend()
    plt.savefig('P3.png')
    
    wordsi = str(f"epsilon = {1*10**-7} most closely approximates the true derivative. \nFor values of epsilon that are too small, the line is not smooth due to precision errors. I think this is a result of rounding, and not using exact numbers. \nFor values of epsilon that are too large, the approximation is not close enough to be very accurate.")
    answeri = str('Answer to Q-i: \n' + wordsi)
    print(answeri)
    wordsii = str(f"By using the chain rule and breaking down the function into smaller derivatives that it can compute accurately, automatic differentiation is able to solve these problems without having to round results or make approximations.")
    answerii = str('\nAnswer to Q-ii: \n' + wordsii)
    print(answerii)
    
    plt.show()
    
