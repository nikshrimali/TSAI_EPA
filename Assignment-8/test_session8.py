import pytest
import random
import session7
from session7 import *
import os
import inspect
import re
import cmath
import math


README_CONTENT_CHECK_FOR = []

def generate_random_list(start, end, in_range):
    '''Generates a random list of numbers as between start_index, end_index and range'''
    list_gen = []
    for _ in range(in_range):
        rand_num = random.randint(start, end)
        list_gen.append(rand_num)
    return list_gen

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


def test_function_name_had_cap_letter():
    '''Raises error if Functions has capital letter'''
    functions = inspect.getmembers(session7, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

# Checks the addition of random lists
def test_add_even_odd_list():
    '''Checks implementation of adding 2 iterables a and b such that a is even and b is odd'''
    for i in range(1000):
        l1 = generate_random_list(start=1, end=10, in_range=20)
        l2 = generate_random_list(start=1, end=10, in_range=20)
        match_list = []

        for i,j in zip(l1,l2):
                if i%2==0 and j%2 !=0:
                    match_list.append(i+j)
        # print('match_list',match_list)
        # print('Add_even_odd',add_even_odd_list(l1,l2))

        assert match_list == add_even_odd_list(l1,l2), 'Even odd list is not working fine'


def test_strip_vowels():
    '''strips every vowel from a string provided'''
    for i in range(1000):
        rand_list = (generate_random_list(start=97, end=120, in_range=5))
        rand_str = [chr(x) for x in rand_list]
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U' ]
        non_vowels = []
        for i in rand_str:
            if i not in vowels:
                non_vowels.append(i)

        assert strip_vowels(rand_str) == ''.join(non_vowels), "Strip vowels not working fine"


def test_check_fibb():
    for i in range(1000):
        rand_int = random.randint(0,1000)
        fibb_list = False
        if rand_int in fibb_nos:
            fibb_list = True

        assert check_fibb(rand_int) == fibb_list, "Check Fibbonacci is working fine"


def test_relu_list():
    '''Checks implementation of adding 2 iterables a and b such that a is even and b is odd'''
    for i in range(1000):
        l1 = generate_random_list(start=-10, end=10, in_range=20)

        match_list = l1

        for index,i in enumerate(l1):
                if i<0:
                    l1[index] = 0

        assert l1 == relu_list(match_list), 'Even odd list is not working fine'


def test_get_sigmoid():
    '''Checks implementation of adding 2 iterables a and b such that a is even and b is odd'''
    for i in range(1000):
        l1 = [0.1111,1,2,3,4]
        match_list = l1

        for index,i in enumerate(l1):

                if math.log(i) > 0.5:
                    l1[index] = 1
                else:
                    l1[index] = 0

        assert l1 == get_sigmoid([0.1111,1,2,3,4]), "Even odd list is not working fine"

def test_getbiggestchar():
    '''Checks implementation of adding 2 iterables a and b such that a is even and b is odd'''
    for i in range(1000):
        l1 = (generate_random_list(start=97, end=120, in_range=5))
        rand_str = [chr(x) for x in l1]
        assert chr(sorted(l1,reverse=True)[0]) == getbiggestchar(rand_str)


def test_sumevenchar():
    '''adds only even numbers in a list'''
    for i in range(1000):
        even_sum = 0
        l1 = generate_random_list(start=-10, end=10, in_range=20)
        for i in l1:
            if i%2==0:
                even_sum += i
        
        assert even_sum == sumevenchar(l1)


def test_add_third_element()->int:
    '''adds every 3rd number in a list'''
    for i in range(1000):
        third_element_sum = 0
        l1 = generate_random_list(start=-10, end=10, in_range=20)
        for i in l1:
            if (l1.index(i)+1)%3==0:
                third_element_sum += i
            
        
        assert third_element_sum == add_third_element(l1)


def test_get_numplate():
    num_plate_list = get_numplate()
    assert len(num_plate_list) == 15, "15 Number plates should be generated"
    for i in num_plate_list:
        # Checks it starts with KA
        assert 'KA' in str(i)
        # Checks the capital letters
        assert ([True for x in [ord(x) for x in (i.split('-')[1])] if (x>64 and x <91)].count(True)==2)
        # Checks the end numbers are between 1000 and 9999
        assert int(i.split('-')[2]) < 9999 and int(i.split('-')[2]) > 1000


def test_call_partial_numplate():
    state_code = "RJ"
    num_plate_list = call_partial_numplate("RJ")
    assert len(num_plate_list) == 15
    for i in num_plate_list:
        # Checks it starts with KA
        assert state_code in str(i), "Error in state code match"
        # Checks the capital letters
        assert ([True for x in [ord(x) for x in (i.split('-')[1])] if (x>64 and x <91)].count(True)==2)
        # Checks the end numbers are between 1000 and 9999
        assert int(i.split('-')[2]) < 9999 and int(i.split('-')[2]) > 1000


def test_check_profane_words():

    random_para = '''Her mom had warned her. She had been warned time and again, but she had refused to believe her. She had done everything right and she knew she would be rewarded for doing so with the promotion. So when the promotion was given to her main rival, it not only stung, it threw her belief system into disarray. It was her first big lesson in life, but not the last
Greg understood that this situation would make Michael terribly uncomfortable. Michael simply had no idea what was about to come and even though Greg could prevent it from happening, he opted to let it happen. It was quite ironic, really. It was something Greg had said he would never wish upon anyone a million times, yet here he was knowingly letting it happen to one of his best friends. He rationalized that it would ultimately make Michael a better person and that no matter how uncomfortable, everyone should experience racism at least once in their lifetime.
There was a time when he would have embraced the change that was coming. In his youth, he sought adventure and the unknown, but that had been years ago. He wished he could go back and learn to find the excitement that came with change but it was useless. That curiosity had long left him to where he had come to loathe anything that put him out of his comfort zone.
As she sat watching the world go by, something caught her eye. It wasn't so much its color or shape, but the way it was moving. She squinted to see if she could better understand what it was and where it was going, but it didn't help. As she continued to stare into the distance, she didn't understand why this uneasiness was building inside her body. She felt like she should get up and run. If only she could make out what it was. At that moment, she comprehended what it was and where it was heading, and she knew her life would never be the same'''

    assert check_profane_words(random_para) == False, "Paragraph is a clean para"
    random_para +=' xxx'
    print(random_para)
    assert check_profane_words(random_para) == True, "Paragraph is a un-clean para"