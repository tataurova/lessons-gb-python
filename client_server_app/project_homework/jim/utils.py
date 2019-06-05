import json

ENCODING = 'utf-8'


def dict_to_bytes(message_dict):
    """
    Преобразование словаря в байты
    :param message_dict: словарь
    :return: bytes
    """
    if isinstance(message_dict, dict):
        jmessage = json.dumps(message_dict)
        bmessage = jmessage.encode(ENCODING)
        return bmessage
    else:
        raise TypeError


def bytes_to_dict(message_bytes):
    """
    Получение словаря из байтов
    :param message_bytes: сообщение в виде байтов
    :return: словарь сообщения
    """

    if isinstance(message_bytes, bytes):
        jmessage = message_bytes.decode(ENCODING)
        message = json.loads(jmessage)
        if isinstance(message, dict):
            return message
        else:
            raise TypeError
    else:
        raise TypeError


def send_message(sock, message):
    """
    Отправка сообщения
    :param sock: сокет
    :param message: словарь сообщения
    :return: None
    """
    bprescence = dict_to_bytes(message)
    sock.send(bprescence)


def get_message(sock):
    """
    Получение сообщения
    :param sock:
    :return: словарь ответа
    """
    bresponse = sock.recv(1024)
    response = bytes_to_dict(bresponse)
    return response
