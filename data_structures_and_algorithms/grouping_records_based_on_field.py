"""
Pattern to take sequence of dictionaries - iterate data in groups
based on value of a field (i.e date)

The function itertools.groupby() allows you to group data in such a manner.

groupby() works by scanning a sequence and finding sequential 'runs' of
identical values. On each iteration it returns the value and iterator that
produces all of the ite in a group with the same value

YOU MUST SORT DATA FIRST based on field of interest, as groupby
only examines consecutive items.
"""
from operator import itemgetter
from itertools import groupby
from collections import defaultdict

rows = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
    {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]

# Sort by desired field
rows.sort(key=itemgetter('date'))

# Iterate in groups
for date, items in groupby(rows, key=itemgetter('date')):
    print(date)
    for i in items:
        print('    ', i)


"""
If memory is not a concern (and your not sorting before hand) use
defaultdict() to build a multidict as so...
"""
rows_by_date = defaultdict(list)
for row in rows:
    rows_by_date[row['date']].append(row)

# records can be accessed as so...
for r in rows_by_date['07/01/2012']:
    print(r)
