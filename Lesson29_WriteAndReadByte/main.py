# Работа с файлом в режиме байтов
# open('filename', 'wb') - режим записи байтов
# open('filename', 'rb') - режим чтения байтов
# Параметр encoding определяет кодировку

# open('filename', 'w', encoding)
with open('bytes.txt', 'wb') as f:
    pass

with open('bytes.txt', 'rb') as f:
    pass



with open('bytes.txt', 'r', encoding='utf-8') as f:
    pass

# запись набора байт в фаил

# f.write(b'some bytes') - фаил открыт в режиме wb
# f.write('some str') - фаил открыт в режиме w
# в любом случае информация хранится как 0 и 1
with open('bytes.txt', 'wb') as f:
    f.write(b'Hello bytes')

# читаем как текст
with open('bytes.txt', 'r', encoding='ascii') as f:
    # пишем строку байт
    print(f.read())

# открываем файл для записи байтов
with open('bytes.txt', 'wb') as f:
    str = 'Привет мир'
    f.write(str.encode('utf-8'))

with open('bytes.txt', 'r', encoding='utf-8') as f:
    print(f.read())

# чтение байтов из файла
# когда фаил открыт в режиме rb то мы будем читать как байты
# r - как строки

with open('bytes.txt', 'wb') as f:
    str = 'Привет мир'
    f.write(str.encode('utf-8'))

with open('bytes.txt', 'w', encoding='utf-8') as f:
    f.write('Привет мир')

with open('bytes.txt', 'rb') as f:
    result = f.read()
    print(result)
    print(type(result))

    s = result.decode('utf-8')
    print(s)

