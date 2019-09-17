def print_sep():
    print('-' * 100)


def print_sep_params(sep):
    print(sep * 100)


def print_sep_param_len(sep, sep_len):
    print(sep * sep_len)


def get_sep_result(sep, len):
    return sep * len


print('Моя первая функция')
print_sep()
print('Красивый разделитель')
print_sep()
print('Что если их будет много?')
print_sep()
print_sep()
print_sep()
# меняем знак разделитея
print_sep_params('*')
# меняем знак и длину
print_sep_param_len('-', 2)
# используем разделитель в тексте
result = print_sep_params('d')
print(result)

sep = get_sep_result('-', 20)
text = 'Hello {} Func {}'.format(sep, sep)
print(text)

# 3 части функции - параметры, имя, возвращаемое значение
