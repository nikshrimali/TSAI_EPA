# Assignment 5

## Problem Statement

Time It Function
Write a function which gives out average run time per call, such that it's definition is:

def time_it(fn, *args, repetitons= 1, **kwargs): your code comes here.

We should be able to call it like this:

- time_it(print, 1, 2, 3, sep='-', end= ' ***\n'. repetitons=5)
- time_it(squared_power_list, 2, start=0, end=5, repetitons=5) #2 is the number you are calculating power of, [1, 2, 4, 8, 16, 32]
- time_it(polygon_area, 15, sides = 3, repetitons=10) # 15 is the side length. - This polygon supports area calculations of upto a hexagon
- time_it(temp_converter, 100, temp_given_in = 'f', repetitons=100) # 100 is the base temperature given to be converted
- time_it(speed_converter, 100, dist='km', time='min', repetitons=200) #dist can be km/m/ft/yrd, time can be ms/s/m/hr/day, speed given by user is in kmph

## Target

- all the test conditions to check each of the above 6 functions. All must be checked for "basics"
- if you change any character in def time_it(fn, *args, repetitons= 1, **kwargs): then 0 marks
- your test file must have atleast 25 tests
- upload to github/github-actions and then share the github URL
- 250 for the code and 250 for the tests (code + tests getting cleared)

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

