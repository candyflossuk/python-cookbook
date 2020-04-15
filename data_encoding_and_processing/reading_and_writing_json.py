"""
This script shows how to read and write data encoded in JSON

The json module provides a way to encode and decode JSON.
The two main functions are json.dumps() and json.loads(),
this mirrors the interface of other serialization libraries
such as pickle
"""
import json
from urllib.request import urlopen
from pprint import pprint
from collections import OrderedDict

data = {
    'name': 'ACME',
    'shares': 100,
    'price': 542.23
}

json_str = json.dumps(data)

# and here is how to turn a json-encoded string back into a python data structure
data = json.loads(json_str)

# if working with files instead of strings use json.dump() and json.load()
# writing json data
with open('data.json', 'w') as f:
    json.dump(data, f)

# Reading data back in
with open('data', 'r') as f:
    data = json.load(f)

"""
JSON supports the following basic types:
None
bool
int 
float 
str
lists,tuples and dicts (keys converted to string)

In web apps it is standard practice for the top level to be a dictionary

To print out json use the pprint() function in the pprint() module 
This will alphabetize the keys and output a dictionary in a more sane way.
Here is an example
"""
u = urlopen('http://search.twitter.com/search.json?q=python&rpp=5')
resp = json.loads(u.read().decode('utf-8'))
pprint(resp)

"""
Normally json decoding will create dicts or lists from the supplied data, 
if you want to create different kinds of objects - supply the object_pairs_hook
or object_hook to json.loads(). For example here is how you 
would decode JSON data preserving the order in OrderedDict
"""
s = {
    'name': 'ACME',
    'shares': 100,
    'price': 542.23
}
data = json.loads(s, object_pairs_hook=OrderedDict)


# heres how to turn a JSON dictionary into a python object
class JSONObject:
    def __init__(self, d):
        self.__dict__ = d


data = json.loads(s, object_hook=JSONObject)
data.name  # ACME
data.shares  # 100
data.price  # 490.1

"""
For encopding you can use the indent argument to json.dumps to nicely format the output
"""
print(json.dumps(data, indent=4))

# to sort keys on output use the sort_keys argument
print(json.dumps(data, sort_keys=True))

# Instances of objects are not normally serizliable to serialize instances you can supply a function
# that takes an instance and returns a dictionary that can be serialized as so


class Point:
    def __init__(self, x, y):
        self.x =x
        self.y = y


p = Point(2,3)
json.dumps(p)

def serialize_instance(obj):
    d = {'__classname__': type(obj).__name__}
    d.update(vars(obj))
    return d


# To get the instance back do the following
classes = {
    'Point': Point
}


def unserialize_object(d):
    clsname = d.pop('__classname__', None)
    if clsname:
        cls = classes[clsname]
        obj = cls.__new__(cls) # make instance without calling __init__
        for key, value in d.items():
            setattr(obj, key, value)
            return obj
    else:
        return d

# Here is how to use this
p = Point(2,3)
s = json.dumps(p, default=serialize_instance)
a = json.loads(s, object_hook=unserialize_object)
a.x  # 2
