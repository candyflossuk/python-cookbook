"""
This script shows how to output data using print() but also change the separator character or line ending

To do this use the sep and end keyword arguments to print() to change the output as you wish
"""
print('ACME', 50, 91.5)  # ACME 50 91.5
print('ACME', 50, 91.5, sep=',')  # ACME,50,91.5
print('ACME', 50, 91.5, sep=',', end='!!\n')  # ACME,50,91.5!!

# use of the end argument is also how to suppress the output of newlines in output
for i in range(5):
    print(i)
"""
0
1
2
3
4
"""

for i in range(5):
    print(i, end=' ')
# 0 1 2 3 4

"""
using print() with different item separator is often the easiest way to output data when you need something
other than a space separating the items. Sometimes you will see programmers use str.join() ...
"""
print(','.join('ACME', '50', '91.5')) # DOES NOT WORK

# To get this working you have to do
row = ('ACME', 50, 91.5)
print(','.join(row))
# Even then it dosn't work so you have to do this trickery
print(','.join(str(x) for x in row))

# OR you could just do this
print(*row, sep=',')

