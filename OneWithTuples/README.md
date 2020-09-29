# Decorators

## <b> Functions Implemented </b>

## sod(fn):
    '''Maps the user's and returns information applicable to him'''

##  timed(n_times: int):
    '''Decorates the function to get its performance for n times'''
   
    
##  run_oddsec(fn):
    '''Checks and runs the function only if the cuurent second is odd'''

##  htmlize(obj):
    '''Takes differnt functions under its registry and converts them into html forms'''

## logger(fn):
    '''Decorator takes care of function stats'''

## authenticate(fn):
    '''Decorator to authenticate  before accessing any functions'''

## <b>Testcases Implemented</b>

##  test_readme_exists():
    Checks if README.md exists

##  test_readme_contents():
    Contents of readme file has been properly written or not
   

##  test_readme_file_for_formatting():
    Checks for Readme File formatting

##  test_function_name_had_cap_letter():
    Raises error if Functions has capital letter

##  test_add_evensec():
    '''Checks implementation of run_oddsec decorator'''

##  test_logger():
    '''Checks if logger decorator returns a dictionary'''

##  test_sod():
    '''Creates a dataframe that follows the template and adds data to validate sod decorator'''

##  test_authentication():
    '''Checks the authentication by setting a password and calling the function'''

## test_htmlize():
    '''Validates different html syntax implementations of htmlize decorator'''

## check_timed():
    '''Checks the returned values of timed decorator'''