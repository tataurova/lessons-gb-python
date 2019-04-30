import re
from wiki_requests import get_topic_page



def get_topic_words(topic):
    html_content = get_topic_page(topic)
    words = re.findall("[а-яА-Я\-\']+", html_content)
    # слова, в которых более 3-х букв
    words = re.findall("[а-яА-Я\-\']{3,}", html_content)
    return words

def get_common_words(topic):
    words_list = get_topic_words(topic)
    # рейтинг встречаемости слов
    rate = {}
    for word in words_list:
        if word in rate:
            rate[word] += 1
        else:
            rate[word] = 1
    #return rate
    rate_list = list(rate.items())
    print(rate_list)
    # сортируем - самые редкие
    rate_list.sort(key = lambda x: x[1])
    # сортируемы - самые частые
    rate_list.sort(key = lambda x: -x[1])
    return rate_list

rate = get_common_words("Россия")
print(rate)

# красивая визуализация для отчета
def visualize_common_words(topic):
    words = get_common_words(topic)
    for w in words[100:110]:
        print(w[0])
    print("top 50:53:", words[50:53])

def main():
    topic = input("Topic: ")
    visualize_common_words(topic)

visualize_common_words("Россия")


# через консоль
#words = get_topic_words("россия")
#print(len(words))
#print(words[1010])
#rate = get_common_words("Россия")
#rate[0]
#rate[100]
#rate = get_common_words("Россия")
#print(rate)




