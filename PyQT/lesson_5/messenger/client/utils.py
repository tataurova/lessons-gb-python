from .errors import IncorrectDataRecivedError, NonDictInputError
import json
import logging
import sys

sys.path.append('../')

from log.client_log_config import *
from log.decorators import Log


logger = logging.getLogger('client')
log = Log(logger)


# Утилита приёма и декодирования сообщения
# принимает байты, выдаёт словарь, если принято что-то другое, отдаёт ошибку значения


def get_message(client):
    encoded_response = client.recv(1024)
    logger.info(f'get_messsage {encoded_response}')
    if isinstance(encoded_response, bytes):
        json_response = encoded_response.decode('utf-8')
        response = json.loads(json_response)
        if isinstance(response, dict):
            return response
        else:
            raise IncorrectDataRecivedError
    else:
        raise IncorrectDataRecivedError


# Утилита кодирования и отправки сообщения
# принимает словарь и отправляет его

def send_message(sock, message):
    if not isinstance(message, dict):
        raise NonDictInputError
    js_message = json.dumps(message)
    encoded_message = js_message.encode('utf-8')
    sock.send(encoded_message)
