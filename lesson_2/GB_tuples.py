print('СОРЕВНОВАНИЯ ПО ПИТОН')

count = int(input('Ввдедите количетсво участников '))

print('В соревнованиях участвовали: ')

i = count
members = []
while i > 0:
    name = input('Кто занял {} место'.format(i))
    members.append(name)
    i -= 1

print('В соревнованиях участвовали', members)

members.reverse()
result = members[:3]

result = 'Победители: {}. Подравляем!'.format(result)

print(result)
