'''

def log(func, logger):

    def decorated(*args, **kwargs):
        res = func(*args, **kwargs)
        logger.debug('function {} completed with result {}, with arguments: {}'.format(func.__name__, res, args, kwargs))
        return res

    return decorated

'''


class Log:

    def __init__(self, logger):
        # запоминаем логгер, чтобы можно было использовать разные
        self.logger = logger

    def __call__(self, func):

        def decorated(*args, **kwargs):
            res = func(*args, **kwargs)
            self.logger.debug(
                'function {} completed with result {}, with arguments: {}'.format(func.__name__, res, args, kwargs))
            return res

        return decorated