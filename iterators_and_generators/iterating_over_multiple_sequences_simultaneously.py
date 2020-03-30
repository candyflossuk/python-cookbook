"""
This script shows how to iterate over items contained in one or more sequence at a time

To do this use the zip() function
"""
from itertools import zip_longest

xpts = [1, 5, 4, 2, 10, 7]
ypts = [101, 78, 37, 15, 62, 99]
for x, y in zip(xpts, ypts):
    print(x, y)

"""
1 101
5 78
4 37
2 15
10 62
7 99
"""

"""
zip(x, y) works by creating an iterator that produces tuples (x,y) where x is taken from a and y is taken from b.
Iteration stops whenever one of the input sequences is exhausted - length of the iteration is the same as the length
of the shortest input i.e"""

a = [1, 2, 3]
b = ['w', 'x', 'y', 'z']
for i in zip(a, b):
    print(i)
"""
(1, 'w')
(2, 'x')
(3, 'y')
"""

# If this behaviour is not desired use itertools.zip_longest() instead i.e
for i in zip_longest(a,b):
    print(i)
"""
(1, 'w')
(2, 'x')
(3, 'y')
(None, 'z')
"""

for i in zip_longest(a, b, fillvalue=0):
    print(i)
"""
(1, 'w')
(2, 'x')
(3, 'y')
(0, 'z')
"""

# zip() is used when you need to pair data together. i.e headers and values
headers = ['name', 'shares', 'price']
values = ['ACME', 100, 490.1]

# pair up to a dictionary as so
s = dict(zip(headers, values))

# to produce output you can do this
for name, val in zip(headers, values):
    print(name, '=', val)
"""
name = ACME
shares = 100
price = 490.1
"""

# a lesson common use case is to use zip() and pass more than two sequences. For this - the resulting tuples have the
# same number of items as the input sequences. e.g

a = [1, 2, 3]
b = [10, 11, 12]
c = ['x', 'y', 'z']
for i in zip(a, b, c):
    print(i)

# Zip creates an iterator as a result - if you need them in a list use the list function
zip(a,b)  # produces iterator
list(zip(a,b))  # produces list
