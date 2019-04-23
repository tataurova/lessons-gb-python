# открываем файл на запись - файла не существует
# f = open('first.txt', 'w')

# открываем файл на чтение - файла не существует
# f = open('second.txt', 'r')

# открываем файл на чтение - файл существует
# f = open('first.txt', 'r')

# открываем файл на запись

#f = open('first.txt', 'w')
#f.write('Hello\n')
#f.write('World\n')

#f.writelines(['Hello\n', 'Python\n'])


# открываем файл на чтение - файл существует. 3 способа чтения:
f = open('first.txt', 'r')

# print(f.read())

# for line in f:
#    print(line.replace('\n', ''))

# print(f.readlines())

# закрытие:

for line in f:
    print(line.replace('\n', ''))

f.close()


with open('first.txt', 'r') as f:
    for line in f:
        print(line.replace('\n', ''))

print('end')





