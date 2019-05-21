# Программа клиента, передающего серверу сообщения при каждом запросе на соединение
from socket import *

s = socket(AF_INET, SOCK_DGRAM)
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
while True:
    mes = 'Запрос на соединение!'
    s.sendto(mes.encode('utf-8'),('localhost',8888))
