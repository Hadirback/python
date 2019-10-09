import os
import shutil
import datetime


# метод для получения рабочей директории
def get_work_directory():
    print(os.getcwd())


# метод для изменения рабочей директории
def change_work_directory(path):
    if os.path.exists(path):
        os.chdir(path)


# метод выдает итоговый путь до папки или файла
def get_path(path, name):
    if os.path.isabs(path):
        return os.path.join(os.path.abspath(path), name)
    else:
        return os.path.join(os.getcwd(), path, name)


# метод для получения информации о файлах и папках в указанной директории
def get_list(path=None, folders_only=False):
    try:
        result = None
        if not path:
            result = os.listdir()
        else:
            if os.path.exists(path):
                result = os.listdir(path)
            else:
                print('Такого пути не существует!')
        if result:
            if folders_only:
                result = [f for f in result if os.path.isdir(f)]
            print(result)
        else:
            raise Exception('Что то не так! result == None. Метод get_list')
    except Exception as ex:
        print(f'Ошибка в методе get_list. Message: {ex}')


# метод для создания файла
def create_file(name, path=None, text=None):
    try:
        result = None
        if not path:
            result = name
        else:
            if os.path.exists(path):
                result = get_path(path, name)
            else:
                print('Не удалось создать фаил! Такого пути не существует!')
                return

        if result:
            # создание и запись в фаил
            with open(result, 'w', encoding='utf-8') as f:
                if text:
                    f.write(text)
        else:
            raise Exception('Что то не так! result == None. Метод create_file')
    except Exception as ex:
        print(f'Неизвестная ошибка в методе create_file. Message: {ex}')


# метод для создания папки
def create_folder(name, path=None):
    try:
        result = None
        # Если нет пути, создаем папку в рабочей директории.
        if not path:
            result = name
        # Если путь не пустой - проверяем существует ли такая директория, если нет выдаем ошибку
        elif os.path.exists(path):
            # Является ли путь абсолютным, если нет то использоуем относительный путь
            result = get_path(path, name)
        else:
            print('Не удалось создать папку! Такого пути не существует!')
            return

        if result:
            os.mkdir(name)
            print('Папка успешно создана!')
        else:
            raise Exception('Что то не так! result == None. Метод create_file')
    except FileExistsError:
        print('Такая папка уже есть')
    except Exception as ex:
        print(f'Неизвестная ошибка в методе create_folder. Message: {ex}')


# метод для удаления файла
def delete_file(name):
    if os.path.isdir(name):
        os.rmdir(name)
    else:
        os.remove(name)


def copy_file(name, new_name):
    if os.path.isdir(name):
        try:
            shutil.copytree(name, new_name)
        except FileExistsError:
            print('ТАкая папка уже есть')
    else:
        shutil.copy(name, new_name)


def save_info(message):
    current_time = datetime.datetime.now()
    result = f'{current_time} - {message}'
    print(result)
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.write(result + '\n')


print(os.path.isabs(u'/dfdfs'))
print()
print(os.getcwd())
