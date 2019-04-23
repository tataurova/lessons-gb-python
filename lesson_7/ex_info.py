number = int(input('Введите число '))

try:
    # код, кот может вызвать исключит ситуацию
    result = 100 / number
except ZeroDivisionError as e:
    # что делать, если произошла исключит ситуация
    print('Деление на 0')
    print('Информация об исключении', e)
except Exception as e:
    print('Неизвестная ошибка')
    print('Информация об исключении', e)
print('Конец')
