"""
This pattern shows how to cleanup hardcoded slice indices
"""

# COMMON USAGE
# 0123456789012345678901234567890123456789012345678901234567890'
record = '....................100          .......513.25     ..........'

const = int(record[20:32]) * float(record[40:48])

# BETTER USAGE - shows how the slices are being used, making it easier to read
SHARES = slice(20, 32)
PRICE = slice(40, 48)

cost = int(record[SHARES]) * float(record[PRICE])

#  slice() creates a slice object that can be used anywhere slice can
items = [0, 1, 2, 3, 4, 5, 6,]
a = slice(2,4)
items[2: 4] # [2,3]
items[a] # [2,3]

items[a] = [10, 11]
items # [0, 1, 10, 11, 4, 5, 6]
del items[a]
items # [0, 1, 4, 5, 6]

# for more info on a slice instance use s.start, s.top and s.step for more info
a = slice(5, 50, 2)
a.start # 5
a.stop # 50
a.step # 2


"""
map a slice onto a sequence of a specific size using indices(size)
tuple(start, stop, step) is returned and fitted within bounds
"""
s = 'HelloWorld'
a.indices(len(s))  # (5, 10, 2)
for i in range(*a.indices(len(s))):
    print(s[i])
# prints out 'w' 'r' 'd'
