class Operation:
    """
    Абстракция операции.
    """

    def __init__(self, id_tr: int):
        """
        Инициализация класа.
        :param id_tr: id операции обязателен
        """
        self.id: int = id_tr
        self.state: str = ''  # EXECUTED` — выполнена, `CANCELED` — отменена.
        self.date_t = None  # Объект класса datetime
        self.op_am = {}  # сумма операции и валюта
        self.descr: str = ''  # описание типа перевода
        self.from_: str = ''  # откуда(может отсутстовать)
        self.to: str = ''  # куда

    def __repr__(self):
        data = [
            f'id:{self.id}',
            f'state:{self.state}',
            f'datetime:{self.date_t}',
            f'op_am:{self.op_am}',
            f'descr:{self.descr}',
            f'from_:{self.from_}',
            f'to:{self.to}'
        ]
        return ', '.join(data)

    def __str__(self):
        data = [
            f'{self.id}',
            f'{self.state}',
            f'{self.date_t}',
            f'{self.op_am}',
            f'{self.descr}',
            f'{self.from_}',
            f'{self.to}'
        ]
        return ', '.join(data)


class Client:
    """
    Абстракция клиента
    """
    def __init__(self):
        self.operations: list = []

    def __repr__(self):
        """
        __repr__
        :return: Список из всех операций клиента
        """
        return ', '.join(self.operations)

    def add_operation(self, operation):
        """
        Добавляет операцию клиенту
        :param operation: сама операция
        :return: None
        """
        self.operations.append(operation)

    def get_operation(self):
        op_addr = 0
        for i in range(len(self.operations)):
            if self.operations[i].date_t < self.operations[op_addr].date_t:
                op_addr = i
        return self.operations.pop(op_addr)
