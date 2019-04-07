number = 0
n = int(input('Введите число n '))

while number <= n:
    if number % 2 == 0:
        number +=1
        continue
    print(number)
    number +=1