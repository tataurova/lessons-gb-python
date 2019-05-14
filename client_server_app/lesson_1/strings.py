# примеры строк
progr_1 = 'Программирование'
print(progr_1)
print(type(progr_1))
progr_2 = 'Programování'
print(progr_2)

# форматы записи юникод-символов
unic_s_1 = '\N{LATIN SMALL LETTER C WITH DOT ABOVE}'
print(unic_s_1)

unic_s_2 = '\u010B'
print(unic_s_2)

# строка, как последовательность юникод-символов
progr_3 = 'Программа'
progr_4 = '\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430'
print(progr_4)

print(progr_3 == progr_4)

print(len(progr_4))

# функция ord позволяет получить числовое значение юникод-символа
print(ord('ã'))

# ункция chr позволяет получить символ по коду
print(chr(227))