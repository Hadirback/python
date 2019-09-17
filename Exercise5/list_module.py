import random


def get_random_elem(list):
    if not list:
        return None

    return random.choice(list)


def fill_list():
    my_list = []
    while True:
        elem = input('Введите элемент списка или Enter чтобы закончить ввод: ')
        if not elem:
            return my_list
        else:
            my_list.append(elem)


main_list = fill_list()
print(f'Мой список элементов: {main_list}')
print(f'Мой рандомный элемент из списка - {get_random_elem(main_list)}')