"""
This script shows how to navigate through a complicated data structure with different kind of objects,
where each is handled differently. i.e walking through a tree structure and performing different
actions depending on the type of tree nodes encountered.

This is done by using the visitor pattern

The example that follows is that of a mathematical expressions, that employ a number of classes
"""


class Node:
    pass


class UnaryOperator(Node):
    def __init__(self, operand):
        self.operand = operand


class BinaryOperator(Node):
    def __init__(self, left, right):
        self.left = left
        self.right = right


class Add(BinaryOperator):
    pass


class Sub(BinaryOperator):
    pass


class Mul(BinaryOperator):
    pass


class Div(BinaryOperator):
    pass


class Negate(BinaryOperator):
    pass


class Number(Node):
    def __init__(self, value):
        self.value = value


# You can then build up nested data structures as follows
t1 = Sub(Number(3), Number(4))
t2 = Mul(Number(2), t1)
t3 = Div(t2, Number(5))
t4 = Add(Number(1), t3)

# To enable general purpose processing, a visitor pattern can be implemented


class NodeVisitor:
    def visit(self, node):
        methname = "visit_" + type(node).__name__
        meth = getattr(self, methname, None)
        if meth is None:
            meth = self.generic_visit
        return meth(node)

    def generic_visit(self, node):
        raise RuntimeError("No {} method".format("visit_" + type(node).__name))


# To use - inherit from NodeVisitor and implement methods of the form visit_Name() where name is substituted by node type


class Evaluator(NodeVisitor):
    def visit_Number(self, node):
        return node.value

    def visit_Add(self, node):
        return self.visit(node.left) + self.visit(node.right)

    def visit_Sub(self, node):
        return self.visit(node.left) - self.visit(node.right)

    def visit_Mul(self, node):
        return self.visit(node.left) * self.visit(node.right)

    def visit_Div(self, node):
        return self.visit(node.left) / self.visit(node.right)

    def visit_Negate(self, node):
        return -node.operand


# Here is how you use this
e = Evaluator()
e.visit(t4)  # 0.6
