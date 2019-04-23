'''
global_var = 555
a = 1


def my_f():
    my_var = 999
    print('Внутри функции:', my_var)  # вывод локальной переменной
    print(a)  # вывод глобальной переменной, не изменить
    global global_var
    global_var = 4444
    print(global_var)


my_f()
print('Глобальная переменная после изменения в функции:', global_var)


my_f()
print('После выполнения функции', a)


def some_f():
    a = 999
    print('переменная внутри функции:', a)

a = 1
some_f()
print('Переменная после выполнения функции:', a)

'''

# Почему не надо менять глобальную переменную

global_var = 2


def my_f():
    result = global_var * 5
    print(result)


def my_change_f():
    global global_var
    global_var = 'Строка'


my_change_f()
my_f()  # после выполнени предыдущей функции глобальная переменная изменилась
