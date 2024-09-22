from src.template_method import client


def test_client():
    assert client() == [
        "do specific operation1",
        "do something default",
        "do specific operation3",
    ]
