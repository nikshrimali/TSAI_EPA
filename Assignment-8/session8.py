# Assignment 8

def get_next_fibbonacci():
    '''Write a closure that gives you the next Fibonacci number'''
    index = 1

    def Fibonacci(n:int)-> int:
        '''Generates nth fibonacci number in the series'''
        if n==1:
            fibonacci = 0
        elif n==2:
            fibonacci = 1
        else:
            fibonacci = Fibonacci(n-1) + Fibonacci(n-2)
        return fibonacci

    def next_fibonacci():
        '''Closure '''
        nonlocal index
        fibb_no = Fibonacci(index)
        index += 1
        return fibb_no
    return next_fibonacci


def check_docstring(func):
    '''closure that takes a function and then check whether the function passed has a docstring with more than 50 characters. 50 is stored as a free variable'''
    length = 50
    doc = (func.__doc__)

    def validate_docstring():
        if len(doc.split()) >= length:
            return True
        else:
            return False
    return validate_docstring


def func_count():
    '''Closure  that can keep a track of how many times add/mul/div functions were called, and update a global dictionary variable with the counts'''
    dic_oper = {"add":0, "mul":0, "div":0}

    def inc(func, param1, param2, increment = 1):
        func(param1, param2)
        nonlocal dic_oper
        dic_oper[func.__name__] += increment
        return dic_oper
    return inc

def add(a:int, b:int):
    return a + b

def mul(a:int, b:int):
    return a * b

def div(a:int, b:int):
    return a / b

def func_count_dict(dic_oper):
    '''Modifies func_count such that now we can pass in different dictionary variables to update different dictionaries'''

    def inc(func, param1, param2, increment = 1):
        func(param1, param2)
        nonlocal dic_oper
        dic_oper[func.__name__] += increment
        return dic_oper
    return inc

def add(a:int, b:int):
    return a + b

def mul(a:int, b:int):
    return a * b

def div(a:int, b:int):
    return a / b