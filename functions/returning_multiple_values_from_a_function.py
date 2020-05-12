"""
This script shows how to return multiple values from a function

To do this simply return a tuple
"""


def myfun():
    return 1, 2, 3


a, b, c = myfun()

"""
Although it looks like multiple values are returned - a tuple is actually being
created. The comma is what forms the tuple

When returning a tuple it is common to assign the result to multiple variables
This is tuple unpacking. It can also be assigned to a single variable
"""
