# sorted сортирует последовательность
# sorted(iterable, *, kay=None, reverse=False) последовательность и ключ, можем изменять порядок сортировки



numbers = [1, 5, 6, 3, 78, 3]

print(sorted(numbers))
print(sorted(numbers, reverse=True))

names = ['Max', 'Ole', 'Ali']
print(sorted(names))

cities = [('Москва', 1000), ('Лас-Вегас', 500), ('Антверпен', 2000)]
print(sorted(cities))

# функция для определения сортировки
def by_count(city):
    return city[1]

print(sorted(cities, key=by_count))
print(sorted(cities, key=lambda city: city[1]))

# filter (function, iterable)

numbers = (1, 2, 3, 4, 5, 6, 7, 8)

def is_even(number):
    return number % 2 == 0

result = filter(is_even, numbers)
print(result)
print(type(result))
print(list(result))

names = ['Max', 'Leo', 'Kate']

print(list(filter(lambda x: len(x) > 3, names)))

# map - Применяет функцию к каждому элетенту последовательности
# map(func, iterable)

numbers = [5, 76, 3, 2, 8]

# Получение квадратов для каждого числа
print(type(map(lambda x: x ** 2, numbers)))
print(list(map(lambda x: x ** 2, numbers)))

print(list(map(lambda x: str(x), numbers)))