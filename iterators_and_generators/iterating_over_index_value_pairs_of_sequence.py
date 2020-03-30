"""
This script shows how to iterate over a sequence whilst keeping track of which element
in the sequence is currently being processed.

To do this you can use the built in enumerate() function
"""
from collections import defaultdict

my_list = ['a', 'b', 'c']
for idx, val in enumerate(my_list):
    print(idx, val)
"""
0 a
1 b
2 c
"""

"""
For printing output with canonical line numbers (starting count at 1 instead of 0) - you 
can pass in a start argument as follows:
"""
for idx, val in enumerate(my_list, 1):
    print(idx, val)
"""
1 a
2 b
3 c
"""

# This is useful for tracking line numbers in files - should you want to use a line number in an error message


def parse_data(filename):
    with open(filename, 'rt') as f:
        for lineno, line in enumerate(f, 1):
            fields = line.split()
            try:
                count = int(fields[1])
            except ValueError as e:
                print('Line {}: Parse error: {}'.format(lineno, e))

"""
enumerate() can also be handy for keeping track of the offset into a list for occurences of a specified
value. For example if you want to map words in a file to the lines in which they occur - this can be done using
enumerate() to map each word to the line offset in the file where it was found
"""
word_summary = defaultdict(list)

with open('myfile.txt', 'r') as f:
    lines = f.readlines()

for idx, line in enumerate(lines):
    # Create a list of words in current line
    words = [w.strip().lower() for w in line.split()]
    for word in words:
        word_summary[word].append(idx)

# This produces a dictionary where the key is the word
# and the value will be a list of line numbers the word was found in.

# enumerate() returns an enumerate object - which is an iterator that returns successive tuples

# GOTCHA:
# When applying enumerate() to a sequence of tuples that are also being unpacked - you have to do the following:

data = [ (1, 2), (3, 4), (5, 6), (7, 8)]

for n, (x, y) in enumerate(data):
    # Correct
    print('Do something')

for n, x, y in enumerate(data):
    print('Do something')

