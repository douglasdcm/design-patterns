from src.visitor import client


def test_client():
    assert client() == (
        "TypeCheckingVisitor.assigment",
        "TypeCheckingVisitor.variable_ref",
    )
