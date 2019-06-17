
# --------------------- Атрибут __slots__ ----------------------------------

# В обычной ситуации в Python в объекты можно добавлять новые атрибуты
# вне описания класса:
"""
class BasicClass(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Создадим объект нашего класса.
bc = BasicClass(13, 42)
# В обычной ситуации все атрибуты объекта хранятся во внутреннем словаре __dict__:
print(bc.__dict__)

# Строка ниже не вызовет ошибку. Атрибут z будет добавлен в уже созданный объект
bc.z = 777
print(bc.__dict__)
print(dir(bc))
"""

# Но такое поведение классов/объектов не всегда удобно.

# В классах "нового стиля" (в Python 3 - все классы нового стиля)
# имеется возможность задавать атрибут класса __slots__, который позволяет
# ограничить добавление объекту новых атрибутов вне описания класса.
"""
class StrictClass():
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.z = {'name': 'John', 'age':12}

sc = StrictClass(13, 42)
sc2 = StrictClass(11, 44)

# У объекта такого класса не будет атрибута __dict__:
print(dir(sc))
# print(sc.__dict__)        # <- вызовет ошибку
print(sc.__slots__)

print(sc.x, sc.y, sc2.x, sc2.y)

# Такому объекту невозможно добавить новый атрибут:
# sc.z = 16                 # <- вызовет ошибку
"""

class StrictClass():
    __slots__ = ('x', 'y', 'z')
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.z = {'name': 'John', 'age':12}

r = StrictClass(2, 3)
print(dir(r))
print(r.z)
r.z['name'] = 'Vanya'
r.z['age'] = 15
r.z['sdf'] = 17
print(r.z)