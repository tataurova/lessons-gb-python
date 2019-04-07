# Шаг 1 Загадать случайное число

import random

number = random.randint(1, 100)
print(number)


user_number = None

count = 0

# max_count = 3

levels = {1: 10, 2: 5, 3: 3}

level = int(input('Выберите уровень сложности '))

max_count = levels[level]


while number != user_number:
    count += 1

    if count > max_count:
        print('Вы проиграли')
        break
    print(f'попытка № {count}')
    user_number = int(input('Введите число '))

    if number < user_number:
        print('Ваше число больше загаданного')
    elif number > user_number:
        print('Ваше число меньше загаданного')
else:
    print('Победа!')
