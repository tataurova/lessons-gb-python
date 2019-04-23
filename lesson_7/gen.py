# записать в список только положительные числа

numbers = [1, 2, 3, 4, 5, 6, -1, -2, -3]

# классический способ

result = []
for number in numbers:
    if number > 0:
        result.append(number)

print(result)

# через функцию filter
result = filter(lambda number: number > 0, numbers)
print(list(result))

# через генератор
result = [number for number in numbers if number > 0]
print(result)
