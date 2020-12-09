"""
You want to change the way in which instances are created
in order to implement singletons, caching or other similar
features. To do this you can use a metaclass to control
instance creation.

You call a class like a function to create instances - as
follows
"""
import weakref


class Spam:
    def __init__(self, name):
        self.name = name


a = Spam("Guido")
b = Spam("Diana")

"""
To customize you can define a metaclass and reimplement
the __call__() method. So if you didnt want someone
to create instances at all you can do the following
"""


class NoInstances(type):
    def __call__(self, *args, **kwargs):
        raise TypeError("Can't instantiate directly")


# Static methods can be called - but you cannot create an instance

# The singleton pattern can be implemented as follows
class Singleton(type):
    def __init__(self, *args, **kwargs):
        self.__instance = None
        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance = super().__call__(*args, **kwargs)
            return self.__instance
        else:
            return self.__instance


class Spam(metaclass=Singleton):
    def __init__(self):
        print("Creating Spam")


"""
Now, here is an example of creating cached instances
"""


class Cached(type):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__cache = weakref.WeakValueDictionary()

    def __call__(self, *args):
        if args in self.__cache:
            return self.__cache[args]
        else:
            obj = super().__call__(*args)
            self.__cache[args] = obj
            return obj


"""
Using a metaclass to implement various instance 
creation patterns can be more elegant than not using 
metaclasses- whereby you would have to use factory 
functions.
"""
