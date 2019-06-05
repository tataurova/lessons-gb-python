
class Log:

    def __call__(self, func):
        def decorated(*args, **kwargs):
            res = func(*args, **kwargs)
            print('log2: {}({}, {}) = {}'.format(func.__name__, args, kwargs, res))
            return res

        return decorated


@Log()
def func2(a, b):
    return a ** b


print('-- Функции с декораторами --')
func2(4, 5)

# другой подход применения декоратора к функции func2 = Log()(func2)
# func2 = Log()(func2)
# func2(4, 5)

