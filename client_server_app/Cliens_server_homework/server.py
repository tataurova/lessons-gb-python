from socket import *
from utils_server import get_message, presence_response, send_message
from log.server_log_config import *
import select
import logging

logger = logging.getLogger('server')


def read_requests(r_clients, all_clients):
    messages = []
    for sock in r_clients:
        try:
            message = get_message(sock)
            messages.append(message)
        except:
            print('Клиент {} {} отключился'.format(sock.fileno(), sock.getpeername()))
            all_clients.remove(sock)
    return messages


def write_responses(messages, w_clients, all_clients):
    for sock in w_clients:
        for message in messages:
            try:
                send_message(sock, message)
            except:
                print('Клиент {} {} отключился'.format(sock.fileno(), sock.getpeername()))
                sock.close()
                all_clients.remove(sock)

# Запуск сервера


if __name__ == '__main__':

    server = socket(AF_INET, SOCK_STREAM)
    try:
        port = 7777
        server.bind(('', port))
    except Exception:
        port = 7778
        server.bind(('', port))
        res = 'Port 7777 unreachable. Port used 7778'
        logger.warning('{} {} - {}'.format(res, server.bind.__name__, __name__))
    server.listen(15)
    server.settimeout(0.2)
    clients = []
    while True:
        try:
            res = 'Waiting for client'
            logger.info('{}'.format(res))
            client, address = server.accept()
            res = 'Client connected from address {}'.format(address)
            logger.info('{}'.format(res))
            presence = get_message(client)
            print(presence)
            response = presence_response(presence)
            send_message(client, response)
            client.close()
        except OSError as e:
            pass  # timeout вышел
        else:
            print("Получен запрос на соединение от %s" % str(address))
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

        requests = read_requests(r, clients)  # Получаем входные сообщения
        write_responses(requests, w, clients)  # Выполним отправку входящих сообщений



