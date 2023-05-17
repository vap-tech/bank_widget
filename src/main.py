from src.utils import read_operations, get_client
from src.constants import FILE_NAME


data1 = read_operations('..', FILE_NAME)

cl = get_client(data1)

[print(i) for i in cl.operations]
