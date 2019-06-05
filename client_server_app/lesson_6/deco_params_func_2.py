import requests
import time


def decorator(iters):
    def real_decorator(func):

        def wrapper(*args, **kwargs):
            total = 0
            for i in range(iters):
                start = time.time()
                return_value = func(*args, **kwargs)
                end = time.time()
                total = total + (end-start)
            print('Среднее время выполнения: {} секунд.'.format(round(total/iters, 2)))
            return return_value

        return wrapper
    return real_decorator


@decorator(iters=10)
def get_wp(url):
    wp = requests.get(url)
    return wp


get_wp('https://google.com')
