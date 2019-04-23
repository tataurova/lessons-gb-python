# Создайте функцию, принимающую на вход 3 числа и возвращающую наибольшее из них.


def my_func():
    numbers = []
    for i in range(3):
        number = int(input('Введите число '))
        numbers.append(number)
    print(max(numbers))


my_func()
