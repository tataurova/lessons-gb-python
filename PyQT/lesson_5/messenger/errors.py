

# Исключение. Отсутствует обязательный атрибут response
class MandatoryKeyError(Exception):
    def __init__(self, key):
        self.key = key

    def __str__(self):
        return 'Не хватает обязательного атрибута {}'.format(self.key)


# Исключение  - некорректные данные получены от сокета
class IncorrectDataRecivedError(Exception):
    def __str__(self):
        return 'Принято некорректное сообщение от удалённого компьютера.'


# Исключение - ошибка сервера
class ServerError(Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text


# исключение - аргумент функции не словарь.
class NonDictInputError(Exception):
    def __str__(self):
        return 'Аргумент функции должен быть словарём.'


# Ошибка - отсутствует обязательное поле в принятом словаре.
class ReqFieldMissingError(Exception):
    def __init__(self, missing_field):
        self.missing_field = missing_field

    def __str__(self):
        return f'В принятом словаре отсутствует обязательное поле {self.missing_field}.'

