#tan.py

import math

def tan(x:float) -> float:
    '''Gets the tangant value of the input'''
    return math.tan(x)

def derivative_tan(x:float)-> float:
    '''Gets the derivative of tangant of x'''
    return (1/math.cos(x))**2