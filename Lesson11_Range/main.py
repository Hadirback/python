numbers = range(10)
print(type(numbers))
print(list(numbers))
print(numbers)
winners = ['Max', 'Kate', 'Lol']
for i in range(len(winners)):
    print(i + 1)
    print(i + 1, ')', winners[i])

# range(start, stop, step)
print(list(range(1, 1000, 2)))

for i in range(1, 1000, 2):
    print(i)