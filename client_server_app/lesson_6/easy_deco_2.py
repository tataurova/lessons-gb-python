import requests
import time


def decorator(func):

    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print('Время выполнения оборачиваемой ф-ции: {} секунд.'.format(round(end-start, 2)))
    return wrapper


@decorator
def get_wp():
    # получаем ответ сервера
    # 200 - запрос успешно обработан
    wp = requests.get('https://google.com')


get_wp()
