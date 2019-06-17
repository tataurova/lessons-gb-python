# Написать функцию host_ping(), в которой с помощью утилиты ping будет проверяться доступность сетевых узлов.
# Аргументом функции является список, в котором каждый сетевой узел должен быть представлен именем хоста или ip-адресом.
# В функции необходимо перебирать ip-адреса и проверять их доступность с выводом соответствующего сообщения
# («Узел доступен», «Узел недоступен»). При этом ip-адрес сетевого узла должен создаваться с помощью функции
# ip_address().

import os
from ipaddress import ip_address


google = ip_address('64.233.164.94')
yandex = ip_address('77.88.55.80')
mail = ip_address('217.69.139.202')
ipv4 = ip_address('192.168.9.3')

ip_list = [google, yandex, mail, ipv4]


def host_ping(hosts_list):
    for host in hosts_list:
        response = os.system("ping -c 1 -t 2 " + str(host) + " > /dev/null")
        if response == 0:
            print(f'Узел {host} доступен')
        else:
            print(f'Узел {host} недоступен!')


host_ping(ip_list)
