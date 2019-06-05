
import time


def sleep(timeout):

    def decorator(func):

        def decorated(*args, **kwargs):

            t1 = time.sleep(timeout)
            res = func(*args, **kwargs)

            print('Function {} was sleeping'.format(func.__name__))

            return res

        return decorated

    return decorator


@sleep(1)
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)


print(' -- Использован декоратор, реализованный через функцию --')
print('!!! Обратите внимание на то, сколько раз будет вызван декоратор (рекурсия) !!!')
print(factorial(5))
print()

