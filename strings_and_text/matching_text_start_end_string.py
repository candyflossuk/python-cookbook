"""
Pattern to show how to check start or end of a string for specific
text patterns like filename extensions, url schemes etc.
"""
import os
from os import listdir
from urllib.request import urlopen

# Simplest way is to use str.startswith() str.endswith()
filename = 'spam.txt'
filename.endswith('.txt')  # True
filename.startswith('file:')  # False

url = 'http://www.python.org'
url.startswith('http:') # True

"""
If you need to check against multiple choices, simply provide
a tuple of possibilities to startswith() or endwith()
"""
filenames = os.listdir('.')
filenames  # ['README.md', 'strings_and_text', '.gitignore', 'data_structures_and_algorithms', 'venv', '.git', '.idea']
[name for name in filenames if name.endswith(('.md', '.idea'))]  # ['README.md', '.idea']
any(name.endswith('.py') for name in filenames)  # False


def read_data(name):
    """
    Takes an input 'name' and checks whether it starts 
    with http: , https: or ftp: if so the url is opened
    and read using the urlib module
    :param name: 
    :return: 
    """
    if name.startswith(('http:', 'https:', 'ftp:')):
        return urlopen(name).read()
    else:
        with open(name) as f:
            return f.read()


# using tuples and the startswith method you can look up the string within a url as so
choices = tuple(['http:', 'ftp:'])
url = 'http://www.python.org'
url.startswith(choices)  # True

# Simple matching can be done using slices (less elegant) and regex (overkill)
# Data reductions can be used in conjunction with startswith() .. etc
dirname = '../..'  # Enter some directory name here
if any(name.endswith(('.c', '.h')) for name in listdir(dirname)):
    print('Do something')
