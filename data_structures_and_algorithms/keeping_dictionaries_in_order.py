"""
Create a dictionary and control the order of items when iterating or serializing

Use an OrderedDict from the collections module
"""
from collections import OrderedDict
import json

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4

# outputs OrderedDict([('foo', 1), ('bar', 2), ('spam', 3), ('grok', 4)])
for key in d:
    print(key, d[key])

"""
OrderedDict can be useful to build a mapping you want to serialize or encode into 
a different format later.
i.e controlling order of fields in JSON
"""
json.dumps(d)  # Will always be consistent

"""
Internally the OrderedDict maintains a doubly linked list that orders the keys
by insertion order.
The size of an OrderedDict is more than twice as large as a normal dictionary -
due to this extra linked list.
Always look at the benefits of having order vs the extra memory overhead
"""
