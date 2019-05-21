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
import time
from socket import socket, AF_INET, SOCK_STREAM
from errors import UsernameToLongError, ResponseCodeLenError, MandatoryKeyError, ResponseCodeError
from jim.config import *
from jim.utils import send_message, get_message


def create_presence(account_name="Guest"):
    """
    Сформировать ​​presence-сообщение
    :param account_name: Имя пользователя
    :return: Словарь сообщения
    """
    if not isinstance(account_name, str):
        raise TypeError
    if len(account_name) > 25:
        raise UsernameToLongError(account_name)
    message = {
        ACTION: PRESENCE,
        TIME: time.time(),
        USER: {
            ACCOUNT_NAME: account_name
        }
    }
    return message


def translate_message(response):
    """
    Разбор сообщения
    :param response: Словарь ответа от сервера
    :return: корректный словарь ответа
    """
    if not isinstance(response, dict):
        raise TypeError
    if RESPONSE not in response:
        raise MandatoryKeyError(RESPONSE)
    code = response[RESPONSE]
    if len(str(code)) != 3:
        raise ResponseCodeLenError(code)
    if code not in RESPONSE_CODES:
        raise ResponseCodeError(code)
    return response


# ЗАПУСКАЕМ КЛИЕНТА!!!
if __name__ == '__main__':
    client = socket(AF_INET, SOCK_STREAM)  # Создать сокет TCP
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
    client.connect((addr, port))
    presence = create_presence()
    send_message(client, presence)
    response = get_message(client)
    response = translate_message(response)
    print(response)
