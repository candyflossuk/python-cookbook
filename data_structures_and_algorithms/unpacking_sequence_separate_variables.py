"""
N-element tuple or sequence that you want to unpack to a collection
of N variables

> Unpacking works with an object that is iterable (not just tuples and lists)

> For values you are not interested in use a throwaway variable name '_'
"""
p = (4, 5)
x, y = p
print(x)  # 4
print(y)  # 5

data = ['ACME', 50, 91.1, (2012, 12, 21)]
name, shares, price, date = data
print(name)  # ACME
print(shares)  # 50
print(price)  # 91.1
print(date)  # (2012, 12, 21)

name, shares, price, (year, mon, day) = data
print(name)  # ACME
print(year)  # 2012
print(mon)  # 12
print(day)  # 21

#  Example with a string
s = 'Hello'
a, b, c, d, e = s
#  Will assign each character to a variable

#  Using _ to throw away certain values
# noinspection PyRedeclaration
_, shares, price, _ = data


"""
Mismatch in the number of elements will result in a ValueError 
being thrown as there are more values to unpack than 
values in the sequence
"""
