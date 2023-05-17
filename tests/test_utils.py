from src.utils import read_operations, get_client
from src.constants import FILE_NAME
from src.classes import Client

def test_read_operations():
    assert read_operations('.', '1234') == []
    assert read_operations('.', FILE_NAME) != []


def test_get_client():
    data = {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  }
    cl = get_client([data])
    cl2 = get_client([{}])
    assert isinstance(cl, Client)
    assert cl2.operations == []
