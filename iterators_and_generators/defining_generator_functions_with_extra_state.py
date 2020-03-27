"""
This script shows how to define a generator function which involves extra state that
you would like to expose to the user.

To expose state we should implement a class, putting the generator function code into the iter() method
"""
from collections import deque


class linehistory:  # named as you want to treat it like a generator function
    def __init__(self, lines, histlen=3):
        self.lines = lines
        self.history = deque(maxlen=histlen)

    def __iter__(self):
        for lineno, line in enumerate(self.lines, 1):
            self.history.append((lineno, line))
            yield line

    def clear(self):
        self.history.clear()


"""
To use the above - treat it like a normal generator function. Given it is also an instance of an object
you can access the internal attributes such as history or clear() method
"""
with open('somefile.txt') as f:
    lines = linehistory(f)
    for line in lines:
        if 'python' in line:
            for lineno, hline in lines.history:
                print('{}:{}'.format(lineno, hline), end='')

"""
With generators you can fall into the trap of trying to do everything in functions. This will
lead to complicated code if the generator function needs to interact with the application in other
ways (exposing attributes, allowing control via method calls etc)
If this occurs - simply use a class definition (as shown above). Defining the generator in __itter__()
does not change anything about how you write your algorithm. Because it is a class - it simply 
makes ie easier to provide attributes and methods for users to interact with.

One subtle thing to remember that you have to call iter() if you are driving iteration from anything
but a for loop (see below)
"""
f = open('somefile.txt')
lines = linehistory(f)
next(lines)
# Throws TypeError
# Instead - call iter() first then iterate
it = iter(lines)
next(it)
