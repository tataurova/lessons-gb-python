# Давайте опишем пару сущностей player и enemy через словарь, который будет иметь ключи и значения:
# name — строка, полученная от пользователя,
# health = 100,
# damage = 50.
#
# Поэкспериментируйте с значениями урона и жизней по желанию.
# Теперь надо создать функцию attack(person1, person2).
# Примечание: имена аргументов можете указать свои.
# Функция в качестве аргумента будет принимать атакующего и атакуемого.
# В теле функция должна получить параметр damage атакующего и отнять это количество от health атакуемого.
# Функция должна сама работать со словарями и изменять их значения.

player = {'name': 'None', 'health': 100, 'damage': 50}

enemy = {'name': 'None', 'health': 100, 'damage': 50}

player['name'] = str(input('Введите имя игрока '))
enemy['name'] = str(input('Введите имя врага '))

print(f"Здоровье игрока {player['name']} до атаки: {player['health']}")
print(f"Здоровье врага {enemy['name']} до атаки: {enemy['health']}")


def attack(person1, person2):
        person2['health'] = person2['health'] - person1['damage']
        print(f"******* АТАКА на {person2['name']}! *******")


attack(player, enemy)

print(f"После атаки игрока здоровье игрока: {player['health']}, здоровье врага: {enemy['health']}")

attack(enemy, player)

print(f"После атаки врага здоровье игрока: {player['health']}, здоровье врага: {enemy['health']}")
