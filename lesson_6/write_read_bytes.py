# открываем файл для записи байт

with open('bytes.txt', 'wb') as f:
    # пишем строку байт
    f.write(b'Hello bytes')


# открываем файл в текстовом режиме с указанием кодировки, читаем

with open('bytes.txt', 'r', encoding='ascii') as f:
    # пишем строку байт
    print(f.read())


# открываем файл для записи байт

with open('bytes.txt', 'wb') as f:
    # пишем строку байт
    str = 'Привет мир'
    f.write(str.encode('utf-8'))


#  читаем как текст с кодиовкой utf-8

with open('bytes.txt', 'r', encoding='utf-8') as f:
    # пишем строку байт
    print(f.read())


with open('bytes.txt', 'w', encoding='utf-8') as f:
    # пишем строку
    f.write('Привет мир')


# открываем файл в режиме чтения байт

with open('bytes.txt', 'rb') as f:
    # читаем байты
    result = f.read()
    print(result)
    print(type(result))
    # декодируем для получения строки
    s = result.decode('utf-8')
    print(s)

