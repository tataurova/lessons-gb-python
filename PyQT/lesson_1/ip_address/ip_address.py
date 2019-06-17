from ipaddress import ip_address

# создание IPv4-адреса
# протокол версии ip4 используется в старых виндовсах (до хр )
# а ip6 в висте и дальше, это для настройки сети и интернета
ipv4 = ip_address('192.168.0.1')
print(ipv4)

# набор специальных методов и атрибутов
# 127.0.0.1 — это адрес интернет-протокола loopback (IP),
# также называемый «localhost». Адрес используется для установления
# соединения с тем же компьютером, который используется конечным пользователем.
# is_loopback - возвращает True, если находит loopback-адрес
print(ipv4.is_loopback)
# is_multicast - возвращает True, если находит multicast-адрес
# групповой адрес адрес, определяющий группу станций локальной сети, одновременно получающих сообщение
print(ipv4.is_multicast)
# is_reserved - возвращает True, если находит IETF-зарезервированный адрес
# Инжене́рный сове́т Интерне́та (англ. Internet Engineering Task Force, IETF) —
# открытое международное сообщество проектировщиков, учёных, сетевых операторов и провайдеров,
# созданное IAB в 1986 году и занимающееся развитием протоколов и архитектуры Интернета.
print(ipv4.is_reserved)
# is_private - возвращает True, если адрес выделен для частных сетей
# Частный IP-адрес[1][2] (англ. private IP address), также называемый внутренним,
# внутрисетевым, локальным или «серым» — IP-адрес, принадлежащий к специальному диапазону,
# не используемому в сети Интернет. Такие адреса предназначены для применения в локальных сетях,
# распределение таких адресов никем не контролируется. В связи с дефицитом свободных IP-адресов,
# провайдеры всё чаще раздают своим абонентам именно внутрисетевые адреса,
# а не внешние, при этом один внешний айпи выдаётся нескольким клиентам.
print(ipv4.is_private)

# операции с объектами-адресами
ip1 = ip_address('192.168.1.0')
ip2 = ip_address('192.168.1.255')
# сравнение ip-адресов
if ip2 > ip1:
    print(True)
# конвертация ip-адреса в строку
print(str(ip1))
# конвертация ip-адреса в целое число
print(int(ip1))
# изменение идентификатора узла в сети
print(ip1 + 5)
print(ip1 - 5)


