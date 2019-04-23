import os

# имя ос
print(os.name)

# текущая директория
print(os.getcwd())

# создать новый путь ( в скобках текущий путь и папка, которую будем создавать)
new_path = os.path.join(os.getcwd(), 'new_f')

# создать папку по новому пути
os.mkdir(new_path)
