import numpy as np 

def add(x, y):
    """This is an add function"""
    return x + y

def numpy_add(x, y):    
    return x + y 


print(add(1, 1))

print(add(2, 1))

print(numpy_add(np.arange(4), np.arange(4)))