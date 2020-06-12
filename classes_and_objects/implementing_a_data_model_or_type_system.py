"""
This script shows how to define various kinds of data structures
where you want to enforce constraints on the values that are
allowed to be assigned to certain attributes

To do this you should use descriptors to implement a system
type and value checking framework
"""


# Base class. Uses a descriptor to set a value
class Descriptor:
    def __init__(self, name=None, **opts):
        self.name = name
        for key, value in opts.items():
            setattr(self, key, value)

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value


# Descriptor for enforcing types
class Typed(Descriptor):
    expected_type = type(None)

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError("expected " + str(self.expected_type))
        super().__set__(instance, value)


# Descriptor for enforcing values
class Unsigned(Descriptor):
    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Expected >= 0")
        super().__set__(instance, value)


class MaxSized(Descriptor):
    def __init__(self, name=None, **opts):
        if "size" not in opts:
            raise TypeError("missing size option")
        super().__init__(name, **opts)

    def __set__(self, instance, value):
        if len(value) >= self.size:
            raise ValueError("size must be < " + str(self.size))
        super().__set__(instance, value)


# The above are building blocks - some usage examples are shown below


class Integer(Typed):
    expected_type = int


class UnsignedInteger(Integer, Unsigned):
    pass


class Float(Typed):
    expected_type = float


class UnsignedFloat(Float, Unsigned):
    pass


class String(Typed):
    expected_type = str


class SizedString(String, MaxSized):
    pass


# These can be used to construct classes as so
class Stock:
    # Specify constraints
    name = SizedString("name", size=8)
    shares = UnsignedInteger("shares")
    price = UnsignedFloat("price")

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price


# You can use decorators to simplify the specification of constraints in classes.
def check_attributes(**kwargs):
    def decorate(cls):
        for key, value in kwargs.items():
            if isinstance(value, Descriptor):
                value.name = key
                setattr(cls, key, value)
            else:
                setattr(cls, key, value[key])
        return cls

    return decorate()


# Example
@check_attributes(name=SizedString(size=8), shares=UnsignedInteger, price=UnsignedFloat)
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price


# Another method is to use a metaclass
class checkedmeta(type):
    def __new__(cls, clsname, bases, methods):
        # Attach attribute names to the descriptors
        for key, value in methods.items():
            if isinstance(value, Descriptor):
                value.name = key
        return type.__new__(cls, clsname, bases, methods)


# Usage
class Stock(metaclass=checkedmeta):
    name = SizedString(size=8)
    shares = UnsignedInteger()
    price = UnsignedFloat()

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price


"""
Some points:
> In the Descriptor base class - there is a __set__ and no __get__
If a descriptor will do nothing more than extract an identically named
value from underlying instance dictionary __get__() will just make it slower.

> mixins are used to build new types - like unsigned floats etc

> __init__() of descriptors have identical signatures involving kwargs **opts.
A tricky thing defining these classes is that you dont know how classes are going to be chained or what super()
will invoke. You need to make it work with any possible combo of classes.

The class decorator provides th most flexibility and is most easily understood - it is something
that can be added and removed easily. They can also be used as a replacement to mixins
This is shown below
"""


class Descriptor:
    def __init__(self, name=None, **opts):
        self.name = name
        for key, value in opts.items():
            setattr(self, key, value)

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value


# Decorator for applying type checking
def Typed(expected_type, cls=None):
    if cls is None:
        return lambda cls: Typed(expected_type, cls)

    super_set = cls.__set__

    def __set__(self, instance, value):
        if not isinstance(value, expected_type):
            raise TypeError("expected " + str(expected_type))
        super_set(self, instance, value)

    cls.__set__ = __set__
    return cls


# Decorator for unsigned values
def Unsigned(cls):
    super_set = cls.__set__

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Expected >= 0")
        super_set(self, instance, value)

    cls.__set__ = __set__
    return cls


# Decorator for allowing sized values
def MaxSized(cls):
    super_init = cls.__init__

    def __init__(self, name=None, **opts):
        if "size" not in opts:
            raise TypeError("missing size option")
        super_init(self, name, **opts)

    cls.__init__ = __init__

    super_set = cls.__set__

    def __set__(self, instance, value):
        if len(value) >= self.size:
            raise ValueError("size must be < " + str(self.size))
        super_set(self, instance, value)

    cls.__set__ = __set__
    return cls


# Specialized descriptors
@Typed(int)
class Integer(Descriptor):
    pass


@Unsigned
class UnsignedInteger(Integer):
    pass


@Typed(float)
class Float(Descriptor):
    pass


@Unsigned
class UnsignedFloat(Float):
    pass


@Typed(str)
class String(Descriptor):
    pass


@MaxSized
class SizedString(String):
    pass


# This runs about 100% faster than mixins
