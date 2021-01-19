"""
This script shows how to join together multiple directories into one common package prefix

To do this you need to define a top level package that serves as a namespace for a large collection
of separately maintained subpackages. To unify directories under a common namespace -
organize the code like a normal python package but omit the __init__.py files where
the directories are going to join together.

See common_namespace module...

import using
import sys
sys.path.extend(['modules_and_packages/common_namespace/foo-package', 'modules_and_packages/common_namespace/bar-package'])
import spam.blah
import spam.grok

This is known as a 'namespace package'. For large frameworks this can be useful.

The key to this is to make sure there are no __init__.py files in the top level directory that serves as the common namespace.
When the __init__ is ommitted the interpreter creates a list of all directories that happen to contain a matching
package name. A namespace package module is then created and a read only copy of the list of dirs is stored in
its __path__ var.

Anyone can then extend this namespace with their own code.

A package can be identified as a namespace by checking the __file__ attribute - if its missing it is a namespace.
"""
