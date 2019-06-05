
# -------------- Декораторы и атрибуты функций ------------------------------

# При использовании декораторов теряются оригинальные атрибуты декорируемой функции.

from functools import wraps


def factorial(n):
    """ Вычисляет факториал числа n. Например:
        >>> factorial(6)
        120
        >>>
    """
    if n <= 1: 
        return 1
    else: 
        return n * factorial(n-1)


print(" -- Оригинальные строки документации --")
help(factorial)


# ----------- Теперь применим декоратор -------------------
def wrap(func):
    def call(*args, **kwargs):
        return func(*args, **kwargs)
    return call


@wrap
def factorial(n):
    """ Вычисляет факториал числа n. Например:
        >>> factorial(6)
        120
        >>>
    """
    if n <= 1: 
        return 1
    else: 
        return n * factorial(n-1)


print()
print(" -- Теперь к функции применили декоратор --")
# Что будет выведено в консоль?
help(factorial)

# --- Декоратор заменил оригинальное имя функции и строки документации ---

# Для того, чтобы решить эту проблему, можно использовать несколько подходов.

# 1. Явно прописать в коде декоратора те атрибуты, которые должны быть сохранены


def wrap(func):
    def call(*args, **kwargs):
        return func(*args, **kwargs)

    # Обязательный минимум - скопировать имя функции и строки документации:
    call.__doc__ = func.__doc__
    call.__name__ = func.__name__

    # Для случая, если у исходной функции есть дополнительные атрибуты:
    call.__dict__.update(func.__dict__)

    return call


# 2. Воспользоваться декоратором functools.wraps, который сделает то же самое


def wrap(func):

    @wraps(func)
    def call(*args, **kwargs):
        return func(*args, **kwargs)

    return call 


# Проверка возможностей декоратора сохранять атрибуты функции
@wrap
def factorial(n):
    """ Вычисляет факториал числа n. Например:
        >>> factorial(6)
        120
        >>>
    """
    if n <= 1: 
        return 1
    else: 
        return n * factorial(n-1)


print()
print(" -- Теперь декоратор 'умеет' сохранять атрибуты функции -- ")
# Что будет выведено в консоль?
help(factorial)