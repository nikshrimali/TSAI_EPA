import pytest
import session9
import inspect
from session9 import *
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
    functions = inspect.getmembers(session9, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

def test_add_evensec():
    '''Checks implementation of run_oddsec decorator'''
    assert add(1,3, sec=34) == None, "Function runs at even second, not cool"
    assert add(1,3, sec=33) == 4, "Function runs at odd second, so cool"
    assert add(1,2,3) == 6 or add(1,2,3) == None, "Function works perfectly fine"

def test_logger():
    '''Checks if logger function returns a dictionary'''
    assert type(check_logger()) == dict, "No logging dictionary returned"


def test_sod():
    '''Creates a dataframe that follows the template and adds data to check sod function'''

    data = { "Emp_Names":['Nikhil','Naman', 'Ad', 'SupAd'],
            "ID": [1,2,3,4],
            "Priviledge": [1,2,3,4], 
            "Money": ["Bohotkam", "Bohotzada", "Mat hi poocho", "Paisa kya hota hai"],
            "Useless_Info": ['sdfsadg', 'srtwtrew', 'kyukuiuy', 'gjkgjh']}

    df = pd.DataFrame(data, columns = ['Emp_Names', "Priviledge", "Money", "ID", "Useless_Info"])
    assert check_userdata('Nikhil', df).equals(df[['Emp_Names']]) == True
    assert check_userdata('Naman', df).equals(df[['Emp_Names',"Priviledge", "Money"]]) == True
    assert check_userdata('Ad', df).equals(df[['Emp_Names',"Priviledge", "Money", "ID"]]) == True
    assert check_userdata('SupAd', df).equals(df[['Emp_Names',"Priviledge", "ID",  "Useless_Info"]]) == True
    

def test_authentication():
    '''Checks the authentication by setting a password and calling the function'''
    user_password = set_password()
    assert add_auth(user_password, 'tsaiRocks123', 1,2) == 3
    assert add_auth(user_password, 'dfdssdf', 1,2) == None


def test_htmlize():
    '''Validates different html syntax implementations of htmlize decorator'''
    assert htmlize([2,3]) == '<ul>\n<li>2</li>\n<li>3</li>\n</ul>'
    assert htmlize(1/3) == str(round(1/3,2))
    assert htmlize({1:1,2:2}) == '<ul>\n<li>1=1</li>\n<li>2=2</li>\n</ul>'


def check_timed():
    '''Checks the returned values of timed decorator'''
    assert type(square(2)) == float, "Checks the return value of avg time taken for 100 reps"
