"""
This script demonstrates how to perform calculations on
a dictionary of data
"""

prices = {
    'ACME': 45.23,
    'AAPL': 612.76,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

# Invert keys and values of dictionary using zip to perform useful calculations
min_price = min(zip(prices.values(), prices.keys()))
# (10.75, 'FB')

max_price = max(zip(prices.values(), prices.keys()))
# (612.76, 'AAPL')

# To quickly rank data use zip() and sorted()
prices_sorted = sorted(zip(prices.values(), prices.keys()))
# [(10.75, 'FB'), (37.2, 'HPQ'), (45.23, 'ACME'), (205.55, 'IBM'), (612.76, 'AAPL')]

# Be aware zip() creates an iterator that can only be consumed once
prices_and_names = zip(prices.values(), prices.keys())
print(min(prices_and_names))  # (10.75, 'FB')
print(max(prices_and_names))  # ValueError: max() arg is an empty sequence

# performing common data reductions on dictionaries only processes keys
min(prices)  # AAPL
max(prices)  # IBM

# performing the same operations on prices.values() wont give you key information
min(prices.values())  # 10.75
# instead supply a key function to min() and max()
min(prices, key=lambda k: prices[k])  # FB
max(prices, key=lambda k: prices[k])  # AAPL
# to get the minimum value one extra step is taken

min_value = prices[min(prices, key=lambda k: prices[k])]  # 10.75
# using zip() where there are values that are identical the min or max key, based on
# sort will be returned

prices = { 'AAA': 45.23, 'ZZZ': 45.23 }
min(zip(prices.values(), prices.keys()))  # (45.23, 'AAA')
max(zip(prices.values(), prices.keys()))  # (45.23, 'ZZZ')


