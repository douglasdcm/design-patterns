from src.state import client, TCPClose


def test_client():
    assert isinstance(client(), TCPClose)
