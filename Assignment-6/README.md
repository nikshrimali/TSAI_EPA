# Assignment 6

## Problem Statement

- Write a single expression that includes lambda, zip and map functions to select create 52 cards in a deck - 50 pts
- Write a normal function without using lambda, zip, and map function to create 52 cards in a deck - 50 pts
- Write a function that, when given 2 sets of 3 or 4 or 5 cards (1 game can only have 3 cards with each player or 4 cards or 5 cards per player) (1 deck of cards only), (2 players only), can identify who won the game of poker 

## Target

- Basics (applicable to 2/3 above):

- Proper readme file - 50 (if not there then 0)
- Docstrings must, and it must mention what the function is doing (2, 3) - 50
- Write annotations for 3 - 50 pts
- Basics tests to ensure your code if correct (20+ combination tests (counted as 1 test) in 3, check 1/2 with a manual list of 52 cards. Overall 20 tests at minimum) - 200 pts
- Submit Github link with all test files and github actions in place. 


##  Functions Implemented 

## time_it(fn, *args, repetitons= 1, **kwargs)
>Calculates the average time taken to perform any transaction by Function fn averaging the total time taken for transaction over Repetations

## squared_power_list(number, start, end)
>Returns a list of numbers created by adding powers of 2 from start till end to number n
>- squared_power_list(2,0,5) = [1, 2, 4, 8, 16, 32]

## polygon_area(side_length, sides)
>Calcuates the area of a regular polygon for no of sides of side_length

## temp_converter(base_temp, temp_given_in)
> Convert the temperature base_temp from Farhenite to Celcius or Celcius to Farhenite as mentioned in temp_given_in
>- temp_converter(100,'c') = 37.76

## speed_converter(speed, dist, time)

>The input speed is assumed in kmph, conversion can be made for any combination of conversion metrics of distance and time as mentioned below
  > - DIST_METRIC
        meter
        'kilometer'
        'yard'
        'feet
   >- TIME_METRIC =
        'milisec'
        'sec'
        'min'
        'hour'
        'day'

