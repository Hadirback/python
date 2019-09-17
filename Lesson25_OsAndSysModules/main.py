# Модуль OS содержит функции для работы с операционной системой
# name - имя операционной системы
# chdir - смена текущей директории
# getcwd() - текущая рабочая директория
# mkdir() - создание директории
# os.path - модуль для работы с путями

import os
import sys
import math

print(os.name)

print(os.getcwd())

# создаем новый путь
new_path = os.path.join(os.getcwd(), 'new_f')
# create folder

# os.mkdir(new_path)

# модуль sys взаимодействие с интерпретатором python
# executable - путь к интерпретатору python
# exit() - выход из python
# platform - информация об ОС
# path - список путей поиска модулей
# args - список аргументов командной строки
print(sys.executable)
print(sys.platform)
# sys.exit()

# print('Этот код мы не выполним')

print(sys.path)

print(type(sys.path))

for path in sys.path:
    print(path)


# как подключит свой модуль если в списке нет модуля в данном списке
# sys.path.append('D:')

name = sys.platform

for i in range(1, 6):
    new_path = os.path.join(os.getcwd(), '{}_{}'.format(name, i))
    os.mkdir(new_path)