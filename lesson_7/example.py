# создать список из случайных чисел от 1 до 100

import random

numbers = [random.randint(1, 100) for i in range(10)]
print(numbers)


# создать список квадратов чисел

numbers = [1, 2, 3, -4]
numbers = [number**2 for number in numbers]
print(numbers)

# создать список имен на букву А

names = ['Руслан', 'Дмитрий', 'Алексей', 'Аркадий']
names = [name for name in names if name.startswith('А')]
print(names)
