"""
Script showing how to make a dictionary that is a subset of
another dictionary
"""

# Easiest with dictionary comprehension
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

# make dictionary of all items where value > 200
p1 = {key: value for key, value in prices.items() if value > 200}

# make a dictionary of tech stocks
tech_names = { 'AAPL', 'IBM', 'HPQ', 'MSFT' }
p2 = {key: value for key, value in prices.items() if key in tech_names}

# creating a sequence could be done the same way by using the dict() funciton
p1 = dict((key, value) for key, value in prices.items() if value > 200)

# dictionary comprehension however is clearer and runs nearly twice as fast
# another way this can be written (again slower is as (1.6 times as slow:)
p2 = {key: prices[key] for key in prices.keys() & tech_names}
