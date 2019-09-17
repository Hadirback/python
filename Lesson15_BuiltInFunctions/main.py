# Функция фрагмент программного кода для повторного использования кода, для создания более логичного
# использования команд


# Печать - фунция с параметрами
print('Hello, function')

# Функция без параметров но возвращает значение
name = input()

# тип переменной - функия с параметрами и возвращающим значением
t = type(123)

# Диапазон - функция с параметрами и возвращаемым значение
r = range(10)

# Длина последовательности
len([1, 2, 3, 4])

# Преобразование типов
int('10')

# abs - найти модуль числа
# main max - минимальное и максимальное число
# round - округляет число
# sum - сумма элементов последовательности
# enumerate - пронумеровать последовательность

print(abs(-7))

numbers = [1, 2, 3, 4]
print(max(numbers))
print(min(numbers))

print(round(10.234545, 2))

print(sum(numbers))

winners = ['Kate', 'Leo', 'Max']
for number, winner in enumerate(winners, 1):
    print(number, winners)


numbers2 = []
for i in range(3):
    number = int(input('Введите число: '))
    numbers2.append(number)

print(min(numbers2))
print(max(numbers2))
print(sum(numbers2))
