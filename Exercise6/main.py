import music_serialize as serialize
import music_deserialize as deserialize

my_favourite_group = {
    'name': 'Sum 41',
    'tracks': [
        'Fat Lip',
        'Still Waiting',
        'Over My Head',
        'Pieces',
        'Some Say',
        'With Me'
        'War'
    ],
    'albums': [
        {'name': 'All Killer No Filler', 'year': '2001'},
        {'name': 'Does This Look Infected?', 'year': '2002'},
        {'name': 'Chuck', 'year': '2004'},
        {'name': 'Underclass Hero', 'year': '2007'},
        {'name': '13 Voices', 'year': '2016'}
    ]
}

# Сериализуем в байты
bytes_data = serialize.serialize_to_bytes(my_favourite_group)
print(bytes_data)

# Сериализуем в json
json_data = serialize.serialize_to_json(my_favourite_group)
print(json_data)

# Сохраняем в файлы
serialize.write_bytes_data(bytes_data)
serialize.write_json_data(json_data)

# Десериализация из group.pickle
bytes_output_data = deserialize.deserialize_bytes_from_file()
print('Десериализуем данные из файла group.pickle')
print(bytes_output_data)
print(type(bytes_output_data))

# Десериализация из group.json
json_output_data = deserialize.deserialize_json_from_file()
print('Десериализуем данные из файла group.json')
print(json_output_data)
print(type(json_output_data))

# Получаем итоговый массив 2 способами
my_group1 = deserialize.deserialize_bytes(bytes_output_data)
print('Десериализуем данные из переменной bytes_output_data')
print(my_group1)
print(type(my_group1))

my_group2 = deserialize.deserialize_json(json_output_data)
print('Десериализуем данные из переменной json_output_data')
print(my_group2)
print(type(my_group2))

