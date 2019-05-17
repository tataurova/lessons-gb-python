import csv

# Простое чтение из файла kp_data.csv
with open('kp_data.csv') as f_n:
    f_n_reader = csv.reader(f_n)
    print(type(f_n_reader))
    for row in f_n_reader:
        print(row)

with open('kp_data.csv') as f_n:
    f_n_reader = csv.reader(f_n)
    print(list(f_n_reader))

with open('kp_data.csv') as f_n:
    f_n_reader = csv.reader(f_n)
    f_n_headers = next(f_n_reader)
    print('Headers: ', f_n_headers)
    for row in f_n_reader:
        print(row)

with open('kp_data.csv') as f_n:
    f_n_reader = csv.DictReader(f_n)
    for row in f_n_reader:
        print(row)
        print(row['hostname'], row['model'])


'''
# Получаем итератор объекта
with open('kp_data.csv') as f_n:
    f_n_reader = csv.reader(f_n)
    print(f_n_reader)

# Преобразование итератора в список
with open('kp_data.csv') as f_n:
    f_n_reader = csv.reader(f_n)
    print(list(f_n_reader))



# Разделение строки заголовков от содержимого
with open('kp_data.csv') as f_n:
    f_n_reader = csv.reader(f_n)
    f_n_headers = next(f_n_reader)
    print('Headers: ', f_n_headers)
    for row in f_n_reader:
        print(row)


# Вывод результата с помощью метода DictReader
with open('kp_data.csv') as f_n:
    f_n_reader = csv.DictReader(f_n)
    for row in f_n_reader:
        print(row)
        print(row['hostname'], row['model'])
'''