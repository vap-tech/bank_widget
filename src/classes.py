class Operation:
    """
    Абстракция операции.
    """

    def __init__(self, id_tr):
        """
        Инициализация класа.
        :param id_tr: id операции обязателен
        """
        self.id = id_tr
        self.state: str = ''  # EXECUTED` — выполнена, `CANCELED` — отменена.
        self.date: str = ''
        self.op_am = {}  # сумма операции и валюта
        self.descr: str = ''  # описание типа перевода
        self.from_: str = ''  # откуда(может отсутстовать)
        self.to: str = ''  # куда

    def __repr__(self):
        data = [
            f'id:{self.id}',
            f'state:{self.state}',
            f'date:{self.date}',
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
            f'{self.date}',
            f'{self.op_am}',
            f'{self.descr}',
            f'{self.from_}',
            f'{self.to}'
        ]
        return ', '.join(data)
