import yaml

# считывавем данные
with open('data_write.yaml') as f_n:
    f_n_content = yaml.load(f_n, Loader=yaml.FullLoader)
print(f_n_content)

# изменяем формат записи
action_list = ['msg_1',
          'msg_2',
          'msg_3']

to_list = ['account_1',
      'account_2',
      'account_3']

data_to_yaml = {'action':action_list, 'to':to_list}

with open('data_write.yaml', 'w') as f_n:
    yaml.dump(data_to_yaml, f_n, default_flow_style=False)

with open('data_write.yaml') as f_n:
    print(f_n.read())
