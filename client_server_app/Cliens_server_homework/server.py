from socket import *
from utils import get_message, send_message
import select


def presence_response(presence_message):

    if 'action' in presence_message and \
        presence_message['action'] == 'presence' and \
        'time' in presence_message and isinstance(presence_message['time'], str):

        return {'response': 200}
    else:
        return {'response': 900, 'error': 'Неправильный запрос'}


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
    port = 7777
    server.bind(('', 7777))
    server.listen(15)
    server.settimeout(0.2)
    clients = []
    while True:
        try:
            client, address = server.accept()
            presence = get_message(client)
            print(presence)
            response = presence_response(presence)
            send_message(client, response)
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



