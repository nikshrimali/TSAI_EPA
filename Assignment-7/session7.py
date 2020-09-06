fibb_nos = [ 0, 1, 2 , 3, 5, 8,21,34,55,89,144,233,377,610,987,1597,2584,4181,6765]

def check_fibb(t):
    '''A function using only list filter lambda that can tell whether a number is a Fibonacci number or not Using a pre-calculated list to store fab numbers till 10000'''
    return list(filter(lambda x: x in fibb_nos, (t,))).count(t) > 0

def add_even_odd_list(l1,l2):
    '''adds 2 iterables a and b such that a is even and b is odd'''
    return [a+b for a,b in zip(l1,l2) if a%2==0 and b%2!=0]

add_even_odd_list(l1,l2)

def strip_vowels(input_str):
    '''strips every vowel from a string provided'''
    vowels = ['a', 'e', 'i', 'o', 'u']
    return ''.join(list(filter(lambda x: x not in vowels, input_str)))

'''acts like a ReLU function for a 1D array'''
l = [0,-1,-2,3,4,5]
l = [x for x in l if x >= 0]
print(l)

'''Sigmoid Function'''
[math.log(x) for x in l]