import time


def decorator(func):

    def wrapper():
        print('Сейчас выполняется функция-обёртка')
        time.sleep(4)
        print('Это просто ссылка на экземпляр оборачиваемой функции: {}'.format(func))
        time.sleep(4)
        print('Выполняем оборачиваемую (исходную) функцию...')
        time.sleep(4)
        func()
        time.sleep(4)
        print('Выходим из обёртки')

    return wrapper


@decorator
def some_text():
    print('Это просто текст')


some_text()

# some_text = decorator(some_text)
# some_text()

