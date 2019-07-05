
class Log:
    """
    Класс декоратор для логирования функций
    """

    def __init__(self, logger):
        # запоминаем логгер, чтобы можно было использовать разные
        self.logger = logger

    def __call__(self, func):
        """
        Определяем __call__ для возможности вызова экземпляра как декоратора
        :param func: функция, которую будем декорировать
        :return: новая функция
        """

        def decorated(*args, **kwargs):
            # Выполняем функцию и получаем результат
            res = func(*args, **kwargs)
            # Пишем сообщение в лог
            self.logger.debug(
                'function {} completed with result {}, with arguments: {}'.format(func.__name__, res, args, kwargs))
            return res

        return decorated