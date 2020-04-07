"""
This script shows how to test for the existence of a file or directory

To do this use the os.path module to test for the existence of a file or
directory.
"""
import os
import time

os.path.exists('/etc/passwd')  # True
os.path.exists('/tmp/spam')  # False

# You can perform further tests to see what kind of file it might be.

# Is a regular file
os.path.isfile('/etc/passwd')  # True

# Is a directory
os.path.isdir('/etc/passwd')  # False

# Is a symbolic link
os.path.islink('/usr/local/bin/python3')  # True

# Get the file linked to
os.path.realpath('/usr/local/bin/python3')  # '/Library/Frameworks/Python.framework/Versions/3.8/bin/python3.8'

# If you need metadata that is also available in the os.path module
os.path.getsize('/etc/passwd')  # 6946

os.path.getatime('/etc/passwd')  # 1585253880.027065
time.ctime(os.path.getatime('/etc/passwd'))  # 'Thu Mar 26 20:18:00 2020'

"""
File testing is easy enough using os.path. You might need to worry about permissions
especially scripts involving metadata
You are likely to get 'Permission denied' if the script does not have sufficient
privileges to read the metadata of the file
"""
