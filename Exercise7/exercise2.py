numbers = [1, -3, -8, 23, 3, 8, -4, 6, 5, 9, 0, -10, 12, -2]

new_list = [number for number in numbers if number > 0 and number % 3 == 0 and number % 4 != 0]
print(new_list)