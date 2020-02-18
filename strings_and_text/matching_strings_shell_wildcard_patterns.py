"""
Script showing how to match text using wildcard patterns
that are used when working in shell.

e,g *.py, Dat[0-9]*.csv ...

To do this - you can use the fnmatch module - in particular
the fnmatch() and fnmatchcase() functions
"""
from fnmatch import fnmatch, fnmatchcase

fnmatch('foo.txt', '*.txt')  # True
fnmatch('foo.txt', '?oo.txt')  # True
fnmatch('Dat45.csv', 'Dat[0-9]*')  # True

names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
[name for name in names if fnmatch(name, 'Dat*.csv')]  # ['Dat1.csv', 'Dat2.csv']

# NOTE - the behaviour of fnmatch with regards to case sensitivity rules will vary based on OS
# i.e Mac is case sensitive, windows is not
# If the distinction matters, use fnmatchcase() instead

fnmatchcase('foo.txt', '*.TXT')  # False

# The use of these functions isn't reserved for just file names
addresses = [
    '5412 N CLARK ST',
    '1060 W ADDISON ST',
    '1039 W GRANVILLE AVE',
    '2122 N CLARK ST',
    '4802 N BROADWAY',
]

# Get all ST's
[addr for addr in addresses if fnmatchcase(addr, '* ST')]
# ['5412 N CLARK ST', '1060 W ADDISON ST', '2122 N CLARK ST']

[addr for addr in addresses if fnmatchcase(addr, '54[0-9][0-9] *CLARK*')]
# ['5412 N CLARK ST']

"""
The functionality sits between simple string methods and regex.
For simple wildcards its often sufficient. 
If writing code to match filenames - use glob module
"""
