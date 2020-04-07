"""
This script shows how to manipulate pathnames in order to find the base file name, dir name
absolute path etc.

To manipulate pathnames, use the functions in the os.path module.
"""
import os
path = 'Users/beazley/Data/data.csv'

# Get the last component of the path
os.path.basename(path)
# 'data.csv'

# Get the directory name
os.path.dirname(path)
#  '/Users/beazley/Data'

# Join path components together
os.path.join('tmp', 'data', os.path.basename(path))
#  'tmp/data/data.csv'

# Expand the user's home directory
path = "~/Data/data.csv"
os.path.expanduser(path)
# '/Users/beazley/Data/data.csv'

# Split the file extension
os.path.splitext(path)
#  ('-/Data/data', 'csv')

"""
For any manipulation of filenames you should use the os.path module instead of cooking your own code.
This is for portability reasons.
"""
