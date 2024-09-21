from src.observer import client


def test_client():
    assert client() == "inactive"
