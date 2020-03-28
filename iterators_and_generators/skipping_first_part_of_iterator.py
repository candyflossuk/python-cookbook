"""
This script shows you how to iterate over the items in an iterable where the first few items
are not of interest and you want to discard them.

The itertools module can be used to do this. itertools.dropwhile() is ideal. To use it, supply
the function an iterable. The returned iterator discards the first items in the sequence
as long as the supplied function returns true. Then the entirety of the sequence is returned

The example below shows how to read a file and skip the series of comments at the start
of the file
"""
from itertools import dropwhile
from itertools import islice

with open('/etc/passwd') as f:
    for line in f:
        print(line, end='')

# To skip all initial comment lines
with open('/etc/passwd') as f:
    for line in dropwhile(lambda line: line.startswith('#'), f):
        print(line, end='')

# If you know exactly how many items to skip use itertoolsislice()
items = ['a', 'b', 'c', 1, 4, 10, 15]
for x in islice(items, 3, None):
    print(x)

# The None argument above is required to indicate you want everything beyond
# the first three items, instead of just the first three

# This recipe works with all iterables, including those whose size can't be determined in advance.
# This includes generators, files and similar
