import random
import requests
import math
from functools import reduce
from functools import partial

fibb_nos = [ 0, 1, 2 , 3, 5, 8,21,34,55,89,144,233,377,610,987,1597,2584,4181,6765]

def check_fibb(t:int)-> bool:
    '''A function using only list filter lambda that can tell whether a number is a Fibonacci number or not Using a pre-calculated list to store fab numbers till 10000'''
    return list(filter(lambda x: x in fibb_nos, (t,))).count(t) > 0

def add_even_odd_list(l1:list,l2:list)-> list:
    '''adds 2 iterables a and b such that a is even and b is odd'''
    return [a+b for a,b in zip(l1,l2) if a%2==0 and b%2!=0]

add_even_odd_list(l1,l2)

def strip_vowels(input_str:str)->str:
    '''strips every vowel from a string provided'''
    vowels = ['a', 'e', 'i', 'o', 'u']
    return ''.join(list(filter(lambda x: x not in vowels, input_str)))

def relu_list(input_list:list)->list:
    '''acts like a ReLU function for a 1D array'''
    return [(lambda x: x if x >= 0 else 0)(x) for x in input_list]
    
l = [0,-1,-2,3,4,5]
relu_list(l)

'''Sigmoid Function'''
def get_sigmoid(input_list:list)->list:
    '''acts like a sigmoid function for a 1D array'''
    return [(lambda x: 1 if math.log(x) > 0.5 else 0)(x) for x in input_list]

get_sigmoid([0.1111,1,2,3,4])

def getbiggestchar(test):
    return reduce(lambda x,y: max(x,y), test)

getbiggestchar("AacBa")

def add_third_element(input_list:list)->int:
    '''adds every 3rd number in a list'''
    return reduce(lambda x,y: x+y,[(lambda x:x if (input_list.index(x)+1)%3==0 else 0)(x) for x in input_list])
input_list = [3,4,9,2,3,1]

def check_profane_words(input_para:str)->bool:
    '''A list comprehension expression that takes a ~200 word paragraph, and checks whether it has any of the swear words mentioned in '''
    input_list = (str(input_para).split(' '))
    
    a = requests.get('https://raw.githubusercontent.com/RobertJGabriel/Google-profanity-words/master/list.txt')

    profane_list = (str(a.content).split('\\n'))
    return [i == j for i in input_list for j in profane_list].count(True)>0

def get_numplate()-> list:
    '''Using randint, random.choice and list comprehensions, write an expression that generates 15 random KADDAADDDD number plates, where KA is fixed, D stands for a digit, and A stands for Capital alphabets. 10<<DD<<99 & 1000<<DDDD<<9999 PTS:100'''
    return [("KA")+ str(random.randint(10,99))+'-'+chr(ord('A')+(random.randint(0,25)))+chr(ord('A')+(random.randint(0,25)))+'-'+str(random.randint(1000,9999)) for _ in range(15)]


def partial_numplate(st_code, range_start:int, range_end:int)-> list:
    '''Write the above again from scratch where KA can be changed to DL, and 1000/9999 ranges can be provided. Now use a partial function such that 1000/9999 are hardcoded, but KA can be provided'''

    return [st_code+ str(random.randint(10,99))+'-'+chr(ord('A')+(random.randint(0,25)))+chr(ord('A')+(random.randint(0,25)))+'-'+str(random.randint(range_start,range_end)) for _ in range(15)]

f = partial(partial_numplate, range_start=1000, range_end=9999)

def shift_char(input_str:str)-> str:
    '''Takes a small character string and shifts all characters by 5 (handle boundary conditions) tsai>>yxfn'''
    return ''.join([(lambda x: chr(ord(x)+5) if ord(x) <118 else chr(ord(x)-21))(x) for x in input_str])