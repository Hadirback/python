# 1: Создать модуль music_serialize.py.
# В этом модуле определить словарь для вашей любимой музыкальной группы, например:
# my_favourite_group = {
# 'name': 'Г.М.О.',
# 'tracks': ['Последний месяц осени', 'Шапито'],
# 'Albums': [{'name': 'Делать панк-рок','year': 2016},
# {'name': 'Шапито','year': 2014}]}
# С помощью модулей json и pickle сериализовать данный словарь в json и в байты,
# вывести результаты в терминал. Записать результаты в файлы group.json, group.pickle соответственно.
# В файле group.json указать кодировку utf-8
import os

my_favourite_group = {
    'name': 'Г.М.О.',
    'tracks': ['Последний месяц осени', 'Шапито'],
    'Albums': [
        {'name': 'Делать панк-рок', 'year': 2016},
        {'name': 'Шапито', 'year': 2014}
    ]
}

import json
import pickle

with open('group.pickle', 'wb') as f:
    pickle.dump(my_favourite_group, f)

with open('group.json', 'w', encoding='utf-8') as f:
    json.dump(my_favourite_group, f)

with open('group.json', 'r', encoding='utf-8') as f:
    print(f.read())

with open('group.pickle', 'rb') as f:
    print(f.read())

with open('group.json', 'r', encoding='utf-8') as f:
    my_favourite_group = json.load(f)

print(my_favourite_group, type(my_favourite_group))

with open('group.pickle', 'rb') as f:
    my_favourite_group = pickle.load(f)

print(my_favourite_group, type(my_favourite_group))


def deserialize_bytes_from_file():
    if os.path.exists(os.path.join(os.getcwd(), 'group.pickle')):
        with open('group.pickle', 'rb') as f:
            return pickle.load(f)
    else:
        print('File is not exists! Method deserialize_bytes_from_file')
        return None

def write_bytes_data(b_data):
    if b_data:
        with open('group.pickle', 'wb') as f:
            pickle.dump(b_data, f)
    else:
        print('Empty data! Method write_bytes_data')


def serialize_to_bytes(group):
    if group:
        return pickle.dumps(group)
    else:
        print('Empty dict - my favourite group! Method serialize_to_bytes')
        return None


sdfsdsdfdsdfsd = serialize_to_bytes(my_favourite_group)
print(type(sdfsdsdfdsdfsd))

write_bytes_data(sdfsdsdfdsdfsd)

asdasd = deserialize_bytes_from_file()
print(asdasd)
