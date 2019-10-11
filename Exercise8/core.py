import os
import shutil
import datetime


# метод для получения рабочей директории
def get_work_directory():
    print(os.getcwd())


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
            path = ''
        elif os.path.exists(path):
            result = os.listdir(path)
        else:
            save_info('Такого пути не существует!')
            return

        if result:
            if folders_only:
                result = [f for f in result if os.path.isdir(os.path.join(path, f))]

            print(result)
        else:
            raise Exception('Что то не так! result == None. Метод get_list')

    except Exception as ex:
        save_info(f'Ошибка в методе get_list. Message: {ex}')


# метод для создания файла
def create_file(name, path=None, text=None):
    try:
        result = None
        if not path:
            result = name
        elif os.path.exists(path):
            result = get_path(path, name)
            if os.path.exists(result):
                save_info('Фаил будет переписан!')
        else:
            save_info('Не удалось создать фаил! Такого пути не существует!')
            return

        if result:
            # создание и запись в фаил
            with open(result, 'w', encoding='utf-8') as f:
                if text:
                    f.write(text)
                    save_info('Фаил успешно создан')
        else:
            raise Exception('Что то не так! result == None. Метод create_file')

    except Exception as ex:
        save_info(f'Ошибка в методе create_file. Message: {ex}')


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
            save_info('Не удалось создать папку! Такого пути не существует!')
            return

        if result:
            os.mkdir(result)
            save_info('Папка успешно создана!')
        else:
            raise Exception('Что то не так! result == None. Метод create_file')

    except FileExistsError:
        save_info('Такая папка уже есть')
    except Exception as ex:
        save_info(f'Ошибка в методе create_folder. Message: {ex}')


# метод для удаления файла
def delete_file_or_folder(name, path=None):
    try:
        result = None
        if not path:
            result = name
        elif os.path.exists(path):
            result = get_path(path, name)
        else:
            save_info('Не удалось удалить фаил/папку! Такого пути не существует!')
            return

        if result:
            if os.path.isdir(result):
                if not os.listdir(result):
                    shutil.rmtree(result)
                    save_info('Папка успешно удалена')
                else:
                    raise Exception('Папка не пуста!')
            else:
                os.remove(result)
                save_info('Фаил успешно удален')
        else:
            raise Exception('Что то не так! result == None. Метод create_file')

    except IOError as ex:
        save_info('Такого файла/папки нет!')
    except Exception as ex:
        save_info(f'Ошибка в методе delete_file_or_folder. Message: {ex}')


# Метод для копирования файла
def copy_file_or_folder(name, new_name, path=None):
    try:
        if not os.path.exists(name):
            save_info('Неверный путь оригинального файла!')
            return

        if name == new_name and path:
            save_info('Одинаковые названия в одной папке!')
            return

        result = None
        if not path:
            result = new_name
        elif os.path.exists(path):
            result = get_path(path, new_name)
        else:
            save_info('Не удалось скопировать фаил/папку! Такого пути не существует!')
            return

        if result:
            if os.path.isdir(name):
                shutil.copytree(name, result)
                save_info('Папка успешно скопирована')
            else:
                shutil.copy(name, result)
                save_info('Фаил успешно скопирован')
        else:
            raise Exception('Что то не так! result == None. Метод copy_file_or_folder')
    except FileExistsError:
        save_info('Такая папка уже есть')
    except Exception as ex:
        save_info(f'Ошибка в методе copy_file_or_folder. Message: {ex}')


# Метод для введения лога
def save_info(message):
    current_time = datetime.datetime.now()
    result = f'{current_time} - {message}'
    print(result)
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.write(result + '\n')


if __name__ == '__main__':
    get_work_directory()