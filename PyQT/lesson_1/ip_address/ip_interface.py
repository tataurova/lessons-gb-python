# создание объектов IPv4Interface или IPv6Interface
from ipaddress import ip_interface, ip_network

ipv4_int = ip_interface('10.0.1.1/24')

# получение адреса, маски, сети интерфейса
print(ipv4_int.ip)
print(ipv4_int.netmask)
print(ipv4_int.network)

# проверка типа адреса
ip_1 = '10.0.1.1/24'
ip_2 = '10.0.1.0/24'

def ip_network_check(ip_addr):
    try:
        ip_network(ip_addr)
        return True
    except ValueError:
        return False
print(ip_network_check(ip_1))
print(ip_network_check(ip_2))
