

# Исключение - ошибка сервера
class ServerError(Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text


class IncorrectDataRecivedError(Exception):
    def __str__(self):
        return 'Принято некорректное сообщение от удалённого компьютера'


# исключение - аргумент функции не словарь.
class NonDictInputError(Exception):
    def __str__(self):
        return 'Аргумент функции должен быть словарём'
