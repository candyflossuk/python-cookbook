"""
Data inside a sequence - need to extract values or reduce sequence
using a search criteria
"""
import math
from itertools import compress

# list comprehension is often easiest
mylist = [1, 4, -5, 10, -7, 2, 3, -1]
[n for n in mylist if n > 0]
# [1, 4, 10, 2, 3]
[n for n in mylist if n < 0]
# [-5, -7, -1]

""" the downside is it might produce a large output, if this is a concern use
generator expressions to produce the filtered values iteratively
"""
pos = (n for n in mylist if n > 0)
for x in pos:
    print(x)

"""
When the filtering criteria is not simple - put the filtering code
into its own function and use builtin filter() function
"""
values = ['1', '2', '-3', '-', '4', 'N/A', '5']


def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False


ivals = list(filter(is_int, values))
print(ivals)
# ['1', '2', '-3', '4', '5']
# filter creates an iterator, so if you want a list - make sure you use list()

# data can also be transformed using the generator expression
mylist = [1, 4, -5, 10, -7, 2, 3, -1]
[math.sqrt(n) for n in mylist if n > 0]
# [1.0, 2.0, 3.1622776601683795, 1.4142135623730951, 1.7320508075688772]

# One variation is to replace values that don't meet the criteria with a new one
# This is done by moving from a filter criteria to a conditional expression
clip_neg = [n if n > 0 else 0 for n in mylist]
clip_neg
# [1, 4, 0, 10, 0, 2, 3, 0]

clip_pos = [n if n < 0 else 0 for n in mylist]
clip_pos
# [0, 0, -5, 0, -7, 0, 0, -1]

"""
Another notable tool that can be used is itertools.compress()
Takes an iterable and accompanying Boolean selector sequence as input.
Output - all items in iterable where corresponding element in selector is True.
Useful for applying results of filtering one sequence to another. 
"""

addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK',
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE',
]

counts = [ 0, 3, 10, 4, 1, 7, 6, 1]

# show list of all addresses where corresponding count > 5
more5 = [n > 5 for n in counts]
# [False, False, True, False, False, True, True, False]
list(compress(addresses, more5)) # compress picks out True values
['5800 E 58TH', '1060 W ADDISON', '4801 N BROADWAY']
# compress returns an iterator - use list() to get the list

