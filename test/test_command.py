from src.command import client


def test_client():
    assert client() == "do action"
