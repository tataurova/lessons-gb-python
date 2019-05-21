"""
Функции ​​сервера:​
- принимает ​с​ообщение ​к​лиента;
- формирует ​​ответ ​к​лиенту;
- отправляет ​​ответ ​к​лиенту;
- имеет ​​параметры ​к​омандной ​с​троки:
- -p ​​<port> ​-​ ​​TCP-порт ​​для ​​работы ​(​по ​у​молчанию ​​использует ​​порт ​​7777);
- -a ​​<addr> ​-​ ​I​P-адрес ​​для ​​прослушивания ​(​по ​у​молчанию ​с​лушает ​​все ​​доступные ​​адреса).
"""
import sys
# import json
from socket import socket, AF_INET, SOCK_STREAM
from jim.utils import get_message, send_message
# dict_to_bytes, bytes_to_dict,
from jim.config import *


def presence_response(presence_message):
    if ACTION in presence_message and \
                    presence_message[ACTION] == PRESENCE and \
                    TIME in presence_message and \
            isinstance(presence_message[TIME], float):
        return {RESPONSE: 200}
    else:
        return {RESPONSE: 400, ERROR: 'Не верный запрос'}


# ЗАПУСКАЕМ СЕРВЕР!!!
if __name__ == '__main__':
    server = socket(AF_INET, SOCK_STREAM)
    try:
        addr = sys.argv[0]
    except IndexError:
        addr = ''
    try:
        port = int(sys.argv[2])
    except IndexError:
        port = 7777
    except ValueError:
        print('Порт должен быть целым числом')
        sys.exit(0)
        server.bind((addr, port))  # Присваивает порт 8888
        server.listen(5)
        while True:
            client, addr = server.accept()
            presence = get_message(client)
            print(presence)
            response = presence_response(presence)
            send_message(client, response)
            client.close()

