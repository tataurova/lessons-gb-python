# Функция простой разделитель


def get_sep(sep, sep_len):
# print(sep * sep_len)
    return sep * sep_len


sep = get_sep('-', 50)
text = 'Hello {} Func {}'.format(sep, sep)
print(text)

print(get_sep('=', 200))

'''

print_sep('*', 100)

print_sep('-', 50)

print('Моя первая функция')
print_sep()
print_sep()

print('Что если их будет много')
print_sep()
print_sep()
print_sep()
print_sep()

'''
