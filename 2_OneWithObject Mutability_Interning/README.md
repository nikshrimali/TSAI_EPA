
    # **Something** - This class is to demonstrate how we create cyclic reference while doing the coding. After initialization, we defind something_new instance variable, which is initialized as None.
    Something_New is referenced inside of this class, this shows a cyclic reference.

    # **SomethingNew** - This class is to demonstrate how we create cyclic reference while doing the coding, base class of this is an object.

    when class is initialized with # **__init__**, it takes an object of Something as an object, which is intialized to None. This parameter is then converted to instance variable in the same method. Which is then referenced to Something class

    # **add_something** - This function takes a list of object of something as argument after then in the body, object of type something is initialized. 
    Something_new instance variable is referenced and set as the value of object of class SomethingNew with parameters provided as object of something class. The something object is also appended into list.

    # **clear_memory** - In python the objects are stored in memory and their reference is assigned to variables, the objects with no refernce are cleared automatically by Pyhton memory manager.

    But when it comes to cyclic reference, this is done by Garbage Collector, it runs automatically and removes all the cyclic reference which makes our programs faster. In case we have to turn it off, we have to manually do it.


    # **critical_function** - This function defines a list as instance variable, after it applies a loop in the range 1 - 1024*28 and calls function add_something, which in turn creates a cyclic refernce by calling Class Something and Something.
    After that it calls clear_memory, in which the code for garbage collection is added

    # **compare_strings_old** - This function compares string in really suboptimal way. There are two things happening inside it, first two very long string is created and then compared by value method.
    Also it loops and tryies to find if character d is the current alphabet or not in the list char_list, this is again done by list mehtod which takes 10 times more time.

    # **compare_strings_new** - This function has some changes which makes it much more ptimal than the previous function. 
    String comparision is changes to is than ==, which it more reliable as it only one variable is created and refernce is assigned to both the strings.
    Secondly iteration done to search letter d is changed to set, it is hashed and searches are 10 times faster than

    Also it loops and tries to find if character d is the current alphabet or not, this is again done by list method which takes 10 times more time in any collection

    # **sleep** - Python has a module named time which provides several useful functions to handle time-related tasks. One of the popular functions among them is sleep().
	The sleep() function suspends execution of the current thread for a given number of seconds. 
	As the name suggests, the execution of the thread is paused when this command is found, it takes time period as an argument.

    # **collection** - Any object that can be iterated upon is called a collection, some notable examples are
     - Lists
     - Sets
     - Tuples
     - Dictionaries

     These can be furthur divided into Mutable and Immutables.

     Mutables are those in which any opeation like insertion, updation, deletion can be performed without any change in the internal state of the object.
     - Lists
     - Tuples
     

     Immutables- Objects which doesn't allow any update opeations on them.
     Their internal state changes when any updates are applied
     Eg:
     - Strings
     - Sets
     - User defined classes
     - Dictioanries

