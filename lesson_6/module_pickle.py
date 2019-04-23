person = {'name': 'Max', 'phones': [123, 345]}

# откроем файл

with open('person.dat', 'wb') as f:
    # запишем объект в файл построчно
    # возьмем имя
    name = person['name']
    # добавим перенос строки, переведем в байты и запишем
    f.write(f'{name}\n'.encode('utf-8'))
    # получим телефоны
    phones = person['phones']
    # запишем 1 телефон в новую строку
    for phone in phones:
        f.write(f'{phone}\n'.encode('utf-8'))

print('Объект записан')

# читаем объект из файла

# откроем файл

with open('person.dat', 'rb') as f:
    # теперь надо знать, как записывали объект
    # прочитаем файл в список
    result = f.readlines()

# теперь воссоздаем исходный объект

person = {}

# первый элемент это имя

person['name'] = result[0].decode('utf-8').replace('\n', '')

# далее идут телефоны

phones = []

for bphone in result[1:]:
    phones.append(bphone.decode('utf-8').replace('\n', ''))

person['phones'] = phones

# получили исходный объект, а что, если он изменится?
print(person)
