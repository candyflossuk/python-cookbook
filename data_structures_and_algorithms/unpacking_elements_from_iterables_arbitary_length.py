"""
Unpack N elements from an iterable, iterable may be longer than N elements,
causes 'too many values to unpack' exception

> Extended iterable unpacking is made for unpacking iterables
of unknown or arbitrary length

> Often the iterables have some 'known' component, the * unpacking
allows a developer to leverage the pattern instead of writing
long

> * syntax is useful when iterating over sequence of tuples of
varying length

"""

# Use star expressions to address the problem
from statistics import mean


def drop_first_last(grades):
    first, *middle, last = grades
    return mean(middle)  # throws StatisticsError if grades is empty


record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = record
# phone_numbers will always be a list - no matter the number of phone numbers

# the starred variable can also be the first in the list
sales_record = [10, 11, 12, 13, 14, 15, 16, 17]
*trailing_qtrs, current_qtr = sales_record
trailing_avg = mean(trailing_qtrs)
print('Past 7 Quarters: ' + str(trailing_avg) +
      ' Current Quarter: ' + str(current_qtr))

# using star syntax to iterate over tuples of varying length
records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4)
]


def do_foo(x, y):
    print('foo', x, y)


def do_bar(s):
    print('bar', s)


for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)

# * unpacking can be combined with string operations also
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
# This is particularly useful if you are trying to do some inspection on log files

# As with unpacking sequences into separate variables you can throw away values
record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = record

# Using star unpacking you can split head and tail components as so...
items = [1, 10, 7, 4, 5, 9]
head, *tail = items


# Splitting to do a type of recursion also
def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head
    # Note - pythons recursion limit means this isn't a strong Python pattern


sum(items)
