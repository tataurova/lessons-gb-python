# Давайте усложним предыдущее задание. Измените сущности, добавив новый параметр — armor = 1.2
# (величина брони персонажа)
# Теперь надо добавить новую функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
# Следовательно, у вас должно быть 2 функции:
# 1. Наносит урон. Это улучшенная версия функции из задачи 3.
# 2. Вычисляет урон по отношению к броне.
# Примечание. Функция номер 2 используется внутри функции номер 1 для вычисления урона и вычитания его из здоровья
# персонажа.


player = {'name': 'None', 'health': 100, 'damage': 50, 'armor': 1.2}

enemy = {'name': 'None', 'health': 100, 'damage': 50, 'armor': 1.2}

player['name'] = str(input('Введите имя игрока '))
enemy['name'] = str(input('Введите имя врага '))

print(f"Здоровье игрока {player['name']} до атаки: {player['health']}")
print(f"Здоровье врага {enemy['name']} до атаки: {enemy['health']}")


def attack(person1, person2):
    protection = protection_func(person1['damage'], person1['armor'])
    person2['health'] = person2['health'] - protection
    print(f"******* АТАКА на {person2['name']}! *******")


def protection_func(damage, armor):
    protection = round(damage / armor, 2)
    return protection


attack(player, enemy)

print(f"После атаки игрока здоровье игрока: {player['health']}, здоровье врага: {enemy['health']}")

attack(enemy, player)

print(f"После атаки врага здоровье игрока: {player['health']}, здоровье врага: {enemy['health']}")
