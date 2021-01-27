"""
This script (and accompanying scripts referenced) show how to customize
Python's import statement so that it can transparently load modules from
a remote machine.

The code shown here should (in production) include an authentication layer -
as you are effectively executing remote code.

This recipe (as a side effect) focuses on the inner workings of Python's
import statement.

See 'testcode' package

The first method to load a remote module - is to create an explicit loading function (see below)
"""
import imp
import urllib.request
import sys


def load_module(url):
    u = urllib.request.urlopen(url)
    source = u.read().decode("utf-8")
    mod = sys.modules.setdefault(url, imp.new_module(url))
    code = compile(source, url, "exec")
    mod.__file__ = url
    mod.__package__ = ""
    exec(code, mod.__dict__)
    return mod


# This downloads the source code, compiles it and executes it - see below for uage
fib = load_module("http://localhost:15000/fib.py")
fib.fib(10)
spam = load_module("http://localhost:1500/spam.py")
spam.hello("Ross")

"""
This works very simply - however its not plugged into the import statement - and extending it 
to support pacakges requries more work - a better appraoch is to create a custom importer - the 
first way we can achieve this is by using a meta path importer. 
"""
