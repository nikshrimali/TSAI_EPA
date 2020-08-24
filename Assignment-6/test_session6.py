import pytest
import random
import session
from session6 import *
import os
import inspect
import re
import cmath
import math



README_CONTENT_CHECK_FOR = []


def test_readme_exists():
    '''Checks if README.md exists'''
    assert os.path.isfile("README.md", ), "README.md file missing!"


def test_readme_contents():
    '''Contents of readme file has been properly written or not'''
    readme = open("README.md", "r", encoding="utf-8")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 100, "Make your README.md file interesting! Add atleast 100 words"


def test_readme_proper_description():
    '''Checks for the functions implemented has proper description or not'''
    READMELOOKSGOOD = True
    f = open("README.md", "r")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"


def test_readme_file_for_formatting():
    '''Checks for Readme File formatting'''
    f = open("README.md", "r")
    content = f.read()
    f.close()
    assert content.count("#") >= 10


def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(session5)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"


def test_function_name_had_cap_letter():
    '''Raises error if Functions has capital letter'''
    functions = inspect.getmembers(session5, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"


def test_value_error_speed():
    '''Sends an invalid argument and checks if error with description is raised or not'''
    with pytest.raises(ValueError):
        assert speed_converter(3600,'ft','xyz')

def test_incorrect_value():
    '''Sends an invalid input as cards to check if code is raising error'''
    with pytest.raises(ValueError):
        kinda_poker(['queen-hearts', 'queen-clubs', 'sdf-clubs'], ['ace-clubs','ace-clubs','ace-clubs'])

def test_3_players():
    '''Checks the code behaviour when 3 values are sent as inputs instead of 2'''
    with pytest.raises(TypeError):
        kinda_poker(['queen-hearts', 'queen-clubs', 'sdf-clubs'], ['ace-clubs','ace-clubs','ace-clubs'],[])

def test_poker_doc():
    '''Checks if the poker function has docstrings or not'''
    assert (test_incorrect_value.__doc__) is None, "The Poker code is unworthy, can't hold Mjölnir"

def test_poker_annotations():
    '''Checks if the poker function has annotations or not'''
    assert (test_incorrect_value.__annotations__) is None, "The Poker code is unworthy, can't hold Mjölnir"