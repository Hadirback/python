# [ number for number in numbers if number > 0]

numbers = [1, 2, 3, 4, 5, -1, -2, -3]

# классический способ
result = []
for number in numbers:
    if number > 0:
        result.append(number)

print(result)

# через функцию filter
result = filter(lambda number: number > 0, numbers)
print(list(result))

# Через генератор
result = [number for number in numbers if number > 0]
print(result)


pairs = [(1, 'a'), (2, 'B'), (3, 'c')]

# классический способ
result = {}
for pair in pairs:
    key = pair[0]
    val = pair[1]
    result[key] = val

print(result)


result = {pair[0]: pair[1] for pair in pairs}
print(result)


# создать список случайных чисел от 1 до 100
import random
numbers = [random.randint(1, 100) for i in range(10)]
print(numbers)

# создать список квадратов числе
numbers = [1, 2, 3, -4]

pow_numbers = [number ** 2 for number in numbers]
print(pow_numbers)

# создать списко имен на букву А
names = ['Руслан', 'Дмитрий', 'Алексей', 'Андрей']

names_filter = [name for name in names if name.startswith('А')]
print(names_filter)