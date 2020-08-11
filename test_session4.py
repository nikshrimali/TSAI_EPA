import pytest
import random
import session4
import os
import inspect
import re
import math
from session4 import Qualean

l = [-1,0,1]

README_CONTENT_CHECK_FOR = ['__and__', '__or__', '__repr__', '__str__', '__add__',
'__eq__', '__float__', '__ge__', '__gt__', '__invertsign__', '__le__', '__lt__',
 '__mul__', '__sqrt__', '__bool__']


def test_repr(): # 1. Proper description in __repr__() exists
    r = session4.Qualean(1)
    assert r.__repr__(), 'The representation of the Qualean object does not meet expectations'


def test_readme_exists(): # 2. Readme exists
    assert os.path.isfile("README.md", ), "README.md file missing!"


def test_readme_contents(): # 3. Contents of readme
    readme = open("README.md", "r", encoding="utf-8")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 100, "Make your README.md file interesting! Add atleast 100 words"


def test_readme_proper_description(): # 4. Check for the functions implemented
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


def test_check_add_q(): # 6. q + q + q ... 100 times != 100 * q 
    rand_num = random.choice(l)
    q = session4.Qualean(rand_num)
    q_sum = 0
    q_mul = 0
    for i in range(100):
        q_sum = q_sum +q_sum
    q_mul = q*100

    assert q_sum != q_mul, "q + q + q ... 100 times != 100 * q"


# def test_indentations(): # 7. Testing spaces and indentations
#     ''' Returns pass if used four spaces for each level of syntactically \
#     significant indenting.'''
#     lines = inspect.getsource(session4)
#     spaces = re.findall('\n +.', lines)
#     for space in spaces:
#         assert len(space) % 4 == 2, "Your script contains misplaced indentations"
#         assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines" 


def test_function_name_had_cap_letter(): # 8. Functions has capital letter
    functions = inspect.getmembers(session4, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"


def test_add_million_q(): # 9. Functions has capital letter
    q_sum = 0
    for i in range(1000000):
        rand_num = random.choice(l)
        q = Qualean(rand_num)
        q = q.get_value()
        q_sum += q
    assert math.isclose(q_sum, 0, rel_tol=1), "Sum of million q's is not close to zero"

def test_check_and_q(): # 10. q1 is False and q2 is not defined
    q1 = Qualean(0)
    assert (q1 and q2) == q1, "q1 is not False and q2 is not defined"


def test_check_or_q(): # 11. q1 is not False or q2 is not defined
    q1 = session4.Qualean(1)
    assert (q1 or q2) == q1, "q1 is not False or q2 is not defined"


def test_check_add_q(): # 12. Check add function
    q1 = session4.Qualean(rand_num = random.choice(l))
    q2 = session4.Qualean(rand_num = random.choice(l))

    a1 = q1.get_value()
    a2 = q2.get_value()
    assert a1+a2 == q1.__add__(q2), "Add working as expected"

def test_check_invalid_valueerror(): # 13. Value error is raised when lower values are assigned
    with pytest.raises(ValueError):
        session4.Qualean(4)


def test_check_mul_q(): # 13. Check multilpication function
    q1 = Qualean(rand_num = random.choice(l))
    q2 = Qualean(rand_num = random.choice(l))
    a1 = q1.get_value()
    a2 = q2.get_value()
    assert q1.__mul__(q2) == a1*a2, "Qualean Multiplication works"


def test_invert_sign(): #14. Check invert sign function
    q = session4.Qualean(-1)
    a = q.get_value()
    assert a*-1 == q.__invertsign__(), "Invertsign condition matches"

def test_qual_equality(): # 15. Check equality in Qualean values
    q1 = Qualean(random.choice(l))
    q2 = q1
    a1 = q1.get_value()
    a2 = q2.get_value()
    assert q1.__eq__(q2) == (a1 == a2), "Qualean equality is working fine"

def test_qual_gt(): # 16. Check Greater than in Qualean values
    q1 = Qualean(random.choice(l))
    q2 = Qualean(random.choice(l))
    a = (q1.get_value()) > (q2.get_value())
    b = (q1.__gt__(q2))
    assert a==b, "Greater than is not working fine"

def test_qual_ge(): #17. Check Greater than equal to in Qualean values
    q1 = Qualean(random.choice(l))
    q2 = Qualean(random.choice(l))
    a = (q1.get_value()) >= (q2.get_value())
    b = (q1.__ge__(q2))
    assert a==b, ">=  is not working fine"

def test_qual_lt(): # 18. Check less than values
    q1 = Qualean(random.choice(l))
    q2 = Qualean(random.choice(l))
    a = (q1.__lt__(q2))
    b = (q1.get_value() < q2.get_value())
    assert a==b, "LT is not working fine, results are mismatch"

def test_qual_le(): #19. Less than Equal to working fine
    q1 = Qualean(random.choice(l))
    q2 = Qualean(random.choice(l))
    a = (q1.__le__(q2))
    b = (q1.get_value() <= q2.get_value())
    assert a==b, "LE is not working fine, results are mismatch"
