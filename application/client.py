from socket import *
from utils import send_message, get_message, translate_message
import time

ACCOUNT_NAME = input('Введите Ваше имя: ')
MESSAGE = input('Введите сообщение, которое хотите отправить серверу: ')


# сообщение серверу
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


# Запуск клиента
if __name__ == '__main__':
    client = socket(AF_INET, SOCK_STREAM)
    client.connect(('localhost', 7777))
    presence = create_presence()
    send_message(client, presence)
    response = get_message(client)
    response = translate_message(response)
    print(response)
