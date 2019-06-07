from socket import *
from utils_client import send_message, get_message, translate_message
import time
from log.client_log_config import *
from utils_client import log
import sys
import logging

logger = logging.getLogger('client')


# input('Введите Ваше имя: ')
#MESSAGE = input('Введите сообщение, которое хотите отправить серверу: ')

ACCOUNT_NAME = 'test'
#MESSAGE = 'test message'


# сообщение серверу
@log
def create_presence(account_name="Guest"):
    message = {
        'action': 'presence',
        'time': time.strftime("%d-%m-%Y %H:%M:%S", time.localtime()),
        'user': {
            'account_name': account_name
        }
       # 'message': MESSAGE
    }
    return message


def read_messages(client):
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
    while True:
        # Вводим сообщение с клавиатуры
        text = input(':)>')
        # Создаем jim сообщение
        message = create_message('Всем в чате: ', text)
        # отправляем на сервер
        send_message(client, message)


# Запуск клиента
if __name__ == '__main__':
    client = socket(AF_INET, SOCK_STREAM)
    try:
        addr = sys.argv[1]
    except IndexError:
        addr = 'localhost'
    try:
        port = int(sys.argv[2])
    except IndexError:
        port = 7777
    except ValueError:
        print('Порт должен быть целым числом')
        sys.exit(0)
    try:
        mode = sys.argv[3]
    except IndexError:
        mode = 'r'
    '''
    try:
        mode = sys.argv[3]
    except IndexError:
        mode = 'r'
        print(mode)
       
    try:
        client.connect(('localhost', 7777))
    except Exception:
        client = socket(AF_INET, SOCK_STREAM)
        client.connect(('localhost', 7778))
        mes = 'Port 7777 unreachable. Port used 7778'
        logger.warning('{} {} - {}'.format(mes, client.bind.__name__, __name__))
        print(mes)
    res = 'Connected to server {} from {}'.format(client.getpeername(), client.getsockname())
    logger.info('{}'.format(res))
'''
    client.connect(('localhost', 7777))
    presence = create_presence()
    send_message(client, presence)
    response = get_message(client)
    response = translate_message(response)
    print(response)
    print(response['response'])
    if response['response'] == 200:
        print(mode)
        print('что не так?')
        # в зависимости от режима мы будем или слушать или отправлять сообщения
        if mode == 'r':
            print('режим r')
            read_messages(client)
        elif mode == 'w':
            print('режим w')
            write_messages(client)
        else:
            raise Exception('Не верный режим чтения/записи')
