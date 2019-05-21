s = 'Python'

bs = b'Python'

ba = bytearray(bs)

s2 = bs.decode('cp1251')
bs2 = s.encode('koi8-r')
ba2 = bytearray(s, 'utf-8')
