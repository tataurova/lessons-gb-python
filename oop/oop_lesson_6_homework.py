# 1. Создайте классы Noun и Verb.
# 2. Настройте наследование от Word.
# 3. Добавьте защищенное свойство «Грамматические характеристики».
# 4. Перестройте работу метода show класса Sentence.
# 5. Перестройте работу метода show_part класса Sentence, чтобы он показывал грамматические характеристики.


class Word:
    def __init__(self, text, number):
        self.text = text
        self.number = number


class Verb(Word):
    _gram_char = 'глагол'


class Noun(Word):
    _gram_char = 'существительное'


w1 = Noun('студент', 1)
w2 = Verb('выполняет', 2)
w3 = Noun('задания', 3)
w4 = Noun('лишнее', 4)

print(w1.text, w1._gram_char)
print(w2.text, w2._gram_char)
print(w3.text, w3._gram_char)


# из 5 урока
# 4. Создайте класс Sentence
# 5. Добавьте свойство content, равное списку, состоящему из номеров слов, входящих в предложение.
# 6. Добавьте метод show, составляющий предложение.
# 7. Добавьте метод show_parts, отображающий, какие части речи входят в предложение.


class Sentence:
    def __init__(self, content, words):
        self.content = content
        self.words = words

    def show(self):
        print("Результат выполнения метода show (составление предложения): ")
        for i in self.content:
            for k in range(len(self.words)):
                if self.words[k - 1].number == i:
                    print(f"{self.words[k - 1].text}", end=" ")
        print('\n')

    def show_parts(self):
        print(f"Результат выполнения метода show_parts (части речи, входящие в предложение):")
        for i in self.content:
            print(f" {self.words[i - 1]._gram_char}")


my_sent = Sentence([1, 2, 3], [w4, w3, w2, w1])

my_sent.show()
my_sent.show_parts()
