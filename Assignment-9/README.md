# Assignment 8

## <b>Problem Statement</b>

- Write a closure that takes a function and then check whether the function passed has a docstring with more than 50 characters. 50 is stored as a free variable - 200
- Write a closure that gives you the next Fibonacci number - 100
- We wrote a closure that counts how many times a function was called. Write a new one that can keep a track of how many times add/mul/div functions were called, and update a global dictionary variable with the counts - 250
- Modify above such that now we can pass in different dictionary variables to update different dictionaries - 250
- No readme or no docstring for each function, or no test cases, 0. Write test cases to check boundary conditions that might cause your code to fail. 
 

## <b> Functions Implemented </b>

## get_next_fibbonacci()-> list:
    Write a closure that gives you the next Fibonacci number

##  func_count():
    Closure  that can keep a track of how many times add/mul/div functions were called, and update a global dictionary variable with the counts
   
    
##  check_fibb():
    A function using only list filter lambda that can tell whether a number is a Fibonacci number or not Using a pre-calculated list to store fab numbers till 10000

##  func_count_dict(dic_oper:dict):
    Modifies func_count such that now we can pass in different dictionary variables to update different dictionaries

## <b>Testcases Implemented</b>

##  test_readme_exists():
    Checks if README.md exists

##  test_readme_contents():
    Contents of readme file has been properly written or not
   

##  test_readme_file_for_formatting():
    Checks for Readme File formatting

##  test_function_name_had_cap_letter():
    Raises error if Functions has capital letter

##  test_check_docstring():
    Checks working of check_docstring function

##  test_func_count():
    Checks working of func_count function that returns a dict

##  test_func_count_dict():
    Checks working of func_count_dict function that takes input a dict and returns dict

##  test_indentations():
     Returns pass if used four spaces for each level of syntactically
    significant indenting