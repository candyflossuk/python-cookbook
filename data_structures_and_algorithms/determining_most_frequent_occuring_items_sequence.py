"""
Script showing given a sequence of items - how to find
the most frequently occurring items.

This pattern should always be used over rolling your own tabulation
and counting of data
"""
from collections import Counter

words = [
   'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
   'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
   'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
   'my', 'eyes', "you're", 'under'
]

word_counts = Counter(words)
top_three = word_counts.most_common(3)
print(top_three)  # [('eyes', 8), ('the', 5), ('look', 4)]

"""
Counter objects can be fed any sequence of hashable items

The counter is simply a dictionary, so manual adjustments can be made
"""
word_counts['eyes'] += 1
# The object can also be updated using update
more_words = ['eyes', 'eyes', 'this']
word_counts.update(more_words)

# Because the object is a dictionary - you can do mathematical operations as so
a = Counter(words)
b = Counter(more_words)
c = a + b
"""
Counter({'eyes': 10, 'the': 5, 'look': 4, 'into': 3, 'my': 3, 
'around': 2, 'not': 1, "don't": 1, "you're": 1, 'under': 1, 
'this': 1})
"""

d = a - b
"""
Counter({'eyes': 6, 'the': 5, 'look': 4, 'into': 3, 'my': 3, 
'around': 2, 'not': 1, "don't": 1, "you're": 1, 'under': 1})
"""



