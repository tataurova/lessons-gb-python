class NonNegative:
    # вместо my_attr на самом деле будет hours или rate
    def __init__(self, my_attr):
        self.my_attr = my_attr  # (3)
    def __get__(self, instance, owner):
        # owner - класс
        return instance.__dict__[self.my_attr]  # (5)
    def __set__(self, instance, value):
        # instance - экземпляр класса
        if value < 0:
            raise ValueError("Не может быть отрицательным")
        instance.__dict__[self.my_attr] = value  # (9)

class Worker:
    hours = NonNegative('hours')
    rate = NonNegative('rate')

    def __init__(self, name, surname, hours, rate):
        self.name = name
        self.surname = surname
        self.hours = hours
        self.rate = rate

    def total_profit(self):
        return self.hours * self.rate

w = Worker('Иван', 'Иванов', 10, -100)
print(w.total_profit())

#w.hours = 10
#w.rate = 100
#print(w.total_profit())

