# использование метода load для чтения json-файла
import json

with open('mes_example_read.json') as f_n:
    obj = json.load(f_n)
    print(type(obj))

#for section, commands in obj.items():
    #print(section)
    #print(commands)



# использование метода loads для чтения json-строки

with open('mes_example_read.json') as f_n:
    f_n_content = f_n.read()
    print(type(f_n_content))
    obj = json.loads(f_n_content)
    print(type(obj))

#print(obj)

#for section, commands in obj.items():
    #print(section)
    #print(commands)



