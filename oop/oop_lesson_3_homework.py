# 1. Написать функцию получения IATA-кода города из его названия, используя API Aviasales.

import requests
import json

origin = input('Введите название города: ')


def f(origin):
    link = "http://autocomplete.travelpayouts.com/places2?term=" + origin + "&locale=ru&types[]=city"
    data = json.loads(requests.get(link).text)
    a = data[0]
    b = a.get('code')
    return b


print(f(origin))

