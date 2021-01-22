import pkgutil

data = pkgutil.get_data(__package__, "somedata.dat")

"""
The above code results in the data variable containing a byte string containing 
the raw contents of the file.

Using built in I/O functions such as open() can lead to issues.
A package has little control over the current working directory 
of the interpreter - so absolute filenames have to be used.

packages are also installed as .zip or .egg files 
which dont preserve the files in the same way as a filesystem.

pkgutil.get_data() is a high level tool for getting a datafile regardless
of where or how a package has been installed - it simply works

The first argument to get_data() is a string containing the package name.
The second argument is the relative name of the file within the package. You 
can navigate into different directories using standard unix filename 
conventions as long as the final directory is still located within the package
"""
