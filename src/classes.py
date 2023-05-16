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
        data = [
            f'id:{self.id}',
            f'date:{self.date}',
            f'state:{self.state}',
            f'op_am:{self.op_am}',
            f'descr:{self.descr}',
            f'from_:{self.from_}',
            f'to:{self.to}'
        ]
        return ', '.join(data)

    def __str__(self):
        return f'id:{self.id}, state:{self.state}'
