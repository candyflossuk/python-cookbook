"""
This script shows how to implement a custom iteration pattern that is different
than that offered from the built-in functions such as range(), reversed() etc

To do this - define the iteration pattern using a generator function.
"""


def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment


# To use this iterate over it using a for loop - or use it with a function that consumes an iterable (sum, list etc)
for n in frange(0, 4, 0.5):
    print(n)

list(frange(0, 1, 0.125))  # [0, 0.125, 0.25, 0.375, 0.5, 0.625, 0.75, 0.875]

"""
The presence of the yield statement in a function - turns it into a generator.
A generator only runs in response to iteration. 

The below shows how to see the underlying mechanics of how such a function works.
"""
def countdown(n):
    print('Starting to count from', n)
    while n > 0:
        yield n
        n -= 1
    print('Done!')

# Create generator, no output will appaer
c = countdown(3)
next(c)  # Starting to count from 3

# Run to next yield
next(c)  # 2

# And again
next(c)  # 1

next(c)
"""
Done!
Traceback (most recent call last):
  File "<input>", line 1, in <module>
StopIteration
"""

"""
The key feature is that a generator function only runs in response to 'next' operations carried out in iteration.
Once a generator returns, iteration stops. for statement will take care of the details so you don't have to worry
about them. 
"""
