cities = ['Moskva', 'SPb', 'SPb']

print(type(cities))
print(cities)

cities = set(cities)
print(cities)
print(type(cities))

cities = {'Moskva', 'SPb'}
print(cities)
print(type(cities))

cities.add('Vologda')
print(cities)

cities.remove('SPb')
print(cities)

print(len(cities))

print('Moskva' in cities)

for city in cities:
    print(city)

max_things = {'телефон', 'Бритва'}
kate_things = {'телефон', 'шорты'}

# какие вещи они взяли
print(max_things | kate_things)

# какие вещи повторяются
print(max_things & kate_things)

# какие вещи взял Макс, но не взяла Кейт
print(max_things - kate_things)

# какие вещи взяла Кейт, но не взял Макс
print(kate_things - max_things)