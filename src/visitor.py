# When it is necessary to decouple the function from its classes
# Visitor allows to define new operations not changins the classes it operates over


# Interface of operations to be applied (Visitors)
# New operations are defined by new subclasses of NodeVisitor
class NodeVisitor:
    # Visit the concret element AssigmentNode
    # node: AssigmentNode
    def visit_assigment(self, node):
        raise NotImplementedError

    # node: VariableRefNode
    def visiti_variable_ref(self, node):
        raise NotImplementedError


class TypeCheckingVisitor(NodeVisitor):
    def visit_assigment(self, node):
        # specific inplementation
        return "TypeCheckingVisitor.assigment"

    def visiti_variable_ref(self, node):
        return "TypeCheckingVisitor.variable_ref"


class CodeGeneratingVisitor(NodeVisitor):
    def visit_assigment(self, node):
        return "CodeGeneratingVisitor.assigment"

    def visiti_variable_ref(self, node):
        return "CodeGeneratingVisitor.variable_ref"


# Interface for elements which the operations are going to be applied
class Node:
    def accept(self, v: NodeVisitor):
        pass


class AssigmentNode(Node):
    def accept(self, v):
        # specific implementation
        return v.visit_assigment(self)


class VariableRefNode(Node):
    def accept(self, v):
        return v.visiti_variable_ref(self)


class Program:
    node: Node = None


def client():
    result1 = AssigmentNode().accept(TypeCheckingVisitor())
    result2 = VariableRefNode().accept(TypeCheckingVisitor())
    return result1, result2
