# One With Iterables and Iterators

In the last assignment our focus was to build a sequence types, in this assignment that code has been modified to create a Iterables and Iterators

## What is an Iterator?
An iterator is an object that provides you the values sequentially
It implements two methods 
- __iter__ - Returns itself
- __next__

In Iterators looping through for loop is enabled. Once the iterator is exhausted, we cannot reuse it. Using next method over it will throw a StopIteration and looping it using for loops will return nothing as for loops provides
exception handling for StopIteration errors.


## What is an Iterable?

- Iterables comes in handy when we want to loop something again and again without worrying about exhausting of the elements. 

- A list, tuple and dictionaries are iterables. Every time you call them, they will start the index from 0 and will never get exhausted

- This is achieved as implementations of below methods.
    - __iter__ - Returns an iterator not itself
    - __next__
    -  __getitem__ - Enable sequencing functionality to the Itearable



The code for these classes along with the unit tests for the Polygon class are below if you want to use those as your starting point. But use whatever you came up with in the last project.

> Goal 1
Refactor the Polygon class so that all the calculated properties are lazy properties, i.e. they should still be calculated properties, but they should not have to get recalculated more than once (since we made our Polygon class "immutable").


> Goal 2
Refactor the Polygons (sequence) type, into an iterable. Make sure also that the elements in the iterator are computed lazily - i.e. you can no longer use a list as an underlying storage mechanism for your polygons.

You'll need to implement both an iterable, and an iterator.