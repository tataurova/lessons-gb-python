# ошибка - преобразование кириллицы в байты
err_str_1 = 'Программа'
print(err_str_1.encode('ascii'))

# ошибка - строку, преобразованную в байты в кодировке utf-8
# преобразуем в строку в кодировке ascii
err_str_2 = 'Программа'
err_str_2_bytes = err_str_2.encode('utf-8')
err_str_2_str = err_str_2_bytes.decode('ascii')
print(err_str_2_str)

# ошибка - разные кодировки для преобразований
err_str_3 = 'Testování'
utf_16_bytes = err_str_3.encode('utf-16')
utf_8_str = utf_16_bytes.decode('utf-8')
print(utf_8_str)