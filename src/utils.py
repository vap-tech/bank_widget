from zipfile import ZipFile
import os.path as pth
import json


FILE_NAME = 'operations.zip'


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
