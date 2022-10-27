# worked with Annabel Yim

import numpy as np

p=np.array([1,0])
#p=[0,1]
#p=[1,1]
x=np.array([1,1])

class derivative:
    def __init__(self,Dpf=None):
        self.Dpf = Dpf
        
    def __call__(self,f):
        def closure(x,p):
            return [f(x),Dpf(x,p)]
        return closure
    

def Dpf(x,p):
    return np.dot(np.array([2*x[0],2*x[1]]),np.array(p))

@derivative(Dpf)
def f(x):
    return np.array([x[0]**2 + x[1]**2])

for p in np.transpose(p):
    print(f(x,p))
    
    
class DualNumber:
    def __init__(self,real,dual=1):
        self.real=real
        self.dual=dual
        
    def __add__(self,other):
        if not isinstance(other,(DualNumber,int,float)):
            raise TypeError('Wrong input type')
        if isinstance(other,(int,float)):
            other = DualNumber(other,0)
        return DualNumber(self.real+other.real,self.dual+other.dual)
    
    def __mul__(self,other):
        if not isinstance(other,(DualNumber,int,float)):
            raise TypeError('Wrong input type')
        if isinstance(other,(int,float)):
            other = DualNumber(other,0)
        return DualNumber(self.real*other.real,self.real*other.dual+self.dual*other.real)