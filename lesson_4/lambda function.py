def some_f():
    return 10


result = some_f()
print(result)

a = some_f
print(a)
print(type(a))
print(a())


def f():
    print('Hello from other function')


def to(f_param):
    # параметром будет функция
    # поэтому в теле функции мы ее вызовем
    f_param()


to(f)


def my_filter(numbers, function):
    result = []
    for number in numbers:
        if function(number):
            result.append(number)
    return result


numbers = [1, 2, 3, 4, 5]


def is_even(number):
    return number % 2 == 0


def is_not_even(number):
    return number % 2 != 0


print(my_filter(numbers, is_even))

print(my_filter(numbers, is_not_even))


def big_4(number):
    return number > 4


print(my_filter(numbers, big_4))
print(my_filter(numbers, lambda number: number > 4))

