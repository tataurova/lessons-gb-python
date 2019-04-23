# Напишите функцию, которая принимает на вход список.
# Функция создает из этого списка новый список из квадратных корней чисел (если число положительное)
# и самих чисел (если число отрицательное) и возвращает результат (желательно применить генератор и
# тернарный оператор при необходимости). В результате работы функции исходный список не должен измениться.
# Например:
# old_list = [1, -3, 4]
# result = [1, -3, 2]
# Примечание: Список с целыми числами создайте вручную в начале файла. Не забудьте включить туда отрицательные числа.
# 10-20 чисел в списке вполне достаточно.

import math

my_list = [1, 4, 9, 16, 4, -7, -12, 144, 25, -1, 0]
result = []
print(my_list)

# через цикл


def my_func(list):
    for number in list:
        if number > 0:
            result.append(int(math.sqrt(number)))
        else:
            result.append(number)
    return result


print(my_func(my_list))


# через генератор


def my_func_gen(list):
    result = [number if number < 0 else int(math.sqrt(number)) for number in list]
    return result


print(my_func_gen(my_list))
