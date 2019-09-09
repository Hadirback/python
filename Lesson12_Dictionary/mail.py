# dict my_dict = {key1:val1, key2:val2, ...}

friends = {
    'name': 'Max',
    'age': 23
}

print(friends)
print(type(friends))
print(friends['name'])
friends['has_car'] = True
print(friends)
friends['has_car'] = False
print(friends)
del friends['age']
print(friends)

if 'age' in friends:
    print('Есть возраст')

if 'name' in friends:
    print('Есть Name ')

friends['age'] = 23

for key in friends.keys():
    print(key, friends[key])

for value in friends.values():
    print(value)

for item in friends.items():
    print(item)
    print(type(item))

for key, val in friends.items():
    print(key, val)