name = 'Оля'
name2 = "Артем"
print(name)
print(type(name))
print(name2)
print(type(name2))
print(name[-1])
print(name[1:3])

friend = 'Максим Дмитрий Юлия'

print(friend.find('кс'))

print(friend.isdigit())

print(friend.upper())

print(friend.lower())

print(friend.split())

# форматирование строк

name = 'Оля'
age = 35

#1 конкатенация

print('Привет ' + name + ' тебе ' + str(age) + ' лет')

#2 %

print('Привет %s тебе %d лет'%(name, age))

#3 format

print('Привет {} тебе {} лет'.format(name,age))


# Задача

top5 = 'Первые 5 мест на соревнованиях: 1. Петров 2. Иванов 3. Сидоров 4. Сурков 5. Пупкн'

start = top5.find('1')
end = top5.find('4')

top3 = top5[start:end]

result = 'Поздравляем {} с победой!'.format(top3.upper())
print(result)