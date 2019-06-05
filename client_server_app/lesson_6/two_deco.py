def make_ext(fn):
    return lambda: "<ext_tag>" + fn() + "</ext_tag>"


def make_int(fn):
    return lambda: "<int_tag>" + fn() + "</int_tag>"


@make_ext
@make_int
def func():
  return "Какой-то текст"

# порядок выполнения декораторов
# сначала make_ext, потом make_int
# func = make_ext(make_int(func))

# описание вызовов
'''
hello() = lambda : "<ext_tag>" + fn() + "</ext_tag>" #  где fn() ->
    lambda : "<int_tag>" + fn() + "</int_tag>" # где fn() ->
        return "Какой-то текст"
'''

print(func())
