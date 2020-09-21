# Assignment 9


import pandas as pd
data = { "Emp_Names":['Nikhil','Naman', 'Ad', 'SupAd'],
        "ID": [1,2,3,4],
        "Priviledge": [1,2,3,4 ], 
        "Money": ["Bohotkam", "Bohotzada", "Mat hi poocho", "Paisa kya hota hai"],
        "Useless_Info": ['sdfsadg', 'srtwtrew', 'kyukuiuy', 'gjkgjh']}

df = pd.DataFrame(data, columns = ['Emp_Names', "Priviledge", "Money", "ID", "Useless_Info"])

from functools import wraps
def sod(fn):
    '''Maps the user's and returns information applicable to him'''
    dict_priv = {
    1: ["Emp_Names"],
    2: ["Emp_Names", "Priviledge", "Money"],
    3: ["Emp_Names", "Priviledge", "Money", "ID"],
    4: ["Emp_Names", "Priviledge", "ID", "Useless_Info"]}
    
    @wraps(fn)
    def check_priv(emp_name):
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
    print("abc")


# Logger

def logger(fn):
    '''Decorator takes care of function stats'''

    from functools import wraps
    stats_dict = dict()

    @wraps(fn)
    def store_stats():
        stats_dict["func_started"] = time.perf_counter()
        fn()
        stats_dict["func_ended"] = time.perf_counter()
        stats_dict["run_time"] = stats_dict["func_ended"]  - stats_dict["func_started"]
        stats_dict["func_name"] = fn.__name__
        stats_dict["func_docstr"] = fn.__doc__

        return stats_dict

    return store_stats

@logger
def add():
    print (1+2)


# Function runs on the even sec

import time
from time import perf_counter

def run_oddsec(fn):

    def check_run():
        check_timenow = round(perf_counter(),0)
        print('time checknow' ,check_timenow)

        if check_timenow % 2 == 0:
            print("Func runs now - even sec")
            fn()
    
    return check_run


@run_oddsec
def add():
    print (1+2)

# authenticate - 300pts

def authenticate(fn):
    '''Decorator to check for the authentication before accessing any functions'''

    def check_creds(*, user_password, in_password:str):
        if user_password() != hash(in_password):
            print('Bhai isko hack karke kya hi achive kar lega life mai')

        else:
            print('suer Authenticated')
            print(f"Function {fn.__name__} is called")
            return fn()
    return check_creds