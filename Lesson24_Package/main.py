from hopital.h import get_main
from hopital.patients.index import get_index
# Пакет может содержать другие пакеты или модули
# Пакет содержит внутри себя __init__py

# Можно создать обычную папку и такой фаил чтобы он идентифицировался
# Пакеты позволяют создавать простанства имен
# Работа с модулями с указанием уровня вложенности
# пакет1.пакет2.модуль

# Внутри пакета из одного модуля в другой мы можем воспользоваться
# конструкцией import .модуль
# Если в другом пакете пакет.модуль
# Так же работают import from as
# Вложенность может быть любой

# Основной фаил


get_main()
get_index()