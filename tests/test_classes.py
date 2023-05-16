from src.classes import Operation, Client


def test_operations():
    op = Operation(123)
    assert op.id == 123
    assert 'id:123' in op.__repr__()
    assert '123' in op.__str__()


def test_client():
    cl = Client()
    cl.add_operation('12')
    cl.add_operation('hi')
    assert cl.operations[0] == '12'
    assert cl.operations[1] == 'hi'
    assert cl.__repr__() == '12, hi'
