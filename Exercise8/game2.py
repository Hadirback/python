import random


def computer_guesses_number():
    start_number = 1
    end_number = 100

    operation_list = ['i', 'r', 'e']
    count = 0

    print('Компьютер попытвется угадать число!')
    print('Введите букву I(increase), если число компьютера меньше загаданного ')
    print('Введите букву R(reduce), если число компьютера больше загаданного')
    print('Введите букву E(equally) если это загаданное число')
    input('Загадайте число от 1 до 100 и нажмите ENTER.')

    while True:
        count += 1
        number = None

        if start_number == end_number:
            number = start_number
        elif start_number > end_number:
            print('Вы забыли свое число? Начните заново!')
            break
        else:
            number = random.randint(start_number, end_number)

        print(f'Компьютер выводит число {number}')
        operation = None
        while True:
            operation = input('Если число компьютера меньше - (I), больше - (R) или равно - (E)?').lower()
            if not (operation in operation_list):
                print('Неизвестная операция, повторите ввод')
            else:
                break

        if operation == 'e':
            print(f'Компьютер угадал ваше число с {count} попытки')
            break
        elif operation == 'i':
            start_number = number + 1
        elif operation == 'r':
            end_number = number - 1








