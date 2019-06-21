# Подключение библиотеки, соответствующей типу требуемой базы данных
import sqlite3
import os.path

sqlfile = os.path.join(os.path.dirname(__file__), "demo.sqlite")

# Создание соединения с базой данных
# В данном случае это файл базы
conn = sqlite3.connect(sqlfile)

# Создаем курсор — это специальный объект, который делает запросы и получает их результаты
cursor = conn.cursor()

# ========== ТУТ БУДЕТ КОД РАБОТЫ С БАЗОЙ ДАННЫХ ===========
# ===== КОД ДАЛЬНЕЙШИХ ПРИМЕРОВ ВСТАВЛЯТЬ СЮДА =============

# В конце необходимо закрыть соединение с базой данных
conn.close()

'''
conn = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
'''

############################Чтение##################################
cursor.execute("SELECT Name FROM Artist ORDER BY Name LIMIT 3")

# Получение результатов запроса
results = cursor.fetchall()
results2 = cursor.fetchall()

print(results)
# [('A Cor Do Som',), ('Aaron Copland & London Symphony Orchestra',), ('Aaron Goldberg',)]
print(results2)
# []

############################Запись###################################
# Выполняется INSERT-запрос к базе данных с обычным SQL-синтаксисом
cursor.execute("insert into Artist values (Null, 'A Aagrh!') ")

# Если выполняются изменения в базе данных, необходимо сохранить транзакцию
conn.commit()
# Проверка результатов
cursor.execute("SELECT Name FROM Artist ORDER BY Name LIMIT 3")
results = cursor.fetchall()
print(results)  # [('A Aagrh!',), ('A Cor Do Som',), ('Aaron Copland & London Symphony Orchestra',)]

#################Несколько запросов за раз####################
#cursor.execute("""
  #insert into Artist values (Null, 'A Aagrh!');
  #insert into Artist values (Null, 'A Aagrh-2!');
#""")
# Будет ошибка
# sqlite3.Warning: You can only execute one statement at a time.

'''
cursor.execute("""insert into Artist values (Null, 'A Aagrh!');""")
cursor.execute("""insert into Artist values (Null, 'A Aagrh-2!');""")
'''

cursor.executescript("""
 insert into Artist values (Null, 'A Aagrh!');
 insert into Artist values (Null, 'A Aagrh-2!');
""")

#################Подстановка значений в запрос#####################
# 1. C подстановкой по порядку на места знаков вопросов:
cursor.execute("SELECT Name FROM Artist ORDER BY Name LIMIT ?", ('2'))
# 2. C использованием именованных замен:
cursor.execute("SELECT Name from Artist ORDER BY Name LIMIT :limit", {"limit": 3})

paramstyle = sqlite3.paramstyle

if paramstyle == 'qmark':
    ph = "?"
elif paramstyle == 'format':
    ph = "%s"
else:
    raise Exception("Unexpected paramstyle: %s" % paramstyle)

sql = "INSERT INTO foo VALUES (%(ph)s, %(ph)s, %(ph)s)" % { "ph" : ph }

################Множественная подстановка значений########################
# Обратите внимание: даже одно значение нужно передавать кортежем!
# Именно поэтому тут используется запятая в скобках
new_artists = [
    ('A Aagrh!',),
    ('A Aagrh!-2',),
    ('A Aagrh!-3',),
]
cursor.executemany("insert into Artist values (Null, ?);", new_artists)


###############Получение результатов#################
cursor.execute("SELECT Name FROM Artist ORDER BY Name LIMIT 3")
print(cursor.fetchone())    # ('A Cor Do Som',)
print(cursor.fetchone())    # ('Aaron Copland & London Symphony Orchestra',)
print(cursor.fetchone())    # ('Aaron Goldberg',)
print(cursor.fetchone())    # None

########################Курсор как итератор#########################
# Использование курсора как итератора
for row in cursor.execute('SELECT Name from Artist ORDER BY Name LIMIT 3'):
    print(row)

# Полученный результат:
# ('A Cor Do Som',)
# ('Aaron Copland & London Symphony Orchestra',)
# ('Aaron Goldberg',)

##########################Обработка ошибок###############################
try:
    cursor.execute(sql_statement)
    result = cursor.fetchall()
except sqlite3.DatabaseError as err:
    print("Error: ", err)
else:
    conn.commit()







