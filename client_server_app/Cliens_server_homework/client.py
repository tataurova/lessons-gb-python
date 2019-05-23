from socket import *
import time
import json


ACCOUNT_NAME = input('Введите Ваше имя: ')
MESSAGE = input('Введите сообщение, которое хотите отправить серверу: ')


# сообщение серверу
def create_presence():
    message = {
        'action': 'presence',
        'time': time.time(),
        'user': {
            'account name': ACCOUNT_NAME
        },
        'message': MESSAGE
    }
    return message


# разбор ответа от сервера
def translate_message(response):
    return response


def presence_response(presence_message):

    if 'action' in presence_message and \
                    presence_message['action'] == 'presence' and \
                    'time' in presence_message and \
            isinstance(presence_message['time'], float):
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


# Запуск клиента
if __name__ == '__main__':
    s = socket(AF_INET, SOCK_STREAM)
    s.connect(('localhost', 8888))
    presence = create_presence()
    send_message(s, presence)
    response = get_message(s)
    response = translate_message(response)
    print(response)



