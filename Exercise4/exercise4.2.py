# Можно было бы использовать numbers[] в аргументе функции, но сказано на вход именно 3 числа
def get_max_number(num1, num2, num3):
    return max(num1, num2, num3)


print(get_max_number(3, 6, 4))
