def square_number(input_number):
    if 1 > input_number or input_number > 100:
        raise Exception('Число должно быть в интервале от 1 до 100')

    if input_number == 13:
        raise ValueError('Число 13!')

    return input_number ** 2


while True:
    number = input('Введите число: ')

    try:
        new_value = square_number(int(number))
    except ValueError as e:
        print(f'Ошибка в функции square_number! Type: ValueError Message: {e}')
    except Exception as e:
        print(f'Ошибка в функции square_number! Type: Exception Message: {e}')
    else:
        print(f'Квадрат числа {number} равен {new_value}')
        break
