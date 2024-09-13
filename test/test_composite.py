from src.composite import client
from pytest import raises


def test_cliet():
    composite, leaf = client()
    assert composite.get_children(0) is not None
    with raises(NotImplementedError):
        leaf.get_children(0)
    assert composite.draw() == ["draw line", "draw text"]
