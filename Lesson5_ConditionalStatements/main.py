age = int(input('Введите свой возраст: '))

if age < 18:
    print('Доступ запрещен')
elif age == 18:
    print('Вам ровно 18')
    print('Что с вами делать?')
elif age > 18 and age < 25:
    print('категория пользователей')
else:
    print('Доступ разрешен')

    if age % 5 == 0:
        print('У вас юбилей!')

print('Какие то действия')
print('end')

number = 43
value = int(input('Введите число от 1 до 100'))

if value == number:
    print('Вы угадали')
else:
    if value > number:
        print('Нужно меньше')
    else:
        print('Нужно больше')
