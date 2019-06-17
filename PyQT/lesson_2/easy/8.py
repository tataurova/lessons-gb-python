# создаем метакласс - фабрику классов
# определяем для фабрики классов общие параметры
My = type("MyClass", (), {"attribute": 5})
print(My)

my_class = My()
print(my_class.attribute)

my_class_new = My()
print(my_class_new.attribute)


