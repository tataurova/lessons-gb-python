import time
import requests


def decorator(func):

    def wrapper(*args, **kwargs):
        start = time.time()
        return_value = func(*args, **kwargs)
        end = time.time()
        print('Отправлен запрос на адрес {}. Время выполнения: {} секунд.'.format(*args, round(end-start, 2)))
        return return_value
    return wrapper


@decorator
def get_wp(url):
    wp = requests.get(url)
    return wp


get_wp('https://google.com')

