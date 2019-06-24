"""
Функции ​​сервера:​
- принимает ​с​ообщение ​к​лиента;
- формирует ​​ответ ​к​лиенту;
- отправляет ​​ответ ​к​лиенту;
- параметры ​к​омандной ​с​троки:
- -p ​​<port> ​-​ ​​TCP-порт ​​для ​​работы ​(​по ​у​молчанию ​​использует ​​порт ​​7777);
- -a ​​<addr> ​-​ ​I​P-адрес ​​для ​​прослушивания ​(​по ​у​молчанию ​с​лушает ​​все ​​доступные ​​адреса).
"""

import socket
from utils import get_message, send_message
import select
from descrptrs import Port
from metaclasses import ServerMaker
import sys
import logging
import argparse
from log.server_log_config import *
from log.decorators import Log


'''

def presence_response(presence_message):
    """
    Формирование ответа клиенту
    :param presence_message: Словарь presence запроса
    :return: Словарь ответа
    """
    # Проверки
    if 'action' in presence_message and \
        presence_message['action'] == 'presence' and \
        'time' in presence_message and isinstance(presence_message['time'], str):
        # Если проверка прошла, сервер отвечает ОК
        return {'response': 200}
    else:
        # Если проверка не прошла, сервер отвечает ошибкой
        return {'response': 900, 'error': 'Неправильный запрос'}


def read_requests(r_clients, all_clients):
    """
    Чтение сообщений, которые будут отправлять клиенты
    :param r_clients: клиенты, которые могут отправлять сообщения
    :param all_clients: все клиенты
    :return:
    """
    # Список входящих сообщений
    messages = []
    for sock in r_clients:
        try:
            # Получаем входящие сообщения
            message = get_message(sock)
            # Добаляем сообщения в список
            messages.append((message, sock))
        except:
            print('Клиент {} {} отключился'.format(sock.fileno(), sock.getpeername()))
            all_clients.remove(sock)
    for message in messages:
        print(message)
    # Возвращаем словарь сообщений
    return messages


def write_responses(messages):
    """
    Отправка сообщений тем клиентам, которые их ждут
    :param messages: список сообщений
    :param w_clients: клиенты, которые читают
    :param all_clients: все клиенты
    :return:
    """
    for message, sender in messages:
        if message['action'] == 'msg':
            # Получаем, кому отправить сообщение
            to = message['to']
            sock = names[to]
            msg = message['message']
            send_message(sock, message)


# Запуск сервера
if __name__ == '__main__':
    # Создается TCP-сокет сервера
    server = socket(AF_INET, SOCK_STREAM)
    port = 7777
    server.bind(('', 7777))  # Присваивает порт 7777
    server.listen(15)
    server.settimeout(0.2)
    clients = []  # Список объектов клиентских сокетов
    names = {}
    while True:
        try:
            client, address = server.accept()  # Проверка подключений
            presence = get_message(client)  # Получаем сообщение от клиента
            client_name = presence['user']['account_name']
            print(presence)
            response = presence_response(presence)  # Формируем ответ
            send_message(client, response)  # Отправляем ответ клиенту
        except OSError as e:
            pass  # timeout вышел
        else:
            print("Получен запрос на соединение от %s" % str(address))
            names[client_name] = client
            clients.append(client)
        finally:
            # Проверить наличие событий ввода-вывода
            wait = 0
            r = []
            w = []
            try:
                r, w, e = select.select(clients, clients, [], wait)
            except:
                pass

            requests = read_requests(r, clients)  # Получаем входящие сообщения
            write_responses(requests)  # Выполняем отправку входящих сообщений



-------------------------------------------------------------------------------------------------------------------
'''


# Инициализация логирования сервера.
logger = logging.getLogger('server')
log = Log(logger)

# Парсер аргументов командной строки.


def arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', default=7777, type=int, nargs='?')
    parser.add_argument('-a', default='', nargs='?')
    namespace = parser.parse_args(sys.argv[1:])
    listen_address = namespace.a
    listen_port = namespace.p
    return listen_address, listen_port


