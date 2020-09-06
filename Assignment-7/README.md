# Assignment 7

## Problem Statement

- Write a function using only list filter lambda that can tell whether a number is a Fibonacci number or not. You can use a pre-calculated list/dict to store fab numbers till 10000 PTS:100
- Using list comprehension (and zip/lambda/etc if required) write an expression that: PTS:100
- add 2 iterables a and b such that a is even and b is odd
- strips every vowel from a string provided (tsai>>t s)
- acts like a ReLU function for a 1D array
- acts like a sigmoid function for a 1D array
- takes a small character string and shifts all characters by 5 (handle boundary conditions) tsai>>yxfn
- A list comprehension expression that takes a ~200 word paragraph, and checks whether it has any of the swear words mentioned in https://github.com/RobertJGabriel/Google-profanity-words/blob/master/list.txt PTS:200 (Links to an external site.)
Using reduce function: PTS:100
- add only even numbers in a list
- find the biggest character in a string (printable ascii characters)
- adds every 3rd number in a list
- Using randint, random.choice and list comprehensions, write an expression that generates 15 random KADDAADDDD number plates, where KA is fixed, D stands for a digit, and A stands for Capital alphabets. 10<<DD<<99 & 1000<<DDDD<<9999 PTS:100
- Write the above again from scratch where KA can be changed to DL, and 1000/9999 ranges can be provided. Now use a partial function such that 1000/9999 are hardcoded, but KA can be provided PTS:100
 

## Target

- Basics (applicable to 2/3 above):
- Proper readme file - 50 (if not there then 0)
- Docstrings must, and it must mention what the function is doing (2, 3) - 50
- Write annotations for 3 - 50 pts
- Basics tests to ensure your code if correct (20+ combination tests (counted as 1 test) in 3, check 1/2 with a manual list of 52 cards. Overall 20 tests at minimum) - 200 pts
- Submit Github link with all test files and github actions in place. 


#  Functions Implemented 

## get_player_score(a:list) -> dict
    Checks the cards, identifies and computes a score of user's deck

## get_my_deck_normally
    Returns a deck of 52 cards when function is called using normal string

## kinda_poker(a:list, b:list) -> list
    Checks the type of cards and computes a score to predict who wins

## get_deck_oneline()
    single expression that includes lambda, zip and map functions to select create 52 cards in a deck



# Testcases Implemented

## test_readme_exists
    Checks if README.md exists

## test_readme_contents
    Contents of readme file has been properly written or not

## test_readme_file_for_formatting
    Checks for Readme File formatting

## test_function_name_had_cap_letter
    Raises error if Functions has capital letter

## test_incorrect_value
    Sends an invalid input as cards to check if code is raising error


## test_normal_deck_doc
    Checks if the normal_deck function has docstrings or not

## test_normal_deck_annotations
    Checks if the normal_deck function has annotations or not