"""
This script shows how iterate in reverse over a sequence.

To do this use the built-in reversed() function.
"""

a = [1, 2, 3, 4]
for x in reversed(a):
    print(x)

# Reversed iteration only works if the object has a size that can be determined OR if object implements __reversed__()
# If neither satisfied then conver the object to a list first

f = open('somefile')
for line in reversed(list(f)):
    print(line, end='')

"""
The reversed iteration can be customized on user-defined classes if they implement
__reversed__() method i.e :
"""


class Countdown:
    def __init__(self, start):
        self.start = start

    # Forward iterator
    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1

    # Reversed iterator
    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1

# Defining a reversed iterator makes the code more efficient -
# as you don't have to pull the data into a list and iterate in reverse
