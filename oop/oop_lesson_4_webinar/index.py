import re
from wiki_requests import get_topic_page

def get_topic_text(topic):
    html_content = get_topic_page(topic)
    words = re.findall("[а-яА-Я\-\']+", html_content)
    text = " ".join(words)
    return text

def get_topic_words(topic):
    html_content = get_topic_page(topic)
    words = re.findall("[а-яА-Я\-\']+", html_content)
    return words
'''
text1 = get_topic_page("Россия")
print(text1)
text1 = get_topic_text("россия")
print(text1)
print(text1[10000:10200])
print(len(text1))
text2 = get_topic_text("Москва")
print(text2)
print(len(text2))
print(text2[10000:10200])
'''



