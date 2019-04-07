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

user_count = int(input('Введите количество пользователей '))

users = []

for i in range(user_count):
    user_name = input(f'Введите имя пользователя {i + 1} ')
    users.append(user_name)

print(users)

is_winner = False

winner_name: None

while not is_winner:
    count += 1

    if count > max_count:
        print('Все пользователи проиграли')
        break
    print(f'Попытка № {count}')

    for user in users:
        print(f'Ход пользователя {user}')

        user_number = int(input(f'Введите число, {user} '))

        if user_number == number:
            is_winner = True
            winner_name = user
            break

        elif number < user_number:
            print('Ваше число больше загаданного')
        elif number > user_number:
            print('Ваше число меньше загаданного')
else:
    print(f'Победитель: {winner_name}')






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
