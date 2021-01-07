"""
This script shows a simple way of defining context managers
using the @contextmanager annotation - rather than having to write
the __enter__ and __exit__ methods in context manager class definition.
"""
import time
from contextlib import contextmanager


@contextmanager
def timethis(label):
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print("{}: {}".format(label, end - start))


# Example Usage
with timethis("counting"):
    n = 100000000
    while n > 0:
        n -= 1


# Advanced context manager
@contextmanager
def list_transaction(orig_list):
    """
    Changes made to a list only take effect if an
    entire block runs to completion with no exceptions.
    :param orig_list:
    :return:
    """
    working = list(orig_list)
    yield working
    orig_list[:] = working


# Example usage of list_transactions
items = [1, 2, 3]
with list_transaction(items) as working:
    working.append(4)
    working.append(5)

items  # [1, 2, 3, 4, 5]


# Example of using __enter__ and __exit__
class timethiscls:
    def __init__(self, label):
        self.label = label

    def __enter__(self):
        self.start = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        end = time.time()
        print("{}: {}".format(self.label, end - self.start))
