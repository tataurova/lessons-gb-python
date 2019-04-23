# строка

s = 'Hello'

print(type(s))

# строка байт

sb = b'Hello bytes'

print(type(sb))

# вывод строки байт

print(sb)

# индекс строки

print(s[1])

print(sb[1])

# срез

print(s[1:3])
print(sb[1:3])

# перебор строки байт в цикле (получим код символа)

for item in sb:
    print(item)

sb2 = b'Ad'

# по ascii должно получиться 65

print(sb2[0])
print(sb[1])


s2 = 'Hello world Мир'

sb3 = s2.encode('utf-8')
print(sb3)
print(type(sb3))

s2 = sb3.decode('utf-8')
print(s2)
print(type(s))
