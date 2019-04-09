# Создайте модуль. В нем создайте функцию, которая принимает список и возвращает из него случайный элемент.
# Если список пустой, функция должна вернуть None. Проверьте работу функций в этом же модуле.
# Примечание: Список для проверки введите вручную. Или возьмите этот: [1, 2, 3, 4]


from random import choice

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
my_list2 = []


def my_func(some_list):
    if len(some_list) == 0:
        return None
    else:
        return choice(some_list)


print(my_func(my_list))
print(my_func(my_list2))



