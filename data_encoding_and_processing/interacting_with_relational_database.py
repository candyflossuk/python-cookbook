"""
This script shows how to select, insert and delete
rows in a relational database
"""
import sqlite3
# A standard way to represent data is as a sequence of tuples
stocks = [
    ('GOOG', 100, 490.1),
    ('FB', 150, 7.45),
    ('APPL', 50, 545.75),
    ('HPQ', 75, 33.2),
]

"""
Given data in this form it is relatively straightforward
to interact with a relational database using Python's standard
database API - see PEP 249.

Each row of input or output data is represented by a tuple
"""

# Firstly connect to the database
db = sqlite3.connect('database.db')

# To do anything you need to create a cursor, then you can execute queries
c = db.cursor()
c.execute('create table portfolio (symbol text, shares integer, price real)')
db.commit()

# To insert a sequence of rows into data use the following
c.executemany('insert into portfolio values (?,?,?)', stocks)
db.commit()

# To perform a query use the following
for row in db.execute('select * from portfolio'):
    print(row)

# To peform queries that accept user-supplied input paramaters escape params using ?
min_price = 100
for row in db.execute('select * from portfolio where price >= ?',
                      (min_price,)):
    print(row)

"""
Some complexities exist using SQL and Python. One
complexity is the mapping from db to python types.
Dates in particular - it is common to use datetime
instances from the datetime module, or system timestamps.
For numerical data involving decimals use Decimal from the
decimal module. However the mappings vary for the database
used.

Never use Python string operators like % or .format() 
to create sql statements. If the values are derived from user input
it leaves you open to sql injection.

Libraries such as SQLAlchemy allow database tables 
to be described as Python classes, hiding the underlying
SQL.
"""
