# sigmoid.py

import math
import numpy as np

def softmax(x:float)->float:
    '''Gets the softmax value of the input'''
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum()

def derivative_softmax(X:float)->float:
    '''Gets the derivative of softmax of the input'''
    x = softmax(X)
    s = x.reshape(-1,1)
    return (np.diagflat(s) - np.dot(s, s.T))