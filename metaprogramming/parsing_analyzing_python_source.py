"""
This script shows how to parse and analyze Python source code.

Using the ast module - you can compile Python source code into
an abstract syntax tree (AST) that can be analyzed.
"""
import ast

ex = ast.parse("2 + 3*4 + x", mode="eval")
ex  # <_ast.Expression object at 0x104dbfbb0>
ast.dump(ex)

"""
"Expression(body=BinOp(left=BinOp(left=Constant(value=2, kind=None),
op=Add(), right=BinOp(left=Constant(value=3, kind=None),
op=Mult(), right=Constant(value=4, kind=None))),
op=Add(), right=Name(id='x', ctx=Load())))

The easiest way to work with the AST nodes is defining a vistor class
that implements visit_NodeName() methods - where the NodeName()
is substituted with the node of interest. The code example below 
shows a class that records information about which names are loaded,
stored and deleted.
"""


class CodeAnalyzer(ast.NodeVisitor):
    def __init__(self):
        self.loaded = set()
        self.stored = set()
        self.deleted = set()

    def visit_Name(self, node):
        if isinstance(node.ctx, ast.Load):
            self.loaded.add(node.id)
        elif isinstance(node.ctx, ast.Store):
            self.stored.add(node.id)
        elif isinstance(node.ctx, ast.Del):
            self.deleted.add(node.id)


# Sample usage
if __name__ == "__main__":
    # Some Python code
    code = """
    for i in range(10):
        print(i)
    del i
    """
    # Parse into an AST
    top = ast.parse(code, mode="exec")

    # Feed the AST to analyze name usage
    c = CodeAnalyzer()
    c.visit(top)
    print("Loaded:", c.loaded)
    print("Stored", c.stored)
    print("Deleted", c.deleted)

# ASTs can be compiled and executed using the compile() function
exec(compile(top, "<stdin>", "exec"))
