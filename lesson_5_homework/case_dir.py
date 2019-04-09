# Создайте модуль (модуль — программа на Python, т.е. файл с расширением .py).
# В нем напишите функцию, создающую директории от dir_1 до dir_9 в папке, из которой запущен данный код.
# Затем создайте вторую функцию, удаляющую эти папки. Проверьте работу функций в этом же модуле.

import os


def create_dir():
    for i in range(1, 10):
        new_path = os.path.join(os.getcwd(), f'dir_{i}')
        os.mkdir(new_path)


create_dir()


def remove_dir():
    for i in range(1, 10):
        path = os.path.join(os.getcwd(), f'dir_{i}')
        os.rmdir(path)


remove_dir()

test = 'Привет'

