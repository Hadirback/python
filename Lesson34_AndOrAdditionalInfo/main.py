# Приведение типов к bool в python
# True - не пустая строки, список, кортеж словарь, не равен 0
# false  - '', (), {}, [], 0, None

# and не проверяет следующие логическое выражение если текущее равно false
# оператор and возвращает первый ложный элемент или последний истинный
import math
if 1 > 2 and math.sqrt(-1):
    print('Ошибки не будет')
print('двигаемся дальше')

print([1] and [2] and '' and 1)
print([1] and 1 and 20 and 1.1 and [1])

if 2 > 1 or math.sqrt(-1):
    print('Ошибки не будет')
print('двигаемся дальше')

print(0 or [] or 8 or 5)

numbers = [4, 1, 3, 2, -4, -2, 7, 16]

result = []
for number in numbers:
    if number > 0:
        sqrt = math.sqrt(number)

        if sqrt < 2:
            result.append(number)

print(result)

result = []
for number in numbers:
    if number > 0 and math.sqrt(number) < 2:
        result.append(number)

print(result)


result = [number for number in numbers if number > 0 and math.sqrt(number) < 2]
print(result)

def add_to_list(input_list = None):
    if input_list is None:
        input_list = []
    input_list.append(2)
    return input_list

result = add_to_list([0, 1])
print(result)
result = add_to_list()
print(result)

# через or
def add_to_list(input_list = None):
    input_list = input_list or []
    input_list.append(2)
    return input_list

result = add_to_list([0, 1])
print(result)
result = add_to_list()
print(result)