import requests
import json

origin = "LED"
link = "http://min-prices.aviasales.ru/calendar_preload?one_way=true&origin="+origin+"&destination=NCE"
data = json.loads(requests.get(link).text)

print(data["best_prices"][0])
