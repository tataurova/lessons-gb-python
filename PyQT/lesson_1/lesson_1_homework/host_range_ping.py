# Написать функцию host_range_ping() для перебора ip-адресов из заданного диапазона. Меняться должен только последний
# октет каждого адреса. По результатам проверки должно выводиться соответствующее сообщение.
import os
from ipaddress import ip_network

subnet = ip_network('192.168.2.0/28')


def host_range_ping(network):
    address = list(network.hosts())
    for host in address:
        response = os.system("ping -c 1 -t 2 " + str(host) + " > /dev/null")
        if response == 0:
            print(f'Узел {host} доступен')
        else:
            print(f'Узел {host} недоступен!')


host_range_ping(subnet)
