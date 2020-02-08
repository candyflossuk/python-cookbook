"""
A pattern to sort objects of the same class, where the class
does not natively support comparison operations.

built-in sorted() takes a key argument that can be passed a callable
that will return some value in the object that sorted will use to
compare the objects.

i.e you have users you want to sort bt the user_id attribute
"""
from operator import attrgetter


class User:
    def __init__(self, user_id, first_name, last_name):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return 'User({},{},{})'.format(self.user_id, self.first_name, self.last_name)


users = [User(23, 'Ross', 'Humphrey'),
         User(3, 'Sam', 'Clarke'),
         User(99, 'Gurbaj', 'Rai')]
print(sorted(users, key=lambda u: u.user_id))

"""
as well as using lambda - operator.attrgetter() can be used

attrgetter is often slightly faster - and allows multiple
fields to be extracted. 
"""
print(sorted(users, key=attrgetter('user_id')))

# an example using first_name and last_name
by_name = sorted(users, key=attrgetter('last_name',
                                       'first_name'))
print(by_name)

# the same technique can be applied to functions like max/min
min(users, key=attrgetter('user_id'))
max(users, key=attrgetter('user_id'))
