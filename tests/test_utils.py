from src.utils import read_operations
from src.utils import FILE_NAME


def test_read_operations():
    assert read_operations('.', '1234') == []
    assert read_operations('.', FILE_NAME) != []
