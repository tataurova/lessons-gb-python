import math

if 1 > 2 and math.sqrt(-1):
    print('Ошибки не будет, т.к. первое условие ложь, дальше проверка не пойдет')

# вернется первая ложь ''
print([1] and [2] and '' and 1)

# вернется последняя истина

print([1] and [1] and 20 and 1)
