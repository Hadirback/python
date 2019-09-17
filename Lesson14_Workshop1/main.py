# шаг 1 загадать случайное число
import random

number = random.randint(1, 100)
user_number = None
count = 0

levels = {1: 10, 2: 5, 3: 3}
level = int(input('Выберете уровень сложности: '))

max_count = levels[level]

user_count = int(input('Введите количество пользователей: '))
users = []
for i in range(user_count):
    user_name = input(f'Введите имя  пользователя {i + 1}: ')
    users.append(user_name)
is_winner = False
winner_name = None

while not winner_name:
    # шаг 2 ввод числа
    count += 1

    if count > max_count:
        print('Все пользователи проиграли!')
        break
    print(f'Попытка № {count}')
    for user in users:
        print(f'ход пользователя {user}')
        user_number = int(input('Введите число'))

        # шаг 3 проверка равенства чисел
        if number == user_number:
            is_winner = True
            winner_name = user
            break
        elif number < user_number:
            print('Вы ввели число больше загаданного!')
        else:
            print('Вы ввели число меньшее чем загаданного!')
else:
    print(f'Победил {winner_name}! ')
