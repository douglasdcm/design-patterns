# Interface: holds the Receiver which is the object to suffer the action
# Aa all Commands implement the "exceute" they can be executed in sequence just calling this
# method
class Command:
    def __init__(self, receiver) -> None:
        self._receiver = receiver

    def exceute(self):
        raise NotImplementedError


# Implements the interface calling the Receiver
# Example: Given that the Application handles Documents, so a concrete command could be
# PasteCommand (paste something in the document) or OpenCommand(opens the document)
class ConcretCommand(Command):
    state = None

    def exceute(self):
        return self._receiver.action()


# Knows how to execute the action
# A Document in the case o PasteCommand or an Application when is OpenCommand
class Receiver:
    def action(self):
        return "do action"


# Holds the Command and requests the action. It does not knows how to perform the actions,
# but knows who knows
# Example: A MenuItem in the Application. It calls the Command which knows what to do
class Invoker:
    def __init__(self, command: Command) -> None:
        self._command = command

    def request(self):
        return self._command.exceute()


def client():
    return Invoker(ConcretCommand(Receiver())).request()
