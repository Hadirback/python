while True:
    number = input('Введите число: ')

    if number.isdigit():
        number = int(number)

        if 0 < number < 10:
            power_of_number = number ** 2
            print(power_of_number)
            break
        else:
            print('Введите число больше 0, но меньше 10')
    else:
        print('Введеные данные не являются числом!')