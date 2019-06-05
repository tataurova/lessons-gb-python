import time


class Sleep:

    def __init__(self, timeout):
        self.timeout = timeout

    def __call__(self, func):

        def decorated(*args, **kwargs):

            time.sleep(self.timeout)
            res = func(*args, **kwargs)
            print('Function {} was sleeping in class'.format(func.__name__))
            return res
        return decorated


@Sleep(3)
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)


print(' -- Использован декоратор, реализованный через класс --')
print('!!! Обратите внимание на то, сколько раз будет вызван декоратор (рекурсия) !!!')
print(factorial(5))


