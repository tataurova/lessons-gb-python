class T1:
    def total(self, n):
        self.value = n + 10


class T2:
    def total(self, s):
        self.value = len(str(s))


t1 = T1()
t2 = T2()
t1.total(45)
t2.total(45)
print(t1.value)
print(t2.value)

print(1 + 1)
print("1" + "1")


class A:
    def __init__(self, v1, v2):
        self.field1 = v1
        self.field2 = v2

    def __str__(self):
        return str(self.field1 + self.field2)


a = A(20, 20)
print(a)
