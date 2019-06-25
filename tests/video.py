from bs4 import BeautifulSoup
from urllib.request import urlopen

html_doc = urlopen('https:').read()

soup = BeautifulSoup(html_doc)

print(soup)
print(soup)

print(soup.find('div', ''))


print(soup.prettify())

print(soup.contents)
