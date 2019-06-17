'''
a = 5
print(type(a))
print(type(int))
'''

# первый вариант создания пользовательксого класса
class A():
    pass

#a = A()
#print(a)

# второй вариант создания пользовательксого класса
#A = type(A, (), {})
#a = A()
#print(a)


class MyInt(type):
    def __call__(cls, *args, **kwargs):
       print("Здесь какое-то поведение для класса int")
       return type.__call__(cls, *args, **kwargs)

class int(metaclass=MyInt):
    def __init__(self, x, y):
        self.x = x
        self.y = y

i = int(4,5)
print(i.x)
