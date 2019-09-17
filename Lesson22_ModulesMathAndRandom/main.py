import math
import random

r = 100
# Длина окружности
len = 2 * r * math.pi
print(len)

# Площать окружности
print(math.pi * r ** 2)
print(math.pi * math.pow(r, 2))

# найти корень
x1 = 10
y1 = 10
x2 = 50
y2 = 100
l = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print(l)
# Факториал
print(math.factorial(9))


# Загадать число от до
print(random.randint(1, 100))

# Выбрать опбедителя лотерии
players = ['Max', 'Lol', 'Leo', 'Kate']
print(random.choice(players))

# Выбрать 3 победителей
print(random.sample(players, 3))

# Перемешать карты в стопке
cards = ['6', '7', '8', '9', 'T', 'J', 'Q', 'K']
print(cards)
random.shuffle(cards)
print(cards)