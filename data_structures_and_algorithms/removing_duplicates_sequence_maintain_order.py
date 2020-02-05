"""
Remove the duplicates from a sequence - preserve the order of
remaining items
"""


def dedupe_hashable(items):
    """
    Where values in the sequence are hashable -
    a set and a generator can be used to solve the problem
    :param items: sequence
    :return:
    """
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


def dedupe_non_hashable(items, key=None):
    """
    Where values are not hashable, a variation
    on the previous function can be made

    The key argument specifies a function that
    converts sequence items into a hashable type for
    the purpose of duplication detection
    :param items:
    :return:
    """
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if item not in seen:
            yield item
            seen.add(val)


#  example usage
a = [{'x': 1, y: 2}, {'x': 1, y: 3}, {'x': 1, y: 2},{'x': 2, y: 4}]
list(dedupe_non_hashable(a, key=lambda d: (d['x'], d['y'])))
# can also be used on single keys in the dictionary
list(dedupe_non_hashable(a, key=lambda d: d['x']))

"""
Using set() doesn't preserve order - the result is scrambled
The use of the generator function - means that the function can be general
purpose - i.e - file processing to remove duplicate lines

with open(somefile, 'r') as f:
    for line in dedupe(f):
        ...
"""

