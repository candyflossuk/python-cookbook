"""
This script demonstrates that when you have a collection of sorted sequences and you want to
iterate over a sorted sequence of them all merged together - how you would do this.

The heapq.merge() function does the above - as shown below
"""
import heapq

a = [1, 4, 7, 10]
b = [2, 5, 6, 11]

for c in heapq.merge(a, b):
    print(c)

"""
The iterative nature of heapq.merge means it never reads and of the supplied sequences all at once,
this means you can use it for large sequences with little overhead - for instance 
you want to merge two sorted files.
"""
with open('sorted_file_1', 'rt') as file1, \
    open('sorted_file_2', 'rt') as file2, \
    open('sorted_file_3', 'rt') as outf:

    for line in heapq.merge(file1, file2):
        outf.write(line)

"""
heapq.merge() requires all input is sorted.
"""
