"""
This script shows how to redirect the output of the print() function to a file
"""
with open('somefile.txt', 'wt') as f:
    print('hello world', file=f)

# not much to this - make sure the file is opened in text mode, printing will fail if in binary mode.
