# 1. Написать функцию получения IATA-кода города из его названия, используя API Aviasales.

import requests
import json


origin = input('Введите название города: ')
link = "https://www.travelpayouts.com/widgets_suggest_params?q=Из%20"+origin+"%20в%20Лондон"

data = json.loads(requests.get(link).text)
print(data)
