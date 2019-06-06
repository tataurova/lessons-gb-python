from socket import *
from utils_client import send_message, get_message, translate_message
import time
from log.client_log_config import *
from utils_client import log
import sys
import logging

logger = logging.getLogger('client')


if __name__ == '__main__':
    ACCOUNT_NAME = input('Введите Ваше имя: ')
    MESSAGE = input('Введите сообщение, которое хотите отправить серверу: ')
else:
    ACCOUNT_NAME = 'test'
    MESSAGE = 'test message'


# сообщение серверу
@log
def create_presence():
    message = {
        'action': 'presence',
        'time': time.strftime("%d-%m-%Y %H:%M:%S", time.localtime()),
        'user': {
            'account name': ACCOUNT_NAME
        },
        'message': MESSAGE
    }
    return message


def read_messages(client):
    """
    Клиент читает входящие сообщения в бесконечном цикле
    :param client: сокет клиента
    """
    while True:
        # читаем сообщение
        print('Читаю')
        message = get_message(client)
        print(message)
        # там должно быть сообщение всем
        print(message['message'])


def create_message(message_to, text, account_name='Guest'):
    return {'action': 'msg', 'time': time.time(), 'to': message_to, 'from': account_name, 'message': text}


def write_messages(client):
    """Клиент пишет сообщение в бесконечном цикле"""
    while True:
        # Вводим сообщение с клавиатуры
        text = input(':)>')
        # Создаем jim сообщение
        message = create_message('#all', text)
        # отправляем на сервер
        send_message(client, message)


# Запуск клиента
if __name__ == '__main__':
    client = socket(AF_INET, SOCK_STREAM)
    try:
        mode = sys.argv[3]
    except IndexError:
        mode = 'r'
    try:
        client.connect(('localhost', 7777))
    except Exception:
        client = socket(AF_INET, SOCK_STREAM)
        client.connect(('localhost', 7778))
        mes = 'Port 7777 unreachable. Port used 7778'
        logger.warning('{} {} - {}'.format(mes, client.bind.__name__, __name__))
    res = 'Connected to server {} from {}'.format(client.getpeername(), client.getsockname())
    logger.info('{}'.format(res))
    presence = create_presence()
    send_message(client, presence)
    response = get_message(client)
    response = translate_message(response)
    print(response)
    if response['response'] == 'ok':
        # в зависимости от режима мы будем или слушать или отправлять сообщения
        if mode == 'r':
            read_messages(client)
        elif mode == 'w':
            write_messages(client)
        else:
            raise Exception('Не верный режим чтения/записи')
