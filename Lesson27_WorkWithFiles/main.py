# open function и ее параметры
# f = open('mt_txt', 'w') mode - режим encoding - кодировка
# r - чтени
# w - запись если файла нет, создается новый
# x - запись если файла нет, ошибка
# a - дозапись
# + - открытие на чтение и запись
f = open('first.txt', 'w')

# f = open('sec.txt', 'r') ошибка так как его нет
f = open('first.txt', 'r')

# Запись текста в фаил
# write - одну стоку в фаил
# writelines - запись списка строк в фаил
# \n - символ конца строки

f = open('second.txt', 'w')
f.write('Hello\n')
f.write('World\n')

f.writelines(['Hello\n', 'Python\n'])

# Чтение текста из файла
# read - прочитать фаил целиком
# for line in f - чтение построчно
# readlines - чтение файла в список строк

f = open('second.txt', 'r')
print(f.read())

f = open('second.txt', 'r')
for line in f:
    print(line.replace('\n', ''))

f = open('second.txt', 'r')
print(f.readlines())

# Закрытие файла
# f.close однако если была ошибка то он не выполнится
# удобнее исполльзовать конструкцию with
f.close()

with open('second.txt', 'r') as f:
    for line in f:
        print(line.replace('\n', ''))


# Работа через with
