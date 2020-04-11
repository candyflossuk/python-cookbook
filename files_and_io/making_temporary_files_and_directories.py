"""
This script shows how to create temporary files or directories,
where the file once used - you may want to destroy

To do this you an use tempfile.TemporaryFile
"""
from tempfile import TemporaryFile, NamedTemporaryFile, TemporaryDirectory
import tempfile

with TemporaryFile('w+t') as f:
    #  Read/Write to file
    f.write('Hello World \n')
    f.write('Testing \n')

    # Seek back to beginning and read the data
    f.seek(0)
    data = f.read()

# Temp file destroyd

# Or you can use a file like this
f = TemporaryFile('w+t')
# Use the temporary file
f.close()
# File is destroyed

"""
First argument is the file mode:
w + t for text
w + b for binary

These modes support read and write
The temporary file also accepts the same arguments as the builtin open() function as shown
"""
with TemporaryFile('w+t', encoding='utf-8', errors='ignore') as f:
    # Do something
    print ('OK')

# In Unix systems - the temp file wont have a name or have directory entry - this can be relaxed
with NamedTemporaryFile('w+t') as f:
    print('filename is:', f.name)

# File closed

# If you don't want to delete use delete=False as follows as an arg
with NamedTemporaryFile('w+t', delete=False) as f:
    print('filename is:', f.name)

# To make a temp directory use tempfile.TemporaryDirectory()
with TemporaryDirectory() as dirname:
    print('dirname is:', dirname)
    # use directory

# Directory and all contents destroyed

# You can also use mkstempt() and mkdtemp() to create temp files and directories
tempfile.mkstemp() # file
tempfile.mkdtemp() # directory

"""
These do not take care of further management - i.e mkstemp() dosnt give you a file object
and its up to you to clean it up - the files are stored in var/tmp but you should use
tempfile.gettempdir() to find out exactly where

You can also override the default temp directory

tempfile() creates files in the most secure manner possible - only giving
access to the current user and taking steps to avoid race conditions. This
can be different between platfors however
"""
