number = input('Введите число: ')

if number.isdigit():
    number = int(number) + 2
    print(number)
else:
    print('Введеные данные не являются числом!')