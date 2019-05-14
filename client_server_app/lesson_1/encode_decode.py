# прсстое кодирование - encode
enc_str = 'Кодировка'
enc_str_bytes = enc_str.encode('utf-8')
print(enc_str_bytes)

# простое декодирование - decode
dec_str_bytes = b'\xd0\x9a\xd0\xbe\xd0\xb4\xd0\xb8\xd1\x80\xd0\xbe\xd0\xb2\xd0\xba\xd0\xb0'
dec_str = dec_str_bytes.decode('utf-8')
print(dec_str)

# метод encode для класса str (кодировка указана как ключевой аргумент)
str_1 = 'Программа'
str_1_enc = str.encode(str_1, encoding='utf-8')
print(str_1_enc)

# метод decode для класса bytes (кодировка указана как ключевой аргумент)
bytes_1 = b'\xd0\x9f\xd1\x80\xd0\xbe\xd0\xb3\xd1\x80\xd0\xb0\xd0\xbc\xd0\xbc\xd0\xb0'
bytes_1_enc = bytes.decode(bytes_1, encoding='utf-8')
print(bytes_1_enc)

