"""
Pattern to show how to execute a reduction function - but
prior to this - transform/filter data
"""
import os

# nice way - use generator expression argument - i.e sum of squares
nums = [1, 2, 3, 4, 5]
s = sum(x * x for x in nums)

# more examples
# determine if any .py files exist in a directory
files = os.listdir('dirname')
if any(name.endswith('.py') for name in files):
    print('There be python!')
else:
    print('Sorry, no python')

# output a tuple as CSV
s = ('ACME', 50, 123.45)
print(','.join(str(x) for x in s))

# Data reduction across fields of a data structure
portfolio = [
    {'name': 'GOOG', 'shares': 50},
    {'name': 'YHOO', 'shares': 75},
    {'name': 'AOL', 'shares': 20},
    {'name': 'SCOX', 'shares': 65}
]
min_shares = min(s['shares'] for s in portfolio)

"""
The solution shows a syntactic aspect of generator
expressions when supplied as a single as an arg (no parens needed)

The following are equivalent
"""
s = sum((x * x for x in nums))
# generator-expr as arg
s_gen = sum(x * x for x in nums)

# generators are often more efficient and elegent - otherwise you have to do this
nums = [1, 2, 3, 4, 5]
s = sum([x * x for x in nums])
"""
This dosnt matter when the list is small, however if nums is large then the 
large temp data structure is not necessary

Some reduction functions accept a key arg that is useful where you might
want to use a generator instead
"""
min_shares = min(s['shares'] for s in portfolio)

# instead you can use ...
min_shares = min(portfolio, key=lambda s: s['shares'])
