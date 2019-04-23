# Создайте модуль main.py. Из модулей, реализованных в заданиях 1 и 2, сделайте импорт
# в main.py всех функций.
# Вызовите каждую функцию в main.py и проверьте, что все работает как надо.
# Примечание: Попробуйте импортировать как весь модуль целиком (например из задачи 1),
# так и отдельные функции из модуля.


# импорт всего модуля:
import case_dir
import case_list

case_dir.create_dir()

case_dir.remove_dir()

print(case_list.my_func(case_list.my_list))
print(case_list.my_func(case_list.my_list2))

# Импорт отдельных функций и переменных:

# from dir import test, create_dir, remove_dir

# create_dir()

# remove_dir()

# print(test)
