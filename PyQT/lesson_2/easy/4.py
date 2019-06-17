'''
class Worker:
    hours = NonNegative()
    rate = NonNegative()

    def __init__(self, name, surname, hours, rate):
        ...
'''

'''
class NonNegative:
    ...
    def __set_name__(self, owner, name):
        self.name = name
'''
# object.__set_name__(self, owner, name)

class NonNegative:
    def __get__(self, instance, owner):
        return instance.__dict__[self.my_attr]
    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Не может быть отрицательным")
        instance.__dict__[self.my_attr] = value
    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr

class Worker:
    hours = NonNegative()
    rate = NonNegative()

    def __init__(self, name, surname, hours, rate):
        self.name = name
        self.surname = surname
        self.hours = hours
        self.rate = rate

    def total_profit(self):
        return self.hours * self.rate

w = Worker('Иван', 'Иванов', -10, 100)
print(w.total_profit())

#w.hours = 10
#w.rate = 100
#print(w.total_profit())