import modules
# import modec # импорт всего модуля (будет выполняться сначала)
from modec import foo # при частичном импорте выполняется весь скрипт. имя модуля будет modec



# from folderb.modb import foo, bar # импорт из папки folderb файла modb функции foo


print(modules.foo)

modules.bar()

# print(foo) # если подклюены функция и перемен из др модуля
# bar()
