import re

# 1. Получите текст из файла.
f = open('text', 'r', encoding='utf-8')
f = f.read()

# 2. Разбейте текст на предложения.
li1 = re.split("\.\s", f)
print(li1)

# 3. Найдите самую используемую форму слова, состоящую из 4 букв и более, на русском языке.
pattern = "[а-яА-Я]{4,}"  # создаем шаблон для поиска слов
a = re.findall(pattern, f)
print(a)  # выводим список слов

words4 = []
for i in a:
    words4.append(i[0:4])

print(words4)  # выводим список слов, обрезанных до 4 символов

dict = {}
for i in words4:
    dict[i] = words4.count(i)  # создаем словарь, где записываем слово и количество повторов в тексте

print(dict)

list_items = list(dict.items())
list_items.sort(key=lambda i: i[1])
for i in list_items:
    print(i[0], ':', i[1])  # выводим отсортированные элементы (по количеству повторов)
print(f'Самая используемая форма слова: {list_items[len(list_items) - 1][0]}')

# 4. Отберите все ссылки.

li_ref = re.findall("[\d+\w+\.]{1,}ru/*[\d+\w+]*", f)
print(li_ref)

# 5. Ссылки на страницы какого домена встречаются чаще всего?

li_ref_filter = re.findall("[\d+\w+]*.ru", f)  # выводим домены
print(li_ref_filter)

dict_ref = {}  # создаем словарь, где записываем домен и количество повторов в тексте
for i in li_ref_filter:
    dict_ref[i] = li_ref_filter.count(i)
print(dict_ref)

list_ref_items = list(dict_ref.items())
list_ref_items.sort(key=lambda i: i[1])
for i in list_ref_items:
    print(i[0], ':', i[1])  # выводим отсортированные элементы (по количеству повторов)
print(f'Самый используемый домен: {list_ref_items[len(list_ref_items) - 1][0]}')

# 6. Замените все ссылки на текст «Ссылка отобразится после регистрации».
f = ''' В этой статье собраны самые интересные, популярные и полезные туристические сайты. А дальше анализ сайта
 и его удобство вы оцените для себя сами.
 1) travel.mail.ru/travel. Проект под названием Путешествия @ Mail.ru был создан для того, чтобы помочь
  путешественникам найти лучшие места для отдыха, а продавцам туров дать возможность объявить о своих привлекательных
   ценовых предложениях. Затратив минимум времени, посетители портала могут получить всю необходимую информацию по
    турам и странам.
 2) travel.mail.ru/travel2. Один из самых известных сайтов среди любителей далеких путешествий. Здесь постоянно
  обновляются новости, можно купить билеты и туры, а также найти горящие путевки. Удобство сайта заключается еще
   в том, что имеется табло аэропортов, информация о безвизовых странах, о выставках, цены на авиабилеты и
    фоторепортажи.
 3) votpusk.ru/main. Это популярный портал, выполненный в виде интернет-магазина туристических услуг. Описание стран,
  отелей и курортов, отзывы туристов, обзоры, новости и другая полезная информация. Работает портал с 1999 года.
 4) 3totravel.ru. Ресурс посвящен любознательным особам, кто желает побольше узнать информации об удивительных странах.
  Здесь можно не только прочитать свежие новости, но и самим стать авторами статей о приключениях за границей.
   Кроме описания курортов и отелей, на сайте есть гастрономическая страничка, где рассказывается о блюдах с разных
    уголков мира.
 5) geospot.ru/about. На этом ресурсе есть информация о разных странах, а также детальное описание и тонкости получения
  виз. Для тех, кто не желает тратить время на собирание бумажек для посольств, на сайте есть список стран, куда можно
   отправиться сейчас же, безо всяких виз. Путешественники оставляют не только фотоотчеты, а еще видеозаписи
    из поездок.'''

f = re.sub("[\d+\w+\.]{1,}ru/*[\d+\w+]*", "Ссылка отобразится после регистрации", f)
print(f)
