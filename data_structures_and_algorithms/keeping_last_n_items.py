"""
Keep a limited history of the last few items seen during iteration

Limited history use collections.deque

> Use when you need a simple queue structure. If you don't give
it a maxlen - you get an unbounded queue.

> O(1) complexity for popping items from either end of the queue.
For comparison a list would take O(N)
>
"""
from collections import deque


def search(lines, pattern, history=5):
    """
    Given a set of lines, the pattern parsed as a parameter
    is searched for on given lines. If a match to the pattern
    is found on the given lines the line is saved in
    'previous_lines' which stores the number of lines given
    as the param history
    :param lines: lines to search (iterable)
    :param pattern: pattern to match
    :param history: number of most recent lines to store
    :return:
    """
    previous_lines = deque(maxlen=history) # creates a fixed size queue
    for line in lines:
        if pattern in line:
            # yield - returns generator function
            yield line, previous_lines
        previous_lines.append(line)


# Example use on a file
if __name__ == '__main__':
    with open('somefile.txt') as f:
        for line, prevlines in search(f, 'python', 5):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-'*20)
