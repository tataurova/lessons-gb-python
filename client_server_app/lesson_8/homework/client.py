"""
Функции ​к​лиента:​
- сформировать ​​presence-сообщение;
- отправить ​с​ообщение ​с​ерверу;
- получить ​​ответ ​с​ервера;
- разобрать ​с​ообщение ​с​ервера;
- параметры ​к​омандной ​с​троки ​с​крипта ​c​lient.py ​​<addr> ​[​<port>]:
- addr ​-​ ​i​p-адрес ​с​ервера;
- port ​-​ ​t​cp-порт ​​на ​с​ервере, ​​по ​у​молчанию ​​7777.
"""

import sys
import logging
import time
import threading
from socket import socket, AF_INET, SOCK_STREAM
from utils import send_message, get_message, translate_message
from log.client_log_config import *
from log.decorators import Log

# Получаем по имени клиентский логгер, он уже нестроен в client_log_config
logger = logging.getLogger('client')
log = Log(logger)


# функция формирования сообщения
@log
def create_presence(account_name="Guest"):
    """
        Сформировать ​​presence-сообщение
        :param account_name: Имя пользователя
        :return: Словарь сообщения
        """
    # формируем словарь сообщения
    message = {
        'action': 'presence',
        'time': time.strftime("%d-%m-%Y %H:%M:%S", time.localtime()),
        'user': {
            'account_name': account_name
        }
    }
    # возвращаем сообщение в виде словаря
    return message


def read_messages(client, account_name):
    """
    Клиент читает входящие сообщения в бесконечном цикле
    :param client: сокет клиента
    """
    while True:
        # читаем сообщение
        message = get_message(client)
        print(message['message'])


@log
def create_message(message_to, text, account_name='Guest'):
    return {'action': 'msg', 'time': time.time(), 'to': message_to, 'from': account_name, 'message': text}


# Запуск клиента
if __name__ == '__main__':
    # Создается TCP-сокет клиента
    client = socket(AF_INET, SOCK_STREAM)
    # Если ip-адрес указан в параметрах -p <addr>
    try:
        addr = sys.argv[1]
    # если ip-адрес не указан в параметрах
    except IndexError:
        addr = 'localhost'
    # если порт указан в параметрах
    try:
        port = int(sys.argv[2])
    # если порт не указан в параметрах
    except IndexError:
        port = 7777
    # если порт - не целое число
    except ValueError:
        print('Порт должен быть целым числом')
        sys.exit(0)
    try:
        mode = sys.argv[3]
    except IndexError:
        mode = 'r'
    try:
        account_name = sys.argv[4]
        print(account_name)
    except IndexError:
        print('Укажите получателя')
    # Соединиться с сервером
    client.connect(('localhost', 7777))
    res = 'Подключение к серверу от {} from {}'.format(client.getpeername(), client.getsockname())
    logger.info('{}'.format(res))
    # Сформировать сообщение серверу. account_name=Console0
    presence = create_presence(account_name)
    # Отправить сообщение серверу
    send_message(client, presence)
    # Разобрать ответ сервера
    response = get_message(client)
    response = translate_message(response)
    print(response)
    if response['response'] == 200:
        # Определить поток для запуска функции read_message
        t = threading.Thread(target=read_messages, args=(client, account_name))
        # Запустить поток
        t.start()

        while True:
            message_str = input(':) >')
            if message_str.startswith('message'):
                params = message_str.split()
                try:
                    to = params[1]
                    text = ' '.join(params[2:])
                except IndexError:
                    print('Не задан получатель или текст сообщения')
                else:
                    message = create_message(to, text, account_name)
                    send_message(client, message)

            elif message_str == 'help':
                print('message <получатель> <текст> - отправить сообщение')
            elif message_str == 'exit':
                break
            else:
                print('Неверная команда, для справки введите help')

        client.disconnect()
