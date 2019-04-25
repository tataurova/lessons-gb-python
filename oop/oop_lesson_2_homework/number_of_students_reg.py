# Получить количество учеников с сайта geekbrains.ru:
# a) при помощи регулярных выражений

import re

with open("index_gb.html", encoding="utf-8") as f:
    s = f.read()

li = re.findall("Нас уже[\d+\s+]*человек", s)
print(li)
li = str(li)

w = re.sub("\s+", "", li)  # убираем пробелы

number = re.findall("\d+", w)  # достаем число
print(number)
