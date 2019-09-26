import math
numbers = [1, -4, 0, 12, -9, 16]


def change_number_list(input_list):
    return [math.sqrt(number) if number > 0 else number for number in input_list]


print(change_number_list(numbers))
print(numbers)
