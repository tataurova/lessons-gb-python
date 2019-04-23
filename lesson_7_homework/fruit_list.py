# Даны два списка фруктов. Получить список фруктов, присутствующих в обоих исходных списках.
# Примечание: Списки фруктов создайте вручную в начале файла.

list1 = ['apple', 'banana', 'orange', 'pineapple']
list2 = ['pear', 'apple', 'kiwi', 'banana']

# через цикл

result = []
for fruit in list1:
    if fruit in list2:
        result.append(fruit)

print(result)

# через lambda

result = filter(lambda fruit: fruit in list2, list1)
print(list(result))

# через генератор

result = [fruit for fruit in list1 if fruit in list2]
print(result)
