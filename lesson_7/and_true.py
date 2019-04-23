import math
numbers = [4, 1, 2, 3, -4, -2, 7, 16]

# создать список из 3 чисел, которые имеют квадратный корень меньше 2 [1, 2, 3]

result = []

# обычный способ

for number in numbers:
    if number > 0:
        sqrt = math.sqrt(number)
        # квадратный корень меньше 2
        if sqrt < 2:
            result.append(number)
print(result)

result = []

# через ленивый and

for number in numbers:
    if number > 0 and math.sqrt(number) < 2:
        result.append(number)
print(result)

# через генератор

result = [number for number in numbers if number > 0 and math.sqrt(number) < 2]
print(result)

