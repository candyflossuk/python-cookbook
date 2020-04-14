"""
This script shows how to read or write data encoded as a csv file.

To read as a sequence of tuples, do the following
"""
import csv
from collections import namedtuple
import re

with open('stocks.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for row in f_csv:
        # do something
        print(str(row))

"""
Row in the above example is a tuple. To access certain fields you will have
to use an index [0] = symbol, [4] = change
"""
with open('stocks.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    Row = namedtuple('Row', headers)
    for r in f_csv:
        row = Row(*r)
        # Process row
        print(str(row))

"""
The above code allows you to use column headers such as row.Symbol and row.change
To achieve something similar you can read the data as a sequence of dictionaries
"""
with open('stocks.csv') as f:
    f_csv = csv.DictReader(f)
    for row in f_csv:
        # process row
        print(str(row))

# To write CSV data
headers = ['Symbol','Price','Date','Time','Change','Volume']
rows = [('AA', 39.48, '6/11/2007', '9:36am', -0.18, 181800),
        ('AIG', 71.38, '6/11/2007', '9:36am', -0.15, 195500),
        ('AXP', 62.58, '6/11/2007', '9:36am', -0.46, 935000),
       ]

with open('stocks.csv', 'w') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(headers)
    f_csv.writerows(rows)

headers = ['Symbol', 'Price', 'Date', 'Time', 'Change', 'Volume']
rows = [{'Symbol':'AA', 'Price':39.48, 'Date':'6/11/2007',
          'Time':'9:36am', 'Change':-0.18, 'Volume':181800},
        {'Symbol':'AIG', 'Price': 71.38, 'Date':'6/11/2007',
          'Time':'9:36am', 'Change':-0.15, 'Volume': 195500},
        {'Symbol':'AXP', 'Price': 62.58, 'Date':'6/11/2007',
          'Time':'9:36am', 'Change':-0.46, 'Volume': 935000},
        ]

# If data is a dictionary do the following
with open('stocks.csv', 'w') as f:
    f_csv = csv.DictWriter(f, headers)
    f_csv.writeheader()
    f_csv.writerows(rows)

# Always prefer the use of the csv module

# To read in a tab de limited file
with open('stock.tsv') as f:
    f_tsv = csv.reader(f, delimited='\t')
    for row in f_tsv:
        print(str(row))

# When reading in CSV data and converting to tuples you need to validate
# column headers for nonvalid identifier characters
with open('stocks.csv') as f:
    f_csv = csv.reader(f)
    headers = [re.sub('[^a-zA-Z_]', '_', h) for h in next(f_csv)]
    Row = namedtuple('Row', headers)
    for r in f_csv:
        row = Row(*r)
        # Process row
        print(str(row))

"""
csv does not try to interpret the data or convert it to a type other than a string.
You want to do this with caution as the fields often are ommitting data etc.
"""

col_types = [str, float, str, str, float, int]
with open('stocks.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for row in f_csv:
        # Apply conversions to row items
        row = tuple(convert(value) for convert, value in zip(col_types, row))
        # ...

# You can also use this method of converting selected fields of dictionaries
print('Reading as dicts with type conversion')
field_types = [('Price', float),
                ('Change', float),
                ('Volume', int)]

with open('stocks.csv') as f:
    for row in csv.DictReader(f):
        row.update((key, conversion(row[key]))
                   for key, conversion in field_types)
        print(row)

# For data analysis and statistics use Pandas - this will convert the csv to a dataframe that can
# then be used to perform a number of operations and data summary stats
