import requests
import re

req = requests.get("https://yandex.ru")
s = req.text


li = re.findall("<a class=\"home-link home-link_black_yes\" aria-label=\"([^\"]+)\" href=", s)

print(s)
print(li)
