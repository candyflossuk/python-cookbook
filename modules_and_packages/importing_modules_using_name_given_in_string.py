"""
This script shows how to import a module where the name of the
module is being held in a string.
"""
import importlib

math = importlib.import_module("math")
math.sin(2)

mod = importlib.import_module("urllib.request")
u = mod.urlopen("http://www.python.org")

"""
The import_module performs the same steps as import - but 
returns the module object as a result. You store it as a variable
and use it like a module

If you are using packages, import_module() can be used to perform
relative imports - however it needs 1 more argument
"""
b = importlib.import_module(".b", __package__)
