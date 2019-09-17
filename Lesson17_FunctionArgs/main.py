def hello_max():
    print('Hello Max')


def hello(who):
    print('Hello', who)


def greetiong(who, say):
    print(say, who)


def greetiong_default(who, say='Hello'):
    print(say, who)


hello_max()

hello('Leo')
hello('Max')

greetiong('Привет епта', 'Максон')

greetiong(say='Hi', who='Lol')

greetiong_default('Beel')


# Иногда нужно реализовать передачу любого количества параметров
# args - передача любого кол-ва параметров по порядку
# kwargs - передача любого кол-ва по имени
# agrs - Кортеж
def greeting_args(say, *args):
    print(type(args))
    print(say, args)


greeting_args('Hello', 'Kate')
greeting_args('Hello', 'Kate', 'Leo')
greeting_args('Hello', 'Kate', 'Leo', 'Lol')

#kwargs - словарь
def get_person(**kwargs):
    for k, v in kwargs.items():
        print(k, v)


get_person(name='Leo', age=20)
get_person(name='Leo', age=20, has_car=True)