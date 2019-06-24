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


import logging
from socket import socket, AF_INET, SOCK_STREAM
from utils import send_message, get_message, translate_message
from log.client_log_config import *
from log.decorators import Log

# Получаем по имени клиентский логгер, он уже нестроен в client_log_config
logger = logging.getLogger('client')
log = Log(logger)

'''
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
-------------------------------------------------------------------------

'''

import sys
import json
import socket
import time
import dis
import argparse
import logging
import threading
from utils import *
from metaclasses import ClientMaker
from errors import IncorrectDataRecivedError, ServerError, ReqFieldMissingError

# Инициализация клиентского логера
logger = logging.getLogger('client')


# Класс формировки и отправки сообщений на сервер и взаимодействия с пользователем.
class ClientSender(threading.Thread, metaclass=ClientMaker):
    def __init__(self, account_name, sock):
        self.account_name = account_name
        self.sock = sock
        super().__init__()

    # Функция создаёт словарь с сообщением о выходе.
    def create_exit_message(self):
        return {
            'action': 'exit',
            'time': time.strftime("%d-%m-%Y %H:%M:%S", time.localtime()),
            'account_name': self.account_name
        }

    # Функция запрашивает, кому отправить сообщение и само сообщение, и отправляет полученные данные на сервер.
    def create_message(self):
        to = input('Введите получателя сообщения: ')
        message = input('Введите сообщение для отправки: ')
        message_dict = {
            'action': 'message',
            'from': self.account_name,
            'to': to,
            'time': time.strftime("%d-%m-%Y %H:%M:%S", time.localtime()),
            'mess_text': message
        }
        logger.debug(f'Сформирован словарь сообщения: {message_dict}')
        try:
            send_message(self.sock, message_dict)
            logger.info(f'Отправлено сообщение для пользователя {to}')
        except:
            logger.critical('Потеряно соединение с сервером.')
            exit(1)

    # Функция взаимодействия с пользователем, запрашивает команды, отправляет сообщения
    def run(self):
        self.print_help()
        while True:
            command = input('Введите команду: ')
            if command == 'message':
                self.create_message()
            elif command == 'help':
                self.print_help()
            elif command == 'exit':
                try:
                    send_message(self.sock, self.create_exit_message())
                except:
                    pass
                print('Завершение соединения.')
                logger.info('Завершение работы по команде пользователя.')
                # Задержка неоходима, чтобы успело уйти сообщение о выходе
                time.sleep(0.5)
                break
            else:
                print('Команда не распознана, попробуйте снова. help - вывести поддерживаемые команды.')

    # Функция, выводящяя справку по использованию.
    def print_help(self):
        print('Поддерживаемые команды:')
        print('message - отправить сообщение. Кому и текст будет запрошены отдельно.')
        print('help - вывести подсказки по командам')
        print('exit - выход из программы')


# Класс-приёмник сообщений с сервера. Принимает сообщения, выводит в консоль.
class ClientReader(threading.Thread, metaclass=ClientMaker):
    def __init__(self, account_name, sock):
        self.account_name = account_name
        self.sock = sock
        super().__init__()

    # Основной цикл приёмника сообщений, принимает сообщения, выводит в консоль. Завершается при потере соединения.
    def run(self):
        while True:
            try:
                message = get_message(self.sock)
                if 'action' in message and message['action'] == 'message' and 'from' in message and 'to' in message \
                        and 'mess_text' in message and message['to'] == self.account_name:
                    print(f'\nПолучено сообщение от пользователя {message["from"]}:\n{message["mess_text"]}')
                    logger.info(f'Получено сообщение от пользователя {message["from"]}:\n{message["mess_text"]}')
                else:
                    logger.error(f'Получено некорректное сообщение с сервера: {message}')
            except IncorrectDataRecivedError:
                logger.error(f'Не удалось декодировать полученное сообщение.')
            except (OSError, ConnectionError, ConnectionAbortedError, ConnectionResetError, json.JSONDecodeError):
                logger.critical(f'Потеряно соединение с сервером.')
                break


