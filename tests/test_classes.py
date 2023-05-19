from src.classes import Operation
from src.utils import get_client
from tests.data_to_tests import op_data


def test_operations():
    op = Operation(123)
    assert op.id == 123
    assert op.__repr__()
    assert op.__str__()


def test_client():
    cl = get_client(op_data)
    assert cl.__repr__()
    assert isinstance(cl.get_operation(), Operation)
