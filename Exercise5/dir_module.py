import os


def create_dir():
    for i in range(1, 10):
        path = os.path.join(os.getcwd(), f'dir_{i}')
        if not os.path.exists(path):
            os.mkdir(path)
        else:
            print(f'Директория {path} уже существует')


def remove_dir():
    for i in range(1, 10):
        path = os.path.join(os.getcwd(), f'dir_{i}')
        if os.path.exists(path):
            os.rmdir(path)
        else:
            print(f'Директория {path} уже удалена')


create_dir()
input('Enter для удаления директорий')
remove_dir()