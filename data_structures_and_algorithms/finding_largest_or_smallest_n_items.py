"""
Find the a list of the largest or smallest N items in a collection.

To do this you can use heapq - that has two functions nlargest() and nsmallest().
This should be used when N is comparatively small compared to the size of the collection

"""
import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums))  # [42, 37, 23]
print(heapq.nsmallest(3, nums))  # [-4, 1, 2]

# nsmallest and nlargest also accept a key parameter - to use with complex data structures

portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65},
]

cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])

"""
> Q. How do these methods work under the covers?
  A. The data is first converted to a list where items are ordered as a heap
"""
heap = list(nums)
heapq.heapify(heap)
"""
> heap[0] is always the smallest number. Subsequent items can be found using heapq.heappop()
> heappop() will pop off the first item and replace it with the next smallest - O(log N) operations

To find the 3 smallest you would do the following
"""
heapq.heappop(heap)
heapq.heappop(heap)
heapq.heappop(heap)

# To find largest and smallest simply use min() or max()

"""
If N (number of items being looked for) is the size of the collection (or there abouts) then sort and take a slice.
i.e sorted(items)[:] or sorted(items)[-N:]
nlargest() and nsmallest() is adaptive - it will carry out optimizations on the developers behalf
"""
