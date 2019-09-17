def some_f():
    return 10

result = some_f()
print(result)

a = some_f
print(a)
print(type(a))
print(a())

def f():
    print('hello from f')

def to(f_param):
    f_param()

to(f)

# Применение Внутри функции передается алгоритм или последовательность действий либо сами действия.

def my_filter(numbers):
    result = []
    for number in numbers:
        if(number % 2 == 0):
            result.append(number)
    return result

def my_filter_params(numbers, function):
    result = []
    for number in numbers:
        if(function(number)):
            result.append(number)
    return result

def is_even(number):
    return number % 2 == 0

def is_not_even(number):
    return number % 2 != 0

def big_f(number):
    return number > 4


numbers = [1, 2, 3, 4, 5, 6, 7, 8]

print(my_filter(numbers))
print(my_filter_params(numbers, is_even))
# Если нужны нечетные числа
print(my_filter_params(numbers, is_not_even))
# Если нужны числа > 4
print(my_filter_params(numbers, big_f))


# lambda-Функции
# lambda () когда нужно записать краткую запись
print(my_filter_params(numbers, lambda number: number % 2 == 0))
print(my_filter_params(numbers, lambda number: number % 2 != 0))
print(my_filter_params(numbers, lambda number: number > 4))



