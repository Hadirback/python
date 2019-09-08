say = 'say "Hello"'
print(say)
say = "say 'Hello'"
print(say)

friend = 'Максим Леонид'
first_letter = friend[0]
print('Первая буква имени твоего друга', first_letter)
print(type(first_letter))

print(friend[1])
print(friend[-1])

# Срез
print(friend[2:4])
print(friend[:4])
print(friend[2:])

# длина строки
print(len(friend))
print(friend.find('а'))
print(friend.split())
print(friend.upper())
print(friend.lower())

friend2 = 'Мак; Афв'
print(friend2.split(';'))

# Все методы
help(friend2)
name = 'Вася'
age = 23
hello_str = 'Привет %s тебе %d лет' % (name, age)
print(hello_str)
hello_str2 = 'Привет {} тебе {} лет'.format(name, age)
print(hello_str2)

top5 = 'Первые 5 мест на соревнованиях: 1. иванов 2. петров 3. сидоров 4. орлов 5. соколов'
start = top5.find('1')
end = top5.find('4')
top3 = top5[start : end - 1]
result = 'Поздравляем {} с успехом!'. format(top3.upper())
print(result)