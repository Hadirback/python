print('СОРЕВНОВАНИЯ ПО PYTHON!')
count = int(input('Введите количество участников: '))
i = count
members = []
while i > 0:
    name = input('Кто занял {} место? '.format(i))
    members.append(name)
    i -= 1
members = sorted(members)
print('В соревнованиях участвовали: ', members)

# мы записали людей с конца
members.reverse()

result = members[:3]
result = 'Победители: {}. Поздравляем с успехом!'.format(result)

print(result)