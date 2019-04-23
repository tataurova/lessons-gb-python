# Шаг 1 Загадать случайное число

import random

number = random.randint(1,100)

print(number)

# Шаг 2. Пользователь должен угадать число

user_number = int(input('Введите число: '))

print(user_number)

# Шаг 3. Сравнить число с загаданным

'''
if number == user_number:
    print('Победа!')
elif number < user_number:
    print('Ваше число больше загаанного')
elif number > user_number:
    print('Ваше число меньше загаданного')
'''
while True:
    user_number = int(input('Введите число: '))
    if number == user_number:
        print('Победа!')
        break
    elif number < user_number:
        print('Ваше число больше загаанного')
    elif number > user_number:
        print('Ваше число меньше загаданного')