from src.classes import Operation


def test_operations():
    op = Operation(123)
    assert op.id == 123
    assert op.__repr__() == 'id:123'
    assert op.__str__() == 'id:123, state:None'
