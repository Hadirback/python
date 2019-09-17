import folderb.modb as modb
import moba
# Если использовать обычный импорт модуля с то получится что выполниться скрипт
# import folderb.modc as ccc
from folderb.modc import foo


print(modb.foo)
modb.bar()

print(moba.foo)
moba.bar()

# Можно ограничить выполнение скипторв конструкцией
# if __name__ = '__main__'
# но скрипт будет выполняться при запуске модуля
