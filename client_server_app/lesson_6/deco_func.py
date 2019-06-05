
def log(func):

    def decorated(*args, **kwargs):
        res = func(*args, **kwargs)
        print('log: {}({}, {}) = {}'.format(func.__name__, args, kwargs, res))
        return res

    return decorated


@log
def func(a, b):
    return a * b


print('-- Функции с декораторами --')
func(14, 15)

# другой подход применения декоратора к функции func = log(func)
# func = log(func)
# func(14, 15)
