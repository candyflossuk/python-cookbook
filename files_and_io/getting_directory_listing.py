"""
This script shows how to get a list of the files contained in a directory on
the filesystem.

To do this you can use os.listdir()
"""
import os.path
import glob
from fnmatch import fnmatch

names = os.listdir('../files_and_io')

"""
The above gives a 'raw' directory listing - all files, sub directories, symbolic links etc.
If you want to filter - use list comprehension combined with functions in os.path library
"""

# Get all regular files
file_names = [name for name in os.listdir('../files_and_io')
              if os.path.isfile(os.path.join('../files_and_io', name))]

# Get all directories
directory_names = [name for name in os.listdir('../files_and_io')
                   if os.path.isdir(os.path.join('../files_and_io', name))]

# startswith() and endswith() can be useful for filtering the contents of a directory
python_files = [name for name in os.listdir('../files_and_io')
                if name.endswith('.py')]

# For file name matching you can use glob or fnmatch modules as shown below
python_files = glob.glob('../files_and_io/*.py')

python_files = [name for name in os.listdir('somedir')
                if fnmatch(name, '*.py')]

"""
The above will of course only get you the file names, if you want 
metadata such as size etc on the files you need to use additional functions in
os.path - or os.stat() - see example below.
"""

python_files = glob.glob('../files_and_io/.*py')

# Get files sizes and modification dates
names_sz_date = [(name, os.path.getsize(name), os.path.getmtime(name))
                 for name in python_files]

for name, size, mtime in names_sz_date:
    print(name, size, mtime)

# Alternative: Get file metadata
file_metadata = [(name, os.stat(name)) for name in python_files]
for name, meta, in file_metadata:
    print(name, meta.st_size, meta.st_mtime)

# Warning sometimes the filenames are not decodable - and this must be dealt with

