from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 8007))
s.listen(5)

while True:
    client, addr = s.accept()
    data = client.recv(4096)
    print('Сообщение: ', data.decode('utf-8'), ', было отправлено клиентом: ', addr)
    msg = 'Привет, клиент'
    client.send(msg.encode('utf-8'))
    client.close()