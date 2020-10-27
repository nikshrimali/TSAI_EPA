import pytest
import inspect
import os
import calculator as calc
import calculator.derivatives as der
import math



def test_readme_exists():
    '''Checks if README.md exists'''
    assert os.path.isfile("README.md", ), "README.md file missing!"


def test_readme_contents():
    '''Contents of readme file has been properly written or not'''
    readme = open("README.md", "r", encoding="utf-8")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 10, "Make your README.md file interesting! Add atleast 100 words"


def test_readme_file_for_formatting():
    '''Checks for Readme File formatting'''
    f = open("README.md", "r")
    content = f.read()
    f.close()
    assert content.count("#") >= 1


def test_relu():

    assert calc.relu(-0.1) == 0
    assert calc.relu(0.1) == 0.1

def test_der_relu():

    assert der.derivative_relu(0.1) == 1
    assert der.derivative_relu(-0.1) == 0

def test_sin():
    assert calc.sin(90) == math.sin(90)


def test_der_sin():

    assert der.derivative_sin(90) ==  math.cos(90)

test_der_sin()

def test_cos():
    assert calc.cos(90) == math.cos(90)


def test_derivative_cos():
    assert der.derivative_cos(90) == -calc.sin(90)


def test_tan():
    assert calc.tan(90) == math.tan(90)


def test_derivative_tan():
    assert der.derivative_tan(90) == (1/math.cos(90))**2


def test_tanh():
    assert calc.tanh(90) == math.tanh(90)



def test_derivative_tanh():
    assert der.derivative_tanh(90) ==  1-(math.tanh(90))**2


def test_log():
    assert calc.log(52) == math.log(52)


def test_derivative_log():
    assert der.derivative_log(2) == 1/2


def test_exp():
    assert calc.exp(1) == math.exp(1)


def test_derivative_exp():
    assert der.derivative_exp(1) == math.exp(1)
