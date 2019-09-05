print(True)
print(None)
print(9.9)

name = 'Кеша'
age = 2

print(name, age)
print(name, age, sep='/')
print(name, age, sep='/;h')

print('-------->')
print(name, end=';')
print(age, end=';')

result = input()
print('Пользователь ввел', result)
name = input('Как тебя зовут')
print('Привет', name)

age_my = int(input('Сколько вам лет?'))
print(type(age_my))

period_new = 20
age_period = age_my + period_new

print('Через', period_new, 'вам будет', age_period)

is_love = input('Вы любите python?')
print(type(is_love))
