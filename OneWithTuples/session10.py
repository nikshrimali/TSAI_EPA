import time
from time import perf_counter
import pandas as pd
from functools import wraps
from datetime import datetime
from numbers import Integral
from collections.abc import Sequence, Set 
from decimal import Decimal
from functools import singledispatch
from html import escape
import time


def run_oddsec(fn):
    '''Checks and runs the function only if the cuurent second is odd'''

    def check_run(*args, sec = None, **kwargs):
        if sec is None:
            sec = datetime.now().second
        print('time checknow', sec)
        if sec % 2 != 0:
            print("Func runs now - odd sec")
            return fn(*args, **kwargs)
        else:
            print('Even second, not running now')
    return check_run

@run_oddsec
def add(*args):
    return sum(args)

# HTMLIZE

@singledispatch
def htmlize(obj):
    '''Takes differnt functions under its registry and converts them into html forms'''
    return escape(str(obj))

@htmlize.register(Integral)
def html_real(a):
    return f'{round(a, 2)}'

@htmlize.register(float)
def html_real(a):
    return f'{round(a, 2)}'

@htmlize.register(Decimal)
def html_real(a):
    return f'{round(a, 2)}'

@htmlize.register(str)
def html_str(s):
    return escape(s).replace('\n', '<br/>\n')

@htmlize.register(tuple)
@htmlize.register(list)
def html_sequence(l):
    items = (f'<li>{htmlize(item)}</li>' for item in l)
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'

@htmlize.register(dict)
def html_dict(d):
    items = (f'<li>{k}={v}</li>' for k, v in d.items())
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'

# Log of functions

def logger(fn):
    '''Decorator takes care of function stats'''

    stats_dict = dict()

    @wraps(fn)
    def store_stats(*args, **kwargs):
        func_started = time.perf_counter()
        stats_dict["func_started"] = datetime.now()
        fn(*args, **kwargs)
        stats_dict["func_ended"] = datetime.now()
        func_ended = time.perf_counter()
        stats_dict["run_time"] = func_ended - func_started
        stats_dict["func_name"] = fn.__name__
        stats_dict["func_docstr"] = fn.__doc__

        return stats_dict

    return store_stats

@logger
def check_logger():
    a = 1
    for i in range(1000):
        a = a**i
        

# Authenticate
def set_password(password=None):
    '''Sets the default password if no values are supplied
    :args password: str
    :returns inner: closure function
    '''
    def inner():
        nonlocal password
        if password == None:
            password = 'tsaiRocks123'
        return hash(password)
    return inner


def authenticate(fn):
    '''Decorator to authenticate  before accessing any functions'''

    def check_creds(user_password, in_password, *args, **kwargs):
        if user_password() != hash(in_password):
            print('Bhai isko hack karke kya hi achive kar lega life mai')

        else:
            print('suer Authenticated')
            print(f"Function {fn.__name__} is called")
            return fn(*args)
    return check_creds

@authenticate
def add_auth(*args):
    return sum(args)


# Admin stuff

def sod(fn):
    '''Maps the user's and returns information applicable to him'''
    dict_priv = {

    1: ["Emp_Names"],
    2: ["Emp_Names", "Priviledge", "Money"],
    3: ["Emp_Names", "Priviledge", "Money", "ID"],
    4: ["Emp_Names", "Priviledge", "ID", "Useless_Info"]
    }
    
    @wraps(fn)
    def check_priv(emp_name, df):
        '''Returns dataframe output based on user's priviledges'''
        if emp_name in df.values:
            priv_no = df.loc[df['Emp_Names'] == emp_name]["Priviledge"]
            priv_no = (priv_no.item())
            return df[dict_priv[priv_no]]
        else:
            print('Employee data not in system, please double check')
    return check_priv

@sod
def check_userdata(emp_name):
    return None


def timed(n_times: int):
    '''Decorates the function to get its performance for n times'''
    def outer(fn):
        
        def inner(*args, **kwargs):
            total_elapsed = 0
            for i in range(n_times):
                timer_start  = perf_counter()
                fn(*args, **kwargs)
                total_elapsed  += (perf_counter() - timer_start)
            
            avg_time = total_elapsed/n_times
            print('Avg Run time: {0:.6f}s ({1} reps)'.format(avg_time, n_times))
            return avg_time
        return inner
    return outer

@timed(100)
def square(a):
    '''Tests timed funtion by squaring a no n times'''
    a = a**2