number = int(input('Введите число '))

try:
    # код, кот может вызвать исключит ситуацию
    result = 100 / number
except:
    # что делать, если произошла исключит ситуация
    print('Деление на 0')
else:
    # что делать, если ошибок не было
    print('Все хорошо')
finally:
    print('Выполняется всегда')