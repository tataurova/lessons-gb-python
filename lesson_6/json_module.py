import json

friends = [{'name ': 'Max', 'age': 23, 'phones': [123, 234]}, {'name': 'Leo', 'age': 34}]

# посмотрим тип объекта

print(type(friends))

# открываем файл
with open('friends.jon', 'w') as f:
        # преобразуем список друзей в json
        json_friends = json.dump(friends, f)


print(json_friends)
print(type(json_friends))

# обратно из json в объект

with open('friends.jon', 'r') as f:
    friends = json.load(f)


print(friends)
print(type(friends))

