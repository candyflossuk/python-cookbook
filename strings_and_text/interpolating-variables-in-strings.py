"""
Interpolating Variables in Strings

You want to create a string in which embedded
variable names are substituted with a string
representation of a variables value

Python has no diret support substituing variable values in strings.
format() can be used to approximate e.g
"""
import sys
import string

s = '{name} has {n} messages.'
s.format(name='Guido', n=37)  # s.format(name='Guido', n=37)

"""
If values to be substituted are found in variables, you 
can use combination of format_map() and vars()
"""
name = 'Guido'
n = 37
s.format_map(vars())  # 'Guido has 37 messages.'

# vars also allows you to work with instances


class Info:
    def __init__(self, name, n):
        self.name = name
        self.n = n


a = Info('Guido', 37)
s.format_map(vars(a))  # 'Guido has 37 messages.'

"""
One downside of format() and format_map() is they do
not deal with missing values very well.
"""
s.format(name='Guido')
"""
Traceback (most recent call last):
  File "<input>", line 1, in <module>
KeyError: 'n'
"""

"""
one way to avoid this is to define an alternative dictionary class
with a __missing__() method
"""


class safesub(dict):
    def __missing__(self, key):
        return '{' + key + '}'

# now use this class to wrap inputs to format_map
del n
s.format_map(safesub(vars()))  # 'Guido has {n} messages.'

"""
If you are doing this alot - hide variable substitution process
behind a small utility function that employs 
a 'frame hack'
"""


def sub(text):
    return text.format_map(safesub(sys._getframe(1).f_locals))


name = 'Guido'
n = 37
print(sub('Hello {name}'))  # Hello Guido
print(sub('You have {n} messages.'))  # You have 37 messages.
print(sub('Your favorite color is {color}'))  # Your favorite color is {color}

# some other alternatives
'%(name) has %(n) messages' % vars()

# or template strings
s = string.Template('$name has $n messages')
s.substitute(vars())

"""
format() and format_map() methods are more modern than either and are preffered.

format() gets you all string formatting features

__missing__() method of mapping/dict classes is a method that you can define to handle missing values.
in safesub class, method is defined to return missing values as a placeholder.

in sub() we use sys._getframe(1) to return the stack frame of the caller.
From this f_locals attribute gets the local variables
This is best avoided in most code - for utility functions it can be useful.
f_locals is a dictionary that is a copy of local variables - although f-Local
is modifiable they dont have a lasting effect - and it is also 
not advisable to change the stack of the caller!

"""
