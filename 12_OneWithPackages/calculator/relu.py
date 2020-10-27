# relu.py

import math

def relu(x:float) -> float:
    '''Gets the relu value of the input'''
    x = 0 if x < 0 else x
    return x

def derivative_relu(x:float) -> float:
    '''Gets the derivative relu value of the input'''
    x = 1 if x > 0 else 0
    return x