# 6. Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование»,
# «сокет», «декоратор». Проверить кодировку файла по умолчанию. Принудительно открыть файл в формате Unicode
# и вывести его содержимое.

# получаем кодировку для ОС по умолчанию
import locale

def_coding = locale.getpreferredencoding()
print(def_coding)

f_n = open('test_file.txt', 'w', encoding='utf-8')
f_n.write('сетевое программирование \n сокет \n декоратор')
f_n.close()
print(type(f_n))


with open('test_file.txt', encoding='utf-8') as f_n:
    for el_str in f_n:
        print(el_str, end='')



