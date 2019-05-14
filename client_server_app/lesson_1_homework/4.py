# 4. Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления
# в байтовое

s1 = 'разработка'
s2 = 'администрирование'
s3 = 'protocol'
s4 = 'standard'

print('******Преобразование из строки в байты encode******')

enc_s1 = s1.encode('utf-8')
print(enc_s1)

enc_s2 = s2.encode('utf-8')
print(enc_s2)

enc_s3 = s3.encode('utf-8')
print(enc_s3)

enc_s4 = s4.encode('utf-8')
print(enc_s4)

# выполнить обратное преобразование (используя методы encode и decode).
print('******Обратное преобразование decode******')

dec_s1 = enc_s1.decode('utf-8')
print(dec_s1)

dec_s2 = enc_s2.decode('utf-8')
print(dec_s2)

dec_s3 = enc_s3.decode('utf-8')
print(dec_s3)

dec_s4 = enc_s4.decode('utf-8')
print(enc_s4)