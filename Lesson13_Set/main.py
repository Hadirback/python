# set - cities = {'Las vegas', 'Moscow', 'Paris'}

cities = ['Las vegas', 'Paris', 'Moscow', 'Moscow', 'Paris']
print(type(cities))
print(cities)

cities = set(cities)
print(type(cities))
print(cities)
cities.add('Burma')
print(cities)
cities.remove('Moscow')
print(cities)

print(len(cities))

print('Paris' in cities)

for city in cities:
    print(city)

max_things = {'Телефон', 'Бритва', 'Рубашка', 'Шорты'}
kate_things = {'Телефон', 'Шорты', 'Зонтик', 'Помада'}


# какие вещи взяли супруги вместе
print(max_things | kate_things)
# какие вещи повторяются
print(max_things & kate_things)
# какие вещи взял макс но не взяла кейт и наоборот
print(max_things - kate_things)
print(kate_things - max_things)
