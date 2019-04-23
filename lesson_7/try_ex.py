number = int(input('Введите число '))
try:
    result = 100 / number
except ZeroDivisionError:
    print('Деление на 0')
except Exception:
    print('Неизвестная ошибка')
print('Конец')
