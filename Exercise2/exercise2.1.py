first_list = [2, 3, 5, 2, 8, 10, 15, 17, 4]
second_list = [2, 4, 3, 6, 15, 20]

for elem_first_list in first_list:
    if elem_first_list in second_list:
        first_list.remove(elem_first_list)

print(first_list)