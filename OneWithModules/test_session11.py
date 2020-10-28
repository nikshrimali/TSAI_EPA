import pytest
import inspect
import os
from alterimg.cropper import *
from alterimg.resize import *
from alterimg.typeconv import *



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

def test_png_conv():
    code_stat = 'python alterimg -f "assets\\test_images\\*" -r "j2p"'
    execute_command = os.system(code_stat)
    print(execute_command)
    assert not execute_command

def test_jpg_conv():
    code_stat = 'python alterimg -f ".\\assets\\test_images\\*" -r "p2j"'
    execute_command = os.system(code_stat)
    print(execute_command)
    assert not execute_command

def test_center_crop():
    code_stat = 'python alterimg -f "assets\\test_images\\*" -r "crp_px" -v "0,0,224,224"'
    execute_command = os.system(code_stat)
    print(execute_command)
    assert not execute_command

def test_crop_percent():
    code_stat = 'python alterimg -f ".\\assets\\test_images\\*" -r "crp_p" -v "80"'
    execute_command = os.system(code_stat)
    print(execute_command)
    assert not execute_command

def test_resize_percent():
    code_stat = 'python alterimg -f ".\\assets\\test_images\\*" -r "res_p" -v "80"'
    execute_command = os.system(code_stat)
    print(execute_command)
    assert not execute_command

# resize to 500 width
def test_resize_width():
    code_stat = 'python alterimg -f ".\\assets\\test_images\\*" -r "res_w" -v "500"'
    execute_command = os.system(code_stat)
    print(execute_command)
    assert not execute_command

def test_resize_length():
    code_stat = 'python alterimg -f ".\\assets\\test_images\\*" -r "res_h" -v "500"'
    execute_command = os.system(code_stat)
    print(execute_command)
    assert not execute_command

# Checks from files

def test_dirpng_conv():
    file_list = [".\\OneWithModules\\assets\\test_images\\4.jpg"]
    typeconv(file_list, type='p2j')
    assert os.path.exists("assets\\test_images\\4.png") == True

def test_dirjpg_conv():
    file_list = [".\\OneWithModules\\assets\\test_images\\4.png"]
    typeconv(file_list, type='j2p')
    assert os.path.exists("assets\\test_images\\4.jpg") == True


def test_dircrop_percent():

    file_list = [".\\OneWithModules\\assets\\test_images\\3.jpg"]
    x, y = Image.open(file_list[0]).size
    percent_reduction = 80
    a, b = int(x*(percent_reduction/100)), int(y*(percent_reduction/100))
    reshaper(file_list, percent_reduction)
    x, y = Image.open(file_list[0]).size
    print(x,y,a,b)
    assert (x,y) == (a,b)

def test_dircrop_width():

    file_list = [".\\OneWithModules\\assets\\test_images\\5.jpg"]
    x, y = Image.open(file_list[0]).size
    width = 100
    print(x,y)
    percent_reduction = (width/x*100)
    print(percent_reduction)
    a, b = int(x*(percent_reduction/100)), int(y*(percent_reduction/100))
    reshaper(file_list, width=width)
    x, y = Image.open(file_list[0]).size
    print(x,y,a,b)
    assert (x,y) == (a,b)

def test_dircrop_length():

    file_list = [".\\OneWithModules\\assets\\test_images\\6.jpg"]
    x, y = Image.open(file_list[0]).size
    height = 50
    print(x,y)
    percent_reduction = (height/x*100)
    print(percent_reduction)
    a, b = int(x*(percent_reduction/100)), int(y*(percent_reduction/100))
    reshaper(file_list, height=height)
    x, y = Image.open(file_list[0]).size
    print(x,y,a,b)
    assert (x,y) == (a,b)

def test_check_docstring():
    '''Checks working of check_docstring function'''
    assert typeconv.__doc__ != None
    assert reshaper.__doc__ != None
    assert cropconv.__doc__ != None

def test_alterimg_returns_processed():
    file_list = [".\\assets\\test_images\\6.jpg"]
    converted, not_altered = typeconv(file_list, type='j2p')
    assert converted == file_list

def test_alterimg_returns_notprocessed():
    file_list = [".\\assets\\test_images\\xyz.jpg"]
    converted, not_altered = typeconv(file_list, type='j2p')
    assert not_altered == file_list

def test_check_annotations():
    '''Checks working of check_docstring function'''
    assert typeconv.__annotations__ != None
    assert reshaper.__annotations__ != None
    assert cropconv.__annotations__ != None
