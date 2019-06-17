class Worker:
    def __init__(self, name, surname, hours, rate):
        self.name = name
        self.surname = surname
        self.hours = hours
        self.rate = rate
    def total_profit(self):
        return self.hours * self.rate
w = Worker('Иван', 'Иванов', 10, 100)
print(w.total_profit())


w.hours = -10
w.rate = 100
print(w.total_profit())



