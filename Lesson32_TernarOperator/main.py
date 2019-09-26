is_has_name = True
name = 'Nax' if is_has_name else 'Empty'
print(name)

IS_ONE = False

number = 1 if IS_ONE else 2
print(number)

word = 'слово'

result = []
for i in range(len(word)):
    # if i % 2 != 0:
    #     letter = word[i].lower()
    # else:
    #     letter = word[i].upper()
    #
    letter = word[i].lower() if i % 2 != 0 else word[i].upper()
    result.append(letter)

result = ''.join(result)
print(result)

password = input('Введите пароль')
print('Войти' if password == 'secret' else 'Вход запрещен!')