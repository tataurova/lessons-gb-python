# набор чисел

numbers = [1, 5, 3, 5, 9, 7, 11]

# Сортировка по возрастанию
print(sorted(numbers))

# Сортировка по убыванию
print(sorted(numbers, reverse=True))

# набор строк
names = ['Max', 'Ola', 'Masha']
# сортировка по алфавиту
print(sorted(names))

cities = [('Москва', 1000), ('СПб', 40), ('Псков', 400)]  # кортеж
# сортировка по алфавиту
print(sorted(cities))

# сортировка по численности


def by_count(city):
    return city[1]


print(sorted(cities, key=by_count))
print(sorted(cities, key=lambda city: city[1]))

