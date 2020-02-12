"""
With code that accesses a list or tuple elements by position you
want to make the code easier to read. You also want be less dependant
on getting values by position - and rather by name

collections.namedtuple() provides this with minimal overhead (over a normal tuple).
namedtuple() is a factory method that returns a subclass of the normal 'tuple'.

You give it a name, and the fields it should have and it returns a class
to instantiate, passing in values for the fields you have defined

"""

from collections import namedtuple
Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('jonesy@example.com', '2012-10-19')
sub # Subscriber(addr='jonesy@example.com', joined='2012-10-19')
sub.addr # 'jonesy@example.com'
sub.joined # '2012-10-19'

"""
Looks like a normal tuple although it is interchangeable with a tuple
and supports all of the usual tuple operations such as indexing and unpacking
"""
len(sub) # 2
addr, joined = sub
addr # 'jonesy@example.com'
joined # '2012-10-19'

"""
Major use case - decoupling code from position of elements.
For example a database dump - if your reliant on column positions,
a new column is added - and your code blows up
"""


# using normal tuples
def compute_cost(records):
    total = 0.0
    for rec in records:
        total += rec[1] + rec[2]
    return total

"""
References to positional elements make code less expressive - 
more dependant on structure of records 
"""

# using namedtuple

Stock = namedtuple('Stock', ['name', 'shares', 'price'])


def compute_cost_named_tuple(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total += s.shares * s.price
    return total


"""
a use case is replacing the a dictionary - requires more space.
large dictionaries = use a namedtuple as its more efficient
namedtuple however is immutable
"""

s = Stock('ACME', 100, 123.45)
s.shares = 74  # throws an AttributeError

# when replacing attributes use _replace() method on namedtuple, creating new namedtuple
s = s._replace(shares=75)

"""
this method _replace is a subtle way to populate namedtuples with optional or missing fields
building a prototype tuple and using _replace is shown below
"""

Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])

# Create prototype
stock_prototype = Stock('', 0, 0.0, None, None)


# Function to convert dictionary to stock
def dict_to_stock(s):
    return stock_prototype._replace(**s)

a = {'name': 'ACME', 'shares': 100, 'price': 123.45}
dict_to_stock(a)  # Stock(name='ACME', shares=100, price=123.45, date=None, time=None)
b = {'name': 'ACME', 'shares': 100, 'price': 123.45, 'date': '12/17/2012'}
dict_to_stock(b)  # Stock(name='ACME', shares=100, price=123.45, date='12/17/2012', time=None)

# if you are changing various instance attributes then the use of __slots__ is better


