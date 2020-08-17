import pytest
import random
import session5
from session5 import *
import os
import inspect
import re
import cmath
import math



README_CONTENT_CHECK_FOR = ['time_it', 'squared_power_list', 'polygon_area', 'temp_converter', 'speed_converter']


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


def test_time_converter_farhenite():
    '''Checks for conversion from temperature given in Celcius to Farhenite'''
    assert temp_converter(100, 'f' ) == 37.78, "Incorrect Conversion"


def test_time_converter_celcius():
    '''Checks for conversion from temperature given in  Farhenite to Celcius'''
    assert temp_converter(37.78, 'c' ) == 100, "Incorrect Conversion"


def test_value_error_temp():
    '''Sends an invalid argument and checks if error with description is raised or not'''
    with pytest.raises(ValueError):
        temp_converter(37.78, 'ef')


def test_powerlist():
    '''Checks if powerlist function is properly implemented or not'''
    assert squared_power_list(2, start=0, end=5) == [1,2,4,8,16,32], "Powered list not working as expected"


def test_polygon_area_error():
    '''Sends an invalid argument and checks if error with description is raised or not'''
    with pytest.raises(ValueError):
        polygon_area(15, sides=10)


def test_polygon_area_correctness():
    '''Compares the actual calculation of area of Traingle with the Function implemented'''

    assert polygon_area(15, sides=3) == round((3**(1/2)/4)*(15**2),2), "Area of equilateral traingle not matching"


def test_average_time():
    '''Calculates the average of the list and compares it with the function implemented'''
    l = [0.15,0.68,0.97,0.58]
    assert avg_time(l) == sum(l)/len(l), "Average of time period is calculated wrong"

def test_value_error_speed():
    '''Sends an invalid argument and checks if error with description is raised or not'''
    with pytest.raises(ValueError):
        speed_converter(3600,'sdfs','ssdf')


def test_speed_converter_m():
    '''Checks conversions from m'''
    assert speed_converter(3600,'m','s') == 1000, "Conversion to m/sec from km/hr"
    assert speed_converter(3600,'m','ms') == (speed_converter(3600,'m','s')/1000), "Conversion into m/ms"


def test_speed_converter_km():
    '''Checks conversions from kms'''
    assert speed_converter(100,'km','hr') == 100, "Conversion to m/sec from km/hr"
    assert speed_converter(1000,'km','m') == round(speed_converter(1000,'km','hr')/60,2), "Conversion into m/ms"


def test_speed_converter_yrd():  
    '''Checks conversions from yard'''
    assert speed_converter(100,'yrd','s') == 30.38, "Conversion to m/sec from km/hr"


def test_speed_converter_ft(): 
    '''Checks conversions from feet''' 
    assert speed_converter(1,'ft','m') == 54.68, "Conversion to m/sec from km/hr"
    assert round(speed_converter(1,'ft','hr')) == round(speed_converter(1,'ft','m')*60), "Conversion into m/ms"


def test_speed_timeit():
    '''Checks if time calculated is a significant value'''
    assert time_it(speed_converter, 3600, dist='km', time='s', repetitons=200)>0, "Timeit is not working as expected"


def test_powerlist_timeit():
    '''Checks if time calculated is a significant value'''
    assert time_it(squared_power_list,2, start=0, end=5, repetitons=5)>0,"Timeit working as expected"


def test_print_timeit():
    '''Checks if time calculated is a significant value'''
    assert time_it(print, 1, 2, 3, sep='-', end= ' ***\n', repetitons=5)>0, "Timeit not working as expected"


def test_temp_timeit():
    '''Checks if time calculated is a significant value'''
    assert time_it(speed_converter, 3600, dist='km', time='s', repetitons=200)>0, "Timeit is not working as expected"


def test_polygon_timeit():
    '''Checks if time calculated is a significant value'''
    assert time_it(polygon_area, 15, sides = 3, repetitons=10)>0, "Timeit is not working as expected"

def test_junk_squaredlist():
    '''Checks if sqaured list returns error when passed junk'''
    with pytest.raises(ValueError):
        squared_power_list(2, -1, 1)

def test_junk_squaredlist2():
    '''Checks if sqaured list returns error when passed junk'''

    with pytest.raises(ValueError):
        squared_power_list(2, -1, 0)