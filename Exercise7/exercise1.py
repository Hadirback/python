first_list = ['Апельсин', 'Яблоко', 'Груша', 'Ананас', 'Банан']
second_list = ['Манго', 'Груша', 'Киви', 'Банан', 'Мандарин', 'Апельсин']

fruits = [fruit for fruit in first_list if fruit in second_list]
print(fruits)
