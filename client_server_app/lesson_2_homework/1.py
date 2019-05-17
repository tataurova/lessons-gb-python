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


with open('info_1.txt') as f:
    s = f.read()
    temp_sys = re.compile("Изготовитель ОС:[\s+\S+]{1,}\n")
    sys = temp_sys.findall(s)
    #temp_sys = re.compile("Изготовитель ОС:[\s]{1,}[\s+\w+]{1,}\n")


    print(sys)
    temp_os = re.compile("Название ОС:[\s+\S+]{1,}\n")
    #temp_os = re.compile("Название ОС:[\s]{1,}[\s+\w+\d+]{1,}\n")
    os = temp_os.findall(s)
    print(os)
    temp_code = re.compile("Код продукта:[\s+\S+]{1,}\n")
    code = temp_code.findall(s)
    print(code)
    temp_type = re.compile("Тип системы:[\s+\S+]{1,}\n")
    type = temp_type.findall(s)
    print(type)

    '''
    os_prod_list =
    os_name_list =
    os_code_list =
    os_type_list =
'''