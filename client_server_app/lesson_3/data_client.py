from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 8007))
msg = 'Привет, сервер'
s.send(msg.encode('utf-8'))
data = s.recv(4096)
print('Сообщение от сервера: ', data.decode('utf-8'), ', длиной ', len(data), ' байт')
s.close()