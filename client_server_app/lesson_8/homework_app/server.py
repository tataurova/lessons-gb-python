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
import json
from socket import socket, AF_INET, SOCK_STREAM
from jim.utils import get_message, send_message
#dict_to_bytes, bytes_to_dict,
from jim.config import *

# функция форсмрования ответа
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
    server.listen(5)
    while True:
        # Принять запрос на соединение
        client, addr = server.accept()
        # принимает сообщение клиента
        presence = get_message(client)
        print(presence)
        # формирует ответ
        response = presence_response(presence)
        # отправляет ответ клиенту
        send_message(client, response)
        client.close()
