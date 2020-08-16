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

- expecting you to add all the test conditions to check each of the above 6 functions. All must be checked for "basics"
- if you change any character in def time_it(fn, *args, repetitons= 1, **kwargs): then 0 marks
- your test file must have atleast 25 tests
- upload to github/github-actions and then share the github URL
- 250 for the code and 250 for the tests (code + tests getting cleared)
 