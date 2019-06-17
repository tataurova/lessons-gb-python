from socket import *
from utils import get_message, presence_response, send_message


# Запуск сервера
if __name__ == '__main__':
    server = socket(AF_INET, SOCK_STREAM)
    server.bind(('', 7777))
    server.listen(5)
    while True:
        client, address = server.accept()
        presence = get_message(client)
        print(presence)
        response = presence_response(presence)
        send_message(client, response)
        client.close()
