import requests

def get_link(topic):
    link = f"https://ru.wikipedia.org/wiki/{topic.capitalize()}"
    return link

def get_topic_page(topic):
    link = get_link(topic)
    html_content = requests.get(link).text
    return html_content

print(get_topic_page("россия"))

