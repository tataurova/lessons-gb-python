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

import logging
import log.client_log_config
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
    # Если имя не строка
    if not isinstance(account_name, str):
        # Генерируем ошибку передан неверный тип
        raise TypeError
    # Если длина имени пользователя больше 25 символов
    if len(account_name) > 25:
        # генерируем нашу ошибку имя пользователя слишком длинное
        raise UsernameToLongError(account_name)
    # если все хорошо, то
    # формируем словарь сообщения
    message = {
        ACTION: PRESENCE,
        TIME: time.time(),
        USER: {
            ACCOUNT_NAME: account_name
        }
    }

    # возвращаем сообщение в виде словаря
    return message

# функция разбора ответа сервера
@log
def translate_message(response):
    """
    Разбор сообщения
    :param response: Словарь ответа от сервера
    :return: корректный словарь ответа
    """
    # Передали не словарь
    if not isinstance(response, dict):
        raise TypeError
    # Нету ключа response
    if RESPONSE not in response:
        # Ошибка нужен обязательный ключ
        raise MandatoryKeyError(RESPONSE)
    # если все хорошо, то
    # получаем код ответа
    code = response[RESPONSE]
    # длина кода не 3 символа
    if len(str(code)) != 3:
        # Ошибка неверная длина кода ошибки
        raise ResponseCodeLenError(code)
    # неправильные коды символов
    if code not in RESPONSE_CODES:
        # ошибка неверный код ответа
        raise ResponseCodeError(code)

    # возвращаем ответ
    return response


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
        print(message[MESSAGE])

def create_message(message_to, text, account_name='Guest'):
    return {ACTION: MSG, TIME: time.time(), TO: message_to, FROM: account_name, MESSAGE: text}

def write_messages(client):
    """Клиент пишет сообщение в бесконечном цикле"""
    while True:
        # Вводим сообщение с клавиатуры
        text = input(':)>')
        # Создаем jim сообщение
        message = create_message('#all', text)
        #print(client)
        # отправляем на сервер
        send_message(client, message)

# ЗАПУСКАЕМ КЛИЕНТА!!!
if __name__ == '__main__':
    # Создать TCP-сокет клиента
    client = socket(AF_INET, SOCK_STREAM)  # Создать сокет TCP
    # Пытаемся получить параметры скрипта
    # Получаем аргументы скрипта
    #------------ip-адрес-----------#
    # если ip-адрес указан в параметрах -p <addr>
    try:
        addr = sys.argv[1]
    # если ip-адрес не указан в параметрах
    except IndexError:
        addr = 'localhost'
    #--------------порт-------------#
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
    # ДАННЫЕ ПОЛУЧИЛИ -> СОЕДИНЯЕМСЯ С СЕРВЕРОМ
    # Соединиться с сервером
    client.connect((addr, port))
    # Сформировать сообщение серверу
    presence = create_presence()
    # Отправить сообщение серверу
    send_message(client, presence)
    # Получить ответ сервера
    response = get_message(client)
    # Разобрать ответ сервера
    response = translate_message(response)
    #print(response)
    if response['response'] == OK:
        # в зависимости от режима мы будем или слушать или отправлять сообщения
        if mode == 'r':
            read_messages(client)
        elif mode == 'w':
            write_messages(client)
        else:
            raise Exception('Не верный режим чтения/записи')
