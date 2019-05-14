# Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.

s1 = b'attribute'
# s2 = b'класс'   s2 и s3 не записать в байтовом типе
# s3 = b'функция'
s4 = b'type'

print(s1)
print(type(s1))

'''
print(s2)
print(type(s2))

print(s3)
print(type(s3))
'''

print(s4)
print(type(s4))
