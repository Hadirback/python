import sys
import os
from core import create_file, create_folder, get_list, get_work_directory, \
    delete_file_or_folder, copy_file_or_folder, save_info
from game1 import guess_number_of_computer
from game2 import computer_guesses_number


save_info('Start')
try:
    command = sys.argv[1]
except Exception:
    print('Нет команды')
else:
    if command == 'list':
        save_info('command list')
        try:
            path = sys.argv[2] if len(sys.argv) >= 3 else None
            foldes_only = sys.argv[3] if len(sys.argv) >= 4 else False
        except Exception as ex:
            print(f'Ошибка - {ex}')
        else:
            get_list(path, foldes_only)

    elif command == 'work_dir':
        save_info('command work_dir')
        get_work_directory()

    elif command == 'create_file':
        save_info('command create_file')
        try:
            name = sys.argv[2] if len(sys.argv) >= 3 else 'temp.txt'
            path = sys.argv[3] if len(sys.argv) >= 4 else None
            text = sys.argv[4] if len(sys.argv) >= 5 else None
        except Exception as ex:
            print(f'Ошибка - {ex}')
        else:
            create_file(name, path, text)

    elif command == 'create_folder':
        save_info('command create_folder')
        try:
            name = sys.argv[2] if len(sys.argv) >= 3 else 'Temp'
            path = sys.argv[3] if len(sys.argv) >= 4 else None
        except Exception as ex:
            print(f'Ошибка - {ex}')
        else:
            create_folder(name, path)

    elif command == 'delete':
        save_info('command delete')
        try:
            name = sys.argv[2]
            path = sys.argv[3] if len(sys.argv) >= 4 else None
        except IndexError:
            print('Отсутствует название файла')
        except Exception as ex:
            print(f'Ошибка - {ex}')
        else:
            delete_file_or_folder(name, path)

    elif command == 'copy':
        save_info('command copy')
        try:
            name = sys.argv[2]

            obj_name = None
            if os.path.isdir(name):
                obj_name = 'Temp'
            else:
                obj_name = 'temp.txt'

            new_name = sys.argv[3] if len(sys.argv) >= 4 else obj_name
            path = sys.argv[4] if len(sys.argv) >= 5 else None
        except IndexError:
            print('Отсутствует названия оригинально файла')
        except Exception as ex:
            print(f'Ошибка - {ex}')
        else:
            copy_file_or_folder(name, new_name, path)

    elif command == 'guess_number_of_computer':
        save_info('command guess_number_of_computer')
        guess_number_of_computer()

    elif command == 'computer_guesses_number':
        save_info('command computer_guesses_number')
        computer_guesses_number()
    elif command == 'help':
        save_info('help')
        print('list - список файлов и папок')
        print('work_dir - рабочая директория')
        print('create_file - создание файла')
        print('create_folder - создание папки')
        print('delete - удаление файла или папки')
        print('copy - копирование файла или папки')
        print('guess_number_of_computer - игра "угадай число компьютера"')
        print('computer_guesses_number - игра "компьютер угадывает твое число"')
save_info('End')
