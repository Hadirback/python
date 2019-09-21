# Сериализация - это процесс преобразования объекта в поток
# байтов для сохранения или передачи в память, БД или файл
# при сохранении и передачи сложного объекта

person = {'name': 'Max', 'phones': [123, 234]}

with open('person.dat', 'wb') as f:
    # например запишем объект в файил построчно
    name = person['name']
    f.write(f'{name}\n'.encode('utf-8'))
    phones = person['phones']

    for phone in phones:
        f.write(f'{phone}\n'.encode('utf-8'))

print('объект записан')

with open('person.dat', 'rb') as f:
    result = f.readlines()

person = {}
person['name'] = result[0].decode('utf-8').replace('\n', '')

phones = []
for bphone in result[1:]:
    phones.append(bphone.decode('utf-8').replace('\n', ''))

person['phones'] = phones
print(person)

# pickle -> сохраняет сложные объекты и преобразует их в байт

# dump - сохранение объекта в файл
# dumps - преобразование объекта в байты
# load - загрузка объекта из файла
# loads - загрузка объекта из набора байт

import pickle

person = {'name': 'Max', 'phones': [123, 234]}
person2 = {'name': 'Max', 'phones': [123, 234], 'age': 20}
with open('person2.dat', 'wb') as f:
    pickle.dump(person2, f)

print('объект записан')

with open('person2.dat', 'rb') as f:
    person = pickle.load(f)

print(person)