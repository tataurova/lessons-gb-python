# проект - парсинг википедии
# по названию темы получить статью из википедии

'''https://ru.wikipedia.org/wiki/Россия'''

import requests


def get_link(topic):
    link = f"https://ru.wikipedia.org/wiki/{topic.capitalize()}"
    return link

#print(get_link('россия'))


def get_topic_page(topic):
    link = get_link(topic)
    html_content = requests.get(link).text
    with open("new.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    return True


print(get_link("россия"))

print(get_topic_page("россия"))

