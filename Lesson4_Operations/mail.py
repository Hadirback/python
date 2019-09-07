ale = 71
age = int(input('Сколько вам лет?'))

# +
after20 = age + 20
print('Через 20 лет вам будет', after20)

# -
alive = ale - age
print('По статистике вам осталось жить', alive)

# +
count = 144000000
all_alive = count * ale
print('Среднее врямя жизни всех людей', all_alive)

# /
live_part = age / ale
print('Часть прожитой жизни', live_part)

print(type(live_part))

# // Целая часть
live_part = age//ale
print(live_part)
# % остаток от деления
print(3%2)
print(4%2)
print(5%2)

# ** Возведение в степень
print(2**10)
print(2**2)

print(ale == age)
print(ale != age)
print(age < ale)
print(age > ale)
print(age <= ale)
print(age >= ale)

print('У вас юбилей', age % 5 == 0)

print('У ваc не юбилей', age % 5 != 0)
print('У вас не юбилей', not age % 5 == 0)

print('У вас юбилей и ваш возраст меньше средней продоложительности жизни:', age % 5 == 0 and age < ale)
print('У вас юбилей или ваш возраст меньше средней продоложительности жизни:', age % 5 == 0 or age < ale)

print((1 > 2 and (0 < 5 or 0 < 2) and 2 > 1))
