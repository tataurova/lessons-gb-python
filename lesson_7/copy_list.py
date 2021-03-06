import copy

a = [1, 2, 3]
# копия с помощью среза

b = a[:]
b[1] = 200
print(a)

# копия методом copy

b = a.copy()
b[1] = 200
print(a)

# способы не будут работать, если есть вложенные списки

a = [1, 2, [1, 2]]
b = a[:]
b[2][1] = 200
# список a меняется, т к копирование не учитывает вложенность списков
print(a)

b = a.copy()
b[2][1] = 400
print(a)

# копирование модулем copy

a = [1, 2, [1, 2]]
b = copy.deepcopy(a)
b[2][1] = 999
print(a)  # список не меняется