# Основной класс сервера
class Server(metaclass=ServerMaker):
    port = Port()

    def __init__(self, listen_address, listen_port):
        # Параментры подключения
        self.addr = listen_address
        self.port = listen_port

        # Список подключённых клиентов.
        self.clients = []

        # Список сообщений на отправку.
        self.messages = []

        # Словарь, содержащий сопоставленные имена и соответствующие им сокеты.
        self.names = dict()

    def init_socket(self):
        logger.info(
            f'Запущен сервер, порт для подключений: {self.port} , адрес с которого принимаются подключения:'
            f' {self.addr}.'
            f' Если адрес не указан, принимаются соединения с любых адресов.')
        # Готовим сокет
        transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        transport.bind((self.addr, self.port))
        transport.settimeout(0.5)

        # Начинаем слушать сокет.
        self.sock = transport
        self.sock.listen()

    def main_loop(self):
        # Инициализация Сокета
        self.init_socket()

        # Основной цикл программы сервера
        while True:
            # Ждём подключения, если таймаут вышел, ловим исключение.
            try:
                client, client_address = self.sock.accept()
            except OSError:
                pass
            else:
                logger.info(f'Установлено соедение с ПК {client_address}')
                self.clients.append(client)

            recv_data_lst = []
            send_data_lst = []
            err_lst = []
            # Проверяем на наличие ждущих клиентов
            try:
                if self.clients:
                    recv_data_lst, send_data_lst, err_lst = select.select(self.clients, self.clients, [], 0)
            except OSError:
                pass

            # принимаем сообщения и если ошибка, исключаем клиента.
            if recv_data_lst:
                for client_with_message in recv_data_lst:
                    try:
                        self.process_client_message(get_message(client_with_message), client_with_message)
                    except:
                        logger.info(f'Клиент {client_with_message.getpeername()} отключился от сервера')
                        self.clients.remove(client_with_message)

            # Если есть сообщения, обрабатываем каждое.
            for message in self.messages:
                try:
                    self.process_message(message, send_data_lst)
                except:
                    logger.info(f'Связь с клиентом с именем {message["to"]} была потеряна')
                    self.clients.remove(self.names[message['to']])
                    del self.names[message['to']]
            self.messages.clear()

    # Функция адресной отправки сообщения определённому клиенту. Принимает словарь сообщение, список зарегистрированых
    # пользователей и слушающие сокеты. Ничего не возвращает.
    def process_message(self, message, listen_socks):
        if message['to'] in self.names and self.names[message['to']] in listen_socks:
            send_message(self.names[message['to']], message)
            logger.info(f'Отправлено сообщение пользователю {message["to"]} от пользователя {message["from"]}.')
        elif message['to'] in self.names and self.names[message['to']] not in listen_socks:
            raise ConnectionError
        else:
            logger.error(
                f'Пользователь {message["to"]} не зарегистрирован на сервере, отправка сообщения невозможна.')

    # Обработчик сообщений от клиентов, принимает словарь - сообщение от клиента, проверяет корректность, отправляет
    #     словарь-ответ в случае необходимости.
    def process_client_message(self, message, client):
        logger.debug(f'Разбор сообщения от клиента : {message}')
        # Если это сообщение о присутствии, принимаем и отвечаем
        if 'action' in message and message['action'] == 'presence' and 'time' in message and 'user' in message:
            # Если такой пользователь ещё не зарегистрирован, регистрируем, иначе отправляем ответ и завершаем
            # соединение.
            if message['user']['account_name'] not in self.names.keys():
                self.names[message['user']['account_name']] = client
                send_message(client, {'response': 200})
            else:
                response = {
                            'response': 400,
                            'error': None
                }
                response['error'] = 'Имя пользователя уже занято'
                send_message(client, response)
                self.clients.remove(client)
                client.close()
            return
        # Если это сообщение, то добавляем его в очередь сообщений. Ответ не требуется.
        elif 'action' in message and message['action'] == 'message' and 'to' in message and 'time' in message \
                and 'from' in message and 'mess_text' in message:
            self.messages.append(message)
            return
        # Если клиент выходит
        elif 'action' in message and message['action'] == 'exit' and 'account_name' in message:
            self.clients.remove(self.names['account_name'])
            self.names['account_name'].close()
            del self.names['account_name']
            return
        # Иначе отдаём Bad request
        else:
            response = {
            'response': 400,
            'error': None
        }
            response['error'] = 'Запрос некорректен'
            send_message(client, response)
            return


def main():
    # Загрузка параметров командной строки, если нет параметров, то задаём значения по умоланию.
    listen_address, listen_port = arg_parser()

    # Создание экземпляра класса - сервера.
    server = Server(listen_address, listen_port)
    server.main_loop()


if __name__ == '__main__':
    main()



