"""
This script shows how to attach additional information to the arguments so that others know more
about how a function is supposed to be used.

Function argument annotations are a useful way to give programmers hints about how to use args for a function
"""


def add(x: int, y: int) -> int:
    return x + y


"""
The python interpreter does not attach any semantic meaning to the annotations.
They are not type checks, nor do they make Python behave differently. However
they give hints about what you had in mind. Third party tools can 
also pick up on these annotations - and they appear in documentation

Function annotations are stored in the functions __annotations__ attribute
add.__annotations__

The primary use of annotations is documentations.
"""
