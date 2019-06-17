import json
from log.server_log_config import *

logger = logging.getLogger('server')


def log(func):

    def decorated(*args, **kwargs):
        res = func(*args, **kwargs)
        logger.debug('function {} completed with result {}, with arguments: {}'.format(func.__name__, res, args, kwargs))
        return res

    return decorated

@log
def presence_response(presence_message):

    if 'action' in presence_message and \
        presence_message['action'] == 'presence' and \
        'time' in presence_message and isinstance(presence_message['time'], str):
        #'user' in presence_message

        return {'response': 200}
    else:
        return {'response': 900, 'error': 'Неваывфыв верный запрос'}

# 'message' in presence_message and \

@log
def dict_to_bytes(message_dict):
    if isinstance(message_dict, dict):
        jmessage = json.dumps(message_dict)
        bmessage = jmessage.encode('utf-8')
        return bmessage
    else:
        raise TypeError

@log
def bytes_to_dict(message_bytes):
    if isinstance(message_bytes, bytes):
        jmessage = message_bytes.decode('utf-8')
        message = json.loads(jmessage)
        if isinstance(message, dict):
            return message
        else:
            raise TypeError
    else:
        raise TypeError

@log
def send_message(sock, message):
    bprescence = dict_to_bytes(message)
    sock.send(bprescence)


@log
def get_message(sock):
    bresponse = sock.recv(1024)
    response = bytes_to_dict(bresponse)
    return response

@log
def translate_message(response):
    if not isinstance(response, dict):
        raise TypeError
    if 'response' not in response:
        response = 'MandatoryKeyError'
    return response