# Функция генерирует запрос о присутствии клиента
@log
def create_presence(account_name):
    out = {
        'action': 'presence',
        'time': time.strftime("%d-%m-%Y %H:%M:%S", time.localtime()),
        'user': {
            'account_name': account_name
        }
    }
    logger.debug(f'Сформировано {out} сообщение для пользователя {account_name}')
    return out


# Функция разбирает ответ сервера на сообщение о присутствии, возращает 200, если все ОК или генерирует исключение при
# ошибке.
@log
def process_response_ans(message):
    logger.debug(f'Разбор приветственного сообщения от сервера: {message}')
    if 'response' in message:
        if message['response'] == 200:
            return '200 : OK'
        elif message['response'] == 400:
            raise ServerError(f'400 : {message["error"]}')
    raise ReqFieldMissingError('response')


# Парсер аргументов командной строки
@log
def arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('addr', default='localhost', nargs='?')
    parser.add_argument('port', default=7777, type=int, nargs='?')
    parser.add_argument('-n', '--name', default=None, nargs='?')
    namespace = parser.parse_args(sys.argv[1:])
    server_address = namespace.addr
    server_port = namespace.port
    client_name = namespace.name

    # проверим подходящий номер порта
    if not 1023 < server_port < 65536:
        logger.critical(
            f'Попытка запуска клиента с неподходящим номером порта: {server_port}. Допустимы адреса с 1024 до 65535. Клиент завершается.')
        exit(1)

    return server_address, server_port, client_name


def main():
    # Сообщаем о запуске
    print('Консольный мессенджер. Клиентский модуль.')

    # Загружаем параметы коммандной строки
    server_address, server_port, client_name = arg_parser()

    # Если имя пользователя не было задано, необходимо запросить пользователя.
    if not client_name:
        client_name = input('Введите имя пользователя: ')
    else:
        print(f'Клиентский модуль запущен с именем: {client_name}')

    logger.info(
        f'Запущен клиент с парамертами: адрес сервера: {server_address} , порт: {server_port}, имя пользователя: {client_name}')

    # Инициализация сокета и сообщение серверу о нашем появлении
    try:
        transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        transport.connect((server_address, server_port))
        send_message(transport, create_presence(client_name))
        answer = process_response_ans(get_message(transport))
        logger.info(f'Установлено соединение с сервером. Ответ сервера: {answer}')
        print(f'Установлено соединение с сервером.')
    except json.JSONDecodeError:
        logger.error('Не удалось декодировать полученную Json строку.')
        exit(1)
    except ServerError as error:
        logger.error(f'При установке соединения сервер вернул ошибку: {error.text}')
        exit(1)
    except ReqFieldMissingError as missing_error:
        logger.error(f'В ответе сервера отсутствует необходимое поле {missing_error.missing_field}')
        exit(1)
    except (ConnectionRefusedError, ConnectionError):
        logger.critical(
            f'Не удалось подключиться к серверу {server_address}:{server_port}, конечный компьютер отверг запрос на подключение.')
        exit(1)
    else:
        # Если соединение с сервером установлено корректно, запускаем клиенский процесс приёма сообщений
        module_reciever = ClientReader(client_name, transport)
        module_reciever.daemon = True
        module_reciever.start()

        # затем запускаем отправку сообщений и взаимодействие с пользователем.
        module_sender = ClientSender(client_name, transport)
        module_sender.daemon = True
        module_sender.start()
        logger.debug('Запущены процессы')

        # Watchdog основной цикл, если один из потоков завершён, то значит или потеряно соединение или пользователь
        # ввёл exit. Поскольку все события обработываются в потоках, достаточно просто завершить цикл.
        while True:
            time.sleep(1)
            if module_reciever.is_alive() and module_sender.is_alive():
                continue
            break


if __name__ == '__main__':
    main()
