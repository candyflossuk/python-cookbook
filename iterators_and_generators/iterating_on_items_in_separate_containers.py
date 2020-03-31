"""
This script shows how to perform the same action on many objects that
are contained in separate containers - avoiding nested loops to keep
the readability levels of your code high.

To do this - use itertools.chain().  This takes a list of iterables as input,
and returns an iterator that masks the fact that your acting on multiple
containers.
"""
from itertools import chain

a = [1, 2, 3, 4]
b = ['x', 'y', 'z']

for x in chain(a, b):
    print(x)
"""
1
2
3
4
x
y
z
"""

"""
A common use of chain() is where you want to perform certain operations on all items at once
but items are pooled into different working sets - i.e 
"""
active_items = set()
inactive_items = set()

# Iterate over all items
for item in chain(active_items, inactive_items):
    # Process item
    print(str(item))  # Do something

# This is more elegant than using two for loops on both the active_items and inactive_items iterables

"""
iterools.chain() accepts one or more iterables as arguments. It then creates an iterator that consumes
and returns the items produced by each supplied iterable one after the other. chain() is actually 
more efficient that combining the sequences then iterating.
"""
for x in a + b:
    print('Not efficient')

for x in chain(a, b):
    print('Efficient')

"""
a + b creates a new sequence and requires a nad b to be of the same type. chain() performs no such operation 
so it is more efficient with memory if the input sequences are large and it can easily be applied to iterables
of different types.
"""
