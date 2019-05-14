# 1. Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и проверить тип и содержание
# соответствующих переменных. Затем с помощью онлайн-конвертера преобразовать строковые представление в формат Unicode
# и также проверить тип и содержимое переменных.

str_1 = 'разработка'
str_2 = 'сокет'
str_3 = 'декоратор'
print(str_1)
print(type(str_1))

print(str_2)
print(type(str_2))

print(str_3)
print(type(str_3))

enc_str_1 = b'\xd1\x80\xd0\xb0\xd0\xb7\xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd0\xba\xd0\xb0'
enc_str_2 = b'\xd1\x81\xd0\xbe\xd0\xba\xd0\xb5\xd1\x82'
enc_str_3 = b'\xd0\xb4\xd0\xb5\xd0\xba\xd0\xbe\xd1\x80\xd0\xb0\xd1\x82\xd0\xbe\xd1\x80'

print(enc_str_1)
print(type(enc_str_1))
print(enc_str_2)
print(type(enc_str_2))
print(enc_str_3)
print(type(enc_str_3))
