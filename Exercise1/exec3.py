while True:
    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    age = input('Введите возрас: ')
    weight = input('Введите вес: ')

    if not age.isdigit():
        print('Неверно введен возраст')
        continue
    else:
        age = int(age)

    if not weight.isdigit():
        print('Неверно введен вес')
        continue
    else:
        weight = int(weight)

    if not name or not surname:
        print('Введены пустые данные')
        continue

    message = None

    if age == 30:
        message = 'В этом году вы записаны на полное обследование!'
    elif 50 < weight < 120:
        message = 'Пациент в хорошем состоянии.'
    elif age < 30:
        if weight < 50:
            message = 'Нужно больше есть и качаться!'
        else:
            message = 'Нужно следить за диетой и бегать!'
    else:
        if age > 40 and (weight < 50 or weight > 120):
            message = 'Пациенту требуется врачебный осмотр!'
        elif weight < 50:
            message = 'Нужно есть больше вареной, белкой пищи и заниматься спортом'
        else:
            message = 'Нужно следить за диетой и ходить в бассеин!'

    print(name, surname + ',', age, 'год,', 'вес', weight, '-', message)
    break
