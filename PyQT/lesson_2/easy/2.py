class Worker:
    def __init__(self, name, surname, hours, rate):
        self.name = name
        self.surname = surname
        self._hours = hours
        self._rate = rate

    @property
    def hours(self):
        return self._hours

    @hours.setter
    def hours(self, value):
        if value < 0:
            raise ValueError("Значение часов не может быть отрицательным")
        self._hours = value

    @property
    def rate(self):
        return self._rate

    @rate.setter
    def rate(self, value):
        if value < 0:
            raise ValueError("Значение ставки не может быть отрицательным")
        self._rate = value

    def total_profit(self):
        return self.hours * self.rate

w = Worker('Иван', 'Иванов', 10, 100)
print(w.total_profit())

w.hours = -10
w.rate = 100
print(w.total_profit())


