"""
This script shows how to apply decorators to functions in an existing module, but only doing this
when the module is imported and used.

An example of this would be executing a callback when a module is imported
"""
import importlib
import sys
from collections import defaultdict

_post_import_hooks = defaultdict(list)


class PostImportFinder:
    def __init__(self):
        self._skip = set()

    def find_module(self, fullname, path=None):
        if fullname in self._skip:
            return None
        self._skip.add(fullname)
        return PostImportLoader(self)
