"""
Makes a dictionary that maps keys to more than one value (i.e - multidict)
"""
from collections import defaultdict

# example using lists - to preserve the insertion order of the items
d = {
    'a': [1, 2, 3],
    'b': [4, 5]
}

# example using set - to eliminate duplicates
e = {
    'a': {1, 2, 3},
    'b': {4, 5}
}

# use defaultdict, initializes the first value, focus on adding items
dd_list = defaultdict(list)
dd_list['a'].append(1)
dd_list['a'].append(2)
dd_list['b'].append(4)

dd_set = defaultdict(set)
dd_set['a'].add(1)
dd_set['a'].add(2)
dd_set['b'].add(4)

"""
when using defaultdict use caution - as when entries are accessed (even when not present
an entry will be created in the dictionary.

If you don't want this behaviour use setdefault() on a normal dictionary
"""
d_using_setdefault = {}
d_using_setdefault.setdefault('a', []).append(1)
d_using_setdefault.setdefault('a', []).append(2)
d_using_setdefault.setdefault('b', []).append(4)

# This is slightly odd - as you have to create a new instance with the initial value on every call
# The use of defaultdict makes the code cleaner - as follows
pairs = {}
dd_clean = defaultdict(list)
for key, value in pairs:
    dd_clean[key].append(value)
