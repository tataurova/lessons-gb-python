 # обработка ошибки кодирования с заменой символа знаком вопроса
handl_err = 'Testování'
handl_err_bytes_1 = handl_err.encode('ascii', 'replace')
print(handl_err_bytes_1)


# обработка ошибки кодирования с заменой символа его именем
handl_err_bytes_2 = handl_err.encode('ascii', 'namereplace')
print(handl_err_bytes_2)


# игнорирование ошибки при кодировании
handl_unicode = 'Testování'
handl_bytes = handl_unicode.encode('ascii', 'ignore')
print(handl_bytes)



# игнорирование лшибки при декодировании
handl_str = 'Testování'
handl_str_utf8 = handl_str.encode('utf-8')
print(handl_str_utf8)
handl_str_utf8_str = handl_str_utf8.decode('ascii', 'ignore')
print(handl_str_utf8_str)


# замена ошибки при декодировании
handl_str = 'Testování'
handl_str_utf8 = handl_str.encode('utf-8')
handl_str_utf8_str = handl_str_utf8.decode('ascii', 'replace')
print(handl_str_utf8_str)
