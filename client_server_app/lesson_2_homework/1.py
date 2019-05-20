'''
1. Задание на закрепление знаний по модулю CSV.

    Написать скрипт, осуществляющий выборку определенных данных из файлов
    info_1.txt, info_2.txt, info_3.txt и формирующий новый «отчетный» файл в формате CSV. Для этого:

a. Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными, их открытие и считывание
    данных. В этой функции из считанных данных необходимо с помощью регулярных выражений извлечь значения параметров
    «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы». Значения каждого параметра поместить в
    соответствующий список. Должно получиться четыре списка — например, os_prod_list, os_name_list, os_code_list,
    os_type_list. В этой же функции создать главный список для хранения данных отчета — например, main_data — и
    поместить в него названия столбцов отчета в виде списка: «Изготовитель системы», «Название ОС», «Код продукта»,
    «Тип системы». Значения для этих столбцов также оформить в виде списка и поместить в файл main_data (также для
    каждого файла);
b. Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. В этой функции реализовать получение данных
    через вызов функции get_data(), а также сохранение подготовленных данных в соответствующий CSV-файл;

'''

import csv
import re
import glob

os_prod_list = []
os_name_list = []
os_code_list = []
os_type_list = []
headers = ['Изготовитель ОС', 'Название ОС', 'Код продукта', 'Тип системы']


def check_string(line, parameter_name):
    template = "^" + parameter_name + ":"
    result = re.search(template, line)
    if "re" in dir(result):
        return True


def get_data():
    files = glob.glob('*.txt')

    for file in files:
        log_file = open(file, mode="r", encoding="windows-1251")

        for line in log_file:
            if check_string(line, "Изготовитель ОС"):
                os_prod_list.append(line[34:-1])
            elif check_string(line, "Название ОС"):
                os_name_list.append(line[34:-1])
            elif check_string(line, "Код продукта"):
                os_code_list.append(line[34:-1])
            elif check_string(line, "Тип системы"):
                os_type_list.append(line[34:-1])

        log_file.close()


def write_to_csv(file_csv):
    f_n_writer = csv.writer(file_csv)
    f_n_writer.writerow(headers)

    get_data()

    for i in range(len(os_prod_list)):
        current_row = []
        current_row.append(os_prod_list[i])
        current_row.append(os_name_list[i])
        current_row.append(os_code_list[i])
        current_row.append(os_type_list[i])
        f_n_writer.writerow(current_row)


write_to_csv(open('main_data.csv', 'w'))
