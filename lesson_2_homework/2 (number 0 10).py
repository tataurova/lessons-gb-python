n = int(input('Введите число '))
while n < 0 or n > 10:
    n = int(input('Число должно быть от 0 до 10. Введите еще раз '))
    if 0 <= n <= 10:
        break

print(n * n)


