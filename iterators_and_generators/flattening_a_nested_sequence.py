"""
This script shows how to flatten a sequence of values into a single
list of values.

This can be done using a recursive generator function involving a yield from statement
"""
from collections import Iterable


def flatten(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from flatten(x, ignore_types)
        else:
            yield x


items = [1, 2, [3, 4, [5, 6], 7], 8]

for x in flatten(items):
    print(x)

"""
isinstance(x, Iterable) checks to see if an item is iterable. If so yield from is used to emit 
all of its values as a sub routine. The end result is a single sequence of output with no nesting.

The extra arg ignore_types and the check for not isinstance(x, ignore_types) is there to prevent strings and 
bytes being interpreted as iterables and expanded as characters. This allows nested lists of strings to work in
the way people would expect

yield from is a great shortcut when you want to write generators that call other generators as subroutines. 
If you do not use it - you need to write code with an extra for loop
"""


def flatten(items, ignore_types=(str, bytes0)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            for i in flatten(x):
                yield i
        else:
            yield x

"""
The above is a minor tweak - yield from is just cleaner code.

If other types need to be skipped then include these in the ignore_types argument
"""
