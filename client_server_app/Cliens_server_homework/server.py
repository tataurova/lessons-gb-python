from socket import *
from utils import *
from config import *
import json
import sys

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 8888))
s.listen(5)


def presence_response(presence_message):

    if 'action' in presence_message and \
                    presence_message['action'] == 'presence' and \
                    'time' in presence_message and \
            isinstance(presence_message['time'] and 'message' in presence_message, float):
        return {'response': 200}
    else:
        return {'response': 400, 'error': 'Не верный запрос'}


def dict_to_bytes(message_dict):
    if isinstance(message_dict, dict):
        jmessage = json.dumps(message_dict)
        bmessage = jmessage.encode('utf-8')
        return bmessage
    else:
        raise TypeError


def bytes_to_dict(message_bytes):
    if isinstance(message_bytes, bytes):
        jmessage = message_bytes.decode('utf-8')
        message = json.loads(jmessage)
        if isinstance(message, dict):
            return message
        else:
            raise TypeError
    else:
        raise TypeError


def send_message(sock, message):
    bprescence = dict_to_bytes(message)
    sock.send(bprescence)


def get_message(sock):
    bresponse = sock.recv(1024)
    response = bytes_to_dict(bresponse)
    return response


# Запуск сервера
if __name__ == '__main__':
    while True:
        client, addr = s.accept()
        presence = get_message(client)
        print(presence)
        response = presence_response(presence)
        send_message(client, response)
        client.close()
