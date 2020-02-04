"""
When two dictionaries are present, you can find commonalities
between the two dictionaries

The keys views supports set operations such as union, intersection and difference
The items view also supports set operations
The values view however does not support set operations - as there is no
guarantee of uniqueness - you can perform said operations by converting values
to a set
"""

a = {
    'x': 1,
    'y': 2,
    'z': 3
}

b = {
    'w': 10,
    'x': 11,
    'y': 2
}

# find the keys in common
a.keys() & b.keys()  # {'y', 'x'}

# find the keys in a that are not in b
a.keys() - b.keys()  # {'z'}

# find common key value pairs
a.items() & b.items()  # {('y', 2)}

# the same methods can be used to filter out selected keys
c = {key: a[key] for key in a.keys() - {'z', 'w'}}  # {'y': 2, 'x': 1}
