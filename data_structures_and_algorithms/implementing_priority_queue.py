"""
Implement a queue that sorts items by a given
priority - always returns item with highest
priority with each pop operation

This recipe makes use of the heapq module.
heapqpush() and heapqpop insert and remove from a list _queue
in a way such that the first item is the smallest priority.

push and pop both have O(log N) complexity where N is items in the heap.

"""

import heapq


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        # Index is Used to properly order items with the same
        # priority level - as no two indexes are the same
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)


"""
example usage:

q = PriorityQueue()
q.push(Item("foo"), 1)
q.push(Item("bar"), 5)
q.push(Item("spam"), 4)
q.push(Item("grok"), 1)
q.pop() 
# bar
q.pop()
# spam
q.pop()
# foo
q.pop()
# grok
# were items share the same priority they are returned in the same 
# order they are inserted


"""
