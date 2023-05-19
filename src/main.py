from src.utils import read_operations, get_client, operation_to_stdout
from src.constants import FILE_NAME, NUMBER_OF_OPERATIONS
COUNT = 5

data1 = read_operations('..', FILE_NAME)  # Читаем файлик в список

cl = get_client(data1)  # Инициируем клиента с данными из шага выше

data = [cl.get_operation() for i in range(NUMBER_OF_OPERATIONS)]  # list из операций
revers_data = data[::-1]  # Реверс этого листа

for i in revers_data:  # Печать этого листа через пустую строку
    print()
    operation_to_stdout(i)
