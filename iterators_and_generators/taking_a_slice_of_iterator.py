"""
This script shows how to take a slice of data produced by an iterator (where the normal slicing
operator does not work'

To do this use itertools.islice() function - this takes care of slicing iterators and generators
"""
import itertools

def count(n):
    while True:
        yield n
        n += 1

c = count(0)
# c[10:20]
# Throws TypeError: 'generator' object is not subscriptable

# Now using islice()
for x in itertools.islice(c, 10, 20):
    print(x)

"""
Iterators and generators can't normally be slices - because no information is known
about their length - and they dont implement indexing. islice() is an iterator 
that produces the desired slice items, but it does this by consumjng and discarding all of the
items up to the starting slice index. 

Further items are then produced by islice object until the end index is reached.

islice() WILL consume data on the supplied iterator, since these cannot be rewound this 
should be something to consider when using them. If you need to 'go back' then 
you should change the data into a list first
"""
