import sys
from core import create_file, create_folder, get_list, delete_file, copy_file, save_info


save_info('Start')
try:
    command = sys.argv[1]
except Exception:
    print('Нет команды')
else:
    if command == 'list':
        get_list()
    elif command == 'create_file':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутствует называние файла')
        else:
            create_file(name)
    elif command == 'create_folder':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутствует называние файла')
        else:
            create_folder(name)
    elif command == 'delete':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутствует называние файла')
        else:
            delete_file(name)
    elif command == 'copy':
        try:
            name = sys.argv[2]
            new_file = sys.argv[3]
        except IndexError:
            print('Отсутствуют называния файлов')
        else:
            copy_file(name, new_file)
    elif command == 'help':
        print('list - список файлов и папок')
        print('create_file - создание файла')
        print('create_folder - создание папки')
        print('delete - удаление файла или папки')
        print('copy - копирование файла или папки')

save_info('End')