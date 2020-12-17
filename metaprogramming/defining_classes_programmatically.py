"""
This script shows how to have code create a new class object.

You can use the function types.new_class() to instantiate new
class objects. Provide the name of the class, tuple of parent classes,
keyword args and a callback that populates the class dictionary with
members as follows
"""
import types


def __init__(self, name, shares, price):
    self.name = name
    self.shares = shares
    self.price = price


def cost(self):
    return self.shares * self.price


cls_dict = {"__init__": __init__, "cost": cost}

Stock = types.new_class("Stock", (), {}, lambda ns: ns.update(cls_dict))
Stock.__module__ = __name__

# This creates a normal class object that works exactly like a class would work
