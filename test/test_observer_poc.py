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


class UpgrpSubject(Subject):
    def __init__(self) -> None:
        super().__init__()
        self._subject_state = "inactive"
        self._schedule = None

    @property
    def state(self):
        return self._subject_state

    @state.setter
    def state(self, value):
        self._subject_state = value

    @property
    def schedule(self):
        return self._schedule

    @schedule.setter
    def schedule(self, value):
        self._schedule = value


class ScheduleSubject(Subject):
    def __init__(self) -> None:
        super().__init__()
        self._executions = []
        self._subject_state = "active"

    @property
    def state(self):
        return self._subject_state

    @state.setter
    def state(self, value):
        self._subject_state = value

    @property
    def executions(self):
        return self._executions

    @executions.setter
    def executions(self, value):
        self._executions = value


class SysinSubject(Subject):
    def __init__(self) -> None:
        super().__init__()
        self._subject_state = "active"

    @property
    def state(self):
        return self._subject_state

    @state.setter
    def state(self, state):
        self._subject_state = state


class SysinvObserver(Observer):
    def __init__(self, subject: Subject) -> None:
        super().__init__(subject)
        self._observer_state = None
        subject.attach(self)

    @property
    def state(self):
        return self._observer_state

    def add_subject(self, subject: Subject):
        subject.attach(self)

    def update(self, subject: Subject):
        if isinstance(subject, type(self._subject)):
            self._observer_state = subject.state
            # take some action depending on the subject state


class UpgrpObserver(Observer):
    def __init__(self, subject: Subject) -> None:
        super().__init__(subject)
        self._observer_state = None
        subject.attach(self)

    @property
    def state(self):
        return self._observer_state

    def update(self, subject: Subject):
        if isinstance(subject, type(self._subject)):
            self._observer_state = subject.state
            # take some action depending on the subject state


def test_sysinv_observer():
    upgrp_subject = UpgrpSubject()
    sysinv_observer = SysinvObserver(upgrp_subject)
    upgrp_subject.state = "active"
    upgrp_subject.notify()
    assert sysinv_observer.state == "active"


def test_upgrp_observer():
    subject = SysinSubject()
    observer = UpgrpObserver(subject)
    subject.state = "failed"
    subject.notify()
    assert observer.state == "failed"


def test_schedule_observer():
    subject = ScheduleSubject()
    observer = UpgrpObserver(subject)
    subject.schedule = {"date": "today and now", "count": 10}
    subject.executions = ["e1", "e2"]
    subject.notify()

    assert observer.state == "active"
