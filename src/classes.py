class Operation:

    def __init__(self, id_tr):
        self.id = id_tr
        self.date = None
        self.state = None  # EXECUTED` — выполнена, `CANCELED` — отменена.
        self.op_am = {}  # сумма операции и валюта
        self.descr: str = ''  # описание типа перевода
        self.from_: str = ''  # откуда(может отсутстовать)
        self.to: str = ''  # куда
        pass

    def __repr__(self):
        return f'id:{self.id}'

    def __str__(self):
        return f'id:{self.id}, state:{self.state}'
