"""
This script shows how to write data to a file that does not exist
on the file system.

This can be done using open() with x mode instead of w mode
"""
import os

with open('somefile', 'wt') as f:
    f.write('Hello\n')

with open('somefile', 'xt') as f:
    f.write('Hello\n')

# In binary mode use xb

"""
This solution is neat and solves a problem that occurs when writing to files 

The alternative is verbose and requires checking for a file first
"""
if not os.path.exists('somefile'):
    with open('somefile', 'wt') as f:
        f.write('Hello\n')
else:
    print('File already exists')

"""
Using x file mode is easier - and is python 3 specific to the open() 
function. No mode exists in earlier versions of python.
"""
