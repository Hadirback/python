# Lesson 5 Exercise 3
import dir_module
from list_module import get_random_elem, fill_list


dir_module.create_dir()
input('Enter для удаления директорий')
dir_module.remove_dir()

main_list = fill_list()
print(f'Мой список элементов: {main_list}')
print(f'Мой рандомный элемент из списка - {get_random_elem(main_list)}')
