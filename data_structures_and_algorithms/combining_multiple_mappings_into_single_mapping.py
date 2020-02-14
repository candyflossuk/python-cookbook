"""
Script showing how to combine multiple dictionaries
logically into one single mapping to perform operations on
"""
from collections import ChainMap

a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}

# can check both dictionaries for an object using ChainMap
c = ChainMap(a,b)
print(c['x'])  # 1
print(c['y'])  # 2
print(c['z'])  # 3

"""
A ChainMap takes multiple mappings and makes the appear as one
logically - the mappings however are not merged. Instead 
the ChainMap keeps a list of the underlying mappings and redefines
dictionary operations to scan the list.
"""
len(c) # 3
list(c.keys())  # ['y', 'z', 'x']
list(c.values())  # [2, 3, 1]

# When there are duplicates values from the first mapping are used
# Operations that mutate the mapping always affect the 1st mapping

c['z'] = 10
c['w'] = 40
c  # ChainMap({'x': 1, 'z': 10, 'w': 40}, {'y': 2, 'z': 4})
a  # {'x': 1, 'z': 10, 'w': 40}
del c['y']  # Throws a KeyError

"""
A ChainMap is particularly useful when working with 
scoped values such as variables in a programming language
such as globals locas etc"""

values = ChainMap()
values['x'] = 1
# Add a new mapping
values = values.new_child()
values['x'] = 2
# Add a new mapping
values = values.new_child()
values['x'] = 3
values  # ChainMap({'x': 3}, {'x': 2}, {'x': 1})
values['x']  # 3
#Discard last mapping
values = values.parents
values['x']  # 2
values = values.parents
values['x']  # 1
values

# Another alternative to ChainMap - is merging dictionaries using update
a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
merged = dict(b)
merged.update(a)
merged['x']  # 1
merged['y']  # 2
merged['z']  # 3
# only problem with this method it is destructive - a ChainMap uses the original dictioanries

a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
merged = ChainMap(a, b)
merged['x']  # 1
a['x'] = 42
merged['x'] # 42 - Change made to merged dictionary
