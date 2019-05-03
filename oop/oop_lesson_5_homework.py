# 1. Создайте класс Word.
# 2. Добавьте свойства text и part of speech.
# 3. Добавьте возможность создавать объект слово со значениями в скобках.


class Word:
    def __init__(self, text, part_of_speech):
        self.text = text
        self.part_of_speech = part_of_speech


w1 = Word('студент', 'существительное')
w2 = Word('выполняет', 'глагол')
w3 = Word('задания', 'существительное')

print(w1.text, w1.part_of_speech)
print(w2.text, w2.part_of_speech)
print(w3.text, w3.part_of_speech)

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
            print(f"{self.words[i-1].text}", end=" ")
        print('\n')

    def show_parts(self):
        print(f"Результат выполнения метода show_parts (части речи, входящие в предложение):")
        for i in self.content:
            print(f" {self.words[i-1].part_of_speech}")


my_sent = Sentence([1, 2, 3], [w1, w2, w3])

my_sent.show()
my_sent.show_parts()



