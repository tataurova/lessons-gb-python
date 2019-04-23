a = 1
b = a
b = 100
print(a)  # число не меняется

a = [1, 2, 3]
b = a
b[1] = 100
print(a)  # в списке меняется значение

numbers = [1, 2, 3]


def change_number_in_list(input_list):
    input_list[1] = 200


change_number_in_list(numbers)
print(numbers)
