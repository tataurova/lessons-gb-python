# добавление элемента в список

# классический способ


def add_to_list(input_list=None):
    if input_list is None:
        input_list = []
    input_list.append(2)
    return input_list


result = add_to_list([0, 1])
print(result)
result = add_to_list()
print(result)

# через or


def add_to_list(input_list=None):
    # используем свойство вместо условия
    input_list = input_list or []
    input_list.append(2)
    return input_list


result = add_to_list([0, 1])
print(result)
result = add_to_list()
print(result)
