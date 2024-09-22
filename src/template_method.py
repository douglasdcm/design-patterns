# Defines the template structure
class TemplateClass:
    # this is the method with the invariant steps to execute something
    def template_method(self):
        op1 = self.primitive_operation1()
        op2 = self.primitive_operation2()
        op3 = self.primitive_operation3()
        return [op1, op2, op3]

    # a primitive operation can be a method that must be impletended by subclasses
    def primitive_operation1(self):
        raise NotImplementedError

    # or a method with default behavior that can be (optional) overriden by suclasses
    def primitive_operation2(self):
        return "do something default"

    def primitive_operation3(self):
        raise NotImplementedError


# This class extendes the Template and implementes the specific behavior for each operation
class ConcreteClass(TemplateClass):
    def primitive_operation1(self):
        return "do specific operation1"

    def primitive_operation3(self):
        return "do specific operation3"


def client():
    # the template method called is from the interface. As the subclass implemtents the operations, then the
    # process is the same for diffent subclasses, but the specific steps are not
    return ConcreteClass().template_method()
