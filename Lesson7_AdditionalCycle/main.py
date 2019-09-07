name = None

while True:
    name = input('Кто создатель Python?')
    if name == 'Гвидо':
        break
    print('не верно')
print('верно')
number = 0
n = int(input('Введите n'))

while number <= n:
    if number % 2 == 0:
        number += 1
        continue
    print(number)
    if number == 33 :
        break
    number += 1
else:
    print('end')

print('end program')