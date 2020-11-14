"""
This pattern shows how to traverse a deeply nested data structure using the visitor pattern without exceeding the
maximum recursion limit in Python.

The use of generators can eliminate recursion from algos that use tree traversal or searching. The following
code uses a stack and generators to implement the visitor pattern.
"""
import types


class Node:
    pass


class NodeVisitor:
    def visit(self, node):
        stack = [node]
        last_result = None
        while stack:
            try:
                last = stack[-1]
                if isinstance(last, types.GeneratorType):
                    stack.append(last.send(last_result))
                    last_result = None
                elif isinstance(last, Node):
                    stack.append(self._visit(stack.pop()))
                else:
                    last_result = stack.pop()
            except StopIteration:
                stack.pop()
        return last_result

    def _visit(self, node):
        methname = "visit_" + type(node).__name__
        meth = getattr(self, methname, None)
        if meth is None:
            meth = self.generic_visit
        return meth(node)

    def generic_visit(self, node):
        raise RuntimeError("No {} method".format("visit_" + type(node).__name__))


"""
This code is a droop in replacement for the NodeVisitor implemented as part of 'implementing_visitor_pattern.py'
In this previous example the class Evaluator can be tweaked to ensure that we don't hit those recursion limits
by using 'yield'
"""


class Evaluator(NodeVisitor):
    def visit_Number(self, node):
        return node.value

    def visit_Add(self, node):
        yield (yield node.left) + (yield node.right)

    def visit_Sub(self, node):
        yield (yield node.left) - (yield node.right)

    def visit_Mul(self, node):
        yield (yield node.left) * (yield node.right)

    def visit_Div(self, node):
        yield (yield node.left) / (yield node.right)

    def visit_Negate(self, node):
        yield -(yield node.operand)


"""
In the above example it is shown how generators and co routines can manipulate control flow to create 
more performant code.

Where you are doing tree traversal a strategy to avoid recursion is to use a stack or queue. 
Depth first traversal can be implemented by pushing nodes onto a stack and popping them 
off when finished.
The stack will be as large as the tree.

When yield is encountered - the behaviour of the generator is to emit and suspend.

Therefore instead of writing
value = self.visit(node.left)

You write:
value = yield node.left

This sends the node in question to the visit() method. This carries out the execution. Instead of 
calling visit() recursively the yield statement temporarily backs out of the computation progress. 
This is a signal that tells the algorithm that the yielded node needs to be process before proceeding.

When generators are used - you cannot use return statements to emit values. Instead yield covers this off.


"""
