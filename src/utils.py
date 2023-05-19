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


def hide_schet(data):
    """Маскирует строку "счет №", если на входе None -> пустая строка"""
    if not data:
        return ''
    lst = data.split(' ')
    if len(lst[-1]) == 20:
        return f'Счет **{lst[1][-4:]}'
    elif len(lst[-1]) == 16:
        return f"{' '.join(lst[:-1])} {lst[-1][:4]} {lst[-1][4:6]}** **** {lst[-1][-4:]}"


def operation_to_stdout(op: Operation):
    """Выводит на экран форматированое инфо об операциях"""
    print(op.date_t.strftime('%d.%m.%Y'), op.descr)
    print(hide_schet(op.from_), end='')
    print(bool(op.from_) * ' -> ', end='')
    print(hide_schet(op.to))
    print(op.op_am['amount'], op.op_am['name'])
    return 0
