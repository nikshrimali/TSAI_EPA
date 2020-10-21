
from fractions import Fraction


def encoded_from_base10(number, base, digit_map):
    '''
    This function returns a string encoding in the "base" for the the "number" using the "digit_map"
    Conditions that this function must satisfy:
    - 2 <= base <= 36 else raise ValueError
    - invalid base ValueError must have relevant information
    - digit_map must have sufficient length to represent the base
    - must return proper encoding for all base ranges between 2 to 36 (including)
    - must return proper encoding for all negative "numbers" (hint: this is equal to encoding for +ve number, but with - sign added)
    - the digit_map must not have any repeated character, else ValueError
    - the repeating character ValueError message must be relevant
    - you cannot use any in-built functions in the MATH module

    '''
    if base <= 2 or base >= 36:
        raise ValueError(f'{base}does not match base should be greater than 2 and less than 36!')
    if len(digit_map)<base:
        raise ValueError
    for i in digit_map:
        c = (digit_map.count(i))
        if c > 1:
            raise ValueError("This contains repeating alphanumerics!!")
    neg_val = False
    if number < 0:
        neg_val = True
        number = number*(-1)

    dict = {}
    hex_val = ""
    for i in range(len(digit_map)):
        dict[i] = digit_map[i]

    rem = []

    for _ in range(base):
        if number is 0:
            break
        else:
            div = (number//16)
            rem = number%16
            hex_val =dict[rem]+ hex_val
            number = div

    if neg_val:
        hex_val = '-'+ hex_val
    return hex_val

def float_equality_testing(a, b):
    '''
        This function emulates the ISCLOSE method from the MATH module, but you can't use this function
        We are going to assume:
        - rel_tol = 1e-12
        - abs_tol = 1e-05
    '''
    rel_tol = 1e-12
    abs_tol = 1e-05

    #Calc Absolute tol
    a = format(a,'.20f')
    b = format(b,'.20f')

    a = float(a)
    b = float(b)

    if a<0:
        a = a*-1
    if b<0:
        b = b*-1

    if a - b < abs_tol:
        return True
    elif rel_tol*max(a,b) < rel_tol:
        return True
    else:
        return False

def manual_truncation_function(f_num):
    '''
    This function emulates python's MATH.TRUNC method. It ignores everything after the decimal point. 
    It must check whether f_num is of correct type before proceed. You can use inbuilt constructors like int, float, etc
    '''
    f_num = Fraction(f_num)
    f_num = (f_num.numerator//f_num.denominator)

    if f_num >= 1:
        return f_num
    elif f_num >= 0 and f_num < 1:
        return 0
    elif f_num < 0:
        return f_num+1

def man_tc(f_num):

    f_num = Fraction(f_num)
    f_num = (f_num.numerator//f_num.denominator)

    if f_num >= 0 and f_num < 1:
        return 0
    else:
        return f_num

def manual_rounding_function(f_num):
    '''
    This function emulates python's inbuild ROUND function. You are not allowed to use ROUND function, but
    expected to write your one manually.
    '''
    a = man_tc(f_num)
    if a > 0:
        if f_num-a<(a+1)-f_num:
            f_num = a
        else:
            f_num = a+1
    else:
        if f_num -a < (a+1) - f_num:
            f_num = a
        else:
            f_num = a+1   
    return f_num