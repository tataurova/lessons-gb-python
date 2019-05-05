class A:
    def __init__(self, v1):
        self.field = v1

    def str(self):
        return str(self.field1)

    # def foo(self, other):
    #    return self.field > other.field
    def __gt__(self, other):  # магич матоды для сравнения
        return self.field > other.field

    def __lt__(self, other):
        return self.field < other.field


item1 = A(20)
item2 = A(24)
item3 = A(300)
# print(item1.foo(item3))
print(item1 > item2)