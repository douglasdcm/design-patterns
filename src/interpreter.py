# Pattern similar to Composite, but reserved to represent Languages
# expression example 'raining & (dog | cat) repeat' matches 'raining dog dog' or
# 'raining dog cat cat' or combinations


# Holds the state of the Interperter
class Context:
    def __init__(self):
        self._interperter_state = None

    @property
    def state(self):
        return self._interperter_state

    @state.setter
    def state(self, value):
        self._interperter_state = value


# A Regular Expression
class AbstractExpression:
    def interpret(self, context: Context):
        raise NotImplementedError


# Literal Expressions (characters)
class TerminalExpressin(AbstractExpression):
    def __init__(self, components):
        self._components = components  # list of characters

    def interpret(self, context):
        return self._components


# AlternationExpression, RepetionExpression, SequenceExpression (|, &, repeat)
class NonTerminalExpression(AbstractExpression):
    # if repeat the second parameter is None
    def __init__(
        self,
        operation: str,
        param1: AbstractExpression,
        param2: AbstractExpression = None,
    ):
        self._param1: AbstractExpression = (
            param1  # can be a sequence, repeate or alternate expression 1
        )
        self._param2: AbstractExpression = (
            param2  # can be a sequence, repeate or alternate expression 2
        )
        self._operation = operation  # sequence, repeat, alternate

    # The implemtation of the interpreter depends on the rule. For example an 'and' rule would check if
    # param1 and param2 are both valid/true expressions
    def interpret(self, context):
        result = [self._operation]
        result.append(self._param1.interpret(context))
        if self._param2:
            result.append(self._param2.interpret(context))
        return result


def client():
    # interpret 'raining & (dog | cat) repeat'
    context = Context()
    raining = TerminalExpressin("raining")
    dog = TerminalExpressin("dog")
    cat = TerminalExpressin("cat")

    expression = NonTerminalExpression(
        "and",
        raining,
        NonTerminalExpression(
            "or",
            NonTerminalExpression("repeat", dog),
            NonTerminalExpression("repeat", cat),
        ),
    )
    return expression.interpret(context)
