"""
This script shows how to exercise precise control over the symbols exported from a module
or package when a user uses the from module import * statement

This is done using a variable __all__ in the module that explicitly lists the exported names.
import * is strongly discouraged - yet still used. If you do nothing all names that don't
start with an underscore will be exported.

Where __all__ is defined - only the names explicitly listed will be exported.

Where __all__ is defined as an empty list - nothing will be exported.

AttributeError is raised on import if __all__ contains undefined names
"""


def spam():
    pass


def grok():
    pass


blah = 42

# Only export 'spam' and 'grok'

__all__ = ["spam", "grok"]
