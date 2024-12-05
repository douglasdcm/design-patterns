from src.interpreter import client


def test_client():
    assert client() == ["and", "raining", ["or", ["repeat", "dog"], ["repeat", "cat"]]]
