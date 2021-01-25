"""
This script shows how to add new directories to Python's path without
hard coding it into your code
"""

# The first way is thru the PYTHONPATH env var
import sys
from os.path import abspath, join, dirname

sys.path


"""
The second approach is to create a .pth file that lists the directories as so...

/some/dir
/other/dir

The .pth file needs to be placed into one of the Python's site-packages directories

You can work around the problem of hardcoded directories by constructing an appropriate
absolute path using module-level variables such as __file__
"""
sys.path.insert(0, abspath(dirname("__file__"), "src"))

"""
The above adds src to the path where that directory is located in the same directory
as the code that's is executing the insert step
"""
