is_his_name = False
name = 'Max' if is_his_name else 'Empty'
print(name)

is_one = True
number = 1 if is_one else 2
print(number)

is_russian = True
print('привет' if is_russian else 'Hello')

# слово -- СлОвО
word = 'Привет'

result = []

for i in range(len(word)):
    if i % 2 != 0:
        letter = word[i].lower()
    else:
        letter = word[i].upper()
    result.append(letter)


for i in range(len(word)):
    letter = word[i]
    letter = letter.lower() if i % 2 != 0 else letter.upper()
    result.append(letter)


result = ''.join(result)
print(result)
