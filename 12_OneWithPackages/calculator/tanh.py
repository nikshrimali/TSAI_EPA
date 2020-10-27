# tanh.py

import math

def tanh(x:float)->float:
    '''Gets the value of tanh'''
    return math.tanh(x)

def derivative_tanh(x:float)->float:
    '''Gets the derivative value of tanh'''
    return 1-(math.tanh(x))**2