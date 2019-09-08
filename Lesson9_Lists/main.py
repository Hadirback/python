# Пустой список
empty_list = []

friends = ['Max', 'Leo', 'Kate']

# тип данных
print(type(friends))

print(friends[1])
# С конца
print(friends[-1])

# срезы
print(friends[1:3])
print(friends[:2])
print(friends[1:])

print(len(friends))
friends.append('Ron')
friend = friends.pop(3)
print(friend)
friends.remove('Leo')
print(friends)
friends.append('Ron')
del friends[1]
print(friends)


print('Max' in friends)

hero = 'Superman'
if 'man' in hero:
    print('Усть!')