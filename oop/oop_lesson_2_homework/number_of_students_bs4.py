# Получить количество учеников с сайта geekbrains.ru:
# b) при помощи библиотеки BeautifulSoup.

from bs4 import BeautifulSoup as BS
import re

with open("index_gb.html", encoding="utf-8") as f:
    s = f.read()

soup = BS(s, "html.parser")

string = soup.find('span', {'class': 'total-users'}).text  # находим нужный элемент
print(string)

w = re.sub("\s+", "", string)  # убираем пробелы

number = re.findall("\d+", w)  # достаем число
print(number)
