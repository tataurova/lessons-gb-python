# Создать модуль music_deserialize.py.
# В этом модуле открыть файлы group.json и group.pickle, прочитать из них информацию.
# Получить объект — словарь из предыдущего задания.

import pickle
import json

# открываем файл с байтами

with open('group.pickle', 'rb') as f:
    my_favourite_group = pickle.load(f)

print(my_favourite_group)
print(type(my_favourite_group))

# открываем файл .json

with open('group.json', 'r') as f:
    my_favourite_group = json.load(f)

print(my_favourite_group)
print(type(my_favourite_group))
