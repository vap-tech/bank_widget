from src.classes import Operation


def test_operations():
    op = Operation(123)
    assert op.id == 123
    assert 'id:123' in op.__repr__()
    assert op.__str__() == 'id:123, state:None'