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
