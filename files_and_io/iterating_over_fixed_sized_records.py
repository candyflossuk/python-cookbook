"""
This script shows how to iterate over a collection of
fixed-sized records of chunks (rather than by lines)

To do this you can use the iter() function
and functools.partial()
"""
from functools import partial

RECORD_SIZE = 32

with open('somefile.data', 'rb') as f:
    records = iter(partial(f.read, RECORD_SIZE), b'')
    for r in records:
        # DO SOMETHING
        print(str(r))

"""
The records object is an iterable that will produce
fixed-sized chunks until the end of the file is reached.

The last chunk may have fewer bytes than expected - if 
file is not exact multiple of record size.

THis shows off the feature of the iter() function 
that it create an iterator if you pass it a callable
and sentinel value. The resulting iterator
calls the the supplied callable until the sentinel
is reached.

functools.partial is used to create a callable that reads 
a fixed number of bytes from a file each time it is called.
The sentinel of b'' is what gets returned when a file 
is read but the end of the file is reached. 

For fixed sized records, binary mode is the most common 'mode'
of reading the files. For text - reading line by line is more 
common (rt)
"""
