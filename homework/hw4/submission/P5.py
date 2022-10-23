#!/usr/bin/env python3
# File       : P5.py
# Description: Dual number with support for addition and multiplication
# Copyright 2022 Harvard University. All Rights Reserved.

class DualNumber:
    """Simple dual number object (lecture 12)
       Notes About Dual Numbers:
           -> adding: adding functions in the real part and adding derivatives in the dual part
           -> multiplying: multiplying functions in the real part and the product rule for derivatives in the dual part"""
    _supported_scalars = (int,float)
    
    def __init__(self,real,dual=1.0): # dual=1.0 comes from seed vector (p) = 1 to compute derivative. dual part initialized so df/dx results in dual part if dual number used in f
            self.real = real
            self.dual = dual
    
    def __add__(self,other):
        if not isinstance(other,(*self._supported_scalars, DualNumber)):
            raise TypeError("Type not supported: must be int or float")
        if isinstance(other,self._supported_scalars):
            return DualNumber(other+self.real,self.dual)
        else:
            return DualNumber(self.real+other.real,self.dual+other.dual)
        
    def __radd__(self,other):
        return self.__add__(other)
    
    def __mul__(self,other):
        if not isinstance(other,(*self._supported_scalars, DualNumber)):
            raise TypeError("Type not supported: must be int or float") 
        if isinstance(other,self._supported_scalars):
            return DualNumber(self.real*other.real,self.dual*other.real)
        else:
            return DualNumber(self.real*other.real,self.real*other.dual+other.real*self.dual)
        
    def __rmul__(self,other):
        return self.__mul__(other)

if __name__ == "__main__":
    x1 = 0.5
    z = DualNumber(x1)
    a0 = 2.0; a1 = 2.5; a2 = 3.0
    f = a0 + a1 * z + z * a2 * z
    #f = a2 * z * z + a1 * z + a0
    #f=1+z*a0
    print(f.real); print(f.dual)