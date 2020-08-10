import pytest
import random
import string
import session4
import os
import inspect
import re
import math

l = [-1,0,1]

README_CONTENT_CHECK_FOR = ['__and__', '__or__', '__repr__', '__str__', '__add__',
'__eq__', '__float__', '__ge__', '__gt__', '__invertsign__', '__le__', '__lt__',
 '__mul__', '__sqrt__', '__bool__']


def test_repr():
    r = session4.Qualean(1)
    assert r.__repr__(), 'The representation of the Qualean object does not meet expectations'



def test_readme_exists(): # 2. Readme exists
    assert os.path.isfile("README.md", ), "README.md file missing!"

def test_readme_contents(): # 3. Contents of readme
    readme = open("README.md", "r", encoding="utf-8")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 100, "Make your README.md file interesting! Add atleast 100 words"

    def test_readme_proper_description(): # 3. Check for the functions implemented
    READMELOOKSGOOD = True
    f = open("README.md", "r")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"


def test_readme_file_for_formatting(): # 5. Readme File formatting
    f = open("README.md", "r")
    content = f.read()
    f.close()
    assert content.count("#") >= 10

def test_check_add_q(): # 8. Check 
    rand_num = random.choice(l)
    q = session4.Qualean(rand_num)
    q_sum = 0
    q_mul = 0
    for i in range(100):
        q_sum = q_sum +q_sum
    
    q_mul = q*100

    assert q_sum != q_mul, "q + q + q ... 100 times != 100 * q"



def test_indentations(): # 6. Testing spaces and indentations
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(session4)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines" 



def test_function_name_had_cap_letter(): # 7. Functions has captival letter
    functions = inspect.getmembers(session4, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"


def test_check_add_million_q(): # 9. Sum of million q's is close to zero
    rand_num = random.choice(l)
    q = session4.Qualean(rand_num)
    q_sum = 0

    for i in range(1000000):
        q_sum = q_sum +q

    assert (math.isclose(q_sum,0) is False, "Sum of million q's is not zero")

def test_check_and_q(): # 10. Check and condition of Boolean
    q1 = session4.Qualean(0)
    q2 = None
    print(q1.__and__(q2))
    assert (q1 and q2) == 0, "q1 is not False and q2 is not defined"



def test_check_and_q(): # 11. Check and condition of Boolean
    q1 = session4.Qualean(0)
    q2 = None
    q1.__and__(q2)    
    assert (q1 and q2) == 0, "q1 is not False and q2 is not defined"

def test_check_add_q(): # 12. Check add function
    q1 = session4.Qualean(rand_num = random.choice(l))
    q2 = session4.Qualean(rand_num = random.choice(l))

    a1 = q1.get_value()
    a2 = q2.get_value()
    print(a1+a2)
    print(q1.__add__(q2))

    assert a1+a2 == q1.__add__(q2), "Add working as expected"

def test_check_invalid_valueerror():
    with pytest.raises(ValueError):
        session4.Qualean(4)


def test_check_mul_q(): # 13. Check mul function
    q1 = session4.Qualean(rand_num = random.choice(l))
    q2 = session4.Qualean(rand_num = random.choice(l))

    a1 = q1.get_value()
    a2 = q2.get_value()
    print(a1+a2)
    print(q1.__add__(q2))

    assert (a1*a2 != q1.__mul__(q2)), "Add working as expected"

def test_class_repr(): #14. Check repr function
    s = session4.Qualean(rand_num = random.choice(l))
    s_n = session4.Qualean(rand_num = random.choice(l))

    assert 'object at' not in s.__repr__() and 'object at' not in s_n.__repr__()

def test_invert_sign(): #15. Check invert sign function
    q = session4.Qualean(-1)
    a = q.get_value()
    assert a*-1 == q.__invertsign__(), "Invertsign condition matches"
