# dump - сохранение объекта в формате json в фаил
# dumps - преобразование объекта в json в текст
# load - загрузка объекта из файла
# loads - загрузка объекта из формата json
import json
friends = [
    {'name': 'Max', 'age': 23, 'phones': [123, 345]},
    {'name': 'Leo', 'age': 33}
]

# тип объекта
print(type(friends))

# преобразование списка друзей в json
json_friends = json.dumps(friends)

print(json_friends)
print(type(json_friends))


friends = json.loads(json_friends)
print(type(friends))

with open('friends.jon', 'w') as f:
    json_friends = json.dump(friends, f)

with open('friends.jon', 'r') as f:
    friends = json.load(f)

print(friends)
print(type(friends))

favourite_tracks = [
    {'name': 'Вечная любовь', 'artist': 'Агата Кристи'},
    {'name': 'Angel', 'artist': 'Massive Attack'},
    {'name': 'Jamming', 'artist': 'Bob Marley'}
]

with open('tracks.json', 'w', encoding='utf-8') as f:
    json.dump(favourite_tracks, f)


print('Выполнено!')