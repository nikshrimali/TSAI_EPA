## INT 
The INT() method returns an integer object from the given number or string, treats default base as 10
(No parameters) returns zero
(If base given) treats the string in the given base (0, 2, 8, 10, 16)

## encoded_from_base10
- list all the digits of the number you want to convert to base 10.
- Number the digits in ascending order from the first digit on the right to the last digit on the left, starting with zero. Let’s refer to the assigned number given to each digit as its label.
- Convert each digit by using the power of the base that it is in. To do that you multiply each digit by the base of the number raised to the power of the label assigned in step 2. Then add all the converted

## digit_map
This is a mapping of number of digits a base has from starting to end.
A digit map will have all the numbers that are available in a base arranged in ascensing order

## ValueError
- ValueError is raised when a function receives an argument of the correct type but an inappropriate value. 
- We can use try-except block to handle ValueError exception
- ValueError is an error raised in a lot of mathematical operations in the math module.
- We can raise ValueError in a function if it works for only specific range of values.

## math
This module provides access to the mathematical functions defined by the C standard.
These functions cannot be used with complex numbers; use the functions of the same name from the cmath module if you require support for complex numbers. The distinction between functions which support complex numbers and those which don’t is made since most users do not want to learn quite as much mathematics as required to understand complex numbers. Receiving an exception instead of a complex result allows earlier detection of the unexpected complex number used as a parameter, so that the programmer can determine how and why it was generated in the first place.

## isclose
The math.isclose() method checks whether two values are close, or not. This method returns a Boolean value: True if the values are close, otherwise False.

This method uses a relative tolerance, or an absolute tolerance, to see if the values are close.
It uses the following formula to compare the values:
abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)

## absolute
Used to check the equality of two float numbers. Absolute is a fixed value, and does not depend upon the size of the number
##  relative - This is more dynamic, the tolerance depends upon the size of the number used, it generally is a percentage value.

## bin()
Converts from other base forms to Binary
##hex(,
Converts other base forms to hex
##  round
The round() function returns a floating point number that is a rounded version of the specified number, with the specified number of decimals.
The default number of decimals is 0, meaning that the function will return the nearest intege

##truncation
There are many built-in modules in python. Out of these module there is one interesting module known as math module which have several functions in it like, ceil, floor, truncate, factorial, fabs, etc.

Out of these functions there is an interesting function called truncate which behaves as a ceiling function for negative number and floor function for positive number.

This is because the ceiling function is used to round up, i.e., towards positive infinity and floor function is used to round down, i.e., towards negative infinity.

But the truncate function is used to round up or down towards zero away from number.