# Interface for the adapter
class Target:
    def request(self):
        raise NotImplementedError


# Colaborator to be adapted the the Target interface
# Has its own interface
class Adaptee:
    def specific_request(self):
        return "specific request"


# Adapats the Adaptee to the interface of the Adapert (Target)
class Adapter(Target):
    # In languages where multiple inheritance is allowed, it is not necessary to use composition
    # The Adapter can inherit from the target and from the adaptee
    adaptee = Adaptee()

    def request(self):
        # Calls the request from adaptee. Kind of a translator
        return self.adaptee.specific_request()


def client():
    adapter = Adapter()
    return adapter.request()
