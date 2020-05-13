"""
This script shows how to default the value of an argument in a method

On the surface it is fairly straight forward - assign values to the args,
making sure defaults appear last
"""


def spam(a, b=42):
    print(a, b)


# If defaultis supposed to be a mutable container- use None as deafult and write as follows
def spam(a, b=None):
    if b is None:
        b = []


# If instead of a defaul tvalue , you want to test an optional argument was given an interesting value or not use this
_no_value = object()


def spam(a, b=_no_value):
    if b is _no_value:
        print("No b value supplied")


# Here is how this behaves
spam(1)  # No b value supplied
spam(1, 2)  # b = 2
spam(1, None)  # b = None

# There is a distinction between not passing a value and None

"""
Some nuance:

Values are bound only at the time of function definition i.e
"""
x = 42


def spam(a, b=x):
    print(a, b)


spam(1)
# 1, 42

x = 23
spam(1)  # Has no effect - the value is fixed at function definition time
# 1, 42

"""
More nuance - 

Values assigned as defaults should always be immutable objects, such as None, True, False, numbers or strings
i.e never write code like this
"""


def spam(a, b=[]):
    print("NOOOOOOOO")


# This will cause issues - if the default value ever escapes the function and gets modified -
# such changes alter the default value across future calls
def spam(a, b=[]):
    print(b)
    return b


x = spam(1)
x
# []

x.append(99)
x
# [ 99 ]
spam(1)
# Returns the appended list above

"""
A better pattern is to assign None as a default and add a check inside the function for it

The use of the is operator when testing for None is important
"""


def spam(a, b=None):
    if not b:  # DO NOT DO THIS use 'if b is None'
        b = []


# None does evaluate to False, but so do many other objects

"""
Last nuance:

A function that tests to see wheter a value (any value) has been supplied to an optional.
You cannot use a value of None, 0 or False to test the presence of a user supplied argument
since they are all valid. You need something else ...

To do this :
    > Create a unique private instance of object (no_value variable above)
    
The use of object() looks odd - but object serves as a common base class for most python
objects, they have no methods, nor instance data - nor even attributes. The only thing
you can do is perform tests for identity - this makes them useful as special values.


"""
