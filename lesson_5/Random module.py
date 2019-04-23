from random import randint, choice, sample, shuffle


# загадать случ число от 0 до 100

print(randint(0, 100))

# выбрать победителя лотереии из списка

players = ['max', 'igor', 'kola', 'kate']
print(choice(players))

# выбрать 3 победителей
print(sample(players, 3))

# перемешать карты в стопке карт
cards = ['6', '7', '8', '10', 'V', 'D']
print(cards)
shuffle(cards)
print(cards)
