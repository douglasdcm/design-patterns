from src.adapter import client


def test_client():
    assert client() == "specific request"
