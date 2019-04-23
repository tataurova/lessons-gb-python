# Создать модуль music_serialize.py. В этом модуле определить словарь для вашей любимой музыкальной группы, например:
# my_favourite_group = {
# ‘name’: ‘Г.М.О.’,
# ‘tracks’: [‘Последний месяц осени’, ‘Шапито’],
# ‘Albums’: [{‘name’: ‘Делать панк-рок’,‘year’: 2016},
# {‘name’: ‘Шапито’,‘year’: 2014}]}
#
# С помощью модулей json и pickle сериализовать данный словарь в json и в байты,
# вывести результаты в терминал. Записать результаты в файлы group.json, group.pickle соответственно.
# В файле group.json указать кодировку utf-8.

import pickle
import json

my_favourite_group = {'name': 'ГМО', 'tracks': ['Последний месяц осени', 'Шапито'],
                      'Albums': [{'name': 'Делать панк-рок', 'year': 2016},
                                 {'name': 'Шапито', 'year': 2014}]}

print(my_favourite_group)
print(type(my_favourite_group))

# записываем в json

with open('group.json', 'w', encoding='utf-8') as f:
    json.dump(my_favourite_group, f)

print('Записали в json')

# записываем в байты

with open('group.pickle', 'wb') as f:
    pickle.dump(my_favourite_group, f)

print('Записали в байты')
