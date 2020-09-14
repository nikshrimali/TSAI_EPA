import pytest
import session8
import inspect
from session8 import *
import os
import re


def test_readme_exists():
    '''Checks if README.md exists'''
    assert os.path.isfile("README.md", ), "README.md file missing!"


def test_readme_contents():
    '''Contents of readme file has been properly written or not'''
    readme = open("README.md", "r", encoding="utf-8")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 100, "Make your README.md file interesting! Add atleast 100 words"


def test_readme_file_for_formatting():
    '''Checks for Readme File formatting'''
    f = open("README.md", "r")
    content = f.read()
    f.close()
    assert content.count("#") >= 10


def test_function_name_had_cap_letter():
    '''Raises error if Functions has capital letter'''
    functions = inspect.getmembers(session8, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

def test_function_name_had_cap_letter():
    '''Raises error if Functions has capital letter'''
    fibb_nos = [ 0, 1, 1, 2, 3, 5, 8, 13,21,34,55,89,144,233,377,610,987,1597,2584,4181,6765]
    f1 = get_next_fibbonacci()
    for i in range(len(fibb_nos)):
        # print(a = f1(),  fibb_nos[i])
        assert f1() == fibb_nos[i], "Fibonaaci not correct"


def test_check_docstring():
    '''Checks working of check_docstring function'''
    assert check_docstring(print)() is True, "Docstring more than 50 chars works"
    assert check_docstring(test_check_docstring)() is False, "Docstring less than 50 chars works fine"


def test_func_count():
    '''Checks working of func_count function that returns a dict'''
    f1 = func_count()
    for i in range(50):
        count_dict = f1(add, 1,3)
    assert count_dict["add"] == 50, "count dict works fine"
    

def test_func_count_dict():
    '''Checks working of func_count_dict function that takes input a dict and returns dict'''
    count_dict = {'add': 50, 'mul': 0, 'div': 0}
    f1 = func_count_dict(count_dict)
    for i in range(50):
        count_dict = f1(add, 1,3)

    assert count_dict["add"] is 100, "count dict works fine"

def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically
    significant indenting.'''
    lines = inspect.getsource(session8)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"