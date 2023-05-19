from src.utils import read_operations, get_client, operation_to_stdout
from src.constants import FILE_NAME, NUMBER_OF_OPERATIONS
COUNT = 5

data1 = read_operations('..', FILE_NAME)

cl = get_client(data1)

for i in range(NUMBER_OF_OPERATIONS):
    print()
    operation_to_stdout(cl.get_operation())
