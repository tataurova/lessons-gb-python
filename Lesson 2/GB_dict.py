friends = ['max', 'leo', 'pol']
print(friends)
print(type(friends))
friend = friends[0]
print(friend)
print(type(friend))

# добавить возраст другу

friend = {
    'name': 'max',
    'age': 23
}

print(friend)
print(type(friend))

print(friend['age'])

friend['has_car'] = True

print(friend)

del friend['age']
print(friend)

if 'has_car' in friend:
    print('Есть возраст')

# перебор по ключам

for key in friend.keys():
    print(key)
    print(friend[key])

for key in friend:
    print(key)
    print(friend[key])

# по значениям

for val in friend.values():
    print(val)

# пары ключ значение

for item in friend.items():
    print(item)

for key, val in friend.items():
    print(key)
    print(val)

