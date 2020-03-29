"""
This script shows how to iterate over all possible combinations or permutations of a collection

To do the first of three itertools functions you can use is itertools.permutations().
This takes a sequence of tuples and rearranges all of the items into all possible permutations
"""
from itertools import permutations
from itertools import combinations
from itertools import combinations_with_replacement

items = ['a', 'b', 'c']
for p in permutations(items):
    print(p)

"""
('a', 'b', 'c')
('a', 'c', 'b')
('b', 'a', 'c')
('b', 'c', 'a')
('c', 'a', 'b')
('c', 'b', 'a')
"""

# If you want all permutations of a smaller length - you can use the optional length arg
for p in permutations(items, 2):
    print(p)

"""
('a', 'b')
('a', 'c')
('b', 'a')
('b', 'c')
('c', 'a')
('c', 'b')
"""

# Use itertools.combinations() to produce a sequence of combinations of items
for c in combinations(items, 3):
    print(c)
# ('a', 'b', 'c')

for c in combinations(items, 2):
    print(c)
"""
('a', 'b')
('a', 'c')
('b', 'c')
"""
for c in combinations(items, 1):
    print(c)
"""
('a',)
('b',)
('c',)
"""

"""
For combinations() the order is not considered - that is a,b is considered the same as ba (not produced)

When producing combinations, chosen items are removed from the collection of possible candidates (i.e if 'a' 
has already been chosen, then removed from consideration. 

itertools.combinations_with_replacement() function relaxes said rule - and allows same item to be chosen more than
once
"""
for c in combinations_with_replacement(items, 3):
    print(c)

"""
('a', 'a', 'a')
('a', 'a', 'b')
('a', 'a', 'c')
('a', 'b', 'b')
('a', 'b', 'c')
('a', 'c', 'c')
('b', 'b', 'b')
('b', 'b', 'c')
('b', 'c', 'c')
('c', 'c', 'c')
"""

# When faced with complicated iteration problems - refer to itertools first. If common - a solution will be available
