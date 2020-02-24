"""
This script shows how to strip unwanted chars such as whitespace
from beginning middle and end of a string

Use the strip() method to strip characters from the beginning
or end of a string. lstrip() and rstrip() perform stripping
from left or right side.

By default these methods strip whitespace - other chars are given
"""
import re

# White space stripping example
s = '      hello world \n'  # 'hello world'
s.lstrip()  # 'hello world \n'
s.rstrip()  #  '      hello world'

# character stripping
t = '-----hello======'
t.strip('-')  # 'hello======'
t.strip('-=')  # hello

"""
strip() methods are commonly used when reading and cleaning up data.
They can be used to get rid of whitespace, remove quotes etc

It does not apply to text in the middle of a string
"""
s = '    hello      world     \n'
s = strip()  # 'hello      world'

# to get to inner space use replace() or regex substituation
s.replace(' ', '')  # 'helloworld'
re.sub('\s+', ' ', s) # 'hello world'

"""
You can combine string stripping operations with other 
iterative processing - like reading a file, generator 
expressions are useful here
"""
filename = ''
with open(filename) as f:
    lines = (line.strip() for line in f)  # acts as a transform
    # efficient as dosn't read the data into a temp list - just creates iterator
    for line in lines:
        print(line)
        # do something interesting

# for more advanced stripping - you might turn to the translate() method.

