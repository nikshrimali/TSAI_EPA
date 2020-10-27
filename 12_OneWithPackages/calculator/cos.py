# cos.py
import math

def cos(x:float) -> float:
    '''Gets the cosine value of the input'''
    return math.cos(x)

def derivative_cos(x:float)-> float:
    '''Gets the derivative of cosine'''
    return -(math.sin(x))