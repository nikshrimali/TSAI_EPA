# Assignment 7

## Problem Statement

- Write a closure that takes a function and then check whether the function passed has a docstring with more than 50 characters. 50 is stored as a free variable - 200
- Write a closure that gives you the next Fibonacci number - 100
- We wrote a closure that counts how many times a function was called. Write a new one that can keep a track of how many times add/mul/div functions were called, and update a global dictionary variable with the counts - 250
- Modify above such that now we can pass in different dictionary variables to update different dictionaries - 250
- No readme or no docstring for each function, or no test cases, 0. Write test cases to check boundary conditions that might cause your code to fail. 
 

#  Functions Implemented 

## def add_even_odd_list(l1:list,l2:list)-> list:
    '''adds 2 iterables a and b such that a is even and b is odd'''

## def strip_vowels(input_str:str)->str:
    '''strips every vowel from a string provided'''

## def check_fibb(t):
    '''A function using only list filter lambda that can tell whether a number is a Fibonacci number or not Using a pre-calculated list to store fab numbers till 10000'''

## def relu_list(input_list:list)->list:
    '''acts like a ReLU function for a 1D array'''

## def getbiggestchar(test:str)->str:
    '''Outputs the biggest char in the string provided'''

## def relu_list(input_list:list)->list:
    '''acts like a ReLU function for a 1D array'''

## def sumevenchar(input_list):
    '''adds only even numbers in a list'''

## def get_numplate()-> list:
    '''Using randint, random.choice and list comprehensions, write an expression that generates 15 random KADDAADDDD number plates, where KA is fixed, D stands for a digit, and A stands for Capital alphabets. 10<<DD<<99 & 1000<<DDDD<<9999'''

## def partial_numplate(st_code, range_start:int, range_end:int)-> list:
    '''Write the above again from scratch where KA can be changed to DL, and 1000/9999 ranges can be provided. Now use a partial function such that 1000/9999 are hardcoded, but KA can be provided'''

## def check_profane_words(input_para:str)->bool:
    '''A list comprehension expression that takes a ~200 word paragraph, and checks whether it has any of the swear words mentioned in '''
