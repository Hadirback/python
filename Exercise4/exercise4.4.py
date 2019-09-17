player_name = input('Введите имя игрока: ')
count = 0
player_info = {
    'name': player_name,
    'health': 100,
    'damage': 50,
    'armor': 6
}

enemy_info = {
    'name': 'Демон',
    'health': 200,
    'damage': 500,
    'armor': 2
}


# Атака по персонажу, рассчет оставшегося HP
def attack(attacking, defending):
    health_defending = defending['health'] - get_total_damage(defending['armor'], attacking['damage'])

    if attacking['name'] == player_name:
        enemy_info['health'] = health_defending
    else:
        player_info['health'] = health_defending


# Проверка жив ли персонаж
def is_alive(person):
    return person['health'] > 0


# Показывает информацию о персонаже
def print_person_info(person):
    print(f'{person["name"]}, HP - {person["health"]}, ARM - {person["armor"]}, DMG - {person["damage"]}')


# Рассчитывает урон с учетом брони
def get_total_damage(armor, damage):
    return damage / armor


print(f'Вы сразитесь с "{enemy_info["name"]}"')

print_person_info(player_info)
print_person_info(enemy_info)

# Боевые действия
while True:
    count += 1
    print(f'Игрок {player_info["name"]} атакует "{enemy_info["name"]}"')
    attack(player_info, enemy_info)
    if not is_alive(enemy_info):
        print(f'{player_info["name"]} убивает "{enemy_info["name"]}"')
        print('Поздавляем! Противник повержен!')
        break

    if count % 4 == 0:
        print(f'"{enemy_info["name"]}" атакует игрока {player_info["name"]}')
        attack(enemy_info, player_info)

    if not is_alive(player_info):
        print(f'{player_info["name"]} умирает от руки "{enemy_info["name"]}"!')
        print('Повысь свои HP!')
        break
