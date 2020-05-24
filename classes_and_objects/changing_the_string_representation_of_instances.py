"""
This string shows hw to change the output produced by printing or viewing
instances to something more sensible

To do this change the string representation of an instance,
define __str__() and __repr__()
"""


class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Pair({0.x!r}, {0,y!r})".format(self)

    def __str__(self):
        return "({0.x!s}, {0.y!s})".format(self)


"""
The __repr__() method returns the code representation of an instance
this is the text you would use to recreate the instance.

The builtin repr() function returns this text, as does the interactive
interpreter when inspecting values.

The __str__() method converts the instance to a string and is the output 
produced by the str() and print() functions.

This recipe shows how different string representations may be used 
during formatting. Specifically the special !r formatting 
code indicates that the output of __repr__() should be used 
instead of __str__(), the deafult

Defining __repr__() and __str__() is good practice, and simplifies 
debugging and instance output. 

It is standard practice for the output of __repr__() to produce
text such that eval(rer(x)) == x if that is not possible or desired
then it is common to create a useful textual representation enclosed in <
and > instead for example
"""
f = open("file.dat")
f

"""
# If no __str__() is defined the output of __repr__() is used as a fallback.

The use of format() in the solution looks odd, but {0.x} specifies the 
x-attribute argument 0. So in the following function, the 0 is actually the instance self
"""


def __repr__(self):
    return "Pair({0.x!r}, {0.y!r})".format(self)


# As an alternative to this implementation you could use the % operator
def __repr__(self):
    return "Pair(%r, %r)" % (self.x, self.y)
