# декоратор в виде функции
def mod_bar(cls):
    # возвращает модифицированный класс
    def decorate(func):
        # возвращает декорированную функцию
        def new_func(self):
            # здесь вызываем исходную функцию
            # и дополняем ее поведение
            print(self.start_str)
            print(func(self))
            print(self.end_str)

        return new_func

    cls.bar = decorate(cls.bar)
    return cls


@mod_bar
class Test(object):
    def __init__(self):
        self.start_str = "Запуск декоратора"
        self.end_str = "Завершение декоратора"

    def bar(self):
        return "Какая-то функциональность метода класса"


a = Test()
a.bar()
