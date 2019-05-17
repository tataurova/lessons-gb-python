import json
# изменение типа данных при преобразованиях из python в json

tuple_ex = (
    "action",
    "to",
    "from",
    "encoding",
    "message"
    )

print(type(tuple_ex))

with open('tuple_ex.json', 'w') as f_n:
    json.dump(tuple_ex, f_n)

obj = json.load(open('tuple_ex.json'))
print(type(obj))

# ошибка - ограничения по типам данных
dict_to_json = {('action', 'to'): 'msg', 'from': 'account_name'}

#with open('dict_to_json.json', 'w') as f_n:
    #json.dump(dict_to_json, f_n)

# игнорирование ограничения по типам
with open('dict_to_json.json', 'w') as f_n:
    json.dump(dict_to_json, f_n, skipkeys=True)

with open('dict_to_json.json') as f_n:
    f_n_content = f_n.read()
    obj = json.loads(f_n_content)

print(obj)

# конвертация ключей-чисел в строку
d = {5:300, 1:400}
d_to_json = json.dumps(d)
print(d_to_json)

