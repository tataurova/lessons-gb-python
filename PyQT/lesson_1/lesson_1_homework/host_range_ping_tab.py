# Написать функцию host_range_ping_tab(), возможности которой основаны на функции из примера 2. Но в данном случае
# результат должен быть итоговым по всем ip-адресам, представленным в табличном формате (использовать модуль tabulate).
# Таблица должна состоять из двух колонок и выглядеть примерно так:
import os
from tabulate import tabulate
from ipaddress import ip_network

subnet = ip_network('192.168.2.0/28')
list_reach = []
list_unreach = []
tab_list = [list_reach, list_unreach]


def host_range_ping_tab(network):
    address = list(network.hosts())
    for host in address:
        response = os.system("ping -c 1 -t 2 " + str(host) + " > /dev/null")
        if response == 0:
            list_reach.append(host)
            print(f'Узел {host} доступен')
        else:
            list_unreach.append(host)
            print(f'Узел {host} недоступен!')


host_range_ping_tab(subnet)
print('**********************************')
print(tabulate({"Reachable": list_reach, "Unreachable": list_unreach}, headers="keys"))


