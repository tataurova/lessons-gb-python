from tabulate import tabulate

# генерация таблицы без шапки
tuples_list = [('Python', 'interpreted', '1991'),
                ('JAVA', 'compiled', '1995'),
                ('С', 'compiled', '1972')]
print(tabulate(tuples_list))

# генерация таблицы с шапкой
tuples_list = [('Python', 'interpreted', '1991'),
                ('JAVA', 'compiled', '1995'),
                ('С', 'compiled', '1972')]
print()
columns = ['programming language', 'type', 'year']
print(tabulate(tuples_list, headers=columns))

print()

# генерация таблицы с шапкой
# шапка - первый элемент списка
from tabulate import tabulate
tuples_list = [ ('programming language', 'type', 'year'),
                ('Python', 'interpreted', '1991'),
                ('JAVA', 'compiled', '1995'),
                ('С', 'compiled', '1972')]

# Указание первой строки таблицы как набора заголовков
print(tabulate(tuples_list, headers = 'firstrow'))

print()

# если данные - список словарей, значение параметра headers является оператор keys
dicts_list = [{'programming language': 'Python',
               'type': 'interpreted',
               'year': '1991'},
              {'programming language': 'JAVA',
               'type': 'compiled',
               'year': '1995'},
              {'programming language': 'С',
               'type': 'compiled',
               'year': '1972'}]

# Табличное представление списка словарей
print(tabulate(dicts_list, headers = 'keys'))








