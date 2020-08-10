# Assignment 4

##    __and__ 
Both relations must be true for the complex expression to be true.

##    __or__
If either relation is true, the complex expression is true.

##    __repr__
The repr() function returns a printable representation of the given object.
The syntax of repr() is:
repr(obj)

##    __str__
This method returns the string representation of the object. This method is called when print() or str() function is invoked on an object.

This method must return the String object. If we don’t implement __str__() function for a class, then built-in object implementation is used that actually calls __repr__() function.

##    __add__
add(a, b) :- This functions returns addition of the given arguments.

##    __eq__
a.__ge__(b) returns true if a is equals to b, else returns false

##    __float__
Returns float values for the arguments supplied
eg: Float(1) = 1.0

##    __ge__
a.__ge__(b) returns true if a is >= b, else returns false

##    __gt__
a.__gt__(b) returns true if a is > b, else returns false

##    __invertsign__
q.__invertsign__ returns numbers with the inverted sign.

##    __le__
a.__le__(b) returns true if a is =< b, else returns false

##    __lt__
a.__le__(b) returns true if a is < b, else returns false

##    __mul__
mul(a, b) :- This functions returns product of the given arguments

##    __sqrt__
Returns the sqaure root of the number

##    __bool__
Converts the value to Boolean (True or False) using the standard truth testing procedure. It’s not mandatory to pass the value to bool(). If you do not pass a value, bool() returns False.