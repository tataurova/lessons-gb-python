# Написать функцию host_ping(), в которой с помощью утилиты ping будет проверяться доступность сетевых узлов.
# Аргументом функции является список, в котором каждый сетевой узел должен быть представлен именем хоста или ip-адресом.
# В функции необходимо перебирать ip-адреса и проверять их доступность с выводом соответствующего сообщения
# («Узел доступен», «Узел недоступен»). При этом ip-адрес сетевого узла должен создаваться с помощью функции
# ip_address().

from subprocess import Popen, PIPE

ip_list = ['64.233.164.94', '77.88.55.80', '217.69.139.202']


def host_ping(hosts_list):

    for host in hosts_list:
        args = ["ping", host]
        process = Popen(args, stdout=PIPE)
        data = process.communicate()
        for line in data:
            print(line.decode("cp866"))

            if ???:
                print(f'Узел {host} доступен')
            else:
                print(f'Узел {host} недоступен')

