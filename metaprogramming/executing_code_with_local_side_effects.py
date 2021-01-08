"""
This script shows how to pull on the result of an exec function
"""

a = 13
exec("b = a + 1")
print(b)

# Inside a function - a NameError is thrown
def test():
    a = 13
    exec("b = a + 1")
    print(b)


"""
To pull on the result you must use the locals() function to obtain a dictionary
of the local variables prior to the call to exec
"""


def testWithLocals():
    a = 13
    loc = locals()
    exec("b = a + 1")
    b = loc["b"]
    print(b)


"""
When using exec it is advisable to pass in your own dictionary and 
pass it in - as follows
"""


def testWithPassedDict():
    a = 13
    loc = {"a": a}
    glb = {}
    exec("b = a + 1", glb, loc)
    b = loc["b"]
    print(b)


testWithPassedDict()

# Ideally - instead of exec you use closures, decorators, metaclasses or other metaprogramming features
