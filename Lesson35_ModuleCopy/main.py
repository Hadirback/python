a = 1
b = a
b = 100
print(a)

asd = {'d': 2, 'g': 1}
dfg = asd
asd['g'] = 4
print(dfg)

a = [1, 2, 3]
b = a
b[1] = 100
print(a)

numbers = [1, 2, 3]

def change_number_in_list(input_list):
    input_list[1] = 200


change_number_in_list(numbers)
print(numbers)

# первый способ скопировать список - использовать срез [:]
# второй способ - copy

a = [1, 2, 3]

b = a[:]
b[1] = 200
print(a)
print(b)

c = a.copy()
c[1] = 200
print(a)
print(c)

# Способы не будут работать если у нас есть вложенные списки
a = [1, 2, [1, 2]]
b = a[:]
b[2][1] = 200
print(a)

b = a.copy()
b[2][1] = 200
print(a)

# Модуль copy

import copy
a = [1, 2, [1, 2]]

b = copy.deepcopy(a)
b[2][1] = 200
print(a)