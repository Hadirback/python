friend_name = 'Max'
friends = ['Max', 'Lol', 'Kate']
roles = ('admin', 'guest', 'user')

print(type(roles))
print(type(friends))

if 'Max' in friends:
    print('Yeees~')

i = 0
while i < len(friends):
    friend = friends[i]
    print(friend)
    i += 1

for friend in friends:
    print(friend)

print('end')

for role in roles:
    print(role)