my_list_1 = [2, 5, 8, 2, 12, 12, 4]
my_list_2 = [2, 7, 12, 3]

# print(my_list_1)
# print(my_list_2)

for item in my_list_2:
    if item not in my_list_1:
        my_list_1.append(item)

# print(my_list_1)
# print(my_list_2)

