"""
This script simply shows how to distribute a package.

Firstly - clean up the directory structure as such

projectname/
    README.MD
    Doc/
        documentation.txt
    projectname/
        __init__.py
        script.py
        utils/
            something.py
    examples/
        helloworld.py

Then write a setup.py as follows below
"""
from distutils.core import setup

setup(
    name="projectname",
    version="1.0",
    author="Ross Humphrey",
    author_email="you@you.com",
    url="http://you.com/projectname",
    packages=["projectname", "projectname.utils"],
)

# Then make a manifest.in that lists nonsource files to include
# Manifest.in
include *.txt
recursive-include examples *
recursive-include Doc *

"""
Make sure both appear in your top level directory of the packages then you can
make a distribution using

bash python3 setup.py sdist

You can also use setuptools, distribute and other third party libraries. Keeping 
it as simple as possible means others dont need to install additional components.

"""
