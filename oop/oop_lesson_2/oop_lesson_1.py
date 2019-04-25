import re

with open("index.html", encoding="utf-8") as f:
    s = f.read()


li = re.findall("([0-9\-\+]+) °C", s)
li1 = re.findall("<a class=\"home-link home-link_black_yes\" aria-label=\"([^\"]+)\" href=", s)


print(li)
print(li1)
