# Пользователь вводит 3 числа. Найти мин, макс, сумму

numbers = []

for i in range(3):
    number = int(input('Введите число '))
    numbers.append(number)


print(max(numbers))
print(min(numbers))
print(sum(numbers))
