# -*- coding: utf-8 -*-
# получаем кодировку для ОС по умолчанию
import locale

def_coding = locale.getpreferredencoding()
print(def_coding)

# получаем кодировку для файла, с которым работаем
f_n = open('test.txt.txt', 'w')
f_n.write('test.txt test.txt test.txt')
f_n.close()
print(type(f_n))

# явное указание кодировки при работе с файлом
with open('test.txt.txt', encoding='utf-8') as f_n:
    for el_str in f_n:
        print(el_str, end='')