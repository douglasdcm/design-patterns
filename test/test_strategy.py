from src.strategy import client


def test_client():
    assert client() == ("concret strategy A", "concret strategy B")
