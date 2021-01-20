"""
This script shows how to reload an already loaded module because you have made changes to the source.

This is often used during debugging and development - but not safe in production as it does not
always work as expected.

reload wipes out the contents of a modules underlying dictionary and refreshes it by re-executing the modules source
code.reload() does not update definitions that have been imported using statements such as 'from module import name'
"""
import spam
import imp

imp.reload(spam)

"""
If you import using from x import y you will end up with two copies of the function y() imported if you use 
reload().

from spam import x
imp.reload(spam)

you will have two versions of x() 
"""
