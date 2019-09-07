name = input('Кто создал Python?')

while name != 'Гвидо':
    print('не верно')
    name = input('Кто создал Python?')

print('Верно')

number = 0
n = int(input('Введите n'))
while number <= n:
    print(number)
    number += 1

while number <= n:
    # Четные числа
    if number % 2 == 0:
        print(number)
    # Нечетные числа

    number += 1

