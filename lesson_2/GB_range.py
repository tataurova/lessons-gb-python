numbers = range(10)

print(list(numbers))


numbers = range(66)

print(list(numbers))

winners = ['Max', 'Leo', 'Kate']

# простой перебор

for winner in winners:
    print(winner)

# использум range

for i in range(len(winners)):
    print(i, ')', winners[i])


numbers = [1, 3, 5]

for number in numbers:
    print(number)

print(list(range(1, 1000, 2)))

for number in range (1, 10, 2):
    print(number)
