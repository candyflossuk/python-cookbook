"""
List of dictionaries and you want to sort the entries
according to one or more of the values

This structure is easy to create using operator module's
itemgetter function.
operator.itemgetter() function takes as args the lookup indicies
to extract the desired values from records in rows. Works with
any value that can be fed to an objects __getitem__().
Given multiple values the callable produced will return a tuple
with all elements and sorted(0 will order according to sort
order of tuples.
"""
from operator import itemgetter

rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

rows_by_fname = sorted(rows,
                       key=itemgetter('fname'))
rows_by_uid = sorted(rows,
                     key=itemgetter('uid'))

print(rows_by_fname)
print(rows_by_uid)

# The itemgetter() function can also accept multiple keys
rows_by_lfname = sorted(rows,
                        key=itemgetter('lname', 'fname'))
print(rows_by_lfname)

# itemgetter() can be replaced with lambdas - itemgetter() typicall is faster
rows_by_fname = sorted(rows, key=lambda r: r['fname'])
rows_by_lfname = sorted(rows, key=lambda r: (r['lname'], r['fname']))

# this technique can be applied to functions - like min or max
min(rows, key=itemgetter('uid'))
max(rows, key=itemgetter('uid'))
