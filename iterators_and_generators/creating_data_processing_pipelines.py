"""
This script shows how to process data iteratively in the style of data processing
pipelines similar to unix pipes.

i.e you have a lot of data to process but it cannot all be fit into memory.

Generator functions are a good way to implement processing pipelines. To process log files for example we
could define a collection of small generator functions that perform specific self-contained tasks as so...
"""
import os
import fnmatch
import gzip
import bz2
import re


def gen_find(filepat, top):
    """
    Find all filenames in a directory tree that match a shell wildcard pattern
    """
    for path, dirlist, filelist in os.walk(top):
        for name in fnmatch.filter(filelist, filepat):
            yield os.path.join(path, name)


def gen_opener(filenames):
    """
    Open a sequence of filenames one at a time producing a file object.
    The file is closed immediately when proceeding to next iteration
    """
    for filename in filenames:
        if filename.endswith('.gz'):
            f = gzip.open(filename, 'rt')
        elif filename.endswith('.bz2'):
            f = bz2.open(filename, 'rt')
        else:
            f = open(filename, 'rt')
        yield f
        f.close()


def gen_concatenate(iterators):
    """
    Chain a sequence of iterators together into a single sequence
    """
    for it in iterators:
        yield from it


def gen_grep(pattern, lines):
    """
    Look for a regex pattern in a sequence of lines
    """
    pat = re.compile(pattern)
    for line in lines:
        if pat.search(line):
            yield line


"""
From the above it is now pretty easy to stack these functions and create a processing pipeline.
For example find all log lines that contain the word python
"""
lognames = gen_find('access-log*', 'www')
files = gen_opener(lognames)
lines = gen_concatenate(files)
pylines = gen_grep('(?i)python', lines)
for line in pylines:
    print(line)

"""
You can go one step further an extend the pipeline to feed the data in generator expressions.
This example below finds the number of bytes transferred and sums the total
"""
lognames = gen_find('access-log*', 'www')
files = gen_opener(lognames)
lines = gen_concatenate(files)
pylines = gen_grep('(?i)python', lines)
bytecolumn = (line.rsplit(None, 1)[1] for line in pylines)
bytes = (int(x) for x in bytecolumn if x != '-')
print('Total', sum(bytes))

"""
Some Notes:

Processing data in a pipelined way words well for a number of problems including (but not limited to):
    * Parsing
    * Reading from real time data sources
    * Periodic polling and more!
    
yield acts as a data producer whereas a for loop acts a consumer in the examples above.When the generators
are stacked together each yield feeds a single item of data to the next stage of the pipeline that is consuming 
it with each iteration.

A nice feature of the above is generators are small and self-contained - therefore they are easy to write
and maintain.They are so general purpose they can be reused. The code reads like a simple recipe that is 
easy to understand

This code is also extremely memory efficient, and will work on massive files with little memory in use.

gen_concatenate() has some subtlety - the purpose is to concatenate input sequences together into one long
sequence of lines. itertools.chain() performs a similar function but requires all chained iterables be 
specified as arguments - doing that would involve lines = itertools.chain(*files) - which would 
cause the gen_opener() generator to be fully consumed. Since that is producing a sequence of open files 
it cannot be used. 

yield from - simply takes gen_concatenate() emits all the values produced the generator it.
"""
