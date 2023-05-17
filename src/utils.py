from src.classes import Operation, Client
from datetime import datetime
from zipfile import ZipFile
import os.path as pth
import json


def read_operations(lvl: str, filename: str) -> list:
    """
    Функция получает данные из архива
    :param lvl: путь к папке файла
    :param filename: имя файла
    :return: данныt из json в виде списка
    """

    abspath = pth.join(lvl, filename)

    if not pth.isfile(abspath):
        return []

    with ZipFile(abspath, 'r') as myzip:
        data = myzip.read(myzip.infolist()[0].filename)
        return json.loads(data)


def get_client(data: list) -> Client:
    """
    Инициализирует клиента, наполняя его поле операций
    :param data: Список из операций
    :return: Объект класса Client
    """
    client = Client()  # Создаем объект класса Client
    for item in data:

        if not item.get('id'):  # Если нет id, ничего не делаем
            continue
        # Создаем объект класса Operation и набиваем его поля данными
        op = Operation(int(item.get('id')))
        op.state = item.get('state')
        data = item.get('date')
        op.date_t = datetime.strptime(data.split('.')[0], '%Y-%m-%dT%H:%M:%S')
        op_am = item.get('operationAmount').get('currency').get('name')
        op.op_am = {'amount': item.get('operationAmount').get('amount'), 'name': op_am}
        op.descr = item.get('description')
        op.from_ = item.get('from')
        op.to = item.get('to')
        client.add_operation(op)  # Добавляем объект операции клиенту
    return client
