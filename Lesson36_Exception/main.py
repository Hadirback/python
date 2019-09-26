# деление на 0
# Ошибка чтения файла если его нет

number = int(input('Введите число: '))
try:
    result = 100 / number
except ZeroDivisionError as e:
    print('Деление на 0')
    print(f'Информация: {e}')
except Exception as e:
    print('Неизвестная ошибка')
    print(f'Информация: {e}')
else:
    print('Все хорошо ошибок не было')
finally:
    print('Делаем всегда')

print('Конец')


print('Начало')
raise Exception('Что то не так')
print('Конец')