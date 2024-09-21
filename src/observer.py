# This observer has just one subject
class Observer:
    def __init__(self, subject) -> None:
        self._subject = subject

    def update(self, subject):
        raise NotImplementedError


class Subject:
    def __init__(self) -> None:
        self._observers: list[Observer] = []

    def attach(self, observer: Observer):
        self._observers.append(observer)

    def detach(self, observer: Observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self)


class ConcreteSubject(Subject):
    def __init__(self) -> None:
        super().__init__()
        self._subject_state = "active"

    def get_state(self):
        return self._subject_state

    def set_state(self, state):
        self._subject_state = state


class ConcreteObserver(Observer):
    def __init__(self, subject: Subject) -> None:
        super().__init__(subject)
        self._observer_state = None
        subject.attach(self)

    @property
    def state(self):
        return self._observer_state

    def update(self, subject: Subject):
        if isinstance(subject, type(self._subject)):
            self._observer_state = subject.get_state()
            # take some action depending on the subject state


def client():
    # This is the subject the observer observes
    subject = ConcreteSubject()
    # The subject is set when the observer is created
    observer = ConcreteObserver(subject)
    subject.set_state("inactive")
    # Notify the observers that the subject has changed
    subject.notify()
    return observer.state
