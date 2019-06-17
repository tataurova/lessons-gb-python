# операции с объектом-сетью
from ipaddress import ip_network

# атрибут получения широковещательного адреса для сети - broadcast_address
# пакет посланный по этому адресу получат все машины в этой сети
subnet = ip_network('80.0.1.0/28')
ba = subnet.broadcast_address
print(ba)

# просмотр всех хостов для объекта-сети - метод hosts()
print(list(subnet.hosts()))

# разбиение сети на подсети (по умолчанию на 2) - метод subnets()
print(list(subnet.subnets()))

# обращение к любому адресу в сети
# объект-сеть в Python представляется в виде списка ip-адресов, к каждому из которых
# можно обратиться по индексу
print(subnet[1])