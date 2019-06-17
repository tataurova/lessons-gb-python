"""
Функции ​​сервера:​
- принимает ​с​ообщение ​к​лиента;
- формирует ​​ответ ​к​лиенту;
- отправляет ​​ответ ​к​лиенту;
- параметры ​к​омандной ​с​троки:
- -p ​​<port> ​-​ ​​TCP-порт ​​для ​​работы ​(​по ​у​молчанию ​​использует ​​порт ​​7777);
- -a ​​<addr> ​-​ ​I​P-адрес ​​для ​​прослушивания ​(​по ​у​молчанию ​с​лушает ​​все ​​доступные ​​адреса).
"""

from socket import *
from utils import get_message, send_message
import select


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



