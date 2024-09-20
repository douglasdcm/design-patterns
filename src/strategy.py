class Strategy:
    def execute(self):
        raise NotImplementedError


class ConcretStrategyA(Strategy):
    def execute(self):
        return "concret strategy A"


class ConcretStrategyB(Strategy):
    def execute(self):
        return "concret strategy B"


class ConcretStrategyC(Strategy):
    def execute(self):
        return "concret strategy C"


class Context:
    def __init__(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def action(self):
        return self._strategy.execute()


def client():
    strategy_a = ConcretStrategyA()
    strategy_b = ConcretStrategyB()
    # The client need to know the stregy they want to use and pass them to the
    # context class. The context class hold the strategy in a private variable
    # and runs the strategy action via the command "execute"
    context = Context(strategy_a)
    action_a = context.action()

    # changes the strategy
    context = Context(strategy_b)
    action_b = context.action()

    return action_a, action_b
