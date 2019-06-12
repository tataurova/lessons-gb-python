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
import logging
import select

from socket import socket, AF_INET, SOCK_STREAM
from jim.utils import get_message, send_message
from jim.config import *


import log.server_log_config
from log.decorators import Log
# Получаем серверный логгер по имени, он уже объявлен в server_log_config и настроен
logger = logging.getLogger('server')
log = Log(logger)

def read_requests(r_clients, all_clients):
    """
    Чтение сообщений, которые будут посылать клиенты
    :param r_clients: клиенты которые могут отправлять сообщения
    :param all_clients: все клиенты
    :return:
    """
    # Список входящих сообщений
    messages = []

    for sock in r_clients:
        try:
            # Получаем входящие сообщения
            message = get_message(sock)
            print(message)
            # Добавляем их в список
            # В идеале нам нужно сделать еще проверку, что сообщение нужного формата прежде чем его пересылать!
            # Пока оставим как есть, этим займемся позже
            messages.append((message, sock))
        except:
            print('Клиент {} {} отключился'.format(sock.fileno(), sock.getpeername()))
            all_clients.remove(sock)

    # Возвращаем словарь сообщений
    return messages

#all

def write_responses(messages):
    """
    Отправка сообщений тем клиентам, которые их ждут
    :param messages: список сообщений
    :param w_clients: клиенты которые читают
    :param all_clients: все клиенты
    :return:
    """

    for message, sender in messages:
        if message['action'] == MSG:
                # получаем кому отправить сообщение
                to = message['to']
                sock = names[to]
                msg = message['message']
                send_message(sock, message)
@log
def presence_response(presence_message):
    """
    Формирование ответа клиенту
    :param presence_message: Словарь presence запроса
    :return: Словарь ответа
    """
    # Делаем проверки
    if ACTION in presence_message and \
                    presence_message[ACTION] == PRESENCE and \
                    TIME in presence_message and \
            isinstance(presence_message[TIME], float):
        # Если всё хорошо шлем ОК
        return {RESPONSE: 200}
    else:
        # Шлем код ошибки
        return {RESPONSE: 400, ERROR: 'Не верный запрос'}


# ЗАПУСКАЕМ СЕРВЕР!!!
if __name__ == '__main__':
    # Создается TCP-сокет сервера
    server = socket(AF_INET, SOCK_STREAM)
    # Получаем аргументы скрипта
    # ------------ip-адрес-----------#
    # если ip-адрес указан в параметрах
    try:
        addr = sys.argv[1]
    # если ip-адрес не указан в параметрах
    except IndexError:
        addr = ''
    # --------------порт-------------#
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

    server.bind((addr, port))  # Присваивает порт 8888
    server.listen(15)
     # Не забываем поставить таймаут иначен ничего не случиться
    server.settimeout(0.2)
    # список объектов клиентских сокетов
    clients = []
    names = {}
    while True:
        try:
            conn, addr = server.accept()  # Проверка подключений
            # получаем сообщение от клиента
            presence = get_message(conn)

            #print(presence)
            client_name = presence['user']['account_name']
            # формируем ответ
            response = presence_response(presence)
            # отправляем ответ клиенту
            send_message(conn, response)
        except OSError as e:
            pass  # timeout вышел
        else:
            print("Получен запрос на соединение от %s" % str(addr))
            names[client_name] = conn

            clients.append(conn)
        finally:
            # Проверить наличие событий ввода-вывода
            wait = 0
            r = []
            w = []
            try:
                r, w, e = select.select(clients, clients, [], wait)
            except:
                pass  # Ничего не делать, если какой-то клиент отключился

            requests = read_requests(r, clients)  # Получаем входные сообщения
            write_responses(requests)  # Выполним отправку входящих сообщений



