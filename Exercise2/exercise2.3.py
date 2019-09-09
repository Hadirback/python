input_list = [1, 2, 1, 6, 8, 2, 12, 4, 3, 4, 3, 2]
work_list = list(set(input_list))

unique_list = []
for elem in work_list:
    input_list.remove(elem)
    if not (elem in input_list):
        unique_list.append(elem)

print(unique_list)
