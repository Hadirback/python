# Список аргументов командной строки при запуске скпирта python
# sys.argv[0] - путь до скрипта
# Остальные параметы передатся при вызове через пробел
# python main.py par1 par2 par3

import sys

print(sys.argv[0])

for arg in sys.argv:
    print(arg)
    print(type(arg))